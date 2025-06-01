## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

```diff

-165.13.100.0.0
-  __TEXT.__text: 0x183e4
+165.19.0.0.0
+  __TEXT.__text: 0x18a34
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x1100
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x1747
-  __TEXT.__oslogstring: 0x7c6
+  __TEXT.__oslogstring: 0x823
   __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__unwind_info: 0x66c
+  __TEXT.__unwind_info: 0x698
   __TEXT.__objc_classname: 0x72f
-  __TEXT.__objc_methname: 0x48c5
+  __TEXT.__objc_methname: 0x4913
   __TEXT.__objc_methtype: 0x165b
-  __TEXT.__objc_stubs: 0x3500
+  __TEXT.__objc_stubs: 0x3540
   __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5fc8
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_selrefs: 0xe58
   __AUTH_CONST.__objc_const: 0x8b8
   __AUTH_CONST.__cfstring: 0x1500
   __AUTH_CONST.__const: 0x160

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78BE8B79-DC0F-3616-9E6A-BBDCBB499F02
-  Functions: 588
-  Symbols:   2469
-  CStrings:  1378
+  UUID: 3115A719-70C6-3447-BD14-8458843E012D
+  Functions: 595
+  Symbols:   2486
+  CStrings:  1381
 
Symbols:
+ ___52-[STLocalStatusServer addDataTransformer:forDomain:]_block_invoke_2
+ ___55-[STLocalStatusServer removeDataTransformer:forDomain:]_block_invoke_2
+ ___66-[STLocalStatusServer addClientDataTransformerProvider:forDomain:]_block_invoke_2
+ ___66-[STLocalStatusServer modifyDataTransformer:forDomain:usingBlock:]_block_invoke_2
+ ___68-[STMediaStatusDomainDisplayNameTransformer transformedDataForData:]_block_invoke_7
+ ___68-[STMediaStatusDomainDisplayNameTransformer transformedDataForData:]_block_invoke_8
+ ___69-[STLocalStatusServer removeClientDataTransformerProvider:forDomain:]_block_invoke_2
+ ___80-[STLocalStatusServer modifyClientDataTransformerProvider:forDomain:usingBlock:]_block_invoke_2
+ ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.137
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_literal_global.5
+ ___block_literal_global.8
+ _objc_msgSend$microphoneRecordingAttributions
+ _objc_msgSend$mutedMicrophoneRecordingAttributions
+ _objc_msgSend$setMicrophoneRecordingAttributions:
+ _objc_msgSend$setMutedMicrophoneRecordingAttributions:
+ _objc_msgSend$setSystemAudioRecordingAttributions:
+ _objc_msgSend$systemAudioRecordingAttributions
- ___75-[STLocalStatusServer _internalQueue_handleDataTransformerChangeForDomain:]_block_invoke
- ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.139
- ___block_literal_global.136
- ___block_literal_global.6
- _objc_msgSend$audioRecordingAttributionList
- _objc_msgSend$mutedAudioRecordingAttributionList
- _objc_msgSend$setAudioRecordingAttributionList:
- _objc_msgSend$setMutedAudioRecordingAttributionList:
CStrings:
+ "Entity resolver: %{public}@ -- updating dynamic attributions from: %{public}@ to: %{public}@"
+ "microphoneRecordingAttributions"
+ "mutedMicrophoneRecordingAttributions"
+ "setMicrophoneRecordingAttributions:"
+ "setMutedMicrophoneRecordingAttributions:"
+ "setSystemAudioRecordingAttributions:"
+ "systemAudioRecordingAttributions"
- "audioRecordingAttributionList"
- "mutedAudioRecordingAttributionList"
- "setAudioRecordingAttributionList:"
- "setMutedAudioRecordingAttributionList:"

```
