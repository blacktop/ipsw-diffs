## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-145.0.7.0.0
-  __TEXT.__text: 0x350a94
-  __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_stubs: 0x9160
-  __TEXT.__objc_methlist: 0x8c48
-  __TEXT.__gcc_except_tab: 0x1124c
-  __TEXT.__const: 0x9446
-  __TEXT.__cstring: 0x1a70b
-  __TEXT.__oslogstring: 0x100c2
+145.0.10.0.0
+  __TEXT.__text: 0x356f74
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__objc_stubs: 0x9180
+  __TEXT.__objc_methlist: 0x8c50
+  __TEXT.__gcc_except_tab: 0x11510
+  __TEXT.__const: 0x44136
+  __TEXT.__cstring: 0x1a774
+  __TEXT.__oslogstring: 0x10828
   __TEXT.__objc_classname: 0x10a6
-  __TEXT.__objc_methtype: 0x5d7b
-  __TEXT.__objc_methname: 0xbe86
+  __TEXT.__objc_methtype: 0x5def
+  __TEXT.__objc_methname: 0xbea9
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xbe38
+  __TEXT.__unwind_info: 0xc088
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb60
-  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__auth_got: 0xb70
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x22da0
+  __DATA_CONST.__const: 0x25330
   __DATA_CONST.__cfstring: 0x6620
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xff28
-  __DATA.__objc_selrefs: 0x2f78
+  __DATA.__objc_selrefs: 0x2f80
   __DATA.__objc_ivar: 0x930
   __DATA.__objc_data: 0x2f80
   __DATA.__data: 0x2010

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5A49E165-D1E9-3423-AD1D-0E7733EDE5BD
-  Functions: 15913
-  Symbols:   567
-  CStrings:  9741
+  UUID: 11784C1A-0841-3E4B-85B5-EB6ED3F5B42A
+  Functions: 16062
+  Symbols:   572
+  CStrings:  9761
 
Symbols:
+ __ZN33CLKappaDeescalatorCrashClassifier10kConfigKeyE
+ __ZN33CLKappaDeescalatorCrashClassifier13kForceBaseKeyE
+ __ZN33CLKappaDeescalatorCrashClassifier22kConfigurationDefaultsE
+ __ZNSt3__16__sortIRNS_6__lessIddEEPdEEvT0_S5_T_
+ __ZNSt3__16chrono12steady_clock3nowEv
CStrings:
+ "[CrashClassifier-Estimates] summary,A,%{public}d,B,%{public}llu,config-1,%{public}g,config-2,%{public}g,debug-1a,%{public}g,debug-1b,%{public}g,debug-1c,%{public}g,debug-1d,%{public}g,debug-1e,%{public}g,debug-1f,%{public}g,debug-1g,%{public}g,debug-1h,%{public}g,debug-1i,%{public}g,debug-1j,%{public}d"
+ "[CrashClassifier-Features] summary,A,%{public}llu,config-1,%{public}d,config-2,%{public}d,config-3,%{public}d,config-4,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}u,debug-1e,%{public}u,debug-1f,%{public}u,debug-1g,%{public}f,debug-1h,%{public}f,debug-1i,%{public}f,debug-1j,%{public}d,debug-1k,%{public}d,debug-1l,%{public}d,debug-1m,%{public}d,debug-1n,%{public}d,debug-1o,%{public}d,debug-1p,%{public}f"
+ "[CrashClassifier][Estimates] Output ended up being NaN!"
+ "[CrashClassifier][Estimates] Unexpected input buffer size baro,%zu,rotationRate,%zu,inertialAccel,%zunBaro,%zu,nRotationRate,%zu,nInertialAccel,%zu"
+ "[CrashClassifier][Features] Disabled, skipping CrashClassifier"
+ "[CrashClassifier][Features] Tried to calculate the median of an empty buffer"
+ "[CrashClassifier][Features] Tried to normalize a buffer with size,%zu"
+ "[CrashClassifier][Features] forward fill error with bufferSize,%zu,desiredBufferSize%zu"
+ "[CrashClassifier][Features] reset()"
+ "[CrashClassifier][Features] setConfig enabled,%d,requiredBaroBufferSize,%d,requiredRotationRateBufferSize,%d,requiredInertialAccelBufferSize,%d"
+ "[SC] AlgBlock summary,A,%{public}llu,B,%{public}llu,C,%{public}d,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-2a,%{public}u,debug-2b,%{public}u,debug-2c,%{public}u,debug-2d,%{public}u,debug-2e,%{public}u,debug-2f,%{public}u,debug-2g,%{public}u,debug-2h,%{public}u,debug-2i,%{public}u,debug-2j,%{public}u,debug-2k,%{public}u,debug-2l,%{public}u,debug-2m,%{public}u,debug-2n,%{public}u,debug-2o,%{public}u,debug-2p,%{public}u,debug-2q,%{public}u,debug-2r,%{public}u"
+ "[SC] force %d %d %d %d %d is %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d"
+ "[de-CrashClassifier] Unexpected dimensions, crashClassifierFPHistory,%zu,crashHistory,%zu,rolloverHistory,%zu"
+ "[de-CrashClassifier] de-escalate"
+ "[de-CrashClassifier] disabled"
+ "[de-CrashClassifier] missing config"
+ "[de-CrashClassifier] resetConfiguration"
+ "[de-CrashClassifier] setConfig with enable,%d"
+ "[de-CrashClassifier] summary,A,%{public}llu,B,%{public}u,mode,%{public}u,config-1,%{public}u,debug-1a,%{public}u,debug-1b,%{public}zu,debug-1c,%{public}zu,debug-1d,%{public}zu"
+ "de-CrashClassifier"
+ "isCrashClassifierSupportedPlatform"
+ "shouldDeescalateBecauseOfCrashClassifierCondition"
+ "v192@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiiiBiQQQBBBBqI}16"
+ "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"numDeescalationCrashClassifier\"i\"numInertDeescalationCrashClassifier\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q\"deescalationBitmap\"I}"
+ "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q\"deescalationBitmap\"I}"
- "[SC] AlgBlock summary,A,%{public}llu,B,%{public}llu,C,%{public}d,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-2a,%{public}u,debug-2b,%{public}u,debug-2c,%{public}u,debug-2d,%{public}u,debug-2e,%{public}u,debug-2f,%{public}u,debug-2g,%{public}u,debug-2h,%{public}u,debug-2i,%{public}u,debug-2j,%{public}u,debug-2k,%{public}u,debug-2l,%{public}u,debug-2m,%{public}u,debug-2n,%{public}u,debug-2o,%{public}u,debug-2p,%{public}u,debug-2o,%{public}u"
- "[SC] force %d %d %d %d %d is %d %d %d %d %d %d %d %d %d %d %d %d %d %d"
- "v176@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiBiQQQBBBBq}16"
- "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"lowSenseCrashDetected\"B\"highSenseCrashDetected\"B\"ttrType\"q}"
- "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q}"

```
