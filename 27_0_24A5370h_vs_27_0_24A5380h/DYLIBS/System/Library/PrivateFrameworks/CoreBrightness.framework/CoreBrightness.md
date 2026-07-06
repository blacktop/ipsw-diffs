## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-  __TEXT.__text: 0x1681ec
-  __TEXT.__objc_methlist: 0xcf0c
-  __TEXT.__cstring: 0xcdf5
-  __TEXT.__const: 0x16a08
-  __TEXT.__oslogstring: 0x18fed
-  __TEXT.__gcc_except_tab: 0x2758
+  __TEXT.__text: 0x16a888
+  __TEXT.__objc_methlist: 0xd08c
+  __TEXT.__cstring: 0xcb1a
+  __TEXT.__const: 0x169f8
+  __TEXT.__oslogstring: 0x1963d
+  __TEXT.__gcc_except_tab: 0x2768
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__swift5_typeref: 0xeb5
+  __TEXT.__swift5_typeref: 0xeb0
   __TEXT.__constg_swiftt: 0xc2c
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xa4e
+  __TEXT.__swift5_reflstr: 0xa44
   __TEXT.__swift5_fieldmd: 0x1018
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x308

   __TEXT.__swift5_capture: 0x3d0
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x54f0
+  __TEXT.__unwind_info: 0x5580
   __TEXT.__eh_frame: 0xb90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2e98
+  __DATA_CONST.__const: 0x2ec0
   __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x360
+  __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x57b8
+  __DATA_CONST.__objc_selrefs: 0x5898
   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x5b8
   __DATA_CONST.__objc_arraydata: 0xcb8
-  __DATA_CONST.__got: 0x710
-  __AUTH_CONST.__const: 0x3d90
-  __AUTH_CONST.__cfstring: 0xe260
-  __AUTH_CONST.__objc_const: 0x331f0
+  __DATA_CONST.__got: 0x7c0
+  __AUTH_CONST.__const: 0x3dc8
+  __AUTH_CONST.__cfstring: 0xe380
+  __AUTH_CONST.__objc_const: 0x334e0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0xd80

   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0x1370
