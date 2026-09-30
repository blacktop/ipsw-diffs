## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri Jul 31 18:11:41 PDT 2026; root:libignition-58~38607/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Fri Jul 31 18:11:41 PDT 2026; root:libignition-58~38607/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Jul 11 14:30:19 PDT 2026; root:libignition-58~38557/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sat Jul 11 14:30:19 PDT 2026; root:libignition-58~38557/libignition_core/RELEASE_ARM64E"
```
