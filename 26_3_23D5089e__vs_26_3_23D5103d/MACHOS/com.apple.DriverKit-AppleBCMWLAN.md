## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1538.2.0.0.0
-  __TEXT.__text: 0x2b7698
+1538.3.0.0.0
+  __TEXT.__text: 0x2b76e0
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x80454
+  __TEXT.__cstring: 0x80490
   __TEXT.__const: 0x7ea10
   __TEXT.__oslogstring: 0x1f3b
   __TEXT.__unwind_info: 0x5ea0

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: CF053AFF-23AD-3A25-895D-734377730E0B
-  Functions: 13172
-  Symbols:   16397
-  CStrings:  12910
+  UUID: 30609E9B-5FEA-3346-A602-52B465F4C371
+  Functions: 13173
+  Symbols:   16398
+  CStrings:  12911
 
Symbols:
+ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.17
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2286
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2286.cold.1
+ __block_descriptor_tmp.1986
+ __block_descriptor_tmp.2284
+ __block_descriptor_tmp.2288
+ __block_descriptor_tmp.2306
+ __block_descriptor_tmp.2340
+ __block_descriptor_tmp.2667
+ __block_descriptor_tmp.2703
+ __block_descriptor_tmp.3168
+ __block_descriptor_tmp.3251
+ __block_descriptor_tmp.3269
+ __block_descriptor_tmp.3272
+ __block_descriptor_tmp.3278
+ __block_descriptor_tmp.3316
+ __block_literal_global.2308
+ __block_literal_global.2342
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2284
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2284.cold.1
- __block_descriptor_tmp.1984
- __block_descriptor_tmp.2282
- __block_descriptor_tmp.2286
- __block_descriptor_tmp.2304
- __block_descriptor_tmp.2338
- __block_descriptor_tmp.2665
- __block_descriptor_tmp.2701
- __block_descriptor_tmp.3166
- __block_descriptor_tmp.3249
- __block_descriptor_tmp.3265
- __block_descriptor_tmp.3270
- __block_descriptor_tmp.3276
- __block_descriptor_tmp.3314
- __block_literal_global.2306
- __block_literal_global.2340
Functions:
~ __ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData : 5808 -> 5776
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.6 : 96 -> 104
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.7 : 88 -> 96
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.12 : 244 -> 88
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.13 : 100 -> 244
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.14 : 244 -> 100
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.15 : 96 -> 244
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.16 : 100 -> 96
+ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.17
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1538.3\""
+ "/AppleInternal/Library/BuildRoots/4~CGCzugA90H9cvfDVkZw699CQDUHGXNuZ54t8XUA/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1538.3"
+ "Jan  4 2026 19:32:19"
+ "[dk] %s@%d:aggrDistLen %d exceeds buffer size %lu, capping\n"
- "\"AppleBCMWLANV3_driverkit-1538.2\""
- "/AppleInternal/Library/BuildRoots/4~CD29ugA2URBl6tLneftoXwpNw3kZZED6afqygmo/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1538.2"
- "Dec  5 2025 23:31:25"

```