-  __AUTH.__objc_data: 0x1630
-  __AUTH.__data: 0x7f0
-  __DATA.__objc_ivar: 0x16c4
-  __DATA.__data: 0x2eaf0
-  __DATA.__bss: 0x6690
+  __AUTH.__objc_data: 0x2630
+  __AUTH.__data: 0x640
+  __DATA.__objc_ivar: 0x16e0
+  __DATA.__data: 0x2eb78
+  __DATA.__bss: 0x66c0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x3238
-  __DATA_DIRTY.__data: 0x318
+  __DATA_DIRTY.__objc_data: 0x2238
+  __DATA_DIRTY.__data: 0x4e8
   __DATA_DIRTY.__common: 0x10
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8593
-  Symbols:   21908
-  CStrings:  6461
+  Functions: 8675
+  Symbols:   22106
+  CStrings:  6493
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
Symbols:
+ +[CBDisplayHandle handleForUniqueID:]
+ +[CBDisplayHandle handleWithDisplayID:andUUID:andUniqueID:]
+ -[AABRear checkSensorEnablementConditions]
+ -[AABRear getFrontLux]
+ -[AABRear isAODDisabled]
+ -[AABRear isFactorDisabled]
+ -[AABRear isFrontLuxSatisfied]
+ -[AABRear isGrimaldiLuxInUse]
+ -[AABRear isOtherALSDisabled]
+ -[AABRear isPropertyDisabled]
+ -[AABRear sensorIsSampling]
+ -[AABRear setAodDisabled:]
+ -[AABRear setFactorDisabled:]
+ -[AABRear setFrontLux:]
+ -[AABRear setGrimaldiLuxInUse:]
+ -[AABRear setOtherALSDisabled:]
+ -[AABRear setPropertyDisabled:]
+ -[AABRear shouldUseRLux:rLux:inUse:]
+ -[BrightnessSystemClientInternal setSyncProperty:forKey:error:]
+ -[CBALSNode getOcclusionDrivesGrimaldi]
+ -[CBALSNode occlusionDrivesGrimaldi]
+ -[CBClient newDisplayClientForUniqueID:withError:]
+ -[CBColorFilter acknowledgeEvent:]
+ -[CBColorFilter newColorSampleConditionWeightedForServices:]
+ -[CBColorFilter newColorSampleLogWeightedForServices:]
+ -[CBColorFilter newColorSampleWinnerTakesAllForServices:]
+ -[CBColorFilter selectedServices]
+ -[CBColorFilter selectionPolicy]
+ -[CBColorFilter setSelectionPolicy:]
+ -[CBDisplayContaineriOS handle]
+ -[CBDisplayHandle copyDescription]
+ -[CBDisplayHandle dealloc]
+ -[CBDisplayHandle description]
+ -[CBDisplayHandle initWithDisplayID:andUUID:andUniqueID:]
+ -[CBDisplayHandle initWithUniqueID:]
+ -[CBIndicatorBrightnessModule findContrastIndicatorNodeForContext:]
+ -[CBIndicatorBrightnessModule getDCPRoleIDFromContext:]
+ -[CBIndicatorBrightnessModule initWithContext:min:max:maxBoost:andFrameInfoProvider:]
+ -[CBJNDBasedContrastIndicatorPolicy description]
+ -[CBSBIM .cxx_destruct]
+ -[CBSBIM initialiseLimits:]
+ -[VMBLControl requestBrightnessTransactionForDisplayUUID:builtIn:]
+ GCC_except_table133
+ GCC_except_table190
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetName
+ _OBJC_CLASS_$_NSNull
+ _OBJC_IVAR_$_AABRear._aodDisabled
+ _OBJC_IVAR_$_AABRear._factorDisabled
+ _OBJC_IVAR_$_AABRear._frontLux
+ _OBJC_IVAR_$_AABRear._grimaldiLuxInUse
+ _OBJC_IVAR_$_AABRear._otherALSDisabled
+ _OBJC_IVAR_$_AABRear._propertyDisabled
+ _OBJC_IVAR_$_AABRear._sensorIsSampling
+ _OBJC_IVAR_$_CBALSNode._occlusionDrivesGrimaldi
+ _OBJC_IVAR_$_CBColorFilter._arrivedEvents
+ _OBJC_IVAR_$_CBColorFilter._selectionPolicy
+ _OBJC_IVAR_$_CBColorModuleShared._firstALSSelectionPolicy
+ _OBJC_IVAR_$_CBDisplayContaineriOS._handle
+ _OBJC_IVAR_$_CBDisplayHandle._cachedDescription
+ _OBJC_IVAR_$_CBSBIM._previousAccumulatedSBIM
+ __CFXLogHandle.log
+ __CFXLogHandle.once
+ __OBJC_$_INSTANCE_VARIABLES_CBDisplayHandle
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBRearALSModuleProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBRearALSModuleProtocol
+ __OBJC_$_PROTOCOL_REFS_CBRearALSModuleProtocol
+ __OBJC_LABEL_PROTOCOL_$_CBRearALSModuleProtocol
+ __OBJC_PROTOCOL_$_CBRearALSModuleProtocol
+ __ZN36PerceptualLuminanceThresholding_1nit15SetBoolPropertyEP8NSStringb
+ __ZN38PerceptualLuminanceThresholding_legacy15SetBoolPropertyEP8NSStringb
+ __ZN4AABC21_UpdateEsensorTrustedEfNSt3__18optionalIfEE
+ ___34-[CBColorFilter acknowledgeEvent:]_block_invoke
+ ___54-[CBColorFilter newColorSampleLogWeightedForServices:]_block_invoke
+ ___57-[CBColorFilter newColorSampleWinnerTakesAllForServices:]_block_invoke
+ ___60-[CBColorFilter newColorSampleConditionWeightedForServices:]_block_invoke
+ ___63-[BrightnessSystemClientInternal setSyncProperty:forKey:error:]_block_invoke
+ ____CFXLogHandle_block_invoke
+ _binFromAb
+ _kCBKeyDisplayUniqueID
+ _objc_msgSend$acknowledgeEvent:
+ _objc_msgSend$checkSensorEnablementConditions
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$copyDescription
+ _objc_msgSend$createConfigurationFromConfigurationProvider:withFallback:
+ _objc_msgSend$findContrastIndicatorNodeForContext:
+ _objc_msgSend$getDCPRoleIDFromContext:
+ _objc_msgSend$getOcclusionDrivesGrimaldi
+ _objc_msgSend$handleForUniqueID:
+ _objc_msgSend$initWithContext:min:max:maxBoost:andFrameInfoProvider:
+ _objc_msgSend$initWithDisplayID:andUUID:andUniqueID:
+ _objc_msgSend$initWithUniqueID:
+ _objc_msgSend$initialiseLimits:
+ _objc_msgSend$isAODDisabled
+ _objc_msgSend$isFactorDisabled
+ _objc_msgSend$isFrontLuxSatisfied
+ _objc_msgSend$isGrimaldiLuxInUse
+ _objc_msgSend$isOtherALSDisabled
+ _objc_msgSend$isPropertyDisabled
+ _objc_msgSend$newColorSampleConditionWeightedForServices:
+ _objc_msgSend$newColorSampleLogWeightedForServices:
+ _objc_msgSend$newColorSampleWinnerTakesAllForServices:
+ _objc_msgSend$null
+ _objc_msgSend$readerWithService:andPlane:
+ _objc_msgSend$requestBrightnessTransactionForDisplayUUID:builtIn:
+ _objc_msgSend$selectedServices
+ _objc_msgSend$sensorIsSampling
+ _objc_msgSend$setAodDisabled:
+ _objc_msgSend$setFactorDisabled:
+ _objc_msgSend$setFrontLux:
+ _objc_msgSend$setGrimaldiLuxInUse:
+ _objc_msgSend$setOtherALSDisabled:
+ _objc_msgSend$setPropertyDisabled:
+ _objc_msgSend$shouldUseRLux:rLux:inUse:
+ _objc_msgSend$uniqueId
+ _snprintf
+ _strcmp
- +[CBHandle globalHandle]
- -[AABRear checkSensorEnablementConditions:]
- -[AABRear evaluateSamplingFrequencyWithLux:andCap:]
- -[AABRear shouldUseRLux:rLux:]
- -[AABRear shouldUseRearLuxFrontLux:rearLux:andCap:]
- -[AABRear startSampling]
- -[AABRear started]
- -[BrightnessSystemClientInternal setProperty:forKey:error:]
- -[CBColorFilter acknowledgeHIDEvent:from:]
- -[CBColorFilter newColorSampleConditionWeighted]
- -[CBColorFilter newColorSampleLogWeighted]
- -[CBColorFilter newColorSampleWinnerTakesAll]
- -[CBDisplayContaineriOS initWithBacklightService:andSystemContext:]
- -[CBHandle initGlobal]
- -[CBIndicatorBrightnessModule getDCPRoleIDFromString]
- -[CBSBIM initialiseLimits]
- GCC_except_table135
- GCC_except_table139
- GCC_except_table142
- GCC_except_table191
- GCC_except_table42
- _OBJC_IVAR_$_AABRear._activationFLux
- _OBJC_IVAR_$_AABRear._lastFrequency
- _OBJC_IVAR_$_AABRear._sensorEnabled
- _OBJC_IVAR_$_AABRear._shouldUseRearLux
- _OBJC_IVAR_$_AABRear._started
- _OBJC_IVAR_$_CBColorModuleShared._alsSelectionPolicy
- _OBJC_IVAR_$_VMBLControl._cachedBrightnessTransactions
- __ZGVZ106-[CBSBIM updateMitigationStateWithData:andCurrentHeadroom:andRequestedHeadroom:andSDRBrightness:andReset:]E23previousAccumulatedSBIM
- __ZN4AABC21_UpdateEsensorTrustedEf
- __ZN4AABC25evaluateAABRearConditionsEv
- __ZNSt3__18valarrayIfEC2ERKfm
- __ZNSt3__18valarrayIfED1Ev
- __ZZ106-[CBSBIM updateMitigationStateWithData:andCurrentHeadroom:andRequestedHeadroom:andSDRBrightness:andReset:]E23previousAccumulatedSBIM
- ___42-[CBColorFilter acknowledgeHIDEvent:from:]_block_invoke
- ___42-[CBColorFilter newColorSampleLogWeighted]_block_invoke
- ___45-[CBColorFilter newColorSampleWinnerTakesAll]_block_invoke
- ___48-[CBColorFilter newColorSampleConditionWeighted]_block_invoke
- ___59-[BrightnessSystemClientInternal setProperty:forKey:error:]_block_invoke
- ___cxa_atexit
- ___cxa_guard_abort
- _get_type_metadata 15Synchronization5MutexVySo9CPMSAgentCG noncopyable
- _objc_msgSend$acknowledgeHIDEvent:from:
- _objc_msgSend$checkSensorEnablementConditions:
- _objc_msgSend$evaluateSamplingFrequencyWithLux:andCap:
- _objc_msgSend$getDCPRoleIDFromString
- _objc_msgSend$initGlobal
- _objc_msgSend$initialiseLimits
- _objc_msgSend$newColorSampleConditionWeighted
- _objc_msgSend$newColorSampleLogWeighted
- _objc_msgSend$newColorSampleWinnerTakesAll
- _objc_msgSend$setProperty:forKey:error:
- _objc_msgSend$shouldUseRLux:rLux:
- _objc_msgSend$shouldUseRearLuxFrontLux:rearLux:andCap:
- _objc_msgSend$startSampling
- _swift_runtimeSupportsNoncopyableTypes
- _swift_willThrowTypedImpl
- _syslog
CStrings:
+ "%s failed to find matching display"
+ ", "
+ "<%@: sdrParams=(lux=%.4f, nits=%.4f, c=%.4f) hdrParams=(lux=%.4f, nits=%.4f, c=%.4f) lumFactor=%.4f maxBoost=%.1f boosting=%d>"
+ "Adjusting AAB curve for preference point: %s (pre-clamped lux: %f, unscaled nits: %f)"
+ "BrightnessTransactionRequest"
+ "Capabilities were likely late! Not restoring %@ property"
+ "ContentHeadroom"
+ "Created contrast indicator policy: %@"
+ "Display(%@)"
+ "Display(unknown)"
+ "Failed to get child iterator err = %#x (%s)"
+ "Failed to get child node's name err = %#x (%s)"
+ "Grimaldi conditions no longer satisfied, stopping sampling"
+ "Grimaldi conditions satisfied, requesting samples"
+ "Grimaldi conditions: AOD: %d, Factor: %d, Property: %d, other ALS: %d, Front Lux Satisfied: %d, luxInUse: %s"
+ "IODeviceTree:/exbright"
+ "Nits for clamped lux: %f is: %f (unscaled nits: %f)"
+ "ShouldUseRearLuxFrontLux(fLux:%.2f, rLux:%.2f) = %s -> %s"
+ "Using clamped lux = %f as input to AAB (pre-clamped lux = %f)"
+ "VM Requesting brightness transaction for displayUUID:%@ builtIn:%d"
+ "com.apple.CoreBrightness.CBALSSelectionPolicy.%@.%d"
+ "com.apple.CoreBrightness.ColorEffects"
+ "contrast-indicator"
+ "id: %lu"
+ "key=%@ value=%@ handle=%@"
+ "occlusion-drives-grimaldi"
+ "selection policy dropped sample; preserving last sample (mode %lu)"
+ "selectionPolicy refresh: service %lu event overridden with policy-provided cached event. Lux %.2f -> %.2f"
+ "uniqueID: %@"
+ "uniqueID: (null)"
+ "uniqueId"
+ "uuid: %@"
- "%s failed to find matching display, saving transaction"
- "Adjusting AAB curve for preference point: %s (uncapped lux: %f, unscaled nits: %f"
- "Grimaldi; { \"aod_forbidden\": %d, \"factor_forbidden\": %d, \"property_forbidden\": %d, \"isStarted\": %d, \"state_change\": \"%@\" }"
- "Nits for lux: %f is: %f (unscaled nits: %f"
- "ShouldUseRearLuxFrontLux(fLux:%.2f, rLux:%.2f, cap: %.2f) = %s"
- "ShouldUseRearLuxFrontLux(fLux:%.2f, rLux:%.2f, cap: %.2f) = %s -> %s"
- "com.apple.CoreBrightness.CBALSSelectionPolicy.%d"
- "starting"
- "stopping"

```
