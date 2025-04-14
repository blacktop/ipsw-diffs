## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1485.1.0.0.0
-  __TEXT.__text: 0x2b0e20
+1485.3.0.0.0
+  __TEXT.__text: 0x2b113c
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7e76a
+  __TEXT.__cstring: 0x7e80f
   __TEXT.__const: 0x7e320
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5d70
+  __TEXT.__unwind_info: 0x5d78
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1270
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 13069
-  Symbols:   16282
-  CStrings:  12696
+  Functions: 13075
+  Symbols:   16287
+  CStrings:  12700
 
Symbols:
+ _ZN28AppleBCMWLANBusInterfacePCIe17prepareFRCallbackEPK13CCFaultReport.cold.4
+ _ZN28AppleBCMWLANBusInterfacePCIe21createFirmwarePCIeIPCEP22AppleBCMWLANChipMemory.cold.23
+ _ZNK28AppleBCMWLANBusInterfacePCIe21checkAPBAccessibilityEbb.cold.2
+ __ZN22AppleBCMWLANChipMemory10readFlags3Ev
+ __ZN27AppleBCMWLANChipManagerPCIe19setDARUpdateAllowedEb
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1173
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.702
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.702.cold.1
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.702.cold.2
+ __block_descriptor_tmp.1169
+ __block_descriptor_tmp.1176
+ __block_descriptor_tmp.1178
+ __block_descriptor_tmp.1179
+ __block_descriptor_tmp.547
+ __block_descriptor_tmp.590
+ __block_descriptor_tmp.597
+ __block_descriptor_tmp.700
+ __block_descriptor_tmp.705
+ __block_descriptor_tmp.719
+ __block_descriptor_tmp.724
+ __block_descriptor_tmp.731
+ __block_descriptor_tmp.734
+ __block_descriptor_tmp.735
+ __block_descriptor_tmp.745
+ __block_descriptor_tmp.853
+ __block_descriptor_tmp.854
+ __block_descriptor_tmp.863
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1169
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.700
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.700.cold.1
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.700.cold.2
- __block_descriptor_tmp.1165
- __block_descriptor_tmp.1172
- __block_descriptor_tmp.1174
- __block_descriptor_tmp.1175
- __block_descriptor_tmp.545
- __block_descriptor_tmp.588
- __block_descriptor_tmp.595
- __block_descriptor_tmp.698
- __block_descriptor_tmp.703
- __block_descriptor_tmp.717
- __block_descriptor_tmp.722
- __block_descriptor_tmp.729
- __block_descriptor_tmp.732
- __block_descriptor_tmp.733
- __block_descriptor_tmp.741
- __block_descriptor_tmp.851
- __block_descriptor_tmp.852
- __block_descriptor_tmp.861
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1485.3\""
+ "/AppleInternal/Library/BuildRoots/f265592e-1520-11f0-896f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1485.3"
+ "Apr  9 2025 20:55:22"
+ "[dk] %s@%d:DAR Based trap supported\n"
+ "[dk] %s@%d:Host initiated DAR based trap timed out\n"
+ "[dk] %s@%d:Skip APB accessible check\n"
+ "[dk] %s@%d:deviceSharedFlags3 = 0x%x\n"
- "\"AppleBCMWLANV3_driverkit-1485.1\""
- "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1485.1"
- "Mar 21 2025 21:47:49"

```
