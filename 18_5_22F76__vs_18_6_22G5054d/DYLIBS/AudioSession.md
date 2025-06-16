## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-321.603.0.0.0
-  __TEXT.__text: 0x43fdc
+321.702.0.0.0
+  __TEXT.__text: 0x4419c
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_methlist: 0x1c20
-  __TEXT.__gcc_except_tab: 0x7bec
-  __TEXT.__cstring: 0x23b2
+  __TEXT.__gcc_except_tab: 0x7c34
+  __TEXT.__cstring: 0x23d6
   __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x2c12
-  __TEXT.__unwind_info: 0x2748
+  __TEXT.__oslogstring: 0x2c3f
+  __TEXT.__unwind_info: 0x2750
   __TEXT.__objc_classname: 0x30f
   __TEXT.__objc_methname: 0x45f3
   __TEXT.__objc_methtype: 0x1367

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59E071B5-055D-3DE0-B60D-47B4DCE20666
+  UUID: 9D74AAA7-A448-3A99-99C6-AB1BD0711461
   Functions: 1395
   Symbols:   4928
-  CStrings:  1602
+  CStrings:  1604
 
Functions:
~ __ZN2as6client10cache_util12CacheManager35checkAndRefreshCacheForNotificationEP14AVAudioSessionP8NSString : 536 -> 584
~ -[AVAudioSession(ClientCommonImplementation) privatePostNotificationForType:name:userInfo:accessor:] : 820 -> 1024
~ -[AVAudioSessionCallbackDispatcher pingClient:] : 8 -> 204
CStrings:
+ "%25s:%-5d pingClient called for session 0x%x"
+ "AVAudioSessionCallbackDispatcher.mm"

```
