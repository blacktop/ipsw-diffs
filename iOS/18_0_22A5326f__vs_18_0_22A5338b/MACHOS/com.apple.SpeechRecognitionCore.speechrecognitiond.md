## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.18.0.0
-  __TEXT.__text: 0xb94dc
-  __TEXT.__auth_stubs: 0x25f0
+6.3.19.0.0
+  __TEXT.__text: 0xbb15c
+  __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_stubs: 0x37e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x12c0
-  __TEXT.__const: 0x597f
-  __TEXT.__objc_methname: 0x484b
-  __TEXT.__cstring: 0x3be9
-  __TEXT.__oslogstring: 0x455b
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
-  __TEXT.__swift5_typeref: 0x38e
-  __TEXT.__swift5_capture: 0x1dc
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
-  __TEXT.__unwind_info: 0x3f50
-  __TEXT.__eh_frame: 0x8c0
-  __DATA_CONST.__auth_got: 0x1310
-  __DATA_CONST.__got: 0x6b0
+  __TEXT.__unwind_info: 0x3f78
+  __TEXT.__eh_frame: 0x930
+  __DATA_CONST.__auth_got: 0x1370
+  __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x68a8
+  __DATA_CONST.__const: 0x68c8
   __DATA_CONST.__cfstring: 0x1be0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x3688
-  __DATA.__objc_selrefs: 0x10f8
-  __DATA.__objc_ivar: 0x164
-  __DATA.__objc_data: 0xe58
-  __DATA.__data: 0xd48
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

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3464
-  Symbols:   1305
-  CStrings:  2117
+  Functions: 3480
+  Symbols:   1309
+  CStrings:  2140
 
Symbols:
+ __ZN11RDQSREngine12DonateSpeechEv
+ __ZN11RDQSREngine27DidGetUtteranceTotalSamplesEx
+ __ZN11RDQSREngine35DidGetUtteranceTotalSamplesCallbackEPvx
+ __ZN11RDQSREngine36kCircularBufferSizeForSpeechDonationE
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
- "v24@0:8^{RDASRWDelegate=^v^?^?^?^?^?^?}16"
- "v24@0:8^{RDSAPICSpeechAnalyzerDelegate=^v^?^?^?^?^?^?}16"

```
