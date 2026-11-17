## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-449.302.0.0.0
-  __TEXT.__text: 0x6e668
+449.305.0.0.0
+  __TEXT.__text: 0x6e7a8
   __TEXT.__realtime: 0x4b4
   __TEXT.__objc_methlist: 0xc4c
-  __TEXT.__gcc_except_tab: 0xa694
+  __TEXT.__gcc_except_tab: 0xa6bc
   __TEXT.__const: 0xbd0
-  __TEXT.__cstring: 0x490c
-  __TEXT.__oslogstring: 0x54e9
+  __TEXT.__cstring: 0x492f
+  __TEXT.__oslogstring: 0x5540
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x30b8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x8a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__got: 0x4e8
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0xf40
+  __AUTH_CONST.__cfstring: 0xf60
   __AUTH_CONST.__objc_const: 0xe00
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1675
-  Symbols:   2605
-  CStrings:  1015
+  Symbols:   2606
+  CStrings:  1017
 
Symbols:
+ _kAudioSessionNotification_InterruptionInfoKey_EndInterruptionLikelyToBeResumable
Functions:
~ -[AVAudioSessionRemoteXPCClient updateApplicationProperty:clientID:propertyID:propertyValue:context:reply:] : 916 -> 920
~ -[AVAudioSessionRemoteXPCClient setIONode:playState:modes:reply:] : 688 -> 856
~ ____ZN12_GLOBAL__N_130HandleInterruptionNotificationEjP12NSDictionary_block_invoke : 2444 -> 2592
CStrings:
+ "%25s:%-5d IONodeSession privileged play state modes (0x%lx) are not permitted over XPC"
+ "EndInterruptionLikelyToBeResumable"
```
