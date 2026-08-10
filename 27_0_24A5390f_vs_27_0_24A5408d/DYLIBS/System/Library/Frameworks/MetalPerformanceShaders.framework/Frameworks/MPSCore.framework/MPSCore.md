## MPSCore

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-130.0.15.0.0
-  __TEXT.__text: 0x96204
+130.0.19.0.0
+  __TEXT.__text: 0x962b8
   __TEXT.__objc_methlist: 0x27f4
   __TEXT.__const: 0x2924
-  __TEXT.__cstring: 0xa611
+  __TEXT.__cstring: 0xa62c
   __TEXT.__oslogstring: 0x7f
   __TEXT.__gcc_except_tab: 0x4db0
-  __TEXT.__unwind_info: 0x1e30
+  __TEXT.__unwind_info: 0x1e38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__got: 0x208
-  __AUTH_CONST.__const: 0x5f10
+  __AUTH_CONST.__const: 0x5f30
   __AUTH_CONST.__cfstring: 0x37e0
   __AUTH_CONST.__objc_const: 0x5230
   __AUTH_CONST.__weak_auth_got: 0x18

   __DATA.__bss: 0x1c
   __DATA_DIRTY.__objc_ivar: 0x54
   __DATA_DIRTY.__objc_data: 0xe10
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1724
-  Symbols:   799
-  CStrings:  878
+  Functions: 1726
+  Symbols:   800
+  CStrings:  879
 
Symbols:
+ _MPSIsPerfTestCmdSignpostEnabled
CStrings:
+ "130.0.19"
+ "MPS_PERF_TEST_CMD_SIGNPOST"
- "130.0.15"
```
