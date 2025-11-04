## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1576.200.81.2.2
-  __TEXT.__text: 0x16ec18
+1576.300.13.0.0
+  __TEXT.__text: 0x16f068
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_methlist: 0x1a2f0
+  __TEXT.__objc_methlist: 0x1a300
   __TEXT.__cstring: 0x13598
   __TEXT.__const: 0x1218
-  __TEXT.__oslogstring: 0x125c2
-  __TEXT.__gcc_except_tab: 0x1974
+  __TEXT.__oslogstring: 0x125d2
+  __TEXT.__gcc_except_tab: 0x197c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df
   __TEXT.__constg_swiftt: 0x578

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5df0
+  __TEXT.__unwind_info: 0x5df8
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x274f
-  __TEXT.__objc_methname: 0x3c5f8
+  __TEXT.__objc_methname: 0x3c625
   __TEXT.__objc_methtype: 0x7f83
-  __TEXT.__objc_stubs: 0x20f40
+  __TEXT.__objc_stubs: 0x20f60
   __DATA_CONST.__got: 0xe60
   __DATA_CONST.__const: 0x3678
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xafd0
+  __DATA_CONST.__objc_selrefs: 0xafe0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __AUTH_CONST.__auth_got: 0x11d8
   __AUTH_CONST.__const: 0x31a8
   __AUTH_CONST.__cfstring: 0x11ca0
-  __AUTH_CONST.__objc_const: 0x28390
+  __AUTH_CONST.__objc_const: 0x283a0
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C79374F0-0362-3604-B8BB-F380C0B362AC
-  Functions: 10064
-  Symbols:   30077
-  CStrings:  16503
+  UUID: A51D7201-6949-36EE-A1AB-431FB44E72A5
+  Functions: 10066
+  Symbols:   30082
+  CStrings:  16505
 
Symbols:
+ -[TUCall isLockdownModeEnabled]
+ -[TUConversationActivity isTranslationActivity]
+ -[TUNearbyDeviceHandle accessorLock]
+ _OBJC_IVAR_$_TUNearbyDeviceHandle._accessorLock
+ ___block_literal_global.2012
+ ___block_literal_global.2018
+ _objc_msgSend$isLockdownModeEnabled
- -[TUCall lockdownModeEnabled]
- _OBJC_IVAR_$_TUCall._lockdownModeEnabled
- ___block_literal_global.2013
- ___block_literal_global.2019
CStrings:
+ "TB,R,N,GisLockdownModeEnabled"
+ "isLockdownModeEnabled"
+ "isTranslationActivity"
+ "smartHoldingAvailability=%i, validRemoteParticipantCount=%i validNotConferenced=%i, validSystemProvider=%i, validNotEmergencyCall=%i, validCallStatus=%i(%i), validEndpointOnCurrentDevice=%i, validIsNotVideo=%i, validLocale=%i(%@), validCaptioningAvailable=%i, isGASRAvailable=%i, validLockdownMode=%i"
+ "\xf0\xf01"
- "TB,R,N,V_lockdownModeEnabled"
- "smartHoldingAvailability=%i, validRemoteParticipantCount=%i validNotConferenced=%i, validSystemProvider=%i, validNotEmergencyCall=%i, validCallStatus=%i(%i), validEndpointOnCurrentDevice=%i, validIsNotVideo=%i, validLocale=%i(%@), validCaptioningAvailable=%i, isGASRAvailable=%i"
- "\xf0\xf0A"

```
