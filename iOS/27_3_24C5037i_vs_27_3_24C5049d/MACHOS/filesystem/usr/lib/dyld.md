## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__AUTH_CONST.__const`
- `__DATA_DIRTY.__all_image_info`

```diff
Functions:
~ _sandbox_check : 116 -> 120
~ _strrchr : 48 -> 44
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Nov 10 21:40:54 PST 2026; root:libignition-64~30628/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Nov 10 21:40:54 PST 2026; root:libignition-64~30628/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Oct 24 01:08:15 PDT 2026; root:libignition-64~30250/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sat Oct 24 01:08:15 PDT 2026; root:libignition-64~30250/libignition_core/RELEASE_ARM64E"
```
