## Installer

> `/System/Library/CoreServices/Installer.app/Contents/MacOS/Installer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1363.0.0.0.0
-  __TEXT.__text: 0x19f94
+1365.0.0.0.0
+  __TEXT.__text: 0x1a198
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x6f40
-  __TEXT.__objc_methlist: 0x1af8
+  __TEXT.__objc_stubs: 0x6fa0
+  __TEXT.__objc_methlist: 0x1b10
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x304b
-  __TEXT.__objc_methname: 0x6973
+  __TEXT.__objc_methname: 0x69af
   __TEXT.__objc_classname: 0x450
   __TEXT.__objc_methtype: 0xd06
   __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__unwind_info: 0x700
   __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__cfstring: 0x28c0
   __DATA_CONST.__objc_classlist: 0x118

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x500
   __DATA.__objc_const: 0x3720
-  __DATA.__objc_selrefs: 0x2170
+  __DATA.__objc_selrefs: 0x2188
   __DATA.__objc_ivar: 0x2d4
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x270

   - /usr/lib/libDiskUnlock.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 552
-  Symbols:   276
-  CStrings:  1925
+  Functions: 554
+  Symbols:   277
+  CStrings:  1928
 
Symbols:
+ _OBJC_CLASS_$_NSPopUpButton
CStrings:
+ "_styleBottomBarButtonsInView:"
+ "_styleButton:"
+ "setBorderShape:"
```
