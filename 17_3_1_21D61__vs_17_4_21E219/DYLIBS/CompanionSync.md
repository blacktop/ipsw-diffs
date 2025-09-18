## CompanionSync

> `/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync`

```diff

-267.0.0.0.0
-  __TEXT.__text: 0xa3200
+269.0.0.0.0
+  __TEXT.__text: 0xa32d0
   __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x8164
+  __TEXT.__objc_methlist: 0x817c
   __TEXT.__cstring: 0x747e
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x9502
-  __TEXT.__gcc_except_tab: 0x2b3c
-  __TEXT.__unwind_info: 0x296c
+  __TEXT.__gcc_except_tab: 0x2b4c
+  __TEXT.__unwind_info: 0x297c
   __TEXT.__objc_classname: 0xd5a
-  __TEXT.__objc_methname: 0xcba5
-  __TEXT.__objc_methtype: 0x2951
-  __TEXT.__objc_stubs: 0xa2a0
+  __TEXT.__objc_methname: 0xcc4b
+  __TEXT.__objc_methtype: 0x296f
+  __TEXT.__objc_stubs: 0xa2e0
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x1fb8
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12cc8
-  __DATA_CONST.__objc_selrefs: 0x3260
+  __DATA_CONST.__objc_const: 0x12ce8
+  __DATA_CONST.__objc_selrefs: 0x3270
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x4d8
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__cfstring: 0x3520
   __AUTH_CONST.__objc_const: 0x28a0

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x8a0
   __AUTH.__objc_data: 0x1fe0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x4d8
-  __DATA.__objc_superrefs: 0x360
   __DATA.__objc_ivar: 0xbfc
   __DATA.__data: 0xb68
   __DATA.__bss: 0x130

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: ECF83857-63BB-3C47-A76A-83DFE591CC03
-  Functions: 3945
-  Symbols:   12109
-  CStrings:  4990
+  UUID: 9E99DCDB-1BB7-3BBC-80C0-88BF2C34FF11
+  Functions: 3947
+  Symbols:   12116
+  CStrings:  4998
 
Symbols:
+ -[NMSMessageCenter _handleError:context:locked:]
+ -[NMSPersistentDictionary objectWithOldestExpirationDate:]
+ GCC_except_table36
+ ___29-[NMSMessageCenter sendFile:]_block_invoke.83
+ ___32-[NMSMessageCenter sendRequest:]_block_invoke.78
+ ___34-[NMSMessageCenter _sendResponse:]_block_invoke.87
+ ___35-[SYIncomingFullSyncSession start:]_block_invoke.72
+ ___36-[SYOutgoingBatchSyncSession start:]_block_invoke.88
+ ___38-[SYIncomingTransactionSession start:]_block_invoke.71
+ ___39-[_SYInputStreamer stream:handleEvent:]_block_invoke.175
+ ___41-[SYOutgoingSyncAllObjectsSession start:]_block_invoke.74
+ ___43-[SYOutgoingDeltaTransactionSession start:]_block_invoke.82
+ ___45-[SYOutgoingBatchSyncSession _fetchNextBatch]_block_invoke.75
+ ___48-[NMSMessageCenter _handleError:context:locked:]_block_invoke
+ ___48-[SYOutgoingSyncAllObjectsSession _fetchChanges]_block_invoke.67
+ ___48-[_SYInputStreamer readDataOfLength:completion:]_block_invoke.173
+ ___58-[NMSPersistentDictionary objectWithOldestExpirationDate:]_block_invoke
+ ___60-[_SYInputStreamer initWithCompressedFileURL:callbackQueue:]_block_invoke.171
+ ___70-[SYService(CompanionSyncProtoV1) _v1_handleChangeMessage:completion:]_block_invoke.491
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleBatchSyncStart:completion:]_block_invoke.488
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.485
+ ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke.543
+ ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke.545
+ ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.544
+ ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.544.cold.1
+ ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.544.cold.2
+ ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.544.cold.3
+ ___block_descriptor_48_e8_32r40r_e36_v40?0"NSString"816"NSDate"24^B32lr32l8r40l8
+ ___block_literal_global.222
+ ___block_literal_global.225
+ ___block_literal_global.570
+ ___block_literal_global.782
+ __unnamed_array_storage.619
+ _objc_msgSend$_handleError:context:locked:
+ _objc_msgSend$objectWithOldestExpirationDate:
- ___29-[NMSMessageCenter sendFile:]_block_invoke.84
- ___32-[NMSMessageCenter sendRequest:]_block_invoke.79
- ___34-[NMSMessageCenter _sendResponse:]_block_invoke.88
- ___35-[NMSMessageCenter _expireMessages]_block_invoke
- ___35-[SYIncomingFullSyncSession start:]_block_invoke.70
- ___36-[SYOutgoingBatchSyncSession start:]_block_invoke.87
- ___38-[SYIncomingTransactionSession start:]_block_invoke.70
- ___39-[_SYInputStreamer stream:handleEvent:]_block_invoke.174
- ___41-[NMSMessageCenter _handleError:context:]_block_invoke
- ___41-[SYOutgoingSyncAllObjectsSession start:]_block_invoke.73
- ___43-[SYOutgoingDeltaTransactionSession start:]_block_invoke.81
- ___45-[SYOutgoingBatchSyncSession _fetchNextBatch]_block_invoke.74
- ___48-[SYOutgoingSyncAllObjectsSession _fetchChanges]_block_invoke.66
- ___48-[_SYInputStreamer readDataOfLength:completion:]_block_invoke.171
- ___60-[_SYInputStreamer initWithCompressedFileURL:callbackQueue:]_block_invoke.170
- ___70-[SYService(CompanionSyncProtoV1) _v1_handleChangeMessage:completion:]_block_invoke.490
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleBatchSyncStart:completion:]_block_invoke.487
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.484
- ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke.542
- ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke.544
- ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.543
- ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.543.cold.1
- ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.543.cold.2
- ___73-[SYLegacyStore(BatchedSyncSupport) performBatchedSyncToCurrentDBVersion]_block_invoke_2.543.cold.3
- ___block_descriptor_56_e8_32s40s48s_e36_v40?0"NSString"816"NSDate"24^B32ls32l8s40l8s48l8
- ___block_literal_global.221
- ___block_literal_global.224
- ___block_literal_global.569
- ___block_literal_global.780
- __unnamed_array_storage.618
CStrings:
+ "@24@0:8o^@16"
+ "T@\"NSSet\",?,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSURL\",?,R,C"
+ "_handleError:context:locked:"
+ "accommodatePresentedItemEvictionWithCompletionHandler:"
+ "objectWithOldestExpirationDate:"
+ "v36@0:8@16@24B32"

```
