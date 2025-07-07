## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

-7.0.70.0.0
-  __TEXT.__text: 0xd9dc
+7.0.75.1.0
+  __TEXT.__text: 0xda08
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x9f4
+  __TEXT.__objc_methlist: 0x9ec
   __TEXT.__const: 0xdc
-  __TEXT.__cstring: 0xab7
-  __TEXT.__oslogstring: 0x681
-  __TEXT.__gcc_except_tab: 0x470
-  __TEXT.__unwind_info: 0x570
-  __TEXT.__objc_classname: 0x299
-  __TEXT.__objc_methname: 0x12c5
-  __TEXT.__objc_methtype: 0xa7d
-  __TEXT.__objc_stubs: 0xd40
+  __TEXT.__cstring: 0xb22
+  __TEXT.__oslogstring: 0x68e
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__unwind_info: 0x558
+  __TEXT.__objc_classname: 0x298
+  __TEXT.__objc_methname: 0x1253
+  __TEXT.__objc_methtype: 0xa91
+  __TEXT.__objc_stubs: 0xd00
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__const: 0x418
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x498
+  __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_superrefs: 0xa0
   __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x29d8
-  __AUTH_CONST.__objc_doubleobj: 0x110
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_const: 0x2978
+  __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x158

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98B82C89-AFEC-3CF4-8324-534AF7897722
-  Functions: 356
-  Symbols:   1593
-  CStrings:  663
+  UUID: 06049D9B-CDF1-3A44-9ECD-321B10736A04
+  Functions: 349
+  Symbols:   1565
+  CStrings:  664
 
