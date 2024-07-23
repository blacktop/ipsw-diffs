## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-119.0.1.0.0
-  __TEXT.__text: 0x31169c
+120.0.2.0.0
+  __TEXT.__text: 0x314f98
   __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_stubs: 0x89c0
-  __TEXT.__objc_methlist: 0x7cdc
-  __TEXT.__const: 0x82c5
-  __TEXT.__gcc_except_tab: 0xf1c4
-  __TEXT.__cstring: 0x18eea
-  __TEXT.__oslogstring: 0xdd68
+  __TEXT.__objc_stubs: 0x8a20
+  __TEXT.__objc_methlist: 0x7cfc
+  __TEXT.__const: 0x82f5
+  __TEXT.__gcc_except_tab: 0xf1d8
+  __TEXT.__cstring: 0x19285
+  __TEXT.__oslogstring: 0xdde0
   __TEXT.__objc_classname: 0x104c
-  __TEXT.__objc_methtype: 0x5cfb
-  __TEXT.__objc_methname: 0xb2f6
+  __TEXT.__objc_methtype: 0x5e85
+  __TEXT.__objc_methname: 0xb35d
   __TEXT.__ustring: 0x10bc
   __TEXT.__info_plist: 0x458
-  __TEXT.__unwind_info: 0xb3e8
-  __TEXT.__eh_frame: 0x558
+  __TEXT.__unwind_info: 0xb428
+  __TEXT.__eh_frame: 0x590
   __DATA_CONST.__auth_got: 0xb70
   __DATA_CONST.__got: 0x428
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x201c8
-  __DATA_CONST.__cfstring: 0x5ca0
+  __DATA_CONST.__const: 0x20b58
+  __DATA_CONST.__cfstring: 0x5d20
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA.__objc_const: 0x11098
-  __DATA.__objc_selrefs: 0x2a78
+  __DATA.__objc_const: 0x110b8
+  __DATA.__objc_selrefs: 0x2a90
   __DATA.__objc_ivar: 0x908
   __DATA.__objc_data: 0x2e40
   __DATA.__data: 0x1ff0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14923
+  Functions: 14955
   Symbols:   523
-  CStrings:  8356
+  CStrings:  8401
 
