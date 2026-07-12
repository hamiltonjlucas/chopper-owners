from gen.messages_pb2 import OwnerQuery, Owner
from gen.axiom_context import AxiomContext


def list_owners(ax: AxiomContext, input: OwnerQuery) -> Owner:
    """List owners with optional type filtering and pagination."""
    # Note: In production, this would query a database
    # For now, we return an empty owner as a placeholder
    return Owner()
