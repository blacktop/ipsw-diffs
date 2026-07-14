## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Jul  9 23:19:47 PDT 2026; root:libignition-58~38524/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Jul  9 23:19:47 PDT 2026; root:libignition-58~38524/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Jun 28 20:04:39 PDT 2026; root:libignition-58~38430/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sun Jun 28 20:04:39 PDT 2026; root:libignition-58~38430/libignition_core/RELEASE_ARM64E"
```
