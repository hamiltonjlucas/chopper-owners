# Downstream Dependencies

This package is consumed by:

- **chopper-cli** - CLI tool that imports nodes directly for local mode

## Change Notification

If you modify any of the following in this package, you MUST update chopper-cli:

1. **Message schemas** (messages/messages.proto)
   - Adding/removing fields
   - Changing field types
   - Renaming messages

2. **Node interfaces** (nodes/*.py)
   - Changing function signatures
   - Changing input/output messages
   - Adding/removing nodes

3. **Behavior** (nodes/*.py)
   - Changing error messages
   - Changing validation rules
   - Changing default values

## Verification

After making changes to this package:

1. Run `chopper-cli` tests to ensure compatibility
2. Update chopper-cli models if needed
3. Update chopper-cli local clients if needed
