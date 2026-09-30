## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-2300.1.2.0.0
-  __TEXT.__text: 0x15faf4
-  __TEXT.__objc_methlist: 0xd31c
-  __TEXT.__const: 0x127a0
-  __TEXT.__oslogstring: 0x185dd
-  __TEXT.__cstring: 0xcdc5
-  __TEXT.__gcc_except_tab: 0x1fc8
+2300.40.37.0.0
+  __TEXT.__text: 0x161ce0
+  __TEXT.__objc_methlist: 0xd5d0
+  __TEXT.__cstring: 0xcf55
+  __TEXT.__const: 0x12790
+  __TEXT.__gcc_except_tab: 0x1fd8
+  __TEXT.__oslogstring: 0x186ad
   __TEXT.__dlopen_cstrs: 0x10d
   __TEXT.__swift5_typeref: 0xeaf
   __TEXT.__constg_swiftt: 0xc34

   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x7470
+  __TEXT.__unwind_info: 0x7558
   __TEXT.__eh_frame: 0xb90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11d8
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x338
+  __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x56c8
+  __DATA_CONST.__objc_selrefs: 0x5800
   __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x5b8
+  __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xb90
   __DATA_CONST.__got: 0x760
-  __AUTH_CONST.__const: 0x5860
-  __AUTH_CONST.__cfstring: 0xe5c0
-  __AUTH_CONST.__objc_const: 0x34b28
+  __AUTH_CONST.__const: 0x5990
+  __AUTH_CONST.__cfstring: 0xe780
+  __AUTH_CONST.__objc_const: 0x359c0
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xcd8
-  __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__auth_got: 0x1288
-  __AUTH.__objc_data: 0x2680
+  __AUTH_CONST.__objc_dictobj: 0x5f0
+  __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH_CONST.__auth_got: 0x1290
+  __AUTH.__objc_data: 0x2770
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0x1768
-  __DATA.__data: 0x66f50
+  __DATA.__objc_ivar: 0x17ac
+  __DATA.__data: 0x66fb0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x21e8
   __DATA_DIRTY.__data: 0x510

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8200
-  Symbols:   12859
-  CStrings:  4652
+  Functions: 8269
+  Symbols:   13008
+  CStrings:  4673
 
