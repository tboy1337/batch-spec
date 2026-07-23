# Generated from C:/Users/Laptop/Documents/Git/batch-spec/grammar/BatchParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BatchParser import BatchParser
else:
    from BatchParser import BatchParser

# This class defines a complete generic visitor for a parse tree produced by BatchParser.

class BatchParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BatchParser#script.
    def visitScript(self, ctx:BatchParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#line.
    def visitLine(self, ctx:BatchParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#label.
    def visitLabel(self, ctx:BatchParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#commandLine.
    def visitCommandLine(self, ctx:BatchParser.CommandLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#statement.
    def visitStatement(self, ctx:BatchParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#exitStmt.
    def visitExitStmt(self, ctx:BatchParser.ExitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#exitTail.
    def visitExitTail(self, ctx:BatchParser.ExitTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#groupStmt.
    def visitGroupStmt(self, ctx:BatchParser.GroupStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#shiftStmt.
    def visitShiftStmt(self, ctx:BatchParser.ShiftStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifStmt.
    def visitIfStmt(self, ctx:BatchParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifIOpt.
    def visitIfIOpt(self, ctx:BatchParser.IfIOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifBody.
    def visitIfBody(self, ctx:BatchParser.IfBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#elseClause.
    def visitElseClause(self, ctx:BatchParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifErrorlevelStmt.
    def visitIfErrorlevelStmt(self, ctx:BatchParser.IfErrorlevelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifCmdextversionStmt.
    def visitIfCmdextversionStmt(self, ctx:BatchParser.IfCmdextversionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifExistOperand.
    def visitIfExistOperand(self, ctx:BatchParser.IfExistOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifDefinedOperand.
    def visitIfDefinedOperand(self, ctx:BatchParser.IfDefinedOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifPredicate.
    def visitIfPredicate(self, ctx:BatchParser.IfPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#comparison.
    def visitComparison(self, ctx:BatchParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#compareOp.
    def visitCompareOp(self, ctx:BatchParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#compareOperand.
    def visitCompareOperand(self, ctx:BatchParser.CompareOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forStmt.
    def visitForStmt(self, ctx:BatchParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forPath.
    def visitForPath(self, ctx:BatchParser.ForPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forSlashMod.
    def visitForSlashMod(self, ctx:BatchParser.ForSlashModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forFOptions.
    def visitForFOptions(self, ctx:BatchParser.ForFOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forFOptionAnchor.
    def visitForFOptionAnchor(self, ctx:BatchParser.ForFOptionAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forFOptionExtra.
    def visitForFOptionExtra(self, ctx:BatchParser.ForFOptionExtraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forBody.
    def visitForBody(self, ctx:BatchParser.ForBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forList.
    def visitForList(self, ctx:BatchParser.ForListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forListItem.
    def visitForListItem(self, ctx:BatchParser.ForListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#callStmt.
    def visitCallStmt(self, ctx:BatchParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#callTarget.
    def visitCallTarget(self, ctx:BatchParser.CallTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#gotoStmt.
    def visitGotoStmt(self, ctx:BatchParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setStmt.
    def visitSetStmt(self, ctx:BatchParser.SetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setMode.
    def visitSetMode(self, ctx:BatchParser.SetModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setAssign.
    def visitSetAssign(self, ctx:BatchParser.SetAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setlocalStmt.
    def visitSetlocalStmt(self, ctx:BatchParser.SetlocalStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setlocalRest.
    def visitSetlocalRest(self, ctx:BatchParser.SetlocalRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#endlocalStmt.
    def visitEndlocalStmt(self, ctx:BatchParser.EndlocalStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setTarget.
    def visitSetTarget(self, ctx:BatchParser.SetTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setRest.
    def visitSetRest(self, ctx:BatchParser.SetRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#genericCmd.
    def visitGenericCmd(self, ctx:BatchParser.GenericCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#commandTail.
    def visitCommandTail(self, ctx:BatchParser.CommandTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#argWord.
    def visitArgWord(self, ctx:BatchParser.ArgWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#token.
    def visitToken(self, ctx:BatchParser.TokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#block.
    def visitBlock(self, ctx:BatchParser.BlockContext):
        return self.visitChildren(ctx)



del BatchParser