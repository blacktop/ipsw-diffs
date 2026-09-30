## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1485.4.0.0.0
-  __TEXT.__text: 0x2b1138
-  __TEXT.__auth_stubs: 0x24f0
+1487.2.0.0.0
+  __TEXT.__text: 0x2b17cc
+  __TEXT.__auth_stubs: 0x2500
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7e80f
-  __TEXT.__const: 0x7e320
+  __TEXT.__cstring: 0x7e8f2
+  __TEXT.__const: 0x7e330
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5d70
+  __TEXT.__unwind_info: 0x5d78
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1278
+  __DATA_CONST.__auth_got: 0x1280
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x20238
+  __DATA_CONST.__const: 0x201b8
   __DATA_CONST.__osclassinfo: 0x388
   __DATA.__data: 0x390
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 00140447-F5C5-34E5-92A3-CCBA16502827
-  Functions: 13075
-  Symbols:   16288
-  CStrings:  12699
+  UUID: 51F279D4-D754-3356-84F3-8E3882E3A461
+  Functions: 13076
+  Symbols:   16289
+  CStrings:  12704
 
Symbols:
+ _ZN21AppleBCMWLANCommander14initWithConfigEP16AppleBCMWLANCoreP24AppleBCMWLANBusInterfacej.cold.7
+ _ZN30AppleBCMWLANProximityInterface21setPEER_CACHE_CONTROLEP29apple80211_peer_cache_control.cold.9
+ __Z40IO80211CalculateMaxNSSAndVHTMCSForMCSMaptPjS_
+ __ZN21AppleBCMWLANCommander20checkCurrentCmdStuckEP18IO80211TimerSource
+ __ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue15validateMacAddrEP29AppleBCMWLANPCIeSkywalkPacketP28AppleBCMWLANSkywalkInterface
+ __block_descriptor_tmp.129
- _ZN23AppleBCMWLANPCIeSkywalk24attachTxSubmissionQueuesEP23IO80211SkywalkInterface.cold.4
- _ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue18dequeueInfraPacketEP29AppleBCMWLANPCIeSkywalkPacketb.cold.1
- _ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue18dequeueInfraPacketEP29AppleBCMWLANPCIeSkywalkPacketb.cold.2
- __ZN24IOUserNetworkPacketQueue12SetDataQueueEP25IODataQueueDispatchSource
- __ZThn40_N24IOUserNetworkPacketQueue12SetDataQueueEP25IODataQueueDispatchSource
- __block_descriptor_tmp.130
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1487.2\""
+ "/AppleInternal/Library/BuildRoots/4~B2qaugCtzVq5mDMCHFmH8t58X8DE7PMT3RaG_T0/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.6.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1487.2"
+ "Jun  8 2025 20:27:56"
+ "[dk] %s@%d:%s::%s adding HE IE \n"
+ "[dk] %s@%d:Mac adress mismatch local %02x:%02x:%02x:%02x:%02x:%02x  packet %02x:%02x:%02x:%02x:%02x:%02x \n"
+ "[dk] %s@%d:cmd is stuck more than diff<%llu> now<%llu> qTime<%llu> \n"
+ "checkCurrentCmdStuck"
+ "validateMacAddr"
+ "wlan.validateMacAddrOption"
- "\"AppleBCMWLANV3_driverkit-1485.4\""
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1485.4"
- "Apr 27 2025 18:51:40"
- "[dk] %s@%d:Request to attach, while not connected\n"

```
