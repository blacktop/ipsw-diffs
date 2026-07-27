## SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55600.160.5.0.1
-  __TEXT.__text: 0x1fff8
+55600.160.6.0.1
+  __TEXT.__text: 0x20034
   __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_stubs: 0x4620
-  __TEXT.__objc_methlist: 0x1f4c
+  __TEXT.__objc_stubs: 0x4640
+  __TEXT.__objc_methlist: 0x1f54
   __TEXT.__const: 0x140
-  __TEXT.__objc_methname: 0x4ade
+  __TEXT.__objc_methname: 0x4af7
   __TEXT.__oslogstring: 0x22b5
   __TEXT.__objc_classname: 0x35c
   __TEXT.__objc_methtype: 0x15d8
-  __TEXT.__cstring: 0x1e0a
+  __TEXT.__cstring: 0x1e1c
   __TEXT.__gcc_except_tab: 0x3b8
   __TEXT.__ustring: 0x776
   __TEXT.__dlopen_cstrs: 0x10d

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x3018
-  __DATA.__objc_selrefs: 0x1760
+  __DATA.__objc_selrefs: 0x1768
   __DATA.__objc_ivar: 0x290
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x4a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 821
+  Functions: 822
   Symbols:   530
-  CStrings:  1737
+  CStrings:  1739
 
Functions:
~ sub_100011244 : 68 -> 60
+ sub_100011280
CStrings:
+ "SafePluginLoading"
+ "safePluginLoadingEnabled"
```
