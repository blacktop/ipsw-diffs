## SonicAudioUnits

> `/System/Library/PrivateFrameworks/SonicAudioUnits.framework/SonicAudioUnits`

```diff

-  __TEXT.__text: 0x4468c
+  __TEXT.__text: 0x44484
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x3d20
   __TEXT.__gcc_except_tab: 0x1cfc
   __TEXT.__oslogstring: 0x5d4
-  __TEXT.__cstring: 0xab36
-  __TEXT.__unwind_info: 0x1718
+  __TEXT.__cstring: 0xab35
+  __TEXT.__unwind_info: 0x1720
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
Functions:
~ __ZN5ausdk6AUBase15PropertyChangedEjjj : 136 -> 120
~ __ZN5ausdk6AUBase25ProcessForScheduledParamsERNSt3__16vectorI23AudioUnitParameterEventNS1_9allocatorIS3_EEEEjPv : 456 -> 440
~ __ZNSt3__116__insertion_sortB9fqe220106INS_15_RangeAlgPolicyERPDoFbRK23AudioUnitParameterEventS4_EPS2_EEvT1_S9_T0_ : 240 -> 224
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_15_RangeAlgPolicyERPDoFbRK23AudioUnitParameterEventS4_EPS2_EEvT1_S9_T0_ : 260 -> 240
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_15_RangeAlgPolicyEP23AudioUnitParameterEventRPDoFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_ : 372 -> 364
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_15_RangeAlgPolicyERPDoFbRK23AudioUnitParameterEventS4_EPS2_EEbT1_S9_T0_ : 988 -> 964
~ __ZN5ausdk12AUEffectBase15MaintainKernelsEv : 488 -> 468
~ __ZN5ausdk9AUElement16GetParameterListEPj : 92 -> 80
~ __ZN5ausdk9AUElement12RestoreStateEPKh : 120 -> 104
~ __ZN5ausdk7AUScope19SetNumberOfElementsEj : 468 -> 436
~ __ZN12CLiveRemixerC2Ef15TAudioBusFormatP12CBasicFXHostlbb : 3940 -> 3936
~ __ZN12CLiveRemixer8ActivateEbP14CLiveRemixerFXS1_ : 260 -> 256
~ __ZN12CLiveRemixer14NotifyActivityEP14CLiveRemixerFXb : 800 -> 812
~ __ZN12CLiveRemixer9OnProcessEP12TProcessInfo : 1104 -> 1064
~ __ZN25CLiveRemixerFX_BitCrusherC2ER9CProcDataiPPfS3_S3_S3_ : 2568 -> 2572
~ __ZN28CStereoToMultiChannelBasicFXI13CPlatinumVerbEC2E15TAudioBusFormatfl : 1580 -> 1612
~ __ZNSt3__16vectorIN28CStereoToMultiChannelBasicFXI13CPlatinumVerbE11ChannelDataENS_9allocatorIS4_EEEC2B9fqe220106Em : 152 -> 136
~ __ZN20CLiveRemixerFX_GaterC2ER9CProcDataS1_iPPfS3_S3_S3_PN19CLiveRemixerLFObank12apfLfoBufferE : 1868 -> 1872
~ __Z43GetMappingForFormatAndAudioChannelLayoutTag15TAudioBusFormatjP10TChannelID : 112 -> 124
~ __Z20GetLabelForChannelID15TAudioBusFormat10TChannelID : 188 -> 196
~ __ZN8CBlitOsc12CreateOutputEPf : 136 -> 140
~ __ZN8CBlitOsc15CreateOutputTriEPf : 232 -> 228
~ __ZN8CBlitOsc13ProcessNonOptEll : 1800 -> 1792
~ __ZN8CBlitOsc15CreateOutputTriEPfllPP5ICGen : 244 -> 236
~ __ZN8CBlitOsc14CreateOutputDCEPfllPP5ICGen : 220 -> 216
~ __ZN13CInterpolator20GetInterpolatedValueEPKfS1_if : 168 -> 196
~ __ZN8CMixNtoMC2ER9CProcDatajjfb : 672 -> 648
~ __ZN8CMixNtoM5ResetEv : 16 -> 4
~ __ZN8CMixNtoM14ClearAllLevelsEv -> __ZN8CMixNtoM25SetAllLevelsToTargetLevelEv : 8 -> 156
~ __ZN8CMixNtoM12SetAllLevelsEf -> __ZN8CMixNtoM14ClearAllLevelsEv : 160 -> 8
~ __ZN8CMixNtoM25SetAllLevelsToTargetLevelEv -> __ZN8CMixNtoM12SetAllLevelsEf : 156 -> 160
~ __ZN8CMixNtoM7ProcessEv : 664 -> 640
~ __ZN9CNoiseGen7ProcessEv : 744 -> 772
~ __ZN9CNoiseGen13ProcessNonOptEll : 676 -> 684
~ __ZN11COscillator7ProcessEll : 688 -> 668
~ __ZN8CPolyLfo12GetGraphDataEPflfff : 2768 -> 2764
~ __ZN8CPolyLfo7ProcessEllPP5ICGen : 4420 -> 4308
~ __ZN7CRouter4CoreElllPP5ICGen : 1072 -> 1044
~ __ZN7CSource7ProcessEllPP5ICGen : 1216 -> 1108
~ __ZN11CStateVarTV13ProcessNonOptEll : 2972 -> 2912
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:613"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:623"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:624"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:688"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:723"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:724"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:776"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:113"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:144"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:152"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:192"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:212"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:240"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:251"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:263"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:305"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:321"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:99"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:610"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:620"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:621"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:679"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:705"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:706"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/LiveRemixer/CLiveRemixer.cpp:758"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:100"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:114"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:145"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:153"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:194"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:214"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:242"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:253"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:265"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:311"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SonicAudioUnits/Partner/RemixFXAudioUnit/Source/AURemixExtension/DSP/MADSP_Modules/CMixNtoM.cpp:327"

```
