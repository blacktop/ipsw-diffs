## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.8.1.44.0
-  __TEXT.__text: 0x65e18
-  __TEXT.__auth_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x2fd4
-  __TEXT.__const: 0xde8
-  __TEXT.__cstring: 0x89f2
-  __TEXT.__oslogstring: 0x2059
-  __TEXT.__gcc_except_tab: 0xba8
-  __TEXT.__swift5_typeref: 0x85e
+1.8.1.45.0
+  __TEXT.__text: 0x692f8
+  __TEXT.__auth_stubs: 0x1d30
+  __TEXT.__objc_methlist: 0x31ec
+  __TEXT.__const: 0xdc8
+  __TEXT.__cstring: 0x8c92
+  __TEXT.__oslogstring: 0x2159
+  __TEXT.__gcc_except_tab: 0xc00
+  __TEXT.__swift5_typeref: 0x874
   __TEXT.__swift5_capture: 0x334
-  __TEXT.__constg_swiftt: 0x458
+  __TEXT.__constg_swiftt: 0x460
   __TEXT.__swift5_reflstr: 0x2a4
   __TEXT.__swift5_fieldmd: 0x340
   __TEXT.__swift5_proto: 0x68

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x13b8
-  __TEXT.__eh_frame: 0x11b8
-  __TEXT.__objc_classname: 0x671
-  __TEXT.__objc_methname: 0x7ed4
-  __TEXT.__objc_methtype: 0x8cf
-  __TEXT.__objc_stubs: 0x5b60
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0x17d8
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __TEXT.__unwind_info: 0x13f8
+  __TEXT.__eh_frame: 0x11c0
+  __TEXT.__objc_classname: 0x694
+  __TEXT.__objc_methname: 0x8717
+  __TEXT.__objc_methtype: 0x8f2
+  __TEXT.__objc_stubs: 0x5da0
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0x1810
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d88
+  __DATA_CONST.__objc_selrefs: 0x1f18
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0xe00
-  __AUTH_CONST.__const: 0x17e0
-  __AUTH_CONST.__cfstring: 0x5cc0
-  __AUTH_CONST.__objc_const: 0x5dc8
+  __AUTH_CONST.__auth_got: 0xea8
+  __AUTH_CONST.__const: 0x1800
+  __AUTH_CONST.__cfstring: 0x5f40
+  __AUTH_CONST.__objc_const: 0x6188
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH.__objc_data: 0x620
-  __DATA.__objc_ivar: 0x388
-  __DATA.__data: 0x540
-  __DATA.__bss: 0xd30
+  __AUTH.__objc_data: 0x670
+  __DATA.__objc_ivar: 0x3cc
+  __DATA.__data: 0x550
+  __DATA.__bss: 0xd70
   __DATA.__common: 0x9
-  __DATA_DIRTY.__objc_data: 0xf38
+  __DATA_DIRTY.__objc_data: 0xf40
   __DATA_DIRTY.__data: 0x448
   __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CFE9045-7B04-37B1-8106-BDC27643211F
-  Functions: 1804
-  Symbols:   4891
-  CStrings:  3279
+  UUID: 5AA0F290-306D-374D-81D1-AB336E53E656
+  Functions: 1861
+  Symbols:   5042
+  CStrings:  3416
 
