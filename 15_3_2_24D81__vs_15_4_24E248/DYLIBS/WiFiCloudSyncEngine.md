## WiFiCloudSyncEngine

> `/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/Versions/A/WiFiCloudSyncEngine`

```diff

-775.2.0.0.0
-  __TEXT.__text: 0x104bc
-  __TEXT.__auth_stubs: 0x460
+800.6.0.0.0
+  __TEXT.__text: 0x11558
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x24ec
-  __TEXT.__cstring: 0x14df
-  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__cstring: 0x14f1
+  __TEXT.__unwind_info: 0x1e8
   __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x8af
-  __TEXT.__objc_methtype: 0xf2
+  __TEXT.__objc_methname: 0x8c1
+  __TEXT.__objc_methtype: 0xfe
   __TEXT.__objc_stubs: 0xba0
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x40

   __DATA_CONST.__objc_selrefs: 0x310
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0xc20
   __AUTH_CONST.__objc_const: 0x280
   __AUTH_CONST.__objc_intobj: 0xd8

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88E2F3C3-AB3E-378B-A7DC-CCEB3E254694
-  Functions: 118
-  Symbols:   345
-  CStrings:  557
+  UUID: B573A045-A355-3369-A24C-98B61F8291D8
+  Functions: 267
+  Symbols:   500
+  CStrings:  558
 
Symbols:
+ -[WiFiCloudSyncEngineCore addToKVStore:synchronize:].cold.1
+ -[WiFiCloudSyncEngineCore addToKVStore:synchronize:].cold.2
+ -[WiFiCloudSyncEngineCore addToKVStore:synchronize:].cold.3
+ -[WiFiCloudSyncEngineCore addToKVStore:synchronize:].cold.4
+ -[WiFiCloudSyncEngineCore addToKVStore:synchronize:].cold.5
+ -[WiFiCloudSyncEngineCore pruneKVSStoreAndReply:]
+ -[WiFiCloudSyncEngineCore queryKeychainSyncState].cold.1
+ -[WiFiCloudSyncEngineCore readStoreValueForKey:].cold.1
+ -[WiFiCloudSyncEngineCore removeFromKVStore:].cold.1
+ -[WiFiCloudSyncEngineCore removeFromKVStore:].cold.2
+ -[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworksAndReply:]
+ WiFiCloudSyncEngineAddNetworkToCloud.cold.1
+ WiFiCloudSyncEngineAddNetworkToCloud.cold.2
+ WiFiCloudSyncEngineAddNetworkToCloud.cold.3
+ WiFiCloudSyncEngineCheckKeychainSyncState.cold.1
+ WiFiCloudSyncEngineCreate.cold.1
+ WiFiCloudSyncEngineMergeKnownNetworksToCloud.cold.1
+ WiFiCloudSyncEngineMergeKnownNetworksToCloud.cold.2
+ WiFiCloudSyncEngineMergeKnownNetworksToCloud.cold.3
+ WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS.cold.1
+ WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS.cold.2
+ WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS.cold.3
+ WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS.cold.4
+ WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS.cold.5
+ WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS.cold.6
+ WiFiCloudSyncEngineRegisterCallbacks.cold.1
+ WiFiCloudSyncEngineRegisterCallbacks.cold.10
+ WiFiCloudSyncEngineRegisterCallbacks.cold.2
+ WiFiCloudSyncEngineRegisterCallbacks.cold.3
+ WiFiCloudSyncEngineRegisterCallbacks.cold.4
+ WiFiCloudSyncEngineRegisterCallbacks.cold.5
+ WiFiCloudSyncEngineRegisterCallbacks.cold.6
+ WiFiCloudSyncEngineRegisterCallbacks.cold.7
+ WiFiCloudSyncEngineRegisterCallbacks.cold.8
+ WiFiCloudSyncEngineRegisterCallbacks.cold.9
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.1
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.10
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.2
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.3
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.4
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.5
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.6
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.7
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.8
+ WiFiCloudSyncEngineRegisterCallbacksWithQueue.cold.9
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.1
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.2
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.3
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.4
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.5
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.6
+ WiFiCloudSyncEngineRemoveNetworkFromCloud.cold.7
+ WiFiCloudSyncEngineScheduleWithQueue.cold.1
+ WiFiCloudSyncEngineScheduleWithRunLoop.cold.1
+ WiFiCloudSyncEngineStartEngine.cold.1
+ WiFiCloudSyncEngineStopEngine.cold.1
+ WiFiCloudSyncEngineStopEngine.cold.2
+ WiFiCloudSyncEngineUnScheduleWithQueue.cold.1
+ WiFiCloudSyncEngineUnScheduleWithRunLoop.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __Block_release
+ __WiFiCloudSyncEngineAddVersionsToCloudNetwork.cold.1
+ __WiFiCloudSyncEngineAddVersionsToCloudNetwork.cold.2
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.1
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.2
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.3
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.4
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.5
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.6
+ __WiFiCloudSyncEngineCheckWaitingForPasswordList.cold.7
+ __WiFiCloudSyncEngineCreateCloudFromNetworkFormatCallback.cold.1
+ __WiFiCloudSyncEngineCreateNetworkFromCloudFormatCallback.cold.1
+ __WiFiCloudSyncEngineIsCloudNetworkOnDevice.cold.1
+ __WiFiCloudSyncEngineIsCloudNetworkOnDevice.cold.2
+ __WiFiCloudSyncEngineIsNetworkHidden.cold.1
+ __WiFiCloudSyncEngineIsNetworkHidden.cold.2
+ __WiFiCloudSyncEngineIsNetworkHidden.cold.3
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.1
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.10
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.11
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.12
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.13
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.14
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.15
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.16
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.17
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.2
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.3
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.4
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.5
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.6
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.7
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.8
+ __WiFiCloudSyncEngineIsNetworkSyncableFromCloud.cold.9
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.1
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.10
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.11
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.12
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.13
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.2
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.3
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.4
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.5
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.6
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.7
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.8
+ __WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted.cold.9
+ __WiFiCloudSyncEngineKeychainChangedNotificationCallback.cold.1
+ __WiFiCloudSyncEngineKeychainSyncStateChanged.cold.1
+ __WiFiCloudSyncEngineProcessCloudChangeEvent.cold.1
+ __WiFiCloudSyncEngineProcessCloudNetworkChangeEvent.cold.1
+ __WiFiCloudSyncEngineProcessCloudNetworkChangeEvent.cold.2
+ __WiFiCloudSyncEngineRelease.cold.1
+ __WiFiCloudSyncEngineSetupKeychainChangedNotification.cold.1
+ __WiFiCloudSyncEngineSetupKeychainChangedNotification.cold.2
+ __WiFiCloudSyncEngineSetupKeychainChangedNotification.cold.3
+ __WiFiCloudSyncEngineSetupKeychainSyncStateChangeNotification.cold.1
+ __WiFiCloudSyncEngineSetupKeychainSyncStateChangeNotification.cold.2
+ __WiFiCloudSyncEngineSetupKeychainSyncStateChangeNotification.cold.3
+ __WiFiCloudSyncEngineStartEngine_block_invoke.10
+ __WiFiCloudSyncEngineStopKeychainChangedNotifications.cold.1
+ __WiFiCloudSyncEngineStopKeychainChangedNotifications.cold.2
+ __WiFiCloudSyncEngineStopKeychainChangedNotifications.cold.3
+ __WiFiCloudSyncEngineStopKeychainChangedNotifications.cold.4
+ ___49-[WiFiCloudSyncEngineCore pruneKVSStoreAndReply:]_block_invoke
+ ___49-[WiFiCloudSyncEngineCore pruneKVSStoreAndReply:]_block_invoke_2
+ ___67-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworksAndReply:]_block_invoke
+ ___67-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworksAndReply:]_block_invoke_2
+ ___WiFiCloudSyncEngineStartEngine_block_invoke_3
+ ___block_descriptor_56_e8_32o40o48b_e5_v8?0l
+ ___copy_helper_block_e8_32o40o48b
+ ___destroy_helper_block_e8_32o40o48b
+ _dispatch_block_create
+ _objc_msgSend$pruneKVSStoreAndReply:
+ _objc_msgSend$synchronizeAndCallMergeNetworksAndReply:
- -[WiFiCloudSyncEngineCore pruneKVSStore]
- -[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworks]
- __WiFiCloudSyncEngineStartEngine_block_invoke.5
- ___40-[WiFiCloudSyncEngineCore pruneKVSStore]_block_invoke
- ___58-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworks]_block_invoke
- ___WiFiCloudSyncEngineMigrateToEncryptedKVS
- _objc_msgSend$pruneKVSStore
- _objc_msgSend$synchronizeAndCallMergeNetworks
CStrings:
+ "-[WiFiCloudSyncEngineCore pruneKVSStoreAndReply:]"
+ "-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworksAndReply:]"
+ "21:00:36"
+ "Mar  7 2025"
+ "pruneKVSStoreAndReply:"
+ "synchronizeAndCallMergeNetworksAndReply:"
+ "v24@0:8@?16"
- "-[WiFiCloudSyncEngineCore pruneKVSStore]"
- "-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworks]"
- "23:07:22"
- "Dec 13 2024"
- "pruneKVSStore"
- "synchronizeAndCallMergeNetworks"

```
