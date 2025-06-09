## HeartHealth

> `/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x19650
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x2214
+6074.1.2.4.0
+  __TEXT.__text: 0x19870
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0x225c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x23a5
-  __TEXT.__oslogstring: 0xe51
-  __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__unwind_info: 0x820
+  __TEXT.__cstring: 0x2404
+  __TEXT.__oslogstring: 0xe45
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__unwind_info: 0x830
   __TEXT.__objc_classname: 0x7f2
-  __TEXT.__objc_methname: 0x6b06
-  __TEXT.__objc_methtype: 0xc79
-  __TEXT.__objc_stubs: 0x3740
+  __TEXT.__objc_methname: 0x6c0b
+  __TEXT.__objc_methtype: 0xc8d
+  __TEXT.__objc_stubs: 0x3820
   __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0xaa0
+  __DATA_CONST.__const: 0xab0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1588
+  __DATA_CONST.__objc_selrefs: 0x15c0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x20e0
+  __AUTH_CONST.__cfstring: 0x2140
   __AUTH_CONST.__objc_const: 0x4100
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86475F0B-DA6A-3499-A14E-A567C2B07F10
-  Functions: 825
-  Symbols:   2983
-  CStrings:  1707
+  UUID: DD96339F-B4CA-3216-84FE-7E1C4C81FFFE
+  Functions: 832
+  Symbols:   3006
+  CStrings:  1721
 
Symbols:
+ +[_HKHeartSettingsUtilities _setThresholdHeartRate:detectedEnabledDefaultsKey:thresholdHeartRateDefaultKey:userDefaults:]
+ +[_HKHeartSettingsUtilities bradycardiaThresholdHeartRateWithDefaults:]
+ +[_HKHeartSettingsUtilities isBradycardiaDetectionEnabledWithDefaults:]
+ +[_HKHeartSettingsUtilities isTachycardiaDetectionEnabledWithDefaults:]
+ +[_HKHeartSettingsUtilities setBradycardiaThresholdHeartRate:defaults:]
+ +[_HKHeartSettingsUtilities setTachycardiaThresholdHeartRate:defaults:]
+ +[_HKHeartSettingsUtilities tachycardiaThresholdHeartRateWithDefaults:]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs protectedDataOperationRunDate]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs setProtectedDataOperationRunDate:]
+ _HKHRAFibBurdenOnboardingDateOverride
+ _HKHRAFibBurdenOnboardingDateOverrideKey
+ _HKLogHeartRateCategory
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_IVAR_$_HKHRAFibBurdenSevenDayAnalysisBreadcrumbs._protectedDataOperationRunDate
+ ___HKHRAFibBurdenDetermineIsFocusModeOn_block_invoke.302
+ ___HKHRAFibBurdenDetermineIsFocusModeOn_block_invoke.302.cold.1
+ ___HKHRAFibBurdenDetermineIsFocusModeOn_block_invoke.302.cold.2
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.310
+ ___block_literal_global.328
+ ___block_literal_global.337
+ _kHKHRAFibBurdenRescindedNotificationCategoryIdentifier
+ _objc_msgSend$ComputedMode
+ _objc_msgSend$UserFocus
+ _objc_msgSend$_setThresholdHeartRate:detectedEnabledDefaultsKey:thresholdHeartRateDefaultKey:userDefaults:
+ _objc_msgSend$bradycardiaThresholdHeartRateWithDefaults:
+ _objc_msgSend$isBradycardiaDetectionEnabledWithDefaults:
+ _objc_msgSend$isTachycardiaDetectionEnabledWithDefaults:
+ _objc_msgSend$protectedDataOperationRunDate
+ _objc_msgSend$publisher
+ _objc_msgSend$setBradycardiaThresholdHeartRate:defaults:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setTachycardiaThresholdHeartRate:defaults:
+ _objc_msgSend$starting
+ _objc_msgSend$tachycardiaThresholdHeartRateWithDefaults:
- +[_HKHeartSettingsUtilities _setThresholdHeartRate:detectedEnabledDefaultsKey:thresholdHeartRateDefaultKey:]
- -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs initWithAlarmFiredDate:xpcActivityFiredDate:maintenanceOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:]
- -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs maintenanceOperationRunDate]
- -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs setMaintenanceOperationRunDate:]
- _OBJC_CLASS_$_BMStreams
- _OBJC_IVAR_$_HKHRAFibBurdenSevenDayAnalysisBreadcrumbs._maintenanceOperationRunDate
- ___HKHRAFibBurdenDetermineIsFocusModeOn_block_invoke.299
- ___HKHRAFibBurdenDetermineIsFocusModeOn_block_invoke.299.cold.1
- ___HKHRAFibBurdenDetermineIsFocusModeOn_block_invoke.299.cold.2
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.325
- ___block_literal_global.334
- _objc_msgSend$_setThresholdHeartRate:detectedEnabledDefaultsKey:thresholdHeartRateDefaultKey:
- _objc_msgSend$isStarting
- _objc_msgSend$maintenanceOperationRunDate
- _objc_msgSend$numberForKey:error:
- _objc_msgSend$publisherFromStartTime:
- _objc_msgSend$userFocusComputedMode
CStrings:
+ "ComputedMode"
+ "HKHRAFibBurdenOnboardingDateOverride"
+ "HeartAppPlugin.AFibBurden.Rescinded"
+ "ProtectedDataOperationRunDateKey"
+ "T@\"NSDate\",&,N,V_protectedDataOperationRunDate"
+ "UserFocus"
+ "[%{public}s]: Prompted for IRN's 'enabled' state, but setting is missing or invalid; reporting 'off'"
+ "_protectedDataOperationRunDate"
+ "_setThresholdHeartRate:detectedEnabledDefaultsKey:thresholdHeartRateDefaultKey:userDefaults:"
+ "bradycardiaThresholdHeartRateWithDefaults:"
+ "initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:"
+ "isBradycardiaDetectionEnabledWithDefaults:"
+ "isTachycardiaDetectionEnabledWithDefaults:"
+ "protectedDataOperationRunDate"
+ "publisher"
+ "setBradycardiaThresholdHeartRate:defaults:"
+ "setDateFormat:"
+ "setProtectedDataOperationRunDate:"
+ "setTachycardiaThresholdHeartRate:defaults:"
+ "starting"
+ "tachycardiaThresholdHeartRateWithDefaults:"
+ "v48@0:8@16@24@32@40"
+ "yyyy-MM-dd HH:mm:ss"
- "MaintenanceOperationRunDateKey"
- "T@\"NSDate\",&,N,V_maintenanceOperationRunDate"
- "[%{public}s]: Prompted for IRN's 'enabled' state, but setting is missing or invalid; reporting 'off': %{public}@"
- "_maintenanceOperationRunDate"
- "_setThresholdHeartRate:detectedEnabledDefaultsKey:thresholdHeartRateDefaultKey:"
- "initWithAlarmFiredDate:xpcActivityFiredDate:maintenanceOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:"
- "isStarting"
- "maintenanceOperationRunDate"
- "numberForKey:error:"
- "publisherFromStartTime:"
- "setMaintenanceOperationRunDate:"
- "userFocusComputedMode"

```
