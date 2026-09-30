## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1526.62.0.0.0
-  __TEXT.__text: 0x2b3afc
+1526.70.0.0.0
+  __TEXT.__text: 0x2b4ce8
   __TEXT.__auth_stubs: 0x2530
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7f833
+  __TEXT.__cstring: 0x7fbfb
   __TEXT.__const: 0x7ec70
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5e08
+  __TEXT.__unwind_info: 0x5e18
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1298
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x209b0
+  __DATA_CONST.__const: 0x20ab8
   __DATA_CONST.__osclassinfo: 0x388
   __DATA.__data: 0x390
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 94C93CF8-7867-3409-BB27-59041E9FAB7A
-  Functions: 13102
-  Symbols:   16306
-  CStrings:  12840
+  UUID: EF5F7167-F6B3-399E-B838-F41F32301E51
+  Functions: 13126
+  Symbols:   16341
+  CStrings:  12866
 
Symbols:
+ _OUTLINED_FUNCTION_133
+ _OUTLINED_FUNCTION_146
+ _OUTLINED_FUNCTION_279
+ _ZN16AppleBCMWLANCore10getCUR_PMKEP14apple80211_pmk.cold.1
+ _ZN16AppleBCMWLANCore11saveCUR_PMKEP14apple80211_key.cold.1
+ _ZN16AppleBCMWLANCore11saveCUR_PMKEP14apple80211_key.cold.2
+ _ZN16AppleBCMWLANCore17configureWoWEntryEv.cold.6
+ _ZN16AppleBCMWLANCore17setOS_ELIGIBILITYEP25apple80211_os_eligibility.cold.1
+ _ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph.cold.8
+ _ZN22AppleBCMWLANNetAdapter23configureLongRetryLimitEj.cold.1
+ _ZN22AppleBCMWLANNetAdapter23setDefaultWMEParamsSyncEv.cold.3
+ _ZN22AppleBCMWLANNetAdapter24configureShortRetryLimitEj.cold.1
+ _ZN22AppleBCMWLANNetAdapter30setLongRetryLimitAsyncCallbackER9CommandIDiR16CommandRxPayloadPv.cold.1
+ _ZN22AppleBCMWLANNetAdapter31setShortRetryLimitAsyncCallbackER9CommandIDiR16CommandRxPayloadPv.cold.1
+ _ZN30AppleBCMWLANProximityInterface21buildAWDLChanSequenceEP37apple80211_awdl_sync_channel_sequenceP21awdl_channel_sequencePt.cold.5
+ __ZN16AppleBCMWLANCore11saveCUR_PMKEP14apple80211_key
+ __ZN16AppleBCMWLANCore17setOS_ELIGIBILITYEP25apple80211_os_eligibility
+ __ZN16AppleBCMWLANCore24isAggressiveEDCAEligibleEv
+ __ZN16AppleBCMWLANCore8is4388UpEv
+ __ZN17IO80211Controller21getPOWERTABLE_VERSIONEP23IO80211SkywalkInterfaceP34apple80211_powertable_version_data
+ __ZN20IO80211NetworkPacket5setACEh
+ __ZN20IO80211NetworkPacket6getTIDEv
+ __ZN20IO80211NetworkPacket6setTIDEh
+ __ZN21IO80211InfraInterface19setRxDataStallStatsEP22apple80211_stat_reportP31apple80211_rx_data_stall_report
+ __ZN22AppleBCMWLANNetAdapter23configureLongRetryLimitEj
+ __ZN22AppleBCMWLANNetAdapter23configureWmeParamsAsyncER12edcf_acparamR17CommandCompletion
+ __ZN22AppleBCMWLANNetAdapter24configureShortRetryLimitEj
+ __ZN22AppleBCMWLANNetAdapter30setLongRetryLimitAsyncCallbackER9CommandIDiR16CommandRxPayloadPv
+ __ZN22AppleBCMWLANNetAdapter31setShortRetryLimitAsyncCallbackER9CommandIDiR16CommandRxPayloadPv
+ __ZN23IO80211SkywalkInterface19setRxDataStallStatsEP22apple80211_stat_reportP31apple80211_rx_data_stall_report
+ __ZN25AppleBCMWLANInfraProtocol17setOS_ELIGIBILITYEP25apple80211_os_eligibility
+ __ZN25AppleBCMWLANInfraProtocol17setTX_MODE_CONFIGEP25apple80211_tx_mode_config
+ __ZThn112_N25AppleBCMWLANInfraProtocol17setOS_ELIGIBILITYEP25apple80211_os_eligibility
+ __ZThn112_N25AppleBCMWLANInfraProtocol17setTX_MODE_CONFIGEP25apple80211_tx_mode_config
+ __ZThn128_N25AppleBCMWLANInfraProtocol17setOS_ELIGIBILITYEP25apple80211_os_eligibility
+ __ZThn128_N25AppleBCMWLANInfraProtocol17setTX_MODE_CONFIGEP25apple80211_tx_mode_config
+ __ZThn48_N17IO80211Controller21getPOWERTABLE_VERSIONEP23IO80211SkywalkInterfaceP34apple80211_powertable_version_data
+ __ZThn56_N20IO80211NetworkPacket5setACEh
+ __ZThn56_N20IO80211NetworkPacket6getTIDEv
+ __ZThn56_N20IO80211NetworkPacket6setTIDEh
+ __ZThn64_N16AppleBCMWLANCore17setOS_ELIGIBILITYEP25apple80211_os_eligibility
+ __ZThn80_N21IO80211InfraInterface19setRxDataStallStatsEP22apple80211_stat_reportP31apple80211_rx_data_stall_report
+ __ZThn80_N23IO80211SkywalkInterface19setRxDataStallStatsEP22apple80211_stat_reportP31apple80211_rx_data_stall_report
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2273
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2273.cold.1
+ __block_descriptor_tmp.1669
+ __block_descriptor_tmp.1974
+ __block_descriptor_tmp.2271
+ __block_descriptor_tmp.2275
+ __block_descriptor_tmp.2293
+ __block_descriptor_tmp.2327
+ __block_descriptor_tmp.2653
+ __block_descriptor_tmp.2689
+ __block_descriptor_tmp.3153
+ __block_descriptor_tmp.3236
+ __block_descriptor_tmp.3252
+ __block_descriptor_tmp.3254
+ __block_descriptor_tmp.3257
+ __block_descriptor_tmp.3263
+ __block_descriptor_tmp.3301
+ __block_literal_global.2295
+ __block_literal_global.2329
- _OUTLINED_FUNCTION_134
- _OUTLINED_FUNCTION_147
- _ZN22AppleBCMWLANNetAdapter19configureRetryLimitEj.cold.1
- _ZN22AppleBCMWLANNetAdapter26setRetryLimitAsyncCallbackER9CommandIDiR16CommandRxPayloadPv.cold.1
- __ZN20IO80211NetworkPacket5setACEj
- __ZN22AppleBCMWLANNetAdapter19configureRetryLimitEj
- __ZN22AppleBCMWLANNetAdapter26setRetryLimitAsyncCallbackER9CommandIDiR16CommandRxPayloadPv
- __ZThn56_N20IO80211NetworkPacket5setACEj
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2266
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2266.cold.1
- __block_descriptor_tmp.1662
- __block_descriptor_tmp.1967
- __block_descriptor_tmp.2264
- __block_descriptor_tmp.2268
- __block_descriptor_tmp.2286
- __block_descriptor_tmp.2320
- __block_descriptor_tmp.2646
- __block_descriptor_tmp.2682
- __block_descriptor_tmp.3143
- __block_descriptor_tmp.3226
- __block_descriptor_tmp.3242
- __block_descriptor_tmp.3244
- __block_descriptor_tmp.3247
- __block_descriptor_tmp.3253
- __block_descriptor_tmp.3291
- __block_literal_global.2288
- __block_literal_global.2322
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1526.70\""
+ "/AppleInternal/Library/BuildRoots/4~B3ZcugBdhXEPfJRmC9dJ2kcvofhMZFDRYmWeLtk/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1526.70"
+ "Jun 18 2025 21:17:18"
+ "STALL_IN_PROGRESS "
+ "STALL_MU "
+ "STALL_NON_MU "
+ "STALL_TIM_SET "
+ "[dk] %s@%d: %s BE traffic\n"
+ "[dk] %s@%d: Aggressive EDCA eligibility changed: %u->%u\n"
+ "[dk] %s@%d: Aggressive EDCA eligible: %u. Country code: %.2s\n"
+ "[dk] %s@%d: Error: cannot set short retry count: ret %x: %s\n"
+ "[dk] %s@%d: Error: cannot set wme_ac_sta (BE): ret %x %s\n"
+ "[dk] %s@%d: Restoring SRL\n"
+ "[dk] %s@%d: setting DFS channel %d bandwidth %d\n"
+ "[dk] %s@%d: setting Short Retry Limit failure, error %s\n"
+ "[dk] %s@%d:%s %d Length check failed with reasonCode %d"
+ "[dk] %s@%d:Get PMK: %p len=%d\n"
+ "[dk] %s@%d:Invalid hc data %d %zu %zu \n"
+ "[dk] %s@%d:Join Adaptor SetKey enter PMK: Cipher=0x%x Len=%d\n"
+ "[dk] %s@%d:PMK data[%d]: %02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X\n"
+ "[dk] %s@%d:Rx Stall %s [if_idx=%u ac=%u link=%u] [Bitmap Reason(s): %s] - Pkts=%u Dropped=%u AlertTh=%u\n"
+ "[dk] %s@%d:Rx Stall Reason Code %s - NumPkts Considered=%u, NumPkts Dropped=%u, Alert Threshold=%u\n"
+ "[dk] %s@%d:Save PMK: %p len=%d type=0x%x\n"
+ "[dk] %s@%d:Save PMK: ok Len:%d TLV_LEN:%d\n"
+ "[dk] %s@%d:SetKey save PMK:\n"
+ "configureLongRetryLimit"
+ "configureShortRetryLimit"
+ "getCUR_PMK"
+ "none"
+ "saveCUR_PMK"
+ "setLongRetryLimitAsyncCallback"
+ "setOS_ELIGIBILITY"
+ "setShortRetryLimitAsyncCallback"
+ "wifi"
+ "wlan.enableNANDebug"
- "\"AppleBCMWLANV3_driverkit-1526.62\""
- "/AppleInternal/Library/BuildRoots/4~B2ABugDkslcChvMwGs2VprQQs5HqnFa0rHHuL4E/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1526.62"
- "May 30 2025 19:23:25"
- "[dk] %s@%d: %s BE traffic"
- "[dk] %s@%d:%s %d Length check failed withreasonCode %d"
- "[dk] %s@%d:Active port allocation failure\n"
- "[dk] %s@%d:Rx Stall Reason Code %s- NumPkts Considered=%u, NumPkts Dropped=%u, Alert Threshold=%u\n"
- "configureRetryLimit"
- "setRetryLimitAsyncCallback"

```
