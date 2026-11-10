## SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.14.0.0
-  __TEXT.__text: 0x21d84
+55643.40.5.0.0
+  __TEXT.__text: 0x21e3b
   __TEXT.__stubs: 0x5a6
   __TEXT.__const: 0xe0
   __TEXT.__objc_methname: 0x4f47
-  __TEXT.__oslogstring: 0x2831
+  __TEXT.__oslogstring: 0x2851
   __TEXT.__objc_classname: 0x32d
   __TEXT.__objc_methtype: 0x1750
   __TEXT.__cstring: 0x1f17
   __TEXT.__gcc_except_tab: 0x3d0
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xbd
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__unwind_info: 0x770
   __TEXT.__eh_frame: 0x58
   __DATA_CONST.__const: 0x758
   __DATA_CONST.__cfstring: 0x1a00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 768
+  Functions: 772
   Symbols:   524
-  CStrings:  1787
+  CStrings:  1788
 
CStrings:
+ "Prelogin user %{public}@ found, letter case ignored"
+ "Prelogin user %{public}@ not found"
- "Prelogin user %{public}@ does not match user %{public}@, skipping"
```
