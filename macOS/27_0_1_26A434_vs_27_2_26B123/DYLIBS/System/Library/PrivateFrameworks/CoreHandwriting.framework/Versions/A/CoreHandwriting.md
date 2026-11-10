## CoreHandwriting

> `/System/Library/PrivateFrameworks/CoreHandwriting.framework/Versions/A/CoreHandwriting`

```diff

-587.2.100.0.0
-  __TEXT.__text: 0x3687bc
+587.2.104.0.0
+  __TEXT.__text: 0x36aad4
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xdef4
-  __TEXT.__const: 0x4ff0
+  __TEXT.__objc_methlist: 0xdf64
+  __TEXT.__const: 0x5000
   __TEXT.__dlopen_cstrs: 0x1c8
-  __TEXT.__cstring: 0x875b
-  __TEXT.__oslogstring: 0x16374
+  __TEXT.__cstring: 0x8789
+  __TEXT.__oslogstring: 0x1659f
   __TEXT.__swift5_typeref: 0x104
   __TEXT.__swift5_reflstr: 0x2a
   __TEXT.__swift5_assocty: 0x60

   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x14
-  __TEXT.__gcc_except_tab: 0x50458
+  __TEXT.__gcc_except_tab: 0x50750
   __TEXT.__ustring: 0x2786
-  __TEXT.__unwind_info: 0xb9d0
+  __TEXT.__unwind_info: 0xba48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x6538
+  __DATA_CONST.__objc_selrefs: 0x6580
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x7a8
   __DATA_CONST.__objc_arraydata: 0x2030
   __DATA_CONST.__got: 0xa90
-  __AUTH_CONST.__const: 0x99e0
-  __AUTH_CONST.__cfstring: 0xee60
-  __AUTH_CONST.__objc_const: 0x1cb00
+  __AUTH_CONST.__const: 0x9aa0
+  __AUTH_CONST.__cfstring: 0xeec0
+  __AUTH_CONST.__objc_const: 0x1cb20
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_arrayobj: 0xd68
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_intobj: 0x10f8
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x10e8
+  __AUTH_CONST.__auth_got: 0x1100
   __AUTH_CONST.__auth_ptr: 0x128
   __AUTH.__objc_data: 0x64d0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x151c
+  __DATA.__objc_ivar: 0x1520
   __DATA.__data: 0xec8
   __DATA.__bss: 0x1278
   __DATA.__common: 0x80

   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
+  - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage
   - /System/Library/PrivateFrameworks/CVNLP.framework/Versions/A/CVNLP
   - /System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7523
-  Symbols:   1121
-  CStrings:  3534
+  Functions: 7541
+  Symbols:   1124
+  CStrings:  3547
 
Symbols:
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithURL
+ _CGImageDestinationFinalize
CStrings:
+ "%@ render input drawing to %@/%@.png, "
+ "%@ render style drawing to %@/%@.png, "
+ "%@ render synthesis result to %@/%@.png, "
+ "%@ serialize input drawing to %@/%@.json, "
+ "%@ serialize style drawing to %@/%@.json, "
+ "%@ serialize synthesis result to %@/%@.json, "
+ "%@: skipping update, result stroke provider version no longer matches the latest provider. Waiting for a newer result."
+ "%@_%@_input_drawing"
+ "%@_%@_result"
+ "%@_%@_style_drawing"
+ "@\"NSArray\"8@?0"
+ "CHLogAllSynthesisRequestImages"
+ "Drawing writeImageToFile saving image at URL %@"
+ "Drawing writeImageToFile unable to create image destination at URL %@"
+ "Drawing writeImageToFile unable to render drawing with %lu strokes"
+ "Drawing writeImageToFile unable to write image at URL %@"
+ "No reachable predecessor state for stroke %zu, segment %zu"
+ "png"
+ "public.png"
- "%@ serialize input drawing to %@/%@, "
- "%@ serialize style drawing to %@/%@, "
- "%@ serialize synthesis result to %@/%@, "
- "%@_%@_input_drawing.json"
- "%@_%@_result.json"
- "%@_%@_style_drawing.json"
```
