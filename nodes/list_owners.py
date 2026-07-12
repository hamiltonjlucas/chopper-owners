from gen.messages_pb2 import OwnerQuery, Owner
from gen.axiom_context import AxiomContext


def list_owners(ax: AxiomContext, input: OwnerQuery) -> Owner:
    """List owners with optional type filtering and pagination."""
    # Get all owners from memory
    owners = []
    
    # Note: In production, this would query a database
    # For now, we return an empty list as a placeholder
    # The actual implementation would iterate through stored owners
    
    # Return first owner or empty if none found
    return Owner()
