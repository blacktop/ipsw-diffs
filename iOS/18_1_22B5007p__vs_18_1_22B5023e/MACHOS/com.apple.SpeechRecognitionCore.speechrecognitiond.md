## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.15.0.0
-  __TEXT.__text: 0xba1bc
-  __TEXT.__auth_stubs: 0x25f0
+6.3.19.0.0
+  __TEXT.__text: 0xbb15c
+  __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_stubs: 0x37e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x12c0
-  __TEXT.__const: 0x597f
-  __TEXT.__objc_methname: 0x484b
-  __TEXT.__cstring: 0x3c79
-  __TEXT.__oslogstring: 0x45ab
+  __TEXT.__objc_methlist: 0x1318
+  __TEXT.__const: 0x596f
+  __TEXT.__objc_methname: 0x48e5
+  __TEXT.__cstring: 0x3c01
+  __TEXT.__oslogstring: 0x477b
   __TEXT.__objc_classname: 0x307
-  __TEXT.__objc_methtype: 0xefa
-  __TEXT.__gcc_except_tab: 0x8094
+  __TEXT.__objc_methtype: 0xf13
+  __TEXT.__gcc_except_tab: 0x80b8
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__swift5_typeref: 0x390
-  __TEXT.__swift5_capture: 0x1b4
-  __TEXT.__constg_swiftt: 0x544
-  __TEXT.__swift5_reflstr: 0x1e8
-  __TEXT.__swift5_fieldmd: 0x1f0
+  __TEXT.__swift5_typeref: 0x398
+  __TEXT.__swift5_capture: 0x1e8
+  __TEXT.__constg_swiftt: 0x58c
+  __TEXT.__swift5_reflstr: 0x1f8
+  __TEXT.__swift5_fieldmd: 0x208
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3f80
-  __TEXT.__eh_frame: 0x8c8
-  __DATA_CONST.__auth_got: 0x1310
-  __DATA_CONST.__got: 0x6b0
+  __TEXT.__unwind_info: 0x3f78
+  __TEXT.__eh_frame: 0x930
+  __DATA_CONST.__auth_got: 0x1370
+  __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x6898
-  __DATA_CONST.__cfstring: 0x1c60
+  __DATA_CONST.__const: 0x68c8
+  __DATA_CONST.__cfstring: 0x1be0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x3688
-  __DATA.__objc_selrefs: 0x10f8
-  __DATA.__objc_ivar: 0x164
-  __DATA.__objc_data: 0xe58
-  __DATA.__data: 0xd38
-  __DATA.__bss: 0xaf0
+  __DATA.__objc_const: 0x3ab8
+  __DATA.__objc_selrefs: 0x1120
+  __DATA.__objc_ivar: 0x16c
+  __DATA.__objc_data: 0xeb0
+  __DATA.__data: 0xd40
+  __DATA.__bss: 0xb00
   __DATA.__common: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3477
-  Symbols:   1306
-  CStrings:  2125
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3480
+  Symbols:   1309
+  CStrings:  2140
 
