# TESTS — delete this block when done ────────────────────────────────────────
# Tests are required to publish this package. The publish pipeline runs your
# tests as a quality gate — a package will not be published if tests fail or
# do not meet the minimum requirements.
#
# Requirements checked before publishing:
#   - At least one test per node
#   - All tests must pass
#   - Output fields must be meaningfully asserted — not just type-checked
#
# The generated test below is a starting point. Replace the TODO comment with
# real assertions that verify your node returns correct data for known inputs.
# Think: given a specific input, what should the output fields contain?
#
# Run your tests locally at any time:
#   axiom test
from gen.messages_pb2 import OwnerCreate, Owner
from nodes.create_owner import create_owner


class _TestContext:
    """Minimal AxiomContext implementation for unit tests.

    Override secrets_map with a dict to supply specific secrets your node
    requires, e.g. _TestContext(secrets_map={"OPENAI_KEY": "sk-test"}).
    """

    class _Logger:
        def debug(self, msg: str, **attrs) -> None: pass
        def info(self, msg: str, **attrs) -> None: pass
        def warn(self, msg: str, **attrs) -> None: pass
        def error(self, msg: str, **attrs) -> None: pass

    class _Secrets:
        def __init__(self, m: dict) -> None:
            self._m = m or {}
        def get(self, name: str):
            v = self._m.get(name)
            return (v, True) if v is not None else ("", False)

    class _SessionHistory:
        async def last(self, n: int) -> list: return []
        async def append(self, *, role: str, content: str) -> None: pass

    class _SessionMemory:
        def __init__(self) -> None:
            self.history = _TestContext._SessionHistory()
        async def search(self, query: str, limit: int = 5) -> list: return []
        async def write(self, content: str, importance: float = 0.5) -> str: return ""
        async def end(self) -> None: pass

    class _AgentMemory:
        def session(self, session_id: str): return _TestContext._SessionMemory()
        async def search(self, query: str, limit: int = 5) -> list: return []
        async def write(self, content: str, importance: float = 0.5) -> str: return ""

    class _Agent:
        def __init__(self) -> None:
            self.memory = _TestContext._AgentMemory()

    def __init__(self, secrets_map: dict | None = None) -> None:
        self.log = self._Logger()
        self.secrets = self._Secrets(secrets_map or {})
        self.agent = self._Agent()
        self.execution_id = "test-execution-id"
        self.flow_id = "test-flow-id"
        self.tenant_id = "test-tenant-id"


def test_create_owner():
    ax = _TestContext()
    input_msg = OwnerCreate()
    result = create_owner(ax, input_msg)
    assert isinstance(result, Owner)
    # TODO: assert output fields — e.g. assert result.some_field == "expected"
