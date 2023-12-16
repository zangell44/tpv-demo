from prefect import flow, get_run_logger
from prefect.engine import pause_flow_run

@flow
async def input_flow():        
    # Local variables
    x = 1
    y = 2

    logger = get_run_logger()

    while True:
        input_str = await pause_flow_run(wait_for_input=str, timeout=99999)
        logger.info(f">>> {input_str}")
        if input_str == "q":
            break
        else:
            result = eval(input_str)
            logger.info(result)


    logger.info(f"End of flow. X is {x}. Y is {y} ")

