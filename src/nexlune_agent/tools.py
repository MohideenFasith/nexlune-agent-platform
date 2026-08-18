import ast, operator
from collections.abc import Callable

class SafeCalculator:
    OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.USub:operator.neg}
    def evaluate(self, expression:str)->float:
        node=ast.parse(expression, mode="eval").body
        return float(self._eval(node))
    def _eval(self,node):
        if isinstance(node,ast.Constant) and isinstance(node.value,(int,float)): return node.value
        if isinstance(node,ast.BinOp) and type(node.op) in self.OPS: return self.OPS[type(node.op)](self._eval(node.left),self._eval(node.right))
        if isinstance(node,ast.UnaryOp) and type(node.op) in self.OPS: return self.OPS[type(node.op)](self._eval(node.operand))
        raise ValueError("unsupported expression")

class ToolRegistry:
    def __init__(self):
        calc=SafeCalculator()
        self._tools:dict[str,Callable[[str],str]]={
            "echo":lambda x:x.strip(),
            "calculator":lambda x:str(calc.evaluate(x)),
        }
    def execute(self,name:str,arg:str)->str:
        if name not in self._tools: raise KeyError(name)
        return self._tools[name](arg)
