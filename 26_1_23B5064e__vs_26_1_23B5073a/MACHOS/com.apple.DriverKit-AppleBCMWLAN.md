## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1535.9.0.0.0
-  __TEXT.__text: 0x2b77b8
+1535.9.4.1.0
+  __TEXT.__text: 0x2b78c4
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x8035f
-  __TEXT.__const: 0x7ee50
+  __TEXT.__cstring: 0x8053b
+  __TEXT.__const: 0x7ee90
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5ea0
+  __TEXT.__unwind_info: 0x5e98
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: E3A5B34E-9F47-3FE7-BCD4-745C76192DD2
-  Functions: 13170
-  Symbols:   16395
-  CStrings:  12905
+  UUID: 52236D4B-455F-35C8-AE13-6EB6AD83E25E
+  Functions: 13169
+  Symbols:   16394
+  CStrings:  12910
 
Symbols:
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1186
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.709
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.709.cold.1
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.709.cold.2
+ __block_descriptor_tmp.1182
+ __block_descriptor_tmp.1191
+ __block_descriptor_tmp.1192
+ __block_descriptor_tmp.131
+ __block_descriptor_tmp.595
+ __block_descriptor_tmp.602
+ __block_descriptor_tmp.707
+ __block_descriptor_tmp.712
+ __block_descriptor_tmp.726
+ __block_descriptor_tmp.731
+ __block_descriptor_tmp.741
+ __block_descriptor_tmp.742
+ __block_descriptor_tmp.750
+ __block_descriptor_tmp.752
+ __block_descriptor_tmp.860
+ __block_descriptor_tmp.861
+ __block_descriptor_tmp.870
- _ZN28AppleBCMWLANBusInterfacePCIe18createFlowCallbackEit.cold.5
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1183
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706.cold.1
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706.cold.2
- __block_descriptor_tmp.1179
- __block_descriptor_tmp.1186
- __block_descriptor_tmp.1188
- __block_descriptor_tmp.129
- __block_descriptor_tmp.592
- __block_descriptor_tmp.599
- __block_descriptor_tmp.704
- __block_descriptor_tmp.709
- __block_descriptor_tmp.723
- __block_descriptor_tmp.728
- __block_descriptor_tmp.735
- __block_descriptor_tmp.739
- __block_descriptor_tmp.747
- __block_descriptor_tmp.749
- __block_descriptor_tmp.857
- __block_descriptor_tmp.858
- __block_descriptor_tmp.867
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1535.9.4.1\""
+ "/AppleInternal/Library/BuildRoots/4~CAMWugDtCRi38K5WhWC0LsOen0kU0TbTjKiNvpo/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1535.9.4.1"
+ "Oct 16 2025 23:20:53"
+ "[dk] %s@%d:Clearing flowId:%d ac:%d for ifId:%d\n"
+ "[dk] %s@%d:Failed to unassign FlowId:%d from flowQ - ifId:%d ac:%d isLowLatencyRing:%s\n"
+ "[dk] %s@%d:FlowQueue for flowId:%d ac:%d ifId:%d not found in bus's packetQDb!\n"
+ "[dk] %s@%d:Found flowQueue for flowId:%d in AppleBCMWLANBusInterfacePCIe database\n"
+ "[dk] %s@%d:Unable to find flowQueue for flowId:%d in AppleBCMWLANBusInterfacePCIe database\n"
+ "[dk] %s@%d:clearFlowIdInFlowQ failed on ifId:%x (op:%x)  bitmap:%x validation\n"
+ "[dk] %s@%d:clearFlowIdInFlowQ ifId:%d ac:%d flowId:%d\n"
+ "[dk] %s@%d:deleteFlow for flowId:%d as part of eviction in requestFlowId\n"
+ "invalidateFlowId"
- "\"AppleBCMWLANV3_driverkit-1535.9\""
- "/AppleInternal/Library/BuildRoots/4~B_YjugBCCd8LTQZS2DfHML8qs_wyYbULYdnPH9w/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1535.9"
- "Oct  5 2025 22:06:23"
- "[dk] %s@%d:Failed to map FlowID %d to FlowQueue\n"
- "[dk] %s@%d:Failed to unassign FlowId from flowQ - IfId:%d Error:%s\n"
- "kIOReturnError"
- "kIOReturnIOError"

```
