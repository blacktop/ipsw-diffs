## com.apple.iokit.IOAVBFamily

> `com.apple.iokit.IOAVBFamily`

```diff

-  __TEXT.__cstring: 0x257c
-  __TEXT.__os_log: 0x9d27
+  __TEXT.__cstring: 0x2575
+  __TEXT.__os_log: 0x9d5c
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0x1e214
+  __TEXT_EXEC.__text: 0x1e328
   __TEXT_EXEC.__auth_stubs: 0x690
   __DATA.__data: 0xcc
   __DATA.__common: 0x220

   __DATA_CONST.__kalloc_type: 0x340
   __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0xf8
-  Functions: 666
-  Symbols:   2125
+  Functions: 669
+  Symbols:   2129
   CStrings:  388
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _ZN18IOAVBNubUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv
+ __ZZN27IOAVBTimeSyncSyncUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_0
Functions:
~ __ZN27IOAVBTimeSyncSyncUserClient12initWithTaskEP4taskPvjP12OSDictionary : 172 -> 208
+ _OUTLINED_FUNCTION_0
~ __ZN18IOAVBNubUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 1196 -> 1240
~ _ZN27IOAVBTimeSyncSyncUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1 : 100 -> 64
+ _ZN30IOAVBTimeSyncCaptureUserClient5startEP9IOService.cold.1
+ _ZN18IOAVBNubUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/ClockServices/IOAVBGPIOEdgeTimeCapture.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/ClockServices/IOAVBLocalClock.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/ClockServices/IOAVBTimeSyncSyncUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBControllerHelper.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBNub.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBNubUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBValidate.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBValidateUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBStreamCapture.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBStreamCaptureUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBTimeSyncCapture.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBTimeSyncCaptureUserClient.cpp"
+ "fIOTimeSyncServiceLock != nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/ClockServices/IOAVBGPIOEdgeTimeCapture.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/ClockServices/IOAVBLocalClock.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/ClockServices/IOAVBTimeSyncSyncUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBControllerHelper.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBNub.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBNubUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBValidate.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/IOAVBValidateUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBStreamCapture.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBStreamCaptureUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBTimeSyncCapture.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBFamily/NetworkInterface/IOAVBTimeSyncCaptureUserClient.cpp"
- "1211111212221212111111111111111111111211"

```
