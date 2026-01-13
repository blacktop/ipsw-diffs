## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon`

```diff

-3864.400.1.0.0
-  __TEXT.__text: 0x2ab604
+3864.400.12.0.0
+  __TEXT.__text: 0x2ab864
   __TEXT.__auth_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0x131bc
+  __TEXT.__objc_methlist: 0x131d4
   __TEXT.__const: 0x374c
-  __TEXT.__gcc_except_tab: 0x4f340
-  __TEXT.__cstring: 0x264aa
-  __TEXT.__oslogstring: 0x19fc4
+  __TEXT.__gcc_except_tab: 0x4f3a0
+  __TEXT.__cstring: 0x265aa
+  __TEXT.__oslogstring: 0x1a034
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0xb28

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x109d0
+  __TEXT.__unwind_info: 0x109e0
   __TEXT.__eh_frame: 0xd60
-  __TEXT.__objc_classname: 0x2c42
-  __TEXT.__objc_methname: 0x37ae7
+  __TEXT.__objc_classname: 0x2c68
+  __TEXT.__objc_methname: 0x37af8
   __TEXT.__objc_methtype: 0x795a
   __TEXT.__objc_stubs: 0x25040
   __DATA_CONST.__got: 0x1b78
   __DATA_CONST.__const: 0x1ad8
-  __DATA_CONST.__objc_classlist: 0x940
+  __DATA_CONST.__objc_classlist: 0x948
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x590
   __AUTH_CONST.__auth_got: 0x1280
   __AUTH_CONST.__const: 0xe328
-  __AUTH_CONST.__cfstring: 0xfd60
-  __AUTH_CONST.__objc_const: 0x219b0
+  __AUTH_CONST.__cfstring: 0xfda0
+  __AUTH_CONST.__objc_const: 0x21aa0
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xfb0
+  __AUTH.__objc_data: 0x1000
   __AUTH.__data: 0x528
   __DATA.__objc_ivar: 0x1490
   __DATA.__data: 0x3788

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 38B1D513-161A-39A5-A7EB-B4C6F74F330B
-  Functions: 10789
-  Symbols:   25813
-  CStrings:  16288
+  UUID: 1E1B5AB4-FDBF-3532-93A7-1697362E4776
+  Functions: 10788
+  Symbols:   25821
+  CStrings:  16294
 
Symbols:
+ +[EDAddMessagesIsUrgentIndexUpgradeStep runWithConnection:error:]
+ _OBJC_CLASS_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ _OBJC_METACLASS_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __103-[EDMessagePersistence _predicatesSeparatedByMailboxOrAccountForAndPredicate:containsMailboxPredicate:]_block_invoke.538
+ __115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.510
+ __45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.110
+ __45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.114
+ __46-[EDBIMIManager _verifyIndicator:failingOpen:]_block_invoke.137
+ __46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.811
+ __46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.815
+ __67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.672
+ __67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.679
+ __69-[EDMessagePersistence messageObjectIDsForSearchableItemIdentifiers:]_block_invoke.826
+ __70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.661
+ __75-[EDMessagePersistence messagesForMessageObjectIDs:missedMessageObjectIDs:]_block_invoke.602
+ __75-[EDMessagePersistence messagesForMessageObjectIDs:missedMessageObjectIDs:]_block_invoke.610
+ __75-[EDMessagePersistence messagesForMessageObjectIDs:missedMessageObjectIDs:]_block_invoke.616
+ __75-[EDMessagePersistence persistedMessagesForObjectIDs:requireProtectedData:]_block_invoke.566
+ __76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.451
+ __82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.506
+ __85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.472
+ __89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.794
+ __OBJC_$_CLASS_METHODS_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_$_PROP_LIST_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_CLASS_PROTOCOLS_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_CLASS_RO_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __OBJC_METACLASS_RO_$_EDAddMessagesIsUrgentIndexUpgradeStep
+ __block_literal_global.113
+ __block_literal_global.533
+ __block_literal_global.569
+ __block_literal_global.577
+ __block_literal_global.597
+ __block_literal_global.599
+ __block_literal_global.613
+ __block_literal_global.622
+ __block_literal_global.657
+ __block_literal_global.663
+ __block_literal_global.681
+ __block_literal_global.732
+ __block_literal_global.762
+ __block_literal_global.764
+ __block_literal_global.772
+ __block_literal_global.774
+ __block_literal_global.787
+ __block_literal_global.793
+ __block_literal_global.797
+ __block_literal_global.810
+ __block_literal_global.814
+ __block_literal_global.823
+ _objc_msgSend$operationQueueSchedulerWithMaxConcurrentOperationCount:qualityOfService:
- -[EDCachingMailboxPredictor predictMailboxIDsForMessages:limit:].cold.1
- -[EDCachingMailboxPredictor predictMailboxIDsForMessages:limit:].cold.2
- __103-[EDMessagePersistence _predicatesSeparatedByMailboxOrAccountForAndPredicate:containsMailboxPredicate:]_block_invoke.535
- __115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.507
- __45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.109
- __45-[EDBIMIManager _downloadAndVerifyIndicators]_block_invoke.113
- __46-[EDBIMIManager _verifyIndicator:failingOpen:]_block_invoke.136
- __46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.808
- __46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.812
- __67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.669
- __67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.676
- __69-[EDMessagePersistence messageObjectIDsForSearchableItemIdentifiers:]_block_invoke.823
- __70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.658
- __75-[EDMessagePersistence messagesForMessageObjectIDs:missedMessageObjectIDs:]_block_invoke.599
- __75-[EDMessagePersistence messagesForMessageObjectIDs:missedMessageObjectIDs:]_block_invoke.607
- __75-[EDMessagePersistence messagesForMessageObjectIDs:missedMessageObjectIDs:]_block_invoke.613
- __75-[EDMessagePersistence persistedMessagesForObjectIDs:requireProtectedData:]_block_invoke.563
- __76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.448
- __82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.503
- __85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.469
- __89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.791
- __block_literal_global.451
- __block_literal_global.527
- __block_literal_global.566
- __block_literal_global.574
- __block_literal_global.594
- __block_literal_global.596
- __block_literal_global.610
- __block_literal_global.616
- __block_literal_global.654
- __block_literal_global.660
- __block_literal_global.678
- __block_literal_global.729
- __block_literal_global.759
- __block_literal_global.761
- __block_literal_global.769
- __block_literal_global.771
- __block_literal_global.781
- __block_literal_global.790
- __block_literal_global.794
- __block_literal_global.804
- __block_literal_global.811
- __block_literal_global.820
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
