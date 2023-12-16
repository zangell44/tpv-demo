from pydantic import Field

from prefect import flow, get_run_logger
from prefect.engine import pause_flow_run
from prefect.input import RunInput

@flow
async def input_flow():        
    # Local variables
    x = 1
    y = 2

    class DebuggerCommand(RunInput):
        command: str = Field(..., description="The debug to execute")

    logger = get_run_logger()

    while True:
        input_str = await pause_flow_run(wait_for_input=DebuggerCommand, timeout=99999)
        logger.info(f">>> {input_str.command}")
        if input_str.command == "q":
            break
        else:
            result = eval(input_str.command, globals(), locals())
            logger.info(result)


    logger.info(f"End of flow. X is {x}. Y is {y} ")

