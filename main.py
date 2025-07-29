import asyncio
import logging
import sys

from carddavmerger import ComparisonMethod, load_address_book_merger

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


async def main(config_path: str) -> None:
    async with load_address_book_merger(config_path) as merger:
        await merger.do_merge(ComparisonMethod.CONTENT)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"File path provided: {file_path}")
    else:
        raise RuntimeError(
            "No file path provided. Please provide a file path as a command line argument."
        )

    asyncio.run(main(file_path))
