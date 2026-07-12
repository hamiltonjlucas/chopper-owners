from gen.messages_pb2 import OwnerCreate, Owner
from gen.axiom_context import AxiomContext
from google.protobuf.timestamp_pb2 import Timestamp
import time


def create_owner(ax: AxiomContext, input: OwnerCreate) -> Owner:
    """Create a new owner identity (user or agent)."""
    now = Timestamp()
    now.FromDatetime(time.gmtime())
    
    owner = Owner(
        owner_id=input.owner_id,
        owner_type=input.owner_type,
        display_name=input.display_name,
        avatar_url=input.avatar_url,
        created_at=now
    )
    
    # Store in agent memory for persistence
    ax.agent.memory.set(f"owner:{input.owner_id}", owner.SerializeToString())
    
    return owner
