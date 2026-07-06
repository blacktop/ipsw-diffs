## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/Versions/A/AudioSessionServer`

```diff

-  __TEXT.__text: 0x544c0
+  __TEXT.__text: 0x54010
   __TEXT.__realtime: 0x40
   __TEXT.__objc_methlist: 0x934
   __TEXT.__const: 0xaf0
-  __TEXT.__gcc_except_tab: 0x7fec
-  __TEXT.__cstring: 0x3b90
-  __TEXT.__oslogstring: 0x5946
+  __TEXT.__gcc_except_tab: 0x7fb8
+  __TEXT.__cstring: 0x35f8
+  __TEXT.__oslogstring: 0x58ff
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__unwind_info: 0x24d8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__got: 0x698
   __AUTH_CONST.__const: 0x1258
   __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0xbb0
+  __AUTH_CONST.__objc_const: 0xb70
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x58
   __DATA.__data: 0x250
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x400
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1293
-  Symbols:   2993
-  CStrings:  1000
+  Symbols:   2990
+  CStrings:  979
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ __ZL28AudioSessionServerXPCTimeoutv
+ __ZZL28AudioSessionServerXPCTimeoutvE8onceFlag
- OBJC_IVAR_$_AVAudioSessionRemoteXPCClient._replyWatchdogFunctionName
- OBJC_IVAR_$_AVAudioSessionRemoteXPCClient._replyWatchdogMinTimestamp
- __ZL28AudioSessionServerXPCTimeoutPKc
- __ZZL28AudioSessionServerXPCTimeoutPKcE8onceFlag
Functions:
~ __ZN4avas6server20LegacySessionManager18HandleProcessDeathEi : 524 -> 512
~ __ZN4avas6server16AudioSessionInfo37HasObserverForGenericPipeNotificationEP8NSString : 208 -> 196
~ -[AVAudioSessionRemoteXPCClient initWithServer:process:delegate:] : 768 -> 748
~ -[AVAudioSessionRemoteXPCClient destroySession:reply:] : 1040 -> 1012
~ -[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:] : 688 -> 660
~ -[AVAudioSessionRemoteXPCClient createSession:reply:] : 3124 -> 3092
~ -[AVAudioSessionRemoteXPCClient activateSession:options:requestID:reply:] : 2516 -> 2524
~ -[AVAudioSessionRemoteXPCClient deactivateSession:options:priority:requestID:reply:] : 1276 -> 1284
~ -[AVAudioSessionRemoteXPCClient getProperty:propertyName:MXProperty:reply:] : 744 -> 716
~ -[AVAudioSessionRemoteXPCClient getMXPropertyGenericPipe:propertyName:reply:] : 736 -> 708
~ -[AVAudioSessionRemoteXPCClient getProperties:properties:genericMXPipe:reply:] : 636 -> 608
~ -[AVAudioSessionRemoteXPCClient getPropertiesForCache:reply:] : 648 -> 620
~ -[AVAudioSessionRemoteXPCClient getDeferredMessages:reply:] : 1008 -> 980
~ -[AVAudioSessionRemoteXPCClient getDeferredMessagesForSessions:reply:] : 1168 -> 1140
~ -[AVAudioSessionRemoteXPCClient addMXNotificationListener:notificationName:reply:] : 716 -> 688
~ -[AVAudioSessionRemoteXPCClient removeMXNotificationListener:notificationName:reply:] : 716 -> 688
~ -[AVAudioSessionRemoteXPCClient createAudioApplicationForSpecification:reply:] : 1420 -> 1400
~ -[AVAudioSessionRemoteXPCClient sessionIDs:clientID:reply:] : 796 -> 768
~ -[AVAudioSessionRemoteXPCClient getApplicationProperty:clientID:propertyID:isMXProperty:reply:] : 1012 -> 984
~ -[AVAudioSessionRemoteXPCClient setApplicationProperty:clientID:propertyID:propertyValue:reply:] : 1308 -> 1280
~ -[AVAudioSessionRemoteXPCClient updateApplicationProperty:clientID:propertyID:propertyValue:context:reply:] : 1008 -> 980
~ -[AVAudioSessionRemoteXPCClient getApplicationMessages:clientID:reply:] : 540 -> 512
~ -[AVAudioSessionRemoteXPCClient setMXPropertyOnAllSessions:clientID:MXProperty:values:reply:] : 228 -> 200
~ -[AVAudioSessionRemoteXPCClient toggleInputMuteForRecordingProcess:] : 628 -> 600
~ -[AVAudioSessionRemoteXPCClient updateRunningIOStates:inputRunning:outputRunning:implicitCategory:deviceUIDs:reply:] : 3112 -> 2984
~ -[AVAudioSessionRemoteXPCClient createIONodeWithSourceSession:sessionOwnerPID:playerType:reply:] : 628 -> 600
~ -[AVAudioSessionRemoteXPCClient reconfigureIONode:withSourceSession:sessionOwnerPID:playerType:reply:] : 856 -> 828
~ -[AVAudioSessionRemoteXPCClient invalidateIONode:reply:] : 528 -> 500
~ -[AVAudioSessionRemoteXPCClient setIONode:playState:modes:reply:] : 460 -> 432
~ -[AVAudioSessionRemoteXPCClient setPropertiesIONode:values:reply:] : 580 -> 552
~ -[AVAudioSessionRemoteXPCClient getPropertiesIONode:properties:reply:] : 584 -> 556
~ -[AVAudioSessionRemoteXPCClient updateMicrophonePermission:clientToken:reply:] : 452 -> 424
~ -[AVAudioSessionRemoteXPCClient .cxx_construct] : 72 -> 68
~ __ZNSt3__110__function6__funcIZ65-[AVAudioSessionRemoteXPCClient initWithServer:process:delegate:]E3$_2FvvEEclEv : 240 -> 124
~ __ZL28AudioSessionServerXPCTimeoutPKc -> __ZL28AudioSessionServerXPCTimeoutv : 920 -> 768
~ __ZN4avas6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ : 692 -> 668
~ __ZN4avas6server27HandleBatchedMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ : 720 -> 696
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mSFDh8/Sources/AudioSession/Server/AudioSession/AudioSessionServerImpNotificationHandlers.mm"
+ "XPC message timeout in AudioSessionServer, probably deadlocked. Writing a stackshot and terminating."
- "%25s:%-5d XPC watchdog timer fired too soon, skipping timeout handling"
- ", probably deadlocked. Writing a stackshot and terminating."
- "-[AVAudioSessionRemoteXPCClient addMXNotificationListener:notificationName:reply:]"
- "-[AVAudioSessionRemoteXPCClient createIONodeWithSourceSession:sessionOwnerPID:playerType:reply:]"
- "-[AVAudioSessionRemoteXPCClient createSession:reply:]"
- "-[AVAudioSessionRemoteXPCClient destroySession:reply:]"
- "-[AVAudioSessionRemoteXPCClient getDeferredMessagesForSessions:reply:]"
- "-[AVAudioSessionRemoteXPCClient getMXPropertyGenericPipe:propertyName:reply:]"
- "-[AVAudioSessionRemoteXPCClient getProperties:properties:genericMXPipe:reply:]"
- "-[AVAudioSessionRemoteXPCClient getPropertiesForCache:reply:]"
- "-[AVAudioSessionRemoteXPCClient getPropertiesIONode:properties:reply:]"
- "-[AVAudioSessionRemoteXPCClient getProperty:propertyName:MXProperty:reply:]"
- "-[AVAudioSessionRemoteXPCClient invalidateIONode:reply:]"
- "-[AVAudioSessionRemoteXPCClient reconfigureIONode:withSourceSession:sessionOwnerPID:playerType:reply:]"
- "-[AVAudioSessionRemoteXPCClient removeMXNotificationListener:notificationName:reply:]"
- "-[AVAudioSessionRemoteXPCClient setIONode:playState:modes:reply:]"
- "-[AVAudioSessionRemoteXPCClient setMXPropertyOnAllSessions:clientID:MXProperty:values:reply:]"
- "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]"
- "-[AVAudioSessionRemoteXPCClient setPropertiesIONode:values:reply:]"
- "-[AVAudioSessionRemoteXPCClient toggleInputMuteForRecordingProcess:]"
- "-[AVAudioSessionRemoteXPCClient updateMicrophonePermission:clientToken:reply:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.faI4cR/Sources/AudioSession/Server/AudioSession/AudioSessionServerImpNotificationHandlers.mm"
- "XPC message timeout in "

```
