/*
 * Created on 2005-nov-18
 */
package se.vxu.msi.malteval;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.TreeSet;
import java.util.Vector;

import se.vxu.msi.malteval.MaltEvalConfig.RemoveSentences;
import se.vxu.msi.malteval.configdata.GenericEvaluationParameters;
import se.vxu.msi.malteval.configdata.GenericExperimentSetup;
import se.vxu.msi.malteval.configdata.ReadEvaluationSetup;
import se.vxu.msi.malteval.configdata.util.Evaluation;
import se.vxu.msi.malteval.configdata.util.Evaluator;
import se.vxu.msi.malteval.configdata.util.Feature;
import se.vxu.msi.malteval.corpus.MaltTreebank;
import se.vxu.msi.malteval.datareaders.ReadCoNLL;
import se.vxu.msi.malteval.datareaders.ReadMaltTab;
import se.vxu.msi.malteval.evaluator.MaltParserEvaluator;
import se.vxu.msi.malteval.exceptions.MaltEvalException;
import se.vxu.msi.malteval.selectionfile.SelectionFileComputation;
import se.vxu.msi.malteval.statistics.ComputeMcNemar;
import se.vxu.msi.malteval.treeviewer.MaltTreeViewerGui;
import se.vxu.msi.malteval.util.DataContainer;

public class MaltEvalConsole {
	// static public boolean useLog4j = true;

	private String posFile_, depFile_, evalPath_, selectionFile_;
	private String parserFileFormat_, gsFileFormat_;
	private String[] parserFiles_, gsFiles_;
	private boolean isUsingSTDOUT_;
	private boolean computeStatisticalSignificance_;

	private boolean visualizeFiles;
	private boolean eval07;
	private boolean shownArgumentsOnce;

	private ReadEvaluationSetup readEvaluationSetup;
	private PrintStream evalutationOutputWriter_;

	private String[] args_;

	public static void main(String[] args) {
		// useLog4j = false;
		MaltEvalConfig.init();
		if (args.length == 0) {
			welcome();
			System.out.println("\n\tUsage: [-e <evaluation file> (optional)] [arguments]\n");
			System.out.println("Required Arguments:\n" + "\t-s <file, files or directory with parser output (tab|xml|conll)>\n"
					+ "\t-g <gold-standard file, files or directory (tab|xml|conll)>");
			System.out.println("\nOptional Formatting Arguments:");
			MaltEvalConfig.printFormattingArgumentsHelpTexts();
			System.out.println("\nOther Arguments:");
			System.out
					.println("\t-v <0|1>: vizualize the parsed and/or gold-standard files with the tree viewer (default: 0)\n"
							+ "\t--deprels <dep file>: file with allowed dependency types\n"
							+ "\t--cpostags <cpos file>: file with allowed coarse grained postags\n\n"
							+ "\t--help = help for the evaluation file\n"
							+ "\t--examples = help for using the flags and evaluation file arguments");
			System.exit(0);
		} else if (args.length == 1 && args[0].equals(MaltEvalConfig.help)) {
			welcome();
			System.out.println();
			try {
				MaltParserEvaluator.initialize();
			} catch (MaltEvalException mee) {
				System.err.println("\nEvaluation aborted: " + mee.getMessage());
				if (MaltEvalConfig.DEBUG_MODE) {
					mee.printStackTrace();
				}
			}
			printOptions(MaltParserEvaluator.constructMaltParserEvaluator());
			System.exit(0);
		} else if (args.length == 1 && args[0].equals(MaltEvalConfig.examples)) {
			welcome();
			examples();
			System.exit(0);
		} else if (args.length > 1 && args[0].equals(MaltEvalConfig.EVAL_FILES) && args[1].equals("eval07.pl")) {
			String[][] argss = CoNLLEval.getEvalParameters(args);
			String[] eval07Descriptions = CoNLLEval.getDescriptions();
			int eval07DescriptionsIndex = 0;
			for (String[] oneArgs : argss) {
				try {
					System.out.println(eval07Descriptions[eval07DescriptionsIndex]);
					new MaltEvalConsole(oneArgs);
				} catch (Exception mee) {
					System.err.println("\nEvaluation aborted: " + mee.getMessage());
					if (MaltEvalConfig.DEBUG_MODE) {
						mee.printStackTrace();
					}
				}
				eval07DescriptionsIndex++;
			}
		} else {
			try {
				new MaltEvalConsole(args);
			} catch (Exception mee) {
				System.err.println("\nEvaluation aborted: " + mee.getMessage());
				if (MaltEvalConfig.DEBUG_MODE) {
					mee.printStackTrace();
				}
			}
		}
	}

