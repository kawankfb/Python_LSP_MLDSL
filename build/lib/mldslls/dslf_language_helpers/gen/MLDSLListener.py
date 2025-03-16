# Generated from D:/PhD/Projects/Framework/mldsl-language-server-master/mldslls/dslf_language_helpers/MLDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MLDSLParser import MLDSLParser
else:
    from MLDSLParser import MLDSLParser

# This class defines a complete listener for a parse tree produced by MLDSLParser.
class MLDSLListener(ParseTreeListener):

    # Enter a parse tree produced by MLDSLParser#program.
    def enterProgram(self, ctx:MLDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLDSLParser#program.
    def exitProgram(self, ctx:MLDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLDSLParser#statement.
    def enterStatement(self, ctx:MLDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by MLDSLParser#statement.
    def exitStatement(self, ctx:MLDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by MLDSLParser#load.
    def enterLoad(self, ctx:MLDSLParser.LoadContext):
        pass

    # Exit a parse tree produced by MLDSLParser#load.
    def exitLoad(self, ctx:MLDSLParser.LoadContext):
        pass


    # Enter a parse tree produced by MLDSLParser#load_dataset.
    def enterLoad_dataset(self, ctx:MLDSLParser.Load_datasetContext):
        pass

    # Exit a parse tree produced by MLDSLParser#load_dataset.
    def exitLoad_dataset(self, ctx:MLDSLParser.Load_datasetContext):
        pass


    # Enter a parse tree produced by MLDSLParser#load_model.
    def enterLoad_model(self, ctx:MLDSLParser.Load_modelContext):
        pass

    # Exit a parse tree produced by MLDSLParser#load_model.
    def exitLoad_model(self, ctx:MLDSLParser.Load_modelContext):
        pass


    # Enter a parse tree produced by MLDSLParser#save.
    def enterSave(self, ctx:MLDSLParser.SaveContext):
        pass

    # Exit a parse tree produced by MLDSLParser#save.
    def exitSave(self, ctx:MLDSLParser.SaveContext):
        pass


    # Enter a parse tree produced by MLDSLParser#save_dataset.
    def enterSave_dataset(self, ctx:MLDSLParser.Save_datasetContext):
        pass

    # Exit a parse tree produced by MLDSLParser#save_dataset.
    def exitSave_dataset(self, ctx:MLDSLParser.Save_datasetContext):
        pass


    # Enter a parse tree produced by MLDSLParser#save_model.
    def enterSave_model(self, ctx:MLDSLParser.Save_modelContext):
        pass

    # Exit a parse tree produced by MLDSLParser#save_model.
    def exitSave_model(self, ctx:MLDSLParser.Save_modelContext):
        pass


    # Enter a parse tree produced by MLDSLParser#save_metrics.
    def enterSave_metrics(self, ctx:MLDSLParser.Save_metricsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#save_metrics.
    def exitSave_metrics(self, ctx:MLDSLParser.Save_metricsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#show.
    def enterShow(self, ctx:MLDSLParser.ShowContext):
        pass

    # Exit a parse tree produced by MLDSLParser#show.
    def exitShow(self, ctx:MLDSLParser.ShowContext):
        pass


    # Enter a parse tree produced by MLDSLParser#show_dataset.
    def enterShow_dataset(self, ctx:MLDSLParser.Show_datasetContext):
        pass

    # Exit a parse tree produced by MLDSLParser#show_dataset.
    def exitShow_dataset(self, ctx:MLDSLParser.Show_datasetContext):
        pass


    # Enter a parse tree produced by MLDSLParser#show_model.
    def enterShow_model(self, ctx:MLDSLParser.Show_modelContext):
        pass

    # Exit a parse tree produced by MLDSLParser#show_model.
    def exitShow_model(self, ctx:MLDSLParser.Show_modelContext):
        pass


    # Enter a parse tree produced by MLDSLParser#show_metrics.
    def enterShow_metrics(self, ctx:MLDSLParser.Show_metricsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#show_metrics.
    def exitShow_metrics(self, ctx:MLDSLParser.Show_metricsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#dataset_details.
    def enterDataset_details(self, ctx:MLDSLParser.Dataset_detailsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#dataset_details.
    def exitDataset_details(self, ctx:MLDSLParser.Dataset_detailsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#model_details.
    def enterModel_details(self, ctx:MLDSLParser.Model_detailsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#model_details.
    def exitModel_details(self, ctx:MLDSLParser.Model_detailsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#metrics_details.
    def enterMetrics_details(self, ctx:MLDSLParser.Metrics_detailsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#metrics_details.
    def exitMetrics_details(self, ctx:MLDSLParser.Metrics_detailsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#set.
    def enterSet(self, ctx:MLDSLParser.SetContext):
        pass

    # Exit a parse tree produced by MLDSLParser#set.
    def exitSet(self, ctx:MLDSLParser.SetContext):
        pass


    # Enter a parse tree produced by MLDSLParser#preprocess.
    def enterPreprocess(self, ctx:MLDSLParser.PreprocessContext):
        pass

    # Exit a parse tree produced by MLDSLParser#preprocess.
    def exitPreprocess(self, ctx:MLDSLParser.PreprocessContext):
        pass


    # Enter a parse tree produced by MLDSLParser#preprocess_method.
    def enterPreprocess_method(self, ctx:MLDSLParser.Preprocess_methodContext):
        pass

    # Exit a parse tree produced by MLDSLParser#preprocess_method.
    def exitPreprocess_method(self, ctx:MLDSLParser.Preprocess_methodContext):
        pass


    # Enter a parse tree produced by MLDSLParser#method_name.
    def enterMethod_name(self, ctx:MLDSLParser.Method_nameContext):
        pass

    # Exit a parse tree produced by MLDSLParser#method_name.
    def exitMethod_name(self, ctx:MLDSLParser.Method_nameContext):
        pass


    # Enter a parse tree produced by MLDSLParser#split.
    def enterSplit(self, ctx:MLDSLParser.SplitContext):
        pass

    # Exit a parse tree produced by MLDSLParser#split.
    def exitSplit(self, ctx:MLDSLParser.SplitContext):
        pass


    # Enter a parse tree produced by MLDSLParser#split_method.
    def enterSplit_method(self, ctx:MLDSLParser.Split_methodContext):
        pass

    # Exit a parse tree produced by MLDSLParser#split_method.
    def exitSplit_method(self, ctx:MLDSLParser.Split_methodContext):
        pass


    # Enter a parse tree produced by MLDSLParser#split_method_name.
    def enterSplit_method_name(self, ctx:MLDSLParser.Split_method_nameContext):
        pass

    # Exit a parse tree produced by MLDSLParser#split_method_name.
    def exitSplit_method_name(self, ctx:MLDSLParser.Split_method_nameContext):
        pass


    # Enter a parse tree produced by MLDSLParser#train.
    def enterTrain(self, ctx:MLDSLParser.TrainContext):
        pass

    # Exit a parse tree produced by MLDSLParser#train.
    def exitTrain(self, ctx:MLDSLParser.TrainContext):
        pass


    # Enter a parse tree produced by MLDSLParser#model.
    def enterModel(self, ctx:MLDSLParser.ModelContext):
        pass

    # Exit a parse tree produced by MLDSLParser#model.
    def exitModel(self, ctx:MLDSLParser.ModelContext):
        pass


    # Enter a parse tree produced by MLDSLParser#validate.
    def enterValidate(self, ctx:MLDSLParser.ValidateContext):
        pass

    # Exit a parse tree produced by MLDSLParser#validate.
    def exitValidate(self, ctx:MLDSLParser.ValidateContext):
        pass


    # Enter a parse tree produced by MLDSLParser#validation_metrics.
    def enterValidation_metrics(self, ctx:MLDSLParser.Validation_metricsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#validation_metrics.
    def exitValidation_metrics(self, ctx:MLDSLParser.Validation_metricsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#evaluate.
    def enterEvaluate(self, ctx:MLDSLParser.EvaluateContext):
        pass

    # Exit a parse tree produced by MLDSLParser#evaluate.
    def exitEvaluate(self, ctx:MLDSLParser.EvaluateContext):
        pass


    # Enter a parse tree produced by MLDSLParser#evalutaion_metrics.
    def enterEvalutaion_metrics(self, ctx:MLDSLParser.Evalutaion_metricsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#evalutaion_metrics.
    def exitEvalutaion_metrics(self, ctx:MLDSLParser.Evalutaion_metricsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#tune.
    def enterTune(self, ctx:MLDSLParser.TuneContext):
        pass

    # Exit a parse tree produced by MLDSLParser#tune.
    def exitTune(self, ctx:MLDSLParser.TuneContext):
        pass


    # Enter a parse tree produced by MLDSLParser#hyperparameters.
    def enterHyperparameters(self, ctx:MLDSLParser.HyperparametersContext):
        pass

    # Exit a parse tree produced by MLDSLParser#hyperparameters.
    def exitHyperparameters(self, ctx:MLDSLParser.HyperparametersContext):
        pass


    # Enter a parse tree produced by MLDSLParser#hyperparameter.
    def enterHyperparameter(self, ctx:MLDSLParser.HyperparameterContext):
        pass

    # Exit a parse tree produced by MLDSLParser#hyperparameter.
    def exitHyperparameter(self, ctx:MLDSLParser.HyperparameterContext):
        pass


    # Enter a parse tree produced by MLDSLParser#compare.
    def enterCompare(self, ctx:MLDSLParser.CompareContext):
        pass

    # Exit a parse tree produced by MLDSLParser#compare.
    def exitCompare(self, ctx:MLDSLParser.CompareContext):
        pass


    # Enter a parse tree produced by MLDSLParser#model_list.
    def enterModel_list(self, ctx:MLDSLParser.Model_listContext):
        pass

    # Exit a parse tree produced by MLDSLParser#model_list.
    def exitModel_list(self, ctx:MLDSLParser.Model_listContext):
        pass


    # Enter a parse tree produced by MLDSLParser#predict.
    def enterPredict(self, ctx:MLDSLParser.PredictContext):
        pass

    # Exit a parse tree produced by MLDSLParser#predict.
    def exitPredict(self, ctx:MLDSLParser.PredictContext):
        pass


    # Enter a parse tree produced by MLDSLParser#py_injection.
    def enterPy_injection(self, ctx:MLDSLParser.Py_injectionContext):
        pass

    # Exit a parse tree produced by MLDSLParser#py_injection.
    def exitPy_injection(self, ctx:MLDSLParser.Py_injectionContext):
        pass


    # Enter a parse tree produced by MLDSLParser#python_code.
    def enterPython_code(self, ctx:MLDSLParser.Python_codeContext):
        pass

    # Exit a parse tree produced by MLDSLParser#python_code.
    def exitPython_code(self, ctx:MLDSLParser.Python_codeContext):
        pass


    # Enter a parse tree produced by MLDSLParser#parameters.
    def enterParameters(self, ctx:MLDSLParser.ParametersContext):
        pass

    # Exit a parse tree produced by MLDSLParser#parameters.
    def exitParameters(self, ctx:MLDSLParser.ParametersContext):
        pass


    # Enter a parse tree produced by MLDSLParser#parameter.
    def enterParameter(self, ctx:MLDSLParser.ParameterContext):
        pass

    # Exit a parse tree produced by MLDSLParser#parameter.
    def exitParameter(self, ctx:MLDSLParser.ParameterContext):
        pass


    # Enter a parse tree produced by MLDSLParser#value.
    def enterValue(self, ctx:MLDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by MLDSLParser#value.
    def exitValue(self, ctx:MLDSLParser.ValueContext):
        pass


    # Enter a parse tree produced by MLDSLParser#range.
    def enterRange(self, ctx:MLDSLParser.RangeContext):
        pass

    # Exit a parse tree produced by MLDSLParser#range.
    def exitRange(self, ctx:MLDSLParser.RangeContext):
        pass


    # Enter a parse tree produced by MLDSLParser#list.
    def enterList(self, ctx:MLDSLParser.ListContext):
        pass

    # Exit a parse tree produced by MLDSLParser#list.
    def exitList(self, ctx:MLDSLParser.ListContext):
        pass


    # Enter a parse tree produced by MLDSLParser#list_element.
    def enterList_element(self, ctx:MLDSLParser.List_elementContext):
        pass

    # Exit a parse tree produced by MLDSLParser#list_element.
    def exitList_element(self, ctx:MLDSLParser.List_elementContext):
        pass


    # Enter a parse tree produced by MLDSLParser#number.
    def enterNumber(self, ctx:MLDSLParser.NumberContext):
        pass

    # Exit a parse tree produced by MLDSLParser#number.
    def exitNumber(self, ctx:MLDSLParser.NumberContext):
        pass


    # Enter a parse tree produced by MLDSLParser#dataset_name.
    def enterDataset_name(self, ctx:MLDSLParser.Dataset_nameContext):
        pass

    # Exit a parse tree produced by MLDSLParser#dataset_name.
    def exitDataset_name(self, ctx:MLDSLParser.Dataset_nameContext):
        pass


    # Enter a parse tree produced by MLDSLParser#model_name.
    def enterModel_name(self, ctx:MLDSLParser.Model_nameContext):
        pass

    # Exit a parse tree produced by MLDSLParser#model_name.
    def exitModel_name(self, ctx:MLDSLParser.Model_nameContext):
        pass


    # Enter a parse tree produced by MLDSLParser#file_path.
    def enterFile_path(self, ctx:MLDSLParser.File_pathContext):
        pass

    # Exit a parse tree produced by MLDSLParser#file_path.
    def exitFile_path(self, ctx:MLDSLParser.File_pathContext):
        pass


    # Enter a parse tree produced by MLDSLParser#sql_config.
    def enterSql_config(self, ctx:MLDSLParser.Sql_configContext):
        pass

    # Exit a parse tree produced by MLDSLParser#sql_config.
    def exitSql_config(self, ctx:MLDSLParser.Sql_configContext):
        pass


    # Enter a parse tree produced by MLDSLParser#url.
    def enterUrl(self, ctx:MLDSLParser.UrlContext):
        pass

    # Exit a parse tree produced by MLDSLParser#url.
    def exitUrl(self, ctx:MLDSLParser.UrlContext):
        pass


    # Enter a parse tree produced by MLDSLParser#detail.
    def enterDetail(self, ctx:MLDSLParser.DetailContext):
        pass

    # Exit a parse tree produced by MLDSLParser#detail.
    def exitDetail(self, ctx:MLDSLParser.DetailContext):
        pass


    # Enter a parse tree produced by MLDSLParser#var_id.
    def enterVar_id(self, ctx:MLDSLParser.Var_idContext):
        pass

    # Exit a parse tree produced by MLDSLParser#var_id.
    def exitVar_id(self, ctx:MLDSLParser.Var_idContext):
        pass


    # Enter a parse tree produced by MLDSLParser#columns.
    def enterColumns(self, ctx:MLDSLParser.ColumnsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#columns.
    def exitColumns(self, ctx:MLDSLParser.ColumnsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#column.
    def enterColumn(self, ctx:MLDSLParser.ColumnContext):
        pass

    # Exit a parse tree produced by MLDSLParser#column.
    def exitColumn(self, ctx:MLDSLParser.ColumnContext):
        pass


    # Enter a parse tree produced by MLDSLParser#record.
    def enterRecord(self, ctx:MLDSLParser.RecordContext):
        pass

    # Exit a parse tree produced by MLDSLParser#record.
    def exitRecord(self, ctx:MLDSLParser.RecordContext):
        pass


    # Enter a parse tree produced by MLDSLParser#string.
    def enterString(self, ctx:MLDSLParser.StringContext):
        pass

    # Exit a parse tree produced by MLDSLParser#string.
    def exitString(self, ctx:MLDSLParser.StringContext):
        pass


    # Enter a parse tree produced by MLDSLParser#metric.
    def enterMetric(self, ctx:MLDSLParser.MetricContext):
        pass

    # Exit a parse tree produced by MLDSLParser#metric.
    def exitMetric(self, ctx:MLDSLParser.MetricContext):
        pass


    # Enter a parse tree produced by MLDSLParser#id.
    def enterId(self, ctx:MLDSLParser.IdContext):
        pass

    # Exit a parse tree produced by MLDSLParser#id.
    def exitId(self, ctx:MLDSLParser.IdContext):
        pass



del MLDSLParser