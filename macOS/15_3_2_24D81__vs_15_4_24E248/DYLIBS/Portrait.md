## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Versions/A/Portrait`

```diff

-436.81.2.0.0
-  __TEXT.__text: 0x9dd98
-  __TEXT.__auth_stubs: 0x1060
+436.100.8.0.0
+  __TEXT.__text: 0x9d260
+  __TEXT.__auth_stubs: 0x1080
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0x8040
-  __TEXT.__const: 0x21274
-  __TEXT.__cstring: 0x7700
-  __TEXT.__oslogstring: 0x3bdf
-  __TEXT.__gcc_except_tab: 0x738
+  __TEXT.__objc_methlist: 0x8934
+  __TEXT.__const: 0x21254
+  __TEXT.__cstring: 0x7756
+  __TEXT.__oslogstring: 0x3bb5
+  __TEXT.__gcc_except_tab: 0x780
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x1f10
-  __TEXT.__objc_classname: 0x11b1
-  __TEXT.__objc_methname: 0x181c9
-  __TEXT.__objc_methtype: 0x52f1
-  __TEXT.__objc_stubs: 0xe140
-  __DATA_CONST.__got: 0x900
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__objc_classlist: 0x500
+  __TEXT.__unwind_info: 0x1f78
+  __TEXT.__objc_classname: 0x11d6
+  __TEXT.__objc_methname: 0x18412
+  __TEXT.__objc_methtype: 0x538b
+  __TEXT.__objc_stubs: 0xe240
+  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4758
+  __DATA_CONST.__objc_selrefs: 0x4910
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x468
   __DATA_CONST.__objc_arraydata: 0x660
-  __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x4d40
-  __AUTH_CONST.__objc_const: 0x1bed8
+  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__const: 0x870
+  __AUTH_CONST.__cfstring: 0x4d60
+  __AUTH_CONST.__objc_const: 0x1b5a0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x3200
+  __AUTH.__objc_data: 0x3250
   __AUTH.__data: 0xbd0
-  __DATA.__objc_ivar: 0x15c4
-  __DATA.__data: 0x8b8
-  __DATA.__bss: 0x1c0
+  __DATA.__objc_ivar: 0x15d4
+  __DATA.__data: 0x918
+  __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87A3B786-197B-373C-94DD-BC98F7C3ACAB
-  Functions: 3779
-  Symbols:   9413
-  CStrings:  6942
+  UUID: C6B3197F-9B73-31D8-AE60-EF93B7FB49B5
+  Functions: 3801
+  Symbols:   9484
+  CStrings:  6974
 
Symbols:
+ +[PTCinematographyDecision defaultTransition].cold.1
+ +[PTCinematographyFocusFramesOptions _defaultMaximumDisparityPerSecond].cold.1
+ +[PTCinematographyFocusFramesOptions _defaultMaximumRackFocusPullTime].cold.1
+ +[PTCinematographyFocusFramesOptions _defaultMinimumRackFocusPullTime].cold.1
+ +[PTCinematographyFocusPuller defaultEMASampleCount].cold.1
+ +[PTCinematographyFocusPuller defaultMaximumVelocity].cold.1
+ +[PTCinematographyFocusPuller defaultResistance].cold.1
+ +[PTCinematographyFocusPuller defaultStrategy].cold.1
+ -[PTAtomStream _readAtomHeader].cold.1
+ -[PTAtomWriter appendBytes:size:].cold.1
+ -[PTAtomWriter appendVersion:flags:].cold.1
+ -[PTAtomWriter beginAtomOfType:].cold.1
+ -[PTCommandQueueProxy .cxx_destruct]
+ -[PTCommandQueueProxy forwardInvocation:]
+ -[PTCommandQueueProxy initWithInitializerCommandQueue:]
+ -[PTCommandQueueProxy methodSignatureForSelector:]
+ -[PTCommandQueueProxy switchToCommandQueue:]
+ -[PTEffectRenderRequest gestureCount]
+ -[PTEffectRenderRequest setGestureCount:]
+ -[PTEffectRenderRequest setSuppressGestureTriggeredReactions:]
+ -[PTEffectRenderRequest suppressGestureTriggeredReactions]
+ -[PTEffectRenderer copyInYUV:toOutYUV:].cold.2
+ -[PTHumanDetections unpackDetections:].cold.1
+ -[PTMSRResize _downsample:toDest:useCustomFilter:centerAlignment:synchronous:].cold.1
+ -[PTMSRResize rotate:crop:rotationDegree:toDest:synchronous:].cold.1
+ -[PTVFXRenderEffect asyncVFXInit]
+ -[PTVFXRenderEffect asyncVFXInit].cold.1
+ -[PTVFXRenderEffect asyncVFXInit].cold.2
+ -[PTVFXRenderEffect setupCommonVFXSceneLoadOptions:metalLibraryURL:commandQueue:]
+ GCC_except_table31
+ GCC_except_table39
+ GCC_except_table6
+ GCC_except_table72
+ HistogramInNormalizedRectFromLockedPixelBufferInfo_FloatSize.cold.1
+ OBJC_IVAR_$_PTCommandQueueProxy._commandQueue
+ OBJC_IVAR_$_PTEffectRenderRequest._gestureCount
+ OBJC_IVAR_$_PTEffectRenderRequest._suppressGestureTriggeredReactions
+ OBJC_IVAR_$_PTEffectRenderer._reactionsToRender
+ PTDetectionTypeIsBetter.cold.1
+ PTKTraceInit.cold.1
+ PTSerializationDebugIsEnabled.cold.1
+ _MGGetSInt64Answer
+ _OBJC_CLASS_$_MTLCommandQueueDescriptor
+ _OBJC_CLASS_$_PTCommandQueueProxy
+ _OBJC_METACLASS_$_PTCommandQueueProxy
+ _PTLogSystem.cold.1
+ _StringFromTimeRange
+ __19-[PTEffect render:]_block_invoke.250
+ __33-[PTEffect updateEffectDelegate:]_block_invoke.241
+ __33-[PTEffect updateEffectDelegate:]_block_invoke.241.cold.1
+ __OBJC_$_INSTANCE_METHODS_PTCommandQueueProxy
+ __OBJC_$_INSTANCE_VARIABLES_PTCommandQueueProxy
+ __OBJC_$_PROP_LIST_MTLCommandQueue
+ __OBJC_$_PROP_LIST_PTCommandQueueProxy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLCommandQueue
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLCommandQueue
+ __OBJC_$_PROTOCOL_REFS_MTLCommandQueue
+ __OBJC_CLASS_PROTOCOLS_$_PTCommandQueueProxy
+ __OBJC_CLASS_RO_$_PTCommandQueueProxy
+ __OBJC_LABEL_PROTOCOL_$_MTLCommandQueue
+ __OBJC_METACLASS_RO_$_PTCommandQueueProxy
+ __OBJC_PROTOCOL_$_MTLCommandQueue
+ ___33-[PTVFXRenderEffect asyncVFXInit]_block_invoke
+ ___78-[PTMSRResize _downsample:toDest:useCustomFilter:centerAlignment:synchronous:]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48w_e28_v16?0"<MTLCommandBuffer>"8l
+ ___copy_helper_block_e8_32w
+ ___destroy_helper_block_e8_32w
+ __block_literal_global.238
+ __block_literal_global.256
+ _atanf
+ _downsample:toDest:useCustomFilter:centerAlignment:synchronous:.customFilterSupported
+ _downsample:toDest:useCustomFilter:centerAlignment:synchronous:.onceToken
+ _objc_msgSend$asyncVFXInit
+ _objc_msgSend$initWithInitializerCommandQueue:
+ _objc_msgSend$instanceMethodSignatureForSelector:
+ _objc_msgSend$newCommandQueueWithDescriptor:
+ _objc_msgSend$setGestureCount:
+ _objc_msgSend$setQosLevel:
+ _objc_msgSend$setupCommonVFXSceneLoadOptions:metalLibraryURL:commandQueue:
+ _objc_msgSend$suppressGestureTriggeredReactions
+ _objc_msgSend$switchToCommandQueue:
- +[PTGlobalVideoMetadata deserializeMetadataWithType:fromGlobalMetadata:error:].cold.1
- -[PTGlobalVideoMetadata writeToData:withOptions:].cold.1
- -[PTVFXRenderEffect initVFX:asyncInitQueue:].cold.1
- -[PTVFXRenderEffect initVFX:asyncInitQueue:].cold.2
- -[PTVFXRenderEffect initVFX:asyncInitQueue:].cold.3
- -[PTVFXRenderEffect setupCommonVFXSceneLoadOptions:metalLibraryURL:]
- GCC_except_table63
- GCC_except_table64
- GCC_except_table65
- GCC_except_table71
- PTParameterPairSerialization_GetParameter.cold.2
- __19-[PTEffect render:]_block_invoke.136
- __33-[PTEffect updateEffectDelegate:]_block_invoke.127
- __33-[PTEffect updateEffectDelegate:]_block_invoke.127.cold.1
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0l
- __block_literal_global.124
- __block_literal_global.142
- _objc_msgSend$setupCommonVFXSceneLoadOptions:metalLibraryURL:
CStrings:
+ "/System/AppleInternal/Library/Frameworks/MediaAnalysis.framework/MediaAnalysis"
+ "@\"<MTLCommandBuffer>\"16@0:8"
+ "@\"<MTLCommandBuffer>\"24@0:8@\"MTLCommandBufferDescriptor\"16"
+ "ChipID"
+ "MSR error %i"
+ "MTLCommandQueue"
+ "Out of bounds crop rect"
+ "PTCommandQueueProxy"
+ "T@\"NSString\",C"
+ "TB,V_suppressGestureTriggeredReactions"
+ "TQ,V_gestureCount"
+ "_gestureCount"
+ "_reactionsToRender"
+ "_suppressGestureTriggeredReactions"
+ "addResidencySet:"
+ "addResidencySets:count:"
+ "asyncVFXInit"
+ "commandBufferWithDescriptor:"
+ "commandBufferWithUnretainedReferences"
+ "gestureCount"
+ "initWithInitializerCommandQueue:"
+ "insertDebugCaptureBoundary"
+ "instanceMethodSignatureForSelector:"
+ "newCommandQueueWithDescriptor:"
+ "removeResidencySet:"
+ "removeResidencySets:count:"
+ "setGestureCount:"
+ "setQosLevel:"
+ "setSuppressGestureTriggeredReactions:"
+ "setupCommonVFXSceneLoadOptions:metalLibraryURL:commandQueue:"
+ "suppressGestureTriggeredReactions"
+ "switchToCommandQueue:"
+ "v24@0:8@\"<MTLResidencySet>\"16"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8r^@16Q24"
- "Error initializing VFX %@"
- "Failed to get parameter %d of type %d. Unknown type."
- "setupCommonVFXSceneLoadOptions:metalLibraryURL:"
- "\xe2"

```