	static private void welcome() {
		System.out.println("-----------------------------------------------------------------------------");
		System.out.println("-                              MaltEval 1.0                                 -");
		System.out.println("-----------------------------------------------------------------------------");
		System.out.println("-        MALT (Models and Algorithms for Language Technology) Group         -");
		System.out.println("- The School of Mathematics and Systems Engineering (MSI), Vaxjo University -");
		System.out.println("-----------------------------------------------------------------------------");
	}

	static private void examples() {
		System.out.println("java -jar MaltEval.jar -s parser.conll -g gold.conll\n"
				+ "\t--Metric \"LA\" --GroupBy Deprel:all|recall-10\n" + "\t--MinSentenceLength 1 --MaxSentenceLength 40\n"
				+ "\t--ExcludeDeprels \";Punc|Dummy\" --details 1\n" + "\t--header-info 1 --row-header 1 --tab 0\n"
				+ "\t--output result.out --pattern 0.0000 --stat 0\n" + "\t--confusion-matrix 0\n");
		System.out.println("This is equivalent to:");
		System.out.println("java -jar MaltEval.jar -e eval.xml -s parser.conll -g gold.conll");
		System.out.println("Using eval.xml:");
		System.out.println("<evaluation>\n" + "\t<parameter name=\"Metric\">\n"	+ "\t\t<value>LA</value>\n" + "\t</parameter>\n" + "\t<parameter name=\"GroupBy\">\n"
				+ "\t\t<value format=\"all|recall-10\">Deprel</value>\n" + "\t</parameter>\n" + "\t<parameter name=\"ExcludeDeprels\">\n"
				+ "\t\t<value></value>\n" + "\t\t<value>Punc|Dummy</value>\n" + "\t\t</parameter>\n"
				+ "\t\t<parameter name=\"MinSentenceLength\">\n" + "\t\t<value>1</value>\n" + "\t</parameter>\n"
				+ "\t\t<parameter name=\"MaxSentenceLength\">\n" + "\t\t<value>40</value>\n" + "\t</parameter>\n"
				+ "\t<formatting argument=\"details\" format=\"1\"/>\n" + "\t<formatting argument=\"header-info\" format=\"1\"/>\n"
				+ "\t<formatting argument=\"row-header\" format=\"1\"/>\n" + "\t<formatting argument=\"tab\" format=\"0\"/>\n"
				+ "\t<formatting argument=\"output\" format=\"result.out\"/>\n"
				+ "\t<formatting argument=\"pattern\" format=\"0.0000\"/>\n" + "\t<formatting argument=\"stat\" format=\"0\"/>\n"
				+ "\t<formatting argument=\"confusion-matrix\" format=\"0\"/>\n" + "</evaluation>\n");
	}

	static private void printOptions(Evaluator evaluator) {
		int j;
		Feature feature;
		Iterator<Feature> i = evaluator.getOptionFeatureIterator();
		System.out.println("Available Evaluation Options:");
		while (i.hasNext()) {
			feature = (Feature) i.next();
			System.out.println(feature.getName() + " (\"" + feature.getDefaultValue() + "\" is default):");
			if (feature.getName().equals(MaltEvalConfig.excludeCpostags) || feature.getName().equals(MaltEvalConfig.excludeDeprels)
					|| feature.getName().equals(MaltEvalConfig.excludeFeats) || feature.getName().equals(MaltEvalConfig.excludeLemma)
					|| feature.getName().equals(MaltEvalConfig.excludePdeprels) || feature.getName().equals(MaltEvalConfig.excludePostags)
					|| feature.getName().equals(MaltEvalConfig.excludeWordforms)) {
				System.out.println("\tTags seperated by \"|\", e.g.: <tag1>|<tag2>|...");
			} else if (feature.getName().equalsIgnoreCase("maxSentenceLength")) {
				System.out.println("\t0 = infinity");
			}
			for (j = 0; j < feature.getValues().length; j++) {
				System.out.println("\t" + feature.getValues()[j] + " ");
			}
			System.out.println();
		}
	}

