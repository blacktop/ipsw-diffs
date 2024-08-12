## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-120.0.2.0.0
-  __TEXT.__text: 0x314f98
+120.0.4.0.0
+  __TEXT.__text: 0x3161ec
   __TEXT.__auth_stubs: 0x16b0
   __TEXT.__objc_stubs: 0x8a20
   __TEXT.__objc_methlist: 0x7cfc
-  __TEXT.__const: 0x82f5
-  __TEXT.__gcc_except_tab: 0xf1d8
-  __TEXT.__cstring: 0x19285
+  __TEXT.__const: 0x83d5
+  __TEXT.__gcc_except_tab: 0xf208
+  __TEXT.__cstring: 0x1935c
   __TEXT.__oslogstring: 0xdde0
   __TEXT.__objc_classname: 0x104c
-  __TEXT.__objc_methtype: 0x5e85
-  __TEXT.__objc_methname: 0xb35d
+  __TEXT.__objc_methtype: 0x5e99
+  __TEXT.__objc_methname: 0xb36b
   __TEXT.__ustring: 0x10bc
-  __TEXT.__unwind_info: 0xb428
+  __TEXT.__unwind_info: 0xb460
   __TEXT.__eh_frame: 0x590
   __DATA_CONST.__auth_got: 0xb70
   __DATA_CONST.__got: 0x428
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x20b58
+  __DATA_CONST.__const: 0x20ba8
   __DATA_CONST.__cfstring: 0x5d20
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14955
+  Functions: 14974
   Symbols:   523
-  CStrings:  8401
+  CStrings:  8410
 
CStrings:
+ "@232@0:8Q16{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}24{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}104{CSSPUHistoricalLoudness_Struct=ffff}184f200I204I208Q212Q220I228"
+ "T^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQI},R,N"
+ "^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQI}16@0:8"
+ "dramDuration"
+ "gestureLengthSeconds"
+ "initWithEpochTimestamp:planarResult:rolloverResult:historicalLoudness:maxRMS:numShortAudio:numPointsInEpoch:epochMinTimestamp:epochMaxTimestamp:dramDuration:"
+ "isWristLooselyLevel"
+ "pauseBtwPeaksSeconds"
+ "rotZRangeDuringGestureRad"
+ "screenTiltAtEndDegrees"
+ "screenTiltAtStartDegrees"
+ "streamingHighFrequencyHeartRateData"
+ "wristAngleDiffBtwPeaksDegrees"
+ "{CSSPUTrustedAudioResult_Struct=\"timestamp\"Q\"planarResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"rolloverResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"historicalLoudness\"{CSSPUHistoricalLoudness_Struct=\"soundMaxMeanOverArmSession\"f\"soundMeanLast15s\"f\"soundMeanCurrentWindow\"f\"soundEnvelopeCount\"f}\"maxRMS\"f\"numShortAudio\"I\"numPointsInEpoch\"I\"epochMinTimestamp\"Q\"epochMaxTimestamp\"Q\"dramDuration\"I}"
- "@228@0:8Q16{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}24{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}104{CSSPUHistoricalLoudness_Struct=ffff}184f200I204I208Q212Q220"
- "T^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQ},R,N"
- "^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQ}16@0:8"
- "initWithEpochTimestamp:planarResult:rolloverResult:historicalLoudness:maxRMS:numShortAudio:numPointsInEpoch:epochMinTimestamp:epochMaxTimestamp:"
- "{CSSPUTrustedAudioResult_Struct=\"timestamp\"Q\"planarResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"rolloverResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"historicalLoudness\"{CSSPUHistoricalLoudness_Struct=\"soundMaxMeanOverArmSession\"f\"soundMeanLast15s\"f\"soundMeanCurrentWindow\"f\"soundEnvelopeCount\"f}\"maxRMS\"f\"numShortAudio\"I\"numPointsInEpoch\"I\"epochMinTimestamp\"Q\"epochMaxTimestamp\"Q}"

```
