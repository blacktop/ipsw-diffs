## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1430.31.0.0.0
-  __TEXT.__text: 0x280dc4
+1430.33.0.0.0
+  __TEXT.__text: 0x2816c0
   __TEXT.__auth_stubs: 0x2480
   __TEXT.__init_offsets: 0x1b8
-  __TEXT.__cstring: 0x7d66e
-  __TEXT.__const: 0x7c930
+  __TEXT.__cstring: 0x7d8ff
+  __TEXT.__const: 0x77210
   __TEXT.__oslogstring: 0x1e6a
-  __TEXT.__unwind_info: 0x37d8
+  __TEXT.__unwind_info: 0x37e8
   __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1fa08
+  __DATA_CONST.__const: 0x1fa48
   __DATA_CONST.__osclassinfo: 0x378
   __DATA.__data: 0x590
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 6888
-  Symbols:   9586
-  CStrings:  12621
+  Functions: 6897
+  Symbols:   9600
+  CStrings:  12631
 
Symbols:
+ __ZL10bw160MHz6g
+ __ZL19nan6GoperClassTable
+ __ZL9bw80MHz6g
+ __ZN17IO80211Controller26getActionFramePoolCapacityEv
+ __ZN20AppleBCMWLANItemRing20getReadableItemCountEjj
+ __ZN20AppleBCMWLANItemRing20getWritableItemCountEjj
+ __ZN20AppleBCMWLANItemRing30getReadableItemCountContinuousEjj
+ __ZN20AppleBCMWLANItemRing30getWritableItemCountContinuousEjj
+ __ZN24AppleBCMWLANNANInterface22setP2P_STEERING_POLICYEP29apple80211_6g_steering_config
+ __ZN30AppleBCMWLANProximityInterface22setP2P_STEERING_POLICYEP29apple80211_6g_steering_config
+ __ZN30AppleBCMWLANProximityInterface26convertOpClassToNanChannelEhthPhS0_S0_
+ __ZThn112_N24AppleBCMWLANNANInterface22setP2P_STEERING_POLICYEP29apple80211_6g_steering_config
+ __ZThn112_N30AppleBCMWLANProximityInterface22setP2P_STEERING_POLICYEP29apple80211_6g_steering_config
+ __ZThn128_N24AppleBCMWLANNANInterface22setP2P_STEERING_POLICYEP29apple80211_6g_steering_config
+ __ZThn128_N30AppleBCMWLANProximityInterface22setP2P_STEERING_POLICYEP29apple80211_6g_steering_config
+ __ZThn48_N17IO80211Controller26getActionFramePoolCapacityEv
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2256
+ __block_descriptor_tmp.1653
+ __block_descriptor_tmp.1960
+ __block_descriptor_tmp.2254
+ __block_descriptor_tmp.2258
+ __block_descriptor_tmp.2276
+ __block_descriptor_tmp.2308
+ __block_descriptor_tmp.2635
+ __block_descriptor_tmp.2671
+ __block_descriptor_tmp.3143
+ __block_descriptor_tmp.3228
+ __block_descriptor_tmp.3244
+ __block_descriptor_tmp.3246
+ __block_descriptor_tmp.3249
+ __block_descriptor_tmp.3255
+ __block_descriptor_tmp.3293
+ __block_literal_global.2278
+ __block_literal_global.2310
- __ZN20AppleBCMWLANItemRing30getReadableItemCountContinuousEv
- __ZN20AppleBCMWLANItemRing30getWritableItemCountContinuousEv
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2255
- __block_descriptor_tmp.1652
- __block_descriptor_tmp.1959
- __block_descriptor_tmp.2253
- __block_descriptor_tmp.2257
- __block_descriptor_tmp.2275
- __block_descriptor_tmp.2307
- __block_descriptor_tmp.2634
- __block_descriptor_tmp.2670
- __block_descriptor_tmp.3142
- __block_descriptor_tmp.3227
- __block_descriptor_tmp.3243
- __block_descriptor_tmp.3245
- __block_descriptor_tmp.3248
- __block_descriptor_tmp.3254
- __block_descriptor_tmp.3292
- __block_literal_global.2277
- __block_literal_global.2309
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1430.33\""
+ "/AppleInternal/Library/BuildRoots/ced2dcaf-948d-11ef-b50f-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1430.33"
+ "Oct 27 2024 14:50:53"
+ "[dk] %!s(MISSING)@%!d(MISSING): parseEventLogRecordBTCoexStatsV12: Invalid btc slice_index [%!u(MISSING)] \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):%!s(MISSING):%!d(MISSING) [Steer]: policy:%!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):%!s(MISSING)[%!d(MISSING)]: bw %!d(MISSING) channel %!d(MISSING) tBw %!x(MISSING) op_class %!x(MISSING) op_class_bitmap %!x(MISSING) prim_chan_bitmap %!x(MISSING) chSpec %!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):ERROR: opclass %!x(MISSING) opclassbitmap %!x(MISSING) primchanbitmap %!x(MISSING) num_channels %!d(MISSING) \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):ERROR:NOT 6G OPCLASS: Should not come here..\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):SHOULD NOT COME HERE temp_band %!x(MISSING)\n"
+ "convertOpClassToNanChannel"
+ "setP2P_STEERING_POLICY"
+ "virtual int32_t AppleBCMWLANNANInterface::setP2P_STEERING_POLICY(apple80211_6g_steering_config *)"
+ "virtual int32_t AppleBCMWLANProximityInterface::setP2P_STEERING_POLICY(apple80211_6g_steering_config *)"
- "\"AppleBCMWLANV3_driverkit-1430.31\""
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1430.31"
- "Oct 16 2024 12:02:36"

```
