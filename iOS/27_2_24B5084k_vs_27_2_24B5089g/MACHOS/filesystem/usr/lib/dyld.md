## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Sep 13 19:37:18 PDT 2026; root:libignition-64~27375/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sun Sep 13 19:37:18 PDT 2026; root:libignition-64~27375/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri Sep  4 23:05:44 PDT 2026; root:libignition-64~25453/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Fri Sep  4 23:05:44 PDT 2026; root:libignition-64~25453/libignition_core/RELEASE_ARM64E"
```
