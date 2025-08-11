## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.8.1.51.0
-  __TEXT.__text: 0x7620c
-  __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0x32bc
-  __TEXT.__const: 0xe58
-  __TEXT.__cstring: 0x8f82
-  __TEXT.__oslogstring: 0x2589
-  __TEXT.__gcc_except_tab: 0xd30
+1.8.1.52.0
+  __TEXT.__text: 0x78830
+  __TEXT.__auth_stubs: 0x1ec0
+  __TEXT.__objc_methlist: 0x32f4
+  __TEXT.__const: 0xe68
+  __TEXT.__cstring: 0x9132
+  __TEXT.__oslogstring: 0x2619
+  __TEXT.__gcc_except_tab: 0xd28
   __TEXT.__swift5_typeref: 0x8da
-  __TEXT.__swift5_capture: 0x348
-  __TEXT.__constg_swiftt: 0x490
+  __TEXT.__swift5_capture: 0x35c
+  __TEXT.__constg_swiftt: 0x498
   __TEXT.__swift5_reflstr: 0x2c4
   __TEXT.__swift5_fieldmd: 0x34c
   __TEXT.__swift5_proto: 0x68

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1598
+  __TEXT.__unwind_info: 0x15c0
   __TEXT.__eh_frame: 0x1810
   __TEXT.__objc_classname: 0x695
-  __TEXT.__objc_methname: 0x8a0e
-  __TEXT.__objc_methtype: 0x8f2
-  __TEXT.__objc_stubs: 0x5f20
-  __DATA_CONST.__got: 0x6e8
-  __DATA_CONST.__const: 0x1898
+  __TEXT.__objc_methname: 0x8ad6
+  __TEXT.__objc_methtype: 0x8d5
+  __TEXT.__objc_stubs: 0x5fa0
+  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__const: 0x18b8
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_selrefs: 0x1fd8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0xf50
-  __AUTH_CONST.__const: 0x1930
-  __AUTH_CONST.__cfstring: 0x6260
-  __AUTH_CONST.__objc_const: 0x6280
+  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH_CONST.__const: 0x19a8
+  __AUTH_CONST.__cfstring: 0x6320
+  __AUTH_CONST.__objc_const: 0x62c0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x620
-  __DATA.__objc_ivar: 0x3dc
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0x580
   __DATA.__bss: 0xd30
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0xfc8
+  __DATA_DIRTY.__objc_data: 0xfd0
   __DATA_DIRTY.__data: 0x460
   __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3955E10-2130-3936-BFCC-9B8437D80D3D
-  Functions: 1946
-  Symbols:   5124
-  CStrings:  3518
+  UUID: A8B82E61-18BF-3E2A-9258-E0C3118CDC5A
+  Functions: 1966
+  Symbols:   5154
+  CStrings:  3543
 
