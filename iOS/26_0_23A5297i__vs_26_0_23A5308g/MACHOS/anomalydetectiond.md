## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-145.0.3.0.0
-  __TEXT.__text: 0x34fd6c
+145.0.5.0.0
+  __TEXT.__text: 0x350060
   __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_stubs: 0x9140
-  __TEXT.__objc_methlist: 0x8c40
-  __TEXT.__gcc_except_tab: 0x111ec
+  __TEXT.__objc_stubs: 0x9160
+  __TEXT.__objc_methlist: 0x8c48
+  __TEXT.__gcc_except_tab: 0x11234
   __TEXT.__const: 0x92fe
-  __TEXT.__cstring: 0x1a533
-  __TEXT.__oslogstring: 0xffe4
+  __TEXT.__cstring: 0x1a6d3
+  __TEXT.__oslogstring: 0x100bf
   __TEXT.__objc_classname: 0x10a6
-  __TEXT.__objc_methtype: 0x5d48
-  __TEXT.__objc_methname: 0xbe6c
+  __TEXT.__objc_methtype: 0x5d7b
+  __TEXT.__objc_methname: 0xbe86
   __TEXT.__ustring: 0x10ae
   __TEXT.__unwind_info: 0xbe18
   __TEXT.__eh_frame: 0x590

   __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x22d50
-  __DATA_CONST.__cfstring: 0x64a0
+  __DATA_CONST.__cfstring: 0x6620
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xff28
-  __DATA.__objc_selrefs: 0x2f70
+  __DATA.__objc_selrefs: 0x2f78
   __DATA.__objc_ivar: 0x930
   __DATA.__objc_data: 0x2f80
   __DATA.__data: 0x2010

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2F3511C4-B344-33C6-A969-36AC7105371D
-  Functions: 15892
+  UUID: 1F5781D2-D0AF-3438-9440-B4BBE220AEBE
+  Functions: 15895
   Symbols:   567
-  CStrings:  9711
+  CStrings:  9739
 
CStrings:
+ "CSKappaHighSenseCrashTokenCount"
+ "CSKappaHighSenseCrashTokenCountDefault"
+ "CSKappaHighSenseCrashTokenReplenishPeriod"
+ "CSKappaHighSenseCrashTokenReplenishTimestamp"
+ "CSKappaLowSenseCrashTokenCount"
+ "CSKappaLowSenseCrashTokenCountDefault"
+ "CSKappaLowSenseCrashTokenReplenishPeriod"
+ "CSKappaLowSenseCrashTokenReplenishTimestamp"
+ "acquiring kappa high sense crash token"
+ "acquiring kappa low sense crash token"
+ "acquiring kappa trigger token"
+ "highSenseCrashDetected"
+ "isHighOrLowSenseDetection"
+ "kappaHighSenseCrashTokenCount"
+ "kappaLowSenseCrashTokenCount"
+ "lowSenseCrashDetected"
+ "punch thru early %d highsense %d lend %d decided %d severe %d cand %d"
+ "tokenTriggerCnt = %d, tokenLowSenseCrashCnt = %d, tokenHighSenseCrashCnt = %d"
+ "v176@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiBiQQQBBBBq}16"
+ "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q}"
- "acquiring kappa token"
- "tokenCnt = %d"
- "v176@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiBiQQQBBq}16"
- "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"ttrType\"q}"

```
