## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3437.120.13.0.1
-  __TEXT.__text: 0x2f0ce0
+3437.120.20.0.0
+  __TEXT.__text: 0x2f1af4
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x18fec
+  __TEXT.__objc_methlist: 0x1909c
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0x7a38a
-  __TEXT.__oslogstring: 0x3ae00
-  __TEXT.__gcc_except_tab: 0x19a68
+  __TEXT.__cstring: 0x7a493
+  __TEXT.__oslogstring: 0x3aeaf
+  __TEXT.__gcc_except_tab: 0x19a80
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9988
+  __TEXT.__unwind_info: 0x9998
   __TEXT.__objc_classname: 0x269f
-  __TEXT.__objc_methname: 0x4101a
-  __TEXT.__objc_methtype: 0x8807
-  __TEXT.__objc_stubs: 0x2c940
+  __TEXT.__objc_methname: 0x411de
+  __TEXT.__objc_methtype: 0x882e
+  __TEXT.__objc_stubs: 0x2cae0
   __DATA_CONST.__got: 0x16f8
-  __DATA_CONST.__const: 0x8e08
+  __DATA_CONST.__const: 0x8e10
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc30
+  __DATA_CONST.__objc_selrefs: 0xdca8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x878
+  __DATA_CONST.__objc_superrefs: 0x880
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x2958
-  __AUTH_CONST.__cfstring: 0x21f40
-  __AUTH_CONST.__objc_const: 0x3b1c8
+  __AUTH_CONST.__cfstring: 0x22040
+  __AUTH_CONST.__objc_const: 0x3b298
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1ebc
+  __DATA.__objc_ivar: 0x1ec8
   __DATA.__data: 0x2630
   __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0x3ac0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13104
-  Symbols:   42847
-  CStrings:  22597
+  Functions: 13121
+  Symbols:   42898
+  CStrings:  22627
 
