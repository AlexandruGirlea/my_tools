import ast

from agentos_common_extn.app.tools.tool_base import BaseTool

config = {
  "expression": {
    "type": "str",
    "description": "Reverse a string",
    "default": ""
  }
}

StringArgs = BaseTool.create_args_model("StringArgs", config)

@BaseTool.register_tool("ReverseStringTool")
class ReverseStringTool(BaseTool):
  type: str = "tool"
  name: str = "ReverseStringTool"
  description: str = "reverse a string"
  args_schema: StringArgs= {}
  
  def _run(self, parameters: StringArgs, flow_state: dict = None) -> str:
    expression = parameters.get("expression")
    if not isinstance(expression, str):
      expression = str(expression)
    return expression[::-1]
  
  async def _arun(self, parameters, flow_state) -> str:
    return await super().arun(parameters, flow_state)
  
