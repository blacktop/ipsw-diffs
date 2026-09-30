## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-4626.103.0.0.0
-  __TEXT.__text: 0xe2b8
+4630.1.102.0.0
+  __TEXT.__text: 0xe3f8
   __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x19a0
   __TEXT.__objc_methlist: 0x64c
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x189f
+  __TEXT.__cstring: 0x18bb
   __TEXT.__objc_methname: 0x19e1
   __TEXT.__oslogstring: 0x130b
   __TEXT.__objc_classname: 0x11a
   __TEXT.__objc_methtype: 0x329
   __TEXT.__gcc_except_tab: 0x140
   __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__const: 0x15b8
+  __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__cfstring: 0xf20
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x128
-  __DATA.__bss: 0x9c0
+  __DATA.__bss: 0x9e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 635
-  Symbols:   376
-  CStrings:  689
+  Functions: 641
+  Symbols:   378
+  CStrings:  691
 
Symbols:
+ _SBLogResourceConditions
+ _SBLogShipMode
CStrings:
+ "ResourceConditions"
+ "ShipMode"
```
