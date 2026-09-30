## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0xb45bc
+3405.20.3.0.0
+  __TEXT.__text: 0xb4ea0
   __TEXT.__auth_stubs: 0x1d90
-  __TEXT.__objc_methlist: 0xb9d0
+  __TEXT.__objc_methlist: 0xba48
   __TEXT.__const: 0x7e0
   __TEXT.__dlopen_cstrs: 0x174
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x13bdf
+  __TEXT.__cstring: 0x13ce9
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__gcc_except_tab: 0x3194
-  __TEXT.__oslogstring: 0xdf2b
-  __TEXT.__unwind_info: 0x2fd0
+  __TEXT.__gcc_except_tab: 0x3214
+  __TEXT.__oslogstring: 0xdfe5
+  __TEXT.__unwind_info: 0x3028
   __TEXT.__eh_frame: 0xe8
   __TEXT.__objc_classname: 0x1a26
-  __TEXT.__objc_methname: 0x1f8e8
-  __TEXT.__objc_methtype: 0x43b4
-  __TEXT.__objc_stubs: 0x10580
+  __TEXT.__objc_methname: 0x1f9c7
+  __TEXT.__objc_methtype: 0x43b7
+  __TEXT.__objc_stubs: 0x105e0
   __DATA_CONST.__got: 0xf20
-  __DATA_CONST.__const: 0x2440
+  __DATA_CONST.__const: 0x2470
   __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67c8
+  __DATA_CONST.__objc_selrefs: 0x67f8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4d8
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xee0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x1550
-  __AUTH_CONST.__cfstring: 0x89c0
-  __AUTH_CONST.__objc_const: 0x12100
+  __AUTH_CONST.__const: 0x1570
+  __AUTH_CONST.__cfstring: 0x8a00
+  __AUTH_CONST.__objc_const: 0x12140
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1b0
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0xbfc
-  __DATA.__data: 0x12d8
+  __DATA.__objc_ivar: 0xc00
+  __DATA.__data: 0x12e0
   __DATA.__bss: 0x8f8
   __DATA_DIRTY.__objc_data: 0x3c68
   __DATA_DIRTY.__data: 0x2c8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4471
-  Symbols:   5909
-  CStrings:  8611
+  Functions: 4482
+  Symbols:   5921
+  CStrings:  8629
 
Symbols:
+ _kXPCEncodeKeyIsNarrowBand
CStrings:
+ "%@ {route = %@, isRemoteDevice = %d, remoteDeviceUID = %@, remoteDeviceProductIdentifier = %@, remoteDeviceUIDString = %@, isNarrowBand = %d}"
+ "%s Launch Agent received audioCallBack from systemDaemon, heartbeat = %{public}lld, for streamId: %{public}lu"
+ "%s Not allowed to initialize new xpcConnection when current user is inactive"
+ "%s Notify Mac User session %@"
+ "%s stopAudioStream successfully? %d"
+ "-[CSAudioRecorder _recordDeviceInfoWithStreamHandleId:]"
+ "-[CSLaunchAgentXPCClient _disconnect]_block_invoke"
+ "-[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:]"
+ "-[CSLaunchAgentXPCClient adBlockerReset]"
+ "-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]"
+ "-[CSLaunchAgentXPCClient recordDeviceInfoWithStreamHandleId:]"
+ "-[CSMacUserSessionMonitor _notifySessionActive:]"
+ "@56@0:8@16B24@28@36@44B52"
+ "TB,R,N,V_isNarrowBand"
+ "_disconnect"
+ "_isNarrowBand"
+ "_recordDeviceInfoWithStreamHandleId:"
+ "adBlockerReset"
+ "deinitializeSecondPass"
+ "exclaveSecondPassVoiceTriggerAnalyzerForFirstPassSource:"
+ "inactive"
+ "initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:isNarrowBand:"
+ "recordDeviceInfoWithStreamHandleId:"
+ "shouldDisableSpeakerRecognition"
- "%@ {route = %@, isRemoteDevice = %d, remoteDeviceUID = %@, remoteDeviceProductIdentifier = %@, remoteDeviceUIDString = %@}"
- "%s LaunchAgentXPCAudioProvidingDelegate messageType : %{public}lld"
- "-[CSAudioRecorder recordDeviceInfoWithStreamHandleId:recordDeviceIndicator:]"
- "-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke"
- "@52@0:8@16B24@28@36@44"
- "exclaveSecondPassVoiceTriggerAnalyzer"
- "initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:"

```
