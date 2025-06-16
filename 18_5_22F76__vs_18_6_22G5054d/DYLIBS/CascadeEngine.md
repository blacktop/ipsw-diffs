## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-166.23.1.0.0
-  __TEXT.__text: 0x1ba50
-  __TEXT.__auth_stubs: 0x6f0
+166.28.0.0.0
+  __TEXT.__text: 0x1b7b4
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_methlist: 0x1604
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x5dc
-  __TEXT.__cstring: 0xc6d
-  __TEXT.__oslogstring: 0x3428
+  __TEXT.__gcc_except_tab: 0x5e0
+  __TEXT.__cstring: 0xe58
+  __TEXT.__oslogstring: 0x320d
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__unwind_info: 0x748
   __TEXT.__objc_classname: 0x46d
-  __TEXT.__objc_methname: 0x4a19
-  __TEXT.__objc_methtype: 0x10a7
-  __TEXT.__objc_stubs: 0x3de0
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x9c8
+  __TEXT.__objc_methname: 0x4a4f
+  __TEXT.__objc_methtype: 0x10b3
+  __TEXT.__objc_stubs: 0x3e40
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xa40
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11d0
+  __DATA_CONST.__objc_selrefs: 0x11e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xa40
+  __AUTH_CONST.__cfstring: 0xc60
   __AUTH_CONST.__objc_const: 0x3090
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5BA0025-32C1-37B3-99AB-84CC12A6C26F
-  Functions: 632
-  Symbols:   2555
-  CStrings:  1401
+  UUID: 5C0858E2-7B5A-3EBF-B9B0-079030788EB3
+  Functions: 633
+  Symbols:   2573
+  CStrings:  1431
 
Symbols:
+ +[CCRapportFileTransferManager defaultInstance:]
+ +[CCRapportFileTransferManager defaultInstance:].cold.1
+ -[CCRapportSyncEngine initWithQueue:].cold.1
+ _CCRapportSyncError
+ _CCRapportSyncErrorDescription
+ _CCRapportSyncErrorDomain
+ _CCRapportSyncErrorWithDetails
+ _CCRapportSyncErrorWithUnderlying
+ _NSUnderlyingErrorKey
+ _RPOptionSenderFileTransferTargetID
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.154
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.cold.3
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.167
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.3
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.4
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.5
+ ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.168
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke_2.130
+ ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8s64l8
+ _objc_msgSend$defaultInstance:
+ _objc_msgSend$fileTransferTargetID
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$stringByAppendingFormat:
- +[CCRapportFileTransferManager defaultInstance]
- +[CCRapportFileTransferManager defaultInstance].cold.1
- +[CCRapportFileTransferManager defaultInstance].cold.2
- +[CCRapportFileTransferManager defaultInstance].cold.3
- _CCRapportErrorDomain
- _NSTemporaryDirectory
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.158
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.165
- ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.166
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.130
- ___block_descriptor_48_e8_32s40w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8s72l8
- _objc_msgSend$fileURLWithPathComponents:
CStrings:
+ " | %@"
+ "%@ cannot be initialized. %@ failed to be initialized: %@"
+ "%@: %@"
+ "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@, trying alternate identifier %@"
+ "%@: could not find device to reciprocate with alternate identifier %@"
+ "%@: discovered syncable set %@ for platform %@"
+ "%@: initiated file transfer session for set %@ with device %@ fileTransferSession %@"
+ "%@: initiating file transfer session for set %@ with device %@"
+ "%@: received fetch mergeable deltas request for set: %@ %@ %@"
+ "%@: sending fetchMergeableDeltas for set: %@ to device %@"
+ "@24@0:8^@16"
+ "Already syncing"
+ "Asked to defer"
+ "CCRapportManager: all known devices %@"
+ "CCRapportSyncErrorDomain"
+ "Cannot access database"
+ "Cannot access file transfer directory"
+ "Device lost"
+ "Failed to setup sync engine, returning from notification handler"
+ "Invalid parameter"
+ "Invalid state"
+ "Max request depth hit"
+ "Protocol version mismatch"
+ "Rapport discovery Timeout"
+ "Rapport sender model not supported"
+ "Request timed out because no devices are nearby or devices failed to respond in time"
+ "Requested set does not exist"
+ "Sync prohibited by policy defined in set configuration"
+ "Temporarily unavailable"
+ "Unknown (%@)"
+ "defaultInstance:"
+ "fileTransferTargetID"
+ "mismatched protocol version %lu, expected %d"
+ "setObject:forKey:"
+ "stringByAppendingFormat:"
+ "while handling fetchMergeableDeltas for set %@"
- "%@: Failed access database while handling fetch mergeable deltas request for set: %@ error: %@"
- "%@: beginning to fetch deltas for set %@ from device %@"
- "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@"
- "%@: could not find device to reciprocate with fallback identifier %@"
- "%@: discovered synable set %@ for platform %@"
- "%@: done fetching deltas for set %@ from device %@"
- "%@: initiated file transfer session with device %@ fileTransferSession %@"
- "%@: initiating file transfer session with device %@"
- "%@: mismatched protocol version %lu, expected %d"
- "%@: received fetch mergeable deltas request %@ %@"
- "%@: request timed out because no devices are nearby"
- "%@: request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
- "%@: sending request for set: %@ to device %@"
- "%@: set does not exist on device %@"
- "%@: syncing to platform %@ is not supported from this device"
- "%@: unable to determine sender model info: %@"
- "CCRapportErrorDomain"
- "CCRapportFileTransferManager could not get access to sync directory %@"
- "CCRapportFileTransferManager: created directory at path %@ with error %@"
- "CCRapportFileTransferManager: failed to create file transfer directory %@ with error %@"
- "CloudKitDistributedSync"
- "Unable to determine sender model info"
- "fileURLWithPathComponents:"

```
