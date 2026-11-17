## CinematicFraming

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`

```diff

-764.60.7.0.2
-  __TEXT.__text: 0x232e4
-  __TEXT.__objc_methlist: 0x24fc
+764.60.13.0.1
+  __TEXT.__text: 0x2332c
+  __TEXT.__objc_methlist: 0x2514
   __TEXT.__const: 0x690
   __TEXT.__gcc_except_tab: 0xcb4
   __TEXT.__cstring: 0x1eb9

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16e8
+  __DATA_CONST.__objc_selrefs: 0x16f8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__got: 0x1f8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1720
-  __AUTH_CONST.__objc_const: 0x4fb0
+  __AUTH_CONST.__objc_const: 0x4fe0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x598
+  __DATA.__objc_ivar: 0x59c
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x3a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 856
-  Symbols:   1635
+  Functions: 858
+  Symbols:   1638
   CStrings:  311
 
Symbols:
+ -[VCProcessor manualFramingFocalLengthMultiplier]
+ -[VCProcessor setManualFramingFocalLengthMultiplier:]
+ _OBJC_IVAR_$_VCProcessor._manualFramingFocalLengthMultiplier
Functions:
~ -[VCProcessor init] : 92 -> 100
~ -[VCProcessor _updateOutputCameraFocalLengthWithVideoZoomFactor] : 156 -> 204
- -[VCProcessor setInputMetadata:]
+ -[VCProcessor inputMetadata]
+ -[VCProcessor setInputCamera:]
+ -[VCProcessor outputCamera]
```