Symbols:
+ +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:]
+ +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:].cold.1
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:]
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:].cold.1
+ +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]
+ +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:].cold.1
+ +[CKRecord(BRCItemAdditions) _validateCKObject:isRereference:enhancedDrivePrivacyEnabled:]
+ +[CKRecord(BRCItemAdditions) _validateCKObject:isRereference:enhancedDrivePrivacyEnabled:].cold.1
+ +[CKRecord(BRCItemAdditions) _validateCKObject:isRereference:enhancedDrivePrivacyEnabled:].cold.2
+ +[CKRecord(BRCItemAdditions) _validateCKObject:isRereference:enhancedDrivePrivacyEnabled:].cold.3
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) dbAge]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasDbAge]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasIsConsolidated]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) isConsolidated]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setDbAge:]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setHasDbAge:]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setHasIsConsolidated:]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setIsConsolidated:]
+ -[AppTelemetryInvestigation(BRCAdditions) _daysSinceLastOSUpdate]
+ -[AppTelemetryInvestigation(BRCAdditions) _daysSinceLastOSUpdate].cold.1
+ -[AppTelemetryInvestigation(BRCAdditions) _dbAgeFromDbCreationDate:]
+ -[AppTelemetryInvestigation(BRCAdditions) init]
+ -[BRCAccountSession dbCreationDate]
+ -[BRCAccountSession isConsolidatedAccount]
+ -[BRCFSUploader _serializeServerSideAssetCopyPluginFieldsForRecord:newZone:origZone:]
+ -[BRCUserDefaults allowAssetReferencesOfMMCSV1Assets]
+ -[BRCUserDefaults enhancedDrivePrivacyRolledBack]
+ GCC_except_table144
+ GCC_except_table199
+ GCC_except_table213
+ GCC_except_table230
+ GCC_except_table242
+ GCC_except_table316
+ GCC_except_table561
+ GCC_except_table94
+ OBJC_IVAR_$_AppTelemetryInvestigation._dbAge
+ OBJC_IVAR_$_AppTelemetryInvestigation._isConsolidated
+ OBJC_IVAR_$_BRCAccountSession._dbCreationDate
+ __OBJC_$_INSTANCE_METHODS_AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension|BRCAdditions)
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.348
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.349
+ ___181+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]_block_invoke
+ ___181+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]_block_invoke.cold.1
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.513
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.259
+ ___65-[AppTelemetryInvestigation(BRCAdditions) _daysSinceLastOSUpdate]_block_invoke
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.212
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.213
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.733
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.737
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.735
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.267
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.267.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.269
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.269.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.275
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.279
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.279.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.279.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.665
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.665.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.666
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.669
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.669.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.669.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.671
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.672
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.391.cold.1
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.395
+ ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.229
+ ___block_descriptor_98_e8_32s40s48s56r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8r56l8
+ ___block_literal_global.278
+ ___block_literal_global.2833
+ ___block_literal_global.347
+ ___block_literal_global.356
+ ___block_literal_global.364
+ ___block_literal_global.381
+ ___block_literal_global.397
+ ___block_literal_global.402
+ ___block_literal_global.407
+ ___block_literal_global.412
+ ___block_literal_global.417
+ ___block_literal_global.422
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.440
+ ___block_literal_global.445
+ ___block_literal_global.450
+ ___block_literal_global.487
+ ___block_literal_global.758
+ ___block_literal_global.939
+ ___block_literal_global.947
+ _kBRRecordAssetReReference
+ _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:
+ _objc_msgSend$_dbAgeFromDbCreationDate:
+ _objc_msgSend$_registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:
+ _objc_msgSend$_serializeServerSideAssetCopyPluginFieldsForRecord:newZone:origZone:
+ _objc_msgSend$_validateCKObject:isRereference:enhancedDrivePrivacyEnabled:
+ _objc_msgSend$allowAssetReferencesOfMMCSV1Assets
+ _objc_msgSend$dbAge
+ _objc_msgSend$dbCreationDate
+ _objc_msgSend$enhancedDrivePrivacyRolledBack
+ _objc_msgSend$hasDbAge
+ _objc_msgSend$hasIsConsolidated
+ _objc_msgSend$isConsolidated
+ _objc_msgSend$isConsolidatedAccount
+ _objc_msgSend$isReference
+ _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:
+ _objc_msgSend$setDbAge:
+ _objc_msgSend$setIsConsolidated:
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) _daysSinceLastOSUpdate]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) _daysSinceLastOSUpdate].cold.1
- +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:]
- +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:]
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]
- +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:].cold.1
- +[CKRecord(BRCItemAdditions) _validateCKObject:enhancedDrivePrivacyEnabled:]
- +[CKRecord(BRCItemAdditions) _validateCKObject:enhancedDrivePrivacyEnabled:].cold.1
- GCC_except_table150
- GCC_except_table171
- GCC_except_table212
- GCC_except_table214
- GCC_except_table216
- GCC_except_table223
- GCC_except_table236
- GCC_except_table241
- GCC_except_table314
- GCC_except_table437
- GCC_except_table559
- __OBJC_$_INSTANCE_METHODS_AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension)
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.344
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.345
- ___166+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke
- ___166+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke.cold.1
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.505
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.258
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.211
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.212
- ___67+[AppTelemetryTimeSeriesEvent(BRCAdditions) _daysSinceLastOSUpdate]_block_invoke
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.725
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.729
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.727
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.263
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.263.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.265
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.265.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.271
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.275
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.275.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.275.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.657
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.657.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.658
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.661
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.661.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.661.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.663
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.664
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.387
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.387.cold.1
- ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.228
- ___block_descriptor_90_e8_32s40s48s56r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.242
- ___block_literal_global.274
- ___block_literal_global.2827
- ___block_literal_global.343
- ___block_literal_global.352
- ___block_literal_global.360
- ___block_literal_global.377
- ___block_literal_global.393
- ___block_literal_global.398
- ___block_literal_global.403
- ___block_literal_global.408
- ___block_literal_global.413
- ___block_literal_global.418
- ___block_literal_global.423
- ___block_literal_global.428
- ___block_literal_global.436
- ___block_literal_global.441
- ___block_literal_global.446
- ___block_literal_global.486
- ___block_literal_global.750
- ___block_literal_global.933
- ___block_literal_global.941
- _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:
- _objc_msgSend$_registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:
- _objc_msgSend$_validateCKObject:enhancedDrivePrivacyEnabled:
- _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:
CStrings:
+ "\b\x16\x1e\xf0/\x02\x11\x15\x1f\x03"
+ "+[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:]"
+ "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:]"
+ "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]"
+ "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:]_block_invoke"
+ "+[CKRecord(BRCItemAdditions) _validateCKObject:isRereference:enhancedDrivePrivacyEnabled:]"
+ "B64@0:8@16B24@28B36^@40^B48^@56"
+ "B88@0:8@16B24@28@36B44^I48^I56^@64^B72^@80"
+ "SELECT date FROM %@ ORDER BY rowid ASC LIMIT 1"
+ "T@\"NSDate\",R,N,V_dbCreationDate"
+ "[DEBUG] Allowing rereference of mmcsv1 asset%@"
+ "[DEBUG] Allowing rereference of mmcsv1 package%@"
+ "[WARNING] Stripping enhanced drive privacy bit because it was rolled back %@%@"
+ "_checkIntegrity:serverTruth:session:skipControlFiles:dbCreationDate:deviceIDChanged:error:"
+ "_dbAge"
+ "_dbAgeFromDbCreationDate:"
+ "_dbCreationDate"
+ "_isConsolidated"
+ "_registerLastBootIfNeeded:table:skipControlFiles:dbCreationDate:deviceIDChanged:"
+ "_serializeServerSideAssetCopyPluginFieldsForRecord:newZone:origZone:"
+ "_validateCKObject:isRereference:enhancedDrivePrivacyEnabled:"
+ "allowAssetReferencesOfMMCSV1Assets"
+ "br_assetRereference"
+ "consolidate = %s|"
+ "dbAge"
+ "dbAge = %lld|"
+ "dbCreationDate"
+ "enhancedDrivePrivacyRolledBack"
+ "errorDomain = %@|errorCode = %lld|errorDescription = %@|underlyingErrorDomain = %@|underlyingErrorCode = %lld|"
+ "hasDbAge"
+ "hasIsConsolidated"
+ "isConsolidated"
+ "isConsolidatedAccount"
+ "isReference"
+ "lastOSUpdate = %lld|"
+ "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:dbCreationDate:deviceIDChanged:error:"
+ "setDbAge:"
+ "setHasDbAge:"
+ "setHasIsConsolidated:"
+ "setIsConsolidated:"
+ "sync.allow-mmcsv1-asset-references"
+ "sync.enhanced-drive-privacy.rollback"
+ "v52@0:8@16@24B32^@36^B44"
+ "{?=\"dbAge\"b1\"errorCode\"b1\"eventTimestamp\"b1\"lastOSUpdate\"b1\"underlyingErrorCode\"b1\"hasForegroundClients\"b1\"isConsolidated\"b1\"isEnhancedDrivePrivacyEnabled\"b1\"isPCSChained\"b1\"nonDiscretionary\"b1\"sharedZone\"b1}"
- "\b\x15\x1e\xf0/\x02\x11\x15\x1f\x03"
- "+[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:]"
- "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:]"
- "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]"
- "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke"
- "+[CKRecord(BRCItemAdditions) _validateCKObject:enhancedDrivePrivacyEnabled:]"
- "B56@0:8@16B24@28B36^B40^@48"
- "B80@0:8@16B24@28@36B44^I48^I56^B64^@72"
- "O"
- "_checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:"
- "_registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:"
- "_validateCKObject:enhancedDrivePrivacyEnabled:"
- "errorDomain = %@|errorCode = %lld| errorDescription = %@| underlyingErrorDomain = %@| underlyingErrorCode = %lld"
- "lastOSUpdate = %lld"
- "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:"
- "v44@0:8@16@24B32^B36"
- "{?=\"errorCode\"b1\"eventTimestamp\"b1\"lastOSUpdate\"b1\"underlyingErrorCode\"b1\"hasForegroundClients\"b1\"isEnhancedDrivePrivacyEnabled\"b1\"isPCSChained\"b1\"nonDiscretionary\"b1\"sharedZone\"b1}"

```
