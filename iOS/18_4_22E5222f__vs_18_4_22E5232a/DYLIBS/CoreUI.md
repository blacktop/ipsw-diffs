## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-918.1.0.0.0
-  __TEXT.__text: 0xa4e28
-  __TEXT.__auth_stubs: 0x2610
+918.3.0.0.0
+  __TEXT.__text: 0xa4ef4
+  __TEXT.__auth_stubs: 0x2630
   __TEXT.__objc_methlist: 0x8918
   __TEXT.__const: 0x49f8
-  __TEXT.__cstring: 0x23a72
-  __TEXT.__gcc_except_tab: 0x13cc
+  __TEXT.__cstring: 0x23b42
+  __TEXT.__gcc_except_tab: 0x1424
   __TEXT.__oslogstring: 0x52
   __TEXT.__swift5_typeref: 0x72
   __TEXT.__swift5_capture: 0x4c

   __TEXT.__swift5_types: 0x20
   __TEXT.__unwind_info: 0x2fc8
   __TEXT.__objc_classname: 0xe01
-  __TEXT.__objc_methname: 0x13660
+  __TEXT.__objc_methname: 0x13667
   __TEXT.__objc_methtype: 0x59be
-  __TEXT.__objc_stubs: 0xc5c0
+  __TEXT.__objc_stubs: 0xc5e0
   __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0xe578
+  __DATA_CONST.__const: 0xe580
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4530
+  __DATA_CONST.__objc_selrefs: 0x4538
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0xbc0
-  __AUTH_CONST.__auth_got: 0x1320
+  __AUTH_CONST.__auth_got: 0x1330
   __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x2700
-  __AUTH_CONST.__cfstring: 0x11800
+  __AUTH_CONST.__cfstring: 0x11860
   __AUTH_CONST.__objc_const: 0xce78
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4366
+  Functions: 4364
   Symbols:   5406
-  CStrings:  9110
+  CStrings:  9114
 
Symbols:
+ _objc_exception_rethrow
+ _objc_terminate
CStrings:
+ "CUIVectorGlyphIncompatiblePointsException"
+ "CoreUI: Incompatible points when attempting to interpolate: Ultralight=%lu, Regular=%lu, Black=%lu"
+ "CoreUI: Incompatible points when attempting to interpolate: bundle-id=\"%@\""
+ "CoreUI: Incompatible points when attempting to interpolate: glyph-name=\"%@\""
+ "Incompatible glyph \"%@\" in bundle \"%@\". %@"
+ "Point counts: Ultralight=%lu, Regular=%lu, Black=%lu"
+ "reason"
- "-[CUIVectorGlyphMutator initWithPointSize:regular:ultralight:black:]"
- "_originPoints.numPoints == _blackDeltas.numDeltas"
- "_originPoints.numPoints == _ultralightDeltas.numDeltas"

```
