## SiriAudioSupport

> `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport`

```diff

-3402.63.2.0.0
-  __TEXT.__text: 0x2265f8
-  __TEXT.__auth_stubs: 0x3880
+3403.2.1.0.0
+  __TEXT.__text: 0x229704
+  __TEXT.__auth_stubs: 0x3980
   __TEXT.__objc_methlist: 0x834
-  __TEXT.__const: 0xa3e8
-  __TEXT.__cstring: 0xb3e0
-  __TEXT.__swift5_typeref: 0x4279
-  __TEXT.__swift5_fieldmd: 0x4500
-  __TEXT.__constg_swiftt: 0x5d60
+  __TEXT.__const: 0xa528
+  __TEXT.__cstring: 0xb400
+  __TEXT.__swift5_typeref: 0x42ef
+  __TEXT.__swift5_fieldmd: 0x4550
+  __TEXT.__constg_swiftt: 0x5dc8
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x48bc
-  __TEXT.__swift5_assocty: 0x648
+  __TEXT.__swift5_reflstr: 0x48dc
+  __TEXT.__swift5_assocty: 0x678
   __TEXT.__swift5_protos: 0x11c
-  __TEXT.__swift5_proto: 0x634
-  __TEXT.__swift5_types: 0x444
+  __TEXT.__swift5_proto: 0x63c
+  __TEXT.__swift5_types: 0x44c
   __TEXT.__swift5_capture: 0x54f4
-  __TEXT.__oslogstring: 0x1fc1e
+  __TEXT.__oslogstring: 0x1fcfe
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4af8
-  __TEXT.__eh_frame: 0x33b4
+  __TEXT.__unwind_info: 0x4bb8
+  __TEXT.__eh_frame: 0x3784
   __TEXT.__objc_classname: 0x19c
   __TEXT.__objc_methname: 0x6308
   __TEXT.__objc_methtype: 0x696
-  __DATA_CONST.__got: 0x1108
+  __DATA_CONST.__got: 0x1120
   __DATA_CONST.__const: 0x888
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1cf8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x1c40
-  __AUTH_CONST.__auth_ptr: 0x1710
-  __AUTH_CONST.__const: 0x155e0
+  __AUTH_CONST.__auth_got: 0x1cc0
+  __AUTH_CONST.__auth_ptr: 0x1738
+  __AUTH_CONST.__const: 0x156f8
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0xb660
   __AUTH.__objc_data: 0x1128
-  __AUTH.__data: 0x5e70
-  __DATA.__data: 0x3008
-  __DATA.__bss: 0x8b90
+  __AUTH.__data: 0x5e90
+  __DATA.__data: 0x30b8
+  __DATA.__bss: 0x8c90
   __DATA.__common: 0x2e8
   __DATA_DIRTY.__objc_data: 0xd0
   __DATA_DIRTY.__data: 0x28

   - /System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils
   - /System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment
   - /System/Library/PrivateFrameworks/SiriInference.framework/SiriInference
+  - /System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch
   - /System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8807
+  Functions: 8846
   Symbols:   1005
-  CStrings:  4121
+  CStrings:  4126
 
CStrings:
+ "AppIntentInvoker#followShowAppIntent invoking showOutputAction intent: %s"
+ "AppIntentInvoker#invokeShowMusicNoticeAppIntent ShowMusicNoticeAppIntent constructed with itemEntity: %s and noticeEntity: %s"
+ "AppIntentInvoker#invokeShowMusicNoticeAppIntent response: %s"
+ "INMediaItem#from Identifier: %s"
+ "INMediaItem#from audioMediaItem failed to create playbackItem with identifier: %s"
+ "OpenMusicItemAppIntent"
+ "PlaybackItem#toMusicSiriRepresentation is %s"
+ "PlaybackItem#toMusicSiriRepresentation musicItemTypedID is nil"
+ "PlaybackItem#toMusicSiriRepresentation musicSiriRep is nil"
+ "PlaybackItem#toMusicSiriRepresentation..."
+ "SiriKitTaskLoggingProvider#curareDonation Making curare donation of Pommes Response"
- "Identifier#toMusicSiriRepresentation failed to create musicSiriRepresentation from source: %s, type: %s, and identifier: %s"
- "MusicSiriRepresentation#from Failed to create valid URL for library content"
- "MusicSiriRepresentation#from Failed to create valid URL for store content"
- "MusicSiriRepresentation#from called with source = %s, type = %s, and identifier = %s"
- "MusicSiriRepresentation#from returning %s"
- "MusicSiriRepresentation#from unknown source type, returning nil"

```