Symbols:
+ -[LSSController _resolveFeatures]
+ -[LSSController _resolveProvider:]
+ -[LSSMotionBasedLightSource updateTargetDirectionWithOrientation:goToRest:timestamp:]
+ -[LSSMotionBasedProvider _updateLight:motionLevel:timestamp:]
+ -[LSSMotionBasedProvider _updateReference:motionLevel:]
+ -[LSSMotionBasedProvider features]
+ -[LSSMotionBasedProvider setFeatures:]
+ -[LSSNullProvider features]
+ -[LSSNullProvider setFeatures:]
+ -[LSSPerformanceTestProvider features]
+ -[LSSPerformanceTestProvider setFeatures:]
+ -[LSSQuaternionSmoothFilter reset]
+ -[LSSResampler features]
+ -[LSSResampler setFeatures:]
+ -[LSSRotationAccumulator .cxx_destruct]
+ -[LSSRotationAccumulator init]
+ -[LSSRotationAccumulator update:]
+ -[LSSStationaryProvider features]
+ -[LSSStationaryProvider setFeatures:]
+ -[LSSTestProvider features]
+ -[LSSTestProvider setFeatures:]
+ -[LSSTimeBasedProvider features]
+ -[LSSTimeBasedProvider setFeatures:]
+ _LSSSettingsLowPerformance
+ _LSSSettingsMotionLightActivateThreshold
+ _LSSSettingsMotionLightDeactivateThreshold
+ _LSSSettingsMotionOrientationActivateThreshold
+ _LSSSettingsMotionOrientationDeactivateThreshold
+ _LSSSettingsMotionOrientationPowerA
+ _LSSSettingsMotionOrientationPowerB
+ _OBJC_CLASS_$_LSSRotationAccumulator
+ _OBJC_IVAR_$_LSSController._features
+ _OBJC_IVAR_$_LSSMotionBasedProvider._features
+ _OBJC_IVAR_$_LSSMotionBasedProvider._inMotion
+ _OBJC_IVAR_$_LSSMotionBasedProvider._lightInMotion
+ _OBJC_IVAR_$_LSSMotionBasedProvider._motionAccumulator
+ _OBJC_IVAR_$_LSSMotionBasedProvider._resumeFrame
+ _OBJC_IVAR_$_LSSNullProvider._features
+ _OBJC_IVAR_$_LSSPerformanceTestProvider._features
+ _OBJC_IVAR_$_LSSResampler._features
+ _OBJC_IVAR_$_LSSRotationAccumulator._accumulator
+ _OBJC_IVAR_$_LSSRotationAccumulator._hasValue
+ _OBJC_IVAR_$_LSSRotationAccumulator._prevValue
+ _OBJC_IVAR_$_LSSStationaryProvider._features
+ _OBJC_IVAR_$_LSSTestProvider._features
+ _OBJC_IVAR_$_LSSTimeBasedProvider._features
+ _OBJC_METACLASS_$_LSSRotationAccumulator
+ __OBJC_$_INSTANCE_METHODS_LSSRotationAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_LSSRotationAccumulator
+ __OBJC_CLASS_RO_$_LSSRotationAccumulator
+ __OBJC_METACLASS_RO_$_LSSRotationAccumulator
+ ___49-[LSSMotionBasedProvider initWithQueue:delegate:]_block_invoke.cold.3
+ ___LSSLogMotionBasedLightSource_block_invoke
+ ___block_literal_global.123
+ ___block_literal_global.153
+ ___block_literal_global.157
+ ___block_literal_global.162
+ ___block_literal_global.168
+ ___block_literal_global.173
+ _objc_msgSend$setFeatures:
- -[LSSController _resolveProviderSetting]
- -[LSSMotionBasedLightSource updateTargetDirectionWithOrientation:timestamp:]
- -[LSSMotionBasedProvider _update:timestamp:].cold.1
- -[LSSMotionBasedProvider _update:timestamp:].cold.2
- -[LSSMotionBasedProvider _update:timestamp:].cold.3
- -[LSSMotionBasedProvider _update:timestamp:].cold.4
- -[LSSMotionBasedProvider _update:timestamp:].cold.5
- -[LSSMotionBasedProvider _update:timestamp:].cold.6
- -[LSSMotionBasedProvider _update:timestamp:].cold.7
- -[LSSMotionBasedProvider observeValueForKeyPath:ofObject:change:context:]
- -[LSSMotionBasedProvider observeValueForKeyPath:ofObject:change:context:].cold.1
- -[LSSMotionBasedProvider setUseLowPower:]
- -[LSSMotionBasedProvider useLowPower]
- -[LSSNullProvider setUseLowPower:]
- -[LSSNullProvider useLowPower]
- -[LSSPerformanceTestProvider setUseLowPower:]
- -[LSSPerformanceTestProvider useLowPower]
- -[LSSResampler setUseLowPower:]
- -[LSSResampler useLowPower]
- -[LSSRotationDetector .cxx_destruct]
- -[LSSRotationDetector init]
- -[LSSRotationDetector setActivateThreshold:]
- -[LSSRotationDetector setDeactivateThreshold:]
- -[LSSRotationDetector update:]
- -[LSSRotationDetector update:].cold.1
- -[LSSRotationDetector update:].cold.2
- -[LSSRotationDetector update:].cold.3
- -[LSSRotationDetector update:].cold.4
- -[LSSStationaryProvider setUseLowPower:]
- -[LSSStationaryProvider useLowPower]
- -[LSSTestProvider setUseLowPower:]
- -[LSSTestProvider useLowPower]
- -[LSSTimeBasedProvider setUseLowPower:]
- -[LSSTimeBasedProvider useLowPower]
- _LSSSettingsMotionActivateThreshold
- _LSSSettingsMotionDeactivateThreshold
- _LSSSettingsMotionReferenceOrientationPowerA
- _LSSSettingsMotionReferenceOrientationPowerB
- _LSSSettingsMotionSettleTime
- _LSSSettingsUseLowPower
- _OBJC_CLASS_$_LSSRotationDetector
- _OBJC_IVAR_$_LSSMotionBasedProvider._heroLightDirection
- _OBJC_IVAR_$_LSSMotionBasedProvider._lastChangedFrame
- _OBJC_IVAR_$_LSSMotionBasedProvider._motionDetector
- _OBJC_IVAR_$_LSSMotionBasedProvider._referenceOrientationFiltered
- _OBJC_IVAR_$_LSSMotionBasedProvider._useLowPower
- _OBJC_IVAR_$_LSSNullProvider._useLowPower
- _OBJC_IVAR_$_LSSPerformanceTestProvider._useLowPower
- _OBJC_IVAR_$_LSSResampler._useLowPower
- _OBJC_IVAR_$_LSSRotationDetector._accumulator
- _OBJC_IVAR_$_LSSRotationDetector._activateThreshold
- _OBJC_IVAR_$_LSSRotationDetector._deactivateThreshold
- _OBJC_IVAR_$_LSSRotationDetector._hasMotion
- _OBJC_IVAR_$_LSSRotationDetector._hasValue
- _OBJC_IVAR_$_LSSRotationDetector._prevValue
- _OBJC_IVAR_$_LSSRotationDetector._rotation
- _OBJC_IVAR_$_LSSStationaryProvider._useLowPower
- _OBJC_IVAR_$_LSSTestProvider._useLowPower
- _OBJC_IVAR_$_LSSTimeBasedProvider._useLowPower
- _OBJC_METACLASS_$_LSSRotationDetector
- __OBJC_$_INSTANCE_METHODS_LSSRotationDetector
- __OBJC_$_INSTANCE_VARIABLES_LSSRotationDetector
- __OBJC_CLASS_RO_$_LSSRotationDetector
- __OBJC_METACLASS_RO_$_LSSRotationDetector
- ___21-[LSSController init]_block_invoke_3
- ___LSSLogFilters_block_invoke
- ___block_literal_global.121
- ___block_literal_global.155
- ___block_literal_global.159
- ___block_literal_global.164
- ___block_literal_global.170
- ___block_literal_global.175
- _objc_msgSend$deviceMotionUpdateInterval
- _objc_msgSend$setUseLowPower:
- _objc_msgSend$useLowPower
CStrings:
+ "!"
+ "@\"LSSRotationAccumulator\""
+ "LSSRotationAccumulator"
+ "MotionBasedLightSource"
+ "Tq,N"
+ "Tq,N,V_features"
+ "[90f]"
+ "_QuaternionFromCMAttitudeQuaternion"
+ "_features"
+ "_frameCount >= _resumeFrame"
+ "_inMotion"
+ "_lightInMotion"
+ "_motionAccumulator"
+ "_resumeFrame"
+ "disabling: assertion"
+ "features"
+ "forcing stationary: device is low performance."
+ "forcing stationary: low power mode"
+ "light activate"
+ "light deactivate"
+ "lowPerformance"
+ "motion activate"
+ "motion deactivate"
+ "motion_lightActivateThreshold"
+ "motion_lightDeactivateThreshold"
+ "motion_orientationActivateThreshold"
+ "motion_orientationDeactivateThreshold"
+ "motion_orientationPowerA"
+ "motion_orientationPowerB"
+ "q16@0:8"
+ "responsive: assertion"
+ "setFeatures:"
+ "simd_all(isfinite(r.vector))"
+ "start fade"
+ "unpausing (light)"
+ "unpausing (reference)"
+ "v24@0:8q16"
+ "\xc1"
- "\v"
- "1"
- "@\"LSSRotationDetector\""
- "Filters"
- "LSSRotationDetector"
- "TB,N"
- "TB,N,V_useLowPower"
- "[64f]"
- "_activateThreshold"
- "_deactivateThreshold"
- "_hasMotion"
- "_heroLightDirection"
- "_lastChangedFrame"
- "_motionDetector"
- "_referenceOrientationFiltered"
- "_rotation"
- "deviceMotionUpdateInterval"
- "disabling due to assertion"
- "f"
- "forcing stationary. device is low power"
- "forcing stationary: device is low power."
- "motion_activateThreshold"
- "motion_deactivateThreshold"
- "motion_directionResponsiveness"
- "motion_referenceOrientationPowerA"
- "motion_referenceOrientationPowerB"
- "motion_settleTime"
- "no motion"
- "resuming (light moving)"
- "resuming (reference)"
- "setUseLowPower:"
- "stableFramesRequiredToPause != 0"
- "updated default light direction used during low power mode"
- "useLowPower"
- "\xd1"
- "\xf0Q"

```
