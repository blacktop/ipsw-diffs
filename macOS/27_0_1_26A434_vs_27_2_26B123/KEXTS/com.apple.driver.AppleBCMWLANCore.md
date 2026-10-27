## com.apple.driver.AppleBCMWLANCore

> `com.apple.driver.AppleBCMWLANCore`

```diff

-1570.66.0.0.0
+1572.8.0.0.0
   __TEXT.__os_log: 0x73b7
   __TEXT.__const: 0x2b88
-  __TEXT.__cstring: 0x6fa5e
-  __TEXT_EXEC.__text: 0x212880
+  __TEXT.__cstring: 0x70030
+  __TEXT_EXEC.__text: 0x213358
   __TEXT_EXEC.__auth_stubs: 0x1b30
   __DATA.__data: 0x492
   __DATA.__common: 0x478
   __DATA.__bss: 0xde0
   __DATA_CONST.__mod_init_func: 0x208
   __DATA_CONST.__mod_term_func: 0x1f8
-  __DATA_CONST.__const: 0x1f330
+  __DATA_CONST.__const: 0x1f370
   __DATA_CONST.__kalloc_type: 0x4440
   __DATA_CONST.__kalloc_var: 0x230
   __DATA_CONST.__auth_got: 0xd98
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 4343
-  Symbols:   6955
-  CStrings:  11582
+  Functions: 4348
+  Symbols:   6961
+  CStrings:  11597
 
Symbols:
+ __ZN16AppleBCMWLANCore33checkForAdaptive11rFromASRSupportEv
+ __ZN23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ __ZN24AppleBCMWLANNANInterface15flushFlowQueuesEP10ether_addr
+ __ZN30AppleBCMWLANProximityInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
+ __ZN30AppleBCMWLANProximityInterface27applyInitialChannelSequenceEPKc
+ __ZN30AppleBCMWLANProximityInterface30fillSliceDataForStandAloneAWDLEP37apple80211_awdl_sync_channel_sequenceP21awdl_channel_sequencePhS4_PiS5_
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51921
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51932
+ __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30126
+ __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30136
+ __ZZN16AppleBCMWLANCore34handlePeerStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_29972
+ __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29057
+ __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29111
+ __ZZN23AppleBCMWLANJoinAdapter14initWithDriverEP16AppleBCMWLANCorePFiP8OSObject17JoinFirmwareEventPvES3_E21kalloc_type_view_1154
+ __ZZN23AppleBCMWLANJoinAdapter4freeEvE20kalloc_type_view_122
+ __ZZN24AppleBCMWLANNANInterface15sendNANSetIOVAREPvjhE21kalloc_type_view_3943
+ __ZZN24AppleBCMWLANNANInterface15sendNANSetIOVAREPvjhE21kalloc_type_view_3951
+ __ZZN24AppleBCMWLANNANInterface15sendNANSetIOVAREPvjhE21kalloc_type_view_3975
+ __ZZN24AppleBCMWLANNANInterface27handleNANIovarAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_3720
+ __ZZN24AppleBCMWLANNANInterface31handleCacheControlAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_6511
+ __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_61816
+ __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_61904
+ __ZZN30AppleBCMWLANProximityInterface18sendUnicastAFIOVarEP5iovecjE21kalloc_type_view_2469
+ __ZZN30AppleBCMWLANProximityInterface18sendUnicastAFIOVarEP5iovecjE21kalloc_type_view_2486
+ __ZZN30AppleBCMWLANProximityInterface29handleOobAfIovarAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_2421
+ __ZZN30AppleBCMWLANProximityInterface41getAWDL_AF_SECONDARY_PAYLOAD_CAPABILITIESEP19apple80211_awdl_capE21kalloc_type_view_2881
+ __ZZN30AppleBCMWLANProximityInterface41getAWDL_AF_SECONDARY_PAYLOAD_CAPABILITIESEP19apple80211_awdl_capE21kalloc_type_view_2908
+ __ZZN30AppleBCMWLANProximityInterface4freeEvE21kalloc_type_view_1070
+ __ZZN30AppleBCMWLANProximityInterface4initEvE20kalloc_type_view_892
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51915
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51926
- __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30120
- __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30130
- __ZZN16AppleBCMWLANCore34handlePeerStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_29966
- __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29051
- __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29105
- __ZZN23AppleBCMWLANJoinAdapter14initWithDriverEP16AppleBCMWLANCorePFiP8OSObject17JoinFirmwareEventPvES3_E21kalloc_type_view_1143
- __ZZN23AppleBCMWLANJoinAdapter4freeEvE20kalloc_type_view_117
- __ZZN24AppleBCMWLANNANInterface15sendNANSetIOVAREPvjhE21kalloc_type_view_3904
- __ZZN24AppleBCMWLANNANInterface15sendNANSetIOVAREPvjhE21kalloc_type_view_3912
- __ZZN24AppleBCMWLANNANInterface15sendNANSetIOVAREPvjhE21kalloc_type_view_3936
- __ZZN24AppleBCMWLANNANInterface27handleNANIovarAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_3681
- __ZZN24AppleBCMWLANNANInterface31handleCacheControlAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_6472
- __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_61805
- __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_61893
- __ZZN30AppleBCMWLANProximityInterface18sendUnicastAFIOVarEP5iovecjE21kalloc_type_view_2450
- __ZZN30AppleBCMWLANProximityInterface18sendUnicastAFIOVarEP5iovecjE21kalloc_type_view_2467
- __ZZN30AppleBCMWLANProximityInterface29handleOobAfIovarAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_2402
- __ZZN30AppleBCMWLANProximityInterface41getAWDL_AF_SECONDARY_PAYLOAD_CAPABILITIESEP19apple80211_awdl_capE21kalloc_type_view_2862
- __ZZN30AppleBCMWLANProximityInterface41getAWDL_AF_SECONDARY_PAYLOAD_CAPABILITIESEP19apple80211_awdl_capE21kalloc_type_view_2889
- __ZZN30AppleBCMWLANProximityInterface4freeEvE21kalloc_type_view_1051
- __ZZN30AppleBCMWLANProximityInterface4initEvE20kalloc_type_view_879
Functions:
~ __ZN23AppleBCMWLANJoinAdapter11performJoinEP25apple80211AssocCandidates : 8048 -> 8100
~ __ZN23AppleBCMWLANJoinAdapter33collectImmediateFaultDataCallbackEP13CCFaultReport : 420 -> 448
~ __ZN16AppleBCMWLANCore20getCARD_CAPABILITIESEP23IO80211SkywalkInterfaceP26apple80211_capability_data : 3076 -> 3144
+ __ZN16AppleBCMWLANCore33checkForAdaptive11rFromASRSupportEv
~ __ZN30AppleBCMWLANProximityInterface11handleEventERK19IO80211BufferCursor : 7176 -> 7292
+ __ZN30AppleBCMWLANProximityInterface27applyInitialChannelSequenceEPKc
~ __ZN30AppleBCMWLANProximityInterface4initEP16AppleBCMWLANCoreP10ether_addrjPc : 2144 -> 2160
~ __ZN30AppleBCMWLANProximityInterface27handleProxSlotBSSCompletionER9CommandIDiR16CommandRxPayloadPv : 768 -> 948
~ __ZN30AppleBCMWLANProximityInterface19deleteChipInterfaceEv : 1404 -> 1412
~ __ZN30AppleBCMWLANProximityInterface24buildChanSequenceCommandEP37apple80211_awdl_sync_channel_sequenceP37apple80211_nan_committed_availability : 4404 -> 4428
~ __ZN30AppleBCMWLANProximityInterface5resetEv : 692 -> 700
+ __ZN30AppleBCMWLANProximityInterface30fillSliceDataForStandAloneAWDLEP37apple80211_awdl_sync_channel_sequenceP21awdl_channel_sequencePhS4_PiS5_
+ __ZN30AppleBCMWLANProximityInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
~ __ZN24AppleBCMWLANNANInterface30handleEventNANFollowupReceivedEP14wl_event_msg_t : 2248 -> 2888
+ __ZN24AppleBCMWLANNANInterface15flushFlowQueuesEP10ether_addr
CStrings:
+ " (NAN availability pending, will ride the next real sequence)"
+ " (WLC_E_IF_ADD retry)"
+ " + NAN availability"
+ "\"AppleBCMWLANV3_Drivers-1572.8\""
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/apple80211/IO80211Util.h"
+ "11212221112222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212221111111111111112212"
+ "<redacted>"
+ "AppleBCMWLANV3_Drivers-1572.8"
+ "Oct 14 2026 23:04:07"
+ "[ik] %s@%d:%s[%d] : Neither channel sequences specified. Bogus command ?\n"
+ "[ik] %s@%d:ERROR: NAN attribute header runs past the end of the attribute list\n"
+ "[ik] %s@%d:ERROR: NAN attribute length %u exceeds the remaining attribute list\n"
+ "[ik] %s@%d:ERROR: NAN shared key descriptor body %u too short, minimum %u\n"
+ "[ik] %s@%d:ERROR: NAN shared key descriptor key data length %u exceeds body %u\n"
+ "[ik] %s@%d:SlotBSS: deferred #%u (guard=fBcmInterfaceIdValid) id=%d valid=%d -- sequence saved, will replay on WLC_E_IF_ADD/interface creation\n"
+ "[ik] %s@%d:SlotBSS: deferred #%u (guard=fInterfaceCreated) -- sequence saved, will replay on interface creation\n"
+ "[ik] %s@%d:SlotBSS: no-op%s: no deferred channel sequence to replay (cached len=%u, pending=%d) -- not sending slot_bss%s\n"
+ "[ik] %s@%d:SlotBSS: replay #%u%s: FW AWDL interface created, re-applying deferred sequence len=%u enc=%u step=%u dup=%u flags=0x%x ch[0]=%u%s\n"
+ "[ik] %s@%d:SlotBSS: watchdog-skipped #%u -- SlotBSS failed but interface already invalid (chip reset in flight)\n"
+ "applyInitialChannelSequence"
- "\"AppleBCMWLANV3_Drivers-1570.66\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/apple80211/IO80211Util.h"
- "11212221112222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212221111111111111112212"
- "AppleBCMWLANV3_Drivers-1570.66"
- "Sep 18 2026 21:50:45"
```
