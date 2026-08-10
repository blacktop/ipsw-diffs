## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-1580.0.0.0.0
-  __TEXT.__text: 0x1ed57c
+1585.0.0.0.0
+  __TEXT.__text: 0x1ed3ec
   __TEXT.__init_offsets: 0x14c
   __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0xedd8
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__gcc_except_tab: 0x2abf8
-  __TEXT.__oslogstring: 0xaa9f
-  __TEXT.__cstring: 0x5ec6
+  __TEXT.__gcc_except_tab: 0x2abd4
+  __TEXT.__oslogstring: 0xaa80
+  __TEXT.__cstring: 0x5ed7
   __TEXT.__unwind_info: 0x8350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Functions:
~ __GLOBAL__sub_I_ResetInfo.cpp : 2588 -> 2676
~ __ZN9SARModule22initializeHelpers_syncEv : 7900 -> 7412
CStrings:
+ ".*ATCS_TIMEOUT.*"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1585"
+ "AppleBasebandServices_Manager-1585"
- "AppleBasebandManager-AppleBasebandServices_Manager-1580"
- "AppleBasebandServices_Manager-1580"
- "Failed to get Accessory State!"
```