Symbols:
+ -[FHBankConnectDescriptionCleaner .cxx_destruct]
+ -[FHBankConnectDescriptionCleaner _aspspDescriptionCleaning:]
+ -[FHBankConnectDescriptionCleaner _furtherRbsCleaning:]
+ -[FHBankConnectDescriptionCleaner _genericDescriptionCleaning:]
+ -[FHBankConnectDescriptionCleaner _paymentDescriptionCleaning:]
+ -[FHBankConnectDescriptionCleaner _paypalDescriptionCleaning:]
+ -[FHBankConnectDescriptionCleaner _rbsCleaning:]
+ -[FHBankConnectDescriptionCleaner _serviceRemovePatternsFromDescription:]
+ -[FHBankConnectDescriptionCleaner aspspPatternKey]
+ -[FHBankConnectDescriptionCleaner cleanDescriptionForTransaction:]
+ -[FHBankConnectDescriptionCleaner cleanTransactionDescription:]
+ -[FHBankConnectDescriptionCleaner descriptionCleaningPatterns]
+ -[FHBankConnectDescriptionCleaner fpDescriptionCleaning:]
+ -[FHBankConnectDescriptionCleaner fpPatternKey]
+ -[FHBankConnectDescriptionCleaner generalRegexPatterns]
+ -[FHBankConnectDescriptionCleaner grouperKey]
+ -[FHBankConnectDescriptionCleaner init]
+ -[FHBankConnectDescriptionCleaner intlPatternKey]
+ -[FHBankConnectDescriptionCleaner paypalPatternKey]
+ -[FHBankConnectDescriptionCleaner rbsDatePatternKey]
+ -[FHBankConnectDescriptionCleaner rbsHeaderPatternKey]
+ -[FHBankConnectDescriptionCleaner serviceMatchKey]
+ -[FHBankConnectDescriptionCleaner serviceMatchPatterns]
+ -[FHBankConnectDescriptionCleaner serviceRemoveKey]
+ -[FHBankConnectDescriptionCleaner serviceRemovePatterns]
+ -[FHBankConnectDescriptionCleaner setAspspPatternKey:]
+ -[FHBankConnectDescriptionCleaner setDescriptionCleaningPatterns:]
+ -[FHBankConnectDescriptionCleaner setFpPatternKey:]
+ -[FHBankConnectDescriptionCleaner setGeneralRegexPatterns:]
+ -[FHBankConnectDescriptionCleaner setGrouperKey:]
+ -[FHBankConnectDescriptionCleaner setIntlPatternKey:]
+ -[FHBankConnectDescriptionCleaner setPaypalPatternKey:]
+ -[FHBankConnectDescriptionCleaner setRbsDatePatternKey:]
+ -[FHBankConnectDescriptionCleaner setRbsHeaderPatternKey:]
+ -[FHBankConnectDescriptionCleaner setServiceMatchKey:]
+ -[FHBankConnectDescriptionCleaner setServiceMatchPatterns:]
+ -[FHBankConnectDescriptionCleaner setServiceRemoveKey:]
+ -[FHBankConnectDescriptionCleaner setServiceRemovePatterns:]
+ -[FHBankConnectDescriptionCleaner setThreeCommaPatternKey:]
+ -[FHBankConnectDescriptionCleaner setTwoCommaPatternKey:]
+ -[FHBankConnectDescriptionCleaner threeCommaPatternKey]
+ -[FHBankConnectDescriptionCleaner twoCommaPatternKey]
+ -[FHDatabaseManager groupingSchemaUpdate]
+ -[FHTransaction processedDescription]
+ -[FHTransaction setProcessedDescription:]
+ GCC_except_table114
+ GCC_except_table196
+ GCC_except_table203
+ GCC_except_table45
+ GCC_except_table99
+ _FHDescriptionCleaningRegexMapping
+ _FHDescriptionCleaningRegexMapping.regexPatterns
+ _FHDescriptionCleaningTimeoutMilliseconds
+ _FHGeneralCleaningRegexPatterns
+ _FHGroupingVersionLatest
+ _FHProcessingHistoryGroupingIdentifier
+ _FHServiceMatchRegexPatterns
+ _FHServiceRemoveRegexPatterns
+ _FHTransactionProcessedDescriptionKey
+ _OBJC_CLASS_$_FHBankConnectDescriptionCleaner
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._aspspPatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._descriptionCleaningPatterns
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._fpPatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._generalRegexPatterns
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._grouperKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._intlPatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._paypalPatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._rbsDatePatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._rbsHeaderPatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._serviceMatchKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._serviceMatchPatterns
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._serviceRemoveKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._serviceRemovePatterns
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._threeCommaPatternKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._twoCommaPatternKey
+ _OBJC_IVAR_$_FHDatabaseManager._descriptionCleaner
+ _OBJC_IVAR_$_FHTransaction._processedDescription
+ _OBJC_METACLASS_$_FHBankConnectDescriptionCleaner
+ __OBJC_$_INSTANCE_METHODS_FHBankConnectDescriptionCleaner
+ __OBJC_$_INSTANCE_VARIABLES_FHBankConnectDescriptionCleaner
+ __OBJC_$_PROP_LIST_FHBankConnectDescriptionCleaner
+ __OBJC_CLASS_RO_$_FHBankConnectDescriptionCleaner
+ __OBJC_METACLASS_RO_$_FHBankConnectDescriptionCleaner
+ ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke.280
+ ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2.284
+ ___179+[FinHealthRecurringHelper histogramKeysForCardPurchaseTransaction:transactionAmount:transactionSourceIdentifier:transactionType:accountType:amountFromDatabase:receiptIdentifier:]_block_invoke.454
+ ___41-[FHDatabaseManager groupingSchemaUpdate]_block_invoke
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.352
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.355
+ ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.121
+ ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.129
+ ___49-[FHDatabaseManager getTransactionIdByServiceId:]_block_invoke.146
+ ___66-[FHBankConnectDescriptionCleaner cleanDescriptionForTransaction:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e42_v32?0"NSArray"8"NSArray"16"NSString"24lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8
+ ___block_literal_global.120
+ ___block_literal_global.124
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.232
+ ___block_literal_global.239
+ ___block_literal_global.259
+ ___block_literal_global.268
+ ___block_literal_global.274
+ ___block_literal_global.283
+ ___block_literal_global.291
+ ___block_literal_global.318
+ ___block_literal_global.374
+ ___block_literal_global.413
+ ___block_literal_global.519
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _objc_msgSend$_aspspDescriptionCleaning:
+ _objc_msgSend$_furtherRbsCleaning:
+ _objc_msgSend$_genericDescriptionCleaning:
+ _objc_msgSend$_paymentDescriptionCleaning:
+ _objc_msgSend$_paypalDescriptionCleaning:
+ _objc_msgSend$_rbsCleaning:
+ _objc_msgSend$_serviceRemovePatternsFromDescription:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$cleanDescriptionForTransaction:
+ _objc_msgSend$cleanTransactionDescription:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$fpDescriptionCleaning:
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$processedDescription
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$setProcessedDescription:
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_msgSend$whitespaceCharacterSet
+ _symbolic SS_Sit
+ _symbolic _____ySS_SitG s23_ContiguousArrayStorageC
- -[FinHealthBankConnectController addGroupingFeatures:databaseManager:]
- GCC_except_table113
- GCC_except_table194
- GCC_except_table199
- GCC_except_table98
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke.279
- ___144-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:merchantEntityMemberships:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2.283
- ___179+[FinHealthRecurringHelper histogramKeysForCardPurchaseTransaction:transactionAmount:transactionSourceIdentifier:transactionType:accountType:amountFromDatabase:receiptIdentifier:]_block_invoke.451
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.351
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.354
- ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.120
- ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.128
- ___49-[FHDatabaseManager getTransactionIdByServiceId:]_block_invoke.145
- ___block_descriptor_56_e8_32s40s48w_e42_v32?0"NSArray"8"NSArray"16"NSString"24lw48l8s32l8s40l8
- ___block_literal_global.119
- ___block_literal_global.123
- ___block_literal_global.198
- ___block_literal_global.200
- ___block_literal_global.229
- ___block_literal_global.238
- ___block_literal_global.258
- ___block_literal_global.265
- ___block_literal_global.273
- ___block_literal_global.282
- ___block_literal_global.288
- ___block_literal_global.315
- ___block_literal_global.373
- ___block_literal_global.516
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_FinHealthCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FinHealthCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FinHealthCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FinHealthCore
- _objc_msgSend$addGroupingFeatures:databaseManager:
- _objc_msgSend$insertGroupForTransaction:withGroup:type:
CStrings:
+ "  "
+ "%%(FHModelIncomeClassificationName)%%"
+ "%s"
+ "(t_tid integer primary key autoincrement, t_identifier text, t_service_identifier text, a_finance_account_id text, t_finance_transaction_id text, t_payment_hash text, t_source_identifier text, t_amount integer, t_currencycode text, t_timezone integer, t_date integer, t_status integer, t_status_changed_date integer, t_source integer, t_card_type integer, t_type integer, a_type integer, t_altDSID text, t_receipt_identifier text, t_associated_receipt_unique_id text, t_fh_internal_state integer, m_merchant_identifier text, m_industrycode integer, m_name text, m_raw_name text, m_category integer, m_detailed_category text, m_displayname text, m_street text, m_city text, m_state text, m_zip text, m_country_code text, m_country text, m_maps_merchant_id text, m_maps_merchant_result_id integer, m_maps_merchant_brand_id text, m_maps_merchant_brand_result_id integer, lat real, long real, v_accuracy real, h_accuracy real, dispute_type integer, dispute_status integer, peer_pay_counterpart text, peer_pay_type integer, t_description text, processed_description text, peer_pay_is_recurring integer, dispute_open_date integer, dispute_last_updated_date integer, proprietary_bank_transaction_code text, proprietary_bank_transaction_issuer text)"
+ "1.0"
+ "11.9"
+ "@\"FHBankConnectDescriptionCleaner\""
+ "ASPSP_PATTERN"
+ "CREATE TRIGGER IF NOT EXISTS transactions_ai AFTER INSERT ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, processed_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_date, new.t_amount, new.processed_description); END;"
+ "CREATE TRIGGER IF NOT EXISTS transactions_au AFTER UPDATE ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, processed_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_date, new.t_amount, new.processed_description); END;"
+ "CREATE TRIGGER IF NOT EXISTS transactions_bd BEFORE DELETE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, processed_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_date, old.t_amount, old.processed_description); END;"
+ "CREATE TRIGGER IF NOT EXISTS transactions_bu BEFORE UPDATE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, processed_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_date, old.t_amount, old.processed_description); END;"
+ "CREATE VIRTUAL TABLE IF NOT EXISTS fts_transactions USING fts5(t_identifier UNINDEXED, t_source_identifier UNINDEXED, a_type UNINDEXED, t_date UNINDEXED, t_amount UNINDEXED, processed_description, content=transactions, content_rowid=t_tid);"
+ "Error - Timed out cleaning transaction description with ID: %@"
+ "Error creating GROUPER regex: %@"
+ "Error creating aspsp regex: %@"
+ "Error creating date regex: %@"
+ "Error creating fp regex: %@"
+ "Error creating intl regex: %@"
+ "Error creating payment match regex: %@"
+ "Error creating paypal regex: %@"
+ "Error creating rbs header regex: %@"
+ "FHBankConnectDescriptionCleaner"
+ "FHProcessingHistoryGrouping"
+ "FP_PATTERN"
+ "FinanceKitDataStore : batch transactions %s"
+ "FinanceKitDateStore:streamTransactions"
+ "FinanceKitDateStore:transactionUpdates"
+ "GENERAL_DESCRIPTION_CLEANING_REGEX_PATTERNS"
+ "GROUPER"
+ "Grouping Schema Will Update"
+ "INTL_PATTERN"
+ "PAYPAL_PATTERN"
+ "RBS_DATE_PATTERN"
+ "RBS_HEADER_PATTERN"
+ "SERVICE_MATCH"
+ "SERVICE_PAYMENT_MATCH_PATTERNS"
+ "SERVICE_REMOVE_MATCH"
+ "SERVICE_REMOVE_PATTERNS"
+ "T@\"NSDictionary\",C,N,V_serviceMatchPatterns"
+ "T@\"NSDictionary\",C,N,V_serviceRemovePatterns"
+ "T@\"NSMutableDictionary\",C,N,V_descriptionCleaningPatterns"
+ "T@\"NSMutableDictionary\",C,N,V_generalRegexPatterns"
+ "T@\"NSString\",C,N,V_aspspPatternKey"
+ "T@\"NSString\",C,N,V_fpPatternKey"
+ "T@\"NSString\",C,N,V_grouperKey"
+ "T@\"NSString\",C,N,V_intlPatternKey"
+ "T@\"NSString\",C,N,V_paypalPatternKey"
+ "T@\"NSString\",C,N,V_processedDescription"
+ "T@\"NSString\",C,N,V_rbsDatePatternKey"
+ "T@\"NSString\",C,N,V_rbsHeaderPatternKey"
+ "T@\"NSString\",C,N,V_serviceMatchKey"
+ "T@\"NSString\",C,N,V_serviceRemoveKey"
+ "T@\"NSString\",C,N,V_threeCommaPatternKey"
+ "T@\"NSString\",C,N,V_twoCommaPatternKey"
+ "THREE_COMMA_PATTERN"
+ "TWO_COMMA_PATTERN"
+ "[Error] Interval already ended"
+ "_aspspDescriptionCleaning:"
+ "_aspspPatternKey"
+ "_descriptionCleaner"
+ "_descriptionCleaningPatterns"
+ "_fpPatternKey"
+ "_furtherRbsCleaning:"
+ "_generalRegexPatterns"
+ "_genericDescriptionCleaning:"
+ "_grouperKey"
+ "_intlPatternKey"
+ "_paymentDescriptionCleaning:"
+ "_paypalDescriptionCleaning:"
+ "_paypalPatternKey"
+ "_processedDescription"
+ "_rbsCleaning:"
+ "_rbsDatePatternKey"
+ "_rbsHeaderPatternKey"
+ "_serviceMatchKey"
+ "_serviceMatchPatterns"
+ "_serviceRemoveKey"
+ "_serviceRemovePatterns"
+ "_serviceRemovePatternsFromDescription:"
+ "_threeCommaPatternKey"
+ "_twoCommaPatternKey"
+ "aspspPatternKey"
+ "characterAtIndex:"
+ "cleanDescriptionForTransaction:"
+ "cleanTransactionDescription:"
+ "descriptionCleaningPatterns"
+ "description_cleaning_patterns"
+ "firstMatchInString:options:range:"
+ "fpDescriptionCleaning:"
+ "fpPatternKey"
+ "generalRegexPatterns"
+ "grouperKey"
+ "groupingSchemaUpdate"
+ "intlPatternKey"
+ "numberOfRanges"
+ "paypalPatternKey"
+ "processedDescription"
+ "rangeAtIndex:"
+ "rbsDatePatternKey"
+ "rbsHeaderPatternKey"
+ "regularExpressionWithPattern:options:error:"
+ "select t_identifier, processed_description from fts_transactions where a_type == %d AND processed_description IS NOT NULL order by t_date asc"
+ "serviceMatchKey"
+ "serviceMatchPatterns"
+ "serviceRemoveKey"
+ "serviceRemovePatterns"
+ "setAspspPatternKey:"
+ "setDescriptionCleaningPatterns:"
+ "setFpPatternKey:"
+ "setGeneralRegexPatterns:"
+ "setGrouperKey:"
+ "setIntlPatternKey:"
+ "setPaypalPatternKey:"
+ "setProcessedDescription:"
+ "setRbsDatePatternKey:"
+ "setRbsHeaderPatternKey:"
+ "setServiceMatchKey:"
+ "setServiceMatchPatterns:"
+ "setServiceRemoveKey:"
+ "setServiceRemovePatterns:"
+ "setThreeCommaPatternKey:"
+ "setTwoCommaPatternKey:"
+ "stringByReplacingMatchesInString:options:range:withTemplate:"
+ "threeCommaPatternKey"
+ "twoCommaPatternKey"
+ "update transactions set t_service_identifier = %@, t_finance_transaction_id = %@, a_finance_account_id = %@, t_payment_hash = %@, t_source_identifier = %@, t_amount = %d, t_currencycode = %@, t_timezone = %@, t_date = %d, t_status = %d, t_status_changed_date = %d, t_source = %d, t_card_type = %d, t_type = %d, a_type = %d, t_altDSID = %@, t_receipt_identifier = %@, t_associated_receipt_unique_id = %@, t_fh_internal_state = %d, m_merchant_identifier = %@, m_industrycode = %d, m_name = %@, m_raw_name = %@, m_category = %d, m_detailed_category = %@, m_displayname = %@, m_street = %@, m_city = %@, m_state = %@, m_zip = %@, m_country_code = %@, m_country = %@, m_maps_merchant_id = %@, m_maps_merchant_result_id = %d, m_maps_merchant_brand_id = %@, m_maps_merchant_brand_result_id = %d, lat = %f, long = %f, v_accuracy = %f, h_accuracy = %f, dispute_type = %d, dispute_status = %d, peer_pay_counterpart = %@, peer_pay_type = %d, t_description = %@, processed_description = %@, peer_pay_is_recurring = %d, dispute_open_date = %d, dispute_last_updated_date = %d, proprietary_bank_transaction_code = %@, proprietary_bank_transaction_issuer = %@ where t_identifier == %@"
+ "whitespaceAndNewlineCharacterSet"
+ "whitespaceCharacterSet"
- "(t_tid integer primary key autoincrement, t_identifier text, t_service_identifier text, a_finance_account_id text, t_finance_transaction_id text, t_payment_hash text, t_source_identifier text, t_amount integer, t_currencycode text, t_timezone integer, t_date integer, t_status integer, t_status_changed_date integer, t_source integer, t_card_type integer, t_type integer, a_type integer, t_altDSID text, t_receipt_identifier text, t_associated_receipt_unique_id text, t_fh_internal_state integer, m_merchant_identifier text, m_industrycode integer, m_name text, m_raw_name text, m_category integer, m_detailed_category text, m_displayname text, m_street text, m_city text, m_state text, m_zip text, m_country_code text, m_country text, m_maps_merchant_id text, m_maps_merchant_result_id integer, m_maps_merchant_brand_id text, m_maps_merchant_brand_result_id integer, lat real, long real, v_accuracy real, h_accuracy real, dispute_type integer, dispute_status integer, peer_pay_counterpart text, peer_pay_type integer, t_description text, peer_pay_is_recurring integer, dispute_open_date integer, dispute_last_updated_date integer, proprietary_bank_transaction_code text, proprietary_bank_transaction_issuer text)"
- "11.8"
- "CREATE TRIGGER IF NOT EXISTS transactions_ai AFTER INSERT ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, t_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_date, new.t_amount, new.t_description); END;"
- "CREATE TRIGGER IF NOT EXISTS transactions_au AFTER UPDATE ON transactions BEGIN INSERT INTO fts_transactions(rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, t_description) VALUES (new.t_tid, new.t_identifier, new.t_source_identifier, new.a_type, new.t_date, new.t_amount, new.t_description); END;"
- "CREATE TRIGGER IF NOT EXISTS transactions_bd BEFORE DELETE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, t_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_date, old.t_amount, old.t_description); END;"
- "CREATE TRIGGER IF NOT EXISTS transactions_bu BEFORE UPDATE ON transactions BEGIN INSERT INTO fts_transactions(fts_transactions, rowid, t_identifier, t_source_identifier, a_type, t_date, t_amount, t_description) VALUES('delete', old.t_tid, old.t_identifier, old.t_source_identifier, old.a_type, old.t_date, old.t_amount, old.t_description); END;"
- "CREATE VIRTUAL TABLE IF NOT EXISTS fts_transactions USING fts5(t_identifier UNINDEXED, t_source_identifier UNINDEXED, a_type UNINDEXED, t_date UNINDEXED, t_amount UNINDEXED, t_description, content=transactions, content_rowid=t_tid);"
- "Failed to update maps groups for bankConnect transaction %@"
- "FinanceKitDataStore : batch transactions update count=%ld deleted count=%ld placeholder=%ld"
- "addGroupingFeatures:databaseManager:"
- "select t_identifier, t_description from fts_transactions where a_type == %d AND t_description IS NOT NULL order by t_date asc"
- "update transactions set t_service_identifier = %@, t_finance_transaction_id = %@, a_finance_account_id = %@, t_payment_hash = %@, t_source_identifier = %@, t_amount = %d, t_currencycode = %@, t_timezone = %@, t_date = %d, t_status = %d, t_status_changed_date = %d, t_source = %d, t_card_type = %d, t_type = %d, a_type = %d, t_altDSID = %@, t_receipt_identifier = %@, t_associated_receipt_unique_id = %@, t_fh_internal_state = %d, m_merchant_identifier = %@, m_industrycode = %d, m_name = %@, m_raw_name = %@, m_category = %d, m_detailed_category = %@, m_displayname = %@, m_street = %@, m_city = %@, m_state = %@, m_zip = %@, m_country_code = %@, m_country = %@, m_maps_merchant_id = %@, m_maps_merchant_result_id = %d, m_maps_merchant_brand_id = %@, m_maps_merchant_brand_result_id = %d, lat = %f, long = %f, v_accuracy = %f, h_accuracy = %f, dispute_type = %d, dispute_status = %d, peer_pay_counterpart = %@, peer_pay_type = %d, t_description = %@, peer_pay_is_recurring = %d, dispute_open_date = %d, dispute_last_updated_date = %d, proprietary_bank_transaction_code = %@, proprietary_bank_transaction_issuer = %@ where t_identifier == %@"
- "\xf1"

```
