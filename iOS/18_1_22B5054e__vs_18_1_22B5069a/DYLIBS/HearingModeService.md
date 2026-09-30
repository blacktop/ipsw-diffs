## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`

```diff

-21.13.3.1.3
-  __TEXT.__text: 0x11b4c
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x1174
+21.16.1.4.0
+  __TEXT.__text: 0x122ec
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0x11b0
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x3f1c
+  __TEXT.__cstring: 0x4152
   __TEXT.__gcc_except_tab: 0x180
   __TEXT.__unwind_info: 0x378
-  __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methname: 0x4d0d
-  __TEXT.__objc_methtype: 0x859
-  __TEXT.__objc_stubs: 0x1ec0
+  __TEXT.__objc_classname: 0x127
+  __TEXT.__objc_methname: 0x4e43
+  __TEXT.__objc_methtype: 0x886
+  __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x590
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb8
+  __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x2e10
+  __AUTH_CONST.__cfstring: 0x13a0
+  __AUTH_CONST.__objc_const: 0x2ec0
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x2a8
+  __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 421
-  Symbols:   542
-  CStrings:  1377
+  Functions: 426
+  Symbols:   548
+  CStrings:  1426
 
Symbols:
+ _CUMetricsLog
+ _HMOcclusionResultIsOverallPassing
CStrings:
+ "\x01\x11\x11\x11\xf0_\x02"
+ "-[HMDeviceDiagnosticRecord _prefsLoadOcclusionStats]"
+ "-[HMDeviceDiagnosticRecord _prefsResetOcclusionStatsForFeatureID:type:]"
+ "-[HMDeviceDiagnosticRecord _prefsSaveOcclusionStats]"
+ "ActiveNotificationNotShown"
+ "B24@0:8i16i20"
+ "CleaningAlertNotShown"
+ "DiagnosticMeasurementCount"
+ "FirmwareVersion"
+ "FirstTimeOfUse"
+ "HMDeviceDiagnosticRecord UUID %!@(MISSING), read occlusion stats from prefs: %!@(MISSING)"
+ "HMDeviceDiagnosticRecord UUID %!@(MISSING), resetOcclusionStats for feature: type %!s(MISSING)"
+ "HPActiveNotificationCount"
+ "HPActiveNotificationFirstTimestamp"
+ "HPPlacardCount"
+ "HPPlacardFirstTimestamp"
+ "HTCleaningAlertFirstTimestamp"
+ "HearingProtectionOcclusionResult"
+ "HearingTestOcclusionResult"
+ "IndicationAction"
+ "IndicationType"
+ "LeftBottomMicFaultCount"
+ "LeftFreqAccFaultCount"
+ "LeftFrontVentFaultCount"
+ "LeftInnerMicFaultCount"
+ "LeftRearVentFaultCount"
+ "LeftSpeakerFaultCount"
+ "LeftTHDFaultCount"
+ "LeftTopMicFaultCount"
+ "PlacardNotShown"
+ "ProductID"
+ "RightBottomMicFaultCount"
+ "RightFreqAccFaultCount"
+ "RightFrontVentFaultCount"
+ "RightInnerMicFaultCount"
+ "RightRearVentFaultCount"
+ "RightSpeakerFaultCount"
+ "RightTHDFaultCount"
+ "RightTopMicFaultCount"
+ "TB,N,V_cloudRecordLoaded"
+ "TimeSinceFirstIndication"
+ "_cloudRecordLoaded"
+ "_firmwareVersion"
+ "_hpActiveNotificationCount"
+ "_hpActiveNotificationFirstTimestamp"
+ "_hpPlacardCount"
+ "_hpPlacardFirstTimestamp"
+ "_htCleaningAlertFirstTimestamp"
+ "_minutesSinceTimestamp:"
+ "_prefsLoadOcclusionStats"
+ "_prefsResetOcclusionStatsForFeatureID:type:"
+ "_prefsSaveOcclusionStats"
+ "_resetAllOcclusionStats"
+ "_submitMetricsForOcclusionIndicationType:action:previousIndicationCount:timeSinceFirstIndicationMins:"
+ "cloudRecordLoaded"
+ "com.apple.AirPods.occlusion.indication"
+ "firmwareVersion"
+ "minute"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "previousIndicationCount"
+ "q24@0:8@16"
+ "setCloudRecordLoaded:"
+ "submitMetricsForOcclusionPolicy"
+ "v36@0:8i16i20I24q28"
- "\x11\xf0o\x02"
- "-[HMDeviceDiagnosticRecord _loadOcclusionStatsFromPrefs]"
- "-[HMDeviceDiagnosticRecord _resetOcclusionStatsForFeatureID:]"
- "-[HMDeviceDiagnosticRecord _saveOcclusionStatsToPrefs]"
- "-[HMServiceClient occlusionIndicationShownForDeviceIdentifier:featureID:type:action:]_block_invoke"
- "FirstHTCleaningAlertTime"
- "HMDeviceDiagnosticRecord UUID %!@(MISSING), read occlusion stats from prefs: HT time %!@(MISSING), HT count %!d(MISSING)"
- "HMDeviceDiagnosticRecord UUID %!@(MISSING), resetOcclusionStats - no stats available for feature %!s(MISSING)"
- "HMDeviceDiagnosticRecord UUID %!@(MISSING), resetOcclusionStats for feature: %!s(MISSING)"
- "NoIndication"
- "_firstHTCleaningAlertTime"
- "_loadOcclusionStatsFromPrefs"
- "_resetOcclusionStatsForFeatureID:"
- "_saveOcclusionStatsToPrefs"
- "clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:"
- "occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"

```
