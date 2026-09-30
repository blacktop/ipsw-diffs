## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1535.9.0.0.0
-  __TEXT.__text: 0x2b77b4
+  __TEXT.__text: 0x2b776c
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x8035f

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: F334C434-25F9-31BA-A40E-686C7246BA57
-  Functions: 13170
-  Symbols:   16395
+  UUID: C8F4D642-88C7-364A-AE0D-548F92BFEC78
+  Functions: 13171
+  Symbols:   16397
   CStrings:  12905
 
Symbols:
+ _OUTLINED_FUNCTION_148
+ _OUTLINED_FUNCTION_281
+ _OUTLINED_FUNCTION_282
- _OUTLINED_FUNCTION_149
Functions:
+ _OUTLINED_FUNCTION_148
+ _OUTLINED_FUNCTION_156
- _OUTLINED_FUNCTION_156
~ _ZN15AppleBCMWLANLQM24updateLinkQualityMetricsEb.cold.3 : 100 -> 96
~ _ZN15AppleBCMWLANLQM24updateLinkQualityMetricsEb.cold.6 : 100 -> 96
~ _ZN25AppleBCMWLANBGScanAdapter33handleGetMotionStateAsyncCallBackER9CommandIDiR16CommandRxPayloadPv.cold.2 : 124 -> 116
~ __ZN23AppleBCMWLANRoamAdapter20restoreReassocParamsEv : 88 -> 84
~ _ZN30AppleBCMWLANProximityInterface11handleEventERK19IO80211BufferCursor.cold.29 : 96 -> 104
~ __ZN39AppleBCMWLANDynamicRingOperationContext18initWithCompletionEP30DynamicRingOperationCompletion : 172 -> 160
~ __ZN28AppleBCMWLANKeepAliveOffload14handleTKOEventEP14wl_event_msg_t : 176 -> 188
~ __ZN16AppleBCMWLANCore8findWordEPKcS1_m : 200 -> 192
~ __ZN16AppleBCMWLANCore14getBssPhyModdeEP21AppleBCMWLANBSSBeacon : 488 -> 484
~ __ZN16AppleBCMWLANCore16getDYNSAR_DETAILEP24apple80211_dynsar_detail : 160 -> 148
~ __ZN16AppleBCMWLANCore29getCOLOCATED_NETWORK_SCOPE_IDEP37apple80211_colocated_network_scope_id : 44 -> 40
~ __ZThn64_N16AppleBCMWLANCore29getCOLOCATED_NETWORK_SCOPE_IDEP37apple80211_colocated_network_scope_id : 44 -> 40
~ __ZN16AppleBCMWLANCore10set6G_MODEEP18apple80211_6G_mode : 116 -> 112
~ __ZN16AppleBCMWLANCore16setHT_CAPABILITYEP24apple80211_ht_capability : 28 -> 24
~ __ZThn64_N16AppleBCMWLANCore16setHT_CAPABILITYEP24apple80211_ht_capability : 28 -> 24
~ __ZN16AppleBCMWLANCore17setVHT_CAPABILITYEP25apple80211_vht_capability : 40 -> 36
~ __ZThn64_N16AppleBCMWLANCore17setVHT_CAPABILITYEP25apple80211_vht_capability : 40 -> 36
~ __ZN16AppleBCMWLANCore13getRADIO_INFOEP26apple80211_radio_info_data : 20 -> 12
~ __ZThn64_N16AppleBCMWLANCore13getRADIO_INFOEP26apple80211_radio_info_data : 20 -> 12
~ __ZN28AppleBCMWLANBusInterfacePCIe24prepareForRingSubmissionEt : 208 -> 204
~ _ZN28AppleBCMWLANBusInterfacePCIe17handleMBDataOOBDWEj.cold.7 : 96 -> 104
~ __ZN27AppleBCMWLANChipManagerPCIe23setChipProvisioningDataEPKcP8OSObject : 72 -> 68
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBlfugBI22H-Pes89jA-us1bkvmkIQ-sKRRO4ck/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Nov  4 2025 22:41:02"
- "/AppleInternal/Library/BuildRoots/4~CBNcugCfTJnjnFGvGUKuKfXopZXA4McNhtuMklE/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Oct 30 2025 20:34:47"

```
