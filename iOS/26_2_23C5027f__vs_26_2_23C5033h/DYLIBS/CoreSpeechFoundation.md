## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

 3510.3.1.0.0
-  __TEXT.__text: 0xc3410
+  __TEXT.__text: 0xc3450
   __TEXT.__auth_stubs: 0x1ec0
   __TEXT.__objc_methlist: 0xc690
   __TEXT.__const: 0x808

   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_classname: 0x1c26
   __TEXT.__objc_methname: 0x20d10
-  __TEXT.__objc_methtype: 0x4482
+  __TEXT.__objc_methtype: 0x44a6
   __TEXT.__objc_stubs: 0x10f80
   __DATA_CONST.__got: 0xf90
   __DATA_CONST.__const: 0x26b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EA62AD50-B3E4-37DE-9457-7BE371E03C2A
+  UUID: AD85CDC8-C436-30DE-B348-ECF86C22FD5E
   Functions: 4783
-  Symbols:   16235
+  Symbols:   16236
   CStrings:  10181
 
Symbols:
+ ___chkstk_darwin
Functions:
~ __ZN22NonlinearBeepCanceller15fcn_vector_initERNSt3__16vectorINS1_INS1_INS1_IfNS0_9allocatorIfEEEENS2_IS4_EEEENS2_IS6_EEEENS2_IS8_EEEEjjjjf : 1168 -> 1188
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l : 360 -> 364
~ -[CSPlainAudioFileWriter addSamples:numSamples:] : 344 -> 364
~ -[CSSelectiveChannelAudioFileWriter addSamples:numSamples:] : 604 -> 624
CStrings:
+ "{unique_ptr<BatchBeepCanceller, std::default_delete<BatchBeepCanceller>>=\"\"{?=\"__ptr_\"^{BatchBeepCanceller}}}"
+ "{unique_ptr<CSAudioSpectralMeterImpl, std::default_delete<CSAudioSpectralMeterImpl>>=\"\"{?=\"__ptr_\"^{CSAudioSpectralMeterImpl}}}"
+ "{unique_ptr<CSAudioZeroFilterImpl<unsigned short>, std::default_delete<CSAudioZeroFilterImpl<unsigned short>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{unique_ptr<corespeech::CSAudioCircularBufferImpl<unsigned short>, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned short>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"\"{?=\"__cap_\"^f}}"
+ "{vector<short, std::allocator<short>>=\"__begin_\"^s\"__end_\"^s\"\"{?=\"__cap_\"^s}}"
- "{unique_ptr<BatchBeepCanceller, std::default_delete<BatchBeepCanceller>>=\"__ptr_\"^{BatchBeepCanceller}}"
- "{unique_ptr<CSAudioSpectralMeterImpl, std::default_delete<CSAudioSpectralMeterImpl>>=\"__ptr_\"^{CSAudioSpectralMeterImpl}}"
- "{unique_ptr<CSAudioZeroFilterImpl<unsigned short>, std::default_delete<CSAudioZeroFilterImpl<unsigned short>>>=\"__ptr_\"^v}"
- "{unique_ptr<corespeech::CSAudioCircularBufferImpl<unsigned short>, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned short>>>=\"__ptr_\"^v}"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
- "{vector<short, std::allocator<short>>=\"__begin_\"^s\"__end_\"^s\"__cap_\"^s}"

```
