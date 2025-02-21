## motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

-502.5.5.0.0
-  __TEXT.__text: 0x25074
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_stubs: 0x6b80
-  __TEXT.__objc_methlist: 0x283c
-  __TEXT.__const: 0x388
-  __TEXT.__gcc_except_tab: 0x8ac
-  __TEXT.__cstring: 0x1af4
-  __TEXT.__oslogstring: 0x1fe2
-  __TEXT.__objc_methname: 0x8aa8
-  __TEXT.__objc_classname: 0x5b4
-  __TEXT.__objc_methtype: 0x1cf9
+502.7.2.0.0
+  __TEXT.__text: 0x275d4
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_stubs: 0x6d80
+  __TEXT.__objc_methlist: 0x2ffc
+  __TEXT.__const: 0x3a8
+  __TEXT.__gcc_except_tab: 0xa18
+  __TEXT.__cstring: 0x2005
+  __TEXT.__oslogstring: 0x20d5
+  __TEXT.__objc_methname: 0x8efc
+  __TEXT.__objc_classname: 0x5e5
+  __TEXT.__objc_methtype: 0x1ec0
   __TEXT.__dlopen_cstrs: 0x285
-  __TEXT.__unwind_info: 0xa58
-  __DATA_CONST.__auth_got: 0x4f0
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x938
-  __DATA_CONST.__cfstring: 0x7c0
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__unwind_info: 0xb00
+  __DATA_CONST.__auth_got: 0x4f8
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x55a0
-  __DATA.__objc_selrefs: 0x1e50
-  __DATA.__objc_ivar: 0x3b0
-  __DATA.__objc_data: 0x910
+  __DATA.__objc_const: 0x4ce8
+  __DATA.__objc_selrefs: 0x1ff0
+  __DATA.__objc_ivar: 0x3d4
+  __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x850
-  __DATA.__bss: 0x268
+  __DATA.__bss: 0x320
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1131
-  Symbols:   294
-  CStrings:  2096
+  Functions: 1200
+  Symbols:   296
+  CStrings:  2170
 
