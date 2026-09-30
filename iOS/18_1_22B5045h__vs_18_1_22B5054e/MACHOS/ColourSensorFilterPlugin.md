## ColourSensorFilterPlugin

> `/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin`

```diff

-1835.40.24.0.0
-  __TEXT.__text: 0x10f94
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__const: 0x190
-  __TEXT.__cstring: 0xfbf
-  __TEXT.__oslogstring: 0x1772
-  __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x70
+1835.40.26.0.0
+  __TEXT.__text: 0x1397c
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__const: 0x530
+  __TEXT.__cstring: 0x11ef
+  __TEXT.__oslogstring: 0x1be9
+  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__unwind_info: 0x2f8
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__cfstring: 0x5e0
-  __DATA.__data: 0x78
+  __DATA_CONST.__const: 0x310
+  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__data: 0x80
+  __DATA.__bss: 0x80
   __DATA.__common: 0x8
-  __DATA.__bss: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 166
-  Symbols:   221
-  CStrings:  327
+  Functions: 224
+  Symbols:   283
+  CStrings:  380
 
Symbols:
+ __NSConcreteGlobalBlock
+ _CBU_IsR2RSupported
+ _CBU_IsNightShiftSupported
+ _CBU_IsSyncBrightnessTransactionsSupported
+ _MGIsDeviceOneOfType
+ _CBU_ShouldNotHandleExistingInternalDisplayAttachment
+ _powf
+ _CBU_DeviceHasGrimaldi
+ _load_integer_array_from_edt
+ _load_uint_from_edt
+ _readDataFromIOService
+ _MGGetSInt32Answer
+ _AMFDRSealingManifestCopyMultiInstanceForClass
+ _MGGetBoolAnswer
+ _get_float_from_cfdata
+ _CBU_IsSliderCommitTelemetrySupported
+ _float_equal
+ _CBU_IsSoftWakeSupported
+ _CBU_IsWatch
+ _mach_time_now_in_seconds
+ _strtol
+ __Z10find_boundPKfmfPmS1_
+ _clamp
+ _CBU_ShouldWaitForALS
+ _get_integer_from_cfdata
+ _matrix_element
+ _CBU_GetNightShiftCCTRange
+ _mach_time_now_in_milliseconds
+ _CBU_SyncDisplayStateControlSupported
+ _load_float_from_edt
+ _load_int_from_edt
+ _CBU_IsHarmonySupported
+ _CBU_ForceUpdateFrequencyAndFrameSkip
+ _create_integer_array_from_cfdata
+ _CBU_ForceFrameAfterBrightnessUpdate
+ __Z30calibrationLoadingTypeToString22CalibrationLoadingType
+ _get_int_from_bootarg
+ _load_fixed_float_from_edt
+ _mach_time_to_seconds
+ _readExactDataFromIOService
+ _CBU_IsPad
+ _convertMachToNanoSeconds
+ _CBU_IsAccessory
+ __ZN17ColorSensorPlugIn18loadFDRCalibrationEbR17CalibrationResult
+ __ZN17ColorSensorPlugIn22copyFDRCalibrationDataEPK10__CFStringR17CalibrationResulti
+ _load_float_array_from_edt
+ _mach_time_to_nanoseconds
+ _CBU_PassContrastEnhancerStrengthThroughSyncDBV
+ _CFPreferencesGetAppBooleanValue
+ _linear_interpolation
+ __Z25calibrationResultToString17CalibrationResult
+ _mach_time_to_milliseconds
+ _logf
+ __ZN17ColorSensorPlugIn15loadCalibrationEbb
+ _scaleForExponent
+ _CBU_RampLumaBoostFactorInAOD
+ _kCFPreferencesCurrentApplication
+ _strlen
+ __Z22get_uint32_from_cfdataPKvPj
+ _mach_time_now_in_nanoseconds
+ _PerceptualToLuminance
+ _dispatch_once
+ _two_dimensional_interpolation
+ _LuminanceToPerceptual
- __ZN17ColorSensorPlugIn22copyFDRCalibrationDataEPK10__CFString
- __ZN17ColorSensorPlugIn18loadFDRCalibrationEb
CStrings:
+ "als_R2R_supported"
+ "Placement"
+ "blr-cct-default"
+ "Calibration loading type was not specified.\n"
+ "Calibration overrides set to %!d(MISSING)"
+ "FORCE_HARMONY_SUPPORT"
+ "IOHIDPlacementType"
+ "found"
+ "[0x%!l(MISSING)lx] Found valid but NOT matching calibration data."
+ "CBU_IsHarmonySupported"
+ "Calibration type: %!s(MISSING), result: %!s(MISSING), sensor type: %!d(MISSING), color support: %!d(MISSING)"
+ "not found"
+ "Unmatched"
+ "als_default_calibration"
+ "FDR calibration %!{(MISSING)public}@ data %!s(MISSING) (%!s(MISSING))."
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData for key %!@(MISSING) failed with error %!@(MISSING)"
+ "[0x%!l(MISSING)lx] Found unmatched calibration data."
+ "[0x%!l(MISSING)lx] Found valid but NOT matching calibration data at index 0."
+ "R2R support is %!s(MISSING) by %!s(MISSING) = %!d(MISSING)"
+ "FDR"
+ "SynchronousDisplayStateControl"
+ "Found cached DB and matched calibration."
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData (index = %!d(MISSING)) for key %!@(MISSING) failed with error %!@(MISSING)"
+ "CalibrationResult"
+ "SysConfig"
+ "Cached DB not found."
+ "Golden (default)"
+ "RearALSCapability"
+ "failed to parse big DB"
+ "Not found"
+ "blr-cct-min"
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData for key %!@(MISSING) succeeded."
+ "[0x%!l(MISSING)lx] AMFDRSealingManifestCopyMultiInstanceForClass found %!d(MISSING) instances for key %!@(MISSING)."
+ "DeviceClassNumber"
+ "disabled"
+ "FDR first then SysConfig"
+ "[0x%!l(MISSING)lx] HmCA CFSN 0x%!l(MISSING)lx - placement match, orientation %!s(MISSING)match"
+ "Process Spectrum only"
+ "Unknown"
+ "Undefined"
+ "Use %!s(MISSING) calibration type"
+ "[0x%!l(MISSING)lx] Found matched HmCA CFSN 0x%!l(MISSING)lx"
+ "[0x%!l(MISSING)lx] Looking for non matching calibration data -> AMFDRSealingMapCopyLocalData (index = 0) for key %!@(MISSING) failed with error %!@(MISSING)"
+ "Use default calibration.\n"
+ "Unmatched calibration => do NOT use cached DB"
+ "[0x%!l(MISSING)lx] HmCA CFSN 0x%!l(MISSING)lx does not match."
+ "Found unmatched calibration."
+ "Matched"
+ "[0x%!l(MISSING)lx] None of the %!s(MISSING) calibrations found matched. %!s(MISSING)"
+ "Synchronous display state control default override -> %!i(MISSING) "
+ "als_calibration_overrides"
+ "doesn't"
+ "blr-cct-max"
+ "DeviceSupportsFrameSynchronousBrightness"
+ "F1Xz9g1JORibBS9DYPUPrg"
+ "%!s(MISSING): boot-arg to enforce harmony support"
+ "blr-cct-warning"
+ "enabled"
+ "Calibration overrides: skipSealingMapCopy = %!d(MISSING), skipSealingManifestCopy = %!d(MISSING), useUnmatched = %!d(MISSING)"
+ "Unmatched calibration was not found either."
- "HmCA CFSN 0x%!l(MISSING)lx != 0x%!l(MISSING)lx ALS CFSN"
- "None of the %!s(MISSING) calibrations found matched"
- "AMFDRSealingMapCopyLocalData for key %!@(MISSING) succeeded."
- "HmCA CFSN 0x%!l(MISSING)lx == 0x%!l(MISSING)lx ALS CFSN"
- "als_default_calibration="
- "Try happened %!d(MISSING)"
- "AMFDRSealingMapCopyLocalData for key %!@(MISSING) failed with error %!@(MISSING)"

```
