## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.8.0.0.0
-  __TEXT.__text: 0xc77cc
+6.9.0.0.0
+  __TEXT.__text: 0xc7820
   __TEXT.__auth_stubs: 0x26d0
   __TEXT.__objc_stubs: 0x3ae0
   __TEXT.__init_offsets: 0x4

   __TEXT.__swift5_capture: 0x49c
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x4a78
+  __TEXT.__unwind_info: 0x4a88
   __TEXT.__eh_frame: 0x3058
   __DATA_CONST.__auth_got: 0x1388
   __DATA_CONST.__got: 0x778
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x7130
+  __DATA_CONST.__const: 0x7158
   __DATA_CONST.__cfstring: 0x1d20
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2C5E2054-A83B-36EA-89B0-851CCE44F24F
-  Functions: 3633
-  Symbols:   1124
+  UUID: 41B23AC8-9BEE-313E-81A4-90AC9AF9755E
+  Functions: 3637
+  Symbols:   1128
   CStrings:  2481
 
Symbols:
+ __ZN16RDQSRSoundSource23InitialRecordingStartedEv
+ __ZN20RDQSRFileSoundSource23InitialRecordingStartedEv
+ __ZN20RDQSRLiveSoundSource23InitialRecordingStartedEv
+ __ZN21RDQSRMixedSoundSource23InitialRecordingStartedEv
Functions:
+ __ZN16RDQSRSoundSource23InitialRecordingStartedEv
+ __ZN21RDQSRMixedSoundSource23InitialRecordingStartedEv
+ __ZN20RDQSRFileSoundSource23InitialRecordingStartedEv
+ __ZN20RDQSRLiveSoundSource23InitialRecordingStartedEv
~ __ZN11RDQSREngine14StartASREngineEv : 1072 -> 1076
~ __ZN11RDQSREngine14UseAudioSourceEP16RDQSRSoundSource : 248 -> 284
~ __ZN11RDQSREngine9CanListenEP9RDQSRPeerb : 404 -> 412

```
