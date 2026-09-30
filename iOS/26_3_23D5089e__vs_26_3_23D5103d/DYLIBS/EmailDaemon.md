## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.400.1.0.0
-  __TEXT.__text: 0x269c4c
+3864.400.12.0.0
+  __TEXT.__text: 0x269e60
   __TEXT.__auth_stubs: 0x2700
-  __TEXT.__objc_methlist: 0x12f84
+  __TEXT.__objc_methlist: 0x12f9c
   __TEXT.__const: 0x37bc
-  __TEXT.__gcc_except_tab: 0x4e7a8
-  __TEXT.__cstring: 0x2704a
-  __TEXT.__oslogstring: 0x1a264
+  __TEXT.__gcc_except_tab: 0x4e808
+  __TEXT.__cstring: 0x2714a
+  __TEXT.__oslogstring: 0x1a2d4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0xb4c

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x10808
+  __TEXT.__unwind_info: 0x10820
   __TEXT.__eh_frame: 0xe70
-  __TEXT.__objc_classname: 0x2bfe
-  __TEXT.__objc_methname: 0x37532
+  __TEXT.__objc_classname: 0x2c24
+  __TEXT.__objc_methname: 0x37543
   __TEXT.__objc_methtype: 0x77ec
   __TEXT.__objc_stubs: 0x24d20
   __DATA_CONST.__got: 0x1ba8
   __DATA_CONST.__const: 0x9340
-  __DATA_CONST.__objc_classlist: 0x930
+  __DATA_CONST.__objc_classlist: 0x938
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x1390
   __AUTH_CONST.__const: 0x5d48
-  __AUTH_CONST.__cfstring: 0x101a0
-  __AUTH_CONST.__objc_const: 0x214c0
+  __AUTH_CONST.__cfstring: 0x101e0
+  __AUTH_CONST.__objc_const: 0x215b0
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xf60
+  __AUTH.__objc_data: 0xfb0
   __AUTH.__data: 0x528
   __DATA.__objc_ivar: 0x1460
   __DATA.__data: 0x3760

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 20FFAA0D-088C-3C01-BC54-9F6D42EBE3E7
-  Functions: 10690
-  Symbols:   34374
-  CStrings:  16294
+  UUID: 5F1BC108-E163-3897-A2F6-9DE373867F6D
+  Functions: 10689
+  Symbols:   34381
+  CStrings:  16300
 
Symbols:
+ +[EDAddMessagesIsUrgentIndexUpgradeStep runWithConnection:error:]
+ _OBJC_CLASS_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ _OBJC_METACLASS_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_$_CLASS_METHODS_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_$_PROP_LIST_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_CLASS_PROTOCOLS_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_CLASS_RO_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_METACLASS_RO_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ ___115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.507
+ ___45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.110
+ ___45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.114
+ ___46-[EDBIMIManager _verifyIndicator:failingOpen:]_block_invoke.135
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.755
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.759
+ ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.636
+ ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.623
+ ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.452
+ ___82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.505
+ ___85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.469
+ ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.742
+ ___block_literal_global.113
+ ___block_literal_global.455
+ ___block_literal_global.526
+ ___block_literal_global.548
+ ___block_literal_global.554
+ ___block_literal_global.570
+ ___block_literal_global.575
+ ___block_literal_global.590
+ ___block_literal_global.619
+ ___block_literal_global.625
+ ___block_literal_global.638
+ ___block_literal_global.686
+ ___block_literal_global.716
+ ___block_literal_global.718
+ ___block_literal_global.724
+ ___block_literal_global.737
+ ___block_literal_global.741
+ ___block_literal_global.745
+ ___block_literal_global.754
+ ___block_literal_global.758
+ ___block_literal_global.765
+ _objc_msgSend$operationQueueSchedulerWithMaxConcurrentOperationCount:qualityOfService:
- -[EDCachingMailboxPredictor predictMailboxIDsForMessages:limit:].cold.1
- -[EDCachingMailboxPredictor predictMailboxIDsForMessages:limit:].cold.2
- ___115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.504
- ___45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.109
- ___45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.113
- ___46-[EDBIMIManager _verifyIndicator:failingOpen:]_block_invoke.134
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.752
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.756
- ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.633
- ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.620
- ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.449
- ___82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.502
- ___85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.466
- ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.739
- ___block_literal_global.112
- ___block_literal_global.452
- ___block_literal_global.520
- ___block_literal_global.545
- ___block_literal_global.551
- ___block_literal_global.567
- ___block_literal_global.569
- ___block_literal_global.581
- ___block_literal_global.616
- ___block_literal_global.622
- ___block_literal_global.635
- ___block_literal_global.683
- ___block_literal_global.713
- ___block_literal_global.715
- ___block_literal_global.721
- ___block_literal_global.723
- ___block_literal_global.731
- ___block_literal_global.738
- ___block_literal_global.742
- ___block_literal_global.748
- ___block_literal_global.755
- ___block_literal_global.762
- _objc_msgSend$operationQueueSchedulerWithMaxConcurrentOperationCount:
CStrings:
+ "CREATE INDEX IF NOT EXISTS messages_is_urgent_deleted_conversation_id_is_urgent_1_deleted_0_index ON messages(is_urgent, deleted, conversation_id) WHERE (is_urgent = 1 AND deleted = 0)"
+ "Cache hit for %{public}@"
+ "Cache miss for %{public}@"
+ "EDAddMessagesIsUrgentIndexUpgradeStep"
+ "Not downloading indicators or mark certificates because remote content is not allowed."
+ "messages_is_urgent_deleted_conversation_id_is_urgent_1_deleted_0_index"
+ "operationQueueSchedulerWithMaxConcurrentOperationCount:qualityOfService:"
- "Cache hit for %@"
- "Cache miss for %@"
- "operationQueueSchedulerWithMaxConcurrentOperationCount:"

```
