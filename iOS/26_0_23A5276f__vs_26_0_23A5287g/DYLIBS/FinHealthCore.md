## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.8.1.45.0
-  __TEXT.__text: 0x692f8
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_methlist: 0x31ec
-  __TEXT.__const: 0xdc8
-  __TEXT.__cstring: 0x8c92
-  __TEXT.__oslogstring: 0x2159
-  __TEXT.__gcc_except_tab: 0xc00
-  __TEXT.__swift5_typeref: 0x874
-  __TEXT.__swift5_capture: 0x334
-  __TEXT.__constg_swiftt: 0x460
+1.8.1.46.0
+  __TEXT.__text: 0x6c39c
+  __TEXT.__auth_stubs: 0x1d80
+  __TEXT.__objc_methlist: 0x3234
+  __TEXT.__const: 0xde8
+  __TEXT.__cstring: 0x8d22
+  __TEXT.__oslogstring: 0x2379
+  __TEXT.__gcc_except_tab: 0xc7c
+  __TEXT.__swift5_typeref: 0x85e
+  __TEXT.__swift5_capture: 0x348
+  __TEXT.__constg_swiftt: 0x488
   __TEXT.__swift5_reflstr: 0x2a4
   __TEXT.__swift5_fieldmd: 0x340
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x4c
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x13f8
-  __TEXT.__eh_frame: 0x11c0
+  __TEXT.__unwind_info: 0x1480
+  __TEXT.__eh_frame: 0x13c8
   __TEXT.__objc_classname: 0x694
-  __TEXT.__objc_methname: 0x8717
+  __TEXT.__objc_methname: 0x87f0
   __TEXT.__objc_methtype: 0x8f2
-  __TEXT.__objc_stubs: 0x5da0
-  __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x1810
+  __TEXT.__objc_stubs: 0x5e60
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x1858
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f18
+  __DATA_CONST.__objc_selrefs: 0x1f48
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0xea8
-  __AUTH_CONST.__const: 0x1800
-  __AUTH_CONST.__cfstring: 0x5f40
-  __AUTH_CONST.__objc_const: 0x6188
+  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH_CONST.__const: 0x1848
+  __AUTH_CONST.__cfstring: 0x5fc0
+  __AUTH_CONST.__objc_const: 0x61c8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x670
-  __DATA.__objc_ivar: 0x3cc
-  __DATA.__data: 0x550
+  __DATA.__objc_ivar: 0x3d0
+  __DATA.__data: 0x540
   __DATA.__bss: 0xd70
   __DATA.__common: 0x9
-  __DATA_DIRTY.__objc_data: 0xf40
+  __DATA_DIRTY.__objc_data: 0xf68
   __DATA_DIRTY.__data: 0x448
   __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5AA0F290-306D-374D-81D1-AB336E53E656
-  Functions: 1861
-  Symbols:   5042
-  CStrings:  3416
+  UUID: 9F49F6FB-12B2-3CB0-B9D4-78B29B089DF8
+  Functions: 1891
+  Symbols:   5073
+  CStrings:  3448
 
