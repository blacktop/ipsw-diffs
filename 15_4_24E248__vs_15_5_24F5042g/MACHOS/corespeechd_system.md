## corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x634c
+3405.20.3.0.0
+  __TEXT.__text: 0x65b8
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x7bc
+  __TEXT.__objc_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x7cc
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__objc_methname: 0x19b6
-  __TEXT.__cstring: 0xe47
-  __TEXT.__oslogstring: 0xc30
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__objc_methname: 0x1a94
+  __TEXT.__cstring: 0xeac
+  __TEXT.__oslogstring: 0xc3e
   __TEXT.__objc_classname: 0x16b
   __TEXT.__objc_methtype: 0x7e5
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__unwind_info: 0x218
   __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA.__objc_const: 0xbc0
-  __DATA.__objc_selrefs: 0x5c0
+  __DATA.__objc_selrefs: 0x5f8
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x180
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 141
-  Symbols:   96
-  CStrings:  464
+  Functions: 143
+  Symbols:   97
+  CStrings:  473
 
Symbols:
+ _OBJC_CLASS_$_CSFAudioRecordDeviceInfo
CStrings:
+ "%s AVVC stopRecordForStream successfully"
+ "%s Calling AVVC to stopRecordForStream for streamId: %{public}lu"
+ "%s System Daemon received audioCallBack from AVVC, heartbeat = %{public}lld, for streamId: %{public}lu"
+ "-[CSLaunchDaemonAudioProvidingProxy voiceControllerAudioCallback:forStream:buffer:]"
+ "_handleDeinitializeSecondPassMessage:messageBody:client:"
+ "_handleRecordDeviceInfoMessage:messageBody:client:"
+ "deinitializeSecondPass"
+ "getRecordDeviceInfoForStream:"
+ "initWithAVVCRecordDeviceInfo:"
+ "loggingHeartbeatRate"
+ "recordDeviceInfo"
+ "xpcObject"
- "%s Audio Providing Request Message has arrived : %{public}lld"
- "%s FirstPass Analyzing Request Message has arrived : %{public}lld"
- "%s SecondPass Analyzing Request Message has arrived : %{public}lld"

```