	public MaltEvalConsole(String[] args) throws MaltEvalException, FileNotFoundException {
		int i;
		DataContainer[][] evaluationDataContainers;
		args_ = args;
		init();
		MaltParserEvaluator.initialize();
		if (eval07) {

		} else if (visualizeFiles) {
			try {
				new MaltTreeViewerGui(parserFiles_, (parserFiles_ != null ? getFileFormat(parserFiles_[0]) : null), gsFiles_,
						(gsFiles_ != null ? getFileFormat(gsFiles_[0]) : null));
			} catch (Exception e) {
				throw new MaltEvalException(e.getMessage(), this.getClass());
			}
		} else {
			validateInitialization();
			if (selectionFile_ == null) {
				evaluationDataContainers = compute();
				if (gsFiles_.length > 1) {
					for (i = 0; i < evaluationDataContainers.length; i++) {
						DataContainer crossvalidation = DataContainer.collectAggregationData(evaluationDataContainers[i]);
						crossvalidation.setRowHeadingsHeading("File number");
						openResultDataFile("cs_aggr", i, "Mean:\n", arrayToString(gsFiles_), arrayToString(parserFiles_), "res");
						printResultData(crossvalidation.toString());
						closeResultDataFile();
					}
				}
			} else {
				computeWithSelectionFile();
			}
		}
	}

	private void parseArguments(String[] args) throws MaltEvalException {
		int i = 0;
		String argument, value;
		HashSet<String> usedArguments = new HashSet<String>(), required = new HashSet<String>();
		required.add(MaltEvalConfig.SYSTEM_FILES);
		required.add(MaltEvalConfig.GOLD_FILES);
		if (args[i].equals(MaltEvalConfig.EVAL_FILES)) {
			i++;
			if (args[i].equals("eval07.pl")) {
				eval07 = true;
			} else {
				readEvaluationSetup.readFromFile(args[i]);
				evalPath_ = args[i];
			}
			i++;
		} else {
			readEvaluationSetup.setDefultEvaluation();
			evalPath_ = "./";
		}
		while (i < args.length && args[i].startsWith("-")) {
			if (args[i].length() < 2) {
				throw new MaltEvalException("Unable to parse argument number " + i + " (" + args[i] + ")", this.getClass());
			}
			argument = args[i];
			if (usedArguments.contains(argument)) {
				throw new MaltEvalException("The argument " + argument + " is specified twice", this.getClass());
			}
			usedArguments.add(argument);
			required.remove(argument);
			i++;
			if (i == args.length) {
				throw new MaltEvalException("Unable to find the argument value for the argument " + argument, this.getClass());
			}
			value = args[i];
			if (MaltEvalConfig.isFormattingArgument(argument)) {
				readEvaluationSetup.setFormattingValue(argument, value);
			} else if (MaltEvalConfig.isParameterArgument(argument)) {
				readEvaluationSetup.setParameterValue(argument, value);
			} else if (MaltEvalConfig.isExcludeType(argument)) {
				readEvaluationSetup.setParameterValue(argument, value);
			} else if (MaltEvalConfig.isExcludeUnicodePunctuation(argument)) {
				readEvaluationSetup.setParameterValue(argument, value);
			} else if (MaltEvalConfig.isIntervalType(argument)) {
				readEvaluationSetup.setParameterValue(argument, value);
			} else if (argument.equals(MaltEvalConfig.CHAR_SET_NAME)) {
				ReadMaltTab.setCharsetName(value);
				ReadCoNLL.setCharsetName(value);
			} else if (argument.equals(MaltEvalConfig.SELECTION_FILE)) {
				selectionFile_ = value;
			} else if (argument.equals(MaltEvalConfig.SYSTEM_FILES)) {
				Vector<String> systemFiles = new Vector<String>();
				while (i < args.length && !args[i].startsWith("-")) {
					systemFiles.add(args[i]);
					i++;
				}
				i--;
				if (systemFiles.size() > 1) {
					parserFiles_ = (String[]) systemFiles.toArray(new String[0]);
				} else {
					parserFiles_ = getFiles(value);
				}
			} else if (argument.equals(MaltEvalConfig.GOLD_FILES)) {
				Vector<String> gsFiles = new Vector<String>();
				while (i < args.length && !args[i].startsWith("-")) {
					gsFiles.add(args[i]);
					i++;
				}
				i--;
				if (gsFiles.size() > 1) {
					gsFiles_ = (String[]) gsFiles.toArray(new String[0]);
				} else {
					gsFiles_ = getFiles(value);
				}
			} else if (argument.equals(MaltEvalConfig.CPOSTAG_FILE)) {
				posFile_ = value;
			} else if (argument.equals(MaltEvalConfig.DEPREL_FILE)) {
				depFile_ = value;
			} else if (argument.equals(MaltEvalConfig.REMOVE_SENTENCES)) {
				for (MaltEvalConfig.RemoveSentences removeSentences : MaltEvalConfig.RemoveSentences.values()) {
					if (value.equals(removeSentences.toString())) {
						MaltEvalConfig.removeProjectiveTrees = removeSentences;
					}
				}
			} else if (MaltEvalConfig.isVizualizationFlag(argument)) {
				if (value.equals("0") || value.equals("1")) {
					visualizeFiles = value.equals("1");
				} else {
					throw new MaltEvalException("The flag " + MaltEvalConfig.VISUALIZATION + " can only have the value 0 or 1", this
							.getClass());
				}
			} else {
				throw new MaltEvalException("Expected some other argument. Found: " + argument, this.getClass());
			}
			i++;
		}
		if (!required.isEmpty() && !visualizeFiles) {
			throw new MaltEvalException("The required arguments " + required.toString() + " have not been specified", this.getClass());
		}
		if (i != args.length) {
			throw new MaltEvalException("Unable to parse all arguments. Stopped at argument number " + i, this.getClass());
		}
	}

