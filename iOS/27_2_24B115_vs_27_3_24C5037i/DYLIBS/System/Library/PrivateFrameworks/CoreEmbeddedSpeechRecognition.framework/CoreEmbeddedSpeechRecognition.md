## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

-3605.14.1.0.0
-  __TEXT.__text: 0x349850
+3610.5.1.0.0
+  __TEXT.__text: 0x35cc10
   __TEXT.__objc_methlist: 0x4f00
-  __TEXT.__const: 0x9628
-  __TEXT.__cstring: 0xeb7d
+  __TEXT.__const: 0x9778
+  __TEXT.__cstring: 0xebfd
   __TEXT.__gcc_except_tab: 0xd80
-  __TEXT.__oslogstring: 0xd1d5
+  __TEXT.__oslogstring: 0xd4a5
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0xdc
-  __TEXT.__swift5_typeref: 0x4546
-  __TEXT.__constg_swiftt: 0x28f4
-  __TEXT.__swift5_reflstr: 0x2e23
-  __TEXT.__swift5_fieldmd: 0x2cd8
+  __TEXT.__swift5_typeref: 0x45ec
+  __TEXT.__constg_swiftt: 0x2944
+  __TEXT.__swift5_reflstr: 0x2f93
+  __TEXT.__swift5_fieldmd: 0x2dac
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_assocty: 0x600
-  __TEXT.__swift5_proto: 0x55c
-  __TEXT.__swift5_types: 0x2d0
-  __TEXT.__swift5_capture: 0xcc14
+  __TEXT.__swift5_proto: 0x564
+  __TEXT.__swift5_types: 0x2d8
+  __TEXT.__swift5_capture: 0xd264
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift_as_entry: 0x260
-  __TEXT.__swift_as_ret: 0x2dc
-  __TEXT.__swift_as_cont: 0x6e4
+  __TEXT.__swift_as_entry: 0x274
+  __TEXT.__swift_as_ret: 0x2ec
+  __TEXT.__swift_as_cont: 0x718
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xb880
-  __TEXT.__eh_frame: 0x5e8c
+  __TEXT.__unwind_info: 0xbc20
+  __TEXT.__eh_frame: 0x603c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x478
-  __DATA_CONST.__got: 0x1b08
-  __AUTH_CONST.__const: 0x23ea0
+  __DATA_CONST.__got: 0x1b50
+  __AUTH_CONST.__const: 0x24eb8
   __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0xba80
+  __AUTH_CONST.__objc_const: 0xbae0
   __AUTH_CONST.__objc_intobj: 0xeb8
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x23e8
+  __AUTH_CONST.__auth_got: 0x24b0
   __AUTH.__objc_data: 0x1128
-  __AUTH.__data: 0xb60
-  __DATA.__objc_ivar: 0x530
-  __DATA.__data: 0x2810
+  __AUTH.__data: 0xc90
+  __DATA.__objc_ivar: 0x534
+  __DATA.__data: 0x28b0
   __DATA.__common: 0x108
   __DATA_DIRTY.__objc_data: 0x1d30
-  __DATA_DIRTY.__data: 0x42e0
+  __DATA_DIRTY.__data: 0x42c0
   __DATA_DIRTY.__bss: 0x4068
   __DATA_DIRTY.__common: 0x188
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11448
-  Symbols:   4996
-  CStrings:  2564
+  Functions: 11672
+  Symbols:   5012
+  CStrings:  2575
 
Symbols:
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._pendingCascadeSetsTransaction
+ _symbolic Say_____GSg 6Speech21PersonalEntityMentionV
+ _symbolic Shy_____G 6Speech17ServerTranscriberC15ReportingOptionO
+ _symbolic Shy_____G 6Speech17ServerTranscriberC19TranscriptionOptionO
+ _symbolic Shy_____G 6Speech17ServerTranscriberC21ResultAttributeOptionO
+ _symbolic Shy_____GIegr_ 6Speech17ServerTranscriberC15ReportingOptionO
+ _symbolic Shy_____GIegr_ 6Speech17ServerTranscriberC19TranscriptionOptionO
+ _symbolic Shy_____GIegr_ 6Speech17ServerTranscriberC21ResultAttributeOptionO
+ _symbolic _____ 29CoreEmbeddedSpeechRecognition23ServerTranscriberResultV
+ _symbolic _____ 29CoreEmbeddedSpeechRecognition31CombinedServerTranscriberOutputV
+ _symbolic _____ 6Speech13EARResultTypeO
+ _symbolic _____ 6Speech17ServerTranscriberC6ResultV
+ _symbolic _____Sg 29CoreEmbeddedSpeechRecognition31CombinedServerTranscriberOutputV
+ _symbolic _____Sg 6Speech6AssetsV
+ _symbolic _____y_Qo_ 6Speech17ServerTranscriberC7resultsQrvpQO
+ _symbolic _____y_____y_Qo______G s16AsyncMapSequenceV 6Speech17ServerTranscriberC7resultsQrvpQO 012CoreEmbeddedD11Recognition08CombinedeF6OutputV
CStrings:
+ "%s: Emergency mode with missing on-device assets for locale: %{public}s; falling back to ServerTranscriber"
+ "%s: Not in emergency orchestration mode; no server fallback"
+ "%s: On-device assets already installed for locale: %{public}s; no server fallback needed"
+ "Configuring ServerTranscriber with:\n- transcriptionOptions: %s\n- reportingOptions: %s\n- attributeOptions: %s"
+ "Configuring analyzer to produce ServerTranscriber results."
+ "Receiving ServerTranscriber results."
+ "ServerTranscriber unexpectedly produced a %{public}s result; ignoring"
+ "Skipping on-screen context entity retrieval — using ServerTranscriber for requestId %s"
+ "Using ServerTranscriber for this request"
+ "analyzerDidProduceServerTranscriberResult(_:)"
+ "com.apple.corespeechd.pendingcascadesets"
+ "shouldUseServerTranscriber(locale:taskHint:)"
- "\t"
```
