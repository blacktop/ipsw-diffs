## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-170.0.0.0.0
-  __TEXT.__text: 0x36fcdc
+173.0.0.0.0
+  __TEXT.__text: 0x373ca0
   __TEXT.__auth_stubs: 0x1840
   __TEXT.__objc_stubs: 0x9480
   __TEXT.__objc_methlist: 0x8d98
-  __TEXT.__gcc_except_tab: 0x10560
-  __TEXT.__const: 0xfcbe
-  __TEXT.__cstring: 0x1c922
-  __TEXT.__oslogstring: 0x11b5f
+  __TEXT.__gcc_except_tab: 0x105bc
+  __TEXT.__const: 0xfcde
+  __TEXT.__cstring: 0x1cb71
+  __TEXT.__oslogstring: 0x11c3b
   __TEXT.__objc_classname: 0x1070
-  __TEXT.__objc_methtype: 0x5f74
+  __TEXT.__objc_methtype: 0x601d
   __TEXT.__objc_methname: 0xc220
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc840
+  __TEXT.__unwind_info: 0xc858
   __TEXT.__eh_frame: 0x670
   __DATA_CONST.__const: 0x28848
-  __DATA_CONST.__cfstring: 0x6a60
+  __DATA_CONST.__cfstring: 0x6a00
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17220
+  Functions: 17223
   Symbols:   608
-  CStrings:  9354
+  CStrings:  9381
 
CStrings:
+ "[PU] config-1,%f,config-2,%f,config-3,%f,config-4,%d,config-5,%f,config-6,%f,config-7,%d,config-8,%f,config-9,%f,config-10,%d,config-11,%f,config-12,%f,config-13,%f,config-14,%f,config-15,%f,config-16,%d,config-17,%f,config-18,%f"
+ "[PU] stiction detected: axis %d, %llu us above %f g"
+ "[PU] summary,%{public}d,A,%{public}f,B,%{public}f,C,%{public}llu,D,%{public}f,E,%{public}f,F,%{public}f,G,%{public}f,H,%{public}f,I,%{public}f,J,%{public}f,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}f,O,%{public}f,P,%{public}llu,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}d,config-5,%{public}f,config-6,%{public}f,config-7,%{public}d,config-8,%{public}f,config-9,%{public}f,config-10,%{public}d,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}d,config-17,%{public}f,config-18,%{public}f,debug-1,%{public}llu,debug-2,%{public}llu,debug-3,%{public}d,debug-4,%{public}d,debug-5,%{public}d,debug-6,%{public}d"
+ "adhrHeartRate"
+ "adhrHeartRateConfidence"
+ "epochsWithInsufficientHGForStiction"
+ "epochsWithStiction"
+ "epochsWithoutStiction"
+ "groupADeltaVThreshold1"
+ "groupADeltaVThreshold2"
+ "groupAMaxAccelNormThreshold"
+ "groupAPeakPressure"
+ "groupAShortAudioNumThreshold"
+ "groupAZgTimeThreshold"
+ "groupApplied"
+ "groupBDeltaVThreshold1"
+ "groupBDeltaVThreshold2"
+ "groupBMaxAccelNormThreshold"
+ "groupBPeakPressure"
+ "groupBShortAudioNumThreshold"
+ "groupBZgTimeThreshold"
+ "groupIsA"
+ "invalid stiction status"
+ "scaledADHRMets"
+ "stictionDuration"
+ "stictionStatus"
+ "stictionThreshold"
+ "v200@0:8{KappaSessionDetails=fCiiiiiiiiifffiiiiiiiiiiiiiiiiiiBiQQQBBBBqI}16"
+ "zgIsAHStateStable"
+ "zgIsFreefallA"
+ "zgIsFreefallB"
+ "zgMetaTotalZgTimeA"
+ "zgMetaTotalZgTimeB"
+ "zgSelectedVariant"
+ "zgSettledAHState"
+ "zgUsedSettledState"
+ "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"epochsWithStiction\"i\"epochsWithoutStiction\"i\"epochsWithInsufficientHGForStiction\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"numDeescalationCrashClassifier\"i\"numInertDeescalationCrashClassifier\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q\"deescalationBitmap\"I}"
+ "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"epochsWithStiction\"i\"epochsWithoutStiction\"i\"epochsWithInsufficientHGForStiction\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q\"deescalationBitmap\"I}"
- "[PU] config-1,%f,config-2,%f,config-3,%f,config-4,%d,config-5,%f,config-6,%f,config-7,%d,config-8,%f,config-9,%f,config-10,%d,config-11,%f,config-12,%f,config-13,%f,config-14,%f,config-15,%f,config-16,%d"
- "[PU] summary,%{public}d,A,%{public}f,B,%{public}f,C,%{public}llu,D,%{public}f,E,%{public}f,F,%{public}f,G,%{public}f,H,%{public}f,I,%{public}f,J,%{public}f,K,%{public}f,L,%{public}f,M,%{public}f,N,%{public}f,O,%{public}f,P,%{public}llu,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}d,config-5,%{public}f,config-6,%{public}f,config-7,%{public}d,config-8,%{public}f,config-9,%{public}f,config-10,%{public}d,config-11,%{public}f,config-12,%{public}f,config-13,%{public}f,config-14,%{public}f,config-15,%{public}f,config-16,%{public}d,debug-1,%{public}llu,debug-2,%{public}llu"
- "pu-A"
- "pu-B"
- "pu-C"
- "pu-D"
- "pu-E"
- "pu-config-1"
- "v192@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiiiBiQQQBBBBqI}16"
- "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"numDeescalationCrashClassifier\"i\"numInertDeescalationCrashClassifier\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q\"deescalationBitmap\"I}"
- "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q\"deescalationBitmap\"I}"
```
