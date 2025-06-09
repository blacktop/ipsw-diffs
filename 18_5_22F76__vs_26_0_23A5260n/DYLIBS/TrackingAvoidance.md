## TrackingAvoidance

> `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance`

```diff

-107.0.3.0.0
-  __TEXT.__text: 0x483d4
+107.0.6.0.0
+  __TEXT.__text: 0x48c0c
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x45f0
-  __TEXT.__const: 0x340
-  __TEXT.__oslogstring: 0x6b0f
-  __TEXT.__cstring: 0x2ddb
-  __TEXT.__gcc_except_tab: 0x5cc
-  __TEXT.__unwind_info: 0xd00
+  __TEXT.__objc_methlist: 0x465c
+  __TEXT.__const: 0x348
+  __TEXT.__oslogstring: 0x7009
+  __TEXT.__cstring: 0x2e3b
+  __TEXT.__gcc_except_tab: 0x5d4
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__objc_classname: 0x77a
-  __TEXT.__objc_methname: 0xcba6
-  __TEXT.__objc_methtype: 0x1231
-  __TEXT.__objc_stubs: 0x74e0
+  __TEXT.__objc_methname: 0xcd70
+  __TEXT.__objc_methtype: 0x1264
+  __TEXT.__objc_stubs: 0x75e0
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21d0
+  __DATA_CONST.__objc_selrefs: 0x2210
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x4740
-  __AUTH_CONST.__objc_const: 0x84d0
+  __AUTH_CONST.__cfstring: 0x47a0
+  __AUTH_CONST.__objc_const: 0x8538
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x614
+  __DATA.__objc_ivar: 0x61c
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 692E0256-8C45-30D5-B50A-2CEE76E464B8
-  Functions: 1513
-  Symbols:   5337
-  CStrings:  3501
+  UUID: 425FC8DE-5371-3940-B7E4-6F64832B449C
+  Functions: 1521
+  Symbols:   5365
+  CStrings:  3528
 
Symbols:
+ -[TADeviceRecord getNumSurfacedAlerts:]
+ -[TADeviceRecord limitSuspiciousDevicesSentToObservers:forDailyMaximum:]
+ -[TASingleDeviceRecord numPotentialSurfacedAlerts]
+ -[TASingleDeviceRecord setNumPotentialSurfacedAlerts:]
+ -[TATrackingAvoidanceService debugStageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:]
+ -[TATrackingAvoidanceService debugStageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:].cold.1
+ -[TATrackingAvoidanceService getDailyAlertLimitPerAccessory]
+ -[TATrackingAvoidanceServiceManager debugStageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:]
+ -[TATrackingAvoidanceServiceManager debugStageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:].cold.1
+ -[TATrackingAvoidanceServiceSettings dailyAccessoryAlertLimit]
+ -[TATrackingAvoidanceServiceSettings initWithEnableTAFilterGeneral:enableTAFilterVisits:enableTAFilterSingleVisit:enableTAFilterLeavingLOI:classificationTimeInterval:dailyAccessoryAlertLimit:]
+ -[TATrackingAvoidanceServiceSettings initWithEnableTAFilterGeneralOrDefault:enableTAFilterVisitsOrDefault:enableTAFilterSingleVisitOrDefault:enableTAFilterLeavingLOIOrDefault:classificationTimeIntervalOrDefault:dailyAccessoryAlertLimitOrDefault:]
+ _OBJC_IVAR_$_TASingleDeviceRecord._numPotentialSurfacedAlerts
+ _OBJC_IVAR_$_TATrackingAvoidanceServiceSettings._dailyAccessoryAlertLimit
+ _objc_msgSend$dailyAccessoryAlertLimit
+ _objc_msgSend$debugStageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:
+ _objc_msgSend$getDailyAlertLimitPerAccessory
+ _objc_msgSend$getNumSurfacedAlerts:
+ _objc_msgSend$initWithEnableTAFilterGeneral:enableTAFilterVisits:enableTAFilterSingleVisit:enableTAFilterLeavingLOI:classificationTimeInterval:dailyAccessoryAlertLimit:
+ _objc_msgSend$initWithEnableTAFilterGeneralOrDefault:enableTAFilterVisitsOrDefault:enableTAFilterSingleVisitOrDefault:enableTAFilterLeavingLOIOrDefault:classificationTimeIntervalOrDefault:dailyAccessoryAlertLimitOrDefault:
+ _objc_msgSend$limitSuspiciousDevicesSentToObservers:forDailyMaximum:
+ _objc_msgSend$numPotentialSurfacedAlerts
+ _objc_msgSend$setNumPotentialSurfacedAlerts:
+ _objc_msgSend$unsignedLongValue
- -[TATrackingAvoidanceService debugStageTADetection:deviceType:detailsBitmask:].cold.1
- -[TATrackingAvoidanceServiceSettings initWithEnableTAFilterGeneral:enableTAFilterVisits:enableTAFilterSingleVisit:enableTAFilterLeavingLOI:classificationTimeInterval:]
- -[TATrackingAvoidanceServiceSettings initWithEnableTAFilterGeneralOrDefault:enableTAFilterVisitsOrDefault:enableTAFilterSingleVisitOrDefault:enableTAFilterLeavingLOIOrDefault:classificationTimeIntervalOrDefault:]
- _objc_msgSend$initWithEnableTAFilterGeneral:enableTAFilterVisits:enableTAFilterSingleVisit:enableTAFilterLeavingLOI:classificationTimeInterval:
- _objc_msgSend$initWithEnableTAFilterGeneralOrDefault:enableTAFilterVisitsOrDefault:enableTAFilterSingleVisitOrDefault:enableTAFilterLeavingLOIOrDefault:classificationTimeIntervalOrDefault:
CStrings:
+ "#TAStore unreachable state; in-order TAEvent should be added already: %{sensitive}s"
+ "@48@0:8B16B20B24B28d32Q40"
+ "TAServiceDailyAlertLimit"
+ "TQ,N,V_numPotentialSurfacedAlerts"
+ "TQ,R,N,V_dailyAccessoryAlertLimit"
+ "TrackingAvoidance"
+ "UT2025"
+ "_dailyAccessoryAlertLimit"
+ "_numPotentialSurfacedAlerts"
+ "dailyAccessoryAlertLimit"
+ "debugStageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:"
+ "getDailyAlertLimitPerAccessory"
+ "getNumSurfacedAlerts:"
+ "initWithEnableTAFilterGeneral:enableTAFilterVisits:enableTAFilterSingleVisit:enableTAFilterLeavingLOI:classificationTimeInterval:dailyAccessoryAlertLimit:"
+ "initWithEnableTAFilterGeneralOrDefault:enableTAFilterVisitsOrDefault:enableTAFilterSingleVisitOrDefault:enableTAFilterLeavingLOIOrDefault:classificationTimeIntervalOrDefault:dailyAccessoryAlertLimitOrDefault:"
+ "limitSuspiciousDevicesSentToObservers:forDailyMaximum:"
+ "nPotentialSurfaced"
+ "numPotentialSurfacedAlerts"
+ "setNumPotentialSurfacedAlerts:"
+ "unsignedLongValue"
+ "v40@0:8@\"NSData\"16Q24I32B36"
+ "v40@0:8@16Q24I32B36"
+ "{\"msg%{public}.0s\":\"#TADeviceRecord all detections have reached daily surfacing limit; not surfacing any new alerts\", \"numThrottledSuspiciousDevices\":%{public}lu, \"numSuspiciousDevices\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#TADeviceRecord no detections have reached daily surfacing limit; not throttling\", \"numThrottledSuspiciousDevices\":%{public}lu, \"numSuspiciousDevices\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#TADeviceRecord number of staged and potential alerts for device record\", \"singleDeviceRecord\":\"%{private}@\", \"numSurfacedAlerts\":%{private}lu, \"numPotentialSurfacedAlerts\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#TADeviceRecord suppressed alerting for some detections due to daily alert limit\", \"numThrottledSuspiciousDevices\":%{public}lu, \"numSuspiciousDevices\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#TATrackingAvoidanceService reporting suspicious devices\", \"stagedDetectionsReadyForSubmission\":%{private}lu, \"dedupedStagedDetectionsReadyForSubmission\":%{private}lu, \"nonIssuedDedupedStagedDetectionsReadyForSubmission\":%{private}lu, \"allUnfilteredSuspiciousDevices\":%{private}lu, \"dailyAlertLimitFilteredDetectionWithHistoricalObservations\":%{private}lu, \"detectionWithHistoricalObservations\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#TATrackingAvoidanceService start stageTADetection for\", \"address\":\"%{private}@\", \"shouldRemoveSingleDeviceRecord\":%{public}hhd}"
- "#TAStore unreacheable state; in-order TAEvent should be added already: %{sensitive}s"
- "#TATrackingAvoidanceService start stageTADetection for address: %{private}@ "
- "@40@0:8B16B20B24B28d32"
- "initWithEnableTAFilterGeneral:enableTAFilterVisits:enableTAFilterSingleVisit:enableTAFilterLeavingLOI:classificationTimeInterval:"
- "initWithEnableTAFilterGeneralOrDefault:enableTAFilterVisitsOrDefault:enableTAFilterSingleVisitOrDefault:enableTAFilterLeavingLOIOrDefault:classificationTimeIntervalOrDefault:"

```
