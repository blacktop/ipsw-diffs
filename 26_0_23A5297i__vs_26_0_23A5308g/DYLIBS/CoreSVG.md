## CoreSVG

> `/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG`

```diff

-352.0.0.0.0
-  __TEXT.__text: 0x34050
-  __TEXT.__auth_stubs: 0x1260
+353.0.0.0.0
+  __TEXT.__text: 0x34110
+  __TEXT.__auth_stubs: 0x1270
   __TEXT.__const: 0x320
   __TEXT.__cstring: 0x2277
-  __TEXT.__gcc_except_tab: 0x30f0
+  __TEXT.__gcc_except_tab: 0x30e8
   __TEXT.__unwind_info: 0x1b18
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x137
   __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x940
+  __AUTH_CONST.__auth_got: 0x948
   __AUTH_CONST.__const: 0x7a8
   __AUTH_CONST.__cfstring: 0x4c0
   __DATA.__data: 0x48

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 00168D0C-32B6-3C7A-A029-BFA069DAB116
+  UUID: F52B6656-5921-3975-BAC4-0B81CD6A8ABB
   Functions: 1109
   Symbols:   3025
   CStrings:  631
Symbols:
+ _CGAffineTransformEqualToTransform
- _xmlFree
Functions:
~ __ZN9SVGReader17parseXMLNodeStyleEP8_xmlNode : 204 -> 192
~ __ZN12SVGAttributeC2EN7SVGAtom4NameE6CGRect : 436 -> 440
~ __ZN11SVGGradientC2ERKS_ : 396 -> 364
~ __ZNK11SVGGradient7isEqualERKS_ : 248 -> 400
~ __ZNK7SVGNode11boundingBoxE26CGSVGNodeBoundingBoxOption : 300 -> 392
~ __ZL22SetNodeTextIfAvailableP8_xmlNodeP7SVGNode : 224 -> 212

```
