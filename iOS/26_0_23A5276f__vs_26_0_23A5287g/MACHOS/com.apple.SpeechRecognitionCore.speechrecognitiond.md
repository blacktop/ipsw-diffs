## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.57.0.0
-  __TEXT.__text: 0xd4668
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_stubs: 0x3440
+6.3.60.0.0
+  __TEXT.__text: 0xd4c24
+  __TEXT.__auth_stubs: 0x27e0
+  __TEXT.__objc_stubs: 0x3420
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x18d4
-  __TEXT.__const: 0x6476
-  __TEXT.__gcc_except_tab: 0x9480
-  __TEXT.__objc_methname: 0x49c2
-  __TEXT.__cstring: 0x41a2
-  __TEXT.__oslogstring: 0x55b4
+  __TEXT.__const: 0x6546
+  __TEXT.__gcc_except_tab: 0x9438
+  __TEXT.__objc_methname: 0x49a1
+  __TEXT.__cstring: 0x4142
+  __TEXT.__oslogstring: 0x5554
   __TEXT.__objc_classname: 0x348
-  __TEXT.__objc_methtype: 0x1003
+  __TEXT.__objc_methtype: 0x1012
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xd34
-  __TEXT.__swift5_reflstr: 0x7b8
+  __TEXT.__swift5_reflstr: 0x798
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_fieldmd: 0x784
+  __TEXT.__swift5_fieldmd: 0x778
   __TEXT.__constg_swiftt: 0x11c0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_capture: 0x594
+  __TEXT.__swift5_capture: 0x5d4
   __TEXT.__swift5_types: 0xa8
   __TEXT.__swift_as_entry: 0xa0
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x4b98
-  __TEXT.__eh_frame: 0x36fc
-  __DATA_CONST.__auth_got: 0x1408
+  __TEXT.__unwind_info: 0x4bb8
+  __TEXT.__eh_frame: 0x36dc
+  __DATA_CONST.__auth_got: 0x1410
   __DATA_CONST.__got: 0x790
   __DATA_CONST.__auth_ptr: 0x278
-  __DATA_CONST.__const: 0x7670
+  __DATA_CONST.__const: 0x76f8
   __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2cd0
-  __DATA.__objc_selrefs: 0x12b0
+  __DATA.__objc_const: 0x2cb0
+  __DATA.__objc_selrefs: 0x12a8
   __DATA.__objc_ivar: 0x140
-  __DATA.__objc_data: 0x1490
+  __DATA.__objc_data: 0x1488
   __DATA.__data: 0xfb8
-  __DATA.__bss: 0x1010
+  __DATA.__bss: 0x1000
   __DATA.__common: 0xa6
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5495C7F1-3818-363E-918C-B88147F02EF6
-  Functions: 3783
+  UUID: ABAC9E9C-5323-353D-A10B-984357D788A3
+  Functions: 3794
   Symbols:   1134
-  CStrings:  2462
+  CStrings:  2459
 
Symbols:
+ __ZN11RDQSREngine20BuildCombinedGrammarEb
+ __ZN11RDQSREngine22UpdateUserProfileCacheEv
+ __ZN13RDUserProfile33updateUserProfileWithPersonalDataEbNSt3__18functionIFvbEEE
- __ZN11RDQSREngine20BuildCombinedGrammarEv
- __ZN13RDUserProfile28removeLmeDataForTemplateNameEPK10__CFString
- __ZN13RDUserProfile33updateUserProfileWithPersonalDataENSt3__18functionIFvbEEE
CStrings:
+ "Building Grammar for category %s"
+ "RDQSREngine::LoadCustomVocabulary ### phoneticVocabularyMode: %{public}ld, firstTime: %{public}d"
+ "updateUserProfileWithPersonalData:completion:"
+ "v28@0:8B16@?20"
- "AVC: Error setting MX propery for supressing recording state. %@"
- "PrefersSuppressingRecordingState"
- "RDQSREngine::LoadCustomVocabulary ### phoneticVocabularyMode: %{public}ld, set_flag: %{public}d"
- "SRC:Failed to suppress mic indicator"
- "isExclaveCapability"
- "setPrefersNoMicrophoneUsageIndicator:error:"
- "updateUserProfileWithPersonalData:"

```
