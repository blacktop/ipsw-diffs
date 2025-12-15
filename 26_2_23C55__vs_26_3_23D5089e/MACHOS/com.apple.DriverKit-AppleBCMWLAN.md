## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1535.9.0.0.0
-  __TEXT.__text: 0x2b773c
+1538.2.0.0.0
+  __TEXT.__text: 0x2b7698
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x8035f
+  __TEXT.__cstring: 0x80454
   __TEXT.__const: 0x7ea10
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e98
+  __TEXT.__unwind_info: 0x5ea0
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: A123C100-0765-3004-BABF-E5DD7781DDA0
-  Functions: 13171
+  UUID: CF053AFF-23AD-3A25-895D-734377730E0B
+  Functions: 13172
   Symbols:   16397
-  CStrings:  12905
+  CStrings:  12910
 
Symbols:
+ _OUTLINED_FUNCTION_135
+ _OUTLINED_FUNCTION_149
+ _ZN28AppleBCMWLANKeepAliveOffload24setTCPAliveOffloadConfigEhP34IOUserNetworkKeepAliveOffloadFrameP10ether_addrS3_.cold.7
+ _ZN28AppleBCMWLANKeepAliveOffload24setTCPAliveOffloadConfigEhP34IOUserNetworkKeepAliveOffloadFrameP10ether_addrS3_.cold.8
+ __ZN16AppleBCMWLANCore10is4387C3UpEv
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1186
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.709
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.709.cold.1
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.709.cold.2
+ __block_descriptor_tmp.1182
+ __block_descriptor_tmp.1191
+ __block_descriptor_tmp.1192
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
- _OUTLINED_FUNCTION_134
- _OUTLINED_FUNCTION_148
- _OUTLINED_FUNCTION_282
- _ZN28AppleBCMWLANBusInterfacePCIe18createFlowCallbackEit.cold.5
- __ZN16AppleBCMWLANCore8is4388UpEv
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1183
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706.cold.1
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706.cold.2
- __block_descriptor_tmp.1179
- __block_descriptor_tmp.1186
- __block_descriptor_tmp.1188
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
+ "\"AppleBCMWLANV3_driverkit-1538.2\""
+ "/AppleInternal/Library/BuildRoots/4~CD29ugA2URBl6tLneftoXwpNw3kZZED6afqygmo/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1538.2"
+ "Dec  5 2025 23:31:25"
+ "[dk] %s@%d: Router MAC address value = %02x:%02x:%02x:%02x:%02x:%02x\n"
+ "[dk] %s@%d:BSSID is used for router mac address\n"
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
- "/AppleInternal/Library/BuildRoots/4~CCKqugDexe7JGaH8qxhljH2zCEGRc9aD0IoOxSk/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1535.9"
- "Nov 12 2025 20:59:53"
- "[WiFiTimeSync@] Tx UDPv4 message %s sequence %d to %u.%u.%u.%u @ %02x:%02x:%02x:%02x:%02x:%02x Error set ts=-1 if:%d tsEnabled:%d tsRequested:%d tx_status:%d\n"
- "[WiFiTimeSync@] Tx UDPv6 message %s sequence %d to %02x%02x:%02x%02x_%02x%02x:%02x%02x @ %02x:%02x:%02x:%02x:%02x:%02x Error set ts=-1 if:%d tsEnabled:%d tsRequested:%d tx_status:%d\n"
- "[dk] %s@%d:Failed to map FlowID %d to FlowQueue\n"
- "[dk] %s@%d:Failed to unassign FlowId from flowQ - IfId:%d Error:%s\n"
- "kIOReturnError"
- "kIOReturnIOError"

```
