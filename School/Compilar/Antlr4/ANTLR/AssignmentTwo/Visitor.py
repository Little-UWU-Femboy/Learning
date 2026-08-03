from logoVisitor import logoVisitor


class Visitor(logoVisitor):
    def __init__(self, engine):
        self.engine = engine
        self.memory = {}

    def visitFd(self, ctx):
        self.engine.move(self.visit(ctx.expr()))
        return None

    def visitBk(self, ctx):
        self.engine.move(-self.visit(ctx.expr()))
        return None

    def visitRt(self, ctx):
        self.engine.rotate(self.visit(ctx.expr()))
        return None

    def visitLt(self, ctx):
        self.engine.rotate(-self.visit(ctx.expr()))
        return None

    def visitPu(self, ctx):
        self.engine.penUp()
        return None

    def visitPd(self, ctx):
        self.engine.penDown()
        return None

    def visitHm(self, ctx):
        self.engine.home()
        return None

    def visitSc(self, ctx):
        self.engine.setColor(self.visit(ctx.expr()))
        return None

    def visitWidth(self, ctx):
        self.engine.setWidth(self.visit(ctx.expr()))
        return None

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return None

    def visitRepeat(self, ctx):
        times = int(self.visit(ctx.expr()))
        for _ in range(times):
            self.visit(ctx.stmts())
        return None

    def visitIfZero(self, ctx):
        condition = self.visit(ctx.expr())
        if condition == 0:
            self.visit(ctx.stmts(0))
        else:
            self.visit(ctx.stmts(1))
        return None

    def visitStmts(self, ctx):
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    def visitNegation(self, ctx):
        return -self.visit(ctx.expr())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == "*":
            return left * right
        if op == "/":
            return left / right
        if op == "%":
            return left % right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == "+":
            return left + right
        if op == "-":
            return left - right

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        return self.memory.get(var_name, 0.0)

    def visitIntExpr(self, ctx):
        return float(ctx.INT().getText())
