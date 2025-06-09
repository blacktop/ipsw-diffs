## AnnotationKit

> `/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit`

```diff

-522.200.0.0.0
-  __TEXT.__text: 0xce584
-  __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_methlist: 0xe9a0
-  __TEXT.__cstring: 0x6060
-  __TEXT.__const: 0xf60
-  __TEXT.__gcc_except_tab: 0x1888
+546.0.0.0.0
+  __TEXT.__text: 0xd23cc
+  __TEXT.__auth_stubs: 0x1810
+  __TEXT.__objc_methlist: 0xef68
+  __TEXT.__cstring: 0x61b6
+  __TEXT.__const: 0xf80
+  __TEXT.__gcc_except_tab: 0x18b8
   __TEXT.__oslogstring: 0xa63
   __TEXT.__dlopen_cstrs: 0x122
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x2fa8
-  __TEXT.__objc_classname: 0x20da
-  __TEXT.__objc_methname: 0x2268e
-  __TEXT.__objc_methtype: 0x791d
-  __TEXT.__objc_stubs: 0x18240
-  __DATA_CONST.__got: 0xbc8
-  __DATA_CONST.__const: 0xfc0
-  __DATA_CONST.__objc_classlist: 0x740
+  __TEXT.__unwind_info: 0x30c8
+  __TEXT.__objc_classname: 0x210a
+  __TEXT.__objc_methname: 0x22e32
+  __TEXT.__objc_methtype: 0x7afa
+  __TEXT.__objc_stubs: 0x18960
+  __DATA_CONST.__got: 0xbf0
+  __DATA_CONST.__const: 0xfe8
+  __DATA_CONST.__objc_classlist: 0x750
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a28
+  __DATA_CONST.__objc_selrefs: 0x7c40
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x558
-  __DATA_CONST.__objc_arraydata: 0x808
-  __AUTH_CONST.__auth_got: 0xb98
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x6280
-  __AUTH_CONST.__objc_const: 0x153f0
+  __DATA_CONST.__objc_superrefs: 0x560
+  __DATA_CONST.__objc_arraydata: 0x838
+  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x6480
+  __AUTH_CONST.__objc_const: 0x15a60
   __AUTH_CONST.__objc_arrayobj: 0xa08
   __AUTH_CONST.__objc_intobj: 0x6f0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x4150
-  __DATA.__objc_ivar: 0xcfc
-  __DATA.__data: 0x18c8
-  __DATA.__bss: 0x12c8
+  __AUTH.__objc_data: 0x41f0
+  __DATA.__objc_ivar: 0xd38
+  __DATA.__data: 0x18d0
+  __DATA.__bss: 0x1318
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: DCAA9C72-901A-3DC4-BC37-951B001D7830
-  Functions: 4858
-  Symbols:   820
-  CStrings:  8103
+  UUID: 5C81C6A7-D906-367D-9A06-EBC10D86E986
+  Functions: 4967
+  Symbols:   842
+  CStrings:  8244
 
Symbols:
+ _CFAutorelease
+ _CGColorCreateCopyByMatchingToColorSpace
+ _CGColorCreateSRGB
+ _CGColorCreateWithContentHeadroom
+ _CGColorGetContentHeadroom
+ _CGColorGetNumberOfComponents
+ _CGColorSpaceGetName
+ _CGColorSpaceIsHDR
+ _CGColorSpaceRetain
+ _CGColorSpaceSupportsOutput
+ _CGColorSpaceUsesExtendedRange
+ _CGContextSetCTM
+ _CGContextSetEDRTargetHeadroom
+ _CGImageGetColorSpace
+ _CGImageGetContentHeadroom
+ __os_feature_enabled_impl
+ _kCAContentsFormatRGBA16Float
+ _kCAContentsFormatRGBA8Uint
+ _kCGColorSpaceDisplayP3
+ _kCGColorSpaceExtendedDisplayP3
+ _kCGColorSpaceExtendedLinearSRGB
+ _strtod
CStrings:
+ "%@ %f"
+ "%@%f "
+ "+[AKAnnotationRenderer _concreteRenderAnnotation:intoContext:options:pageControllerOrNil:]"
+ "@\"UIColor\"20@0:8B16"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@20@0:8f16"
+ "@24@0:8^{CGColor=}16"
+ "@28@0:8^{CGContext=}16B24"
+ "@40@0:8d16d24d32"
+ "@52@0:8d16d24d32d40f48"
+ "AKAnnotationRendererOptions"
+ "AKColorString"
+ "AKHeadroomLimitForHDR"
+ "B24@0:8^{CGContext=}16"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "CGBitmapContextCreate failed. Unable to draw annotations to image."
+ "HDRMarkup"
+ "Headroom for test color: %g %g %g => %g"
+ "NSColor"
+ "PencilAndPaper"
+ "T@\"NSString\",&,V_string"
+ "T@\"UIColor\",&,V_fillColorHDR"
+ "T@\"UIColor\",&,V_fillColorSDR"
+ "T@\"UIColor\",&,V_foregroundColorHDR"
+ "T@\"UIColor\",&,V_foregroundColorSDR"
+ "T@\"UIColor\",&,V_strokeColorHDR"
+ "T@\"UIColor\",&,V_strokeColorSDR"
+ "T@\"UIColor\",C"
+ "TB,N,V_allowHDR"
+ "TB,N,V_forDisplay"
+ "TB,V_isDetectedSignature"
+ "Td,N,V_maxHDRGain"
+ "Td,R"
+ "Tf,R"
+ "UTF8String"
+ "^{CGImage=}88@0:8^{CGImage=}16B24B28{CGAffineTransform=dddddd}32B80B84"
+ "_allowHDR"
+ "_concreteRenderAnnotation:intoContext:options:pageControllerOrNil:"
+ "_currentMaxHDRGain"
+ "_drawPathForArrow:inContext:options:inPath:pageControllerForPixelAlignmentOrNil:minimumGrabbableBorderThickness:"
+ "_drawPathForArrowShape:inContext:options:inPath:"
+ "_fillAndStrokePath:forAnnotation:inContext:options:"
+ "_fillColorHDR"
+ "_fillColorSDR"
+ "_forDisplay"
+ "_foregroundColorHDR"
+ "_foregroundColorSDR"
+ "_hdrColorRed:green:blue:"
+ "_isDetectedSignature"
+ "_maxHDRGain"
+ "_optionsForContext:forDisplay:"
+ "_propagateTextColors:"
+ "_string"
+ "_strokeColorHDR"
+ "_strokeColorSDR"
+ "_translateColorEncoding:"
+ "_translateObservationKeys:"
+ "_updateLayerRange"
+ "akAdaptToCurrentHeadroom:"
+ "akCGColorWithHeadroom"
+ "akColorString"
+ "akColorWithCGColor:"
+ "akColorWithRed:green:blue:alpha:headroom:"
+ "akHeadroom"
+ "akIsEDR"
+ "akIsHDR"
+ "akToSDR"
+ "allKeys"
+ "allowHDR"
+ "annotationHeadroom"
+ "colorFromString:"
+ "contextWantsHDR:"
+ "defaultMaxHDRGain"
+ "defaultOptions"
+ "desiredHeadroom"
+ "f16@0:8"
+ "fillColorAllowHDR:"
+ "fillColorHDR"
+ "fillColorHDRString"
+ "fillColorSDR"
+ "forDisplay"
+ "foregroundColor"
+ "foregroundColorAllowHDR:"
+ "foregroundColorHDR"
+ "foregroundColorSDR"
+ "groupingLevel"
+ "hasHDRAnnotation"
+ "hasSelectionWithEditableFillColor"
+ "hasSelectionWithEditableStrokeColor"
+ "hasSelectionWithEditableTextColor"
+ "isBitmapContext:"
+ "isDetectedSignature"
+ "maxHDRGain"
+ "numberWithFloat:"
+ "potentialEDRHeadroom"
+ "renderAnnotation:intoContext:options:pageControllerOrNil:"
+ "renderAnnotationText:intoContext:options:pageControllerOrNil:"
+ "renderAnnotationsOnImage:wantsHDR:opaque:withTransform:shouldApplyCropRect:forPreview:"
+ "revalidateHDR"
+ "selectionInteraction:handleTapOnCanvasAtLocation:hitStrokes:inAttachment:"
+ "setAllowHDR:"
+ "setColorMaximumLinearExposure:"
+ "setContentsFormat:"
+ "setFillColorHDR:"
+ "setFillColorSDR:"
+ "setForDisplay:"
+ "setForegroundColor:"
+ "setForegroundColorHDR:"
+ "setForegroundColorSDR:"
+ "setIsDetectedSignature:"
+ "setMaxHDRGain:"
+ "setString:"
+ "setStrokeColorHDR:"
+ "setStrokeColorSDR:"
+ "setWantsExtendedDynamicRangeContent:"
+ "singleSelectedAnnotation"
+ "stringFromColor:"
+ "strokeColorAllowHDR:"
+ "strokeColorHDR"
+ "strokeColorHDRString"
+ "strokeColorSDR"
+ "strokeColorSDRString"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "updateColorWellActivation:"
+ "v48@0:8@16^{CGContext=}24@32@40"
+ "v48@0:8@16^{CGContext=}24@32^{CGPath=}40"
+ "v48@0:8^{CGPath=}16@24^{CGContext=}32@40"
+ "v56@0:8@\"PKSelectionInteraction\"16{CGPoint=dd}24@\"NSArray\"40@\"PKAttachmentView\"48"
+ "v56@0:8@16{CGPoint=dd}24@40@48"
+ "v64@0:8@16^{CGContext=}24@32^{CGPath=}40@48d56"
+ "wantsExtendedDynamicRangeContent"
- "+[AKAnnotationRenderer _concreteRenderAnnotation:intoContext:forDisplay:pageControllerOrNil:]"
- "T@\"UIColor\",&,V_strokeColor"
- "_concreteRenderAnnotation:intoContext:forDisplay:pageControllerOrNil:"
- "_drawPathForArrow:inContext:inPath:pageControllerForPixelAlignmentOrNil:minimumGrabbableBorderThickness:"
- "_drawPathForArrowShape:inContext:inPath:"
- "_fillAndStrokePath:forAnnotation:inContext:"
- "colorWithString:"
- "initWithColor:"
- "renderAnnotation:intoContext:forDisplay:pageControllerOrNil:"
- "renderAnnotationText:intoContext:isForScreen:pageControllerOrNil:"
- "stringRepresentation"
- "v40@0:8@16^{CGContext=}24^{CGPath=}32"
- "v40@0:8^{CGPath=}16@24^{CGContext=}32"
- "v56@0:8@16^{CGContext=}24^{CGPath=}32@40d48"

```