Symbols:
+ +[CBDisplayBrightnessClient copyNSNumberForKey:client:handle:andError:]
+ +[CBRampProfileSpring defaultSpringProfile]
+ -[BLControl callBlockWithProperty:value:origin:]
+ -[BLControl clearKeyboardSet]
+ -[BLControl clearPILSet]
+ -[BacklightDriverPWM _setNits:withFadeSpeed:minPWMPercentage:completion:]
+ -[BacklightDriverPWM initWithBacklightService:configuration:]
+ -[BacklightDriverPWM initWithConfiguration:]
+ -[BacklightDriverPWM setNits:withFadeSpeed:minPWMPercentage:]
+ -[CBCEModule copyCachedInferenceForEvent:]
+ -[CBCEModule invalidateInferenceCache]
+ -[CBCEModule shouldRunInferenceAtTime:]
+ -[CBColorModuleShared CEModulePropertyHandler:key:]
+ -[CBColorPolicyFilter colorAdaptationActive]
+ -[CBColorPolicyFilter setColorAdaptationActive:]
+ -[CBDarwinStateNotifier dealloc]
+ -[CBDarwinStateNotifier initWithNotificationName:logCategory:]
+ -[CBDarwinStateNotifier publishState:]
+ -[CBDisplayBrightnessClient currentSDRNitsWithError:]
+ -[CBDisplayBrightnessClient maxSDRDisplayNitsWithError:]
+ -[CBDisplayStatusBroadcaster activate]
+ -[CBDisplayStatusBroadcaster cancel]
+ -[CBDisplayStatusBroadcaster dealloc]
+ -[CBDisplayStatusBroadcaster displayModeProvidersUpdate:]
+ -[CBDisplayStatusBroadcaster initWithDisplayManager:]
+ -[CBDisplayStatusBroadcaster reevaluateAndNotify]
+ -[CBDisplayStatusBroadcaster sendNotificationForKey:value:origin:]
+ -[CBIndicatorBrightnessModule currentTimeUs]
+ -[CBIndicatorBrightnessModule shouldHintSILOnForEventTimestampUs:]
+ -[CBRampManager insertNewRampOrigin:target:length:frequency:identifier:profile:]
+ -[CBRampManager insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:]
+ -[CBRampProfileLinear normalizedOutputForProgress:]
+ -[CBRampProfileSpring _cacheNormalizer]
+ -[CBRampProfileSpring _springValAtT:]
+ -[CBRampProfileSpring damping]
+ -[CBRampProfileSpring init]
+ -[CBRampProfileSpring initialVelocity]
+ -[CBRampProfileSpring mass]
+ -[CBRampProfileSpring normalizedOutputForProgress:]
+ -[CBRampProfileSpring setDamping:]
+ -[CBRampProfileSpring setInitialVelocity:]
+ -[CBRampProfileSpring setMass:]
+ -[CBRampProfileSpring setStiffness:]
+ -[CBRampProfileSpring stiffness]
+ -[CBRingLight resetUserAdjustmentState]
+ -[CBRingLight statusInfo]
+ -[NightModeControl stop]
+ -[PWMCalibrationManager convertNitsToPWMPercentage:minPWMPercentage:]
+ -[PWMDeviceController setEnabled:commit:applyEnablePulse:]
+ -[VMBLControl addDisplayModuleForBrightnessControlProxy:]
+ -[VMBLControl sendBrightnessTransactionRequestForDisplayUUID:builtIn:]
+ -[VMBLControl sendBrightnessTransactionRequestOnQueueForDisplayUUID:builtIn:]
+ -[VMBLControl sendHeadroomRequestOnQueue:forDisplayUUID:builtIn:]
+ -[VMDisplayModule setPropertyOnQueue:forKey:]
+ CBU_IsDisplayStatusAggregationEnabled
+ CBU_IsDisplayStatusAggregationEnabled.once
+ CBU_IsDisplayStatusAggregationEnabled.result
+ GCC_except_table149
+ GCC_except_table211
+ GCC_except_table46
+ OBJC_IVAR_$_CBCEModule._cachedResult
+ OBJC_IVAR_$_CBCEModule._cadenceSeconds
+ OBJC_IVAR_$_CBCEModule._lastInferenceTime
+ OBJC_IVAR_$_CBColorPolicyFilter._ceModelID
+ OBJC_IVAR_$_CBColorPolicyFilter._colorAdaptationActive
+ OBJC_IVAR_$_CBDarwinStateNotifier._logHandle
+ OBJC_IVAR_$_CBDarwinStateNotifier._name
+ OBJC_IVAR_$_CBDarwinStateNotifier._token
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._displayOnByDisplay
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._hasPublished
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._lastPublishedState
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._logHandle
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._manager
+ OBJC_IVAR_$_CBDisplayStatusBroadcaster._notifier
+ OBJC_IVAR_$_CBRampProfileSpring._damping
+ OBJC_IVAR_$_CBRampProfileSpring._initialVelocity
+ OBJC_IVAR_$_CBRampProfileSpring._mass
+ OBJC_IVAR_$_CBRampProfileSpring._normalizer
+ OBJC_IVAR_$_CBRampProfileSpring._stiffness
+ OBJC_IVAR_$_CBRingLight._overriddenByUser
+ _CBU_IsDisplayStatusAggregationEnabled
+ _DisplayGetBrightnessAfterForcedDynamicSliderRestriction
+ _OBJC_CLASS_$_CBDarwinStateNotifier
+ _OBJC_CLASS_$_CBDisplayStatusBroadcaster
+ _OBJC_CLASS_$_CBRampProfileLinear
+ _OBJC_CLASS_$_CBRampProfileSpring
+ _OBJC_METACLASS_$_CBDarwinStateNotifier
+ _OBJC_METACLASS_$_CBDisplayStatusBroadcaster
+ _OBJC_METACLASS_$_CBRampProfileLinear
+ _OBJC_METACLASS_$_CBRampProfileSpring
+ __73-[BacklightDriverPWM _setNits:withFadeSpeed:minPWMPercentage:completion:]_block_invoke
+ __CLASS_METHODS_CBCoexTracker
+ __OBJC_$_CLASS_METHODS_CBRampProfileSpring
+ __OBJC_$_INSTANCE_METHODS_CBDarwinStateNotifier
+ __OBJC_$_INSTANCE_METHODS_CBDisplayStatusBroadcaster
+ __OBJC_$_INSTANCE_METHODS_CBRampProfileLinear
+ __OBJC_$_INSTANCE_METHODS_CBRampProfileSpring
+ __OBJC_$_INSTANCE_VARIABLES_CBDarwinStateNotifier
+ __OBJC_$_INSTANCE_VARIABLES_CBDisplayStatusBroadcaster
+ __OBJC_$_INSTANCE_VARIABLES_CBRampProfileSpring
+ __OBJC_$_PROP_LIST_CBDarwinStateNotifier
+ __OBJC_$_PROP_LIST_CBDisplayStatusBroadcaster
+ __OBJC_$_PROP_LIST_CBRampProfileLinear
+ __OBJC_$_PROP_LIST_CBRampProfileSpring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBRampProfile
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBStateNotifier
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBRampProfile
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBStateNotifier
+ __OBJC_$_PROTOCOL_REFS_CBRampProfile
+ __OBJC_$_PROTOCOL_REFS_CBStateNotifier
+ __OBJC_CLASS_PROTOCOLS_$_CBDarwinStateNotifier
+ __OBJC_CLASS_PROTOCOLS_$_CBDisplayStatusBroadcaster
+ __OBJC_CLASS_PROTOCOLS_$_CBRampProfileLinear
+ __OBJC_CLASS_PROTOCOLS_$_CBRampProfileSpring
+ __OBJC_CLASS_RO_$_CBDarwinStateNotifier
+ __OBJC_CLASS_RO_$_CBDisplayStatusBroadcaster
+ __OBJC_CLASS_RO_$_CBRampProfileLinear
+ __OBJC_CLASS_RO_$_CBRampProfileSpring
+ __OBJC_LABEL_PROTOCOL_$_CBRampProfile
+ __OBJC_LABEL_PROTOCOL_$_CBStateNotifier
+ __OBJC_METACLASS_RO_$_CBDarwinStateNotifier
+ __OBJC_METACLASS_RO_$_CBDisplayStatusBroadcaster
+ __OBJC_METACLASS_RO_$_CBRampProfileLinear
+ __OBJC_METACLASS_RO_$_CBRampProfileSpring
+ __OBJC_PROTOCOL_$_CBRampProfile
+ __OBJC_PROTOCOL_$_CBStateNotifier
+ __ZN4AABC13setTrustedALSEPNS_3ALSE
+ __ZN4AABC20logTrustedALSSummaryEPNS_3ALSE
+ ___24-[BLControl clearPILSet]_block_invoke
+ ___29-[BLControl clearKeyboardSet]_block_invoke
+ ___29-[VMDisplayModule invalidate]_block_invoke
+ ___45-[VMDisplayModule setPropertyOnQueue:forKey:]_block_invoke
+ ___58-[VMBLControl sendHeadroomRequest:forDisplayUUID:builtIn:]_block_invoke
+ ___70-[VMBLControl sendBrightnessTransactionRequestForDisplayUUID:builtIn:]_block_invoke
+ ___73-[BacklightDriverPWM _setNits:withFadeSpeed:minPWMPercentage:completion:]_block_invoke
+ ___90-[CBRampManager insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:]_block_invoke
+ ___CBU_IsDisplayStatusAggregationEnabled_block_invoke
+ ___DisplayApplyDynamicSliderRestriction
+ ____ZN4AABC20logTrustedALSSummaryEPNS_3ALSE_block_invoke
+ ___block_descriptor_40_e8_32o_e45_v32?08"CBKeyboardBacklightContainer"16^B24l
+ ___block_descriptor_40_e8_32o_e71_v32?08"CBContainer<CBContainerProtocol><CBHIDServiceProtocol>"16^B24l
+ ___block_descriptor_49_e8_32o40o_e5_v8?0l
+ ___block_descriptor_56_e8_32o_e35_v24?0^{__IOHIDServiceClient=}8^v16l
+ ___block_descriptor_57_e8_32o40o48o_e5_v8?0l
+ ___block_descriptor_58_e8_32s40bs_e5_v8?0l
+ ___sincosf_stret
+ _interpolate_value_in_table
+ _kCBSPIBrightnessCommitUpdate
+ _kCBSPIBrightnessCommitUpdateNitsFinal
+ _kCBSPIBrightnessCommitUpdateNitsInitial
+ _load_mapping_table_from_defaults
+ _mapping_table_is_valid
+ _objc_msgSend$CEModulePropertyHandler:key:
+ _objc_msgSend$_cacheNormalizer
+ _objc_msgSend$_setNits:withFadeSpeed:minPWMPercentage:completion:
+ _objc_msgSend$_springValAtT:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$bootNits
+ _objc_msgSend$brightnessCommitUpdate:
+ _objc_msgSend$callBlockWithProperty:value:origin:
+ _objc_msgSend$clearKeyboardSet
+ _objc_msgSend$clearPILSet
+ _objc_msgSend$coexDescription:
+ _objc_msgSend$convertNitsToPWMPercentage:minPWMPercentage:
+ _objc_msgSend$copyCachedInferenceForEvent:
+ _objc_msgSend$copyNSNumberForKey:client:handle:andError:
+ _objc_msgSend$currentTimeUs
+ _objc_msgSend$getBrightnessCapabilities
+ _objc_msgSend$hasAnyCoexForALS:type:
+ _objc_msgSend$initWithIdentifier:configuration:
+ _objc_msgSend$initWithNotificationName:logCategory:
+ _objc_msgSend$insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:
+ _objc_msgSend$invalidateInferenceCache
+ _objc_msgSend$normalizedOutputForProgress:
+ _objc_msgSend$resetUserAdjustmentState
+ _objc_msgSend$sendBrightnessTransactionRequestOnQueueForDisplayUUID:builtIn:
+ _objc_msgSend$sendHeadroomRequestOnQueue:forDisplayUUID:builtIn:
+ _objc_msgSend$setColorAdaptationActive:
+ _objc_msgSend$setEnabled:commit:applyEnablePulse:
+ _objc_msgSend$setPropertyOnQueue:forKey:
+ _objc_msgSend$shouldHintSILOnForEventTimestampUs:
+ _objc_msgSend$shouldRunInferenceAtTime:
+ _objc_msgSend$string
+ _save_mapping_table_to_defaults
- -[BLControl callBlockWithProperty:value:]
- -[CBColorModuleShared CEOverridePropertyHandler:key:]
- -[CBDarwinBrightnessLevelNotifier dealloc]
- -[CBDarwinBrightnessLevelNotifier init]
- -[CBDarwinBrightnessLevelNotifier publishState:]
- -[CBRingLight getStatusInfo]
- -[VMBLControl requestBrightnessTransactionForDisplayUUID:builtIn:]
- GCC_except_table144
- GCC_except_table210
- GCC_except_table54
- GCC_except_table62
- OBJC_IVAR_$_CBDarwinBrightnessLevelNotifier._logHandle
- OBJC_IVAR_$_CBDarwinBrightnessLevelNotifier._token
- OBJC_IVAR_$_CBRingLight._overridenByUser
- _OBJC_CLASS_$_CBDarwinBrightnessLevelNotifier
- _OBJC_METACLASS_$_CBDarwinBrightnessLevelNotifier
- __55-[BacklightDriverPWM setNits:withFadeSpeed:completion:]_block_invoke
- __DisplayGetDeviceBrightnessAfterDynamicSliderAdjustment
- __OBJC_$_INSTANCE_METHODS_CBDarwinBrightnessLevelNotifier
- __OBJC_$_INSTANCE_VARIABLES_CBDarwinBrightnessLevelNotifier
- __OBJC_$_PROP_LIST_CBDarwinBrightnessLevelNotifier
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBBrightnessLevelNotifier
- __OBJC_$_PROTOCOL_METHOD_TYPES_CBBrightnessLevelNotifier
- __OBJC_$_PROTOCOL_REFS_CBBrightnessLevelNotifier
- __OBJC_CLASS_PROTOCOLS_$_CBDarwinBrightnessLevelNotifier
- __OBJC_CLASS_RO_$_CBDarwinBrightnessLevelNotifier
- __OBJC_LABEL_PROTOCOL_$_CBBrightnessLevelNotifier
- __OBJC_METACLASS_RO_$_CBDarwinBrightnessLevelNotifier
- __OBJC_PROTOCOL_$_CBBrightnessLevelNotifier
- ___55-[BacklightDriverPWM setNits:withFadeSpeed:completion:]_block_invoke
- ___block_descriptor_54_e8_32s40bs_e5_v8?0l
- _objc_msgSend$CEOverridePropertyHandler:key:
- _objc_msgSend$callBlockWithProperty:value:
- _objc_msgSend$requestBrightnessTransactionForDisplayUUID:builtIn:
- _objc_msgSend$terminateConnection:
CStrings:
+ "BrightnessCommitUpdate"
+ "BrightnessLevelNotifier"
+ "CECadence"
+ "DisplayStatusNotifier"
+ "Enabling device without enable pulse"
+ "Harmony supported?? %d"
+ "HarmonyShiftA"
+ "HarmonyShiftB"
+ "HarmonyStrength"
+ "Ignoring negative CE cadence %f"
+ "OverriddenByUser"
+ "SIL OFF @ %llu us (was ON for %llu us)"
+ "SIL ON @ %llu us"
+ "Setting CE inference cadence to %f s"
+ "TrueTone: shift-a = %f, shift-b = %f"
+ "Trusted ALS updated: %{public}@"
+ "[%@]cached strength: %.2f, confidence: %f"
+ "[BRT update: %s]: Begin slider drag"
+ "[Color Mitigation] lux=%.1f nits=%.1f mitigated=%d ceEnabled=%d ttActive=%d ceAttempted=%d source=%s confidence=%.3f threshold=%.3f crossedThreshold=%d strength=%.3f"
+ "[SIL Hint] Received MIB while SIL OFF, turning SIL ON... (mibTs=%llu, lastSILOffTs=%llu)"
+ "_S=%f"
+ "com.apple.CoreBrightness.BacklightDriverPWM"
+ "com.apple.CoreBrightness.DisplayStatusBroadcaster"
+ "com.apple.iokit.hid.displayStatus"
+ "dropping departed display %{public}@"
+ "no valid token for %@; dropping state=%llu"
+ "notify_post failed for %@ (status=%u)"
+ "notify_set_state failed for %@ (status=%u)"
+ "orient=%d lux=%.2f coex=%@"
+ "publishing display status state=%llu"
+ "seeding displayID=%lu on=%d"
+ "truetone-shift-a"
+ "truetone-shift-b"
+ "trusted={%@} "
+ "v32@?0@8@\"CBContainer<CBContainerProtocol><CBHIDServiceProtocol>\"16^B24"
+ "v32@?0@8@\"CBKeyboardBacklightContainer\"16^B24"
+ "{%@} "
- "Can't talk to PWM driver. Return code = %d"
- "OverridenByUser"
- "SIL OFF @ %f us (was ON for %f us)"
- "SIL ON @ %f us"
- "[%x]: _S=%f"
- "[CPMS] Current SDR brightness updated: %f -> %f"
- "[Color Mitigation] lux=%.1f nits=%.1f mitigated=%d ceEnabled=%d ceAttempted=%d source=%s confidence=%.3f threshold=%.3f crossedThreshold=%d strength=%.3f"
- "[SIL Hint] Received MIB while SIL OFF, turning SIL ON..."
- "[SIL Hint] now=%f motMet=%d shouldUseHint=%d"
- "com.apple.CoreBrightness.BrightnessLevelNotifier"
- "error: unknown notification type (%@)"
- "failed to terminate SKL client (%@)"
- "harmony HW not supported"
- "harmony HW supported"
- "key=%@ (type=%tu) value=%@  block=%p queue=%p"
- "key=%@ property=%@ queue=%p clientBlock=%p"
```
