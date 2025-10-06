## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.8.2.1.0
-  __TEXT.__text: 0x8abe8
-  __TEXT.__auth_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x330c
+1.8.2.2.0
+  __TEXT.__text: 0x8ba58
+  __TEXT.__auth_stubs: 0x2150
+  __TEXT.__objc_methlist: 0x334c
   __TEXT.__const: 0x1338
-  __TEXT.__cstring: 0xa272
-  __TEXT.__oslogstring: 0x2899
+  __TEXT.__cstring: 0xa242
+  __TEXT.__oslogstring: 0x2a69
   __TEXT.__gcc_except_tab: 0xd40
   __TEXT.__swift5_typeref: 0xb58
   __TEXT.__swift5_capture: 0x550

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x19e8
+  __TEXT.__unwind_info: 0x19f8
   __TEXT.__eh_frame: 0x26b0
   __TEXT.__objc_classname: 0x695
-  __TEXT.__objc_methname: 0x8b2b
+  __TEXT.__objc_methname: 0x8ca4
   __TEXT.__objc_methtype: 0x8d5
-  __TEXT.__objc_stubs: 0x5fe0
+  __TEXT.__objc_stubs: 0x60c0
   __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__const: 0x18b8
+  __DATA_CONST.__const: 0x18c0
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ff8
+  __DATA_CONST.__objc_selrefs: 0x2030
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0x10b0
+  __AUTH_CONST.__auth_got: 0x10b8
   __AUTH_CONST.__const: 0x1f08
-  __AUTH_CONST.__cfstring: 0x6540
+  __AUTH_CONST.__cfstring: 0x6500
   __AUTH_CONST.__objc_const: 0x64d0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x198

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 573115C9-0B98-3DB6-91E3-E6E7887700F9
-  Functions: 2227
-  Symbols:   5219
-  CStrings:  3606
+  UUID: 99267169-7A74-322E-90B3-F0187AEE965E
+  Functions: 2232
+  Symbols:   5238
+  CStrings:  3622
 
Symbols:
+ -[FHDatabaseManager _buildTransactionIdFilter:]
+ -[FHDatabaseManager _executeFeatureQuery:aggregatedFeatures:]
+ -[FHDatabaseManager _executeSeparateQueriesForTransactionId:amountQueries:dateTimeQueries:merchantQueries:multiClassQuery:]
+ -[FHDatabaseManager _executeSeparateQueriesForTransactionIds:amountQueries:dateTimeQueries:merchantQueries:multiClassQuery:]
+ -[FHDatabaseManager _invertFeaturesForTransaction:featuresString:compoundFeatures:]
+ -[FHModel dealloc]
+ GCC_except_table107
+ GCC_except_table114
+ GCC_except_table122
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table174
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table201
+ GCC_except_table206
+ GCC_except_table208
+ _FHGroupingCount
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke.270
+ ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2.274
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.341
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.344
+ ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.120
+ ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.128
+ ___block_descriptor_64_e8_32s40r48r56w_e17_v16?0"NSArray"8ls32l8w56l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e17_v16?0"NSArray"8ls32l8s40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e23_v16?0"FHTransaction"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.119
+ ___block_literal_global.123
+ ___block_literal_global.249
+ ___block_literal_global.264
+ ___block_literal_global.273
+ ___block_literal_global.363
+ ___block_literal_global.396
+ ___block_literal_global.405
+ _objc_msgSend$_buildTransactionIdFilter:
+ _objc_msgSend$_executeFeatureQuery:aggregatedFeatures:
+ _objc_msgSend$_executeSeparateQueriesForTransactionId:amountQueries:dateTimeQueries:merchantQueries:multiClassQuery:
+ _objc_msgSend$_executeSeparateQueriesForTransactionIds:amountQueries:dateTimeQueries:merchantQueries:multiClassQuery:
+ _objc_msgSend$_invertFeaturesForTransaction:featuresString:compoundFeatures:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$setComputeUnits:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_retain_x6
- -[FHDatabaseManager _invertFeaturesForTransactions:]
- GCC_except_table103
- GCC_except_table110
- GCC_except_table118
- GCC_except_table150
- GCC_except_table152
- GCC_except_table158
- GCC_except_table160
- GCC_except_table170
- GCC_except_table176
- GCC_except_table178
- GCC_except_table190
- GCC_except_table191
- GCC_except_table197
- GCC_except_table202
- GCC_except_table204
- ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke.280
- ___118-[FHDatabaseManager computeRecurringClassesWithMerchantEntityCounts:peerPaymentCounts:merchantDetailedCategoryCounts:]_block_invoke_2.284
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.351
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.354
- ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.121
- ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.129
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSArray"8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e23_v16?0"FHTransaction"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40r48r56w_e17_v16?0"NSArray"8lw56l8s32l8r40l8r48l8
- ___block_literal_global.120
- ___block_literal_global.124
- ___block_literal_global.239
- ___block_literal_global.259
- ___block_literal_global.274
- ___block_literal_global.283
- ___block_literal_global.373
- ___block_literal_global.406
- ___block_literal_global.415
- _objc_msgSend$_invertFeaturesForTransactions:
CStrings:
+ "%@ AND f.identifier IN (%@)"
+ "%@ AND t_identifier IN (%@)"
+ "%s No schema found for table: %@"
+ "%s deallocated"
+ "%s: Feature name '%@' does not have version"
+ "%s: Required fields in processing history table not found. Expected %lu got %lu"
+ "+[FHModel retrievePersistedModelVersion:]"
+ "+[FHModel retrievePersistedModelVersion:]_block_invoke_2"
+ "-[FHDatabaseEntity _initWithJoinClauseExpression:databaseManager:entities:]_block_invoke"
+ "-[FHModel dealloc]"
+ "BEGIN \"_computeAllAggregateFeaturesWithTransactionId\""
+ "Creating FHBankConnectDescriptionCleaner"
+ "END \"_computeAllAggregateFeaturesWithTransactionId\""
+ "No model version found for income classification. Skipping income insights retrieval."
+ "SELECT t_identifier, t_compound_feature_value FROM features_compound_realtime WHERE t_identifier IN (%@)"
+ "_buildTransactionIdFilter:"
+ "_computeAllAggregateFeaturesWithTransactionId"
+ "_executeFeatureQuery:aggregatedFeatures:"
+ "_executeSeparateQueriesForTransactionId:amountQueries:dateTimeQueries:merchantQueries:multiClassQuery:"
+ "_executeSeparateQueriesForTransactionIds:amountQueries:dateTimeQueries:merchantQueries:multiClassQuery:"
+ "_invertFeaturesForTransaction:featuresString:compoundFeatures:"
+ "objectForKeyedSubscript:"
+ "select count(*) from fh_grouping"
+ "setComputeUnits:"
+ "setObject:forKeyedSubscript:"
- " union "
- "%@ where simple_features.t_identifier == '%@' limit %%d"
- "%@ where simple_features.t_identifier in (%@) GROUP BY simple_features.t_identifier limit %%d"
- "'), compound_features.t_compound_feature_value simple_features from ("
- ") simple_features left join features_compound_realtime compound_features on simple_features.t_identifier = compound_features.t_identifier "
- "_invertFeaturesForTransactions:"
- "select simple_features.t_identifier, group_concat(FHSmartFeatureAggregateType, '"

```
