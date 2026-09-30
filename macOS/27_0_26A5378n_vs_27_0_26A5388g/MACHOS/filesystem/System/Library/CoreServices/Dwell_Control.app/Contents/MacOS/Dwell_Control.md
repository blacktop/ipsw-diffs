## Dwell Control

> `/System/Library/CoreServices/Dwell Control.app/Contents/MacOS/Dwell Control`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0x8668
-  __TEXT.__auth_stubs: 0x670
+418.0.0.0.0
+  __TEXT.__text: 0x86b0
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_stubs: 0x2620
   __TEXT.__objc_methlist: 0xbc4
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__oslogstring: 0x96
-  __TEXT.__cstring: 0x499
+  __TEXT.__cstring: 0x4c9
   __TEXT.__objc_methname: 0x2880
   __TEXT.__objc_classname: 0xac
   __TEXT.__objc_methtype: 0x89b
   __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__const: 0x540
-  __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x1c0
   __DATA.__objc_const: 0xe08
   __DATA.__objc_selrefs: 0xb78

   - /usr/lib/libUniversalAccess.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 264
-  Symbols:   168
-  CStrings:  584
+  Symbols:   169
+  CStrings:  586
 
Symbols:
+ _SecTaskCopySigningIdentifier
Functions:
~ sub_1000016a8 : 260 -> 332
CStrings:
+ "com.apple.MenuBarAgent"
+ "com.apple.systemuiserver"
```
