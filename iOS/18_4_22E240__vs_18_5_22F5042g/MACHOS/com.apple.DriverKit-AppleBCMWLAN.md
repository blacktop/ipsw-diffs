## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1475.46.0.0.0
-  __TEXT.__text: 0x2b0a2c
+1485.1.0.0.0
+  __TEXT.__text: 0x2b0e20
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7e56c
-  __TEXT.__const: 0x7e310
+  __TEXT.__cstring: 0x7e76a
+  __TEXT.__const: 0x7e320
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5d60
+  __TEXT.__unwind_info: 0x5d70
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1270
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x20228
+  __DATA_CONST.__const: 0x20238
   __DATA_CONST.__osclassinfo: 0x388
   __DATA.__data: 0x390
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 13065
-  Symbols:   16278
-  CStrings:  12690
+  Functions: 13069
+  Symbols:   16282
+  CStrings:  12696
 
Symbols:
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.1
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.2
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.3
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.4
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2270
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2270.cold.1
+ __block_descriptor_tmp.2272
+ __block_descriptor_tmp.2290
+ __block_descriptor_tmp.2324
+ __block_descriptor_tmp.2650
+ __block_descriptor_tmp.2686
+ __block_descriptor_tmp.3143
+ __block_descriptor_tmp.3226
+ __block_descriptor_tmp.3242
+ __block_descriptor_tmp.3244
+ __block_descriptor_tmp.3247
+ __block_descriptor_tmp.3253
+ __block_descriptor_tmp.3291
+ __block_literal_global.2292
+ __block_literal_global.2326
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2266
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2266.cold.1
- __block_descriptor_tmp.2264
- __block_descriptor_tmp.2286
- __block_descriptor_tmp.2320
- __block_descriptor_tmp.2646
- __block_descriptor_tmp.2682
- __block_descriptor_tmp.3139
- __block_descriptor_tmp.3222
- __block_descriptor_tmp.3238
- __block_descriptor_tmp.3240
- __block_descriptor_tmp.3243
- __block_descriptor_tmp.3249
- __block_descriptor_tmp.3287
- __block_literal_global.2288
- __block_literal_global.2322
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1485.1\""
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1485.1"
+ "LinkLoss"
+ "LinkTestFailure"
+ "Mar 21 2025 21:47:49"
+ "[dk] %s@%d:Exiting setRESET_CHIP after calling FaultReport with kFaultActionFullCapture"
+ "[dk] %s@%d:This call to setRESET_CHIP will not actually reset the chip nor collect CoreCapture! Forwarding to dbgTriggerWatchdog()"
+ "[dk] %s@%d:This call to setRESET_CHIP will not actually reset the chip nor collect CoreCapture! returning ENODEV, calling message %s"
+ "[dk] %s@%d:This call to setRESET_CHIP will not actually reset the chip! isTrap=%u, isUserspaceReset=%u, calling message %s"
+ "[dk] %s@%d:isTrap=%u, isUserspaceReset=%u, trap reason %u, message: %s"
- "\"AppleBCMWLANV3_driverkit-1475.46\""
- "/AppleInternal/Library/BuildRoots/46a745fc-02fe-11f0-b780-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1475.46"
- "Mar 17 2025 20:06:53"
- "[dk] %s@%d:isTrap=%u, isUserspaceReset=%u, trap reason %u\n"

```
