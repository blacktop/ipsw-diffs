## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

 3510.3.1.0.0
-  __TEXT.__text: 0x152a5c
+  __TEXT.__text: 0x152a88
   __TEXT.__auth_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x1440c
   __TEXT.__const: 0x58c

   __TEXT.__unwind_info: 0x4dc8
   __TEXT.__objc_classname: 0x2e76
   __TEXT.__objc_methname: 0x37c57
-  __TEXT.__objc_methtype: 0x7a71
+  __TEXT.__objc_methtype: 0x7a83
   __TEXT.__objc_stubs: 0x1c040
   __DATA_CONST.__got: 0x1ab0
   __DATA_CONST.__const: 0x40f8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B20DF82-9DFC-32DA-A73B-0900AA08A12B
+  UUID: 3EBF11FE-719C-3C0A-B35F-0430C018C134
   Functions: 7926
   Symbols:   26053
   CStrings:  15516
Functions:
~ __ZN22NonlinearBeepCanceller15fcn_vector_initERNSt3__16vectorINS1_INS1_INS1_IfNS0_9allocatorIfEEEENS2_IS4_EEEENS2_IS6_EEEENS2_IS8_EEEEjjjjf : 1168 -> 1188
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l : 360 -> 364
~ -[NviAudioFileWriter addSamples:numSamples:] : 316 -> 336
CStrings:
+ "{unique_ptr<SmartSiriVolume, std::default_delete<SmartSiriVolume>>=\"\"{?=\"__ptr_\"^{SmartSiriVolume}}}"
+ "{unique_ptr<corespeech::CSAudioCircularBufferImpl<unsigned char>, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned char>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"\"{?=\"__cap_\"^f}}"
- "{unique_ptr<SmartSiriVolume, std::default_delete<SmartSiriVolume>>=\"__ptr_\"^{SmartSiriVolume}}"
- "{unique_ptr<corespeech::CSAudioCircularBufferImpl<unsigned char>, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned char>>>=\"__ptr_\"^v}"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"

```
