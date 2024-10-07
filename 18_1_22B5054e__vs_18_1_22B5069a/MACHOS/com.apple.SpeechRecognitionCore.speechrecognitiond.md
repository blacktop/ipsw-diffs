## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.22.0.0
-  __TEXT.__text: 0xbb994
+6.3.23.1.0
+  __TEXT.__text: 0xbc098
   __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_stubs: 0x37e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1318
-  __TEXT.__const: 0x596f
+  __TEXT.__const: 0x595f
+  __TEXT.__gcc_except_tab: 0x80fc
   __TEXT.__objc_methname: 0x48e5
-  __TEXT.__cstring: 0x3c91
-  __TEXT.__oslogstring: 0x47fb
+  __TEXT.__cstring: 0x3d11
+  __TEXT.__oslogstring: 0x48cb
   __TEXT.__objc_classname: 0x307
   __TEXT.__objc_methtype: 0xf13
-  __TEXT.__gcc_except_tab: 0x80b8
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__swift5_typeref: 0x398
+  __TEXT.__swift5_typeref: 0x39a
   __TEXT.__swift5_capture: 0x1e8
   __TEXT.__constg_swiftt: 0x58c
   __TEXT.__swift5_reflstr: 0x1f8
   __TEXT.__swift5_fieldmd: 0x208
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3fa8
-  __TEXT.__eh_frame: 0x930
+  __TEXT.__unwind_info: 0x3fb8
+  __TEXT.__eh_frame: 0x958
   __DATA_CONST.__auth_got: 0x1370
   __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__auth_ptr: 0x148
   __DATA_CONST.__const: 0x6948
-  __DATA_CONST.__cfstring: 0x1c60
+  __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3493
+  Functions: 3494
   Symbols:   1318
-  CStrings:  2150
+  CStrings:  2157
 
Symbols:
+ __ZN11RDQSREngine16RestartASREngineEPK10__CFString
- __ZN11RDQSREngine16RestartASREngineEv
CStrings:
+ "ASRWrapper created audio buffer"
+ "ASRWrapper created recognizer"
+ "AudioBuffer is nil."
+ "AudioBuffer was Nil"
+ "Could not attach Transcriber to SpeechAnalyzer %!@(MISSING)"
+ "Could not attach analysis context to SpeechAnalyzer = %!@(MISSING)"
+ "Could not initialize audio buffer"
+ "Could not set recognition replacements = %!@(MISSING)"
+ "Exception thrown in recognition"
+ "Restarting ASR Engine(%!{(MISSING)public}@)"
+ "SpeechAnalyzerObjC recognition failed with task %!@(MISSING)"
+ "SpeechAnalyzerObjC transcriber could not be initialized"
+ "Terminating to restart EAR (%!{(MISSING)public}@)"
+ "Timed out waiting to get attach transcriber. "
- "ASRWrapper create audio buffer"
- "ASRWrapper create recognizer"
- "Audio Buffer is nil."
- "Could not attach Transcriber to SpeechAnalyzer"
- "Could not attach analysis context to SpeechAnalyzer"
- "Could not set recognition replacements"
- "Not Resetting Recognition as AudioBuffer is Nil"
- "Restarting ASR Engine"
- "Terminating to restart EAR"

```
