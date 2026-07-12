from gen.messages_pb2 import OwnerCreate, Owner
from gen.axiom_context import AxiomContext
from datetime import datetime, timezone


def create_owner(ax: AxiomContext, input: OwnerCreate) -> Owner:
    """Create a new owner identity (user or agent)."""
    now = datetime.now(timezone.utc).isoformat()
    
    return Owner(
        owner_id=input.owner_id,
        owner_type=input.owner_type,
        display_name=input.display_name,
        avatar_url=input.avatar_url,
        created_at=now
    )
