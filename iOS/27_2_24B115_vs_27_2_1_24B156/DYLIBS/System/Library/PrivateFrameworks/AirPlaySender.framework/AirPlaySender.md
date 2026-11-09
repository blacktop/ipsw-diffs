## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0x23b9d0
+1005.13.1.2.0
+  __TEXT.__text: 0x23b9f0
   __TEXT.__objc_methlist: 0x81c
-  __TEXT.__cstring: 0x901f4
+  __TEXT.__cstring: 0x90206
   __TEXT.__const: 0x6190
   __TEXT.__gcc_except_tab: 0xaf4
   __TEXT.__dlopen_cstrs: 0x61a
Functions:
~ _coreUtilsPairing_PerformSetup : 496 -> 488
~ _coreUtilsPairing_createAirPlayPairingSession : 636 -> 660
~ _coreUtilsPairing_IsPeerKnown : 236 -> 240
~ _coreUtilsPairing_PerformVerification : 3008 -> 3012
~ _coreUtilsPairing_performSetupInternal : 1468 -> 1476
CStrings:
+ "1005.13.1.2"
+ "OSStatus coreUtilsPairing_createAirPlayPairingSession(APPairingClientRef, PairingSessionType, Boolean, Boolean, Boolean, PairingSessionRef *)"
+ "OSStatus coreUtilsPairing_performSetupInternal(APPairingClientRef, const CFStringRef, APPairingType, Boolean, Boolean, Boolean, CFStringRef, CFStringRef *, CFDataRef *, CFDataRef *, CFTypeRef *, CFDictionaryRef *)"
- "1005.13.1.1"
- "OSStatus coreUtilsPairing_createAirPlayPairingSession(APPairingClientRef, PairingSessionType, Boolean, Boolean, PairingSessionRef *)"
- "OSStatus coreUtilsPairing_performSetupInternal(APPairingClientRef, const CFStringRef, APPairingType, Boolean, Boolean, CFStringRef, CFStringRef *, CFDataRef *, CFDataRef *, CFTypeRef *, CFDictionaryRef *)"
```
