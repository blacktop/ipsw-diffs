## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-422.2.1.1.0
+423.5.0.0.0
   __TEXT.__text: 0x1bc2c
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x1908

   __TEXT.__gcc_except_tab: 0x230
   __TEXT.__unwind_info: 0x660
   __TEXT.__objc_classname: 0x56a
-  __TEXT.__objc_methname: 0x41cf
+  __TEXT.__objc_methname: 0x41eb
   __TEXT.__objc_methtype: 0x1023
   __TEXT.__objc_stubs: 0x2e40
   __DATA_CONST.__got: 0x30

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5d70
   __DATA_CONST.__objc_selrefs: 0xe60
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x118
+  __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__objc_const: 0x1000
   __AUTH_CONST.__cfstring: 0x3480
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__auth_got: 0x240
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x118
-  __DATA.__objc_superrefs: 0xe0
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x920
   __DATA.__bss: 0xd0

   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5116A0B9-3F6D-347A-B430-BE08E5FCD6DF
+  UUID: 797A80E7-F86F-3354-A7E7-104187C8FA57
   Functions: 807
   Symbols:   3292
-  CStrings:  2055
+  CStrings:  2057
 
Symbols:
+ ___46-[FMDFMIPManager pairingCheckWith:completion:]_block_invoke.166
+ ___47-[FMDFMIPManager fetchAccessoryConfigurations:]_block_invoke.158
+ ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.179
+ ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.179.cold.1
+ ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.178
+ ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.178.cold.1
+ ___51-[FMDFMIPManager updatePairingLockInfo:completion:]_block_invoke.165
+ ___54-[FMDFMIPManager _forceFMWUpgradeAlertWithCompletion:]_block_invoke.171
+ ___54-[FMDFMIPManager getConnectedAccessoriesDiscoveryIds:]_block_invoke.161
+ ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.168
+ ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.168.cold.1
+ ___58-[FMDFMIPManager registerDeviceForPairingLock:completion:]_block_invoke.163
+ ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.172
+ ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.172.cold.1
+ ___60-[FMDFMIPManager removeAccessoryWithDiscoveryId:completion:]_block_invoke.159
+ ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.176
+ ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.176.cold.1
+ ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.173
+ ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.173.cold.1
+ ___71-[FMDFMIPManager setPhoneNumber:toAccessoryWithDiscoveryId:completion:]_block_invoke.160
+ ___73-[FMDFMIPManager _initiateLostModeExitAuthForIDSDeviceID:withCompletion:]_block_invoke.175
+ ___block_literal_global.153
+ ___block_literal_global.157
+ ___block_literal_global.170
- ___46-[FMDFMIPManager pairingCheckWith:completion:]_block_invoke.164
- ___47-[FMDFMIPManager fetchAccessoryConfigurations:]_block_invoke.156
- ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.177
- ___49-[FMDFMIPManager stopSoundMessageWithCompletion:]_block_invoke.177.cold.1
- ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.176
- ___50-[FMDFMIPManager playSoundWithMessage:completion:]_block_invoke.176.cold.1
- ___51-[FMDFMIPManager updatePairingLockInfo:completion:]_block_invoke.163
- ___54-[FMDFMIPManager _forceFMWUpgradeAlertWithCompletion:]_block_invoke.169
- ___54-[FMDFMIPManager getConnectedAccessoriesDiscoveryIds:]_block_invoke.159
- ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.166
- ___55-[FMDFMIPManager _getAccessoriesWithFilter:completion:]_block_invoke.166.cold.1
- ___58-[FMDFMIPManager registerDeviceForPairingLock:completion:]_block_invoke.161
- ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.170
- ___60-[FMDFMIPManager _updateManagedLostModeWithInfo:completion:]_block_invoke.170.cold.1
- ___60-[FMDFMIPManager removeAccessoryWithDiscoveryId:completion:]_block_invoke.157
- ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.174
- ___62-[FMDFMIPManager _disableFMIPUsingToken:inContext:completion:]_block_invoke.174.cold.1
- ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.171
- ___67-[FMDFMIPManager _updateNeedsLocateAckLostModeWithInfo:completion:]_block_invoke.171.cold.1
- ___71-[FMDFMIPManager setPhoneNumber:toAccessoryWithDiscoveryId:completion:]_block_invoke.158
- ___73-[FMDFMIPManager _initiateLostModeExitAuthForIDSDeviceID:withCompletion:]_block_invoke.173
- ___block_literal_global.151
- ___block_literal_global.155
- ___block_literal_global.168
- ___block_literal_global.79
CStrings:
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N"

```
