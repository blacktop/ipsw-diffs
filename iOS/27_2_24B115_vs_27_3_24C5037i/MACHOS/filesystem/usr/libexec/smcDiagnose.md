## smcDiagnose

> `/usr/libexec/smcDiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-162.40.11.0.0
-  __TEXT.__text: 0x3d80
+162.60.11.0.0
+  __TEXT.__text: 0x3ed0
   __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x8c2
+  __TEXT.__cstring: 0x958
   __TEXT.__const: 0x1c
   __TEXT.__objc_methname: 0x154
   __TEXT.__objc_classname: 0xe

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 58
+  Functions: 59
   Symbols:   58
-  CStrings:  123
+  CStrings:  126
 
CStrings:
+ "## Key count %u (GetKeyCount) differs from #KEY %u\n"
+ "ERROR: GetKeyCount failed with OS error %s.\n"
+ "ERROR: GetKeyCount failed with SMC error code 0x%x.\n"
```
