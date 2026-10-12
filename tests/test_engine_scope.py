"""Single-engine scope: the SGLang unit must not carry vLLM settings."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / "guest" / "systemd" / "ntrust-inference.service"


class EngineScope(unittest.TestCase):
    def test_sglang_unit_has_no_vllm_variables(self):
        text = UNIT.read_text()
        self.assertIn("/var/lib/ntrust/model/config.json", text) or self.assertIn("SGLANG", text)
        self.assertNotIn("VLLM_", text)
        self.assertIn("SGLANG_", text)


if __name__ == "__main__":
    unittest.main()
