## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-  __TEXT.__text: 0x15d2f0
-  __TEXT.__objc_methlist: 0xcf34
-  __TEXT.__cstring: 0xcdda
-  __TEXT.__const: 0x16e08
-  __TEXT.__gcc_except_tab: 0x1eec
-  __TEXT.__oslogstring: 0x1797d
+  __TEXT.__text: 0x15fbf8
+  __TEXT.__objc_methlist: 0xd02c
+  __TEXT.__cstring: 0xcada
+  __TEXT.__const: 0x138d0
+  __TEXT.__gcc_except_tab: 0x1f10
+  __TEXT.__oslogstring: 0x1816a
   __TEXT.__dlopen_cstrs: 0x10d
-  __TEXT.__swift5_typeref: 0xeb6
+  __TEXT.__swift5_typeref: 0xeb0
   __TEXT.__constg_swiftt: 0xc2c
-  __TEXT.__swift5_reflstr: 0xa44
+  __TEXT.__swift5_reflstr: 0xa3c
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_fieldmd: 0x100c
   __TEXT.__swift5_builtin: 0xdc

   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x5230
+  __TEXT.__unwind_info: 0x5290
   __TEXT.__eh_frame: 0xb88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__const: 0x1190
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5500
+  __DATA_CONST.__objc_selrefs: 0x5590
   __DATA_CONST.__objc_protorefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x5a0
   __DATA_CONST.__objc_arraydata: 0xba0