	private void init() throws MaltEvalException {
		shownArgumentsOnce = false;
		eval07 = false;
		visualizeFiles = false;
		evalutationOutputWriter_ = null;
		posFile_ = null;
		depFile_ = null;
		selectionFile_ = null;
		readEvaluationSetup = new ReadEvaluationSetup(new GenericExperimentSetup());
		parseArguments(args_);
		isUsingSTDOUT_ = readEvaluationSetup.getOutputPath().equals(MaltEvalConfig.STDOUT);
		computeStatisticalSignificance_ = readEvaluationSetup.isComputeStatisticalSignificance();
	}

	private void validateInitialization() throws MaltEvalException {
		if (!readEvaluationSetup.getOutputPath().endsWith("/") && !readEvaluationSetup.getOutputPath().endsWith("\\")) {
			readEvaluationSetup.setOutputPath(readEvaluationSetup.getOutputPath() + String.valueOf(File.separator));
		}
		if (gsFiles_.length != 1 && gsFiles_.length != parserFiles_.length) {
			throw new MaltEvalException("Crossvalidation not possible. Nr of parser files: " + parserFiles_.length
					+ ", and nr of gold-standard files: " + gsFiles_.length, this.getClass());
		}
		if (gsFiles_.length == 1 && parserFiles_.length != 1 && MaltEvalConfig.MICRO_AVERAGE) {
			throw new MaltEvalException("Merging files for crossvalidation is not possible. Nr of parser files: " + parserFiles_.length
					+ ", and nr of gold-standard files: " + gsFiles_.length, this.getClass());
		}
	}
	
	private ArrayList<Integer> getSentencesToRemove(MaltTreebank data) {
		ArrayList<Integer> toRemove = new ArrayList<Integer>();
		if (MaltEvalConfig.removeProjectiveTrees != RemoveSentences.None) {
			for (int j = 0; j < data.getSentenceCount(); j++) {
				if (MaltEvalConfig.removeProjectiveTrees == RemoveSentences.Projective && data.getSentence(j).isProjective() || MaltEvalConfig.removeProjectiveTrees == RemoveSentences.NonProjective && !data.getSentence(j).isProjective()) {
					toRemove.add(0, j);
				}
			}
		}
		return toRemove;
	}
	
	private void removeSentences(MaltTreebank data, ArrayList<Integer> removeList) {
		for (Integer index : removeList) {
			data.removeSentene(index);
		}
	}

