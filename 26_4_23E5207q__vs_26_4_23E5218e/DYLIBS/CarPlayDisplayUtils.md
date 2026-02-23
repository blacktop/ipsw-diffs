## CarPlayDisplayUtils

> `/System/Library/PrivateFrameworks/CarPlayDisplayUtils.framework/CarPlayDisplayUtils`

```diff

-774.8.0.0.0
-  __TEXT.__text: 0x8d50
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__const: 0xa98
-  __TEXT.__oslogstring: 0x601
-  __TEXT.__cstring: 0x24a
+774.12.0.0.0
+  __TEXT.__text: 0x82a8
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__const: 0xaa8
+  __TEXT.__oslogstring: 0x391
+  __TEXT.__cstring: 0x26a
   __TEXT.__swift5_typeref: 0x1a7
   __TEXT.__swift5_reflstr: 0x240
   __TEXT.__swift5_assocty: 0x78

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x40
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_methname: 0x38
   __TEXT.__objc_stubs: 0x60

   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x858
   __DATA.__data: 0x108
   __DATA.__bss: 0xeb0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 477C01F3-BEC6-3628-9201-7020DC60CDC9
-  Functions: 266
-  Symbols:   163
-  CStrings:  32
+  UUID: 954A50FC-86FF-3A1F-B736-3406F9897F2D
+  Functions: 265
+  Symbols:   162
+  CStrings:  29
 
Symbols:
- _objc_release_x28
CStrings:
+ ";\n\nallowsSmartZoom: "
+ ";\n canvasSizes: "
+ ";\n squaredPixelSize: "
+ "Primary display size is less than minimum: CanvasSize(%s) < Min(%s); Returning minimal size;\n minSize(ceilToEven)(%s)"
- "; allowsSmartZoom: "
- "; squaredPixelSize: "
- "Calculated Original canvas size: Result(%s)=SquaredPixelSize(%s) x PointScaleFactor(%f) at PointScale(%ld)\nDisplay: %s"
- "Optimal[no ZoomFactor] primary display scale canvas size calculated: Result(%s) = PixelSize(%s) x OptimalScaleFactor(%s) at PointScale(%ld)\nDisplay: %s"
- "Optimal[with ZoomFactor] primary display scale canvas size calculated: Result(%s) = SquaredPixelSize(%s) x AdjustedScale(%f); AdjustedScale=PointScaleFactor(%f)/zoomFactor(%f)\nDisplay: %s"
- "Primary display size is less than minimum: CanvasSize(%s) < Min(%s); Returning minimal size;\n minSize(%s)"
- "Secondary display size after scaling: Size(%s) = SquaredPixelSize(%s) x Scale(%f); Scale = PointScaleFactor(%f)/ZoomFactor(%f) at PointScale(%ld)"

```
