## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-120.0.11.0.1
-  __TEXT.__text: 0x31ea24
-  __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0x8a80
-  __TEXT.__objc_methlist: 0x7d24
+120.0.11.0.3
+  __TEXT.__text: 0x322258
+  __TEXT.__auth_stubs: 0x16d0
+  __TEXT.__objc_stubs: 0x8b60
+  __TEXT.__objc_methlist: 0x7e24
   __TEXT.__const: 0x8bfd
-  __TEXT.__gcc_except_tab: 0xf8c4
-  __TEXT.__cstring: 0x1916b
-  __TEXT.__oslogstring: 0xe9ab
-  __TEXT.__objc_classname: 0x104c
-  __TEXT.__objc_methtype: 0x5f69
-  __TEXT.__objc_methname: 0xb3bb
-  __TEXT.__ustring: 0x10bc
-  __TEXT.__unwind_info: 0xb810
+  __TEXT.__gcc_except_tab: 0xfe84
+  __TEXT.__cstring: 0x19052
+  __TEXT.__oslogstring: 0xf0a9
+  __TEXT.__objc_classname: 0x1068
+  __TEXT.__objc_methtype: 0x6102
+  __TEXT.__objc_methname: 0xb4f9
+  __TEXT.__ustring: 0x10ae
+  __TEXT.__unwind_info: 0xb8d8
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb78
-  __DATA_CONST.__got: 0x560
+  __DATA_CONST.__auth_got: 0xb80
+  __DATA_CONST.__got: 0x570
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x22168
-  __DATA_CONST.__cfstring: 0x5d00
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __DATA_CONST.__const: 0x221e8
+  __DATA_CONST.__cfstring: 0x5d20
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x420
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_intobj: 0x1800
   __DATA_CONST.__objc_arraydata: 0x1f0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x280
-  __DATA.__objc_const: 0x110d8
-  __DATA.__objc_selrefs: 0x2aa8
-  __DATA.__objc_ivar: 0x90c
-  __DATA.__objc_data: 0x2e40
+  __DATA.__objc_const: 0x11338
+  __DATA.__objc_selrefs: 0x2ae8
+  __DATA.__objc_ivar: 0x920
+  __DATA.__objc_data: 0x2ee0
   __DATA.__data: 0x1ff0
   __DATA.__bss: 0x238
   __DATA.__common: 0x8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15127
-  Symbols:   563
-  CStrings:  8447
+  Functions: 15160
+  Symbols:   564
+  CStrings:  8505
 
