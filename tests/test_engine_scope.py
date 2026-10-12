"""Single-engine scope: the SGLang unit and parser probe must not carry vLLM settings."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / "guest" / "systemd" / "ntrust-inference.service"
PROBE = ROOT / "image" / "check-engine.py"


class EngineScope(unittest.TestCase):
    def test_sglang_unit_and_probe_have_no_vllm_references(self):
        text = UNIT.read_text()
        probe = PROBE.read_text()
        self.assertIn("/var/lib/ntrust/model/config.json", text)
        self.assertNotIn("VLLM_", text)
        self.assertIn("SGLANG_", text)
        self.assertNotIn("vllm", probe.lower())
        self.assertIn("sglang", probe.lower())


if __name__ == "__main__":
    unittest.main()