Symbols:
+ -[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]
+ -[FHDatabaseManager dealloc]
+ -[FHDatabaseManager predictRecurringTransactions]
+ -[FHTransaction financeTransactionSharedIdentifier]
+ -[FHTransaction financeTransactionSource]
+ -[FHTransaction setFinanceTransactionSharedIdentifier:]
+ -[FHTransaction setFinanceTransactionSource:]
+ _FHFinanceTransactionSharedIdIndexField
+ _FHFinanceTransactionSharedIdentifierKey
+ _FHFinanceTransactionSourceIndexField
+ _FHFinanceTransactionSourceKey
+ _OBJC_IVAR_$_FHTransaction._financeTransactionSharedIdentifier
+ _OBJC_IVAR_$_FHTransaction._financeTransactionSource
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke.280
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2.284
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_3
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_4
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.351
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.354
+ ___49-[FHDatabaseManager predictRecurringTransactions]_block_invoke
+ ___49-[FHDatabaseManager predictRecurringTransactions]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72r80r88r96r_e23_v16?0"FHTransaction"8ls32l8s40l8r72l8s48l8r80l8s56l8r88l8r96l8s64l8
+ ___block_descriptor_120_e8_32s40s48r56r64r72r80r88r96r104r112r_e17_v16?0"NSArray"8ls32l8s40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSArray"8ls32l8r48l8s40l8
+ ___block_literal_global.373
+ ___block_literal_global.406
+ ___block_literal_global.415
+ ___block_literal_global.518
+ _block_copy_helper.23
+ _block_copy_helper.26
+ _block_descriptor.25
+ _block_descriptor.28
+ _block_destroy_helper.24
+ _block_destroy_helper.27
+ _objc_msgSend$close:
+ _objc_msgSend$financeTransactionSharedIdentifier
+ _objc_msgSend$financeTransactionSource
+ _objc_msgSend$setFinanceTransactionSharedIdentifier:
+ _objc_msgSend$setFinanceTransactionSource:
+ _objectdestroy.39Tm
+ _swift_bridgeObjectRelease_n
- -[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]
- -[FHDatabaseManager predictRecurringTransactionsWithMerchantEntityMemberships:]
- _OBJC_IVAR_$_FHDatabaseManager._finHealthIncomeClassifier
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke.280
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2.284
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_3
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_4
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.352
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.355
- ___79-[FHDatabaseManager predictRecurringTransactionsWithMerchantEntityMemberships:]_block_invoke
- ___79-[FHDatabaseManager predictRecurringTransactionsWithMerchantEntityMemberships:]_block_invoke_2
- ___block_descriptor_112_e8_32s40s48s56s64s72s80r88r96r104r_e23_v16?0"FHTransaction"8ls32l8s40l8r80l8s48l8s56l8r88l8s64l8r96l8r104l8s72l8
- ___block_descriptor_128_e8_32s40s48s56r64r72r80r88r96r104r112r120r_e17_v16?0"NSArray"8ls32l8s40l8r56l8r64l8s48l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8ls32l8r40l8
- ___block_literal_global.374
- ___block_literal_global.404
- ___block_literal_global.413
- ___block_literal_global.519
- _objc_msgSend$populateRecurringClassHistogramsWithMerchantDetailedCategoryCounts:histogram:transaction:
- _objectdestroy.30Tm
CStrings:
+ "(t_tid integer primary key autoincrement, t_identifier text, t_service_identifier text, a_finance_account_id text, t_finance_transaction_id text, t_finance_transaction_shared_id text, t_finance_transaction_source integer, t_payment_hash text, t_source_identifier text, t_amount integer, t_currencycode text, t_timezone integer, t_date integer, t_status integer, t_status_changed_date integer, t_source integer, t_card_type integer, t_type integer, a_type integer, t_altDSID text, t_receipt_identifier text, t_associated_receipt_unique_id text, t_fh_internal_state integer, m_merchant_identifier text, m_industrycode integer, m_name text, m_raw_name text, m_category integer, m_detailed_category text, m_displayname text, m_street text, m_city text, m_state text, m_zip text, m_country_code text, m_country text, m_maps_merchant_id text, m_maps_merchant_result_id integer, m_maps_merchant_brand_id text, m_maps_merchant_brand_result_id integer, lat real, long real, v_accuracy real, h_accuracy real, dispute_type integer, dispute_status integer, peer_pay_counterpart text, peer_pay_type integer, t_description text, processed_description text, peer_pay_is_recurring integer, dispute_open_date integer, dispute_last_updated_date integer, proprietary_bank_transaction_code text, proprietary_bank_transaction_issuer text)"
+ ".t_finance_transaction_shared_id"
+ ".t_finance_transaction_source"
+ "11.11"
+ "Added %ld CNS transactions to group %s"
+ "CNS Transaction %s excluded from group %s due to shared identifier"
+ "Finance Shared Identifier %@ -> %@"
+ "Finance Transaction Source %lu -> %lu"
+ "T@\"NSString\",C,N,V_financeTransactionSharedIdentifier"
+ "TQ,N,V_financeTransactionSource"
+ "_financeTransactionSharedIdentifier"
+ "_financeTransactionSource"
+ "close:"
+ "computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:"
+ "db dealloced, %@"
+ "financeTransactionSharedIdentifier"
+ "financeTransactionSource"
+ "predictRecurringTransactions"
+ "setFinanceTransactionSharedIdentifier:"
+ "setFinanceTransactionSource:"
+ "t_finance_transaction_shared_id"
+ "t_finance_transaction_source"
+ "update transactions set t_service_identifier = %@, t_finance_transaction_id = %@, t_finance_transaction_shared_id = %@, t_finance_transaction_source = %d, a_finance_account_id = %@, t_payment_hash = %@, t_source_identifier = %@, t_amount = %d, t_currencycode = %@, t_timezone = %@, t_date = %d, t_status = %d, t_status_changed_date = %d, t_source = %d, t_card_type = %d, t_type = %d, a_type = %d, t_altDSID = %@, t_receipt_identifier = %@, t_associated_receipt_unique_id = %@, t_fh_internal_state = %d, m_merchant_identifier = %@, m_industrycode = %d, m_name = %@, m_raw_name = %@, m_category = %d, m_detailed_category = %@, m_displayname = %@, m_street = %@, m_city = %@, m_state = %@, m_zip = %@, m_country_code = %@, m_country = %@, m_maps_merchant_id = %@, m_maps_merchant_result_id = %d, m_maps_merchant_brand_id = %@, m_maps_merchant_brand_result_id = %d, lat = %f, long = %f, v_accuracy = %f, h_accuracy = %f, dispute_type = %d, dispute_status = %d, peer_pay_counterpart = %@, peer_pay_type = %d, t_description = %@, processed_description = %@, peer_pay_is_recurring = %d, dispute_open_date = %d, dispute_last_updated_date = %d, proprietary_bank_transaction_code = %@, proprietary_bank_transaction_issuer = %@ where t_identifier == %@"
+ "\xf1"
- "(t_tid integer primary key autoincrement, t_identifier text, t_service_identifier text, a_finance_account_id text, t_finance_transaction_id text, t_payment_hash text, t_source_identifier text, t_amount integer, t_currencycode text, t_timezone integer, t_date integer, t_status integer, t_status_changed_date integer, t_source integer, t_card_type integer, t_type integer, a_type integer, t_altDSID text, t_receipt_identifier text, t_associated_receipt_unique_id text, t_fh_internal_state integer, m_merchant_identifier text, m_industrycode integer, m_name text, m_raw_name text, m_category integer, m_detailed_category text, m_displayname text, m_street text, m_city text, m_state text, m_zip text, m_country_code text, m_country text, m_maps_merchant_id text, m_maps_merchant_result_id integer, m_maps_merchant_brand_id text, m_maps_merchant_brand_result_id integer, lat real, long real, v_accuracy real, h_accuracy real, dispute_type integer, dispute_status integer, peer_pay_counterpart text, peer_pay_type integer, t_description text, processed_description text, peer_pay_is_recurring integer, dispute_open_date integer, dispute_last_updated_date integer, proprietary_bank_transaction_code text, proprietary_bank_transaction_issuer text)"
- "11.10"
- "@\"FinHealthIncomeClassifier\""
- "_finHealthIncomeClassifier"
- "computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:"
- "predictRecurringTransactionsWithMerchantEntityMemberships:"
- "update transactions set t_service_identifier = %@, t_finance_transaction_id = %@, a_finance_account_id = %@, t_payment_hash = %@, t_source_identifier = %@, t_amount = %d, t_currencycode = %@, t_timezone = %@, t_date = %d, t_status = %d, t_status_changed_date = %d, t_source = %d, t_card_type = %d, t_type = %d, a_type = %d, t_altDSID = %@, t_receipt_identifier = %@, t_associated_receipt_unique_id = %@, t_fh_internal_state = %d, m_merchant_identifier = %@, m_industrycode = %d, m_name = %@, m_raw_name = %@, m_category = %d, m_detailed_category = %@, m_displayname = %@, m_street = %@, m_city = %@, m_state = %@, m_zip = %@, m_country_code = %@, m_country = %@, m_maps_merchant_id = %@, m_maps_merchant_result_id = %d, m_maps_merchant_brand_id = %@, m_maps_merchant_brand_result_id = %d, lat = %f, long = %f, v_accuracy = %f, h_accuracy = %f, dispute_type = %d, dispute_status = %d, peer_pay_counterpart = %@, peer_pay_type = %d, t_description = %@, processed_description = %@, peer_pay_is_recurring = %d, dispute_open_date = %d, dispute_last_updated_date = %d, proprietary_bank_transaction_code = %@, proprietary_bank_transaction_issuer = %@ where t_identifier == %@"

```