-  __DATA_CONST.__got: 0x6b0
-  __AUTH_CONST.__const: 0x5848
-  __AUTH_CONST.__cfstring: 0xe260
-  __AUTH_CONST.__objc_const: 0x33478
+  __DATA_CONST.__got: 0x768
+  __AUTH_CONST.__const: 0x5880
+  __AUTH_CONST.__cfstring: 0xe3a0
+  __AUTH_CONST.__objc_const: 0x33648
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1280
-  __AUTH.__objc_data: 0x1ea0
-  __AUTH.__data: 0x7f0
-  __DATA.__objc_ivar: 0x16f4
-  __DATA.__data: 0x5a668
-  __DATA.__bss: 0x63f0
+  __AUTH_CONST.__auth_got: 0x1278
+  __AUTH.__objc_data: 0x2590
+  __AUTH.__data: 0x628
+  __DATA.__objc_ivar: 0x1708
+  __DATA.__data: 0x5a670
+  __DATA.__bss: 0x63e0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x28d8
-  __DATA_DIRTY.__data: 0x340
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__objc_data: 0x21e8
+  __DATA_DIRTY.__data: 0x510
+  __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreDisplay.framework/Versions/A/CoreDisplay
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8072
-  Symbols:   15307
-  CStrings:  6394
+  Functions: 8120
+  Symbols:   15406
+  CStrings:  6433
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ +[CBDisplayHandle handleForUniqueID:]
+ +[CBDisplayHandle handleWithDisplayID:andUUID:andUniqueID:]
+ -[BacklightDriverPWM bootNits]
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
+ -[PWMDeviceController _loadHardwareRange]
+ -[PWMDeviceController _updateHardwareRangeWithClock:]
+ -[VMBLControl requestBrightnessTransactionForDisplayUUID:builtIn:]
+ CFXAmmoliteDisable
+ CFXAnimateAmbientAdaptationModes
+ CFXInputAmbientColor
+ CFXSetAmbientAdaptationStrength
+ CFXSetNativeWhitePoint
+ CFXSetOutputFormat
+ CFXSetWeakestAmbientAdaptationMode
+ CFXSetWhitePointType
+ CFXUpdateColorFade
+ GCC_except_table53
+ GCC_except_table55
+ OBJC_IVAR_$_CBALSNode._occlusionDrivesGrimaldi
+ OBJC_IVAR_$_CBColorFilter._arrivedEvents
+ OBJC_IVAR_$_CBColorFilter._selectionPolicy
+ OBJC_IVAR_$_CBColorModuleShared._firstALSSelectionPolicy
+ OBJC_IVAR_$_CBDisplayHandle._cachedDescription
+ OBJC_IVAR_$_CBSBIM._previousAccumulatedSBIM
+ OBJC_IVAR_$_PWMDeviceController._pwmFrequencyLoaded
+ _CFXCheckStats
+ _CFXGetTarget
+ _CFXLogHandle.log
+ _CFXLogHandle.once
+ _CFXSetNativeWhitePointCorrection
+ _CFXUpdateColorFadeInternal
+ _IORegistryEntryGetChildIterator
+ _OBJC_CLASS_$_NSNull
+ _ZN4AABC21_UpdateEsensorTrustedEfNSt3__18optionalIfEE
+ __30-[BacklightDriverPWM bootNits]_block_invoke
+ __54-[CBColorFilter newColorSampleLogWeightedForServices:]_block_invoke
+ __OBJC_$_INSTANCE_VARIABLES_CBDisplayHandle
+ __ZN36PerceptualLuminanceThresholding_1nit15SetBoolPropertyEP8NSStringb
+ __ZN38PerceptualLuminanceThresholding_legacy15SetBoolPropertyEP8NSStringb
+ __ZN4AABC21_UpdateEsensorTrustedEfNSt3__18optionalIfEE
+ ___30-[BacklightDriverPWM bootNits]_block_invoke
+ ___34-[CBColorFilter acknowledgeEvent:]_block_invoke
+ ___54-[CBColorFilter newColorSampleLogWeightedForServices:]_block_invoke
+ ___57-[CBColorFilter newColorSampleWinnerTakesAllForServices:]_block_invoke
+ ___60-[CBColorFilter newColorSampleConditionWeightedForServices:]_block_invoke
+ ___63-[BrightnessSystemClientInternal setSyncProperty:forKey:error:]_block_invoke
+ ____CFXLogHandle_block_invoke
+ _kCBKeyDisplayUniqueID
+ _objc_msgSend$_loadHardwareRange
+ _objc_msgSend$_updateHardwareRangeWithClock:
+ _objc_msgSend$acknowledgeEvent:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$copyDescription
+ _objc_msgSend$defaultSoftBoundaryConfiguration
+ _objc_msgSend$findContrastIndicatorNodeForContext:
+ _objc_msgSend$getDCPRoleIDFromContext:
+ _objc_msgSend$getOcclusionDrivesGrimaldi
+ _objc_msgSend$handleForUniqueID:
+ _objc_msgSend$initWithContext:min:max:maxBoost:andFrameInfoProvider:
+ _objc_msgSend$initWithDisplayID:andUUID:andUniqueID:
+ _objc_msgSend$initWithUniqueID:
+ _objc_msgSend$initialiseLimits:
+ _objc_msgSend$newColorSampleConditionWeightedForServices:
+ _objc_msgSend$newColorSampleLogWeightedForServices:
+ _objc_msgSend$newColorSampleWinnerTakesAllForServices:
+ _objc_msgSend$null
+ _objc_msgSend$requestBrightnessTransactionForDisplayUUID:builtIn:
+ _objc_msgSend$selectedServices
+ _objc_msgSend$useEnablePulse
+ _snprintf
+ _strcmp
+ ansiBinFromChromaticity
+ binFromAb
- +[CBHandle globalHandle]
- -[BrightnessSystemClientInternal setProperty:forKey:error:]
- -[CBColorFilter acknowledgeHIDEvent:from:]
- -[CBColorFilter newColorSampleConditionWeighted]
- -[CBColorFilter newColorSampleLogWeighted]
- -[CBColorFilter newColorSampleWinnerTakesAll]
- -[CBHandle initGlobal]
- -[CBIndicatorBrightnessModule getDCPRoleIDFromString]
- -[CBSBIM initialiseLimits]
- GCC_except_table52
- OBJC_IVAR_$_CBColorModuleShared._alsSelectionPolicy
- OBJC_IVAR_$_VMBLControl._cachedBrightnessTransactions
- _ZN4AABC21_UpdateEsensorTrustedEf
- __42-[CBColorFilter newColorSampleLogWeighted]_block_invoke
- __ZGVZ106-[CBSBIM updateMitigationStateWithData:andCurrentHeadroom:andRequestedHeadroom:andSDRBrightness:andReset:]E23previousAccumulatedSBIM
- __ZN14CoreBrightnessL11sbimLimits1E
- __ZN14CoreBrightnessL11sbimLimits2E
- __ZN14CoreBrightnessL11sbimLimits3E
- __ZN14CoreBrightnessL11sbimLimits4E
- __ZN14CoreBrightnessL11sbimLimits5E
- __ZN14CoreBrightnessL11sbimLimits6E
- __ZN14CoreBrightnessL13sbimLimitsD4yE
- __ZN14CoreBrightnessL13sbimLimitsD9xE
- __ZN14CoreBrightnessL16sbimLimitsV5zD23E
- __ZN4AABC21_UpdateEsensorTrustedEf
- __ZNSt3__18valarrayIfED1Ev
- __ZZ106-[CBSBIM updateMitigationStateWithData:andCurrentHeadroom:andRequestedHeadroom:andSDRBrightness:andReset:]E23previousAccumulatedSBIM
- ___42-[CBColorFilter acknowledgeHIDEvent:from:]_block_invoke
- ___42-[CBColorFilter newColorSampleLogWeighted]_block_invoke
- ___45-[CBColorFilter newColorSampleWinnerTakesAll]_block_invoke
- ___48-[CBColorFilter newColorSampleConditionWeighted]_block_invoke
- ___59-[BrightnessSystemClientInternal setProperty:forKey:error:]_block_invoke
- ___cxa_atexit
- ___cxa_guard_abort
- _objc_msgSend$acknowledgeHIDEvent:from:
- _objc_msgSend$displayUUID
- _objc_msgSend$getDCPRoleIDFromString
- _objc_msgSend$initGlobal
- _objc_msgSend$initialiseLimits
- _objc_msgSend$newColorSampleConditionWeighted
- _objc_msgSend$newColorSampleLogWeighted
- _objc_msgSend$newColorSampleWinnerTakesAll
- _objc_msgSend$setProperty:forKey:error:
- _swift_runtimeSupportsNoncopyableTypes
- _swift_willThrowTypedImpl
- _syslog$DARWIN_EXTSN
- get_type_metadata 15Synchronization5MutexVySo9CPMSAgentCG noncopyable
CStrings:
+ "%s failed to find matching display"
+ ", "
+ "<%@: sdrParams=(lux=%.4f, nits=%.4f, c=%.4f) hdrParams=(lux=%.4f, nits=%.4f, c=%.4f) lumFactor=%.4f maxBoost=%.1f boosting=%d>"
+ "Adjusting AAB curve for preference point: %s (pre-clamped lux: %f, unscaled nits: %f)"
+ "BrightnessTransactionRequest"
+ "ContentHeadroom"
+ "Display(%@)"
+ "Display(unknown)"
+ "Failed to get child iterator err = %#x (%s)"
+ "Failed to get child node's name err = %#x (%s)"
+ "IODeviceTree:/exbright"
+ "Load hardware range: min=%llu, max=%llu"
+ "Nits for clamped lux: %f is: %f (unscaled nits: %f)"
+ "Using clamped lux = %f as input to AAB (pre-clamped lux = %f)"
+ "VM Requesting brightness transaction for displayUUID:%@ builtIn:%d"
+ "_loadHardwareRange: pwm-frequency still unavailable."
+ "_updateHardwareRangeWithClock: _frequency is 0, cannot compute hardware range"
+ "_updateHardwareRangeWithClock: period is 0 (clock=%llu, freq=%llu), cannot compute hardware range"
+ "boot Nits: %@ → %.2f%% → %.2f nits"
+ "boot Nits: failed to open IODeviceTree:/options"
+ "boot Nits: failed to parse hex value from NVRAM string: %@"
+ "boot Nits: no boot DC found in NVRAM"
+ "com.apple.CoreBrightness.CBALSSelectionPolicy.%@.%d"
+ "com.apple.CoreBrightness.ColorEffects"
+ "contrast-indicator"
+ "enablePulseRoutine: device already enabled, skipping"
+ "id: %lu"
+ "key=%@ value=%@ handle=%@"
+ "occlusion-drives-grimaldi"
+ "pwm-frequency not yet available; using default clock %llu"
+ "selection policy dropped sample; preserving last sample (mode %lu)"
+ "selectionPolicy refresh: service %lu event overridden with policy-provided cached event. Lux %.2f -> %.2f"
+ "uniqueID: %@"
+ "uniqueID: (null)"
+ "useEnablePulse=YES; skipping initial setNits"
+ "uuid: %@"
- "%s failed to find matching display, saving transaction"
- "Adjusting AAB curve for preference point: %s (uncapped lux: %f, unscaled nits: %f"
- "IODeviceTree:/exbright/contrast-indicator"
- "Nits for lux: %f is: %f (unscaled nits: %f"
- "PWM min, max = %llu, %llu (period = %llu)"
- "Replaying %lu cached brightness transaction(s)"
- "com.apple.CoreBrightness.CBALSSelectionPolicy.%d"

```
