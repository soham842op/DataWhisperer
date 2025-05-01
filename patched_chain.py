from langchain_experimental.sql import SQLDatabaseChain
import re

class PatchedSQLDatabaseChain(SQLDatabaseChain):
    def _call(self, inputs, run_manager=None):
        # Run as normal
        output = super()._call(inputs, run_manager=run_manager)

        # Clean stray newlines, double quotes, etc.
        if isinstance(output, str):
            output = output.strip().replace("\n", " ").replace('"', "'")
        elif isinstance(output, dict) and "result" in output:
            output["result"] = re.sub(r"[\n\r]+", " ", str(output["result"])).strip()

        return output
