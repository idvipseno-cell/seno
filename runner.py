import asyncio
import logging
import subprocess
import sys
import os

logging.basicConfig(level=logging.INFO)

async def run_process(command, name):
    logging.info(f"🚀 Starting {name}...")
    process = await asyncio.create_subprocess_exec(
        sys.executable, *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    async def log_output(stream, prefix):
        while True:
            line = await stream.readline()
            if not line:
                break
            logging.info(f"[{prefix}] {line.decode().strip()}")

    await asyncio.gather(
        log_output(process.stdout, name),
        log_output(process.stderr, name)
    )
    
    return_code = await process.wait()
    logging.error(f"❌ {name} exited with code {return_code}")

async def main():
    # التأكد من وجود قاعدة البيانات
    if not os.path.exists("database"):
        os.makedirs("database")
        
    tasks = [
        run_process(["bot_main/main.py"], "MAIN_BOT"),
        run_process(["bot_secondary/multi_worker.py"], "REACTION_SYSTEM")
    ]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Stopping all services...")
