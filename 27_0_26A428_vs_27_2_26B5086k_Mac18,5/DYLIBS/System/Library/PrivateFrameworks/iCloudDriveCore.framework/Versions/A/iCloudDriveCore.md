## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore`

```diff

-5168.0.55.0.0
-  __TEXT.__text: 0x33bea4
-  __TEXT.__objc_methlist: 0x1c018
+5168.40.149.0.1
+  __TEXT.__text: 0x33e38c
+  __TEXT.__objc_methlist: 0x1c3dc
   __TEXT.__const: 0x4f8
-  __TEXT.__cstring: 0x83115
-  __TEXT.__oslogstring: 0x3ec62
-  __TEXT.__gcc_except_tab: 0x17c60
+  __TEXT.__cstring: 0x84ea5
+  __TEXT.__oslogstring: 0x40047
+  __TEXT.__gcc_except_tab: 0x17f90
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xd7b8
+  __TEXT.__unwind_info: 0xd930
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ff0
-  __DATA_CONST.__objc_classlist: 0xac0
+  __DATA_CONST.__const: 0x2040
+  __DATA_CONST.__objc_classlist: 0xae0
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x2a8
+  __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf2c8
+  __DATA_CONST.__objc_selrefs: 0xf468
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x958
+  __DATA_CONST.__objc_superrefs: 0x960
   __DATA_CONST.__objc_arraydata: 0xfd8
-  __DATA_CONST.__got: 0x1818
-  __AUTH_CONST.__const: 0xbc98
-  __AUTH_CONST.__cfstring: 0x23bc0
-  __AUTH_CONST.__objc_const: 0x419a8
+  __DATA_CONST.__got: 0x1810
+  __AUTH_CONST.__const: 0xbf38
+  __AUTH_CONST.__cfstring: 0x240e0
+  __AUTH_CONST.__objc_const: 0x422d8
   __AUTH_CONST.__objc_intobj: 0xc30
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_got: 0xd18
-  __AUTH.__objc_data: 0x25f8
+  __AUTH.__objc_data: 0x2738
   __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0x2058
-  __DATA.__data: 0x28e8
+  __DATA.__objc_ivar: 0x2078
+  __DATA.__data: 0x29a8
   __DATA_DIRTY.__objc_data: 0x4588
   __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0x430

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14522
-  Symbols:   25393
-  CStrings:  12273
+  Functions: 14624
+  Symbols:   25571
+  CStrings:  12401
 
Symbols:
+ +[BRCClientPrivilegesDescriptor isNonSandboxedForAuditToken:]
+ +[BRCItemID appLibraryForBrainItemIDString:zoneName:zoneAppRetriever:clientZone:]
+ +[BRCItemID appLibraryIDForCrossZoneMovedBrainItemIDString:]
+ +[BRCNotification shouldBlockWithUploadV2Enabled:isIdleOrRejected:]
+ +[BRCPQLInjectionIntegerInListBase _injectionFromValues:]
+ +[BRCPQLInjectionIntegerInListBase columnName]
+ +[BRCPQLInjectionJobStates columnName]
+ +[BRCPQLInjectionRowIDInList columnName]
+ +[BRCPQLInjectionZoneRowIDInList columnName]
+ +[BRCServerChangesApplyUtil_Private itemUndergoingCZMToAnotherZone:si:clientZone:rank:scheduler:zone:session:]
+ +[BRCSyncEngineMigrationManager shouldMigrateToUploadV2]
+ -[BRCAccountSession __getOrCreateServerZone:newlyCreatedDuringInitialSync:]
+ -[BRCAccountSession appLibraryRootNeedsCreationForAppLibraryID:completionHandler:]
+ -[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]
+ -[BRCAccountSession quotaHandler]
+ -[BRCAccountSession quotaUV2Handler]
+ -[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]
+ -[BRCAccountSession zoneAndAppLibraryConsolidationFlagsForItemIDString:zoneName:ownerName:completionHandler:]
+ -[BRCAccountSession zoneAndAppLibraryRootNeedsCreationForZoneName:ownerName:completionHandler:]
+ -[BRCAccountSession zoneHasSyncedDownWithoutError:ownerName:completionHandler:]
+ -[BRCAccountSession zoneNeedsCreation:ownerName:completionHandler:]
+ -[BRCClientDatabaseFacade uv2MigrationPendingLiveItemCount:tombstoneItemCount:]
+ -[BRCClientZone lastSyncDownError]
+ -[BRCClientZone(BRCZoneReset) _rescheduleSuspendedUV2CZMJobsMigratedIntoThisZone]
+ -[BRCItemFetcher localItemBuilder]
+ -[BRCLocalItem _insertUploadV2TombstoneForCrossZoneMove]
+ -[BRCLocalItem cacheUV2MigrationStamp:]
+ -[BRCLocalItem clearUV2MigrationStamp]
+ -[BRCLocalItem clearUploadV2ModifyRedirectPending]
+ -[BRCLocalItem isMigratingToUV2]
+ -[BRCLocalItem markUploadV2ModifyRedirectPending]
+ -[BRCLocalItem syncEngineMarkNeedsSyncingUp]
+ -[BRCLocalItem uv2MigrationNeedsReimport]
+ -[BRCLocalItem uv2MigrationStamp]
+ -[BRCLocalStatInfo _clearProcessingStamp]
+ -[BRCNotification shouldBeBlockedInUploadV2]
+ -[BRCPQLInjectionIntegerInListBase initWithIndexSet:]
+ -[BRCPQLInjectionIntegerInListBase initWithValues:]
+ -[BRCQueryItemInfo _populateShareAttributionFromItem:]
+ -[BRCQueryItemInfo creatorNameComponents]
+ -[BRCQueryItemInfo isCreatedByCurrentUser]
+ -[BRCQueryItemInfo isSharedFolderSubItem]
+ -[BRCQueryItemInfo ownerNameComponents]
+ -[BRCQuotaHandler .cxx_destruct]
+ -[BRCQuotaHandler _fetchedWithinPacerWindow]
+ -[BRCQuotaHandler _registerDailyResolutionTask]
+ -[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]
+ -[BRCQuotaHandler _signalResolvedCategoriesForAvailableBytes:]
+ -[BRCQuotaHandler cancel]
+ -[BRCQuotaHandler dealloc]
+ -[BRCQuotaHandler initWithSessionContext:]
+ -[BRCQuotaHandler quotaAvailableForOwner:]
+ -[BRCQuotaHandler scheduleQuotaFetchIfNeededForOwner:]
+ -[BRCReadWriteClientDatabaseFacade hasUV2MigrationRequestedRowsWithError:]
+ -[BRCReadWriteClientDatabaseFacade markUV2MigrationRequestedForRowIDs:retryAt:error:]
+ -[BRCReadWriteClientDatabaseFacade nextUV2MigrationBatchItemsAtTime:limit:itemBuilder:error:]
+ -[BRCReadWriteClientDatabaseFacade stampUV2MigrationChildrenOfParent:error:]
+ -[BRCSyncEngineMigrationManager _dispatchModify:]
+ -[BRCSyncEngineMigrationManager _dispatchReimportForFileObjectID:]
+ -[BRCSyncEngineMigrationManager _dropStrandedMigrationRowForFileObjectID:]
+ -[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]
+ -[BRCSyncEngineMigrationManager _runPhase2BatchWithTask:]
+ -[BRCUV2MigrationModifyDispatch .cxx_destruct]
+ -[BRCUV2MigrationModifyDispatch fileObjectID]
+ -[BRCUV2MigrationModifyDispatch initWithFileObjectID:parentIdentifier:]
+ -[BRCUV2MigrationModifyDispatch parentIdentifier]
+ -[BRCUserDefaults getBirdBGSTActivitiesConfigsWithAccountFacade:uploadV2Enabled:]
+ -[BRCUserDefaults quotaCategoryMUpperBound]
+ -[BRCUserDefaults quotaCategoryResolutionBGSystemTaskConfig]
+ -[BRCUserDefaults quotaCategorySUpperBound]
+ -[BRCUserDefaults quotaCategoryXSUpperBound]
+ -[BRCUserDefaults quotaUV2FetchPacerDelay]
+ -[BRCUserDefaults uv2MigrationBoostPendingDeletions]
+ -[BRCUserDefaults uv2MigrationRequestThrottleInterval]
+ -[BRCXPCRegularIPCsClient _fpHasNonUploadedFilesWithCompletion:]
+ -[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]
+ -[BRCXPCRegularIPCsClient _getContainersNeedingUploadV2WithFPPendingData:reply:]
+ -[BRCXPCRegularIPCsClient _iCloudDriveContainerSet]
+ -[BRCXPCRegularIPCsClient uv2MigrationPendingItemCountWithReply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:backingStoreIdentity:reply:]
+ -[CKRecordID(BRCItemAdditions) _itemIDWithLibraryRowID:zoneAppRetriever:error:]
+ -[iCDDeleteItemContext clientKey]
+ -[iCDDeleteItemContext initWithZoneName:zoneOwner:itemIDString:serverChangeToken:progress:clientKey:]
+ GCC_except_table104
+ GCC_except_table136
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table179
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table210
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table258
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table276
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table283
+ GCC_except_table287
+ GCC_except_table302
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table319
+ GCC_except_table325
+ GCC_except_table327
+ GCC_except_table333
+ GCC_except_table335
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table344
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table349
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table365
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table389
+ GCC_except_table395
+ GCC_except_table399
+ GCC_except_table403
+ GCC_except_table406
+ GCC_except_table413
+ GCC_except_table417
+ GCC_except_table423
+ GCC_except_table425
+ GCC_except_table430
+ GCC_except_table432
+ GCC_except_table437
+ GCC_except_table439
+ GCC_except_table448
+ GCC_except_table456
+ GCC_except_table466
+ GCC_except_table471
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table480
+ GCC_except_table494
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table506
+ GCC_except_table508
+ GCC_except_table512
+ GCC_except_table523
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table531
+ GCC_except_table537
+ GCC_except_table543
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table551
+ GCC_except_table555
+ GCC_except_table557
+ GCC_except_table559
+ GCC_except_table561
+ GCC_except_table562
+ OBJC_IVAR_$_BRCAccountSession._quotaUV2Handler
+ OBJC_IVAR_$_BRCLocalItem._uv2MigrationStamp
+ OBJC_IVAR_$_BRCQueryItemInfo._creatorNameComponents
+ OBJC_IVAR_$_BRCQueryItemInfo._isCreatedByCurrentUser
+ OBJC_IVAR_$_BRCQueryItemInfo._isSharedFolderSubItem
+ OBJC_IVAR_$_BRCQueryItemInfo._ownerNameComponents
+ OBJC_IVAR_$_BRCQuotaHandler._quotaPacer
+ OBJC_IVAR_$_BRCQuotaHandler._sessionContext
+ OBJC_IVAR_$_BRCQuotaHandler._workQueue
+ OBJC_IVAR_$_BRCSyncEngineMigrationManager._phase2DispatchQueue
+ OBJC_IVAR_$_BRCUV2MigrationModifyDispatch._fileObjectID
+ OBJC_IVAR_$_BRCUV2MigrationModifyDispatch._parentIdentifier
+ OBJC_IVAR_$_iCDDeleteItemContext._clientKey
+ _BRCInsufficientQuotaLCategory
+ _BRCInsufficientQuotaMCategory
+ _BRCInsufficientQuotaSCategory
+ _BRCInsufficientQuotaXSCategory
+ _OBJC_CLASS_$_BRCPQLInjectionIntegerInListBase
+ _OBJC_CLASS_$_BRCPQLInjectionRowIDInList
+ _OBJC_CLASS_$_BRCPQLInjectionZoneRowIDInList
+ _OBJC_CLASS_$_BRCQuotaHandler
+ _OBJC_CLASS_$_BRCUV2MigrationModifyDispatch
+ _OBJC_METACLASS_$_BRCPQLInjectionIntegerInListBase
+ _OBJC_METACLASS_$_BRCPQLInjectionRowIDInList
+ _OBJC_METACLASS_$_BRCPQLInjectionZoneRowIDInList
+ _OBJC_METACLASS_$_BRCQuotaHandler
+ _OBJC_METACLASS_$_BRCUV2MigrationModifyDispatch
+ __125-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:backingStoreIdentity:reply:]_block_invoke
+ __138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2
+ __172-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]_block_invoke
+ __172-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]_block_invoke_2
+ __49-[BRCSyncEngineMigrationManager _dispatchModify:]_block_invoke
+ __65-[BRCXPCRegularIPCsClient uv2MigrationPendingItemCountWithReply:]_block_invoke
+ __67-[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]_block_invoke
+ __67-[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]_block_invoke_2
+ __68-[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]_block_invoke
+ __80-[BRCAccountHandler handleiCloudDesktopSettingsChangeWithAttributes:completion:]_block_invoke
+ __80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]_block_invoke
+ __80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV2WithFPPendingData:reply:]_block_invoke
+ __88-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]_block_invoke
+ __89-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke_2
+ __BRCIsInconclusiveDomainMatchingError
+ __OBJC_$_CLASS_METHODS_BRCPQLInjectionIntegerInListBase
+ __OBJC_$_CLASS_METHODS_BRCPQLInjectionRowIDInList
+ __OBJC_$_CLASS_METHODS_BRCPQLInjectionZoneRowIDInList
+ __OBJC_$_INSTANCE_METHODS_BRCPQLInjectionIntegerInListBase
+ __OBJC_$_INSTANCE_METHODS_BRCQuotaHandler
+ __OBJC_$_INSTANCE_METHODS_BRCUV2MigrationModifyDispatch
+ __OBJC_$_INSTANCE_VARIABLES_BRCQuotaHandler
+ __OBJC_$_INSTANCE_VARIABLES_BRCUV2MigrationModifyDispatch
+ __OBJC_$_PROP_LIST_BRCItemFetcher
+ __OBJC_$_PROP_LIST_BRCQuotaHandler
+ __OBJC_$_PROP_LIST_BRCUV2MigrationModifyDispatch
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCQuotaHandling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCUV2MigrationDatabaseWriteProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRCQuotaHandling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRCUV2MigrationDatabaseWriteProtocol
+ __OBJC_$_PROTOCOL_REFS_BRCQuotaHandling
+ __OBJC_$_PROTOCOL_REFS_BRCUV2MigrationDatabaseWriteProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BRCQuotaHandler
+ __OBJC_CLASS_RO_$_BRCPQLInjectionIntegerInListBase
+ __OBJC_CLASS_RO_$_BRCPQLInjectionRowIDInList
+ __OBJC_CLASS_RO_$_BRCPQLInjectionZoneRowIDInList
+ __OBJC_CLASS_RO_$_BRCQuotaHandler
+ __OBJC_CLASS_RO_$_BRCUV2MigrationModifyDispatch
+ __OBJC_LABEL_PROTOCOL_$_BRCQuotaHandling
+ __OBJC_LABEL_PROTOCOL_$_BRCUV2MigrationDatabaseWriteProtocol
+ __OBJC_METACLASS_RO_$_BRCPQLInjectionIntegerInListBase
+ __OBJC_METACLASS_RO_$_BRCPQLInjectionRowIDInList
+ __OBJC_METACLASS_RO_$_BRCPQLInjectionZoneRowIDInList
+ __OBJC_METACLASS_RO_$_BRCQuotaHandler
+ __OBJC_METACLASS_RO_$_BRCUV2MigrationModifyDispatch
+ __OBJC_PROTOCOL_$_BRCQuotaHandling
+ __OBJC_PROTOCOL_$_BRCUV2MigrationDatabaseWriteProtocol
+ ___109-[BRCAccountSession zoneAndAppLibraryConsolidationFlagsForItemIDString:zoneName:ownerName:completionHandler:]_block_invoke
+ ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:backingStoreIdentity:reply:]_block_invoke
+ ___172-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]_block_invoke
+ ___172-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]_block_invoke_2
+ ___26-[BRCXPCClient invalidate]_block_invoke
+ ___42-[BRCQuotaHandler initWithSessionContext:]_block_invoke
+ ___44-[BRCBGSystemTaskManager unregisterAllTasks]_block_invoke
+ ___47-[BRCQuotaHandler _registerDailyResolutionTask]_block_invoke
+ ___47-[BRCQuotaHandler _registerDailyResolutionTask]_block_invoke_2
+ ___47-[BRCQuotaHandler _registerDailyResolutionTask]_block_invoke_3
+ ___49-[BRCSyncEngineMigrationManager _dispatchModify:]_block_invoke
+ ___53-[BRCPQLInjectionIntegerInListBase initWithIndexSet:]_block_invoke
+ ___55-[BRCBGSystemTaskManager unregisterTaskWithIdentifier:]_block_invoke
+ ___57-[BRCSyncEngineMigrationManager _runPhase2BatchWithTask:]_block_invoke
+ ___62-[BRCQuotaHandler _signalResolvedCategoriesForAvailableBytes:]_block_invoke
+ ___64-[BRCXPCRegularIPCsClient _fpHasNonUploadedFilesWithCompletion:]_block_invoke
+ ___65-[BRCXPCRegularIPCsClient uv2MigrationPendingItemCountWithReply:]_block_invoke
+ ___66-[BRCSyncEngineMigrationManager _dispatchReimportForFileObjectID:]_block_invoke
+ ___67-[BRCAccountSession zoneNeedsCreation:ownerName:completionHandler:]_block_invoke
+ ___67-[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]_block_invoke
+ ___67-[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]_block_invoke_2
+ ___68-[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]_block_invoke
+ ___68-[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]_block_invoke_2
+ ___74-[BRCSyncEngineMigrationManager _dropStrandedMigrationRowForFileObjectID:]_block_invoke
+ ___75-[BRCAccountSession(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke_3
+ ___79-[BRCAccountSession zoneHasSyncedDownWithoutError:ownerName:completionHandler:]_block_invoke
+ ___80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]_block_invoke
+ ___80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]_block_invoke_2
+ ___80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV2WithFPPendingData:reply:]_block_invoke
+ ___81-[BRCUserDefaults getBirdBGSTActivitiesConfigsWithAccountFacade:uploadV2Enabled:]_block_invoke
+ ___82-[BRCAccountSession appLibraryRootNeedsCreationForAppLibraryID:completionHandler:]_block_invoke
+ ___88-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]_block_invoke
+ ___89-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke
+ ___89-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke_2
+ ___93-[BRCReadWriteClientDatabaseFacade nextUV2MigrationBatchItemsAtTime:limit:itemBuilder:error:]_block_invoke
+ ___95-[BRCAccountSession zoneAndAppLibraryRootNeedsCreationForZoneName:ownerName:completionHandler:]_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64s72bs80r88r_e5_v8?0l
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96bs_e23_B16?0"PQLConnection"8l
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0l
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88bs96r104r112r120r_e5_v8?0l
+ ___block_descriptor_161_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r136r144r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8l
+ ___block_descriptor_169_e8_32s40s48s56s64s72s80s88s96s104bs112r120r128r136r144r152r_e5_B8?0l
+ ___block_descriptor_40_e8_32s_e24_v32?0{_NSRange=QQ}8^B24l
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"BRCClientDatabaseFacade"8l
+ ___block_descriptor_48_e8_32s40w_e42_v16?0"BRCReadWriteClientDatabaseFacade"8l
+ ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32bs40r48r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28l
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8l
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48r_e23_B16?0"PQLConnection"8l
+ ___block_descriptor_64_e8_32bs40r48r56r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28l
+ ___block_descriptor_64_e8_32s40s48r_e5_B8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e42_v16?0"BRCReadWriteClientDatabaseFacade"8l
+ ___block_descriptor_64_e8_32s40s48s56r_e45_B24?0"BRCClientZone"8"NSMutableIndexSet"16l
+ ___block_descriptor_64_e8_32s40s48s56r_e5_B8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e20_v24?0Q8"NSError"16l
+ ___block_descriptor_89_e8_32s40s48s56bs64r72r_e48_v36?0"<NSFileProviderItem>"8Q16B24"NSError"28l
+ ___block_descriptor_98_e8_32s40s48s56s64r72r_e23_B16?0"PQLConnection"8l
+ ___br_update_tables_40_000_cleanup_in_flight_cross_zone_moves_block_invoke
+ ___copy_helper_block_e8_32b40r48r56r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112b
+ ___destroy_helper_block_e8_32s40r48r56r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s
+ __br_update_tables_40_000_cleanup_in_flight_cross_zone_moves_block_invoke
+ _br_update_tables_40_000
+ _objc_msgSend$__getOrCreateServerZone:newlyCreatedDuringInitialSync:
+ _objc_msgSend$_createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:
+ _objc_msgSend$_dispatchModify:
+ _objc_msgSend$_dispatchReimportForFileObjectID:
+ _objc_msgSend$_dropStrandedMigrationRowForFileObjectID:
+ _objc_msgSend$_fetchedWithinPacerWindow
+ _objc_msgSend$_fpHasNonUploadedFilesWithCompletion:
+ _objc_msgSend$_getContainersNeedingUploadV1WithFPPendingData:reply:
+ _objc_msgSend$_getContainersNeedingUploadV2WithFPPendingData:reply:
+ _objc_msgSend$_iCloudDriveContainerSet
+ _objc_msgSend$_injectionFromValues:
+ _objc_msgSend$_insertUploadV2TombstoneForCrossZoneMove
+ _objc_msgSend$_itemIDWithLibraryRowID:zoneAppRetriever:error:
+ _objc_msgSend$_populateShareAttributionFromItem:
+ _objc_msgSend$_processPhase2BatchOnWorkloop:task:
+ _objc_msgSend$_registerDailyResolutionTask
+ _objc_msgSend$_rescheduleSuspendedUV2CZMJobsMigratedIntoThisZone
+ _objc_msgSend$_resolveQuotaCategoriesIfPossibleWithCompletion:
+ _objc_msgSend$_runPhase2BatchWithTask:
+ _objc_msgSend$_signalResolvedCategoriesForAvailableBytes:
+ _objc_msgSend$appLibraryForBrainItemIDString:zoneName:zoneAppRetriever:clientZone:
+ _objc_msgSend$appLibraryIDForCrossZoneMovedBrainItemIDString:
+ _objc_msgSend$br_appHasNonUploadedFiles:completion:
+ _objc_msgSend$cacheUV2MigrationStamp:
+ _objc_msgSend$cancelAndDeleteOperationsForZoneReset:ownerName:completionHandler:
+ _objc_msgSend$cancelAndWaitForAllOperationsWithCompletionHandler:
+ _objc_msgSend$cancelOperationsForClientKey:completionHandler:
+ _objc_msgSend$clearUV2MigrationStamp
+ _objc_msgSend$clearUploadV2ModifyRedirectPending
+ _objc_msgSend$columnName
+ _objc_msgSend$creatorNameComponents
+ _objc_msgSend$enumerateRangesUsingBlock:
+ _objc_msgSend$getBirdBGSTActivitiesConfigsWithAccountFacade:uploadV2Enabled:
+ _objc_msgSend$getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:
+ _objc_msgSend$hasUV2MigrationRequestedRowsWithError:
+ _objc_msgSend$indexSet
+ _objc_msgSend$initWithFileObjectID:parentIdentifier:
+ _objc_msgSend$initWithIndexSet:
+ _objc_msgSend$initWithReserverItemIDString:reservedFileProviderIdentifier:parentZoneName:parentZoneOwner:parentIDString:symlinkTarget:parentShareState:shareRootItemIdentifierString:parentPCSChainState:parentSharePermissions:initialItem:resetItem:isInDocumentScope:trashPutBackPath:trashPutbackItemIDString:progress:clientKey:
+ _objc_msgSend$initWithResetItem:forceParentShared:zoneName:zoneOwner:itemIDString:parentZoneName:parentZoneOwner:parentIDString:isInDocumentScope:trashPutBackPath:trashPutbackItemIDString:progress:clientKey:
+ _objc_msgSend$initWithValues:
+ _objc_msgSend$initWithZoneName:zoneOwner:itemIDString:serverChangeToken:progress:clientKey:
+ _objc_msgSend$isCreatedByCurrentUser
+ _objc_msgSend$isMigratingToUV2
+ _objc_msgSend$isNonSandboxedForAuditToken:
+ _objc_msgSend$isSharedFolderSubItem
+ _objc_msgSend$itemUndergoingCZMToAnotherZone:si:clientZone:rank:scheduler:zone:session:
+ _objc_msgSend$localItemBuilder
+ _objc_msgSend$markUV2MigrationRequestedForRowIDs:retryAt:error:
+ _objc_msgSend$markUploadV2ModifyRedirectPending
+ _objc_msgSend$nextUV2MigrationBatchItemsAtTime:limit:itemBuilder:error:
+ _objc_msgSend$parentIdentifier
+ _objc_msgSend$quotaCategoryMUpperBound
+ _objc_msgSend$quotaCategoryResolutionBGSystemTaskConfig
+ _objc_msgSend$quotaCategorySUpperBound
+ _objc_msgSend$quotaCategoryXSUpperBound
+ _objc_msgSend$quotaHandler
+ _objc_msgSend$quotaUV2FetchPacerDelay
+ _objc_msgSend$quotaUV2Handler
+ _objc_msgSend$setBackingStoreIdentity:
+ _objc_msgSend$shouldBeBlockedInUploadV2
+ _objc_msgSend$shouldBlockWithUploadV2Enabled:isIdleOrRejected:
+ _objc_msgSend$stampUV2MigrationChildrenOfParent:error:
+ _objc_msgSend$syncEngineMarkNeedsSyncingUp
+ _objc_msgSend$uv2MigrationBoostPendingDeletions
+ _objc_msgSend$uv2MigrationNeedsReimport
+ _objc_msgSend$uv2MigrationPendingLiveItemCount:tombstoneItemCount:
+ _objc_msgSend$uv2MigrationRequestThrottleInterval
+ _objc_msgSend$uv2MigrationStamp
+ br_update_tables_40_000
- +[BRCClientPrivilegesDescriptor _isNonSandboxedForAuditToken:]
- +[BRCPQLInjectionJobStates _getPQLInjectionFromJobStates:]
- +[BRCServerChangesApplyUtil_Private itemUndergoingCZMToAnotherZone:si:clientZone:rank:scheduler:zone:]
- +[BRCSyncEngineMigrationManager _migrationQueue]
- -[BRCAccountSession hasSyncedDownZoneSinceStartup:ownerName:completionHandler:]
- -[BRCAccountSession(BRCDatabaseManager) clientDBExistsOnDisk]
- -[BRCAccountSession(FPFSAdditions) inflightSyncProgressRegistry]
- -[BRCInflightSyncProgressRegistry .cxx_destruct]
- -[BRCInflightSyncProgressRegistry _cancelAndRemoveProgressesMatchingPredicate:]
- -[BRCInflightSyncProgressRegistry cancelProgressesExcludingClientKey:]
- -[BRCInflightSyncProgressRegistry cancelProgressesForClientKey:]
- -[BRCInflightSyncProgressRegistry close]
- -[BRCInflightSyncProgressRegistry createProgressForClientKey:]
- -[BRCInflightSyncProgressRegistry dumpToContext:]
- -[BRCInflightSyncProgressRegistry init]
- -[BRCInflightSyncProgressRegistry unregisterProgress:forClientKey:]
- -[BRCLocalItem _shouldBlockNotifForUploadV2WithDiffs:]
- -[BRCPQLInjectionJobStates initWithJobStates:]
- -[BRCSyncEngineMigrationManager _cancel]
- -[BRCSyncEngineMigrationManager _isSyncEngineIdleWithDBFacade:]
- -[BRCSyncEngineMigrationManager _markUsageUploadV2SyncEngine:]
- -[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]
- -[BRCSyncEngineMigrationManager markUsageUploadV2SyncEngineForNewDatabaseIfNeeded]
- -[BRCSyncEngineMigrationManager shouldMigrateToUploadV2]
- -[BRCUserDefaults getBirdBGSTActivitiesConfigsWithAccountFacade:]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) _cancelObsoleteSyncEngineRequests]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) _createInflightSyncProgress]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]
- -[CKRecordID(BRCItemAdditions) _itemIDWithLibraryRowID:zoneAppRetriever:]
- -[iCDDeleteItemContext initWithZoneName:zoneOwner:itemIDString:serverChangeToken:progress:]
- GCC_except_table118
- GCC_except_table129
- GCC_except_table135
- GCC_except_table141
- GCC_except_table144
- GCC_except_table151
- GCC_except_table153
- GCC_except_table158
- GCC_except_table164
- GCC_except_table167
- GCC_except_table175
- GCC_except_table180
- GCC_except_table186
- GCC_except_table189
- GCC_except_table192
- GCC_except_table195
- GCC_except_table197
- GCC_except_table199
- GCC_except_table206
- GCC_except_table209
- GCC_except_table211
- GCC_except_table216
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table234
- GCC_except_table237
- GCC_except_table241
- GCC_except_table245
- GCC_except_table247
- GCC_except_table249
- GCC_except_table252
- GCC_except_table254
- GCC_except_table257
- GCC_except_table259
- GCC_except_table261
- GCC_except_table263
- GCC_except_table265
- GCC_except_table266
- GCC_except_table272
- GCC_except_table273
- GCC_except_table278
- GCC_except_table280
- GCC_except_table282
- GCC_except_table284
- GCC_except_table293
- GCC_except_table297
- GCC_except_table299
- GCC_except_table305
- GCC_except_table309
- GCC_except_table311
- GCC_except_table314
- GCC_except_table315
- GCC_except_table320
- GCC_except_table322
- GCC_except_table324
- GCC_except_table326
- GCC_except_table336
- GCC_except_table351
- GCC_except_table354
- GCC_except_table356
- GCC_except_table360
- GCC_except_table363
- GCC_except_table364
- GCC_except_table366
- GCC_except_table371
- GCC_except_table382
- GCC_except_table390
- GCC_except_table397
- GCC_except_table400
- GCC_except_table405
- GCC_except_table408
- GCC_except_table412
- GCC_except_table420
- GCC_except_table424
- GCC_except_table428
- GCC_except_table435
- GCC_except_table438
- GCC_except_table440
- GCC_except_table458
- GCC_except_table462
- GCC_except_table467
- GCC_except_table472
- GCC_except_table474
- GCC_except_table477
- GCC_except_table481
- GCC_except_table484
- GCC_except_table493
- GCC_except_table495
- GCC_except_table499
- GCC_except_table501
- GCC_except_table510
- GCC_except_table518
- GCC_except_table521
- GCC_except_table524
- GCC_except_table530
- GCC_except_table532
- GCC_except_table536
- GCC_except_table538
- GCC_except_table542
- GCC_except_table544
- GCC_except_table546
- GCC_except_table548
- OBJC_IVAR_$_BRCAccountSession._inflightSyncProgressRegistry
- OBJC_IVAR_$_BRCInflightSyncProgressRegistry._progressesByClientKey
- OBJC_IVAR_$_BRCInflightSyncProgressRegistry._queue
- OBJC_IVAR_$_BRCSyncEngineMigrationManager._registeredBGSystemTask
- OBJC_IVAR_$_BRCSyncEngineMigrationManager._resumed
- _BRReadOnlyShareUploadErrorCategory
- _OBJC_CLASS_$_BRCInflightSyncProgressRegistry
- _OBJC_METACLASS_$_BRCInflightSyncProgressRegistry
- _OUTLINED_FUNCTION_29
- __104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke
- __143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke
- __143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke_2
- __58-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]_block_invoke
- __62-[BRCInflightSyncProgressRegistry createProgressForClientKey:]_block_invoke
- __74-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]_block_invoke
- __74-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]_block_invoke_2
- __OBJC_$_INSTANCE_METHODS_BRCInflightSyncProgressRegistry
- __OBJC_$_INSTANCE_METHODS_BRCPQLInjectionJobStates
- __OBJC_$_INSTANCE_VARIABLES_BRCInflightSyncProgressRegistry
- __OBJC_CLASS_RO_$_BRCInflightSyncProgressRegistry
- __OBJC_METACLASS_RO_$_BRCInflightSyncProgressRegistry
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke
- ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke
- ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke_2
- ___39-[BRCSyncEngineMigrationManager cancel]_block_invoke
- ___40-[BRCInflightSyncProgressRegistry close]_block_invoke
- ___48+[BRCSyncEngineMigrationManager _migrationQueue]_block_invoke
- ___49-[BRCInflightSyncProgressRegistry dumpToContext:]_block_invoke
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke_2
- ___58-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]_block_invoke
- ___58-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]_block_invoke_2
- ___62-[BRCInflightSyncProgressRegistry createProgressForClientKey:]_block_invoke
- ___63-[BRCSyncEngineMigrationManager _isSyncEngineIdleWithDBFacade:]_block_invoke
- ___64-[BRCInflightSyncProgressRegistry cancelProgressesForClientKey:]_block_invoke
- ___65-[BRCUserDefaults getBirdBGSTActivitiesConfigsWithAccountFacade:]_block_invoke
- ___67-[BRCInflightSyncProgressRegistry unregisterProgress:forClientKey:]_block_invoke
- ___70-[BRCInflightSyncProgressRegistry cancelProgressesExcludingClientKey:]_block_invoke
- ___74-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]_block_invoke
- ___74-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]_block_invoke_2
- ___79-[BRCAccountSession hasSyncedDownZoneSinceStartup:ownerName:completionHandler:]_block_invoke
- ___79-[BRCInflightSyncProgressRegistry _cancelAndRemoveProgressesMatchingPredicate:]_block_invoke
- ___block_descriptor_113_e8_32s40s48s56s64s72bs80r88r_e5_v8?0l
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e23_B16?0"PQLConnection"8l
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0l
- ___block_descriptor_144_e8_32s40s48s56s64s72s80s88bs96r104r112r120r_e5_v8?0l
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r136r144r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8l
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104bs112r120r128r136r144r152r_e5_B8?0l
- ___block_descriptor_32_e16_B16?0"NSUUID"8l
- ___block_descriptor_40_e8_32s_e16_B16?0"NSUUID"8l
- ___block_descriptor_72_e8_32s40bs48r56r64r_e17_v16?0"NSError"8l
- ___block_descriptor_80_e8_32s40bs48r56r64r72r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28l
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28l
- ___block_descriptor_88_e8_32s40s48s56bs64r72r_e48_v36?0"<NSFileProviderItem>"8Q16B24"NSError"28l
- ___block_descriptor_97_e8_32s40s48s56s64r72r_e23_B16?0"PQLConnection"8l
- ___copy_helper_block_e8_32s40b48r56r64r
- ___copy_helper_block_e8_32s40b48r56r64r72r
- _migrationQueue.migrationQueue
- _migrationQueue.onceToken
- _objc_msgSend$_cancel
- _objc_msgSend$_cancelAndRemoveProgressesMatchingPredicate:
- _objc_msgSend$_cancelObsoleteSyncEngineRequests
- _objc_msgSend$_createInflightSyncProgress
- _objc_msgSend$_getPQLInjectionFromJobStates:
- _objc_msgSend$_isNonSandboxedForAuditToken:
- _objc_msgSend$_isSyncEngineIdleWithDBFacade:
- _objc_msgSend$_itemIDWithLibraryRowID:zoneAppRetriever:
- _objc_msgSend$_markUsageUploadV2SyncEngine:
- _objc_msgSend$_migrationQueue
- _objc_msgSend$_performSyncEngineMigrationCheckWithTask:
- _objc_msgSend$_shouldBlockNotifForUploadV2WithDiffs:
- _objc_msgSend$cancelProgressesExcludingClientKey:
- _objc_msgSend$cancelProgressesForClientKey:
- _objc_msgSend$clientDBExistsOnDisk
- _objc_msgSend$createProgressForClientKey:
- _objc_msgSend$flushWithCheckpoint:performOnSerialQueue:
- _objc_msgSend$getBirdBGSTActivitiesConfigsWithAccountFacade:
- _objc_msgSend$hasNonIdleItemsForSyncEngineMigration
- _objc_msgSend$inflightSyncProgressRegistry
- _objc_msgSend$initWithJobStates:
- _objc_msgSend$initWithReserverItemIDString:reservedFileProviderIdentifier:parentZoneName:parentZoneOwner:parentIDString:primaryZoneNeedsCreation:appLibraryRootNeedsCreation:appLibraryIsConsolidated:symlinkTarget:parentShareState:shareRootItemIdentifierString:parentPCSChainState:parentSharePermissions:initialItem:resetItem:isInDocumentScope:trashPutBackPath:trashPutbackItemIDString:progress:
- _objc_msgSend$initWithResetItem:forceParentShared:zoneName:zoneOwner:itemIDString:parentZoneNeedsCreation:appLibraryRootNeedsCreation:appLibraryIsConsolidated:parentZoneName:parentZoneOwner:parentIDString:isInDocumentScope:trashPutBackPath:trashPutbackItemIDString:progress:
- _objc_msgSend$initWithZoneName:zoneOwner:itemIDString:serverChangeToken:progress:
- _objc_msgSend$itemUndergoingCZMToAnotherZone:si:clientZone:rank:scheduler:zone:
- _objc_msgSend$markUsageUploadV2SyncEngineForNewDatabaseIfNeeded
- _objc_msgSend$unregisterProgress:forClientKey:
CStrings:
+ " and rescheduling its apply from server truth"
+ " uv2-reimport"
+ " uv2-stamp:%lld%s"
+ "#"
+ "%@ = %@"
+ "%@ IN (%@"
+ "+[BRCPQLInjectionIntegerInListBase columnName]"
+ "+[BRCServerChangesApplyUtil_Private itemUndergoingCZMToAnotherZone:si:clientZone:rank:scheduler:zone:session:]"
+ "-[BRCAccountHandler handleiCloudDesktopSettingsChangeWithAttributes:completion:]_block_invoke"
+ "-[BRCAccountSession __getOrCreateServerZone:newlyCreatedDuringInitialSync:]"
+ "-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]"
+ "-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]"
+ "-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke_2"
+ "-[BRCAccountSession(FPFSAdditions) setEnabled:forDesktopAndDocumentsWithCompletion:]"
+ "-[BRCClientZone(BRCZoneReset) _rescheduleSuspendedUV2CZMJobsMigratedIntoThisZone]"
+ "-[BRCDesktopAndDocumentsManager resume]"
+ "-[BRCDesktopAndDocumentsManager setEnabled:forDesktopAndDocumentsWithCompletion:]"
+ "-[BRCLocalItem _insertTombstoneForCrossZoneMove:]"
+ "-[BRCLocalItem _insertUploadV2TombstoneForCrossZoneMove]"
+ "-[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]_block_invoke"
+ "-[BRCQuotaHandler _resolveQuotaCategoriesIfPossibleWithCompletion:]_block_invoke_2"
+ "-[BRCQuotaHandler _signalResolvedCategoriesForAvailableBytes:]_block_invoke"
+ "-[BRCSyncEngineMigrationManager _dispatchModify:]_block_invoke"
+ "-[BRCSyncEngineMigrationManager _dispatchReimportForFileObjectID:]_block_invoke"
+ "-[BRCSyncEngineMigrationManager _dropStrandedMigrationRowForFileObjectID:]_block_invoke"
+ "-[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]"
+ "-[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]_block_invoke"
+ "-[BRCSyncEngineMigrationManager _processPhase2BatchOnWorkloop:task:]_block_invoke_2"
+ "-[BRCXPCRegularIPCsClient _fpHasNonUploadedFilesWithCompletion:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV2WithFPPendingData:reply:]"
+ "-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV2WithFPPendingData:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient uv2MigrationPendingItemCountWithReply:]"
+ "-[BRCXPCRegularIPCsClient uv2MigrationPendingItemCountWithReply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:progress:fromModifyRedirect:completionHandler:]_block_invoke_2"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:backingStoreIdentity:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:backingStoreIdentity:reply:]_block_invoke"
+ "-[CKRecordID(BRCItemAdditions) _itemIDWithLibraryRowID:zoneAppRetriever:error:]"
+ "ALTER TABLE client_items RENAME COLUMN item_transfer_priority TO item_uv2_migration_stamp"
+ "Account handler is unavailable"
+ "Account session is unavailable"
+ "B24@?0@\"BRCClientZone\"8@\"NSMutableIndexSet\"16"
+ "CREATE INDEX \"client_items/uv2_migration_pending\" ON client_items (item_uv2_migration_stamp) WHERE item_localsyncupstate IN (10, 11)"
+ "CREATE TEMP TRIGGER child_item_count_notifs  AFTER UPDATE OF visible_child_count ON main.client_items  BEGIN  UPDATE client_items SET item_notifs_rank = bump_notifs_rank_unless_blocked_and_trigger_notifs(old.rowid, item_localsyncupstate, item_notifs_rank)   WHERE old.visible_child_count != new.visible_child_count     AND rowid = old.rowid     AND item_type = 0 ; END"
+ "CREATE TEMP TRIGGER recursive_notifs  AFTER UPDATE OF dir_faults_count, uploaded_size,needs_upload_size, uploaded_count,needs_upload_count, synced_up_count,needs_sync_up_count, over_quota_count, shared_by_me_count, shared_to_me_count, needs_delete_doc_count ON main.item_recursive_properties  BEGIN  SELECT trigger_notification(old.item_rowid) ;  UPDATE client_items SET item_notifs_rank = bump_notifs_rank_unless_blocked(item_localsyncupstate, item_notifs_rank)  WHERE rowid = old.item_rowid ; END"
+ "Can't resolve zone %@ for record ID %@"
+ "DELETE FROM client_items INDEXED BY \"client_items/uv2_migration_pending\" WHERE item_localsyncupstate IN (10, 11)   AND item_uv2_migration_stamp IS NOT NULL   AND item_stat_ckinfo IS NULL   AND item_type NOT IN (0, 4, 9, 10)   AND EXISTS (SELECT 1 FROM client_zones AS cz WHERE cz.zone_owner = \"__defaultOwner__\" AND cz.rowid = client_items.zone_rowid)   AND EXISTS (       SELECT 1 FROM client_items AS p       WHERE p.zone_rowid = client_items.zone_rowid         AND p.item_id = client_items.item_parent_id         AND p.item_localsyncupstate = 10         AND p.item_stat_ckinfo IS NULL)"
+ "Desktop and documents manager is unavailable"
+ "SELECT 1 FROM client_sync_up WHERE throttle_id = %llu AND %@"
+ "SELECT COALESCE(SUM(item_state = 0), 0), COALESCE(SUM(item_state IN (1, -3)), 0) FROM client_items WHERE item_localsyncupstate IN (10, 11)"
+ "SELECT DISTINCT version_old_zone_rowid FROM client_items WHERE zone_rowid = %@ AND version_old_zone_rowid IS NOT NULL"
+ "SELECT DISTINCT zone_rowid, version_old_zone_rowid FROM client_items INDEXED BY \"client_items/version_old_zone_rowid\" WHERE version_old_zone_rowid IS NOT NULL   AND item_state = 0"
+ "SELECT EXISTS (SELECT 1 FROM client_items WHERE item_localsyncupstate IN (10, 11)   AND item_uv2_migration_stamp IS NOT NULL LIMIT 1)"
+ "SELECT item_uv2_migration_stamp FROM client_items WHERE rowid = %lld"
+ "SELECT rowid, zone_rowid, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_parent_zone_rowid, item_localsyncupstate, item_local_diffs, item_notifs_rank, app_library_rowid, item_min_supported_os_rowid, item_user_visible, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, item_processing_stamp, item_bouncedname, item_scope, item_local_change_count, item_old_version_identifier, fp_creation_item_identifier, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, version_uploaded_assets, version_upload_error, version_old_zone_item_id, version_old_zone_rowid, version_local_change_count, version_old_version_identifier, item_live_conflict_loser_etags, item_file_id, item_generation, item_uv2_migration_stamp FROM client_items WHERE item_localsyncupstate IN (10, 11)   AND item_uv2_migration_stamp IS NOT NULL   AND item_processing_stamp IS NULL   AND (item_localsyncupstate = 10        OR item_uv2_migration_stamp BETWEEN %lld AND %lld) ORDER BY item_uv2_migration_stamp ASC LIMIT %lu"
+ "UPDATE client_items AS ci SET item_stat_ckinfo = si.item_stat_ckinfo FROM server_items AS si WHERE si.item_id = ci.item_id   AND ci.item_stat_ckinfo IS NULL   AND ci.item_type NOT IN (0, 4, 9, 10)   AND EXISTS (SELECT 1 FROM client_zones AS cz WHERE cz.zone_owner = \"__defaultOwner__\" AND cz.rowid = ci.zone_rowid)"
+ "UPDATE client_items INDEXED BY \"client_items/uv2_migration_pending\" SET item_uv2_migration_stamp = NULL WHERE item_localsyncupstate IN (10, 11)   AND item_uv2_migration_stamp IS NOT NULL   AND item_stat_ckinfo IS NULL   AND EXISTS (SELECT 1 FROM client_zones AS cz WHERE cz.zone_owner = \"__defaultOwner__\" AND cz.rowid = client_items.zone_rowid)   AND EXISTS (       SELECT 1 FROM client_items AS p       WHERE p.zone_rowid = client_items.zone_rowid         AND p.item_id = client_items.item_parent_id         AND p.item_localsyncupstate = 10         AND p.item_stat_ckinfo IS NULL)"
+ "UPDATE client_items INDEXED BY \"client_items/version_old_zone_rowid\" SET version_old_zone_item_id = NULL, version_old_zone_rowid = NULL, item_stat_ckinfo = call_block(%p, item_stat_ckinfo), version_ckinfo = call_block(%p, version_ckinfo) WHERE version_old_zone_rowid IS NOT NULL AND (%@)"
+ "UPDATE client_items SET item_localsyncupstate = 10, item_uv2_migration_stamp = (CASE WHEN item_stat_ckinfo IS NULL     AND zone_rowid IN (SELECT rowid FROM client_zones WHERE zone_owner = \"__defaultOwner__\")   THEN -1 ELSE 1 END) WHERE item_state = 0 AND item_localsyncupstate IN (2, 3, 4, 7, 8) AND NOT item_id_is_documents(item_id) AND NOT (%@)"
+ "UPDATE client_items SET item_localsyncupstate = 11 ,   item_uv2_migration_stamp = (CASE WHEN item_uv2_migration_stamp < 0 THEN %lld ELSE %lld END) WHERE %@"
+ "UPDATE client_items SET item_uv2_migration_stamp = 1 WHERE item_parent_id = %@ AND item_parent_zone_rowid = %@   AND item_localsyncupstate = 10   AND item_uv2_migration_stamp IS NULL"
+ "UPDATE client_items SET item_uv2_migration_stamp = NULL WHERE rowid = %lld"
+ "Upload V2 is not enabled; no migration pending count available"
+ "[CRIT] Assertion failed: !li.isMigratingToUV2%@"
+ "[CRIT] Assertion failed: BRCurrentPersonaMatchesID(personaIdentifier)%@"
+ "[CRIT] Assertion failed: db_version <= cap%@"
+ "[CRIT] Assertion failed: zoneResolvedIfNeeded%@"
+ "[CRIT] UNREACHABLE: No previous global ID to leave a cross-zone move tombstone for on %@%@"
+ "[CRIT] UNREACHABLE: Should not get here in uploadv2%@"
+ "[CRIT] UNREACHABLE: Should not get into this code path in uploadv2%@"
+ "[DEBUG] Draining sync engine tasks on zone %@%@"
+ "[DEBUG] FP reports everything uploaded, %@ live items and %@ tombstones still pending UV2 migration%@"
+ "[DEBUG] FileProvider domain supportsBackgroundUpload (%@) is out of sync with shouldMigrateToUploadV2 (%d).%@"
+ "[DEBUG] Postponing apply of UV2 modify-redirected item %@ pending server confirmation%@"
+ "[DEBUG] Rescheduling CZM-suspended jobs in %@ for items migrated into %@%@"
+ "[DEBUG] UV1->UV2 Phase 2: wait for changes under %@ finished with %@%@"
+ "[DEBUG] no database migration required, version is current for this device (db at version %d, cap %d)%@"
+ "[DEBUG] ┏%llx cancelling _quotaUV2Handler...%@"
+ "[DEBUG] ┏%llx draining inflight sync engine tasks...%@"
+ "[ERROR] %@: sandboxed client attempted non-sandboxed access%@"
+ "[ERROR] Can't handle iCloud Desktop settings change: account handler is nil%@"
+ "[ERROR] Can't handle iCloud Desktop settings change: session is nil%@"
+ "[ERROR] Can't set desktop and documents enabled: desktop and documents manager is nil%@"
+ "[ERROR] Failed to ask FP whether %@ has non-uploaded files, assuming it does: %@%@"
+ "[ERROR] UV1->UV2 Phase 2: failed to check for migration-requested rows: %@ — keeping BGSystemTask registered%@"
+ "[ERROR] UV1->UV2 Phase 2: failed to fetch migration batch: %@ — keeping BGSystemTask registered%@"
+ "[ERROR] UV1->UV2 Phase 2: failed to stamp children of %@, keeping the migration row: %@%@"
+ "[ERROR] UV1->UV2 Phase 2: failed to transition %lu rows to NEEDS_UV2_MIGRATION_REQUESTED: %@ — rolling back savepoint%@"
+ "[ERROR] UV1->UV2 Phase 2: reimport failed for %@, will retry: %@%@"
+ "[ERROR] UV1->UV2 Phase 2: requestModification failed for %@, will retry: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: ckinfo backfill failed: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to clear cross-zone-move state on shared-to-me items: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to clear stamps on directory not-known descendants: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to create the migration-pending index: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to delete non-directory not-known descendants: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to look up zones with an in-flight cross-zone move: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to mark live items as NEEDS_UV2_MIGRATION: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to mark zone %@ for reset: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to persist migration flag in client state: %@%@"
+ "[ERROR] UV1->UV2 schema upgrade: failed to rename item_transfer_priority to item_uv2_migration_stamp: %@%@"
+ "[ERROR] failed to adopt persona for quota category resolution: %@%@"
+ "[ERROR] iCloud Desktop settings change failed - %@%@"
+ "[ERROR] signalErrorResolved for quota category %@ failed: %@%@"
+ "[ERROR] signalErrorResolved for verifyTerms failed: %@%@"
+ "[INFO] iCloud Desktop settings change requested: desktop=%@ documents=%@%@"
+ "[NOTICE] D&D enablement change completed: %@ (error: %@)%@"
+ "[NOTICE] Enqueuing D&D enablement change: %@%@"
+ "[NOTICE] Forwarding iCloud Desktop settings change to account handler%@"
+ "[NOTICE] Handling iCloud Desktop settings change: desktop=%@ documents=%@%@"
+ "[NOTICE] Matched known-by-server item %@ on a create — preserving its server record so it syncs up as a modification, not a colliding create%@"
+ "[NOTICE] Rejecting iCloud Desktop settings change: session is data separated%@"
+ "[NOTICE] Resuming desktop and documents manager (restricted: %@)%@"
+ "[NOTICE] Setting D&D enabled: %@%@"
+ "[NOTICE] Setting desktop and documents enabled: %@ (manager: %@)%@"
+ "[NOTICE] Sync: leaving %@ to the UV1->UV2 migration instead of acking request:%llu%@"
+ "[NOTICE] UV1->UV2 Phase 2: batch empty, future-retry pending — keeping BGSystemTask registered%@"
+ "[NOTICE] UV1->UV2 Phase 2: deferring modify of known item %@ — parent %@ is a not-yet-created migration boundary, leaving it for the parent's reimport%@"
+ "[NOTICE] UV1->UV2 Phase 2: processed %lu items, dispatching %lu modify and %lu reimport calls%@"
+ "[NOTICE] UV1->UV2 Phase 2: queue drained, unregistering BGSystemTask%@"
+ "[NOTICE] UV1->UV2 Phase 2: reimport reported no such item for %@ — deferring the drop, %@ promoted child row(s) must drain first%@"
+ "[NOTICE] UV1->UV2 Phase 2: requestModification reported no such item for %@ — boost disabled, leaving the row queued for the pending delete%@"
+ "[NOTICE] UV1->UV2 Phase 2: requestModification reported no such item for %@ — its deletion is pending in FP, waiting for changes under %@%@"
+ "[NOTICE] UV1->UV2 Phase 2: requestModification reported no such item for %@ — no parent to wait on, leaving the row queued%@"
+ "[NOTICE] UV1->UV2 schema upgrade: backfilled CKInfo on %lld client_items rows from server truth%@"
+ "[NOTICE] UV1->UV2 schema upgrade: cleared cross-zone-move state on %lld shared-to-me items%@"
+ "[NOTICE] UV1->UV2 schema upgrade: cleared migration stamps on %lld directory not-known descendants%@"
+ "[NOTICE] UV1->UV2 schema upgrade: deleted %lld non-directory not-known descendants%@"
+ "[NOTICE] UV1->UV2 schema upgrade: marked %lld live items as NEEDS_UV2_MIGRATION%@"
+ "[NOTICE] UV1->UV2 schema upgrade: scheduled a reset on %lu zone(s) out of %lu zone(s) with an in-flight cross-zone move%@"
+ "[NOTICE] createItem matched known-by-server item %@ — handling as a modification to avoid a colliding create%@"
+ "[NOTICE] iCloud Desktop settings change applied: desktop=%@ documents=%@%@"
+ "[NOTICE] iCloud Desktop settings change completed but handler was deallocated%@"
+ "[NOTICE] modifyItem for not-known-by-server directory %@ — failing retriably, the migration reimport owns its subtree%@"
+ "[NOTICE] modifyItem for not-known-by-server item %@ — redirecting to createItemBasedOnTemplate as a fresh upload%@"
+ "[WARNING] Ignoring domain matching error caused by an XPC connection failure: %@%@"
+ "[WARNING] Rescheduling %@ for re-apply without dropping the row%@"
+ "[WARNING] UV1->UV2 Phase 2: batch row failed to hydrate, skipping%@"
+ "[WARNING] UV1->UV2 Phase 2: reimport reported no such item for %@ — dropping the migration row%s%@"
+ "[WARNING] failed to fetch quota for category resolution: %@%@"
+ "_BRCIsInconclusiveDomainMatchingError"
+ "br_update_tables_40_000"
+ "br_update_tables_40_000_cleanup_in_flight_cross_zone_moves"
+ "br_update_tables_40_000_cleanup_in_flight_cross_zone_moves_block_invoke"
+ "br_update_tables_40_000_prepare_columns_and_index"
+ "br_update_tables_40_000_queue_items_for_migration"
+ "br_update_tables_40_000_unqueue_not_known_descendants"
+ "bump_notifs_rank_unless_blocked"
+ "bump_notifs_rank_unless_blocked_and_trigger_notifs"
+ "client_items/uv2_migration_pending"
+ "com.apple.bird.quota-category-resolution"
+ "com.apple.bird.quota.handler"
+ "com.apple.bird.uv2-migration.phase2-dispatch"
+ "insufficientQuotaL"
+ "insufficientQuotaM"
+ "insufficientQuotaS"
+ "insufficientQuotaXS"
+ "item-record-perms"
+ "m-uv2-modify-redirect"
+ "needs-uv2-migration"
+ "needs-uv2-migration-requested"
+ "quota.category-resolution.bgst"
+ "quota.category.m-upper-bound"
+ "quota.category.s-upper-bound"
+ "quota.category.xs-upper-bound"
+ "quotaHandlerLastKnownAvailableQuota"
+ "readOnlyShareUpload"
+ "rowid"
+ "sync.quota.uv2-fetch-delay"
+ "throttle_state"
+ "uv2-migration-boost-pending-deletions"
+ "uv2-migration-request-throttle"
+ "v32@?0{_NSRange=QQ}8^B24"
+ "verifyTerms"
+ "zone_rowid"
- "%@ -> %lu"
- "+[BRCPQLInjectionJobStates _getPQLInjectionFromJobStates:]"
- "+[BRCServerChangesApplyUtil_Private itemUndergoingCZMToAnotherZone:si:clientZone:rank:scheduler:zone:]"
- "-[BRCAccountSession __getOrCreateServerZone:]"
- "-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]"
- "-[BRCInflightSyncProgressRegistry cancelProgressesForClientKey:]"
- "-[BRCInflightSyncProgressRegistry close]"
- "-[BRCInflightSyncProgressRegistry createProgressForClientKey:]"
- "-[BRCInflightSyncProgressRegistry createProgressForClientKey:]_block_invoke"
- "-[BRCSyncEngineMigrationManager _isSyncEngineIdleWithDBFacade:]"
- "-[BRCSyncEngineMigrationManager _isSyncEngineIdleWithDBFacade:]_block_invoke"
- "-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]"
- "-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]_block_invoke"
- "-[BRCSyncEngineMigrationManager _performSyncEngineMigrationCheckWithTask:]_block_invoke_2"
- "-[BRCSyncEngineMigrationManager markUsageUploadV2SyncEngineForNewDatabaseIfNeeded]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke_2"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke"
- "-[CKRecordID(BRCItemAdditions) _itemIDWithLibraryRowID:zoneAppRetriever:]"
- "AND throttle_state = %@"
- "AND throttle_state IN (%@"
- "B16@?0@\"NSUUID\"8"
- "CREATE TEMP TRIGGER child_item_count_notifs  AFTER UPDATE OF visible_child_count ON main.client_items  BEGIN  UPDATE client_items SET item_notifs_rank = bump_notifs_rank_and_trigger_notifs(old.rowid)   WHERE old.visible_child_count != new.visible_child_count     AND rowid = old.rowid     AND item_type = 0 ; END"
- "CREATE TEMP TRIGGER recursive_notifs  AFTER UPDATE OF dir_faults_count, uploaded_size,needs_upload_size, uploaded_count,needs_upload_count, synced_up_count,needs_sync_up_count, over_quota_count, shared_by_me_count, shared_to_me_count, needs_delete_doc_count ON main.item_recursive_properties  BEGIN  SELECT trigger_notification(old.item_rowid) ;  UPDATE client_items SET item_notifs_rank = bump_notifs_rank()  WHERE rowid = old.item_rowid ; END"
- "Inflight Progress Registry:"
- "SELECT 1 FROM client_sync_up WHERE throttle_id = %llu %@"
- "[CRIT] Assertion failed: db_version == DB_VERSION_CURRENT%@"
- "[CRIT] Assertion failed: libraryRowID || sharedZoneRowID || !([identifier isEqualToString:BRCItemIDZoneRoot] || [identifier isEqualToString:BRCItemIDDocuments])%@"
- "[CRIT] Assertion failed: progresses.count <= kBRCInflightSyncProgressRegistryCapacityPerClient%@"
- "[CRIT] UNREACHABLE: Can't register a nil clientKey%@"
- "[CRIT] UNREACHABLE: jobStates is not expected to be empty%@"
- "[DEBUG] Cancelling progress for client with key %@%@"
- "[DEBUG] Closing BRCInflightSyncProgressRegistry%@"
- "[DEBUG] FileProvider domain supportsBackgroundUpload (%@) is out of sync with isSyncEngineMigrated (%d).%@"
- "[DEBUG] Not doing a database migration on an offline database where the major version matches%@"
- "[DEBUG] Setting D&D enabled: %@%@"
- "[DEBUG] Should not migrate to upload v2 yet%@"
- "[DEBUG] We created a new Client DB and we should migrate to upload v2. Migrating to upload v2 now%@"
- "[DEBUG] no database migration required, version is current (db at version %d)%@"
- "[DEBUG] ┏%llx closing _inflightSyncProgressRegistry...%@"
- "[ERROR] Failed adopting persona and run the sync engine migration check: %@%@"
- "[NOTICE] exiting in order to start again with clean sync engine after migration%@"
- "[WARNING] Found non idle items, not migrating to upload v2 yet%@"
- "[WARNING] Task expired while waiting to run on the client truth workloop%@"
- "com.apple.bird.sync-engine.progress-registry"
- "sync-engine-migration-manager"
```