	private DataContainer[][] compute() throws MaltEvalException {
		int i, l;
		DataContainer[][] evaluationDataContainers, evaluationDataContainers2;
		MaltTreebank gsData = null, parserOutput = null;
		Evaluation evaluation;
		ArrayList<Integer> sentencesToRemove = new ArrayList<Integer>(); 

		GenericEvaluationParameters gep = readEvaluationSetup.getGenericEvaluationParameters();

		if (!(new File(readEvaluationSetup.getOutputPath())).isDirectory()) {
			(new File(readEvaluationSetup.getOutputPath())).delete();
		}
		if (gsFiles_.length == 1) {
			gsFileFormat_ = getFileFormat(gsFiles_[0]);
			gsData = new MaltTreebank(gsFiles_[0], gsFileFormat_, posFile_, depFile_, true, true, true);
			sentencesToRemove = getSentencesToRemove(gsData);
			removeSentences(gsData, sentencesToRemove);
			
		} else if (MaltEvalConfig.MICRO_AVERAGE) {
			gsData = mergeFiles(gsFiles_);
			sentencesToRemove = getSentencesToRemove(gsData);
			removeSentences(gsData, sentencesToRemove);
			gsFiles_ = new String[1];
			gsFiles_[0] = "concat_gs";

			parserOutput = mergeFiles(parserFiles_);
			removeSentences(parserOutput, sentencesToRemove);
			parserFiles_ = new String[1];
			parserFiles_[0] = "concat_parsed";
		}
		gep.createExperimentEngineInputDataArray();
		evaluationDataContainers = new DataContainer[gep.getTotalNumberOfCombinationsCount()][];
		evaluationDataContainers2 = new DataContainer[parserFiles_.length][];
		for (i = 0; i < evaluationDataContainers.length; i++) {
			evaluationDataContainers[i] = new DataContainer[parserFiles_.length];
		}
		for (i = 0; i < evaluationDataContainers2.length; i++) {
			evaluationDataContainers2[i] = new DataContainer[gep.getTotalNumberOfCombinationsCount()];
		}
		for (i = 0; i < parserFiles_.length; i++) {
			if (gsFiles_.length != 1 && !MaltEvalConfig.MICRO_AVERAGE) {
				gsFileFormat_ = getFileFormat(gsFiles_[i]);
				gsData = new MaltTreebank(gsFiles_[i], gsFileFormat_, posFile_, depFile_, true, true, true);
				sentencesToRemove = getSentencesToRemove(gsData);
				removeSentences(gsData, sentencesToRemove);
			}
			if (!MaltEvalConfig.MICRO_AVERAGE) {
				parserFileFormat_ = getFileFormat(parserFiles_[i]);
				parserOutput = new MaltTreebank(parserFiles_[i], parserFileFormat_, posFile_, depFile_, true, true, true);
				removeSentences(parserOutput, sentencesToRemove);
			}
			
			
			gsData.getPostags().addAll(parserOutput.getPostags());
			parserOutput.getPostags().addAll(gsData.getPostags());
			gsData.getDeprels().addAll(parserOutput.getDeprels());
			parserOutput.getDeprels().addAll(gsData.getDeprels());
			l = 0;
			do {
				evaluation = gep.getNextEvaluationParameters();
				printHeaderDataToFile(parserFiles_[i] + "." + l + ".", evaluation.toString(), (gsFiles_.length != 1 ? gsFiles_[i]
						: gsFiles_[0]), parserFiles_[i]);
				evaluationDataContainers[l][i] = (new MaltParserEvaluator(parserOutput, gsData)).evaluate(evaluation);
				evaluationDataContainers2[i][l] = evaluationDataContainers[l][i];
				l++;
			} while (gep.incToNextEvaluationParameters());

			boolean mergable = DataContainer.areMergable(evaluationDataContainers2[i]);
			if (MaltEvalConfig.MERGE_TABLES_VALUE && mergable) {
				DataContainer merged = DataContainer.merge(evaluationDataContainers2[i], gep);
				openResultDataFile(parserFiles_[i], -1, merged.getEvaluation().toString(), (gsFiles_.length != 1 ? gsFiles_[i]
						: gsFiles_[0]), parserFiles_[i], "res");
				printResultData(merged.toString());
				closeResultDataFile();
			}
			for (l = 0; l < evaluationDataContainers.length; l++) {
				try {
					if (!MaltEvalConfig.MERGE_TABLES_VALUE || !mergable || evaluationDataContainers[l][i].getConfusionTable() != null
							|| evaluationDataContainers[l][i].getConfusionMatrix() != null) {
						openResultDataFile(parserFiles_[i], l, evaluationDataContainers[l][i].getEvaluation().toString(),
								(gsFiles_.length != 1 ? gsFiles_[i] : gsFiles_[0]), parserFiles_[i], "res");
						if (!MaltEvalConfig.MERGE_TABLES_VALUE || !mergable) {
							printResultData(evaluationDataContainers[l][i].toString());
						}
						if (evaluationDataContainers[l][i].getConfusionTable() != null) {
							printResultData(evaluationDataContainers[l][i].getConfusionTable().toString() + "\n");

						}
						if (evaluationDataContainers[l][i].getConfusionMatrix() != null) {
							printResultData(evaluationDataContainers[l][i].getConfusionMatrix().toString() + "\n");
						}
						closeResultDataFile();
					}
				} catch (MaltEvalException e) {
					printResultData(e.getMessage());
					System.err.println(e.getMessage());
				}
			}
		}
		if (computeStatisticalSignificance_ && gsFiles_.length == 1 && parserFiles_.length > 1) {
			ComputeMcNemar computeMcNemar = new ComputeMcNemar(evaluationDataContainers, parserFiles_);
			openResultDataFile("mcnemar", -1, "McNemar's statistical significance test\n", gsFiles_[0], arrayToString(parserFiles_), "stat");
			for (String setting : computeMcNemar.getZValue().keySet()) {
				printResultData(setting.toString() + computeMcNemar.getZValue().get(setting).toString());
				printResultData(computeMcNemar.getOnePercent().get(setting).toString());
				printResultData(computeMcNemar.getFivePercent().get(setting).toString());
				printResultData("====================================================\n\n");
			}
			closeResultDataFile();
		}
		return evaluationDataContainers;
	}

