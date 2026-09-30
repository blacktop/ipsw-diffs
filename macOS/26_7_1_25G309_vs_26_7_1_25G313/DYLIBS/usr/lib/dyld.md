## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Sep 17 21:10:50 PDT 2026; root:libignition-58~38658/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Sep 17 21:10:50 PDT 2026; root:libignition-58~38658/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri Aug 21 01:53:28 PDT 2026; root:libignition-58~38643/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Fri Aug 21 01:53:28 PDT 2026; root:libignition-58~38643/libignition_core/RELEASE_ARM64E"
```
