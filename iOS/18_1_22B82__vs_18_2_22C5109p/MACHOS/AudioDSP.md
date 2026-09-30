## AudioDSP

> `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioDSP.framework/AudioDSP`

```diff

-747.207.0.0.0
-  __TEXT.__text: 0x1550c0
+747.333.0.0.0
+  __TEXT.__text: 0x157318
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_stubs: 0x340
-  __TEXT.__const: 0xc1d0
-  __TEXT.__gcc_except_tab: 0x9b00
-  __TEXT.__oslogstring: 0x82ed
-  __TEXT.__cstring: 0xc830
+  __TEXT.__const: 0xc220
+  __TEXT.__gcc_except_tab: 0x9c38
+  __TEXT.__oslogstring: 0x82fd
+  __TEXT.__cstring: 0xc8e0
   __TEXT.__objc_methname: 0x207
-  __TEXT.__unwind_info: 0x56e0
+  __TEXT.__unwind_info: 0x5708
   __DATA.__auth_got: 0xbc0
   __DATA.__got: 0x198
-  __DATA.__auth_ptr: 0x118
-  __DATA.__const: 0xc980
-  __DATA.__cfstring: 0xaea0
+  __DATA.__auth_ptr: 0x120
+  __DATA.__const: 0xc918
+  __DATA.__cfstring: 0xab60
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xd0
   __DATA.__data: 0x228
   __DATA.__bss: 0xb38
-  __DATA.__common: 0x34
+  __DATA.__common: 0x2c
   - /System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/ExclaveKit/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation

   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  Functions: 4818
-  Symbols:   7022
-  CStrings:  2480
+  Functions: 4824
+  Symbols:   7031
+  CStrings:  2488
 
Symbols:
+ GCC_except_table67
+ GCC_except_table721
+ GCC_except_table726
+ GCC_except_table730
+ GCC_except_table88
+ _ZN6DspLib11ToneMeister9AlgorithmC2Ev.cold.1
+ __ZN10applesauce2CF7details15make_CFArrayRefIPKcPKS4_EEDaT0_S8_NS1_15counterpart_tagE
+ __ZN11AUNeuralNet15CreateNeuralNetERNS_16NeuralNetWrapperE
+ __ZN11ecMIMO_iQRD20fcn_ecoutOverwrittenEv
+ __ZN18AUAnomalyDetectionD2Ev
+ __ZN20AULoudnessNormalizer12GetParameterEjjjRf
+ __ZN5ausdk9APFactoryINS_27AUBaseProcessMultipleLookupE10AUSeparateE7FactoryEPK25AudioComponentDescription
+ __ZN5ausdk9APFactoryINS_27AUBaseProcessMultipleLookupE10AUSeparateE8DestructEPv
+ __ZN5ausdk9APFactoryINS_27AUBaseProcessMultipleLookupE10AUSeparateE9ConstructEPvP28OpaqueAudioComponentInstance
+ __ZN6DspLib10AudioMeter9Algorithm7analyzeENS_9MultiSpanIKfEE
+ __ZN6DspLib10amp2dBSafeENSt3__14spanIKfLm18446744073709551615EEENS1_IfLm18446744073709551615EEEf
+ __ZN6DspLib11ToneMeister9Algorithm12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib12ControlFreak9Algorithm12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib13AlgorithmBase15setMaxNumFramesEm
+ __ZN6DspLib13AlgorithmBase7processENS_9MultiSpanIKfEENS1_IfEENSt3__18optionalIS3_EE
+ __ZN6DspLib13AlgorithmBase7processENS_9MultiSpanIfEE
+ __ZN6DspLib13AlgorithmBase7processENSt3__14spanIKfLm18446744073709551615EEENS2_IfLm18446744073709551615EEE
+ __ZN6DspLib13AlgorithmBase7processENSt3__14spanIfLm18446744073709551615EEE
+ __ZN6DspLib13DynamicFilter9Algorithm12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib13LoudnessMeter9Algorithm12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib13MeisterStueck6Kernel9Algorithm12processBlockENS_9MultiSpanIKfEENS3_IfEENSt3__18optionalIS5_EE
+ __ZN6DspLib13MeisterStueck9Algorithm12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib13copy_backwardENSt3__14spanIKfLm18446744073709551615EEENS1_IfLm18446744073709551615EEE
+ __ZN6DspLib16setHistoryLengthERNSt3__16vectorIfNS0_9allocatorIfEEEEm
+ __ZN6DspLib18LoudnessNormalizer10Parameters15kGainCurveNamesE
+ __ZN6DspLib18LoudnessNormalizer10Parameters15kResetModeNamesE
+ __ZN6DspLib18LoudnessNormalizer10Parameters19kRenderQualityNamesE
+ __ZN6DspLib18LoudnessNormalizer10Parameters20kAutomationModeNamesE
+ __ZN6DspLib18LoudnessNormalizer10Parameters21kWeightingFilterNamesE
+ __ZN6DspLib18LoudnessNormalizer9Algorithm12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib21PolyPhaseInterpolator16setSrcParametersEjm
+ __ZN6DspLib31FourBandRandomOrderLrFilterBank10FilterBankC2Ev
+ __ZN6DspLib3FFT10Filterbank12processBlockENS_9MultiSpanIKfEENS2_IfEENSt3__18optionalIS4_EE
+ __ZN6DspLib3FFT11ForwardSTFT11stateUpdateEv
+ __ZN6DspLib3FFT19BufferedInverseSTFT9getOutputENSt3__14spanIfLm18446744073709551615EEE
+ __ZN6DspLib3FIR10initializeENSt3__14spanIKfLm18446744073709551615EEEm
+ __ZN6DspLib3FIR15setMaxNumFramesEm
+ __ZN6DspLib3FIR7processENSt3__14spanIKfLm18446744073709551615EEENS2_IfLm18446744073709551615EEE
+ __ZN6DspLib3FIR9configureEv
+ __ZN6DspLib4copyENS_9MultiSpanIKfEENS0_IfEE
+ __ZN6DspLib4copyENSt3__14spanIKfLm18446744073709551615EEENS1_IfLm18446744073709551615EEE
+ __ZN6ecMIMO20fcn_ecoutOverwrittenEv
+ __ZNK11AUNeuralNet36CreateMutableDictionaryWithBatchSizeEN10applesauce2CF13DictionaryRefE
+ __ZNK6DspLib13AlgorithmBase12maxNumFramesEv
+ __ZNK6DspLib13AlgorithmBase16numberOfChannelsEv
+ __ZNSt3__112construct_atB8fe180100IN10applesauce2CF9StringRefEJRKPKcEPS3_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB8fe180100IN6DspLib10AudioMeter9AlgorithmEJS3_EPS3_EEPT_S6_DpOT0_
+ __ZNSt3__124__optional_destruct_baseIN6DspLib10AudioMeter9AlgorithmELb0EE5resetB8fe180100Ev
+ __ZNSt3__124__optional_destruct_baseIN6DspLib10AudioMeter9AlgorithmELb0EED2B8fe180100Ev
+ __ZNSt3__16vectorIN6DspLib3RMSENS_9allocatorIS2_EEE13__vdeallocateEv
+ __ZNSt3__18optionalIN6DspLib10AudioMeter9AlgorithmEEaSB8fe180100IS3_vEERS4_OT_
+ __ZZN6DspLib10AudioMeter9Algorithm7analyzeENS_9MultiSpanIKfEEENK3$_0clES4_
+ __ZZN6DspLib13CircularDelay7processENSt3__14spanIKfLm18446744073709551615EEENS2_IfLm18446744073709551615EEEENK3$_0clEv
+ __block_descriptor_tmp.128
+ __block_literal_global.130
- GCC_except_table134
- GCC_except_table720
- GCC_except_table722
- GCC_except_table728
- GCC_except_table732
- GCC_except_table96
- _ZN6DspLib13MeisterStueck9AlgorithmC2Eb.cold.1
- __ZN10applesauce2CF9StringRefC1EPKc
- __ZN12DspLibBuffer14setFrameOffsetEm
- __ZN12DspLibBuffer33mMaxStackMemoryConsumptionInBytesE
- __ZN12DspLibBufferC1EPKPfmj
- __ZN12DspLibBufferC1EPfmjb
- __ZN12DspLibBufferaSERKS_
- __ZN20AULoudnessNormalizer26ProcessMultipleBufferListsERjjjPPK15AudioBufferListjPPS1_
- __ZN5ausdk9APFactoryINS_19AUBaseProcessLookupE10AUSeparateE7FactoryEPK25AudioComponentDescription
- __ZN5ausdk9APFactoryINS_19AUBaseProcessLookupE10AUSeparateE8DestructEPv
- __ZN5ausdk9APFactoryINS_19AUBaseProcessLookupE10AUSeparateE9ConstructEPvP28OpaqueAudioComponentInstance
- __ZN6DspLib10AudioMeter9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib10AudioMeter9Algorithm12uninitializeEv
- __ZN6DspLib10AudioMeter9AlgorithmC1Ev
- __ZN6DspLib10AudioMeter9AlgorithmD0Ev
- __ZN6DspLib11ToneMeister10ParametersL15kMaxNumChannelsE
- __ZN6DspLib11ToneMeister9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib12ControlFreak9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib13AlgorithmBase24setNumberOfAudioChannelsEjj
- __ZN6DspLib13AlgorithmBase7processEP12DspLibBuffer
- __ZN6DspLib13AlgorithmBase7processEP12DspLibBufferS2_jj
- __ZN6DspLib13DynamicFilter9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib13LoudnessMeter9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib13MeisterStueck6Kernel9Algorithm12processBlockEP12DspLibBufferS4_jj
- __ZN6DspLib13MeisterStueck9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib18LoudnessNormalizer9Algorithm12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib21PolyPhaseInterpolator16setSrcParametersEjj
- __ZN6DspLib3FFT10Filterbank12processBlockEP12DspLibBufferS3_jj
- __ZN6DspLib3FFT19BufferedInverseSTFT18doTransformIfReadyERK15DSPSplitComplex
- __ZN6DspLib3FIR10initializeEmm
- __ZN6DspLib3FIR15setCoefficientsENSt3__14spanIKfLm18446744073709551615EEE
- __ZN6DspLib3FIR5resetEv
- __ZN6DspLib3FIR7processENS_9MultiSpanIKfEENS1_IfEE
- __ZNK11AUNeuralNet15CreateNeuralNetEN10applesauce2CF13DictionaryRefE
- __ZNK12DspLibBuffer11channelsPtrEPPf
- __ZNK12DspLibBuffer13channelBufferEj
- __ZNK6DspLib10AudioMeter9Algorithm9numStatusEv
- __ZNK6DspLib13AlgorithmBase15numOutputFramesEm
- __ZNK6DspLib13AlgorithmBase17maxNumInputFramesEv
- __ZNK6DspLib13AlgorithmBase21numberOfInputChannelsEv
- __ZNK6DspLib13AlgorithmBase22numberOfOutputChannelsEv
- __ZTVN6DspLib10AudioMeter9AlgorithmE
- __ZZN6DspLib18LoudnessNormalizer9Algorithm12processBlockEP12DspLibBufferS3_jjENK3$_0clEm
- __block_descriptor_tmp.125
- __block_literal_global.127
CStrings:
+ "12:50:17"
+ "12:50:27"
+ "Bypass eclee check for specific products"
+ "Ecout overwritten flag"
+ "Failed to retrieve block size. err = %!d(MISSING) batchsize = %!u(MISSING)"
+ "Oct 16 2024"
+ "Post EClee Gain"
+ "[%!p(MISSING)] Failed to retrieve batch size, set to be (%!u(MISSING))."
+ "dB thresh for eclee check"
+ "ecout is overwritten by mic in EC"
+ "ecout overwritting flag"
+ "perc"
+ "sdsp"
- "23:30:47"
- "23:30:58"
- "Failed to retrieve sample rate. err = %!d(MISSING) batchsize = %!u(MISSING)"
- "Sep 28 2024"
- "[%!p(MISSING)] Loading batch size from plist."

```
