## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.19.0.0
-  __TEXT.__text: 0xbb15c
+6.3.20.0.0
+  __TEXT.__text: 0xbb994
   __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_stubs: 0x37e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1318
   __TEXT.__const: 0x596f
   __TEXT.__objc_methname: 0x48e5
-  __TEXT.__cstring: 0x3c01
-  __TEXT.__oslogstring: 0x477b
+  __TEXT.__cstring: 0x3c91
+  __TEXT.__oslogstring: 0x47fb
   __TEXT.__objc_classname: 0x307
   __TEXT.__objc_methtype: 0xf13
   __TEXT.__gcc_except_tab: 0x80b8

   __TEXT.__swift5_fieldmd: 0x208
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3f78
+  __TEXT.__unwind_info: 0x3fa8
   __TEXT.__eh_frame: 0x930
   __DATA_CONST.__auth_got: 0x1370
   __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x68c8
-  __DATA_CONST.__cfstring: 0x1be0
+  __DATA_CONST.__const: 0x6948
+  __DATA_CONST.__cfstring: 0x1c60
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3480
-  Symbols:   1309
-  CStrings:  2140
+  Functions: 3493
+  Symbols:   1318
+  CStrings:  2150
 
Symbols:
+ __ZN11RDQSREngine22KeywordSpottedCallbackEPvPK10__CFStringd
+ __ZN11RDQSREngine14KeywordSpottedEPK10__CFStringd
+ __ZN11RDQSREngine19SpeechEndedCallbackEPv
+ __ZN11RDQSREngine11SpeechEndedEv
+ __ZN11RDQSREngine21SpeechStartedCallbackEPv
+ __ZN11RDQSREngine16saveAudioSamplesEPKsl
+ __ZN11RDQSREngine29KeywordSpotterDidStopCallbackEPv
+ __ZN11RDQSREngine21KeywordSpotterDidStopEv
+ __ZN11RDQSREngine13SpeechStartedEv
CStrings:
+ "wait for the async blocks"
+ "keyword spotted == %!@(MISSING), cost=%!f(MISSING)"
+ "keyword spotter stopped"
+ "speech ended"
+ "open_siri OH p un <w> s EE r ee <w>"
+ "wake_up w EY k <w> uh p <w>"
+ "start_listening s t AH r t <w> l IH s un ih ng <w>"
+ "show_siri sh OH <w> s EE r ee <w>"
+ "speech started"
+ "released RDAudioBufferQueue"

```
