# Generated from D:/PhD/Projects/Framework/mldsl-language-server-master/mldslls/dslf_language_helpers/MLDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MLDSLParser import MLDSLParser
else:
    from MLDSLParser import MLDSLParser

# This class defines a complete generic visitor for a parse tree produced by MLDSLParser.

class MLDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MLDSLParser#program.
    def visitProgram(self, ctx:MLDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#statement.
    def visitStatement(self, ctx:MLDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#load.
    def visitLoad(self, ctx:MLDSLParser.LoadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#load_dataset.
    def visitLoad_dataset(self, ctx:MLDSLParser.Load_datasetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#load_model.
    def visitLoad_model(self, ctx:MLDSLParser.Load_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#save.
    def visitSave(self, ctx:MLDSLParser.SaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#save_dataset.
    def visitSave_dataset(self, ctx:MLDSLParser.Save_datasetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#save_model.
    def visitSave_model(self, ctx:MLDSLParser.Save_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#save_metrics.
    def visitSave_metrics(self, ctx:MLDSLParser.Save_metricsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#show.
    def visitShow(self, ctx:MLDSLParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#show_dataset.
    def visitShow_dataset(self, ctx:MLDSLParser.Show_datasetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#show_model.
    def visitShow_model(self, ctx:MLDSLParser.Show_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#show_metrics.
    def visitShow_metrics(self, ctx:MLDSLParser.Show_metricsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#dataset_details.
    def visitDataset_details(self, ctx:MLDSLParser.Dataset_detailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#model_details.
    def visitModel_details(self, ctx:MLDSLParser.Model_detailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#metrics_details.
    def visitMetrics_details(self, ctx:MLDSLParser.Metrics_detailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#set.
    def visitSet(self, ctx:MLDSLParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#preprocess.
    def visitPreprocess(self, ctx:MLDSLParser.PreprocessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#preprocess_method.
    def visitPreprocess_method(self, ctx:MLDSLParser.Preprocess_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#method_name.
    def visitMethod_name(self, ctx:MLDSLParser.Method_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#split.
    def visitSplit(self, ctx:MLDSLParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#split_method.
    def visitSplit_method(self, ctx:MLDSLParser.Split_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#split_method_name.
    def visitSplit_method_name(self, ctx:MLDSLParser.Split_method_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#train.
    def visitTrain(self, ctx:MLDSLParser.TrainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#model.
    def visitModel(self, ctx:MLDSLParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#validate.
    def visitValidate(self, ctx:MLDSLParser.ValidateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#validation_metrics.
    def visitValidation_metrics(self, ctx:MLDSLParser.Validation_metricsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#evaluate.
    def visitEvaluate(self, ctx:MLDSLParser.EvaluateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#evalutaion_metrics.
    def visitEvalutaion_metrics(self, ctx:MLDSLParser.Evalutaion_metricsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#tune.
    def visitTune(self, ctx:MLDSLParser.TuneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#hyperparameters.
    def visitHyperparameters(self, ctx:MLDSLParser.HyperparametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#hyperparameter.
    def visitHyperparameter(self, ctx:MLDSLParser.HyperparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#compare.
    def visitCompare(self, ctx:MLDSLParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#model_list.
    def visitModel_list(self, ctx:MLDSLParser.Model_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#predict.
    def visitPredict(self, ctx:MLDSLParser.PredictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#py_injection.
    def visitPy_injection(self, ctx:MLDSLParser.Py_injectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#python_code.
    def visitPython_code(self, ctx:MLDSLParser.Python_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#parameters.
    def visitParameters(self, ctx:MLDSLParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#parameter.
    def visitParameter(self, ctx:MLDSLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#value.
    def visitValue(self, ctx:MLDSLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#range.
    def visitRange(self, ctx:MLDSLParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#list.
    def visitList(self, ctx:MLDSLParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#list_element.
    def visitList_element(self, ctx:MLDSLParser.List_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#number.
    def visitNumber(self, ctx:MLDSLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#dataset_name.
    def visitDataset_name(self, ctx:MLDSLParser.Dataset_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#model_name.
    def visitModel_name(self, ctx:MLDSLParser.Model_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#file_path.
    def visitFile_path(self, ctx:MLDSLParser.File_pathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#sql_config.
    def visitSql_config(self, ctx:MLDSLParser.Sql_configContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#url.
    def visitUrl(self, ctx:MLDSLParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#detail.
    def visitDetail(self, ctx:MLDSLParser.DetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#var_id.
    def visitVar_id(self, ctx:MLDSLParser.Var_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#columns.
    def visitColumns(self, ctx:MLDSLParser.ColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#column.
    def visitColumn(self, ctx:MLDSLParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#record.
    def visitRecord(self, ctx:MLDSLParser.RecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#string.
    def visitString(self, ctx:MLDSLParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#metric.
    def visitMetric(self, ctx:MLDSLParser.MetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#id.
    def visitId(self, ctx:MLDSLParser.IdContext):
        return self.visitChildren(ctx)



del MLDSLParser