Symbols:
+ _AXSSIsAppleInternalBuild
+ _OBJC_CLASS_$_AXSSMotionTrackingExpressionConfiguration_Exclave
CStrings:
+ "\x01"
+ "\x012"
+ "\x03"
+ "%@ intrinsics: ((%f, %f, %f), (%f, %f, %f), (%f, %f, %f)"
+ "%s: Failed to get clientDataAXDictionary or smoothDataDictionary"
+ "%s: Failed to get faceKitTrackedFaceDictionary"
+ "-[AXMTFaceKitExclavesResult initWithFaceKitLiteSharedDataDictionary:expressions:noseBaseCenter:referenceDimensionsValue:]"
+ "-[AXMTFaceKitFaceTracker _generateFaceKitResultForLiteOutput:]"
+ "@112@0:8@16{?=QQQQQQQQQ}24@96@104"
+ "@32@0:8@16^{opaqueCMSampleBuffer=}24"
+ "@56@0:8@16@24^{opaqueCMSampleBuffer=}32@40@48"
+ "AXMTFaceKitExclavesResult"
+ "AXMTFaceKitFaceTracker: Failed to create CVAFaceTrackingLiteFilterRef! %d"
+ "AXMTFaceKitXNUResult"
+ "Adjusted"
+ "CVAFaceTrackingLiteFilterCopyDecodedOutput"
+ "CVAFaceTrackingLiteFilterCreate"
+ "CVAFaceTrackingLiteFilterGetOutput"
+ "CVAFaceTrackingLiteFilterProcessVanilla"
+ "Original FaceKit"
+ "Q20@0:8C16"
+ "ShouldLogIntrinsics"
+ "T,D,N"
+ "T@\"NSArray\",R,C,D,N"
+ "T@\"NSDictionary\",C,D,N"
+ "T@\"NSValue\",&,N,V__referenceDimensionsValue"
+ "T@\"NSValue\",&,N,V_noseBaseCenterLandmarkVertex"
+ "T@\"NSValue\",R,D,N"
+ "T^{CVAFaceTrackingLiteFilter=},N,V__faceKitLiteFilterRef"
+ "T{?=QQQQQQQQQ},R,N,V_expressions"
+ "T{?=[4]},D,N"
+ "T{CGPoint=dd},R,D,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,D,N"
+ "T{CGSize=dd},D,N"
+ "^{CVAFaceTrackingLiteFilter=}"
+ "^{CVAFaceTrackingLiteFilter=}16@0:8"
+ "__faceKitLiteFilterRef"
+ "__referenceDimensionsValue"
+ "_axFacialExpressionActivationForFaceKitLiteExpresionActivation:"
+ "_faceKitLiteFilterRef"
+ "_generateFaceKitResultForLiteOutput:"
+ "_generateFaceKitResultForVanillaOutput:withSampleBuffer:"
+ "_logIntrinsicsForInternalBuilds:withLogPrefix:"
+ "_noseBaseCenterLandmarkVertex"
+ "_projectPoint:usingRGBCameraDictionary:pose:referenceDimensions:"
+ "_referenceDimensions"
+ "_referenceDimensionsValue"
+ "_updateAXExpressions:withFaceKitLiteExpresion:faceKitLiteExpressionActivation:"
+ "boolForKey:"
+ "charValue"
+ "didUpdateVideoResolution:"
+ "emptyAccessibilityExpressions"
+ "initWithFaceKitLiteSharedDataDictionary:expressions:noseBaseCenter:referenceDimensionsValue:"
+ "initWithFaceKitTrackedFaceDictionary:semanticsDictionary:sampleBuffer:expressions:referenceDimensionsValue:"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionBrowsUp"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionEyeBlink"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionJawOpen"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionMouthPuckerCenter"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionMouthPuckerLeft"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionMouthPuckerRight"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionNoseSneer"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionSmile"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_ExpressionTongueOut"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_Expressions"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_LandmarkNoseBaseCenter"
+ "kCVAFaceTrackingLiteFilterClientAccessibility_Landmarks"
+ "kCVAFaceTrackingLiteFilter_ClientData"
+ "kCVAFaceTrackingLiteFilter_ClientDataAccessibility"
+ "kCVAFaceTrackingLiteFilter_SharedData"
+ "noseBaseCenterLandmarkVertex"
+ "processExclaveDetectedExpressions:previousExpressions:expressionConfiguration:startExpressionsOutSet:endExpressionsOutSet:"
+ "referenceDimensions"
+ "setNoseBaseCenterLandmarkVertex:"
+ "setReferenceDimensions:"
+ "set_faceKitLiteFilterRef:"
+ "set_referenceDimensionsValue:"
+ "v24@0:8^{CVAFaceTrackingLiteFilter=}16"
+ "v32@0:8^{__CFDictionary=}16^{opaqueCMSampleBuffer=}24"
+ "v40@0:8@\"AXMTVideoCapturer\"16{CGSize=dd}24"
+ "v40@0:8@16{CGSize=dd}24"
+ "v72@0:8{?=[3]}16@64"
+ "videoCapturer:didUpdateVideoResolution:"
+ "{?=\"raiseEyebrows\"Q\"openMouth\"Q\"smile\"Q\"tongueOut\"Q\"eyeBlink\"Q\"noseSneer\"Q\"mouthPuckerCenter\"Q\"puckerLipsLeft\"Q\"puckerLipsRight\"Q}"
+ "{?=QQQQQQQQQ}100@0:8{?=QQQQQQQQQ}16@88C96"
+ "{?=QQQQQQQQQ}16@0:8"
+ "{CGPoint=dd}120@0:816@32{?=[4]}40{CGSize=dd}104"
- "\x01!"
- "\x04"
- "@48@0:8@16@24^{opaqueCMSampleBuffer=}32@40"
- "T,N,V_poseTranslation"
- "T@\"NSDictionary\",C,N,V_semanticsDictionary"
- "T{?=[4]},N,V_pose"
- "T{CGPoint=dd},R,N,V_projectedPoint"
- "_handleDetectedFaceAccelerationModeWithFaceBounds:noseCenter:pose:poseTranslation:imageSize:"
- "_projectPoint:usingFaceInfoDict:pose:"
- "initWithFaceKitTrackedFaceDictionary:semanticsDictionary:sampleBuffer:expressions:"
- "v160@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGPoint=dd}48{?=[4]}64128{CGSize=dd}144"
- "{CGPoint=dd}104@0:816@32{?=[4]}40"

```
