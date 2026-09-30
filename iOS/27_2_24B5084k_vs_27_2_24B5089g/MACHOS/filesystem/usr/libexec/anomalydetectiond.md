## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__oslogstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-175.0.2.0.0
-  __TEXT.__text: 0x36cd50
-  __TEXT.__auth_stubs: 0x1850
+175.0.4.0.0
+  __TEXT.__text: 0x36d8c4
+  __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0x94e0
   __TEXT.__objc_methlist: 0x8e10
-  __TEXT.__gcc_except_tab: 0x10b40
-  __TEXT.__const: 0xfff6
-  __TEXT.__cstring: 0x1cbed
+  __TEXT.__gcc_except_tab: 0x10c48
+  __TEXT.__const: 0x10006
+  __TEXT.__cstring: 0x1cc93
   __TEXT.__oslogstring: 0x12559
   __TEXT.__objc_classname: 0x1079
-  __TEXT.__objc_methtype: 0x60f4
-  __TEXT.__objc_methname: 0xc275
+  __TEXT.__objc_methtype: 0x61dc
+  __TEXT.__objc_methname: 0xc2b8
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xf050
+  __TEXT.__unwind_info: 0xf0a0
   __TEXT.__eh_frame: 0x670
   __DATA_CONST.__const: 0x292d0
-  __DATA_CONST.__cfstring: 0x6a00
+  __DATA_CONST.__cfstring: 0x6aa0
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0xc40
+  __DATA_CONST.__auth_got: 0xc48
   __DATA_CONST.__got: 0x678
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA.__objc_const: 0x10760
+  __DATA.__objc_const: 0x107c0
   __DATA.__objc_selrefs: 0x3068
-  __DATA.__objc_ivar: 0x950
+  __DATA.__objc_ivar: 0x95c
   __DATA.__objc_data: 0x3020
   __DATA.__data: 0x2020
   __DATA.__common: 0x8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17302
-  Symbols:   609
-  CStrings:  9427
+  Functions: 17313
+  Symbols:   610
+  CStrings:  9438
 
Symbols:
+ __ZN6motion2fm6ClientC1ENSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEES9_iS9_PU28objcproto17OS_dispatch_queue8NSObject
+ _getpid
- __ZN6motion2fm6ClientC1EPU28objcproto17OS_dispatch_queue8NSObject
CStrings:
+ "AHStateAtDetection"
+ "AHStateAtEscalation"
+ "AHStateAtSessionStart"
+ "AHStateChangePreTrigger"
+ "AHStateMajority"
+ "[3I]"
+ "_ahEpochStateCounts"
+ "_ahStateAtCrashPending"
+ "_lastCrashTimestampSeen"
+ "com.apple.coremotion.crashdetection"
+ "com.apple.fm.motionanomalyfm.adapter"
+ "com.coremotion.anomalyfm.ctl.queue"
+ "v216@0:8{KappaSessionDetails=fCiiiiiiiiifffiiiiiiiiiiiiiiiiiiBiQQQBBBBqIiiiii}16"
+ "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"epochsWithStiction\"i\"epochsWithoutStiction\"i\"epochsWithInsufficientHGForStiction\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"numDeescalationCrashClassifier\"i\"numInertDeescalationCrashClassifier\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q\"deescalationBitmap\"I\"ahStateAtSessionStart\"i\"ahStateAtDetection\"i\"ahStateAtEscalation\"i\"ahStateChangePreTrigger\"i\"ahStateMajority\"i}"
+ "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"epochsWithStiction\"i\"epochsWithoutStiction\"i\"epochsWithInsufficientHGForStiction\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q\"deescalationBitmap\"I\"ahStateAtSessionStart\"i\"ahStateAtDetection\"i\"ahStateAtEscalation\"i\"ahStateChangePreTrigger\"i\"ahStateMajority\"i}"
- "com.coremotion.imufoundationmodel.ctl.queue"
- "v200@0:8{KappaSessionDetails=fCiiiiiiiiifffiiiiiiiiiiiiiiiiiiBiQQQBBBBqI}16"
- "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"epochsWithStiction\"i\"epochsWithoutStiction\"i\"epochsWithInsufficientHGForStiction\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"numDeescalationCrashClassifier\"i\"numInertDeescalationCrashClassifier\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q\"deescalationBitmap\"I}"
- "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"epochsWithStiction\"i\"epochsWithoutStiction\"i\"epochsWithInsufficientHGForStiction\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q\"deescalationBitmap\"I}"
```
