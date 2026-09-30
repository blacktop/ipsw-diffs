## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-719.1.0.0.0
-  __TEXT.__text: 0x61478
-  __TEXT.__auth_stubs: 0xf60
+728.0.0.0.0
+  __TEXT.__text: 0x61a4c
+  __TEXT.__auth_stubs: 0xf70
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x6464
+  __TEXT.__objc_methlist: 0x64fc
   __TEXT.__const: 0x87c2
   __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x3c99
+  __TEXT.__cstring: 0x3c9a
   __TEXT.__oslogstring: 0x307b
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x17b8
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x11fc
-  __TEXT.__objc_methname: 0xbe23
-  __TEXT.__objc_methtype: 0x17dc
-  __TEXT.__objc_stubs: 0x9520
-  __DATA_CONST.__got: 0x630
+  __TEXT.__objc_methname: 0xbeb8
+  __TEXT.__objc_methtype: 0x17e9
+  __TEXT.__objc_stubs: 0x95a0
+  __DATA_CONST.__got: 0x628
   __DATA_CONST.__const: 0x9a8
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fa0
+  __DATA_CONST.__objc_selrefs: 0x2fc0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x7c8
-  __AUTH_CONST.__const: 0x1168
-  __AUTH_CONST.__cfstring: 0x3f80
-  __AUTH_CONST.__objc_const: 0x132f0
+  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__const: 0x1188
+  __AUTH_CONST.__cfstring: 0x3fa0
+  __AUTH_CONST.__objc_const: 0x133c8
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x694
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x6a0
   __DATA.__data: 0x1c88
-  __DATA.__bss: 0x648
-  __DATA_DIRTY.__objc_data: 0x2800
+  __DATA.__bss: 0x650
+  __DATA_DIRTY.__objc_data: 0x29e0
   __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4905DDB1-1036-3D03-95AC-CF8BE1CB5804
-  Functions: 2476
-  Symbols:   9303
-  CStrings:  4100
+  UUID: B3083F25-BD15-31DF-BD61-E630A1187936
+  Functions: 2488
+  Symbols:   9343
+  CStrings:  4107
 
Symbols:
+ +[IFImage(ISPlaceholderImage) _applyTreatmentsAndCacheResultForResource:fallbackTypeID:descriptor:description:]
+ -[ISDefaults safeBoot]
+ -[ISDefaults safeBoot].cold.1
+ -[ISIconSegmentationFeedbackBilinearGradient initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:meanColor:]
+ -[ISIconSegmentationFeedbackBilinearGradient meanColor]
+ -[ISIconSegmentationFeedbackComplex dealloc]
+ -[ISIconSegmentationFeedbackComplex initWithMeanColor:]
+ -[ISIconSegmentationFeedbackComplex meanColor]
+ -[ISIconSegmentationFeedbackSingleColor meanColor]
+ -[ISIconStackAssetCatalogResource _fallbackImageForSize:scale:]
+ -[ISIconStackCompositeResource _fallbackImageForSize:scale:]
+ -[ISiOSAppClipRecipe generic]
+ -[ISiOSAppClipRecipe setGeneric:]
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackBilinearGradient._meanColor
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackComplex._meanColor
+ _OBJC_IVAR_$_ISiOSAppClipRecipe._generic
+ __OBJC_$_INSTANCE_METHODS_ISIconSegmentationFeedbackComplex
+ __OBJC_$_INSTANCE_VARIABLES_ISIconSegmentationFeedbackComplex
+ __OBJC_$_PROP_LIST_ISIconSegmentationFeedbackBackground
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ISIconSegmentationFeedbackBackground
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ISIconSegmentationFeedbackBackground
+ ___22-[ISDefaults safeBoot]_block_invoke
+ ___block_literal_global.236
+ ___block_literal_global.238
+ _objc_msgSend$_applyTreatmentsAndCacheResultForResource:fallbackTypeID:descriptor:description:
+ _objc_msgSend$_fallbackImageForSize:scale:
+ _objc_msgSend$initWithMeanColor:
+ _objc_msgSend$initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:meanColor:
+ _objc_msgSend$meanColor
+ _objc_msgSend$safeBoot
+ _safeBoot.inSafeMode
+ _safeBoot.onceToken
+ _sysctlbyname
- +[IFImage(ISPlaceholderImage) _applyTreatmentsAndCacheResultForResource:descriptor:description:]
- -[ISIconSegmentationFeedbackBilinearGradient initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:]
- ___block_literal_global.233
- ___block_literal_global.235
- _objc_msgSend$_applyTreatmentsAndCacheResultForResource:descriptor:description:
- _objc_msgSend$initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:
CStrings:
+ "%@_%@,%.1f,%.1f,%.f,%d"
+ "00:29:33"
+ "@56@0:8^{CGColor=}16^{CGColor=}24^{CGColor=}32^{CGColor=}40^{CGColor=}48"
+ "Center Image mask"
+ "T^{CGColor=},R,N"
+ "T^{CGColor=},R,N,V_meanColor"
+ "_applyTreatmentsAndCacheResultForResource:fallbackTypeID:descriptor:description:"
+ "_fallbackImageForSize:scale:"
+ "_meanColor"
+ "initWithMeanColor:"
+ "initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:meanColor:"
+ "kern.safeboot"
+ "meanColor"
+ "safeBoot"
- "%@_%@,%.1f,%.1f,%.f"
- "19:31:56"
- "@48@0:8^{CGColor=}16^{CGColor=}24^{CGColor=}32^{CGColor=}40"
- "OverrideSolarium"
- "Solarium"
- "SwiftUI"
- "_applyTreatmentsAndCacheResultForResource:descriptor:description:"
- "initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:"

```
