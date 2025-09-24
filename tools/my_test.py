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

  def _parse_input(self, tool_input, tool_call_id=None):
    if isinstance(tool_input, str):
      return {"expression": tool_input}
    return tool_input
  
  def _run(self, parameters: StringArgs, flow_state: dict = None) -> str:
    expression = parameters.get("expression")
    if not isinstance(expression, str):
      expression = str(expression)
    return "Here is your reversed string: " + expression[::-1]
  
  async def _arun(self, parameters, flow_state) -> str:
    return await super().arun(parameters, flow_state)
  
