## IsolatedCoreAudioClient

> `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`

```diff

-5.365.0.0.0
-  __TEXT.__text: 0x16754
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__gcc_except_tab: 0x179c
-  __TEXT.__const: 0x23bc
-  __TEXT.__cstring: 0x7a2
-  __TEXT.__oslogstring: 0x2284
-  __TEXT.__unwind_info: 0xce8
-  __TEXT.__objc_classname: 0x1ee
-  __TEXT.__objc_methname: 0xf15
-  __TEXT.__objc_methtype: 0xaea
-  __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0xc8
+5.512.0.0.0
+  __TEXT.__text: 0x1a0a4
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__const: 0x27a6
+  __TEXT.__gcc_except_tab: 0x1c88
+  __TEXT.__cstring: 0x86a
+  __TEXT.__oslogstring: 0x2442
+  __TEXT.__unwind_info: 0xf08
+  __TEXT.__objc_classname: 0x211
+  __TEXT.__objc_methname: 0x1030
+  __TEXT.__objc_methtype: 0xc5a
+  __TEXT.__objc_stubs: 0xb20
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x390
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x1f58
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__const: 0x2468
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x1138
+  __AUTH_CONST.__objc_const: 0xd70
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x1c8
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 743
-  Symbols:   935
-  CStrings:  449
+  Functions: 867
+  Symbols:   1086
+  CStrings:  492
 
Symbols:
+ _AudioHardwareCreateAggregateDevice
+ _AudioHardwareDestroyAggregateDevice
+ _AudioObjectAddPropertyListener
+ _AudioObjectGetPropertyDataSize
+ _AudioObjectHasProperty
+ _AudioObjectRemovePropertyListener
+ _AudioObjectSetPropertyData
+ _CFArrayCreate
+ _CFDictionaryCreate
+ _CFNumberCreate
+ _CFRelease
+ _CFRetain
+ _CFStringCreateWithBytes
+ _CFStringGetCStringPtr
+ _CreateHistoricalAudioPortal
+ __ZNKSt3__119bad_expected_accessIvE4whatEv
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTINSt3__119bad_expected_accessIvEE
+ __ZTISt13runtime_error
+ __ZTVNSt3__117bad_function_callE
+ _kCFTypeArrayCallBacks
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _objc_release_x9
+ _tb_message_precheck_encoding
+ _tb_message_raw_encode_u64
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- _tb_message_encode_u64
CStrings:
+ "\""
+ "%25s:%-5d Could not create get workgroup for deviceID: %u because of Error:%@"
+ "%25s:%-5d Created the portal"
+ "%25s:%-5d HALUseCase::SetDeviceIDUsingUseCaseID mDeviceID: %u"
+ "%25s:%-5d MTDClientInterface - listenForMicrophoneActivity landed in the catch!"
+ "%25s:%-5d MTDClientInterface constructor"
+ "%25s:%-5d MTDClientInterface disableMicrophoneActivityDetection"
+ "%25s:%-5d MTDClientInterface enableMicrophoneActivityDetection"
+ "%25s:%-5d MTDClientInterface listenForMicrophoneActivity"
+ "%25s:%-5d MTDClientInterface stopListeningForMicrophoneActivity"
+ "%25s:%-5d MTDClientInterface test constructor"
+ "%25s:%-5d Received CreateHistoricalAudioPortal request"
+ "@24@0:8@?16"
+ "@?"
+ "Could not construct"
+ "DefaultInput"
+ "DefaultInputUUID"
+ "MADClientInterface"
+ "MADClientInterface.mm"
+ "MicActivityReverseClientProtocol"
+ "MicrophoneActivityPortal.mm"
+ "T@\"NSMutableSet\",&,N,V_mReverseConnections"
+ "T{shared_ptr<MADMultiplexer>=^{MADMultiplexer}^{__shared_weak_count}},N,V_mMADMultiplexer"
+ "_mMADMultiplexer"
+ "_mReverseConnections"
+ "disableMicrophoneActivityDetection:"
+ "enableMicrophoneActivityDetection:"
+ "initForTest:"
+ "listenForMicrophoneActivity:reply:"
+ "mClient"
+ "mMADMultiplexer"
+ "mMTDCallbackReply"
+ "mReverseConnections"
+ "master"
+ "micactivityd input agg"
+ "micactivityd-input-agg"
+ "microphoneActivityStateChanged:reply:"
+ "name"
+ "private"
+ "sIsolatedCoreAudioMicActivity"
+ "setMMADMultiplexer:"
+ "setMReverseConnections:"
+ "setupReverseConnection:"
+ "stopListeningForMicrophoneActivity:"
+ "subdevices"
+ "uid"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?i>20"
+ "v32@0:8{shared_ptr<MADMultiplexer>=^{MADMultiplexer}^{__shared_weak_count}}16"
+ "vector"
+ "{shared_ptr<MADClient>=\"__ptr_\"^{MADClient}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<MADMultiplexer>=\"__ptr_\"^{MADMultiplexer}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<MADMultiplexer>=^{MADMultiplexer}^{__shared_weak_count}}16@0:8"
- "%25s:%-5d Could not create get workgroup for deviceID: %d because of Error:%@"
- "%25s:%-5d CreateMicrophoneActivityPortal unsupported"
- "%25s:%-5d HALUseCase::SetDeviceIDUsingUseCaseID mDeviceID: %d"
- "IsolatedCoreAudio"
- "MTDClientInterface"
- "disable_microphone_activity_detection_with_reply:"
- "enable_microphone_activity_detection_with_reply:"
- "listen_for_microphone_activity:reply:"
- "register_client:reply:"
- "stop_listening_for_microphone_activity_with_reply:"

```