Symbols:
+ +[FHTransactionGroup _updateStateForTransactionsWithIds:]
+ +[FHTransactionGroup deleteInsightsForGroupIds:]
+ +[FHTransactionGroup deleteOutdatedEntityGroupsAndInsights]
+ -[FHDatabaseManager updateStateForTransaction:newState:]
+ -[FinHealthBankConnectController setUpdateInProgress:]
+ -[FinHealthBankConnectController updateInProgress]
+ GCC_except_table103
+ GCC_except_table110
+ GCC_except_table118
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table180
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table31
+ GCC_except_table4
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table97
+ _OBJC_IVAR_$_FinHealthBankConnectController._updateInProgress
+ __OBJC_$_INSTANCE_VARIABLES_FinHealthBankConnectController
+ __OBJC_$_PROP_LIST_FinHealthBankConnectController
+ ___48+[FHTransactionGroup deleteInsightsForGroupIds:]_block_invoke
+ ___48+[FHTransactionGroup deleteInsightsForGroupIds:]_block_invoke.142
+ ___59+[FHTransactionGroup deleteOutdatedEntityGroupsAndInsights]_block_invoke
+ ___59+[FHTransactionGroup deleteOutdatedEntityGroupsAndInsights]_block_invoke_2
+ ___block_descriptor_32_e37_v16?0"FHDatabaseJoinClauseBuilder"8l
+ ___block_descriptor_48_e8_32r40r_e32_v28?0"NSArray"8"NSArray"16B24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ _block_copy_helper.11
+ _block_copy_helper.17
+ _block_copy_helper.22
+ _block_descriptor.13
+ _block_descriptor.19
+ _block_descriptor.24
+ _block_destroy_helper.12
+ _block_destroy_helper.18
+ _block_destroy_helper.23
+ _objc_msgSend$_updateStateForTransactionsWithIds:
+ _objc_msgSend$addKeyPairsWithJoinType:leftEntity:rightEntity:joinKey:
+ _objc_msgSend$deleteInsightsForGroupIds:
+ _objc_msgSend$initWithEntity:joinClause:
+ _objc_msgSend$setUpdateInProgress:
+ _objc_msgSend$updateStateForTransaction:newState:
+ _objc_msgSend$updateTransactionInternalStateByTransaction:newInternalState:
+ _objectdestroy.30Tm
+ _objectdestroy.49Tm
- GCC_except_table102
- GCC_except_table109
- GCC_except_table117
- GCC_except_table149
- GCC_except_table151
- GCC_except_table157
- GCC_except_table159
- GCC_except_table161
- GCC_except_table163
- GCC_except_table169
- GCC_except_table175
- GCC_except_table177
- GCC_except_table179
- GCC_except_table190
- GCC_except_table196
- GCC_except_table201
- GCC_except_table203
- GCC_except_table30
- GCC_except_table45
- GCC_except_table56
- GCC_except_table59
- GCC_except_table63
- GCC_except_table96
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- _block_copy_helper.10
- _block_copy_helper.20
- _block_copy_helper.31
- _block_copy_helper.37
- _block_descriptor.12
- _block_descriptor.22
- _block_descriptor.33
- _block_descriptor.39
- _block_destroy_helper.11
- _block_destroy_helper.21
- _block_destroy_helper.32
- _block_destroy_helper.38
- _objc_msgSend$updateTransactionWholeRaw:
- _objectdestroy.28Tm
- _objectdestroy.44Tm
- _symbolic SS_Sit
- _symbolic _____ySS_SitG s23_ContiguousArrayStorageC
CStrings:
+ "    SELECT         txns.t_identifier, txns.t_description, txns.t_date, txns.t_amount, txns.a_type, txns.proprietary_bank_transaction_issuer, txns.proprietary_bank_transaction_code, accs.account_category, txns.t_type, txns.t_currencycode, fts.rank     FROM         fts_transactions fts         INNER JOIN transactions txns ON fts.t_identifier = txns.t_identifier         LEFT JOIN fh_account_information accs ON txns.t_source_identifier = accs.source_identifier     WHERE         fts_transactions match '^\"%@\"'         AND fts.a_type == %d     UNION     SELECT         txns.t_identifier, txns.t_description, txns.t_date, txns.t_amount, txns.a_type, txns.proprietary_bank_transaction_issuer, txns.proprietary_bank_transaction_code, accs.account_category, txns.t_type, txns.t_currencycode, fts.rank     FROM         fts_transactions fts         INNER JOIN transactions txns ON fts.t_identifier = txns.t_identifier         LEFT JOIN fh_account_information accs ON txns.t_source_identifier = accs.source_identifier     WHERE         fts_transactions match '%@' AND rank < %f         AND fts.a_type == %d     ORDER BY txns.t_date ASC;"
+ "%@.group_id"
+ "%@.t_fh_internal_state"
+ "%@.t_identifier"
+ "%s Group: groupId %@ transactionId %@ similarityScore %@ GroupMethod %lu"
+ "-[FHDatabaseManager computeAndPersistTransactionGroupings]_block_invoke"
+ "All Income Insights Deleted"
+ "Deleted outdated entity groups and insights"
+ "Deleting outdated groups: %@"
+ "Entity Group Deleted: %s"
+ "Error creating three comma regex: %@"
+ "Error creating two comma regex: %@"
+ "Error: %@ when deleting entity group: %s"
+ "Error: %@ when deleting income insight: %s"
+ "Error: %@ when deleting income insights"
+ "Failed to delete group: %@ from FinHealthDB"
+ "Failed to delete real time predictions associated with group: %@ from FinHealthDB"
+ "Group: %@ deleted from FinHealthDB"
+ "Income Insight Deleted: %s"
+ "Real time predictions (if exist) for group: %@ deleted from FinHealthDB"
+ "Recomputing group %@ -- Transaction %@ was deleted"
+ "Recomputing group %@ -- Transaction %@ was updated"
+ "RequiresRecomputation"
+ "TB,N,V_updateInProgress"
+ "Updating BC transaction %@"
+ "_updateInProgress"
+ "_updateStateForTransactionsWithIds:"
+ "deleteInsightsForGroupIds:"
+ "deleteOutdatedEntityGroupsAndInsights"
+ "setUpdateInProgress:"
+ "update transactions set t_fh_internal_state = %d where t_identifier == '%@'"
+ "updateInProgress"
+ "updateStateForTransaction:newState:"
- "    SELECT         txns.t_identifier, txns.t_description, txns.t_date, txns.t_amount, txns.a_type, txns.proprietary_bank_transaction_issuer, txns.proprietary_bank_transaction_code, accs.account_category, txns.t_type, txns.t_currencycode, fts.rank     FROM         fts_transactions fts         INNER JOIN transactions txns ON fts.t_identifier = txns.t_identifier         LEFT JOIN fh_account_information accs ON txns.t_source_identifier = accs.source_identifier     WHERE         fts_transactions match '\"%@\"'         AND fts.a_type == %d     UNION     SELECT         txns.t_identifier, txns.t_description, txns.t_date, txns.t_amount, txns.a_type, txns.proprietary_bank_transaction_issuer, txns.proprietary_bank_transaction_code, accs.account_category, txns.t_type, txns.t_currencycode, fts.rank     FROM         fts_transactions fts         INNER JOIN transactions txns ON fts.t_identifier = txns.t_identifier         LEFT JOIN fh_account_information accs ON txns.t_source_identifier = accs.source_identifier     WHERE         fts_transactions match '%@' AND rank < %f         AND fts.a_type == %d     ORDER BY txns.t_date ASC;"
- "Group: groupId %@ transactionId %@ similarityScore %@ GroupMethod %lu"
- "Updating bankConnect transaction %@ from FinanceKit source"
- "Updating financeTransactionIdentifier %@ and financeAccountIdentifier %@ for Card/Cash transaction service identifier %@ from FinanceKit source"
- "update transactions set t_fh_internal_state = %d where t_identifier == %@"

```
