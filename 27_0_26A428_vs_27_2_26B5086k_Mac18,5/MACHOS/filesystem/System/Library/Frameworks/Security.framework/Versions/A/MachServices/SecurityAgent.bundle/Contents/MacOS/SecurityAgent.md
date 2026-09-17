## SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-55643.0.14.0.0
-  __TEXT.__text: 0x2b588
+55643.40.5.0.0
+  __TEXT.__text: 0x2b648
   __TEXT.__auth_stubs: 0x1240
   __TEXT.__objc_stubs: 0x5580
   __TEXT.__objc_methlist: 0x29e4
   __TEXT.__const: 0x171
   __TEXT.__cstring: 0x3115
   __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__oslogstring: 0x2e09
+  __TEXT.__oslogstring: 0x2e1e
   __TEXT.__objc_methname: 0x5a85
   __TEXT.__objc_classname: 0x618
   __TEXT.__objc_methtype: 0x1897
   __TEXT.__ustring: 0x187e
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x1018
+  __TEXT.__unwind_info: 0x1030
   __DATA_CONST.__const: 0x938
   __DATA_CONST.__cfstring: 0x2a40
   __DATA_CONST.__objc_classlist: 0x1d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1122
+  Functions: 1127
   Symbols:   735
-  CStrings:  2264
+  CStrings:  2265
 
CStrings:
+ "Prelogin user %{public}@ found, letter case ignored"
+ "Prelogin user %{public}@ not found"
- "Prelogin user %{public}@ does not match user %{public}@, skipping"
```
