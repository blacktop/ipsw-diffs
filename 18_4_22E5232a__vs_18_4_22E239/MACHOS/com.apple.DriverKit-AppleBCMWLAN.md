## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1475.46.0.0.0
-  __TEXT.__text: 0x2af618
+  __TEXT.__text: 0x2b0a2c
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7e0e6
+  __TEXT.__cstring: 0x7e56c
   __TEXT.__const: 0x7e310
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5d08
+  __TEXT.__unwind_info: 0x5d60
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1270
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 13038
-  Symbols:   16250
-  CStrings:  12661
+  Functions: 13065
+  Symbols:   16278
+  CStrings:  12690
 
Symbols:
+ _ZN22AppleBCMWLANGCRAdapter13clearGCRStatsEj.cold.1
+ _ZN22AppleBCMWLANGCRAdapter14joinGCRSessionEjP31apple80211_nan_join_gcr_session.cold.1
+ _ZN22AppleBCMWLANGCRAdapter14joinGCRSessionEjP31apple80211_nan_join_gcr_session.cold.2
+ _ZN22AppleBCMWLANGCRAdapter16configureGCRRateEjP23apple80211_nan_gcr_rate.cold.1
+ _ZN22AppleBCMWLANGCRAdapter16configureGCRRateEjP23apple80211_nan_gcr_rate.cold.2
+ _ZN22AppleBCMWLANGCRAdapter16configureGCRRateEjP23apple80211_nan_gcr_rate.cold.3
+ _ZN22AppleBCMWLANGCRAdapter16configureGCRRateEjP23apple80211_nan_gcr_rate.cold.4
+ _ZN22AppleBCMWLANGCRAdapter16createGCRSessionEjP33apple80211_nan_create_gcr_session.cold.1
+ _ZN22AppleBCMWLANGCRAdapter16createGCRSessionEjP33apple80211_nan_create_gcr_session.cold.2
+ _ZN22AppleBCMWLANGCRAdapter19getGCRLinkConditionEjP33apple80211_nan_gcr_link_condition.cold.1
+ _ZN22AppleBCMWLANGCRAdapter19getGCRLinkConditionEjP33apple80211_nan_gcr_link_condition.cold.2
+ _ZN22AppleBCMWLANGCRAdapter19getGCRLinkConditionEjP33apple80211_nan_gcr_link_condition.cold.3
+ _ZN22AppleBCMWLANGCRAdapter19getGCRLinkConditionEjP33apple80211_nan_gcr_link_condition.cold.4
+ _ZN24AppleBCMWLANNANInterface25setNAN_CREATE_GCR_SESSIONEP33apple80211_nan_create_gcr_session.cold.1
+ _ZN24AppleBCMWLANNANInterface25setNAN_CREATE_GCR_SESSIONEP33apple80211_nan_create_gcr_session.cold.2
+ _ZN24AppleBCMWLANNANInterface27setNAN_GCR_Multicast_BitmapE10ether_addr.cold.1
+ _ZN24AppleBCMWLANNANInterface27setNAN_GCR_Multicast_BitmapE10ether_addr.cold.2
+ __ZN16AppleBCMWLANCore16getGCRMACAddressEv
+ __ZN22AppleBCMWLANGCRAdapter13clearGCRStatsEj
+ __ZN22AppleBCMWLANGCRAdapter14joinGCRSessionEjP31apple80211_nan_join_gcr_session
+ __ZN22AppleBCMWLANGCRAdapter16configureGCRRateEjP23apple80211_nan_gcr_rate
+ __ZN22AppleBCMWLANGCRAdapter16createGCRSessionEjP33apple80211_nan_create_gcr_session
+ __ZN22AppleBCMWLANGCRAdapter16getGCRMACAddressEv
+ __ZN22AppleBCMWLANGCRAdapter19getGCRLinkConditionEjP33apple80211_nan_gcr_link_condition
+ __ZN24AppleBCMWLANNANInterface27setNAN_GCR_Multicast_BitmapE10ether_addr
+ __ZNK16AppleBCMWLANCore13getGCRAdapterEv
CStrings:
+ "/AppleInternal/Library/BuildRoots/46a745fc-02fe-11f0-b780-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Mar 17 2025 20:06:53"
+ "[dk] %s@%d:Clearing GCR link condition stats\n"
+ "[dk] %s@%d:Configuring GCR multicast rate, %x, %x\n"
+ "[dk] %s@%d:Configuring NAN Multicast bitmap for ndi: %x:%x:%x:%x:%x:%x, len: %u\n"
+ "[dk] %s@%d:Creating GCR session\n"
+ "[dk] %s@%d:ERROR: Unable to set NAN Multicast bitmap\n"
+ "[dk] %s@%d:Fail to create GCR session\n"
+ "[dk] %s@%d:Fail to set GCR multicast bitmap\n"
+ "[dk] %s@%d:Getting GCR link condition stats\n"
+ "[dk] %s@%d:Got GCR link condition stats rxmpdu:%u, rxholes:%u txPackets:%u, rxPackets: %u snr:%u mcs %u\n"
+ "[dk] %s@%d:Joining GCR session\n"
+ "[dk] %s@%d:Stats tlv is of wrong format %u\n"
+ "[dk] %s@%d:Unable to clear GCR stats: %d:%s\n"
+ "[dk] %s@%d:Unable to configure GCR rate: %d:%s\n"
+ "[dk] %s@%d:Unable to create GCR session: %d:%s\n"
+ "[dk] %s@%d:Unable to join GCR session: %d:%s\n"
+ "[dk] %s@%d:gcr stats get iovar failed\n"
+ "[dk] %s@%d:not enough room for gcr stats version 2 %d,%lu\n"
+ "[dk] %s@%d:not enough room for gcr subcmd resp data\n"
+ "[dk] %s@%d:stats version: %d"
+ "clearGCRStats"
+ "configureGCRRate"
+ "createGCRSession"
+ "getGCRLinkCondition"
+ "invaid GCR rate NSS\n"
+ "invaid GCR rate bandwidth\n"
+ "invaid GCR rate encoding mode\n"
+ "joinGCRSession"
+ "setNAN_CREATE_GCR_SESSION"
+ "setNAN_GCR_Multicast_Bitmap"
- "/AppleInternal/Library/BuildRoots/d6c8d13a-ff2c-11ef-b4ee-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Mar 12 2025 21:46:55"

```
