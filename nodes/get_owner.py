from gen.messages_pb2 import OwnerQuery, Owner
from gen.axiom_context import AxiomContext


def get_owner(ax: AxiomContext, input: OwnerQuery) -> Owner:
    """Retrieve an owner by ID and optional type filter."""
    owner_data = ax.agent.memory.get(f"owner:{input.owner_id}")
    
    if not owner_data:
        raise ValueError(f"Owner not found: {input.owner_id}")
    
    owner = Owner()
    owner.ParseFromString(owner_data)
    
    if input.owner_type and owner.owner_type != input.owner_type:
        raise ValueError(f"Owner type mismatch: expected {input.owner_type}, got {owner.owner_type}")
    
    return owner
