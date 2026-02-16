## AppStoreUtilities

> `/System/Library/PrivateFrameworks/AppStoreUtilities.framework/AppStoreUtilities`

```diff

-12.3.3.0.0
-  __TEXT.__text: 0x1030c
-  __TEXT.__auth_stubs: 0x900
+12.4.20.2.1
+  __TEXT.__text: 0x10568
+  __TEXT.__auth_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x1484
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x8a1
-  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__oslogstring: 0x798
-  __TEXT.__unwind_info: 0x688
+  __TEXT.__unwind_info: 0x660
   __TEXT.__objc_classname: 0x310
-  __TEXT.__objc_methname: 0x290f
+  __TEXT.__objc_methname: 0x292e
   __TEXT.__objc_methtype: 0x7f9
-  __TEXT.__objc_stubs: 0x1de0
+  __TEXT.__objc_stubs: 0x1e00
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x890
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xc40
   __AUTH_CONST.__objc_const: 0x2328

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4998D9EC-C4A4-3BDC-A4BD-48A88BDF343E
+  UUID: E33B4C11-934E-3F00-BC73-E3370C94EAEA
   Functions: 476
-  Symbols:   1792
-  CStrings:  883
+  Symbols:   1790
+  CStrings:  884
 
Symbols:
+ ___chkstk_darwin
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
- _CFStringGetFastestEncoding
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
Functions:
~ -[ASUSQLiteSchema initWithConnection:] : 116 -> 108
~ -[ASUSQLiteSchema column:existsInTable:] : 304 -> 300
~ ___47-[ASUSQLiteSchema migrateToVersion:usingBlock:]_block_invoke : 520 -> 548
~ -[ASUSQLiteSchema tableExists:] : 260 -> 264
~ -[ASUSQLiteDatabaseSession initWithConnection:] : 116 -> 108
~ _ASULogHandleForCategory : 100 -> 108
~ -[ASUSQLiteQueryResults initWithStatement:] : 120 -> 112
~ -[ASUSQLiteQueryResults enumerateRowsUsingBlock:] : 340 -> 328
~ -[ASUSQLiteQueryResults firstNumberValue] : 256 -> 252
~ -[ASUSQLiteCursor initWithStatement:] : 536 -> 544
~ -[ASUSQLiteCursor dictionaryWithValuesForColumnNames:] : 264 -> 268
~ ___54-[ASUSQLiteCursor dictionaryWithValuesForColumnNames:]_block_invoke : 132 -> 136
~ _ASUSQLiteCopyFoundationValue : 672 -> 684
~ -[ASUSQLiteMemoryEntity initWithDatabaseID:propertyValues:externalPropertyValues:] : 180 -> 176
~ -[ASUSQLiteMemoryEntity initWithDatabaseEntity:properties:] : 160 -> 156
~ -[ASUSQLiteMemoryEntity reloadFromDatabaseEntity:properties:] : 144 -> 148
~ -[ASUSQLiteMemoryEntity setValue:forProperty:] : 108 -> 112
~ -[ASUSQLiteMemoryEntity setValues:forProperties:count:] : 112 -> 104
~ -[ASUSQLiteMemoryEntity setValue:forExternalProperty:] : 108 -> 112
~ -[ASUSQLiteMemoryEntity setValues:forExternalProperties:count:] : 112 -> 104
~ -[ASUSQLiteMemoryEntity valueForProperty:] : 348 -> 364
~ -[ASUSQLiteMemoryEntity description] : 148 -> 156
~ -[ASUSQLiteMemoryEntity isEqual:] : 248 -> 264
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) boolValueForProperty:] : 56 -> 60
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) dateValueForProperty:] : 88 -> 104
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) integerValueForProperty:] : 56 -> 60
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) numberValueForProperty:] : 88 -> 104
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) stringValueForProperty:] : 88 -> 104
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) uuidValueForProperty:] : 88 -> 104
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) urlValueForProperty:] : 88 -> 104
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) arrayValueForProperty:] : 88 -> 104
~ -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) dictValueForProperty:] : 88 -> 104
~ -[ASUSQLiteEntity initWithPropertyValues:onConnection:] : 332 -> 328
~ -[ASUSQLiteEntity _copyTableClusteredValuesWithValues:] : 260 -> 252
~ ___55-[ASUSQLiteEntity initWithPropertyValues:onConnection:]_block_invoke : 220 -> 228
~ +[ASUSQLiteEntity _insertValues:intoTable:withPersistentID:onConnection:] : 892 -> 884
~ +[ASUSQLiteEntity disambiguatedSQLForProperty:] : 176 -> 172
~ -[ASUSQLiteEntity deleteFromDatabase] : 264 -> 268
~ ___37-[ASUSQLiteEntity deleteFromDatabase]_block_invoke : 428 -> 444
~ -[ASUSQLiteEntity _deleteRowFromTable:usingColumn:] : 220 -> 216
~ ___37-[ASUSQLiteEntity deleteFromDatabase]_block_invoke_2 : 220 -> 232
~ -[ASUSQLiteEntity existsInDatabase] : 288 -> 292
~ ___35-[ASUSQLiteEntity existsInDatabase]_block_invoke : 96 -> 100
~ -[ASUSQLiteEntity getValuesForProperties:] : 892 -> 900
~ ___42-[ASUSQLiteEntity getValuesForProperties:]_block_invoke_2 : 200 -> 204
~ ___42-[ASUSQLiteEntity getValuesForProperties:]_block_invoke_3 : 220 -> 216
~ ___42-[ASUSQLiteEntity getValuesForProperties:]_block_invoke_4 : 124 -> 128
~ -[ASUSQLiteEntity setValuesWithDictionary:] : 220 -> 228
~ ___43-[ASUSQLiteEntity setValuesWithDictionary:]_block_invoke_2 : 940 -> 928
~ ___43-[ASUSQLiteEntity setValuesWithDictionary:]_block_invoke_3 : 96 -> 100
~ ___43-[ASUSQLiteEntity setValuesWithDictionary:]_block_invoke_4 : 176 -> 172
~ -[ASUSQLiteEntity valueForProperty:] : 204 -> 216
~ ___73+[ASUSQLiteEntity _insertValues:intoTable:withPersistentID:onConnection:]_block_invoke : 328 -> 336
~ ___55-[ASUSQLiteEntity _copyTableClusteredValuesWithValues:]_block_invoke : 276 -> 284
~ -[ASUSQLiteEntity(SQLiteTypeChecking) boolValueForProperty:] : 56 -> 60
~ -[ASUSQLiteEntity(SQLiteTypeChecking) dictValueForProperty:] : 88 -> 104
~ -[ASUSQLiteEntity(SQLiteTypeChecking) errorValueForProperty:] : 148 -> 156
~ -[ASUSQLiteEntity(SQLiteTypeChecking) integerValueForProperty:] : 56 -> 60
~ -[ASUSQLiteEntity(SQLiteTypeChecking) numberValueForProperty:] : 88 -> 104
~ -[ASUSQLiteEntity(SQLiteTypeChecking) stringValueForProperty:] : 88 -> 104
~ -[ASUSQLiteEntity(SQLiteTypeChecking) uuidValueForProperty:] : 88 -> 104
~ -[ASUSQLiteEntity(SQLiteTypeChecking) urlValueForProperty:] : 88 -> 104
~ -[ASUSQLiteDatabase initWithConnection:] : 236 -> 244
~ -[ASUSQLiteDatabase modifyStore:usingTransaction:] : 192 -> 184
~ ___50-[ASUSQLiteDatabase modifyStore:usingTransaction:]_block_invoke : 124 -> 128
~ -[ASUSQLiteDatabase _modifyUsingTransactionClass:withBlock:] : 220 -> 216
~ -[ASUSQLiteDatabase modifyStore:usingTransaction:completion:] : 228 -> 220
~ ___61-[ASUSQLiteDatabase modifyStore:usingTransaction:completion:]_block_invoke : 156 -> 164
~ -[ASUSQLiteDatabase modifyStore:usingTransactionClass:withBlock:] : 196 -> 188
~ -[ASUSQLiteDatabase modifyStore:usingTransactionClass:withBlock:completion:] : 244 -> 228
~ ___76-[ASUSQLiteDatabase modifyStore:usingTransactionClass:withBlock:completion:]_block_invoke : 124 -> 128
~ -[ASUSQLiteDatabase readStore:usingSession:] : 192 -> 184
~ ___44-[ASUSQLiteDatabase readStore:usingSession:]_block_invoke : 236 -> 240
~ -[ASUSQLiteDatabase _readUsingSession:withBlock:] : 364 -> 356
~ -[ASUSQLiteDatabase readStore:usingSession:completion:] : 228 -> 220
~ ___55-[ASUSQLiteDatabase readStore:usingSession:completion:]_block_invoke : 296 -> 304
~ -[ASUSQLiteDatabase connectionNeedsResetForReopen:] : 256 -> 268
~ -[ASUSQLiteDatabase connectionNeedsResetForCorruption:] : 420 -> 432
~ ___44-[ASUSQLiteDatabase verifyDatabaseIntegrity]_block_invoke : 284 -> 296
~ -[ASUSQLiteDatabase _performMigrationIfNeededForStore:calledAfterTransaction:] : 380 -> 384
~ ___78-[ASUSQLiteDatabase _performMigrationIfNeededForStore:calledAfterTransaction:]_block_invoke : 372 -> 380
~ ___78-[ASUSQLiteDatabase _performMigrationIfNeededForStore:calledAfterTransaction:]_block_invoke_2 : 144 -> 140
~ ___49-[ASUSQLiteDatabase _readUsingSession:withBlock:]_block_invoke : 80 -> 84
~ -[ASUSQLiteDatabaseStore initWithDatabase:] : 116 -> 108
~ -[ASUSQLiteDatabaseStoreMigrator initWithConnection:tableNames:] : 160 -> 156
~ -[ASUSQLiteDatabaseStoreMigrator connection] : 8 -> 56
~ -[ASUSQLiteDatabaseStoreMigrator _executeStatement:canFailMigration:bindings:] : 164 -> 160
~ -[ASUSQLiteDatabaseStoreMigrator _executeQuery:canFailMigration:withResults:] : 216 -> 212
~ -[ASUSQLiteQuery initOnConnection:descriptor:] : 152 -> 148
~ -[ASUSQLiteQuery applyBinding:atIndex:] : 152 -> 160
~ -[ASUSQLiteQuery connection] : 8 -> 56
~ ___39-[ASUSQLiteQuery copyEntityIdentifiers]_block_invoke : 96 -> 100
~ -[ASUSQLiteQuery copySelectSQLWithProperties:] : 348 -> 344
~ -[ASUSQLiteQuery createTemporaryTableWithName:properties:] : 612 -> 600
~ ___58-[ASUSQLiteQuery createTemporaryTableWithName:properties:]_block_invoke : 92 -> 96
~ -[ASUSQLiteQuery enumerateMemoryEntitiesUsingBlock:] : 136 -> 140
~ -[ASUSQLiteQuery enumerateMemoryEntitiesWithProperties:usingBlock:] : 328 -> 312
~ -[ASUSQLiteQuery enumeratePersistentIDsAndProperties:usingBlock:] : 556 -> 532
~ ___65-[ASUSQLiteQuery enumeratePersistentIDsAndProperties:usingBlock:]_block_invoke : 292 -> 296
~ ___65-[ASUSQLiteQuery enumeratePersistentIDsAndProperties:usingBlock:]_block_invoke_2 : 340 -> 320
~ ___65-[ASUSQLiteQuery enumeratePersistentIDsAndProperties:usingBlock:]_block_invoke_3 : 124 -> 128
~ -[ASUSQLiteQueryDescriptor _newSelectSQLWithProperties:columns:] : 1084 -> 1104
~ +[ASUSQLiteEntity(ASUSQLiteQuery) anyOnConnection:predicate:] : 356 -> 348
~ +[ASUSQLiteEntity(ASUSQLiteQuery) allOnConnection:predicate:] : 372 -> 364
~ +[ASUSQLiteEntity _aggregateValueForProperty:function:predicate:onConnection:] : 660 -> 644
~ +[ASUSQLiteEntity(ASUSQLiteQuery) sumForProperty:predicate:onConnection:] : 108 -> 124
~ +[ASUSQLiteEntity(ASUSQLiteQuery) queryOnConnection:predicate:orderingProperties:orderingDirections:entityClass:] : 248 -> 228
~ ___94+[ASUSQLiteEntity(ASUSQLiteQuery) _aggregateValueForProperty:function:predicate:onConnection:]_block_invoke : 192 -> 196
~ ___94+[ASUSQLiteEntity(ASUSQLiteQuery) _aggregateValueForProperty:function:predicate:onConnection:]_block_invoke_2 : 80 -> 84
~ +[ASUSQLiteMemoryEntity(ASUSQLiteQuery) anyOnConnection:predicate:] : 324 -> 320
~ ___67+[ASUSQLiteMemoryEntity(ASUSQLiteQuery) anyOnConnection:predicate:]_block_invoke : 56 -> 80
~ +[ASUSQLiteMemoryEntity(ASUSQLiteQuery) queryOnConnection:predicate:orderingProperties:] : 212 -> 204
~ _ASUSQLiteApplyConnectionOptions : 268 -> 276
~ _ASUSQLiteEncryptDatabase : 608 -> 616
~ _ASUSQLiteCreateErrorForResultCode : 288 -> 296
~ _ASUSQLiteTrashDatabaseName : 472 -> 504
~ _ASUSQLiteGetRelatedFilePath : 120 -> 124
~ _ASUSQLiteDeleteDatabase : 276 -> 272
~ _ASUSQLiteOpenDatabaseAndApplyOptions : 300 -> 316
~ -[ASUSQLitePredicate copyWithZone:] : 4 -> 40
~ -[ASUSQLitePropertyPredicate copyWithZone:] : 4 -> 40
~ -[ASUSQLitePropertyPredicate hash] : 112 -> 116
~ -[ASUSQLitePropertyPredicate isEqual:] : 228 -> 244
~ -[ASUSQLitePropertyPredicate property] : 16 -> 8
~ -[ASUSQLitePropertyPredicate .cxx_destruct] : 20 -> 12
~ +[ASUSQLiteComparisonPredicate predicateWithProperty:equalToLongLong:] : 132 -> 136
~ +[ASUSQLiteComparisonPredicate predicateWithProperty:value:comparisonType:] : 232 -> 188
~ -[ASUSQLiteComparisonPredicate copyWithZone:] : 4 -> 40
~ -[ASUSQLiteComparisonPredicate applyBinding:atIndex:] : 252 -> 244
~ -[ASUSQLiteComparisonPredicate description] : 184 -> 180
~ -[ASUSQLiteComparisonPredicate hash] : 96 -> 104
~ -[ASUSQLiteComparisonPredicate isEqual:] : 256 -> 272
~ -[ASUSQLiteComparisonPredicate SQLForEntityClass:] : 168 -> 176
~ -[ASUSQLiteComparisonPredicate comparisonType] : 16 -> 8
~ -[ASUSQLiteComparisonPredicate value] : 16 -> 8
~ -[ASUSQLiteComparisonPredicate .cxx_destruct] : 20 -> 12
~ +[ASUSQLiteContainsPredicate containsPredicateWithProperty:values:] : 180 -> 152
~ +[ASUSQLiteContainsPredicate containsPredicateWithProperty:query:queryProperty:] : 232 -> 188
~ +[ASUSQLiteContainsPredicate doesNotContainPredicateWithProperty:values:] : 184 -> 156
~ -[ASUSQLiteContainsPredicate copyWithZone:] : 4 -> 40
~ -[ASUSQLiteContainsPredicate applyBinding:atIndex:] : 324 -> 308
~ -[ASUSQLiteContainsPredicate isEqual:] : 400 -> 432
~ -[ASUSQLiteContainsPredicate SQLForEntityClass:] : 424 -> 400
~ -[ASUSQLiteContainsPredicate isNegative] : 16 -> 8
~ -[ASUSQLiteContainsPredicate query] : 16 -> 8
~ -[ASUSQLiteContainsPredicate queryProperty] : 16 -> 8
~ -[ASUSQLiteContainsPredicate values] : 16 -> 8
~ -[ASUSQLiteContainsPredicate .cxx_destruct] : 104 -> 80
~ +[ASUSQLiteNullPredicate isNotNullPredicateWithProperty:] : 132 -> 116
~ +[ASUSQLiteNullPredicate isNullPredicateWithProperty:] : 136 -> 120
~ -[ASUSQLiteNullPredicate copyWithZone:] : 4 -> 40
~ -[ASUSQLiteNullPredicate SQLForEntityClass:] : 180 -> 184
~ -[ASUSQLiteNullPredicate matchesNull] : 16 -> 8
~ +[ASUSQLiteCompoundPredicate predicateMatchingAllPredicates:] : 148 -> 132
~ +[ASUSQLiteCompoundPredicate predicateMatchingAnyPredicates:] : 148 -> 132
~ +[ASUSQLiteCompoundPredicate predicateWithProperty:values:comparisonType:] : 384 -> 388
~ -[ASUSQLiteCompoundPredicate copyWithZone:] : 4 -> 40
~ -[ASUSQLiteCompoundPredicate applyBinding:atIndex:] : 280 -> 272
~ -[ASUSQLiteCompoundPredicate hash] : 132 -> 128
~ -[ASUSQLiteCompoundPredicate isEqual:] : 236 -> 220
~ -[ASUSQLiteCompoundPredicate SQLForEntityClass:] : 440 -> 436
~ -[ASUSQLiteCompoundPredicate predicates] : 16 -> 8
~ -[ASUSQLiteCompoundPredicate .cxx_destruct] : 84 -> 68
~ -[ASUSQLiteStatement initWithStatement:onConnection:] : 136 -> 140
~ -[ASUSQLiteStatement columnIndexByName] : 272 -> 276
~ -[ASUSQLiteStatement SQL] : 112 -> 116
~ -[ASUSQLiteStatement bindArray:atPosition:] : 108 -> 112
~ -[ASUSQLiteStatement bindData:atPosition:] : 172 -> 176
~ -[ASUSQLiteStatement bindDataCopy:atPosition:] : 172 -> 176
~ -[ASUSQLiteStatement bindDictionary:atPosition:] : 108 -> 112
~ -[ASUSQLiteStatement bindNumber:atPosition:] : 260 -> 264
~ -[ASUSQLiteStatement bindString:atPosition:] : 284 -> 352
~ -[ASUSQLiteStatement bindUUID:atPosition:] : 96 -> 100
~ -[ASUSQLiteStatement bindURL:atPosition:] : 96 -> 100
~ -[ASUSQLiteDatabaseStoreSchema initWithConnection:schemaName:tableNames:] : 292 -> 288
~ ___52-[ASUSQLiteDatabaseStoreSchema currentSchemaVersion]_block_invoke : 96 -> 100
~ -[ASUSQLiteDatabaseStoreSchema column:existsInTable:] : 304 -> 300
~ ___60-[ASUSQLiteDatabaseStoreSchema migrateToVersion:usingBlock:]_block_invoke_2 : 104 -> 112
~ -[ASUSQLiteDatabaseStoreSchema _migrateToVersion:usingMapping:isReattempt:] : 924 -> 940
~ ___75-[ASUSQLiteDatabaseStoreSchema _migrateToVersion:usingMapping:isReattempt:]_block_invoke : 604 -> 620
~ ___44-[ASUSQLiteDatabaseStoreSchema tableExists:]_block_invoke : 92 -> 96
~ -[ASUSQLiteDatabaseStoreDescriptor initWithSchemaName:tableNames:sessionClass:transactionClass:] : 176 -> 172
~ +[ASUDefaultsManager copyDefaultsKeyForEncryptionKeyWithIdentifier:] : 280 -> 288
~ +[ASUDefaultsManager _copyNumberForKey:applicationId:] : 92 -> 88
~ ___53+[ASUDefaultsManager _isRunningInAppleVirtualMachine]_block_invoke : 220 -> 224
~ -[ASUSQLiteTransporter initWithDatabasePath:] : 116 -> 108
~ -[ASUSQLiteTransporter canBeginTransportation] : 904 -> 932
~ -[ASUSQLiteTransporter endTransportationAndRemoveDatabase] : 416 -> 424
~ -[ASUSQLiteTransporter performTransportationUsingBlock:] : 156 -> 164
~ ___45+[ASUSQLiteTransporter _isKnownDatabasePath:]_block_invoke : 92 -> 96
~ +[ASUSQLiteKeychainHelper fetchKeyWithIdentifier:error:] : 584 -> 596
~ +[ASUSQLiteKeychainHelper storeKey:withIdentifier:error:] : 448 -> 452
~ +[ASUSQLiteKeychainHelper _copyErrorForOSStatus:] : 284 -> 296
~ -[ASUSQLiteSchemaMigration initWithConnection:] : 124 -> 116
~ -[ASUSQLiteSchemaMigration _executeStatement:canFailMigration:bindings:] : 196 -> 184
~ -[ASUSQLiteConnection initWithOptions:] : 140 -> 144
~ -[ASUSQLiteConnection dealloc] : 244 -> 252
~ -[ASUSQLiteConnection _close] : 368 -> 372
~ -[ASUSQLiteConnection dispatchAfterTransaction:] : 176 -> 180
~ -[ASUSQLiteConnection executePreparedQuery:withResults:] : 272 -> 288
~ -[ASUSQLiteConnection _verifiedStatementForPreparedStatement:error:] : 528 -> 504
~ -[ASUSQLiteConnection executePreparedStatement:error:bindings:] : 248 -> 244
~ -[ASUSQLiteConnection _executeStatement:error:] : 200 -> 196
~ -[ASUSQLiteConnection _verifiedStatementForSQL:error:] : 336 -> 328
~ -[ASUSQLiteConnection executeStatement:error:bindings:] : 328 -> 320
~ -[ASUSQLiteConnection finalizePreparedStatement:error:] : 212 -> 216
~ -[ASUSQLiteConnection performSavepoint:] : 436 -> 464
~ -[ASUSQLiteConnection performTransaction:error:] : 916 -> 936
~ -[ASUSQLiteConnection prepareStatement:error:] : 268 -> 276
~ -[ASUSQLiteConnection _prepareStatement:error:] : 320 -> 316
~ ___35-[ASUSQLiteConnection tableExists:]_block_invoke : 92 -> 96
~ -[ASUSQLiteConnection _executeWithError:usingBlock:] : 972 -> 992
~ -[ASUSQLiteConnection _resetAfterCorruptionError] : 524 -> 528
CStrings:
+ "getCString:maxLength:encoding:"

```
