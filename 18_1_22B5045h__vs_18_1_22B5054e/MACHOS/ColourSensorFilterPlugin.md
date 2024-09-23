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
+ __Z25calibrationResultToString17CalibrationResult
+ _CBU_GetNightShiftCCTRange
+ _CBU_ShouldNotHandleExistingInternalDisplayAttachment
+ _MGGetSInt32Answer
+ _CBU_IsAccessory
+ __Z22get_uint32_from_cfdataPKvPj
+ _mach_time_now_in_milliseconds
+ _load_fixed_float_from_edt
+ __Z10find_boundPKfmfPmS1_
+ _get_int_from_bootarg
+ _linear_interpolation
+ _load_integer_array_from_edt
+ _mach_time_to_seconds
+ _strtol
+ _kCFPreferencesCurrentApplication
+ _logf
+ _CBU_PassContrastEnhancerStrengthThroughSyncDBV
+ _strlen
+ _CBU_IsSoftWakeSupported
+ _convertMachToNanoSeconds
+ _powf
+ _AMFDRSealingManifestCopyMultiInstanceForClass
+ _load_int_from_edt
+ __NSConcreteGlobalBlock
+ _get_integer_from_cfdata
+ _CBU_SyncDisplayStateControlSupported
+ _mach_time_now_in_nanoseconds
+ _create_integer_array_from_cfdata
+ _load_float_array_from_edt
+ _mach_time_to_nanoseconds
+ _LuminanceToPerceptual
+ _CBU_IsR2RSupported
+ _clamp
+ _mach_time_now_in_seconds
+ _two_dimensional_interpolation
+ _CBU_ForceUpdateFrequencyAndFrameSkip
+ _load_float_from_edt
+ _readDataFromIOService
+ _CBU_IsPad
+ _load_uint_from_edt
+ _float_equal
+ _get_float_from_cfdata
+ _CBU_ForceFrameAfterBrightnessUpdate
+ __Z30calibrationLoadingTypeToString22CalibrationLoadingType
+ __ZN17ColorSensorPlugIn22copyFDRCalibrationDataEPK10__CFStringR17CalibrationResulti
+ _CBU_IsWatch
+ __ZN17ColorSensorPlugIn15loadCalibrationEbb
+ _CBU_IsSyncBrightnessTransactionsSupported
+ _CBU_RampLumaBoostFactorInAOD
+ _PerceptualToLuminance
+ _CBU_IsHarmonySupported
+ _CFPreferencesGetAppBooleanValue
+ _dispatch_once
+ _scaleForExponent
+ _CBU_ShouldWaitForALS
+ _MGGetBoolAnswer
+ _readExactDataFromIOService
+ _CBU_DeviceHasGrimaldi
+ _matrix_element
+ __ZN17ColorSensorPlugIn18loadFDRCalibrationEbR17CalibrationResult
+ _MGIsDeviceOneOfType
+ _mach_time_to_milliseconds
+ _CBU_IsSliderCommitTelemetrySupported
+ _CBU_IsNightShiftSupported
- __ZN17ColorSensorPlugIn22copyFDRCalibrationDataEPK10__CFString
- __ZN17ColorSensorPlugIn18loadFDRCalibrationEb
CStrings:
+ "[0x%!l(MISSING)lx] Found matched HmCA CFSN 0x%!l(MISSING)lx"
+ "F1Xz9g1JORibBS9DYPUPrg"
+ "[0x%!l(MISSING)lx] HmCA CFSN 0x%!l(MISSING)lx - placement match, orientation %!s(MISSING)match"
+ "als_R2R_supported"
+ "not found"
+ "Cached DB not found."
+ "SynchronousDisplayStateControl"
+ "Calibration loading type was not specified.\n"
+ "Matched"
+ "found"
+ "CalibrationResult"
+ "Not found"
+ "FDR"
+ "[0x%!l(MISSING)lx] Found unmatched calibration data."
+ "als_default_calibration"
+ "Unmatched"
+ "Placement"
+ "SysConfig"
+ "Process Spectrum only"
+ "[0x%!l(MISSING)lx] AMFDRSealingManifestCopyMultiInstanceForClass found %!d(MISSING) instances for key %!@(MISSING)."
+ "[0x%!l(MISSING)lx] HmCA CFSN 0x%!l(MISSING)lx does not match."
+ "blr-cct-max"
+ "DeviceSupportsFrameSynchronousBrightness"
+ "[0x%!l(MISSING)lx] Looking for non matching calibration data -> AMFDRSealingMapCopyLocalData (index = 0) for key %!@(MISSING) failed with error %!@(MISSING)"
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData for key %!@(MISSING) succeeded."
+ "doesn't"
+ "FORCE_HARMONY_SUPPORT"
+ "Calibration overrides: skipSealingMapCopy = %!d(MISSING), skipSealingManifestCopy = %!d(MISSING), useUnmatched = %!d(MISSING)"
+ "disabled"
+ "[0x%!l(MISSING)lx] Found valid but NOT matching calibration data at index 0."
+ "%!s(MISSING): boot-arg to enforce harmony support"
+ "Calibration overrides set to %!d(MISSING)"
+ "[0x%!l(MISSING)lx] None of the %!s(MISSING) calibrations found matched. %!s(MISSING)"
+ "Calibration type: %!s(MISSING), result: %!s(MISSING), sensor type: %!d(MISSING), color support: %!d(MISSING)"
+ "blr-cct-warning"
+ "Undefined"
+ "Found cached DB and matched calibration."
+ "als_calibration_overrides"
+ "Golden (default)"
+ "IOHIDPlacementType"
+ "CBU_IsHarmonySupported"
+ "RearALSCapability"
+ "Use default calibration.\n"
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData (index = %!d(MISSING)) for key %!@(MISSING) failed with error %!@(MISSING)"
+ "FDR calibration %!{(MISSING)public}@ data %!s(MISSING) (%!s(MISSING))."
+ "[0x%!l(MISSING)lx] Found valid but NOT matching calibration data."
+ "Unknown"
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData for key %!@(MISSING) failed with error %!@(MISSING)"
+ "Unmatched calibration => do NOT use cached DB"
+ "Synchronous display state control default override -> %!i(MISSING) "
+ "enabled"
+ "FDR first then SysConfig"
+ "Found unmatched calibration."
+ "blr-cct-min"
+ "Use %!s(MISSING) calibration type"
+ "R2R support is %!s(MISSING) by %!s(MISSING) = %!d(MISSING)"
+ "Unmatched calibration was not found either."
+ "DeviceClassNumber"
+ "blr-cct-default"
+ "failed to parse big DB"
- "AMFDRSealingMapCopyLocalData for key %!@(MISSING) succeeded."
- "HmCA CFSN 0x%!l(MISSING)lx == 0x%!l(MISSING)lx ALS CFSN"
- "als_default_calibration="
- "Try happened %!d(MISSING)"
- "None of the %!s(MISSING) calibrations found matched"
- "AMFDRSealingMapCopyLocalData for key %!@(MISSING) failed with error %!@(MISSING)"
- "HmCA CFSN 0x%!l(MISSING)lx != 0x%!l(MISSING)lx ALS CFSN"

```
