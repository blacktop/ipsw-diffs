## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1526.83.0.0.0
-  __TEXT.__text: 0x2b6efc
+1535.5.0.0.0
+  __TEXT.__text: 0x2b73d0
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x80262
+  __TEXT.__cstring: 0x8031f
   __TEXT.__const: 0x7ee40
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e78
+  __TEXT.__unwind_info: 0x5e98
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 5EF6D90A-6EEA-35D0-9743-85541B1F6DE8
-  Functions: 13165
-  Symbols:   16389
-  CStrings:  12899
+  UUID: 3A339EE5-9068-34CA-8A28-1766C48023A5
+  Functions: 13167
+  Symbols:   16392
+  CStrings:  12903
 
Symbols:
+ _OUTLINED_FUNCTION_134
+ _OUTLINED_FUNCTION_147
+ _OUTLINED_FUNCTION_280
+ _ZN16AppleBCMWLANCore14setIPV4_PARAMSEP22apple80211_ipv4_params.cold.1
+ _ZN16AppleBCMWLANCore14setOFFLOAD_ARPEP27apple80211_offload_arp_data.cold.1
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2284
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2284.cold.1
+ __block_descriptor_tmp.2282
+ __block_descriptor_tmp.2286
+ __block_descriptor_tmp.2304
+ __block_descriptor_tmp.2338
+ __block_descriptor_tmp.2665
+ __block_descriptor_tmp.2701
+ __block_descriptor_tmp.3166
+ __block_descriptor_tmp.3249
+ __block_descriptor_tmp.3267
+ __block_descriptor_tmp.3270
+ __block_descriptor_tmp.3276
+ __block_descriptor_tmp.3314
+ __block_literal_global.2306
+ __block_literal_global.2340
- _OUTLINED_FUNCTION_135
- _OUTLINED_FUNCTION_148
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2283
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2283.cold.1
- __block_descriptor_tmp.2281
- __block_descriptor_tmp.2285
- __block_descriptor_tmp.2303
- __block_descriptor_tmp.2337
- __block_descriptor_tmp.2664
- __block_descriptor_tmp.2700
- __block_descriptor_tmp.3164
- __block_descriptor_tmp.3247
- __block_descriptor_tmp.3263
- __block_descriptor_tmp.3268
- __block_descriptor_tmp.3274
- __block_descriptor_tmp.3312
- __block_literal_global.2305
- __block_literal_global.2339
Functions:
~ __ZN23AppleBCMWLANJoinAdapter11performJoinEP25apple80211AssocCandidates : 5016 -> 5036
~ __ZN23AppleBCMWLANJoinAdapter10handleAuthEP14wl_event_msg_t : 936 -> 1024
~ __ZN16AppleBCMWLANCore22updateWoWReasonToIoRegEjPcjjj : 340 -> 364
~ __ZN16AppleBCMWLANCore36handleKeepaliveDataNotificationGatedEPv : 324 -> 484
~ __ZN16AppleBCMWLANCore14setOFFLOAD_ARPEP27apple80211_offload_arp_data : 788 -> 936
~ __ZN16AppleBCMWLANCore14setIPV4_PARAMSEP22apple80211_ipv4_params : 192 -> 344
+ _OUTLINED_FUNCTION_230
- _OUTLINED_FUNCTION_277
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 4 -> 60
~ _ZN16AppleBCMWLANCore22handlePowerStateChangeE22apple80211_power_state.cold.1 : 176 -> 172
+ _ZN16AppleBCMWLANCore14setOFFLOAD_ARPEP27apple80211_offload_arp_data.cold.1
+ _ZN16AppleBCMWLANCore14setIPV4_PARAMSEP22apple80211_ipv4_params.cold.1
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 104 -> 100
+ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv
- __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv
CStrings:
+ " Reason unknown, please add it"
+ "\"AppleBCMWLANV3_driverkit-1535.5\""
+ "/AppleInternal/Library/BuildRoots/4~B9nwugBULgfjvgbKioRFtBGCu9lWEjGfK4x07x8/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1535.5"
+ "Sep 11 2025 20:35:19"
+ "[dk] %s@%d: Router IPv4 address = %u.%u.%u.%u, MAC = %02X:%02X:%02X:%02X:%02X:%02X\n"
+ "[dk] %s@%d: Router MAC address for ARP = %02X:%02X:%02X:%02X:%02X:%02X\n"
+ "[dk] %s@%d: Router MAC address for IPv4 = %02X:%02X:%02X:%02X:%02X:%02X\n"
+ "[dk] %s@%d:%s reason<%d> -> <%d>, type<%d> subtype<%d> tkoWakeReason<%d>\n"
+ "setIPV4_PARAMS"
- "\"AppleBCMWLANV3_driverkit-1526.83\""
- "/AppleInternal/Library/BuildRoots/4~B6_NugBy6q6w6JYr5eIJtFlgsbk67Pm-Ar6TmsA/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1526.83"
- "Aug  6 2025 21:38:10"
- "[dk] %s@%d: Router IPv4 address = %u.%u.%u.%u, MAC = %02x:%02x:%02x:%02x:%02x:%02x\n"
- "[dk] %s@%d:Reason unknown, please add it reason<%d> type<%d> subtype<%d>\n"

```
