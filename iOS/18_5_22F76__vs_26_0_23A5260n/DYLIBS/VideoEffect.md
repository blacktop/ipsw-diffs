## VideoEffect

> `/System/Library/PrivateFrameworks/VideoEffect.framework/VideoEffect`

```diff

-1.17.0.0.0
-  __TEXT.__text: 0x8f60
+2.4.0.0.0
+  __TEXT.__text: 0x9a80
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x6f4
+  __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0x116
-  __TEXT.__cstring: 0xb52
+  __TEXT.__cstring: 0xc8b
   __TEXT.__oslogstring: 0x79
   __TEXT.__gcc_except_tab: 0x74
   __TEXT.__swift5_typeref: 0xa
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x144
-  __TEXT.__objc_methname: 0x1841
-  __TEXT.__objc_methtype: 0x376
-  __TEXT.__objc_stubs: 0x1000
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__objc_classname: 0x189
+  __TEXT.__objc_methname: 0x1b3d
+  __TEXT.__objc_methtype: 0x42a
+  __TEXT.__objc_stubs: 0x1180
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__objc_const: 0x2e88
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x3a58
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x118
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x138
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 67C3C2FA-A774-34AC-ACB8-F26442F64339
-  Functions: 241
-  Symbols:   1083
-  CStrings:  446
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: DB6943EE-9D33-31EA-8487-B59526B9DAD0
+  Functions: 274
+  Symbols:   1212
+  CStrings:  490
 
Symbols:
+ +[VELensFlareMitigationConfiguration defaultRevision]
+ +[VELensFlareMitigationConfiguration isSupportedRevision:]
+ +[VELensFlareMitigationConfiguration supportedRevisions]
+ +[VELensFlareMitigationParameters getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:]
+ -[VELensFlareMitigationConfiguration .cxx_destruct]
+ -[VELensFlareMitigationConfiguration downloadAssetWithCompletionHandler:]
+ -[VELensFlareMitigationConfiguration frameHeight]
+ -[VELensFlareMitigationConfiguration framePreferredPixelFormats]
+ -[VELensFlareMitigationConfiguration frameSupportedPixelFormats]
+ -[VELensFlareMitigationConfiguration frameWidth]
+ -[VELensFlareMitigationConfiguration getAssetStatusWithPercentCompleted:]
+ -[VELensFlareMitigationConfiguration initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:]
+ -[VELensFlareMitigationConfiguration qualityPrioritization]
+ -[VELensFlareMitigationConfiguration revision]
+ -[VELensFlareMitigationConfiguration usePrecomputedFlow]
+ -[VELensFlareMitigationParameters .cxx_destruct]
+ -[VELensFlareMitigationParameters destinationFrame]
+ -[VELensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:]
+ -[VELensFlareMitigationParameters nextFrameOpticalCenter]
+ -[VELensFlareMitigationParameters nextFrame]
+ -[VELensFlareMitigationParameters opticalCenterShift]
+ -[VELensFlareMitigationParameters opticalFlow]
+ -[VELensFlareMitigationParameters previousOutputFrame]
+ -[VELensFlareMitigationParameters previousPreviousOutputFrame]
+ -[VELensFlareMitigationParameters sourceFrameOpticalCenter]
+ -[VELensFlareMitigationParameters sourceFrame]
+ -[VELensFlareMitigationParameters submissionMode]
+ -[VESuperResolutionConfiguration downloadAssetWithCompletionHandler:]
+ -[VESuperResolutionConfiguration getAssetStatusWithPercentCompleted:]
+ -[VESuperResolutionParameters initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:]
+ -[VESuperResolutionParameters submissionMode]
+ _OBJC_CLASS_$_DVPLensFlareMitigationConfiguration
+ _OBJC_CLASS_$_DVPLensFlareMitigationParameters
+ _OBJC_CLASS_$_VDGProcessor
+ _OBJC_CLASS_$_VELensFlareMitigationConfiguration
+ _OBJC_CLASS_$_VELensFlareMitigationParameters
+ _OBJC_IVAR_$_VEFrameProcessor._vdgProcessor
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._frameHeight
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._framePreferredPixelFormats
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._frameWidth
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._qualityPrioritization
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._revision
+ _OBJC_IVAR_$_VELensFlareMitigationConfiguration._usePrecomputedFlow
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._destinationFrame
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._nextFrame
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._nextFrameOpticalCenter
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._opticalCenterShift
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._opticalFlow
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._previousOutputFrame
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._previousPreviousOutputFrame
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._sourceFrame
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._sourceFrameOpticalCenter
+ _OBJC_IVAR_$_VELensFlareMitigationParameters._submissionMode
+ _OBJC_IVAR_$_VESuperResolutionParameters._submissionMode
+ _OBJC_METACLASS_$_VELensFlareMitigationConfiguration
+ _OBJC_METACLASS_$_VELensFlareMitigationParameters
+ __OBJC_$_CLASS_METHODS_VELensFlareMitigationConfiguration
+ __OBJC_$_CLASS_METHODS_VELensFlareMitigationParameters
+ __OBJC_$_INSTANCE_METHODS_VELensFlareMitigationConfiguration
+ __OBJC_$_INSTANCE_METHODS_VELensFlareMitigationParameters
+ __OBJC_$_INSTANCE_VARIABLES_VELensFlareMitigationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VELensFlareMitigationParameters
+ __OBJC_$_PROP_LIST_VELensFlareMitigationConfiguration
+ __OBJC_$_PROP_LIST_VELensFlareMitigationParameters
+ __OBJC_CLASS_PROTOCOLS_$_VELensFlareMitigationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_VELensFlareMitigationParameters
+ __OBJC_CLASS_RO_$_VELensFlareMitigationConfiguration
+ __OBJC_CLASS_RO_$_VELensFlareMitigationParameters
+ __OBJC_METACLASS_RO_$_VELensFlareMitigationConfiguration
+ __OBJC_METACLASS_RO_$_VELensFlareMitigationParameters
+ ___69-[VESuperResolutionConfiguration downloadAssetWithCompletionHandler:]_block_invoke
+ ___73-[VELensFlareMitigationConfiguration downloadAssetWithCompletionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_VideoEffect
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_VideoEffect
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_VideoEffect
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_VideoEffect
+ _dvpVDGConfigFromVE
+ _dvpVDGParamsFromVE
+ _objc_msgSend$downloadAssetWithCompletionHandler:
+ _objc_msgSend$downloadMobileAssetWithInputType:withCompletionHandler:
+ _objc_msgSend$getAssetStatusWithPercentCompleted:
+ _objc_msgSend$getMobileAssetStatusForInputType:percentCompleted:
+ _objc_msgSend$getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:
+ _objc_msgSend$initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:
+ _objc_msgSend$initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:
+ _objc_msgSend$nextFrameOpticalCenter
+ _objc_msgSend$opticalCenterShift
+ _objc_msgSend$previousPreviousOutputFrame
+ _objc_msgSend$processWithDeghostingParams:error:
+ _objc_msgSend$sourceFrameOpticalCenter
+ _objc_msgSend$startSessionWithDeghostingConfig:error:
- -[VEMotionBlurParameters initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:virtualShutterAngleDegrees:submissionMode:destinationFrame:]
- -[VEMotionBlurParameters virtualShutterAngleDegrees]
- _OBJC_IVAR_$_VEMotionBlurParameters._virtualShutterAngleDegrees
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_VideoEffect
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_VideoEffect
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_VideoEffect
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_VideoEffect
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_VideoEffect
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_VideoEffect
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_VideoEffect
- _objc_msgSend$initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:destinationFrame:
CStrings:
+ "\t"
+ "@\"VDGProcessor\""
+ "@112@0:8@16@24@32{CGPoint=dd}40{CGPoint=dd}56d72@80@88q96@104"
+ "B40@0:8^{CGPoint=dd}16Q24^d32"
+ "Could not init VDGProcessor"
+ "Error: Invalid VELensFlareMitigationConfiguration revision %d"
+ "Fail to to initialize: Mismatch between source, next frame's pixel formats"
+ "T@\"VEFrame\",R,N,V_previousPreviousOutputFrame"
+ "Td,R,N,V_opticalCenterShift"
+ "T{CGPoint=dd},R,N,V_nextFrameOpticalCenter"
+ "T{CGPoint=dd},R,N,V_sourceFrameOpticalCenter"
+ "VDGProcessor already created"
+ "VELensFlareMitigationConfiguration"
+ "VELensFlareMitigationConfiguration is missing"
+ "VELensFlareMitigationParameters"
+ "VELensFlareMitigationParameters is missing"
+ "_nextFrameOpticalCenter"
+ "_opticalCenterShift"
+ "_previousPreviousOutputFrame"
+ "_sourceFrameOpticalCenter"
+ "_vdgProcessor"
+ "d"
+ "d16@0:8"
+ "downloadAssetWithCompletionHandler:"
+ "downloadMobileAssetWithInputType:withCompletionHandler:"
+ "getAssetStatusWithPercentCompleted:"
+ "getMobileAssetStatusForInputType:percentCompleted:"
+ "getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:"
+ "initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:"
+ "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:"
+ "nextFrameOpticalCenter"
+ "opticalCenterShift"
+ "previousPreviousOutputFrame"
+ "processWithDeghostingParams:error:"
+ "q24@0:8^q16"
+ "sourceFrameOpticalCenter"
+ "startSessionWithDeghostingConfig:error:"
+ "v16@?0q8"
+ "v24@0:8@?16"
+ "v24@?0q8@\"NSError\"16"
+ "{CGPoint=\"x\"d\"y\"d}"
+ "{CGPoint=dd}16@0:8"
- "Tq,R,N,V_virtualShutterAngleDegrees"
- "_virtualShutterAngleDegrees"
- "initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:virtualShutterAngleDegrees:submissionMode:destinationFrame:"
- "virtualShutterAngleDegrees"

```