CStrings:
+ "-[CSKappaDetectionService getCrashBlock]"
+ "@228@0:8Q16{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}24{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}104{CSSPUHistoricalLoudness_Struct=ffff}184f200I204I208Q212Q220"
+ "@24@0:8r^{CMSafetyAudioResult=Q{CMSafetyAudioCrashResult=fQfffQfffQffB}{CMSafetyAudioCrashResult=fQfffQfffQffB}fiIQQI{CMSafetyAudioHistoricalLoudness=    }}16"
+ "CSMartyPunchThruTokenCount"
+ "CSMartyPunchThruTokenCountDefault"
+ "CSMartyPunchThruTokenReplenishPeriod"
+ "CSMartyPunchThruTokenReplenishTimestamp"
+ "Ignoring post riding marty trigger"
+ "Letting post riding marty action since it is remotely armed"
+ "Letting post riding marty trigger since it is remotely armed"
+ "T^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQ},R,N"
+ "[C] fractionalAudio %!d(MISSING) %!d(MISSING) %!f(MISSING)"
+ "^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUHistoricalLoudness_Struct=ffff}fIIQQ}16@0:8"
+ "_fractionalAudio"
+ "epochMaxTimestamp"
+ "epochMinTimestamp"
+ "escalation, using punchthru token"
+ "getCrashBlock"
+ "getFractionalAudio"
+ "initWithEpochTimestamp:planarResult:rolloverResult:historicalLoudness:maxRMS:numShortAudio:numPointsInEpoch:epochMinTimestamp:epochMaxTimestamp:"
+ "numPointsInEpoch"
+ "planarChaosAtMaxEnergy"
+ "planarChaosAtMaxSaturation"
+ "planarEnergyAtMaxChaos"
+ "planarEnergyAtMaxSaturation"
+ "planarMaxChaos"
+ "planarMaxEnergy"
+ "planarMaxSaturation"
+ "planarPassThru"
+ "planarSaturationAtMaxChaos"
+ "planarSaturationAtMaxEnergy"
+ "planarTimestampAtMaxChaos"
+ "planarTimestampAtMaxEnergy"
+ "planarTimestampAtMaxSaturation"
+ "recordTrustedAudio:"
+ "rolloverChaosAtMaxEnergy"
+ "rolloverChaosAtMaxSaturation"
+ "rolloverEnergyAtMaxChaos"
+ "rolloverEnergyAtMaxSaturation"
+ "rolloverMaxChaos"
+ "rolloverMaxEnergy"
+ "rolloverMaxSaturation"
+ "rolloverPassThru"
+ "rolloverSaturationAtMaxChaos"
+ "rolloverSaturationAtMaxEnergy"
+ "rolloverTimestampAtMaxChaos"
+ "rolloverTimestampAtMaxEnergy"
+ "rolloverTimestampAtMaxSaturation"
+ "safetyTrustedAudioResult"
+ "soundEnvelopeCount"
+ "soundMaxMeanOverArmSession"
+ "soundMeanCurrentWindow"
+ "soundMeanLast15s"
+ "updateFractionalAudioMetadata"
+ "v24@0:8@\"CSSPUTrustedAudioResult\"16"
+ "{CSSPUTrustedAudioResult_Struct=\"timestamp\"Q\"planarResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"rolloverResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"historicalLoudness\"{CSSPUHistoricalLoudness_Struct=\"soundMaxMeanOverArmSession\"f\"soundMeanLast15s\"f\"soundMeanCurrentWindow\"f\"soundEnvelopeCount\"f}\"maxRMS\"f\"numShortAudio\"I\"numPointsInEpoch\"I\"epochMinTimestamp\"Q\"epochMaxTimestamp\"Q}"
+ "{shared_ptr<CLKappaEstimatesAlgCrash>=^{CLKappaEstimatesAlgCrash}^{__shared_weak_count}}16@0:8"
- "-[CSKappaDetectionService getFractionalAudioAvailability]"
- "@212@0:8Q16{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}24{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}104f184I188I192Q196Q204"
- "@224@0:8{CMSafetyAudioResult=Q{CMSafetyAudioCrashResult=fQfffQfffQffB}{CMSafetyAudioCrashResult=fQfffQfffQffB}fIIQQI}16"
- "T^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}fIIQQ},R,N"
- "^{CSSPUTrustedAudioResult_Struct=Q{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}{CSSPUAudioCrashResult_Struct=fQfffQfffQffB}fIIQQ}16@0:8"
- "_hasAudioInEpochCount"
- "escalation, no token required"
- "fractional audio epoch %!d(MISSING) has %!d(MISSING) %!f(MISSING)"
- "getFractionalAudioAvailability"
- "ignore post riding marty trigger"
- "initWithEpochTimestamp:planarResult:rolloverResult:maxRMS:numShortAudio:numPointsInEpoch:epochMinTimestamp:epochMaxTimestamp:"
- "{CSSPUTrustedAudioResult_Struct=\"timestamp\"Q\"planarResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"rolloverResult\"{CSSPUAudioCrashResult_Struct=\"maxEnergy\"f\"timestampAtMaxEnergy\"Q\"chaosAtMaxEnergy\"f\"saturationAtMaxEnergy\"f\"maxChaos\"f\"timestampAtMaxChaos\"Q\"energyAtMaxChaos\"f\"saturationAtMaxChaos\"f\"maxSaturation\"f\"timestampAtMaxSaturation\"Q\"chaosAtMaxSaturation\"f\"energyAtMaxSaturation\"f\"passThru\"B}\"maxRMS\"f\"numShortAudio\"I\"numPointsInEpoch\"I\"epochMinTimestamp\"Q\"epochMaxTimestamp\"Q}"

```
