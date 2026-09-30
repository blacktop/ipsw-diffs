## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1526.75.0.0.0
-  __TEXT.__text: 0x2b5b8c
+1526.82.0.0.0
+  __TEXT.__text: 0x2b6f1c
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x80035
+  __TEXT.__cstring: 0x80262
   __TEXT.__const: 0x7ee40
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e58
+  __TEXT.__unwind_info: 0x5e80
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: C9B2528F-2A74-32E8-84D6-17D80D271022
-  Functions: 13148
-  Symbols:   16372
-  CStrings:  12883
+  UUID: 7198F5C9-B4F3-306C-AB29-2E43572DC3F8
+  Functions: 13165
+  Symbols:   16389
+  CStrings:  12899
 
Symbols:
+ _ZN16AppleBCMWLANCore11setupDriverEv.cold.13
+ _ZN16AppleBCMWLANCore13setupFirmwareEPK21AppleBCMWLANChipImage.cold.71
+ _ZN16AppleBCMWLANCore13setupFirmwareEPK21AppleBCMWLANChipImage.cold.72
+ _ZN16AppleBCMWLANCore13setupFirmwareEPK21AppleBCMWLANChipImage.cold.73
+ _ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t.cold.25
+ _ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t.cold.26
+ _ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t.cold.27
+ _ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t.cold.28
+ _ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t.cold.29
+ _ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t.cold.30
+ _ZN16AppleBCMWLANCore22setBTCSlottedBssPolicyEj.cold.1
+ _ZN16AppleBCMWLANCore22setBTCSlottedBssPolicyEj.cold.2
+ _ZN16AppleBCMWLANCore35setBTCSlottedBssPolicyAsyncCallbackER9CommandIDiR16CommandRxPayloadPv.cold.1
+ _ZN16AppleBCMWLANCore4initEP12OSDictionary.cold.2
+ _ZN24AppleBCMWLANNANInterface10disableNANEv.cold.2
+ _ZN24AppleBCMWLANNANInterface33handleNANEventDataPathEstablishedEP14wl_event_msg_t.cold.6
+ __ZN16AppleBCMWLANCore22setBTCSlottedBssPolicyEj
+ __ZN16AppleBCMWLANCore35setBTCSlottedBssPolicyAsyncCallbackER9CommandIDiR16CommandRxPayloadPv
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2283
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2283.cold.1
+ __block_descriptor_tmp.1679
+ __block_descriptor_tmp.1984
+ __block_descriptor_tmp.2281
+ __block_descriptor_tmp.2285
+ __block_descriptor_tmp.2303
+ __block_descriptor_tmp.2337
+ __block_descriptor_tmp.2664
+ __block_descriptor_tmp.2700
+ __block_descriptor_tmp.3164
+ __block_descriptor_tmp.3247
+ __block_descriptor_tmp.3263
+ __block_descriptor_tmp.3265
+ __block_descriptor_tmp.3268
+ __block_descriptor_tmp.3274
+ __block_descriptor_tmp.3312
+ __block_descriptor_tmp.686
+ __block_descriptor_tmp.814
+ __block_descriptor_tmp.955
+ __block_literal_global.2305
+ __block_literal_global.2339
- _ZN16AppleBCMWLANCore27configureDefaultCountryCodeEv.cold.9
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2269
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2269.cold.1
- __block_descriptor_tmp.1665
- __block_descriptor_tmp.1970
- __block_descriptor_tmp.2267
- __block_descriptor_tmp.2271
- __block_descriptor_tmp.2289
- __block_descriptor_tmp.2323
- __block_descriptor_tmp.2652
- __block_descriptor_tmp.2688
- __block_descriptor_tmp.3152
- __block_descriptor_tmp.3235
- __block_descriptor_tmp.3251
- __block_descriptor_tmp.3253
- __block_descriptor_tmp.3256
- __block_descriptor_tmp.3262
- __block_descriptor_tmp.3300
- __block_descriptor_tmp.673
- __block_descriptor_tmp.801
- __block_descriptor_tmp.942
- __block_literal_global.2291
- __block_literal_global.2325
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1526.82\""
+ "/AppleInternal/Library/BuildRoots/4~B5F_ugDozVWNCFTxedUflh6x0CHb32V68QpAjOY/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1526.82"
+ "Jul 12 2025 01:02:27"
+ "[dk] %s@%d: Issuing btc_slotted_bss_policy (%d) to FW\n"
+ "[dk] %s@%d:Applying offset of %d."
+ "[dk] %s@%d:Disabling btc slotted bss policy\n"
+ "[dk] %s@%d:Enabling btc slotted bss policy\n"
+ "[dk] %s@%d:Setting btc_slotted_bss_policy callback failed: %s(%d)\n"
+ "[dk] %s@%d:Setting fRangingCorrectionCore0=%d, fRangingCorrectionCore1=%d"
+ "[dk] %s@%d:wlan.ranging.applyRangingoffsetsVsAVP %d\n"
+ "btc_slotted_bss_policy"
+ "marigold"
+ "muscari"
+ "petunia"
+ "poppy"
+ "setBTCSlottedBssPolicy"
+ "setBTCSlottedBssPolicyAsyncCallback"
+ "wlan.isDisable6gFollouwpInLowRssi"
+ "wlan.ranging.applyRangingoffsetsVsAVP"
- "\"AppleBCMWLANV3_driverkit-1526.75\""
- "/AppleInternal/Library/BuildRoots/4~B4R2ugDh2wfuAqJPfm1mN4BjmnXkR819EWIbUVE/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1526.75"
- "Jun 30 2025 22:01:18"

```
