## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Oct 10 01:04:36 PDT 2026; root:libignition-64~29907/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sat Oct 10 01:04:36 PDT 2026; root:libignition-64~29907/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Sep 30 20:51:37 PDT 2026; root:libignition-64~29579/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Wed Sep 30 20:51:37 PDT 2026; root:libignition-64~29579/libignition_core/RELEASE_ARM64E"
```