Symbols:
+ __ZN11RDQSREngine12DonateSpeechEv
+ __ZN11RDQSREngine27DidGetUtteranceTotalSamplesEx
+ __ZN11RDQSREngine35DidGetUtteranceTotalSamplesCallbackEPvx
+ __ZN11RDQSREngine36kCircularBufferSizeForSpeechDonationE
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- __ZN11RDQSREngine11SpeechEndedEv
- __ZN11RDQSREngine13SpeechStartedEv
- __ZN11RDQSREngine14KeywordSpottedEPK10__CFStringd
- __ZN11RDQSREngine16saveAudioSamplesEPKsl
- __ZN11RDQSREngine19SpeechEndedCallbackEPv
- __ZN11RDQSREngine21KeywordSpotterDidStopEv
- __ZN11RDQSREngine21SpeechStartedCallbackEPv
- __ZN11RDQSREngine22KeywordSpottedCallbackEPvPK10__CFStringd
- __ZN11RDQSREngine29KeywordSpotterDidStopCallbackEPv
CStrings:
+ "/tmp/lastDonation.caf"
+ "AF notification didChangeStateFrom %!l(MISSING)ld to %!l(MISSING)ld "
+ "CS notification didChangeStateFrom %!l(MISSING)ld to %!l(MISSING)ld "
+ "Called the callback with partial results = %!@(MISSING)"
+ "Calling didRecognizePartialResultTokens"
+ "CarPlay Active?: %!@(MISSING)"
+ "Siri is idle: %!@(MISSING)"
+ "Siri is listening: %!@(MISSING)"
+ "Siri is speaking: %!@(MISSING)"
+ "Speech detection VAD status changed = %!@(MISSING)"
+ "SpeechAnalyzer finalAndTerminal results"
+ "SpeechAnalyzer partial results"
+ "SpeechAnalyzerObjC recognition started with task %!@(MISSING)"
+ "Start recording Independent VAD since Siri is Idle"
+ "Start recording from CoreSpeech in CarPlay since Siri is Idle"
+ "Stop recording from CoreSpeech in CarPlay since Siri is active"
+ "Stop recording from Independent VAD since Siri is active"
+ "TC,N,V_isSiriIdle"
+ "T^{RDASRWDelegate=^v^?^?^?^?^?^?^?},N,V_recognitionDelegate"
+ "T^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?^?},N,V_delegate"
+ "VoiceControl::SpeechDonation::DonationID is nil"
+ "VoiceControl::SpeechDonation::DonationID, error opening file"
+ "VoiceControl::SpeechDonation::DonationID, error writing to file"
+ "VoiceControl::SpeechDonation::DonationID=%!s(MISSING)"
+ "^v32@0:8^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?^?}16@24"
+ "^{RDASRWDelegate=^v^?^?^?^?^?^?^?}"
+ "^{RDASRWDelegate=^v^?^?^?^?^?^?^?}16@0:8"
+ "^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?^?}"
+ "^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?^?}16@0:8"
+ "_isSiriIdle"
+ "audioPath"
+ "close"
+ "didGetUtteranceTotalSamples:"
+ "didRecognizePartialResultTokens:"
+ "donateAudioFor:logAudioFile:"
+ "donateWithAudioBuffers:logAudioFile:"
+ "file"
+ "isSiriIdle"
+ "setIsSiriIdle:"
+ "v24@0:8^{RDASRWDelegate=^v^?^?^?^?^?^?^?}16"
+ "v24@0:8^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?^?}16"
+ "v24@0:8q16"
- "CS notification didChangeStateFrom %!l(MISSING)lu to %!l(MISSING)lu "
- "Got callback from SpeechAnalyzer with results"
- "Siri is NOT listening, so resume sending audio"
- "Siri is done speaking, so resume sending audio"
- "Siri is listening, so stop sending audio"
- "Siri is speaking, so stop sending audio"
- "Speech dectection VAD status changed = %!@(MISSING)"
- "SpeechAnalyzerObjC recognition started"
- "T^{RDASRWDelegate=^v^?^?^?^?^?^?},N,V_recognitionDelegate"
- "T^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?},N,V_delegate"
- "^v32@0:8^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?}16@24"
- "^{RDASRWDelegate=^v^?^?^?^?^?^?}"
- "^{RDASRWDelegate=^v^?^?^?^?^?^?}16@0:8"
- "^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?}"
- "^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?}16@0:8"
- "donateAudioFor:"
- "donateWithAudioBuffers:"
- "keyword spotted == %!@(MISSING), cost=%!f(MISSING)"
- "keyword spotter stopped"
- "open_siri OH p un <w> s EE r ee <w>"
- "show_siri sh OH <w> s EE r ee <w>"
- "speech ended"
- "speech started"
- "start_listening s t AH r t <w> l IH s un ih ng <w>"
- "v24@0:8^{RDASRWDelegate=^v^?^?^?^?^?^?}16"
- "v24@0:8^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?}16"
- "wake_up w EY k <w> uh p <w>"

```
