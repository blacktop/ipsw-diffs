## AIMLInstrumentationStreams

> `/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams`

```diff

-3402.15.1.0.0
-  __TEXT.__text: 0x7509cc
+3402.16.1.0.0
+  __TEXT.__text: 0x7526ec
   __TEXT.__auth_stubs: 0x2130
   __TEXT.__objc_methlist: 0x694
-  __TEXT.__const: 0x317dc
-  __TEXT.__cstring: 0xd1dc
+  __TEXT.__const: 0x317fc
+  __TEXT.__cstring: 0xd6ec
   __TEXT.__constg_swiftt: 0x6c28
   __TEXT.__swift5_typeref: 0x7840
   __TEXT.__swift5_reflstr: 0x5b2c

   __TEXT.__swift5_capture: 0x254
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xed28
-  __TEXT.__eh_frame: 0x19a8c
+  __TEXT.__unwind_info: 0xed58
+  __TEXT.__eh_frame: 0x19ac4
   __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0xd72
+  __TEXT.__objc_methname: 0xd98
   __TEXT.__objc_methtype: 0x3cc
-  __DATA_CONST.__got: 0x5d0
+  __DATA_CONST.__got: 0x5e0
   __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x420
+  __DATA_CONST.__objc_selrefs: 0x438
   __DATA_CONST.__objc_protorefs: 0x30
   __AUTH_CONST.__auth_got: 0x1098
   __AUTH_CONST.__auth_ptr: 0x1818

   __AUTH_CONST.__objc_const: 0x2778
   __AUTH.__objc_data: 0x16c8
   __AUTH.__data: 0xfba8
-  __DATA.__data: 0xd308
+  __DATA.__data: 0xd3a8
   __DATA.__bss: 0x57200
   __DATA.__common: 0xf0
   __DATA_DIRTY.__objc_data: 0x1d8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 23365
-  Symbols:   403
-  CStrings:  2182
+  Functions: 23387
+  Symbols:   405
+  CStrings:  2196
 
Symbols:
+ _OBJC_CLASS_$_ORCHSchemaORCHTRPCandidateCreated
+ _OBJC_CLASS_$_SISchemaUEIUserSpeakingContext
CStrings:
+ "For non-medoc platforms, ASR Audio Lag is the time between UserStopSpeaking and ASRFinalAudioPacketContainingSpeechReceived."
+ "For non-medoc platforms, ASR Time is the time between UserStopSpeaking and eventually-selected Result Candidate is received."
+ "For non-medoc platforms, Execution Time is the time between eventually-selected Result Candidate's CDM process ends until UUFR is ready."
+ "For non-medoc platforms, NLX Time is the time between the eventually-selected Result Candidate is received and CDM ends for that RC."
+ "For non-medoc platforms, Server Fallback Time is the time between eventually-selected Result Candidate's CDM process ends until final server fallback is complete."
+ "For non-medoc platforms, Siri Response Time is the time between UserStopSpeaking and UUFR Ready."
+ "For non-medoc platforms, Useful User Facing Result is the time between AudioStopRecording and UUFR Ready. In cases where the UUFRReady message is not available, the FLOWStep event with flowStateType 'UUFRREADY_DOMAIN' is used to calculate UUFR."
+ "For non-medoc platforms, User Speech is the time between AudioFirstBufferRecorded and UserStopSpeaking."
+ "asrAudioLagMedoc"
+ "rootTrpId"
+ "serverFallbackTimeMedoc"
+ "srtMedocMissingTrpId"
+ "userTrpIds"

```
