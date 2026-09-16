## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-5168.0.55.0.0
-  __TEXT.__text: 0x30103c
-  __TEXT.__objc_methlist: 0x1be50
+5168.40.149.0.1
+  __TEXT.__text: 0x302560
+  __TEXT.__objc_methlist: 0x1c21c
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x829d8
-  __TEXT.__oslogstring: 0x3de76
-  __TEXT.__gcc_except_tab: 0x17800
+  __TEXT.__cstring: 0x845e9
+  __TEXT.__oslogstring: 0x3ee91
+  __TEXT.__gcc_except_tab: 0x17ad8
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xd3f8
+  __TEXT.__unwind_info: 0xd568
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9ed0
-  __DATA_CONST.__objc_classlist: 0xab0
+  __DATA_CONST.__const: 0xa150
+  __DATA_CONST.__objc_classlist: 0xad0
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x2c0
+  __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf170
+  __DATA_CONST.__objc_selrefs: 0xf318
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x960
+  __DATA_CONST.__objc_superrefs: 0x968
   __DATA_CONST.__objc_arraydata: 0xeb8
-  __DATA_CONST.__got: 0x17c0
-  __AUTH_CONST.__const: 0x2cf8
-  __AUTH_CONST.__cfstring: 0x23640
-  __AUTH_CONST.__objc_const: 0x41a50
+  __DATA_CONST.__got: 0x17b8
+  __AUTH_CONST.__const: 0x2d28
+  __AUTH_CONST.__cfstring: 0x23b00
+  __AUTH_CONST.__objc_const: 0x42388
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_got: 0xda0
-  __AUTH.__objc_data: 0x2558
+  __AUTH.__objc_data: 0x2698
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x2030
-  __DATA.__data: 0x29f0
+  __DATA.__objc_ivar: 0x2050
+  __DATA.__data: 0x2ab0
   __DATA_DIRTY.__objc_data: 0x4588
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x428

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14225
-  Symbols:   24561
-  CStrings:  12153
+  Functions: 14323
+  Symbols:   24732
+  CStrings:  12261
 
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
+ GCC_except_table108
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table141
+ GCC_except_table152
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table180
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table207
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table288
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table312
+ GCC_except_table320
+ GCC_except_table324
+ GCC_except_table341
+ GCC_except_table343
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table360
+ GCC_except_table363
+ GCC_except_table366
+ GCC_except_table368
+ GCC_except_table371
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table386
+ GCC_except_table392
+ GCC_except_table397
+ GCC_except_table401
+ GCC_except_table405
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table415
+ GCC_except_table420
+ GCC_except_table429
+ GCC_except_table434
+ GCC_except_table437
+ GCC_except_table439
+ GCC_except_table441
+ GCC_except_table445
+ GCC_except_table451
+ GCC_except_table453
+ GCC_except_table457
+ GCC_except_table468
+ GCC_except_table472
+ GCC_except_table474
+ GCC_except_table478
+ GCC_except_table482
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table490
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table498
+ GCC_except_table500
+ GCC_except_table501
+ OBJC_IVAR_$_BRCLocalItem._uv2MigrationStamp
+ _BRCInsufficientQuotaLCategory
+ _BRCInsufficientQuotaMCategory
+ _BRCInsufficientQuotaSCategory
+ _BRCInsufficientQuotaXSCategory
+ _OBJC_CLASS_$_BRCPQLInjectionIntegerInListBase
+ _OBJC_CLASS_$_BRCPQLInjectionRowIDInList
+ _OBJC_CLASS_$_BRCPQLInjectionZoneRowIDInList
+ _OBJC_CLASS_$_BRCQuotaHandler
+ _OBJC_CLASS_$_BRCUV2MigrationModifyDispatch
+ _OBJC_IVAR_$_BRCAccountSession._quotaUV2Handler
+ _OBJC_IVAR_$_BRCQueryItemInfo._creatorNameComponents
+ _OBJC_IVAR_$_BRCQueryItemInfo._isCreatedByCurrentUser
+ _OBJC_IVAR_$_BRCQueryItemInfo._isSharedFolderSubItem
+ _OBJC_IVAR_$_BRCQueryItemInfo._ownerNameComponents
+ _OBJC_IVAR_$_BRCQuotaHandler._quotaPacer
+ _OBJC_IVAR_$_BRCQuotaHandler._sessionContext
+ _OBJC_IVAR_$_BRCQuotaHandler._workQueue
+ _OBJC_IVAR_$_BRCSyncEngineMigrationManager._phase2DispatchQueue
+ _OBJC_IVAR_$_BRCUV2MigrationModifyDispatch._fileObjectID
+ _OBJC_IVAR_$_BRCUV2MigrationModifyDispatch._parentIdentifier
+ _OBJC_IVAR_$_iCDDeleteItemContext._clientKey
+ _OBJC_METACLASS_$_BRCPQLInjectionIntegerInListBase
+ _OBJC_METACLASS_$_BRCPQLInjectionRowIDInList
+ _OBJC_METACLASS_$_BRCPQLInjectionZoneRowIDInList
+ _OBJC_METACLASS_$_BRCQuotaHandler
+ _OBJC_METACLASS_$_BRCUV2MigrationModifyDispatch
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
+ ___75-[BRCAccountSession(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke_4
+ ___79-[BRCAccountSession zoneHasSyncedDownWithoutError:ownerName:completionHandler:]_block_invoke
+ ___80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]_block_invoke
+ ___80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV1WithFPPendingData:reply:]_block_invoke_2
+ ___80-[BRCXPCRegularIPCsClient _getContainersNeedingUploadV2WithFPPendingData:reply:]_block_invoke
+ ___81-[BRCUserDefaults getBirdBGSTActivitiesConfigsWithAccountFacade:uploadV2Enabled:]_block_invoke
+ ___82-[BRCAccountSession appLibraryRootNeedsCreationForAppLibraryID:completionHandler:]_block_invoke
+ ___88-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]_block_invoke
+ ___88-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]_block_invoke_2
+ ___88-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]_block_invoke_3
+ ___89-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke
+ ___89-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke_2
+ ___93-[BRCReadWriteClientDatabaseFacade nextUV2MigrationBatchItemsAtTime:limit:itemBuilder:error:]_block_invoke
+ ___95-[BRCAccountSession zoneAndAppLibraryRootNeedsCreationForZoneName:ownerName:completionHandler:]_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64s72bs80r88r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8r88l8s72l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96bs_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s112l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88bs96r104r112r120r_e5_v8?0ls32l8r96l8s40l8r104l8s48l8s56l8s64l8r112l8s72l8s80l8r120l8s88l8
+ ___block_descriptor_161_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r136r144r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8ls32l8r104l8r112l8r120l8s40l8r128l8s48l8s56l8s96l8s64l8s72l8s80l8r136l8s88l8r144l8
+ ___block_descriptor_169_e8_32s40s48s56s64s72s80s88s96s104bs112r120r128r136r144r152r_e5_B8?0ls32l8r112l8r120l8r128l8s40l8r136l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8r144l8s96l8r152l8
+ ___block_descriptor_40_e8_32s_e24_v32?0{_NSRange=QQ}8^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"BRCClientDatabaseFacade"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e42_v16?0"BRCReadWriteClientDatabaseFacade"8lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48r_e23_B16?0"PQLConnection"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32bs40r48r56r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28lr40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48r_e5_B8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e42_v16?0"BRCReadWriteClientDatabaseFacade"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e45_B24?0"BRCClientZone"8"NSMutableIndexSet"16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_B8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e20_v24?0Q8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64w_e5_v8?0ls32l8w64l8s40l8s48l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56bs64r72r_e48_v36?0"<NSFileProviderItem>"8Q16B24"NSError"28ls32l8r64l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_98_e8_32s40s48s56s64r72r_e23_B16?0"PQLConnection"8ls32l8r64l8s40l8s48l8s56l8r72l8
+ ___br_update_tables_40_000_cleanup_in_flight_cross_zone_moves_block_invoke
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
- GCC_except_table106
- GCC_except_table110
- GCC_except_table115
- GCC_except_table118
- GCC_except_table133
- GCC_except_table137
- GCC_except_table140
- GCC_except_table142
- GCC_except_table149
- GCC_except_table153
- GCC_except_table166
- GCC_except_table169
- GCC_except_table172
- GCC_except_table175
- GCC_except_table181
- GCC_except_table183
- GCC_except_table187
- GCC_except_table189
- GCC_except_table193
- GCC_except_table199
- GCC_except_table216
- GCC_except_table219
- GCC_except_table221
- GCC_except_table224
- GCC_except_table226
- GCC_except_table229
- GCC_except_table232
- GCC_except_table234
- GCC_except_table235
- GCC_except_table241
- GCC_except_table244
- GCC_except_table247
- GCC_except_table249
- GCC_except_table253
- GCC_except_table255
- GCC_except_table256
- GCC_except_table264
- GCC_except_table265
- GCC_except_table269
- GCC_except_table270
- GCC_except_table273
- GCC_except_table281
- GCC_except_table284
- GCC_except_table285
- GCC_except_table287
- GCC_except_table289
- GCC_except_table291
- GCC_except_table299
- GCC_except_table311
- GCC_except_table319
- GCC_except_table322
- GCC_except_table325
- GCC_except_table327
- GCC_except_table329
- GCC_except_table330
- GCC_except_table332
- GCC_except_table340
- GCC_except_table353
- GCC_except_table358
- GCC_except_table361
- GCC_except_table365
- GCC_except_table369
- GCC_except_table372
- GCC_except_table377
- GCC_except_table387
- GCC_except_table389
- GCC_except_table393
- GCC_except_table402
- GCC_except_table404
- GCC_except_table407
- GCC_except_table408
- GCC_except_table411
- GCC_except_table416
- GCC_except_table421
- GCC_except_table428
- GCC_except_table432
- GCC_except_table435
- GCC_except_table438
- GCC_except_table440
- GCC_except_table444
- GCC_except_table446
- GCC_except_table455
- GCC_except_table465
- GCC_except_table469
- GCC_except_table471
- GCC_except_table473
- GCC_except_table475
- GCC_except_table477
- GCC_except_table481
- GCC_except_table483
- GCC_except_table485
- GCC_except_table487
- GCC_except_table79
- _BRReadOnlyShareUploadErrorCategory
- _OBJC_CLASS_$_BRCInflightSyncProgressRegistry
- _OBJC_IVAR_$_BRCAccountSession._inflightSyncProgressRegistry
- _OBJC_IVAR_$_BRCInflightSyncProgressRegistry._progressesByClientKey
- _OBJC_IVAR_$_BRCInflightSyncProgressRegistry._queue
- _OBJC_IVAR_$_BRCSyncEngineMigrationManager._registeredBGSystemTask
- _OBJC_IVAR_$_BRCSyncEngineMigrationManager._resumed
- _OBJC_METACLASS_$_BRCInflightSyncProgressRegistry
- _OUTLINED_FUNCTION_29
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
- ___58-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]_block_invoke_3
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
- ___block_descriptor_113_e8_32s40s48s56s64s72bs80r88r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8r88l8s72l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_144_e8_32s40s48s56s64s72s80s88bs96r104r112r120r_e5_v8?0ls32l8r96l8s40l8r104l8s48l8s56l8s64l8r112l8s72l8s80l8r120l8s88l8
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r136r144r_e42_v16?0"BRCReadWriteClientDatabaseFacade"8ls32l8r104l8r112l8r120l8s40l8r128l8s48l8s56l8s96l8s64l8s72l8s80l8r136l8s88l8r144l8
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104bs112r120r128r136r144r152r_e5_B8?0ls32l8r112l8r120l8r128l8s40l8r136l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8r144l8s96l8r152l8
- ___block_descriptor_32_e16_B16?0"NSUUID"8l
- ___block_descriptor_40_e8_32s_e16_B16?0"NSUUID"8ls32l8
- ___block_descriptor_72_e8_32s40bs48r56r64r_e17_v16?0"NSError"8lr48l8r56l8r64l8s32l8s40l8
- ___block_descriptor_80_e8_32s40bs48r56r64r72r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28lr48l8r56l8r64l8s32l8r72l8s40l8
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28lr64l8r72l8s32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56bs64r72r_e48_v36?0"<NSFileProviderItem>"8Q16B24"NSError"28ls32l8r64l8s40l8s48l8r72l8s56l8
- ___block_descriptor_97_e8_32s40s48s56s64r72r_e23_B16?0"PQLConnection"8ls32l8r64l8s40l8s48l8s56l8r72l8
- __migrationQueue.migrationQueue
- __migrationQueue.onceToken
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
+ "-[BRCAccountSession __getOrCreateServerZone:newlyCreatedDuringInitialSync:]"
+ "-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:newlyCreatedDuringInitialSync:]"
+ "-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]"
+ "-[BRCAccountSession reviveAndSignalFPForRootItemID:zoneName:ownerName:completionHandler:]_block_invoke_2"
+ "-[BRCClientZone(BRCZoneReset) _rescheduleSuspendedUV2CZMJobsMigratedIntoThisZone]"
+ "-[BRCClientZone(BRCZoneReset) scheduleReset:completionHandler:]_block_invoke_2"
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
+ "B24@?0@\"BRCClientZone\"8@\"NSMutableIndexSet\"16"
+ "CREATE INDEX \"client_items/uv2_migration_pending\" ON client_items (item_uv2_migration_stamp) WHERE item_localsyncupstate IN (10, 11)"
+ "CREATE TEMP TRIGGER child_item_count_notifs  AFTER UPDATE OF visible_child_count ON main.client_items  BEGIN  UPDATE client_items SET item_notifs_rank = bump_notifs_rank_unless_blocked_and_trigger_notifs(old.rowid, item_localsyncupstate, item_notifs_rank)   WHERE old.visible_child_count != new.visible_child_count     AND rowid = old.rowid     AND item_type = 0 ; END"
+ "Can't resolve zone %@ for record ID %@"
+ "DELETE FROM client_items INDEXED BY \"client_items/uv2_migration_pending\" WHERE item_localsyncupstate IN (10, 11)   AND item_uv2_migration_stamp IS NOT NULL   AND item_stat_ckinfo IS NULL   AND item_type NOT IN (0, 4, 9, 10)   AND EXISTS (SELECT 1 FROM client_zones AS cz WHERE cz.zone_owner = \"__defaultOwner__\" AND cz.rowid = client_items.zone_rowid)   AND EXISTS (       SELECT 1 FROM client_items AS p       WHERE p.zone_rowid = client_items.zone_rowid         AND p.item_id = client_items.item_parent_id         AND p.item_localsyncupstate = 10         AND p.item_stat_ckinfo IS NULL)"
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
+ "[DEBUG] Running in sync bubble. Skipping UV1->UV2 Phase 2 BGSystemTask registration%@"
+ "[DEBUG] UV1->UV2 Phase 2: wait for changes under %@ finished with %@%@"
+ "[DEBUG] no database migration required, version is current for this device (db at version %d, cap %d)%@"
+ "[DEBUG] ┏%llx cancelling _quotaUV2Handler...%@"
+ "[DEBUG] ┏%llx draining inflight sync engine tasks...%@"
+ "[ERROR] %@: sandboxed client attempted non-sandboxed access%@"
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
+ "[ERROR] signalErrorResolved for quota category %@ failed: %@%@"
+ "[ERROR] signalErrorResolved for verifyTerms failed: %@%@"
+ "[NOTICE] Matched known-by-server item %@ on a create — preserving its server record so it syncs up as a modification, not a colliding create%@"
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
- "[DEBUG] Running in sync bubble. Not handling sync engine migration%@"
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