Symbols:
+ _objc_retain_x9
CStrings:
+ "\x03\x11"
+ "\x03\x16\x12\x81\x13\x13\xf0Q\xf021\x12"
+ "\a\x13\x11\x12\x11"
+ "%!@(MISSING), now %!l(MISSING)lu"
+ "%!l(MISSING)lu closeEpoch now %!l(MISSING)lu"
+ "%!u(MISSING) HzSamples %!l(MISSING)lu %!l(MISSING)lu"
+ "-[CSKappaDetectionService getDataIntegrityBlock]"
+ "-[CSKappaTap2Radar radarWithResult:triggerUUID:ttrType:error:]"
+ "/Library/Caches/com.apple.xbs/Sources/CoreSafety/DataCollection/CSKappaTap2Radar.mm"
+ "@24@0:8r^{CMSafetyAudioResult=Q{CMSafetyAudioCrashResult=fQfffQfffQffB}{CMSafetyAudioCrashResult=fQfffQfffQffB}fiIQQQQQQI{CMSafetyAudioHistoricalLoudness=    }}16"
+ "@256@0:8Q16{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}24{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}104{CSSPUHistoricalLoudness_Struct=ffff}184f200I204I208Q212Q220Q228Q236Q244I252"
+ "AudioResult, %!l(MISSING)lu %!d(MISSING) dram %!l(MISSING)lu,%!l(MISSING)lu calc %!l(MISSING)lu wr %!l(MISSING)lu now %!l(MISSING)lu"
+ "B56@0:8{CSKappaTap2RadarConfirmation_struct=i@}16@32q40^@48"
+ "CSSyncQueue"
+ "EC_H"
+ "EC_L"
+ "KappaLastTTREarlyCrashTimestamp"
+ "KappaTTREarlyCrashPopupRate"
+ "KappaTTREnableHighSens"
+ "KappaTap2RadarQueue"
+ "Please tell us more about your incident around %!@(MISSING)."
+ "SentinelSample"
+ "Sorted %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING)"
+ "TQ,N,Vtimestamp"
+ "T^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQQQQI},R,N"
+ "TrustedAudio is before pre-trigger limit"
+ "TrustedAudio is late!"
+ "Unexpected checkpoint class"
+ "[DataIntegrity] Stream=count [min_ts max_ts] epoch %!d(MISSING) accel800=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] hgaccel=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] trigger=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] dm6=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] gps=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] steps=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] audio=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] pressure=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] hertzSample=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] companionStatus=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] remoteSample=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] ta=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] ts %!l(MISSING)lu now %!l(MISSING)lu la=%!d(MISSING) "
+ "[DataIntegrity] is disabled"
+ "[Kappa] False Positive Detection %!@(MISSING) Event=%!@(MISSING)"
+ "[Kappa] Improve Crash Detection %!@(MISSING) Event=%!@(MISSING)"
+ "[Kappa] True Positive Detection %!@(MISSING) Event=%!@(MISSING)"
+ "[LA] effts timestamp %!l(MISSING)lu now %!l(MISSING)lu"
+ "[TAH] %!d(MISSING) %!d(MISSING) %!f(MISSING) %!d(MISSING) %!d(MISSING) %!l(MISSING)lu %!l(MISSING)lu %!f(MISSING) %!l(MISSING)lu"
+ "[TTR] Cannot raise None TTR"
+ "[TTR] Deciding if to show TTR: type,%!d(MISSING)"
+ "[TTR] EarlyCrash alert cooldown expired daysSinceLast,%!d(MISSING),rate,%!f(MISSING)"
+ "[TTR] EarlyCrash alert still cooling down daysSinceLast,%!d(MISSING),rate,%!f(MISSING)"
+ "[TTR] Enqueued TTR with UUID %!@(MISSING), ttrManaged,%!d(MISSING)"
+ "[TTR] Error enqueuing TTR: %!@(MISSING), ttrManaged,%!d(MISSING)"
+ "[TTR] Error enqueuing for TTR test: %!@(MISSING)"
+ "[TTR] Error monitoring for TTR test: %!@(MISSING)"
+ "[TTR] Error starting TTR monitoring: %!@(MISSING)"
+ "[TTR] Setting severe crash"
+ "[TTR] Trigger chosen TTR days %!d(MISSING), rate: %!f(MISSING)"
+ "[TTR] Trigger not chosen TTR days %!d(MISSING), rate: %!f(MISSING)"
+ "[TTR] _mslRecording.shouldDeleteTTR = YES"
+ "[TTR] alpha/early ttr not selected, stopping early"
+ "[TTR] do not send ttr on aborted sessions"
+ "[TTR] lowSens,%!d(MISSING),highSens,%!d(MISSING),highSensEnabled,%!d(MISSING),severe,%!d(MISSING)"
+ "[TTR] show TTR %!d(MISSING)"
+ "[TTR] trigger ttr not selected, stopping early"
+ "^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQQQQI}16@0:8"
+ "_checkpoint"
+ "_dynamicHoldout"
+ "_queue"
+ "_syncQ"
+ "_trustedAudioStats"
+ "calculationTimestamp"
+ "closing epoch because of feedAccel t=%!l(MISSING)lu"
+ "closing epoch because of feedAudioRms t=%!l(MISSING)lu"
+ "closing epoch because of feedCompanionStatus t=%!l(MISSING)lu"
+ "closing epoch because of feedDM t=%!l(MISSING)lu"
+ "closing epoch because of feedFastAccel t=%!l(MISSING)lu"
+ "closing epoch because of feedGPS t=%!l(MISSING)lu"
+ "closing epoch because of feedHertzSample t=%!l(MISSING)lu"
+ "closing epoch because of feedHgAccel t=%!l(MISSING)lu"
+ "closing epoch because of feedPressure t=%!l(MISSING)lu"
+ "closing epoch because of feedRemoteSample t=%!l(MISSING)lu"
+ "closing epoch because of feedRoads t=%!l(MISSING)lu"
+ "closing epoch because of feedSteps t=%!l(MISSING)lu"
+ "closing epoch because of feedTrigger t=%!l(MISSING)lu"
+ "closing epoch because of feedTrustedAudioResult t=%!l(MISSING)lu"
+ "dramMaxTimestamp"
+ "dramMinTimestamp"
+ "fFlowControl->isKappaFeaturesAlgDataIntegrityEnabled()"
+ "feed ta timestamp %!l(MISSING)lu now %!l(MISSING)lu"
+ "found slowest sample at %!l(MISSING)lu type=%!@(MISSING)"
+ "fractionalAudio %!f(MISSING) %!d(MISSING) %!d(MISSING) %!f(MISSING)"
+ "getDataIntegrityBlock"
+ "getNextSortedArray"
+ "getNextSortedArrayAndFlush:"
+ "indexOfObject:inSortedRange:options:usingComparator:"
+ "initWithEpochTimestamp:planarResult:rolloverResult:historicalLoudness:maxRMS:numShortAudio:numPointsInEpoch:epochMinTimestamp:epochMaxTimestamp:dramMinTimestamp:dramMaxTimestamp:calculationTimestamp:dramDuration:"
+ "initWithTimestamp:"
+ "invalid kappa TTR type"
+ "lastSlowSample:"
+ "logAudioStats"
+ "missing _firstTriggerTimestamp"
+ "nextCheckpoint:"
+ "no slowest sample on this queue, but it has been too long, moving to %!l(MISSING)lu (%!f(MISSING) sec ago)"
+ "no slowest sample on this queue, default to %!l(MISSING)lu (%!f(MISSING) sec ago)"
+ "numEpochsMissingAudioAfterStart"
+ "numEpochsMissingAudioAtStart"
+ "preTriggerAudioSec"
+ "radarWithResult:triggerUUID:ttrType:error:"
+ "should not flush syncQ"
+ "shouldKeepEarlyCrashTTR"
+ "showConfirmationWithError:andEventType:"
+ "showTTRWithTriggerUUID:andEventType:"
+ "syncq sorted %!l(MISSING)lu, %!l(MISSING)lu remainder %!l(MISSING)lu, %!l(MISSING)lu, now %!l(MISSING)lu, n %!l(MISSING)u checkpoint %!l(MISSING)lu"
+ "timestampedComparator"
+ "updateTrustedAudioMetadata"
+ "v176@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiBiQQQBBq}16"
+ "{\"msg%!{(MISSING)public}.0s\":\"[DataIntegrity] is disabled\", \"event\":%!{(MISSING)public, location:escape_only}s, \"condition\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"[TTR] Cannot raise None TTR\", \"event\":%!{(MISSING)public, location:escape_only}s, \"condition\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"invalid kappa TTR type\", \"event\":%!{(MISSING)public, location:escape_only}s, \"condition\":%!{(MISSING)private, location:escape_only}s}"
+ "{CSKappaTap2RadarConfirmation_struct=i@}32@0:8^@16q24"
+ "{CSSPUTrustedAudioResult_Struct=\"timestamp\"Q\"planarResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"rolloverResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"historicalLoudness\"{CSSPUHistoricalLoudness_Struct=\"soundMaxMeanOverArmSession\"f\"soundMeanLast15s\"f\"soundMeanCurrentWindow\"f\"soundEnvelopeCount\"f}\"maxRMS\"f\"numShortAudio\"I\"numPointsInEpoch\"I\"epochMinTimestamp\"Q\"epochMaxTimestamp\"Q\"dramMinTimestamp\"Q\"dramMaxTimestamp\"Q\"calculationTimestamp\"Q\"dramDuration\"I}"
+ "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B\"ttrType\"q}"
+ "{TrustedAudioStats=\"fractionalAudio\"f\"numEpochsMissingAudioAtStart\"I\"numEpochsMissingAudioAfterStart\"I\"preTriggerAudioSec\"f}"
+ "{shared_ptr<CLKappaFeaturesAlgDataIntegrity>=^{CLKappaFeaturesAlgDataIntegrity}^{__shared_weak_count}}16@0:8"
- "\x02\x11"
- "\x03\x16\x12\x81\x13\x13\xf0A\xf0\"B"
- "\a\x13\x11\x12\x12"
- "\nBy filing this radar, data submitted anonymously in the past 7 days through Improve Health & Activity will now be correlated with this data submission and associated with you. Data submitted with this radar will only be used to develop and improve this feature and include the following high fidelity sensor data: accelerometer, gyroscope, pressure, odometer, navigation and GPS information, and sound pressure data."
- "\nRecently, your iPhone or Apple Watch detected a potential Kappa event, which may have helped connect you to emergency services. You may choose to file a radar to help develop and improve this feature."
- "%!u(MISSING) HzSamples %!l(MISSING)lu"
- "-Apple Internal- Kappa Event Follow-Up"
- "@232@0:8Q16{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}24{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}104{CSSPUHistoricalLoudness_Struct=ffff}184f200I204I208Q212Q220I228"
- "@24@0:8r^{CMSafetyAudioResult=Q{CMSafetyAudioCrashResult=fQfffQfffQffB}{CMSafetyAudioCrashResult=fQfffQfffQffB}fiIQQI{CMSafetyAudioHistoricalLoudness=    }}16"
- "AudioResult, %!l(MISSING)lu %!d(MISSING)..."
- "B36@0:8i16@20^@28"
- "Cannot raise None TTR"
- "Don't file a radar"
- "Enqueued TTR with UUID %!@(MISSING)"
- "Enqueued TTR with UUID %!@(MISSING), ttrManaged,%!d(MISSING)"
- "Error enqueuing TTR: %!@(MISSING)"
- "Error enqueuing TTR: %!@(MISSING), ttrManaged,%!d(MISSING)"
- "Error enqueuing for TTR test: %!@(MISSING)"
- "Error monitoring for TTR test: %!@(MISSING)"
- "Error starting TTR monitoring: %!@(MISSING)"
- "False Positive Detection %!@(MISSING)"
- "If you want, please tell us more about what you were doing when you got the SOS alert... "
- "If you want, please tell us more about your Kappa incident... "
- "OK"
- "Sorted %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING)"
- "T^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQI},R,N"
- "Trigger chosen TTR days %!d(MISSING), rate: %!f(MISSING)"
- "Trigger not chosen TTR days %!d(MISSING), rate: %!f(MISSING)"
- "True Positive Detection %!@(MISSING)"
- "UUID-NONE"
- "Was NOT in a Kappa incident. File radar."
- "Was in a Kappa incident. File radar."
- "[C] fractionalAudio %!d(MISSING) %!d(MISSING) %!f(MISSING)"
- "[DataIntegrity] Stream=count [min_ts max_ts] epoch %!d(MISSING) accel800=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] hgaccel=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] trigger=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] dm6=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] gps=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] steps=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] audio=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] pressure=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] hertzSample=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] companionStatus=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu] remoteSample=%!u(MISSING) [%!l(MISSING)lu %!l(MISSING)lu]"
- "^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQI}16@0:8"
- "_fractionalAudio"
- "_mslRecording.shouldDeleteTTR = YES"
- "addIndexesInRange:"
- "alpha/early ttr not selected, stopping early"
- "do not send ttr on aborted sessions"
- "early crash chosen TTR days %!d(MISSING), rate: %!f(MISSING)"
- "early crash not chosen TTR days %!d(MISSING), rate: %!f(MISSING)"
- "getFractionalAudio"
- "i24@0:8^@16"
- "initWithEpochTimestamp:planarResult:rolloverResult:historicalLoudness:maxRMS:numShortAudio:numPointsInEpoch:epochMinTimestamp:epochMaxTimestamp:dramDuration:"
- "initWithSpoolerFolder:andConfiguration:withQueue:"
- "radarWithResult:triggerUUID:error:"
- "show TTR %!d(MISSING)"
- "showConfirmationWithError:"
- "trigger ttr not selected, stopping early"
- "updateFractionalAudioMetadata"
- "v168@0:8{KappaSessionDetails=fCiiiiiifffiiiiiiiiiiiiiiiiBiQQQBB}16"
- "{\"msg%!{(MISSING)public}.0s\":\"Cannot raise None TTR\", \"event\":%!{(MISSING)public, location:escape_only}s, \"condition\":%!{(MISSING)private, location:escape_only}s}"
- "{CSSPUTrustedAudioResult_Struct=\"timestamp\"Q\"planarResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"rolloverResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"historicalLoudness\"{CSSPUHistoricalLoudness_Struct=\"soundMaxMeanOverArmSession\"f\"soundMeanLast15s\"f\"soundMeanCurrentWindow\"f\"soundEnvelopeCount\"f}\"maxRMS\"f\"numShortAudio\"I\"numPointsInEpoch\"I\"epochMinTimestamp\"Q\"epochMaxTimestamp\"Q\"dramDuration\"I}"
- "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"numDeescalationJointDetection\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q\"lendCompanionPunchThru\"B\"retractCompanionPunchThru\"B}"

```
