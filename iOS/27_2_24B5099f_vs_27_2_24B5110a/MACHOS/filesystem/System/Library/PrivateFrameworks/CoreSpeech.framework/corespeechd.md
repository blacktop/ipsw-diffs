## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3605.31.3.0.0
-  __TEXT.__text: 0x17e5f8
-  __TEXT.__auth_stubs: 0x1610
+3605.32.1.0.0
+  __TEXT.__text: 0x17f150
+  __TEXT.__auth_stubs: 0x1620
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x22660
-  __TEXT.__objc_methlist: 0x1c3a0
+  __TEXT.__objc_stubs: 0x226a0
+  __TEXT.__objc_methlist: 0x1c430
   __TEXT.__dlopen_cstrs: 0x31a
-  __TEXT.__const: 0x3d0
+  __TEXT.__const: 0x400
   __TEXT.__gcc_except_tab: 0x3138
-  __TEXT.__objc_methname: 0x49237
-  __TEXT.__cstring: 0x3116b
-  __TEXT.__oslogstring: 0x280c5
-  __TEXT.__objc_classname: 0x3a7f
-  __TEXT.__objc_methtype: 0x97e8
-  __TEXT.__unwind_info: 0x7658
-  __DATA_CONST.__const: 0x5e80
-  __DATA_CONST.__cfstring: 0x9180
-  __DATA_CONST.__objc_classlist: 0xa20
+  __TEXT.__objc_methname: 0x49432
+  __TEXT.__cstring: 0x312c0
+  __TEXT.__oslogstring: 0x283f6
+  __TEXT.__objc_classname: 0x3aa5
+  __TEXT.__objc_methtype: 0x97ff
+  __TEXT.__unwind_info: 0x7680
+  __DATA_CONST.__const: 0x5f50
+  __DATA_CONST.__cfstring: 0x91e0
+  __DATA_CONST.__objc_classlist: 0xa28
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_superrefs: 0x848
+  __DATA_CONST.__objc_superrefs: 0x850
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA_CONST.__objc_intobj: 0xd50
+  __DATA_CONST.__objc_intobj: 0xd68
   __DATA_CONST.__objc_arraydata: 0x290
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x5b0
-  __DATA_CONST.__auth_got: 0xb20
-  __DATA_CONST.__got: 0x1550
+  __DATA_CONST.__auth_got: 0xb28
+  __DATA_CONST.__got: 0x1560
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2c900
-  __DATA.__objc_selrefs: 0xd210
-  __DATA.__objc_ivar: 0x22a8
-  __DATA.__objc_data: 0x6540
+  __DATA.__objc_const: 0x2ca28
+  __DATA.__objc_selrefs: 0xd258
+  __DATA.__objc_ivar: 0x22b4
+  __DATA.__objc_data: 0x6590
   __DATA.__lazy_load_got: 0x8
   __DATA.__data: 0x45c4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10623
-  Symbols:   1037
-  CStrings:  17449
+  Functions: 10639
+  Symbols:   1039
+  CStrings:  17480
 
Symbols:
+ _CSIsJ265
+ _OBJC_CLASS_$_CSPickableRouteChangeMonitor
CStrings:
+ "%s #stream CSAudioStreamProviderServiceHandler DROP already emitted for streamId=%@ (useHostTime=%llu)"
+ "%s #stream CSAudioStreamProviderServiceHandler DROP legacy USE, no current stream to attribute it to"
+ "%s #stream CSAudioStreamProviderServiceHandler DROP nil streamId (useHostTime=%llu)"
+ "%s #stream CSAudioStreamProviderServiceHandler DROP no mhId for streamId=%@ (useHostTime=%llu)"
+ "%s #stream CSAudioStreamProviderServiceHandler DROP unknown streamId=%@ (current=%@, previous=%@)"
+ "%s #stream CSAudioStreamProviderServiceHandler EMITTED MHSchemaMHUserSpeakingEnded mhId=%@ useHostTime=%llu streamId=%@"
+ "%s #stream CSAudioStreamProviderServiceHandler EMITTING mhId=%@ useHostTime=%llu (mach_continuous=%llu) streamId=%@ stream=%{public}@"
+ "%s #stream CSAudioStreamProviderServiceHandler SKIP SELF emit — requestMHUUID=%@ is not a valid UUID"
+ "%s #stream CSAudioStreamProviderServiceHandler XPC RECEIVED (legacy, no streamId) useHostTime=%llu"
+ "%s #stream CSAudioStreamProviderServiceHandler XPC RECEIVED useHostTime=%llu streamId=%@"
+ "%s VoiceTrigger cannot be turned on since Hearst is routed and owned with A2DP"
+ "%s VoiceTrigger cannot be turned on since Siri locale is not FarField VT supported"
+ "%s VoiceTrigger cannot be turned on since other non-eligible App is recording and we are not in a connected or outgoing call"
+ "-[CSAudioStreamProviderServiceHandler _forwardUserSpeakingEndAtHostTime:forStreamId:]"
+ "-[CSAudioStreamProviderServiceHandler forwardUserSpeakingEndAtHostTime:forStreamId:]"
+ "-[CSAudioStreamProviderServiceHandler forwardUserSpeakingEndAtHostTime:forStreamId:]_block_invoke"
+ "-[CSVoiceTriggerEnabledPolicyATVExclave _addVoiceTriggerEnabledConditions]_block_invoke"
+ "CSVoiceTriggerEnabledPolicyATVExclave"
+ "T@\"NSString\",C,N,V_previousRequestMHUUID"
+ "T@\"NSUUID\",C,N,V_previousStreamId"
+ "TB,N,V_previousDidEmitForwardedUserSpeakingEnd"
+ "Vv32@0:8Q16@\"NSUUID\"24"
+ "_forwardUserSpeakingEndAtHostTime:forStreamId:"
+ "_previousDidEmitForwardedUserSpeakingEnd"
+ "_previousRequestMHUUID"
+ "_previousStreamId"
+ "current"
+ "forwardUserSpeakingEndAtHostTime:forStreamId:"
+ "isATVFarFieldVoiceTriggerSupportedLanguageCode:"
+ "isOdeonProxyVoiceTriggered"
+ "previous"
+ "previousDidEmitForwardedUserSpeakingEnd"
+ "previousRequestMHUUID"
+ "previousStreamId"
+ "setPreviousDidEmitForwardedUserSpeakingEnd:"
+ "setPreviousRequestMHUUID:"
+ "setPreviousStreamId:"
+ "trailingSilenceDurationThresholdMsPebble"
- "%s #stream CSAudioStreamProviderServiceHandler DROP already emitted (useHostTime=%llu)"
- "%s #stream CSAudioStreamProviderServiceHandler EMITTED MHSchemaMHUserSpeakingEnded mhId=%@ useHostTime=%llu"
- "%s #stream CSAudioStreamProviderServiceHandler EMITTING mhId=%@ useHostTime=%llu (mach_continuous=%llu)"
- "%s #stream CSAudioStreamProviderServiceHandler SKIP SELF emit — no requestMHUUID on _option (MH emission requires it)"
- "%s #stream CSAudioStreamProviderServiceHandler XPC RECEIVED useHostTime=%llu"
- "-[CSAudioStreamProviderServiceHandler _forwardUserSpeakingEndAtHostTime:]"
- "_forwardUserSpeakingEndAtHostTime:"
```
