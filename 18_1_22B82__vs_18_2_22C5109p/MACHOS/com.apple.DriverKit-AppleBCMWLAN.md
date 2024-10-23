## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1260.10.0.0.0
-  __TEXT.__text: 0x280ba4
+1430.31.0.0.0
+  __TEXT.__text: 0x280dc4
   __TEXT.__auth_stubs: 0x2480
   __TEXT.__init_offsets: 0x1b8
-  __TEXT.__cstring: 0x7d5ca
-  __TEXT.__const: 0x7d070
+  __TEXT.__cstring: 0x7d66e
+  __TEXT.__const: 0x7c930
   __TEXT.__oslogstring: 0x1e6a
-  __TEXT.__unwind_info: 0x37d0
+  __TEXT.__unwind_info: 0x37d8
   __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1f9d8
+  __DATA_CONST.__const: 0x1fa08
   __DATA_CONST.__osclassinfo: 0x378
   __DATA.__data: 0x590
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 6885
-  Symbols:   9584
-  CStrings:  12620
+  Functions: 6888
+  Symbols:   9586
+  CStrings:  12621
 
Symbols:
+ _ZN15AppleBCMWLANLQM18getMloPerLinkStatsEhR10ether_addr.cold.1
+ __ZN15AppleBCMWLANLQM14updateCountersER10ether_addr
+ __ZN15AppleBCMWLANLQM15getMloPerfStatsER10ether_addr
+ __ZN15AppleBCMWLANLQM18getMloPerLinkStatsEhR10ether_addr
+ __ZN15AppleBCMWLANLQM7loadBssERbR10ether_addr
+ __ZN16AppleBCMWLANCore29convertChannelNumToCenterFreqE18apple80211_channelj
+ __ZN25AppleBCMWLANInfraProtocol13setSDB_ENABLEEP21apple80211_sdb_enable
+ __ZThn112_N25AppleBCMWLANInfraProtocol13setSDB_ENABLEEP21apple80211_sdb_enable
+ __ZThn128_N25AppleBCMWLANInfraProtocol13setSDB_ENABLEEP21apple80211_sdb_enable
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2255
+ __block_descriptor_tmp.1652
+ __block_descriptor_tmp.1959
+ __block_descriptor_tmp.2253
+ __block_descriptor_tmp.2257
+ __block_descriptor_tmp.2275
+ __block_descriptor_tmp.2307
+ __block_descriptor_tmp.2634
+ __block_descriptor_tmp.2670
+ __block_descriptor_tmp.3142
+ __block_descriptor_tmp.3227
+ __block_descriptor_tmp.3245
+ __block_descriptor_tmp.3248
+ __block_descriptor_tmp.3254
+ __block_descriptor_tmp.3292
+ __block_descriptor_tmp.659
+ __block_descriptor_tmp.796
+ __block_descriptor_tmp.938
+ __block_literal_global.2277
+ __block_literal_global.2309
- _ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh.cold.1
- __ZL35wl2apple80211_channel_switch_reason
- __ZN15AppleBCMWLANLQM14updateCountersEv
- __ZN15AppleBCMWLANLQM15getMloPerfStatsEv
- __ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh
- __ZN15AppleBCMWLANLQM7loadBssERb
- __ZN16AppleBCMWLANCore34convert20MHzChannelNumToCenterFreqE18apple80211_channel
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2253
- __block_descriptor_tmp.1650
- __block_descriptor_tmp.1957
- __block_descriptor_tmp.2251
- __block_descriptor_tmp.2255
- __block_descriptor_tmp.2273
- __block_descriptor_tmp.2305
- __block_descriptor_tmp.2632
- __block_descriptor_tmp.2668
- __block_descriptor_tmp.3140
- __block_descriptor_tmp.3225
- __block_descriptor_tmp.3241
- __block_descriptor_tmp.3246
- __block_descriptor_tmp.3252
- __block_descriptor_tmp.3290
- __block_descriptor_tmp.657
- __block_descriptor_tmp.794
- __block_descriptor_tmp.936
- __block_literal_global.2275
- __block_literal_global.2307
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1430.31\""
+ "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1430.31"
+ "Oct 16 2024 12:02:36"
+ "[dk] %!s(MISSING)@%!d(MISSING):convertChannelNumToCenterFreq: 5G channel = %!d(MISSING), center channel = %!d(MISSING), bandwidth = %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):convertChannelNumToCenterFreq: 6G channel = %!d(MISSING), center channel = %!d(MISSING), bandwidth = %!d(MISSING)\n"
+ "convertChannelNumToCenterFreq"
- "\"AppleBCMWLANV3_driverkit-1260.10\""
- "/AppleInternal/Library/BuildRoots/955b7ce0-87db-11ef-857c-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1260.10"
- "Oct 11 2024 18:44:10"
- "[dk] %!s(MISSING)@%!d(MISSING): Failed to get bssid, error %!s(MISSING)\n"
- "updateCounters"

```
