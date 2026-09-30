## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.68.6.0
-  __TEXT.__text: 0xc81dc
-  __TEXT.__auth_stubs: 0x2680
+6.3.68.7.0
+  __TEXT.__text: 0xca5f4
+  __TEXT.__auth_stubs: 0x2740
   __TEXT.__objc_stubs: 0x34a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x18d4
-  __TEXT.__const: 0x5f36
-  __TEXT.__gcc_except_tab: 0xa320
-  __TEXT.__objc_methname: 0x4a7c
-  __TEXT.__cstring: 0x40b6
-  __TEXT.__oslogstring: 0x5744
+  __TEXT.__objc_methlist: 0x190c
+  __TEXT.__const: 0x6016
+  __TEXT.__gcc_except_tab: 0xa558
+  __TEXT.__objc_methname: 0x4aaa
+  __TEXT.__cstring: 0x4136
+  __TEXT.__oslogstring: 0x56f4
   __TEXT.__objc_classname: 0x348
   __TEXT.__objc_methtype: 0x1012
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__ustring: 0x4
+  __TEXT.__constg_swiftt: 0xbdc
+  __TEXT.__swift5_typeref: 0x7c8
+  __TEXT.__swift5_reflstr: 0x508
+  __TEXT.__swift5_fieldmd: 0x534
+  __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xb94
-  __TEXT.__swift5_typeref: 0x736
-  __TEXT.__swift5_reflstr: 0x4c8
-  __TEXT.__swift5_fieldmd: 0x4cc
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_capture: 0x49c
-  __TEXT.__swift5_types: 0x58
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x47c8
-  __TEXT.__eh_frame: 0x2ba4
-  __DATA_CONST.__auth_got: 0x1360
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__auth_ptr: 0x1c8
-  __DATA_CONST.__const: 0x6ed8
-  __DATA_CONST.__cfstring: 0x1ce0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__unwind_info: 0x48c0
+  __TEXT.__eh_frame: 0x2f64
+  __DATA_CONST.__auth_got: 0x13c0
+  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__auth_ptr: 0x1e0
+  __DATA_CONST.__const: 0x7130
+  __DATA_CONST.__cfstring: 0x1d20
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2cc0
-  __DATA.__objc_selrefs: 0x12f0
+  __DATA.__objc_const: 0x2d08
+  __DATA.__objc_selrefs: 0x1310
   __DATA.__objc_ivar: 0x140
-  __DATA.__objc_data: 0x14b0
-  __DATA.__data: 0xf68
+  __DATA.__objc_data: 0x1560
+  __DATA.__data: 0xfd8
   __DATA.__bss: 0x470
   __DATA.__common: 0xa6
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DF66F57F-F54F-3BDE-B023-37FDCF9273B9
-  Functions: 3574
-  Symbols:   1122
-  CStrings:  2499
+  UUID: 7F3B279B-BF11-3401-9C39-07AADC8296C1
+  Functions: 3615
+  Symbols:   1129
+  CStrings:  2507
 
Symbols:
+ _CFArrayCreateMutableCopy
+ _CFDictionaryCreate
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$__TtC50com_apple_SpeechRecognitionCore_speechrecognitiond21VCPreloadedVocabulary
+ _OBJC_METACLASS_$__TtC50com_apple_SpeechRecognitionCore_speechrecognitiond21VCPreloadedVocabulary
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
CStrings:
+ "%@%@"
+ "AVC: System is sleeping, so don't start recording"
+ "Activating Grammar  -> lmid = %llu, grammarID = %zu, %{public}@"
+ "Deactivating Grammar  -> lmid = %llu, grammarID = %zu, %{public}@"
+ "Deactivating Grammar after end of utterance -> lmid = %llu, grammarID = %zu, %{public}@"
+ "IsPreloaded"
+ "_TtC50com_apple_SpeechRecognitionCore_speechrecognitiond21VCPreloadedVocabulary"
+ "arrayLock"
+ "entriesForVocabularyInjectionWithLocale:"
+ "lock"
+ "setHasSpaceAfter:"
+ "setHasSpaceBefore:"
+ "unlock"
+ "ˈnu.ˈpæ.ɻə.ˈgɻæf"
- "AVC: System is sleeping, so don't strat recording"
- "Activating Grammar  -> lmid = %llu, grammarID = %zu, %@"
- "Deactivating Grammar  -> lmid = %llu, grammarID = %zu, %@"
- "Deactivating Grammar after end of utterance -> lmid = %llu, grammarID = %zu, %@"
- "RDQSREngine::LoadCustomVocabulary: prefValue is NULL."
- "SRC:Failed to suppress mic indicator"
- "setPrefersNoMicrophoneUsageIndicator:error:"
- "writeLinearIndex"

```
