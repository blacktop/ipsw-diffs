## wifid

> `/usr/sbin/wifid`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_imageinfo`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.32.0.0.0
-  __TEXT.__text: 0x1ba6bc
+2029.6.0.0.0
+  __TEXT.__text: 0x1ba9f4
   __TEXT.__auth_stubs: 0x2bf0
-  __TEXT.__objc_stubs: 0x15040
+  __TEXT.__objc_stubs: 0x150a0
   __TEXT.__objc_methlist: 0x68b0
-  __TEXT.__gcc_except_tab: 0x29b8
-  __TEXT.__const: 0xe6b
-  __TEXT.__cstring: 0x75c31
-  __TEXT.__objc_methname: 0x1b3fd
+  __TEXT.__gcc_except_tab: 0x29d8
+  __TEXT.__const: 0xe73
+  __TEXT.__cstring: 0x75dc8
+  __TEXT.__objc_methname: 0x1b455
   __TEXT.__objc_classname: 0x85e
   __TEXT.__objc_methtype: 0x33ac
   __TEXT.__dlopen_cstrs: 0x33c
   __TEXT.__oslogstring: 0x27ef
   __TEXT.__ustring: 0x63e
-  __TEXT.__unwind_info: 0x6cb0
-  __DATA_CONST.__const: 0x7c48
-  __DATA_CONST.__cfstring: 0x1c920
+  __TEXT.__unwind_info: 0x6cb8
+  __DATA_CONST.__const: 0x7c80
+  __DATA_CONST.__cfstring: 0x1c900
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8

   __DATA_CONST.__objc_arrayobj: 0x288
   __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__auth_got: 0x1608
-  __DATA_CONST.__got: 0x1400
+  __DATA_CONST.__got: 0x1408
   __DATA_CONST.__auth_ptr: 0x160
   __DATA.__objc_const: 0xd480
-  __DATA.__objc_selrefs: 0x63b8
+  __DATA.__objc_selrefs: 0x63d0
   __DATA.__objc_ivar: 0xa28
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x1130
-  __DATA.__common: 0x68
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy
   - /System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager
+  - /System/Library/PrivateFrameworks/WirelessPerception.framework/WirelessPerception
+  - /System/Library/PrivateFrameworks/WirelessPerceptionRuntime.framework/WirelessPerceptionRuntime
   - /usr/lib/libAWDSupportFramework.dylib
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libDHCPServer.A.dylib

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 8814
-  Symbols:   1348
-  CStrings:  17375
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 8779
+  Symbols:   1356
+  CStrings:  17384
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _kWAMessageKeyPrivateMacHomeNetwork
CStrings:
+ "%s: %@ just transient-joined; skipping re-queue (SeamlessSSIDList not yet updated)"
+ "%s: CarPlay join already in progress on channel %lu, not updating shared state"
+ "%s: No CA prefs on incoming network %@, preserving existing CA=%d"
+ "%s: dropped %ld own-SoftAP beacon entr%s from \"%@\" scan results (MIS broadcasting, userInteractive=%d)"
+ "%s: incoming network %@ carries explicit CA=%d; downstream record swap will apply it over existing %@"
+ "%s: phyMode 0x%x, %s bandWidth %d"
+ "AppleTV"
+ "WiFiManager-2029.6 Sep  4 2026 22:08:44"
+ "WiFiManager-2029.6 Sep  4 2026 22:09:36"
+ "WiFiNetworkHasConnectivityAssistPreference"
+ "WiFiSiriIsCompanionDevice: boot-arg override - allowing HomePod companion devices\n"
+ "reduce to"
+ "restore to"
+ "setPreviousJoinDate:"
+ "setPrivateMacNetworkTypeHome:"
+ "updateCellularWRMScore:forInterface:"
- "%s: dropped %ld own-SoftAP beacon entr%s from client scan results (MIS broadcasting)"
- "%s: phyMode 0x%x, bandWidth %d"
- "WiFiManager-2027.32 Aug 27 2026 20:53:32"
- "WiFiManager-2027.32 Aug 27 2026 20:54:22"
- "WiFiSiriIsCompanionDevice: boot-arg override - allowing Home companion devices"
- "iPad12,1"
- "iPad12,2"
```