	private void computeWithSelectionFile() throws MaltEvalException {
		MaltTreebank gsData = null, parserOutput;
		if (gsFiles_.length > 1 || parserFiles_.length > 1) {
			throw new MaltEvalException(
					"MaltEvalConsole currently only supports one gold-standards and one parsed file in selection file mode\n", this
							.getClass());
		}
		gsData = new MaltTreebank(gsFiles_[0], getFileFormat(gsFiles_[0]), posFile_, depFile_, true, true, true);
		parserOutput = new MaltTreebank(parserFiles_[0], getFileFormat(parserFiles_[0]), posFile_, depFile_, true, true, true);
		SelectionFileComputation selectionFileComputation = new SelectionFileComputation(gsData, parserOutput, selectionFile_);
		selectionFileComputation.compute();
	}

	private void printHeaderDataToFile(String fileName, String settings, String gsFile, String parsedFile) throws MaltEvalException {
		if (readEvaluationSetup.isPrintSettingsFile()) {
			try {
				BufferedWriter hbw = new BufferedWriter(new FileWriter(getOutputPath(fileName) + "hdr"));
				hbw.write("Gold:   " + gsFile + "\n");
				hbw.write("Parsed: " + parsedFile + "\n");
				hbw.write(settings);
				hbw.close();
			} catch (IOException ioe) {
				throw new MaltEvalException(ioe.getMessage(), this.getClass());
			}
		}
	}

	private void printResultData(String data) throws MaltEvalException {
		evalutationOutputWriter_.print(data);
	}

