## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.25.0.0
-  __TEXT.__text: 0xbc0a8
-  __TEXT.__auth_stubs: 0x26b0
-  __TEXT.__objc_stubs: 0x37e0
+6.3.25.1.0
+  __TEXT.__text: 0xbe0c4
+  __TEXT.__auth_stubs: 0x2740
+  __TEXT.__objc_stubs: 0x3880
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1318
+  __TEXT.__objc_methlist: 0x1380
   __TEXT.__const: 0x595f
-  __TEXT.__gcc_except_tab: 0x80fc
-  __TEXT.__objc_methname: 0x48e5
-  __TEXT.__cstring: 0x3d11
-  __TEXT.__oslogstring: 0x48cb
+  __TEXT.__gcc_except_tab: 0x8158
+  __TEXT.__objc_methname: 0x4a6f
+  __TEXT.__cstring: 0x3e01
+  __TEXT.__oslogstring: 0x4b6b
   __TEXT.__objc_classname: 0x307
-  __TEXT.__objc_methtype: 0xf13
+  __TEXT.__objc_methtype: 0xf3d
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__swift5_typeref: 0x39a
-  __TEXT.__swift5_capture: 0x1e8
-  __TEXT.__constg_swiftt: 0x58c
-  __TEXT.__swift5_reflstr: 0x1f8
-  __TEXT.__swift5_fieldmd: 0x208
+  __TEXT.__swift5_typeref: 0x3ae
+  __TEXT.__swift5_capture: 0x228
+  __TEXT.__constg_swiftt: 0x5d4
+  __TEXT.__swift5_reflstr: 0x248
+  __TEXT.__swift5_fieldmd: 0x220
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3fb8
-  __TEXT.__eh_frame: 0x958
-  __DATA_CONST.__auth_got: 0x1370
-  __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x6948
+  __TEXT.__unwind_info: 0x4020
+  __TEXT.__eh_frame: 0xa70
+  __DATA_CONST.__auth_got: 0x13b8
+  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__auth_ptr: 0x158
+  __DATA_CONST.__const: 0x69e8
   __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x3ab8
-  __DATA.__objc_selrefs: 0x1120
-  __DATA.__objc_ivar: 0x16c
-  __DATA.__objc_data: 0xeb0
-  __DATA.__data: 0xd40
-  __DATA.__bss: 0xb00
+  __DATA.__objc_const: 0x3b58
+  __DATA.__objc_selrefs: 0x1150
+  __DATA.__objc_ivar: 0x174
+  __DATA.__objc_data: 0xf08
+  __DATA.__data: 0xd78
+  __DATA.__bss: 0xb10
   __DATA.__common: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3494
-  Symbols:   1318
-  CStrings:  2157
+  Functions: 3524
+  Symbols:   1326
+  CStrings:  2183
 
Symbols:
+ _RDASRWSpeechRecognitionAudioBufferNewUtteranceBegins
+ _RDSAPICSpeechAnalyzerNewUtteranceBegins
+ _RDSAPICSpeechAnalyzerSetRecognitionReplacements
+ __ZN11RDQSREngine23DidGetUtteranceBoundaryExx
+ __ZN11RDQSREngine31DidGetUtteranceBoundaryCallbackEPvxx
+ __ZN13RDUserProfile28removeLmeDataForTemplateNameEPK10__CFString
+ _objc_loadWeakRetained
+ _objc_retain_x28
+ _objc_retain_x9
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
- _RDSAPICSpeechAnalyzerUseRecognitionReplacements
- __ZN11RDQSREngine27DidGetUtteranceTotalSamplesEx
- __ZN11RDQSREngine35DidGetUtteranceTotalSamplesCallbackEPvx
CStrings:
+ "\x11\x12"
+ "\x12"
+ "@\"RDSAPIObjCSpeechAnalyzerAudioBuffer\""
+ "Attached transcriber to SpeechAnalyzer for recognition replacements %!d(MISSING)"
+ "Could not attach Transcriber to SpeechAnalyzer for %!@(MISSING) due to %!@(MISSING)"
+ "SpeechAnalyzer previous recognition task cancelled for %!@(MISSING)"
+ "SpeechAnalyzerObjC recognition failed for recognition replacements %!d(MISSING)"
+ "SpeechAnalyzerObjC recognition started for recognition replacements %!d(MISSING)"
+ "SpeechDonation : new utterance boundary = %!l(MISSING)ld"
+ "SpeechDonation ::totalSamplesSent =%!l(MISSING)ld ::newUtteranceBeginSampleNumber = %!l(MISSING)ld:: start = %!l(MISSING)ld :: end = %!l(MISSING)ld"
+ "SpeechDonation: Adjusted Start Sample Number = %!l(MISSING)ld, total samples to be read = %!l(MISSING)ld"
+ "SpeechDonation: Samples discarded = %!z(MISSING)u"
+ "SpeechDonation: Samples donated = %!z(MISSING)u"
+ "SpeechDonation: Start Sample Number = %!l(MISSING)ld, end Sample number = %!l(MISSING)ld"
+ "T@\"RDSAPIObjCSpeechAnalyzerAudioBuffer\",&,N,V_speechAnalyzerAudioBuffer"
+ "TC,N,V_useRecognitionReplacements"
+ "Timed out waiting to get attach transcriber for recognition replacements %!d(MISSING)"
+ "_newUtteranceBeginSampleNumber"
+ "_speechAnalyzerAudioBuffer"
+ "_totalSamplesSent"
+ "_useRecognitionReplacements"
+ "didGetUtteranceBoundary:utteranceEndSampleNumber:"
+ "new recognition task "
+ "newUtteranceBegins"
+ "removeLmeDataForTemplateName:"
+ "setRecognitionReplacementsWithUseRecognitionReplacements:completionHandler:"
+ "setSpeechAnalyzerAudioBuffer:"
+ "setUseRecognitionReplacements:"
+ "speechAnalyzerAudioBuffer"
+ "using recognition replacements "
+ "v28@0:8B16@?<v@?@\"_TtC50com_apple_SpeechRecognitionCore_speechrecognitiond28RDSAPISwiftTranscriberModule\">20"
+ "v32@0:8q16q24"
- "\x02"
- "\x11\x11"
- "Could not attach Transcriber to SpeechAnalyzer %!@(MISSING)"
- "SpeechAnalyzer previous recognition task cancelled"
- "didGetUtteranceTotalSamples:"
- "v24@0:8q16"

```
