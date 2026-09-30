## TextRecognition

> `/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition`

```diff

-396.0.0.0.0
-  __TEXT.__text: 0x16d954
-  __TEXT.__auth_stubs: 0x2490
+399.0.0.0.0
+  __TEXT.__text: 0x170fa0
+  __TEXT.__auth_stubs: 0x2520
   __TEXT.__objc_methlist: 0x9d2c
-  __TEXT.__swift5_typeref: 0x153
+  __TEXT.__swift5_typeref: 0x197
   __TEXT.__swift5_capture: 0x3c
-  __TEXT.__cstring: 0x1a153
-  __TEXT.__const: 0x1f1e
-  __TEXT.__constg_swiftt: 0x64
-  __TEXT.__swift5_fieldmd: 0x30
-  __TEXT.__swift5_types: 0x8
+  __TEXT.__cstring: 0x1a29a
+  __TEXT.__const: 0x206e
+  __TEXT.__constg_swiftt: 0x80
+  __TEXT.__swift5_fieldmd: 0x1a8
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_reflstr: 0xc8
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x4
-  __TEXT.__gcc_except_tab: 0x1844c
-  __TEXT.__oslogstring: 0x4baf
+  __TEXT.__gcc_except_tab: 0x18590
+  __TEXT.__oslogstring: 0x4c30
   __TEXT.__ustring: 0xa954
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x5be8
-  __TEXT.__eh_frame: 0x3ec
+  __TEXT.__unwind_info: 0x5ca0
+  __TEXT.__eh_frame: 0x424
   __TEXT.__objc_classname: 0x1953
-  __TEXT.__objc_methname: 0x1a963
-  __TEXT.__objc_methtype: 0xbdc3
+  __TEXT.__objc_methname: 0x1a981
+  __TEXT.__objc_methtype: 0xbdc6
   __TEXT.__objc_stubs: 0x11500
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc78
   __DATA_CONST.__const: 0x20e8
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x50

   __DATA_CONST.__objc_selrefs: 0x50e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x488
-  __DATA_CONST.__objc_arraydata: 0x17a00
-  __AUTH_CONST.__auth_got: 0x1260
-  __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x1cc0
-  __AUTH_CONST.__cfstring: 0x2e320
+  __DATA_CONST.__objc_arraydata: 0x17b90
+  __AUTH_CONST.__auth_got: 0x12a8
+  __AUTH_CONST.__auth_ptr: 0xe0
+  __AUTH_CONST.__const: 0x2040
+  __AUTH_CONST.__cfstring: 0x2e440
   __AUTH_CONST.__objc_const: 0x163c8
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x2ac0
-  __AUTH_CONST.__objc_dictobj: 0x5208
+  __AUTH_CONST.__objc_dictobj: 0x5370
   __AUTH_CONST.__objc_doubleobj: 0xf30
   __AUTH_CONST.__objc_floatobj: 0x220
   __AUTH.__objc_data: 0x428
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xd34
-  __DATA.__data: 0x10470
-  __DATA.__bss: 0x64
+  __DATA.__data: 0x10478
+  __DATA.__bss: 0x1f4
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_ivar: 0xe4
   __DATA_DIRTY.__objc_data: 0x3d68
-  __DATA_DIRTY.__data: 0x88
+  __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__bss: 0x630
-  __DATA_DIRTY.__common: 0x88
+  __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5165
-  Symbols:   6618
-  CStrings:  15534
+  Functions: 5208
+  Symbols:   6635
+  CStrings:  15546
 
Symbols:
+ __ZN15CRDetectorUtils26computeConnectedComponentsEPfmmRNS_38CRTextDetectorConnectedComponentResultE
+ __ZN15CRDetectorUtils31erodeConnectedComponentForLabelERNS_38CRTextDetectorConnectedComponentResultEmPKjmm
+ __ZN15CRDetectorUtils32dilateConnectedComponentForLabelERNS_38CRTextDetectorConnectedComponentResultEmPKjmm
+ __ZN15CRDetectorUtils43recomputeConnectedComponentsForLabelsInRectERNS_38CRTextDetectorConnectedComponentResultEmmmmmm
+ __ZN15CRDetectorUtils59estimateVerticalIsthmusMergedLineCountInConnectedComponentsERKNS_38CRTextDetectorConnectedComponentResultEmm
+ __ZN23CRDetectorPostProcessV328splitIsthmusMergedComponentsEPN15CRDetectorUtils38CRTextDetectorConnectedComponentResultEb
+ __ZN26CRDetectorPolygonExtractor18smoothPivotCentersERNSt3__16vectorI7CGPointNS0_9allocatorIS2_EEEE
+ __ZN26CRDetectorPolygonExtractor20generatePivotCentersERNSt3__16vectorI13PixelPositionNS0_9allocatorIS2_EEEE
+ _utf16CheckIsEnglishCapital
- __ZN15CRDetectorUtils21connectComponentLabelEPfmmRNS_38CRTextDetectorConnectedComponentResultE
- __ZN26CRDetectorPolygonExtractor20generatePivotsCenterERNSt3__16vectorI13PixelPositionNS0_9allocatorIS2_EEEE
CStrings:
+ "CRFormContentTypeConfirmPassword"
+ "CRFormContentTypeConfirmUsername"
+ "CRFormContentTypeCurrentUsername"
+ "CRFormContentTypeInstantMessage"
+ "CRFormContentTypeNewAccountEmailAddress"
+ "CRFormContentTypeNewAccountUsername"
+ "CRFormContentTypeNewPassword"
+ "CRFormContentTypeOneTimeCode"
+ "CameraReader"
+ "Split isthmus merged components."
+ "_adjustBeamSearchResults:tokens:greedyCandidateString:greedyCandidateTokens:decodingLocale:"
+ "_mappedUrlificationRangeFor:withMapping: Range (%!l(MISSING)d, %!l(MISSING)d) out of bounds for mapping length %!l(MISSING)d."
+ "adjustedBeamSearchDecodedString:greedyDecodedString:decodingLocale:"
+ "hasLongLatinWords"
+ "v56@0:8^@16@24@32@40@48"
- "_adjustBeamSearchResults:tokens:greedyCandidateString:greedyCandidateTokens:"
- "adjustedBeamSearchDecodedString:greedyDecodedString:"
- "v48@0:8^@16@24@32@40"

```