	private void openResultDataFile(String fileName, int evalNumber, String settings, String gsFile, String parsedFile, String fileExtention)
			throws MaltEvalException {
		try {
			boolean showArgs = false;
			if (isUsingSTDOUT_) {
				evalutationOutputWriter_ = System.out;
			} else if ((new File(readEvaluationSetup.getOutputPath())).isDirectory()) {
				evalutationOutputWriter_ = new PrintStream(getOutputPath(fileName) + "." + (evalNumber != -1 ? evalNumber + "." : "")
						+ "res", MaltEvalConfig.CHARACTER_SET_ENCODING);
				showArgs = true;
			} else {
				evalutationOutputWriter_ = new PrintStream(new FileOutputStream(readEvaluationSetup.getOutputPath(), true), false,
						MaltEvalConfig.CHARACTER_SET_ENCODING);
			}
			if (DataContainer.printHeader) { // !readEvaluationSetup.isPrintSettingsFile() &&
				if (!shownArgumentsOnce || showArgs) {
					evalutationOutputWriter_.print(getArgs());
					shownArgumentsOnce = true;
				}
				evalutationOutputWriter_.println("====================================================");
				evalutationOutputWriter_.println("Gold:   " + gsFile);
				evalutationOutputWriter_.println("Parsed: " + parsedFile);
				evalutationOutputWriter_.println("====================================================");
				evalutationOutputWriter_.println(settings);
				evalutationOutputWriter_.println("====================================================\n");
			}
		} catch (IOException ioe) {
			throw new MaltEvalException(ioe.getMessage(), this.getClass());
		}
	}

	private void closeResultDataFile() throws MaltEvalException {
		if (!isUsingSTDOUT_) {
			evalutationOutputWriter_.close();
		}
	}

	private String getOutputPath(String fileName) {
		int index;
		if (isUsingSTDOUT_) {
			return readEvaluationSetup.getOutputPath();
		} else {
			if ((index = evalPath_.lastIndexOf("/")) == -1) {
				index = evalPath_.lastIndexOf("\\");
			}
			if ((index = fileName.lastIndexOf("/")) == -1) {
				index = fileName.lastIndexOf("\\");
			}
			return readEvaluationSetup.getOutputPath() + (index != -1 ? fileName.substring(index + 1) : fileName);
		}
	}

	private String[] getFiles(String path) {
		int i;
		TreeSet<String> forSorting = new TreeSet<String>();
		if (!(new File(path)).isDirectory()) {
			forSorting.add(path);
		} else {
			String[] files = (new File(path)).list();
			for (i = 0; i < files.length; i++) {
				if (files[i].endsWith(MaltEvalConfig.MALT_XML_EXT) || files[i].endsWith(MaltEvalConfig.MALT_TAB_EXT)
						|| files[i].endsWith(MaltEvalConfig.CONLL_EXT)) {
					forSorting.add(path + files[i]);
				}
			}
		}
		return (String[]) forSorting.toArray(new String[0]);
	}

	private String getFileFormat(String path) {
		if (path.endsWith(MaltEvalConfig.MALT_XML_EXT)) {
			return MaltEvalConfig.MALT_XML;
		} else if (path.endsWith(MaltEvalConfig.MALT_TAB_EXT)) {
			return MaltEvalConfig.MALT_TAB;
		} else if (path.endsWith(MaltEvalConfig.CONLL_EXT)) {
			return MaltEvalConfig.CONLL;
		} else {
			return MaltEvalConfig.CONLL;
		}
	}

	private String arrayToString(Object[] array) {
		int i;
		StringBuffer sb = new StringBuffer();
		for (i = 0; i < array.length; i++) {
			sb.append(array[i]);
			if (i < array.length - 1) {
				sb.append(", ");
			}
		}
		return sb.toString();
	}

	private String getArgs() {
		StringBuilder sb = new StringBuilder();
		sb.append("Evaluation arguments: ");
		for (String arg : args_) {
			if (arg.contains(";") || arg.contains(" ") || arg.contains("\'") || arg.contains("\"")) {
				sb.append("\"" + arg + "\" ");
			} else {
				sb.append(arg + " ");
			}
		}
		sb.deleteCharAt(sb.length() - 1);
		sb.append("\n");
		return sb.toString();
	}

	private MaltTreebank mergeFiles(String[] files) throws MaltEvalException {
		int i;
		MaltTreebank mergedData, data;
		mergedData = new MaltTreebank(files[0], getFileFormat(files[0]), posFile_, depFile_, true, true, true);
		for (i = 1; i < files.length; i++) {
			data = new MaltTreebank(files[i], getFileFormat(files[i]), posFile_, depFile_, true, true, true);
			mergedData.addTreebank(data);
		}
		return mergedData;
	}
}
