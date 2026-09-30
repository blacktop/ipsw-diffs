## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2175.9.2.0.0
-  __TEXT.__text: 0xadf78
+2175.12.1.0.0
+  __TEXT.__text: 0xae454
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x8d60
-  __TEXT.__const: 0x24a8
-  __TEXT.__cstring: 0xea60
+  __TEXT.__objc_methlist: 0x8dd8
+  __TEXT.__const: 0x24e8
+  __TEXT.__cstring: 0xeac8
   __TEXT.__oslogstring: 0xc712
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x16e0
+  __TEXT.__unwind_info: 0x16e8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1bd0c
-  __TEXT.__objc_methtype: 0x244f
-  __TEXT.__objc_stubs: 0xee60
+  __TEXT.__objc_methname: 0x1bfcb
+  __TEXT.__objc_methtype: 0x2478
+  __TEXT.__objc_stubs: 0xef20
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__const: 0xda0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42f8
+  __DATA_CONST.__objc_selrefs: 0x4340
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xde60
-  __AUTH_CONST.__objc_const: 0x16898
+  __AUTH_CONST.__cfstring: 0xdf20
+  __AUTH_CONST.__objc_const: 0x169f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x2020
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x2044
   __DATA.__data: 0x738
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x78
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0xa0
   __DATA_DIRTY.__common: 0x22
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EFBC49D3-A981-3FFF-A6CF-684DBC76A2BF
-  Functions: 3968
-  Symbols:   13065
-  CStrings:  9274
+  UUID: 7A17B946-945E-383C-B1F8-B868EAF8B39D
+  Functions: 3978
+  Symbols:   13101
+  CStrings:  9307
 
Symbols:
+ -[MultiwayCall matchedOrientationBucketed]
+ -[MultiwayCall mismatchedOrientationBucketed]
+ -[MultiwaySegment alwaysFullBleedStatus]
+ -[MultiwaySegment setAlwaysFullBleedStatus:]
+ -[RTCReportingAgent realtimeEventsEnabled]
+ -[VCAggregator alwaysFullBleedUserPreferenceStatus]
+ -[VCAggregator processAlwaysFullBleedUserPrefer:]
+ -[VCAggregator setAlwaysFullBleedUserPreferenceStatus:]
+ -[VCAggregatorAudioStream processSenderOnlyStats:]
+ -[VCAggregatorMultiway processAlwaysFullBleedUserPrefer:]
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table41
+ _OBJC_IVAR_$_MultiwayCall._matchedOrientationBucketed
+ _OBJC_IVAR_$_MultiwayCall._mismatchedOrientationBucketed
+ _OBJC_IVAR_$_MultiwaySegment._alwaysFullBleedStatus
+ _OBJC_IVAR_$_VCAggregator._alwaysFullBleedStatus
+ _OBJC_IVAR_$_VCAggregator._alwaysFullBleedUserPreferenceStatus
+ _OBJC_IVAR_$_VCAggregatorMultiway._landscapeLeftOrientationBucketed
+ _OBJC_IVAR_$_VCAggregatorMultiway._landscapeRightOrientationBucketed
+ _OBJC_IVAR_$_VCAggregatorMultiway._portraitOrientationBucketed
+ _OBJC_IVAR_$_VCAggregatorMultiway._portraitUpsideDownOrientationBucketed
+ __MergedGlobals.1007
+ ___81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.233
+ ___block_literal_global.230
+ ___block_literal_global.524
+ ___block_literal_global.533
+ ___block_literal_global.616
+ ___reportingSetUserInfo_block_invoke.529
+ ___reportingSetUserInfo_block_invoke.530
+ ___reportingSetUserInfo_block_invoke.530.cold.1
+ _objc_msgSend$matchedOrientationBucketed
+ _objc_msgSend$mismatchedOrientationBucketed
+ _objc_msgSend$processAlwaysFullBleedUserPrefer:
+ _objc_msgSend$processSenderOnlyStats:
+ _objc_msgSend$realtimeEventsEnabled
+ _objc_msgSend$setAlwaysFullBleedUserPreferenceStatus:
+ _orientationDurationBucketRanges
- GCC_except_table127
- GCC_except_table129
- GCC_except_table232
- GCC_except_table233
- GCC_except_table240
- GCC_except_table242
- GCC_except_table40
- __MergedGlobals.1003
- ___81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.227
- ___block_literal_global.224
- ___block_literal_global.517
- ___block_literal_global.526
- ___block_literal_global.609
- ___reportingSetUserInfo_block_invoke.522
- ___reportingSetUserInfo_block_invoke.523
- ___reportingSetUserInfo_block_invoke.523.cold.1
CStrings:
+ "AFBUPENB"
+ "ORTNLandLeft"
+ "ORTNLandRight"
+ "ORTNMatched"
+ "ORTNMismatched"
+ "ORTNPortrait"
+ "ORTNPortraitUpsDown"
+ "T@\"VCReportingHistogram\",R,V_matchedOrientationBucketed"
+ "T@\"VCReportingHistogram\",R,V_mismatchedOrientationBucketed"
+ "Tc,N,V_alwaysFullBleedUserPreferenceStatus"
+ "Tc,V_alwaysFullBleedStatus"
+ "T{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BBB}},V_persistentSettings"
+ "_alwaysFullBleedStatus"
+ "_alwaysFullBleedUserPreferenceStatus"
+ "_landscapeLeftOrientationBucketed"
+ "_landscapeRightOrientationBucketed"
+ "_matchedOrientationBucketed"
+ "_mismatchedOrientationBucketed"
+ "_portraitOrientationBucketed"
+ "_portraitUpsideDownOrientationBucketed"
+ "alwaysFullBleedStatus"
+ "alwaysFullBleedUserPreferenceStatus"
+ "enableRealtimeTelemetryReporting"
+ "matchedOrientationBucketed"
+ "mismatchedOrientationBucketed"
+ "processAlwaysFullBleedUserPrefer:"
+ "processSenderOnlyStats:"
+ "realtimeEventsEnabled"
+ "setAlwaysFullBleedStatus:"
+ "setAlwaysFullBleedUserPreferenceStatus:"
+ "v24@0:8^{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
+ "v40@0:8{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
+ "{tagVCReportingClientSettingsPersist=\"eyeContactStatus\"c\"mlEnhanceStatus\"c\"centerStageStatus\"c\"portraitModeStatus\"c\"studioLightStatus\"c\"reactionsStatus\"c\"backgroundReplacementStatus\"c\"alwaysfullbleedUserPreferenceStatus\"c\"switches\"Q\"experimentSettings\"{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B\"detectInactiveAudioFramesAACELD\"B}}"
+ "{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BBB}}16@0:8"
- "ORTNDurs"
- "ORTNMatchedDurs"
- "T{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}},V_persistentSettings"
- "v24@0:8^{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
- "v40@0:8{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
- "{tagVCReportingClientSettingsPersist=\"eyeContactStatus\"c\"mlEnhanceStatus\"c\"centerStageStatus\"c\"portraitModeStatus\"c\"studioLightStatus\"c\"reactionsStatus\"c\"backgroundReplacementStatus\"c\"switches\"Q\"experimentSettings\"{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B\"detectInactiveAudioFramesAACELD\"B}}"
- "{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16@0:8"

```
