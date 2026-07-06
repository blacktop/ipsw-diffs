## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-  __TEXT.__text: 0x6f3d4
+  __TEXT.__text: 0x6ef38
   __TEXT.__realtime: 0x49c
   __TEXT.__objc_methlist: 0xc4c
-  __TEXT.__gcc_except_tab: 0xa63c
+  __TEXT.__gcc_except_tab: 0xa600
   __TEXT.__const: 0xbf0
-  __TEXT.__cstring: 0x4df9
-  __TEXT.__oslogstring: 0x52ea
+  __TEXT.__cstring: 0x48ff
+  __TEXT.__oslogstring: 0x52a3
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2d40
+  __TEXT.__unwind_info: 0x2d30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x898
+  __DATA_CONST.__objc_selrefs: 0x8a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__got: 0x4e0
   __AUTH_CONST.__const: 0x1188
   __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0xe40
+  __AUTH_CONST.__objc_const: 0xe00
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x378
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0x388
+  __DATA_DIRTY.__bss: 0x390
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1671
-  Symbols:   5748
-  CStrings:  1147
+  Functions: 1673
+  Symbols:   5751
+  CStrings:  1127
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ GCC_except_table110
+ GCC_except_table138
+ GCC_except_table183
+ GCC_except_table186
+ _OBJC_CLASS_$_NSXPCConnection
+ __ZL28AudioSessionServerXPCTimeoutv
+ __ZZL28AudioSessionServerXPCTimeoutvE8onceFlag
+ ___block_descriptor_100_ea8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_92_ea8_32s40r_e5_v8?0lr40l8s32l8
+ _objc_msgSend$_handoffCurrentReplyToQueue:block:
- GCC_except_table100
- GCC_except_table105
- GCC_except_table118
- GCC_except_table122
- GCC_except_table145
- GCC_except_table169
- GCC_except_table177
- GCC_except_table181
- GCC_except_table184
- _OBJC_IVAR_$_AVAudioSessionRemoteXPCClient._replyWatchdogFunctionName
- _OBJC_IVAR_$_AVAudioSessionRemoteXPCClient._replyWatchdogMinTimestamp
- __ZL28AudioSessionServerXPCTimeoutPKc
- __ZNSt3__16chrono12system_clock3nowEv
- __ZZL28AudioSessionServerXPCTimeoutPKcE8onceFlag
- ___block_descriptor_100_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_92_ea8_32s40bs_e5_v8?0ls32l8s40l8
CStrings:
+ "XPC message timeout in AudioSessionServer, probably deadlocked. Writing a stackshot and terminating."
- "%25s:%-5d XPC watchdog timer fired too soon, skipping timeout handling"
- ", probably deadlocked. Writing a stackshot and terminating."
- "-[AVAudioSessionRemoteXPCClient addMXNotificationListener:notificationName:reply:]"
- "-[AVAudioSessionRemoteXPCClient createIONodeWithSourceSession:sessionOwnerPID:playerType:reply:]"
- "-[AVAudioSessionRemoteXPCClient createSession:reply:]"
- "-[AVAudioSessionRemoteXPCClient getDeferredMessagesForSessions:reply:]"
- "-[AVAudioSessionRemoteXPCClient getIOControllerPeriod:decoupledInput:reply:]"
- "-[AVAudioSessionRemoteXPCClient getMXPropertyGenericPipe:propertyName:reply:]"
- "-[AVAudioSessionRemoteXPCClient getProperties:properties:genericMXPipe:reply:]"
- "-[AVAudioSessionRemoteXPCClient getPropertiesForCache:reply:]"
- "-[AVAudioSessionRemoteXPCClient getPropertiesIONode:properties:reply:]"
- "-[AVAudioSessionRemoteXPCClient getProperty:propertyName:MXProperty:reply:]"
- "-[AVAudioSessionRemoteXPCClient invalidateIONode:reply:]"
- "-[AVAudioSessionRemoteXPCClient removeMXNotificationListener:notificationName:reply:]"
- "-[AVAudioSessionRemoteXPCClient setMXPropertyOnAllSessions:clientID:MXProperty:values:reply:]"
- "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]"
- "-[AVAudioSessionRemoteXPCClient setPropertiesIONode:values:reply:]"
- "-[AVAudioSessionRemoteXPCClient toggleInputMuteForRecordingProcess:]"
- "-[AVAudioSessionRemoteXPCClient verifySessionExists:reply:]"
- "XPC message timeout in "
- "unknown"

```
