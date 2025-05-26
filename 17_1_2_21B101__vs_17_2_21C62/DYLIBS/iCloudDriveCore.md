## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-2461.40.47.0.0
-  __TEXT.__text: 0x2b3d40
+2461.62.1.0.0
+  __TEXT.__text: 0x2bcb90
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x1550c
+  __TEXT.__objc_methlist: 0x15d24
   __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x706b3
-  __TEXT.__oslogstring: 0x36e25
-  __TEXT.__gcc_except_tab: 0x1305c
+  __TEXT.__cstring: 0x716a6
+  __TEXT.__oslogstring: 0x36f60
+  __TEXT.__gcc_except_tab: 0x1304c
   __TEXT.__ustring: 0x2be
-  __TEXT.__unwind_info: 0x7f90
-  __TEXT.__objc_classname: 0x2070
-  __TEXT.__objc_methname: 0x372e5
-  __TEXT.__objc_methtype: 0x6a06
-  __TEXT.__objc_stubs: 0x26ae0
-  __DATA_CONST.__got: 0xaf0
-  __DATA_CONST.__const: 0x7d50
+  __TEXT.__unwind_info: 0x8018
+  __TEXT.__objc_classname: 0x2075
+  __TEXT.__objc_methname: 0x39e5b
+  __TEXT.__objc_methtype: 0x70d5
+  __TEXT.__objc_stubs: 0x27760
+  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__const: 0x7de8
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x30438
-  __DATA_CONST.__objc_selrefs: 0xc2b8
+  __DATA_CONST.__objc_const: 0x30dd0
+  __DATA_CONST.__objc_selrefs: 0xc838
   __DATA_CONST.__objc_arraydata: 0xe80
-  __AUTH_CONST.__cfstring: 0x1f340
-  __AUTH_CONST.__objc_const: 0x62b0
-  __AUTH_CONST.__const: 0x2360
-  __AUTH_CONST.__objc_intobj: 0xb88
+  __AUTH_CONST.__cfstring: 0x1f940
+  __AUTH_CONST.__objc_const: 0x62f8
+  __AUTH_CONST.__const: 0x23b0
+  __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__auth_got: 0xda0
-  __AUTH.__objc_data: 0x2710
+  __AUTH.__objc_data: 0x2760
   __AUTH.__data: 0x18
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xc80
+  __DATA.__objc_classrefs: 0xc88
   __DATA.__objc_superrefs: 0x778
-  __DATA.__objc_ivar: 0x1bbc
+  __DATA.__objc_ivar: 0x1c54
   __DATA.__data: 0x1e08
-  __DATA.__bss: 0x210
-  __DATA_DIRTY.__objc_data: 0x2ad0
+  __DATA.__bss: 0x230
+  __DATA_DIRTY.__objc_data: 0x2a80
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x2e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12717
-  Symbols:   38129
-  CStrings:  20467
+  Functions: 12920
+  Symbols:   38687
+  CStrings:  20782
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newContentPolicyProblemCountWithProblemCount:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newCorruptSharingOptionsProblemWithProblemCount:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) nonMigratedItemInvestigationWithFoundInfo:]
+ +[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:]
+ +[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:].cold.1
+ +[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:].cold.2
+ +[BRFieldContentSignature(BRAdditions) localEditCounterFromVersionIdentifier:]
+ -[AppTelemetryFPFSMigrationInvestigation durationBetweenDbCreationAndMigrationStart]
+ -[AppTelemetryFPFSMigrationInvestigation hasDurationBetweenDbCreationAndMigrationStart]
+ -[AppTelemetryFPFSMigrationInvestigation hasIsStreamResetRunning]
+ -[AppTelemetryFPFSMigrationInvestigation hasNumberOfItemsPendingReconciliation]
+ -[AppTelemetryFPFSMigrationInvestigation hasNumberOfItemsPendingScanningDisk]
+ -[AppTelemetryFPFSMigrationInvestigation hasNumberOfItemsPendingScanningProvider]
+ -[AppTelemetryFPFSMigrationInvestigation hasNumberOfItemsPendingSelection]
+ -[AppTelemetryFPFSMigrationInvestigation hasStateOfDownloadJobs]
+ -[AppTelemetryFPFSMigrationInvestigation hasStateOfOtherJobs]
+ -[AppTelemetryFPFSMigrationInvestigation hasStateOfUploadJobs]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityDasdContext]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityIsActive]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityRegisteredWithDuet]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityTimeSinceLastActivation]
+ -[AppTelemetryFPFSMigrationInvestigation hasXpcActivityTimeSinceLastRegistration]
+ -[AppTelemetryFPFSMigrationInvestigation isStreamResetRunning]
+ -[AppTelemetryFPFSMigrationInvestigation numberOfItemsPendingReconciliation]
+ -[AppTelemetryFPFSMigrationInvestigation numberOfItemsPendingScanningDisk]
+ -[AppTelemetryFPFSMigrationInvestigation numberOfItemsPendingScanningProvider]
+ -[AppTelemetryFPFSMigrationInvestigation numberOfItemsPendingSelection]
+ -[AppTelemetryFPFSMigrationInvestigation setDurationBetweenDbCreationAndMigrationStart:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasDurationBetweenDbCreationAndMigrationStart:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasIsStreamResetRunning:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasNumberOfItemsPendingReconciliation:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasNumberOfItemsPendingScanningDisk:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasNumberOfItemsPendingScanningProvider:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasNumberOfItemsPendingSelection:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasStateOfDownloadJobs:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasStateOfOtherJobs:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasStateOfUploadJobs:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityDasdContext:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityIsActive:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityRegisteredWithDuet:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityTimeSinceLastActivation:]
+ -[AppTelemetryFPFSMigrationInvestigation setHasXpcActivityTimeSinceLastRegistration:]
+ -[AppTelemetryFPFSMigrationInvestigation setIsStreamResetRunning:]
+ -[AppTelemetryFPFSMigrationInvestigation setNumberOfItemsPendingReconciliation:]
+ -[AppTelemetryFPFSMigrationInvestigation setNumberOfItemsPendingScanningDisk:]
+ -[AppTelemetryFPFSMigrationInvestigation setNumberOfItemsPendingScanningProvider:]
+ -[AppTelemetryFPFSMigrationInvestigation setNumberOfItemsPendingSelection:]
+ -[AppTelemetryFPFSMigrationInvestigation setStateOfDownloadJobs:]
+ -[AppTelemetryFPFSMigrationInvestigation setStateOfOtherJobs:]
+ -[AppTelemetryFPFSMigrationInvestigation setStateOfUploadJobs:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityDasdContext:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityIsActive:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityRegisteredWithDuet:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityTimeSinceLastActivation:]
+ -[AppTelemetryFPFSMigrationInvestigation setXpcActivityTimeSinceLastRegistration:]
+ -[AppTelemetryFPFSMigrationInvestigation stateOfDownloadJobs]
+ -[AppTelemetryFPFSMigrationInvestigation stateOfOtherJobs]
+ -[AppTelemetryFPFSMigrationInvestigation stateOfUploadJobs]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityDasdContext]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityIsActive]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityRegisteredWithDuet]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityTimeSinceLastActivation]
+ -[AppTelemetryFPFSMigrationInvestigation xpcActivityTimeSinceLastRegistration]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasStuckStatus]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setStuckStatus:]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) stuckStatus]
+ -[AppTelemetryStuckStatus copyTo:]
+ -[AppTelemetryStuckStatus copyWithZone:]
+ -[AppTelemetryStuckStatus description]
+ -[AppTelemetryStuckStatus dictionaryRepresentation]
+ -[AppTelemetryStuckStatus hasItemPendingReconciliationIsLockedInDB]
+ -[AppTelemetryStuckStatus hasItemPendingReconciliationIsLocked]
+ -[AppTelemetryStuckStatus hasItemPendingReconciliationJobBlockingCode]
+ -[AppTelemetryStuckStatus hasItemPendingReconciliationJobCode]
+ -[AppTelemetryStuckStatus hasItemPendingReconciliationJobSchedulingState]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskEnumerationStatus]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskHasMultiplePagesEnumeration]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingReconciliation]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingRejection]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingSyncDown]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent]
+ -[AppTelemetryStuckStatus hasItemPendingScanningDiskNumberOfChildrenPendingSyncUp]
+ -[AppTelemetryStuckStatus hasItemPendingScanningProviderEnumerationStatus]
+ -[AppTelemetryStuckStatus hasItemPendingScanningProviderHasMultiplePagesEnumeration]
+ -[AppTelemetryStuckStatus hasItemPendingScanningProviderNumberOfChildrenFailingCreation]
+ -[AppTelemetryStuckStatus hasItemPendingScanningProviderNumberOfChildrenPendingCreation]
+ -[AppTelemetryStuckStatus hasItemPendingScanningProviderNumberOfChildren]
+ -[AppTelemetryStuckStatus hasItemPendingScanningProviderRemovalOfDatalessBitStatus]
+ -[AppTelemetryStuckStatus hash]
+ -[AppTelemetryStuckStatus isEqual:]
+ -[AppTelemetryStuckStatus itemPendingReconciliationIsLockedInDB]
+ -[AppTelemetryStuckStatus itemPendingReconciliationIsLocked]
+ -[AppTelemetryStuckStatus itemPendingReconciliationJobBlockingCode]
+ -[AppTelemetryStuckStatus itemPendingReconciliationJobCode]
+ -[AppTelemetryStuckStatus itemPendingReconciliationJobSchedulingState]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskEnumerationStatus]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskHasMultiplePagesEnumeration]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingReconciliation]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingRejection]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingSyncDown]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent]
+ -[AppTelemetryStuckStatus itemPendingScanningDiskNumberOfChildrenPendingSyncUp]
+ -[AppTelemetryStuckStatus itemPendingScanningProviderEnumerationStatus]
+ -[AppTelemetryStuckStatus itemPendingScanningProviderHasMultiplePagesEnumeration]
+ -[AppTelemetryStuckStatus itemPendingScanningProviderNumberOfChildrenFailingCreation]
+ -[AppTelemetryStuckStatus itemPendingScanningProviderNumberOfChildrenPendingCreation]
+ -[AppTelemetryStuckStatus itemPendingScanningProviderNumberOfChildren]
+ -[AppTelemetryStuckStatus itemPendingScanningProviderRemovalOfDatalessBitStatus]
+ -[AppTelemetryStuckStatus mergeFrom:]
+ -[AppTelemetryStuckStatus readFrom:]
+ -[AppTelemetryStuckStatus setHasItemPendingReconciliationIsLocked:]
+ -[AppTelemetryStuckStatus setHasItemPendingReconciliationIsLockedInDB:]
+ -[AppTelemetryStuckStatus setHasItemPendingReconciliationJobBlockingCode:]
+ -[AppTelemetryStuckStatus setHasItemPendingReconciliationJobCode:]
+ -[AppTelemetryStuckStatus setHasItemPendingReconciliationJobSchedulingState:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskEnumerationStatus:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskHasMultiplePagesEnumeration:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingReconciliation:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingRejection:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingSyncDown:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingSyncUp:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningProviderEnumerationStatus:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningProviderHasMultiplePagesEnumeration:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningProviderNumberOfChildren:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningProviderNumberOfChildrenFailingCreation:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningProviderNumberOfChildrenPendingCreation:]
+ -[AppTelemetryStuckStatus setHasItemPendingScanningProviderRemovalOfDatalessBitStatus:]
+ -[AppTelemetryStuckStatus setItemPendingReconciliationIsLocked:]
+ -[AppTelemetryStuckStatus setItemPendingReconciliationIsLockedInDB:]
+ -[AppTelemetryStuckStatus setItemPendingReconciliationJobBlockingCode:]
+ -[AppTelemetryStuckStatus setItemPendingReconciliationJobCode:]
+ -[AppTelemetryStuckStatus setItemPendingReconciliationJobSchedulingState:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskEnumerationStatus:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskHasMultiplePagesEnumeration:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingReconciliation:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingRejection:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingSyncDown:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingSyncUp:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:]
+ -[AppTelemetryStuckStatus setItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:]
+ -[AppTelemetryStuckStatus setItemPendingScanningProviderEnumerationStatus:]
+ -[AppTelemetryStuckStatus setItemPendingScanningProviderHasMultiplePagesEnumeration:]
+ -[AppTelemetryStuckStatus setItemPendingScanningProviderNumberOfChildren:]
+ -[AppTelemetryStuckStatus setItemPendingScanningProviderNumberOfChildrenFailingCreation:]
+ -[AppTelemetryStuckStatus setItemPendingScanningProviderNumberOfChildrenPendingCreation:]
+ -[AppTelemetryStuckStatus setItemPendingScanningProviderRemovalOfDatalessBitStatus:]
+ -[AppTelemetryStuckStatus writeTo:]
+ -[BRCAccountHandler _handleOpenError:].cold.8
+ -[BRCAccountSessionFPFS _recoverAndReportBrokenShareOptions]
+ -[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]
+ -[BRCAccountSessionFPFS _recoverAndReportStateIntegrityWithCompletion:]
+ -[BRCAccountSessionFPFS _recoverAndReportStateIntegrityWithCompletion:].cold.1
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) _decorateFPFSDomainUserInfoWithError:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) _decorateFPFSDomainUserInfoWithError:].cold.1
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) reimportFPFSDomainWithError:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _sendItemsPendingReconciliation:event:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _sendItemsPendingScanningDisk:event:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _sendItemsPendingScanningProvider:event:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _sendTelemetryEventForPendingItemsWithFPReport:migrationUUID:daysSinceImportStarted:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _sendTelemetryEventWithDiagnosticAttributes:event:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _shouldTriggerTapToRadar:itemsNotMigrated:reconciledItems:]
+ -[BRCDocumentItem shouldBeGreedy].cold.1
+ -[BRCFPImportReport fpReport]
+ -[BRCFPImportReport setFpReport:]
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.1
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.2
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.3
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.4
+ -[BRCFSImporter _parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:]
+ -[BRCFSImporter _parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:].cold.1
+ -[BRCFSImporter _parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:].cold.2
+ -[BRCFSUploader _fileForUploadExistsInStage:record:]
+ -[BRCPQLConnection scheduleFlushWithCheckpoint:whenFlushed:]
+ -[BRCRTCReporter _processReportingBatch]
+ -[BRCUserDefaults dbIntegrityCheckMissingShareOptions]
+ -[BRCUserDefaults dumpDateFormat]
+ -[BRCUserDefaults dumpDateFormatter]
+ -[BRCUserDefaults integrityCheckContentPolicy]
+ -[BRCUserDefaults migrationStatusPendingItemsTelemetryLimit]
+ -[BRCUserDefaults telemetryRTCPacerMinFireInterval]
+ -[BRFieldContentSignature(BRCItemAdditions) _initWithVersionIdentifier:size:contentSignature:]
+ -[BRFieldContentSignature(BRCItemAdditions) equivalentVersions]
+ GCC_except_table118
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table151
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table183
+ GCC_except_table190
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table216
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table246
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table332
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table342
+ GCC_except_table346
+ GCC_except_table350
+ GCC_except_table354
+ GCC_except_table359
+ GCC_except_table364
+ GCC_except_table375
+ GCC_except_table378
+ GCC_except_table380
+ GCC_except_table385
+ GCC_except_table388
+ GCC_except_table399
+ GCC_except_table403
+ GCC_except_table406
+ GCC_except_table411
+ GCC_except_table415
+ GCC_except_table419
+ GCC_except_table422
+ GCC_except_table439
+ GCC_except_table441
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table448
+ GCC_except_table451
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._durationBetweenDbCreationAndMigrationStart
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._isStreamResetRunning
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._numberOfItemsPendingReconciliation
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._numberOfItemsPendingScanningDisk
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._numberOfItemsPendingScanningProvider
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._numberOfItemsPendingSelection
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._stateOfDownloadJobs
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._stateOfOtherJobs
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._stateOfUploadJobs
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._xpcActivityDasdContext
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._xpcActivityIsActive
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._xpcActivityRegisteredWithDuet
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._xpcActivityTimeSinceLastActivation
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationInvestigation._xpcActivityTimeSinceLastRegistration
+ OBJC_IVAR_$_AppTelemetryInvestigation._stuckStatus
+ OBJC_IVAR_$_AppTelemetryStuckStatus._has
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingReconciliationIsLocked
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingReconciliationIsLockedInDB
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingReconciliationJobBlockingCode
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingReconciliationJobCode
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingReconciliationJobSchedulingState
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskEnumerationStatus
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskHasMultiplePagesEnumeration
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingReconciliation
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingRejection
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingSyncDown
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingSyncUp
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningProviderEnumerationStatus
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningProviderHasMultiplePagesEnumeration
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningProviderNumberOfChildren
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningProviderNumberOfChildrenFailingCreation
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningProviderNumberOfChildrenPendingCreation
+ OBJC_IVAR_$_AppTelemetryStuckStatus._itemPendingScanningProviderRemovalOfDatalessBitStatus
+ OBJC_IVAR_$_BRCLocalVersion._localChangeCount
+ OBJC_IVAR_$_BRCLocalVersion._oldVersionIdentifier
+ OBJC_IVAR_$_BRCLocalVersion._previousItemGlobalID
+ OBJC_IVAR_$_BRCLocalVersion._uploadError
+ OBJC_IVAR_$_BRCLocalVersion._uploadedAssets
+ OBJC_IVAR_$_BRQueryItem._equivalentContentVersions
+ _AppTelemetryStuckStatusReadFrom
+ _BRDomainDatabaseIDKey
+ _OBJC_CLASS_$_AppTelemetryStuckStatus
+ _OBJC_CLASS_$_BRDeviceConfiguration
+ _OBJC_IVAR_$_BRCFPImportReport._fpReport
+ _OBJC_IVAR_$_BRCRTCReporter._events
+ _OBJC_IVAR_$_BRCRTCReporter._pacerQueue
+ _OBJC_IVAR_$_BRCRTCReporter._reportingPacer
+ _OBJC_METACLASS_$_AppTelemetryStuckStatus
+ __OBJC_$_CLASS_METHODS_BRFieldContentSignature(BRAdditions|BRCItemAdditions)
+ __OBJC_$_INSTANCE_METHODS_AppTelemetryStuckStatus
+ __OBJC_$_INSTANCE_VARIABLES_AppTelemetryStuckStatus
+ __OBJC_$_PROP_LIST_AppTelemetryStuckStatus
+ __OBJC_CLASS_PROTOCOLS_$_AppTelemetryStuckStatus
+ __OBJC_CLASS_RO_$_AppTelemetryStuckStatus
+ __OBJC_METACLASS_RO_$_AppTelemetryStuckStatus
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.456
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.456.cold.1
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.460
+ ___102-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke.662
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.61
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.61.cold.1
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.63
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.65
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.68
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.68.cold.1
+ ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.638
+ ___112-[BRCSideCarSyncUpOperation _syncUpRecordBatchWithModifiedRecords:deletedRecordIDs:recordIDToZoneMap:requestID:]_block_invoke.13
+ ___112-[BRCSideCarSyncUpOperation _syncUpRecordBatchWithModifiedRecords:deletedRecordIDs:recordIDToZoneMap:requestID:]_block_invoke_2
+ ___115-[BRCXPCRegularIPCsClient(FPFSAdditions) getDefaultAppContainerItemForContainerID:recreateDocumentsIfNeeded:reply:]_block_invoke.27
+ ___115-[BRCXPCRegularIPCsClient(FPFSAdditions) getDefaultAppContainerItemForContainerID:recreateDocumentsIfNeeded:reply:]_block_invoke_2
+ ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.416
+ ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.417
+ ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.73
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.29
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.31
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.31.cold.1
+ ___188-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]_block_invoke
+ ___188-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]_block_invoke.68
+ ___30-[BRCAccountSessionFPFS close]_block_invoke.262
+ ___36-[BRCUserDefaults dumpDateFormatter]_block_invoke
+ ___38-[BRCNotification subclassDescription]_block_invoke
+ ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.286
+ ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.286.cold.1
+ ___42-[BRCAppLibrary _activateState:origState:]_block_invoke.30
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.231
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.234
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.247
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.233
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.233.cold.1
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.235
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.235.cold.1
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_3.239
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.320
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.320.cold.1
+ ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.448
+ ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.329
+ ___48-[BRCRTCReporter initWithFPRTCReportingSession:]_block_invoke
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.2
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.3
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.4
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.294
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.294.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.297
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.309
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.309.cold.1
+ ___51-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]_block_invoke.657
+ ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke.167
+ ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.412
+ ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.413
+ ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.498
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.414
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.415
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.441
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.442
+ ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.391
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.169
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.169.cold.1
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.170
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.177
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.177.cold.1
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.178
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke_2.179
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.706
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.707
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.362
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.363
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.652
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.652.cold.1
+ ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.278
+ ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.280
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.215
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.224
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.227
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.338
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.339
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.459
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.459.cold.1
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.469
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.423
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.424
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440.cold.1
+ ___60-[BRCAccountSessionFPFS _recoverAndReportBrokenShareOptions]_block_invoke
+ ___60-[BRCPQLConnection scheduleFlushWithCheckpoint:whenFlushed:]_block_invoke
+ ___60-[BRCPQLConnection scheduleFlushWithCheckpoint:whenFlushed:]_block_invoke_2
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.606
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.606.cold.1
+ ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.600
+ ___62-[BRCXPCRegularIPCsClient logoutAccountWithACAccountID:reply:]_block_invoke.439
+ ___62-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke.683
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.324
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.325
+ ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke
+ ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke.45
+ ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke.46
+ ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.390
+ ___65-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke.13
+ ___65-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke_2
+ ___65-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke_2.cold.1
+ ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.289
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.647
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.647.cold.1
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.647.cold.2
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.648
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.608
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.609
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.611
+ ___67-[BRCXPCRegularIPCsClient _presentAcceptDialogsWithMetadata:reply:]_block_invoke.650
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.428
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.428.cold.1
+ ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.322
+ ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.293
+ ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.416
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke.193
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke.195
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_2
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_2.194
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_2.cold.1
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_3
+ ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.403
+ ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.403.cold.1
+ ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.403.cold.2
+ ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.406
+ ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.406.cold.1
+ ___71-[BRCAccountSessionFPFS _recoverAndReportStateIntegrityWithCompletion:]_block_invoke
+ ___71-[BRCAccountSessionFPFS _recoverAndReportStateIntegrityWithCompletion:]_block_invoke_2
+ ___71-[BRCAccountSessionFPFS _recoverAndReportStateIntegrityWithCompletion:]_block_invoke_3
+ ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.656
+ ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.643
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.75
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.78
+ ___72+[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:]_block_invoke
+ ___72+[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:]_block_invoke.cold.1
+ ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.602
+ ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.595
+ ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.417
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.397
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.397.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.398
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.398.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.399
+ ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.651
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.364
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.379
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.570
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.572
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.615
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.617
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.392
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.392.cold.1
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.392.cold.2
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.393
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.393.cold.1
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.612
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.613
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.604
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.604.cold.1
+ ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.568
+ ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.598
+ ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.421
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.1
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.2
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.3
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.4
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke_2
+ ___80-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPFSImportFinishedTelemetryEvent]_block_invoke.172
+ ___80-[BRCFSImporter _parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:]_block_invoke
+ ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.565
+ ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.317
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.443
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.444
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.634
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.569
+ ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.636
+ ___82-[BRCAccountSessionFPFS(BRCDatabaseManager) _decorateFPFSDomainUserInfoWithError:]_block_invoke
+ ___82-[BRCAccountSessionFPFS(BRCDatabaseManager) _decorateFPFSDomainUserInfoWithError:]_block_invoke.cold.1
+ ___82-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke.658
+ ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.515
+ ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.517
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500.cold.1
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500.cold.3
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.514
+ ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.640
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.457
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.458
+ ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.346
+ ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.347
+ ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.348
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.518
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.520
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8.cold.1
+ ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.286
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.33
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.33.cold.1
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.35
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.317
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.317.cold.1
+ ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.574
+ ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.109
+ ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.109.cold.1
+ ___90-[BRCAccountSessionFPFS(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]_block_invoke
+ ___90-[BRCAccountSessionFPFS(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]_block_invoke_2
+ ___90-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke.661
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.577
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.578
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.579
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.580
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.581
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.584
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.590
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.591
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.587
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.1
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.2
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.3
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.4
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke_2
+ ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.626
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.53
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.53.cold.1
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.57
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.343
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.344
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.345
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.316
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.316.cold.1
+ ___block_descriptor_32_e16_16?0"NSData"8l
+ ___block_descriptor_40_e8_32s_e8_v12?0I8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e23_B16?0"BRCAppLibrary"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e28_v24?0"FPItem"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e8_v12?0I8ls32l8r48l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e28_v24?0"FPItem"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e17_v16?0"NSError"8ls48l8w56l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56w_e27_v24?0"NSURL"8"NSError"16ls48l8w56l8s32l8s40l8
+ ___block_literal_global.11
+ ___block_literal_global.1724
+ ___block_literal_global.1736
+ ___block_literal_global.1887
+ ___block_literal_global.191
+ ___block_literal_global.2053
+ ___block_literal_global.2070
+ ___block_literal_global.2079
+ ___block_literal_global.2101
+ ___block_literal_global.2102
+ ___block_literal_global.2108
+ ___block_literal_global.2113
+ ___block_literal_global.217
+ ___block_literal_global.226
+ ___block_literal_global.2380
+ ___block_literal_global.2395
+ ___block_literal_global.2480
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.273
+ ___block_literal_global.285
+ ___block_literal_global.296
+ ___block_literal_global.322
+ ___block_literal_global.415
+ ___block_literal_global.429
+ ___block_literal_global.446
+ ___block_literal_global.492
+ ___block_literal_global.505
+ ___block_literal_global.557
+ ___block_literal_global.766
+ ___block_literal_global.772
+ __unnamed_array_storage.122
+ __unnamed_array_storage.123
+ __unnamed_array_storage.131
+ __unnamed_array_storage.132
+ __unnamed_array_storage.140
+ __unnamed_array_storage.141
+ __unnamed_array_storage.165
+ __unnamed_array_storage.183
+ __unnamed_array_storage.194
+ __unnamed_array_storage.195
+ __unnamed_array_storage.240
+ __unnamed_array_storage.2456
+ __unnamed_array_storage.2474
+ __unnamed_array_storage.249
+ __unnamed_array_storage.258
+ __unnamed_array_storage.259
+ __unnamed_array_storage.2631
+ __unnamed_array_storage.2643
+ __unnamed_array_storage.2722
+ __unnamed_array_storage.2771
+ __unnamed_array_storage.448
+ __unnamed_array_storage.451
+ _br_update_tables_30_016
+ _dumpDateFormatter.df
+ _dumpDateFormatter.onceToken
+ _objc_msgSend$_decorateFPFSDomainUserInfoWithError:
+ _objc_msgSend$_fileForUploadExistsInStage:record:
+ _objc_msgSend$_initWithVersionIdentifier:size:contentSignature:
+ _objc_msgSend$_locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:
+ _objc_msgSend$_parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:
+ _objc_msgSend$_populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:
+ _objc_msgSend$_processReportingBatch
+ _objc_msgSend$_recoverAndReportBrokenShareOptions
+ _objc_msgSend$_recoverAndReportContentPolicyWithCompletion:
+ _objc_msgSend$_recoverAndReportStateIntegrityWithCompletion:
+ _objc_msgSend$_sendItemsPendingReconciliation:event:
+ _objc_msgSend$_sendItemsPendingScanningDisk:event:
+ _objc_msgSend$_sendItemsPendingScanningProvider:event:
+ _objc_msgSend$_sendTelemetryEventForPendingItemsWithFPReport:migrationUUID:daysSinceImportStarted:
+ _objc_msgSend$_sendTelemetryEventWithDiagnosticAttributes:event:
+ _objc_msgSend$_shouldTriggerTapToRadar:itemsNotMigrated:reconciledItems:
+ _objc_msgSend$contentPolicy
+ _objc_msgSend$dbCreationTimestamp
+ _objc_msgSend$dbIntegrityCheckMissingShareOptions
+ _objc_msgSend$dumpDateFormat
+ _objc_msgSend$dumpDateFormatter
+ _objc_msgSend$equivalentVersions
+ _objc_msgSend$fetchItemForItemID:completionHandler:
+ _objc_msgSend$fpReport
+ _objc_msgSend$hasFpfsMigrationInvestigation
+ _objc_msgSend$initForTestingDevice:
+ _objc_msgSend$integrityCheckContentPolicy
+ _objc_msgSend$isPassbookMangledID
+ _objc_msgSend$isStreamResetRunning
+ _objc_msgSend$itemEnumerator
+ _objc_msgSend$itemPendingReconciliationIsLocked
+ _objc_msgSend$itemPendingReconciliationIsLockedInDB
+ _objc_msgSend$itemPendingReconciliationJobBlockingCode
+ _objc_msgSend$itemPendingReconciliationJobCode
+ _objc_msgSend$itemPendingReconciliationJobSchedulingState
+ _objc_msgSend$itemPendingScanningDiskEnumerationStatus
+ _objc_msgSend$itemPendingScanningDiskHasMultiplePagesEnumeration
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingReconciliation
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingRejection
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingSyncDown
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingSyncUp
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion
+ _objc_msgSend$itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent
+ _objc_msgSend$itemPendingScanningProviderEnumerationStatus
+ _objc_msgSend$itemPendingScanningProviderHasMultiplePagesEnumeration
+ _objc_msgSend$itemPendingScanningProviderNumberOfChildren
+ _objc_msgSend$itemPendingScanningProviderNumberOfChildrenFailingCreation
+ _objc_msgSend$itemPendingScanningProviderNumberOfChildrenPendingCreation
+ _objc_msgSend$itemPendingScanningProviderRemovalOfDatalessBitStatus
+ _objc_msgSend$itemsPendingReconciliation
+ _objc_msgSend$itemsPendingScanningDisk
+ _objc_msgSend$itemsPendingScanningProvider
+ _objc_msgSend$localEditCounterFromVersionIdentifier:
+ _objc_msgSend$migrationStatusPendingItemsTelemetryLimit
+ _objc_msgSend$newContentPolicyProblemCountWithProblemCount:
+ _objc_msgSend$newCorruptSharingOptionsProblemWithProblemCount:
+ _objc_msgSend$nonMigratedItemInvestigationWithFoundInfo:
+ _objc_msgSend$numberOfItemsPendingReconciliation
+ _objc_msgSend$numberOfItemsPendingScanningDisk
+ _objc_msgSend$numberOfItemsPendingScanningProvider
+ _objc_msgSend$numberOfItemsPendingSelection
+ _objc_msgSend$postMultipleReports:type:userinfo:session:observer:
+ _objc_msgSend$reimportFPFSDomainWithError:
+ _objc_msgSend$scheduleFlushWithCheckpoint:whenFlushed:
+ _objc_msgSend$setDurationBetweenDbCreationAndMigrationStart:
+ _objc_msgSend$setFpReport:
+ _objc_msgSend$setIsStreamResetRunning:
+ _objc_msgSend$setItemPendingReconciliationIsLocked:
+ _objc_msgSend$setItemPendingReconciliationIsLockedInDB:
+ _objc_msgSend$setItemPendingReconciliationJobBlockingCode:
+ _objc_msgSend$setItemPendingReconciliationJobCode:
+ _objc_msgSend$setItemPendingReconciliationJobSchedulingState:
+ _objc_msgSend$setItemPendingScanningDiskEnumerationStatus:
+ _objc_msgSend$setItemPendingScanningDiskHasMultiplePagesEnumeration:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingReconciliation:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingRejection:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingSyncDown:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingSyncUp:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:
+ _objc_msgSend$setItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:
+ _objc_msgSend$setItemPendingScanningProviderEnumerationStatus:
+ _objc_msgSend$setItemPendingScanningProviderHasMultiplePagesEnumeration:
+ _objc_msgSend$setItemPendingScanningProviderNumberOfChildren:
+ _objc_msgSend$setItemPendingScanningProviderNumberOfChildrenFailingCreation:
+ _objc_msgSend$setItemPendingScanningProviderNumberOfChildrenPendingCreation:
+ _objc_msgSend$setItemPendingScanningProviderRemovalOfDatalessBitStatus:
+ _objc_msgSend$setNumberOfItemsPendingReconciliation:
+ _objc_msgSend$setNumberOfItemsPendingScanningDisk:
+ _objc_msgSend$setNumberOfItemsPendingScanningProvider:
+ _objc_msgSend$setNumberOfItemsPendingSelection:
+ _objc_msgSend$setStateOfDownloadJobs:
+ _objc_msgSend$setStateOfOtherJobs:
+ _objc_msgSend$setStateOfUploadJobs:
+ _objc_msgSend$setStuckStatus:
+ _objc_msgSend$setXpcActivityDasdContext:
+ _objc_msgSend$setXpcActivityIsActive:
+ _objc_msgSend$setXpcActivityRegisteredWithDuet:
+ _objc_msgSend$setXpcActivityTimeSinceLastActivation:
+ _objc_msgSend$setXpcActivityTimeSinceLastRegistration:
+ _objc_msgSend$stateOfDownloadJobs
+ _objc_msgSend$stateOfOtherJobs
+ _objc_msgSend$stateOfUploadJobs
+ _objc_msgSend$telemetryRTCPacerMinFireInterval
+ _objc_msgSend$xpcActivityDasdContext
+ _objc_msgSend$xpcActivityIsActive
+ _objc_msgSend$xpcActivityRegisteredWithDuet
+ _objc_msgSend$xpcActivityTimeSinceLastActivation
+ _objc_msgSend$xpcActivityTimeSinceLastRegistration
- +[BRCImportUtil reimportItemsBelowItemWithIdentifier:error:].cold.1
- +[BRCImportUtil reimportItemsBelowItemWithIdentifier:error:].cold.2
- -[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]
- -[BRCAccountSessionFPFS _recoverAndReportMissingJobs]
- -[BRCAccountSessionFPFS _recoverAndReportMissingJobs].cold.1
- -[BRCAppLibrary addClientUsingUbiquity:]
- -[BRCAppLibrary hasUbiquityClientsConnected]
- -[BRCAppLibrary isGreedy].cold.5
- -[BRCAppLibrary removeClientUsingUbiquity:]
- -[BRCAppLibrary removeClientUsingUbiquity:].cold.1
- -[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:].cold.3
- -[BRCDeviceConfiguration .cxx_destruct]
- -[BRCDeviceConfiguration configuration]
- -[BRCDeviceConfiguration getDeviceConfigurationString]
- -[BRCDeviceConfiguration init]
- -[BRCFPImportReport reconciledItems]
- -[BRCFPImportReport setReconciledItems:]
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:]
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:].cold.1
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:].cold.2
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:].cold.3
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:].cold.4
- -[BRCFSImporter _parseImportBookmark:templateItem:fileURL:]
- -[BRCFSImporter _parseImportBookmark:templateItem:fileURL:].cold.1
- -[BRCFSImporter _parseImportBookmark:templateItem:fileURL:].cold.2
- -[BRCFSUploader _fileForUploadExistsInStage:]
- -[BRCFSUploader _handleFileModifiedError:forItem:].cold.2
- -[BRCPQLConnection flushWithCheckPoint:completionBlock:]
- -[BRCXPCClient isUsingUbiquity]
- -[BRCXPCClient setIsUsingUbiquity:]
- GCC_except_table109
- GCC_except_table122
- GCC_except_table124
- GCC_except_table148
- GCC_except_table152
- GCC_except_table153
- GCC_except_table157
- GCC_except_table159
- GCC_except_table164
- GCC_except_table168
- GCC_except_table170
- GCC_except_table182
- GCC_except_table186
- GCC_except_table189
- GCC_except_table196
- GCC_except_table201
- GCC_except_table204
- GCC_except_table209
- GCC_except_table218
- GCC_except_table222
- GCC_except_table229
- GCC_except_table232
- GCC_except_table234
- GCC_except_table236
- GCC_except_table241
- GCC_except_table245
- GCC_except_table268
- GCC_except_table270
- GCC_except_table272
- GCC_except_table275
- GCC_except_table284
- GCC_except_table287
- GCC_except_table313
- GCC_except_table316
- GCC_except_table323
- GCC_except_table326
- GCC_except_table338
- GCC_except_table341
- GCC_except_table345
- GCC_except_table348
- GCC_except_table352
- GCC_except_table356
- GCC_except_table360
- GCC_except_table365
- GCC_except_table376
- GCC_except_table381
- GCC_except_table384
- GCC_except_table386
- GCC_except_table397
- GCC_except_table400
- GCC_except_table405
- GCC_except_table409
- GCC_except_table412
- GCC_except_table421
- GCC_except_table423
- GCC_except_table434
- GCC_except_table437
- GCC_except_table445
- GCC_except_table447
- GCC_except_table450
- GCC_except_table454
- GCC_except_table457
- GCC_except_table458
- GCC_except_table88
- GCC_except_table98
- _OBJC_CLASS_$_BRCDeviceConfiguration
- _OBJC_IVAR_$_BRCAppLibrary._XPCClientsUsingUbiquity
- _OBJC_IVAR_$_BRCDeviceConfiguration._configuration
- _OBJC_IVAR_$_BRCFPImportReport._reconciledItems
- _OBJC_IVAR_$_BRCLocalVersion._localChangeCount
- _OBJC_IVAR_$_BRCLocalVersion._oldVersionIdentifier
- _OBJC_IVAR_$_BRCLocalVersion._previousItemGlobalID
- _OBJC_IVAR_$_BRCLocalVersion._uploadError
- _OBJC_IVAR_$_BRCLocalVersion._uploadedAssets
- _OBJC_IVAR_$_BRCXPCClient._isUsingUbiquity
- _OBJC_METACLASS_$_BRCDeviceConfiguration
- __OBJC_$_INSTANCE_METHODS_BRCDeviceConfiguration
- __OBJC_$_INSTANCE_VARIABLES_BRCDeviceConfiguration
- __OBJC_$_PROP_LIST_BRCDeviceConfiguration
- __OBJC_CLASS_RO_$_BRCDeviceConfiguration
- __OBJC_METACLASS_RO_$_BRCDeviceConfiguration
- ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.451
- ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.451.cold.1
- ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.455
- ___102-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke.670
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.62
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.62.cold.1
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.64
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.66
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.69
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.69.cold.1
- ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.646
- ___115-[BRCXPCRegularIPCsClient(FPFSAdditions) getDefaultAppContainerItemForContainerID:recreateDocumentsIfNeeded:reply:]_block_invoke.23
- ___115-[BRCXPCRegularIPCsClient(FPFSAdditions) getDefaultAppContainerItemForContainerID:recreateDocumentsIfNeeded:reply:]_block_invoke.28
- ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.410
- ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.411
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.75
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.30
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.32.cold.1
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.33
- ___167-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:]_block_invoke
- ___167-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:]_block_invoke.68
- ___26-[BRCXPCClient invalidate]_block_invoke
- ___30-[BRCAccountSessionFPFS close]_block_invoke.245
- ___40-[BRCAppLibrary addClientUsingUbiquity:]_block_invoke
- ___40-[BRCAppLibrary addClientUsingUbiquity:]_block_invoke.cold.1
- ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.269
- ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.269.cold.1
- ___42-[BRCAppLibrary _activateState:origState:]_block_invoke.32
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.213
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.214
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.217
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.216
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.216.cold.1
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.218
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.218.cold.1
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_3.222
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.328
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.328.cold.1
- ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.456
- ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.337
- ___47-[BRCServerChangeState descriptionWithContext:]_block_invoke
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.2
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.3
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.4
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.277
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.277.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.280
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.292
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.292.cold.1
- ___51-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]_block_invoke.665
- ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke.165
- ___53-[BRCAccountSessionFPFS _recoverAndReportMissingJobs]_block_invoke
- ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.406
- ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.407
- ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.506
- ___54-[BRCDeviceConfiguration getDeviceConfigurationString]_block_invoke
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.422
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.423
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.449
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.450
- ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.399
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.167
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.167.cold.1
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.168
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.175
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.175.cold.1
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.176
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke_2.177
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.714
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.715
- ___56-[BRCPQLConnection flushWithCheckPoint:completionBlock:]_block_invoke
- ___56-[BRCPQLConnection flushWithCheckPoint:completionBlock:]_block_invoke_2
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.370
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.371
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.660
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.660.cold.1
- ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.286
- ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.288
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.199
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.208
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.346
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.347
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.467.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.475
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.477
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.431
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.432
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.448
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.448.cold.1
- ___59-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke
- ___59-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke.115
- ___59-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke_2
- ___59-[BRCFSImporter _parseImportBookmark:templateItem:fileURL:]_block_invoke
- ___59-[BRCXPCRegularIPCsClient checkinAskClientIfUsingUbiquity:]_block_invoke
- ___59-[BRCXPCRegularIPCsClient checkinAskClientIfUsingUbiquity:]_block_invoke.cold.1
- ___60+[BRCImportUtil reimportItemsBelowItemWithIdentifier:error:]_block_invoke.cold.1
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.614
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.614.cold.1
- ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.608
- ___62-[BRCXPCRegularIPCsClient logoutAccountWithACAccountID:reply:]_block_invoke.447
- ___62-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke.691
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.308
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.309
- ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.398
- ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.297
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.655
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.655.cold.1
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.655.cold.2
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.656
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.616
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.617
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.619
- ___67-[BRCXPCRegularIPCsClient _presentAcceptDialogsWithMetadata:reply:]_block_invoke.658
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.436
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.436.cold.1
- ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.330
- ___68-[BRCXPCRegularIPCsClient queryEligibleAccountDescriptorsWithReply:]_block_invoke
- ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.301
- ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.424
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.411
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.411.cold.1
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.411.cold.2
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.414
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.414.cold.1
- ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.664
- ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.651
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.76
- ___71-[BRCXPCTokenClient currentAccountCopyTokenWithBundleID:version:reply:]_block_invoke
- ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.610
- ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.603
- ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.425
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.405
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.405.cold.1
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.406
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.406.cold.1
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.407
- ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.659
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.372
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.387
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.578
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.580
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.623
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.625
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400.cold.1
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400.cold.2
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.401
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.401.cold.1
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.620
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.621
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.612
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.612.cold.1
- ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.576
- ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.606
- ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.429
- ___80-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPFSImportFinishedTelemetryEvent]_block_invoke.164
- ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.573
- ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.325
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.451
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.452
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.642
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.577
- ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.644
- ___82-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke.666
- ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.523
- ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.525
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508.cold.3
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.512
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.522
- ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.648
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.465
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.466
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.354
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.355
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.356
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.526
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.528
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.3
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.3.cold.1
- ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.294
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.34
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.34.cold.1
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.36
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.301
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.301.cold.1
- ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.582
- ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.102
- ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.102.cold.1
- ___90-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke.669
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.585
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.587
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.588
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.592
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.594
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.597
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.598
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.599
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.595
- ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.634
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.55.cold.1
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.56
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.58
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.351
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.352
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.353
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.300
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.300.cold.1
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
- ___block_descriptor_42_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
- ___block_descriptor_72_e8_32s40bs48w_e27_v24?0"NSURL"8"NSError"16ls40l8w48l8s32l8
- ___block_literal_global.1721
- ___block_literal_global.1733
- ___block_literal_global.1884
- ___block_literal_global.201
- ___block_literal_global.2050
- ___block_literal_global.2067
- ___block_literal_global.2076
- ___block_literal_global.2095
- ___block_literal_global.2099
- ___block_literal_global.210
- ___block_literal_global.2105
- ___block_literal_global.2110
- ___block_literal_global.2377
- ___block_literal_global.2392
- ___block_literal_global.247
- ___block_literal_global.2477
- ___block_literal_global.249
- ___block_literal_global.256
- ___block_literal_global.268
- ___block_literal_global.279
- ___block_literal_global.282
- ___block_literal_global.306
- ___block_literal_global.409
- ___block_literal_global.419
- ___block_literal_global.441
- ___block_literal_global.457
- ___block_literal_global.495
- ___block_literal_global.529
- ___block_literal_global.749
- ___block_literal_global.755
- __unnamed_array_storage.108
- __unnamed_array_storage.116
- __unnamed_array_storage.124
- __unnamed_array_storage.125
- __unnamed_array_storage.133
- __unnamed_array_storage.134
- __unnamed_array_storage.157
- __unnamed_array_storage.175
- __unnamed_array_storage.186
- __unnamed_array_storage.187
- __unnamed_array_storage.232
- __unnamed_array_storage.233
- __unnamed_array_storage.242
- __unnamed_array_storage.2453
- __unnamed_array_storage.2471
- __unnamed_array_storage.251
- __unnamed_array_storage.2622
- __unnamed_array_storage.2634
- __unnamed_array_storage.2713
- __unnamed_array_storage.2759
- __unnamed_array_storage.443
- __unnamed_array_storage.446
- _descriptionWithContext:.df
- _descriptionWithContext:.onceToken
- _localEditCounterFromVersionIdentifier
- _objc_msgSend$_decorateFPFSDomainWithMigrationID
- _objc_msgSend$_fileForUploadExistsInStage:
- _objc_msgSend$_locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:
- _objc_msgSend$_parseImportBookmark:templateItem:fileURL:
- _objc_msgSend$_recoverAndReportMissingJobs
- _objc_msgSend$addClientUsingUbiquity:
- _objc_msgSend$flushWithCheckPoint:completionBlock:
- _objc_msgSend$hasUbiquityClientsConnected
- _objc_msgSend$isUsingUbiquity
- _objc_msgSend$postReportWithCategory:type:payload:userinfo:error:decoratedPayload:session:observer:
- _objc_msgSend$reconciledItems
- _objc_msgSend$removeClientUsingUbiquity:
- _objc_msgSend$setIsUsingUbiquity:
- _objc_msgSend$setReconciledItems:
CStrings:
+ " eqVersions:{%@}"
+ "+[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:]"
+ "+[BRCImportUtil reimportItemsBelowItemWithIdentifier:completionHandler:]_block_invoke"
+ "-[BRCAccountSessionFPFS _recoverAndReportBrokenShareOptions]"
+ "-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_2"
+ "-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_3"
+ "-[BRCAccountSessionFPFS _recoverAndReportStateIntegrityWithCompletion:]"
+ "-[BRCAccountSessionFPFS(BRCDatabaseManager) _decorateFPFSDomainUserInfoWithError:]"
+ "-[BRCAccountSessionFPFS(BRCDatabaseManager) _decorateFPFSDomainUserInfoWithError:]_block_invoke"
+ "-[BRCAccountSessionFPFS(BRCDatabaseManager) reimportFPFSDomainWithError:]"
+ "-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke"
+ "-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke_2"
+ "-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]"
+ "-[BRCFSImporter _parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:]"
+ "-[BRCFSImporter _parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:]_block_invoke"
+ "-[BRCFSUploader _fileForUploadExistsInStage:record:]"
+ "-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke"
+ "-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke"
+ "/\x01"
+ "4\"8\x11"
+ "<%@:%p>, deviceID:%d device:'%s' mounted-on:'%s' fstype:%s(%@)"
+ "@\"AppTelemetryStuckStatus\""
+ "@\"FPImportProgressReport\""
+ "@112@0:8@16@24@32Q40@48^Q56^B64@72@80^B88^Q96^@104"
+ "@16@?0@\"NSData\"8"
+ "@48@0:8@16@24@32^B40"
+ "AppTelemetryStuckStatus"
+ "B40@0:8q16q24q32"
+ "BRCFileProviderDaemonUtils was interrupted while waiting for FP to accept xpc connections"
+ "CORRUPT_BASEHASH_SALT_COUNT"
+ "CREATE INDEX \"client_items/corrupt_sharing_options\" ON client_items(rowid) WHERE zone_rowid != item_parent_zone_rowid AND (item_sharing_options & 4) = 0"
+ "FPFS_MIGRATION_STUCK_STATUS"
+ "INCORRECT_CONTENT_POLICY_COUNT"
+ "SELECT 1 FROM client_items AS ci INNER JOIN server_items AS si ON ci.version_old_zone_item_id = si.item_id AND ci.version_old_zone_rowid = si.zone_rowid  WHERE si.item_parent_id = %@ AND si.zone_rowid = %@ LIMIT 1"
+ "SELECT ci.rowid, ci.zone_rowid, ci.item_id, ci.item_creator_id, ci.item_sharing_options, ci.item_side_car_ckinfo, ci.item_parent_zone_rowid, ci.item_localsyncupstate, ci.item_local_diffs, ci.item_notifs_rank, ci.app_library_rowid, ci.item_min_supported_os_rowid, ci.item_user_visible, ci.item_stat_ckinfo, ci.item_state, ci.item_type, ci.item_mode, ci.item_birthtime, ci.item_lastusedtime, ci.item_favoriterank,ci.item_parent_id, ci.item_filename, ci.item_hidden_ext, ci.item_finder_tags, ci.item_xattr_signature, ci.item_trash_put_back_path, ci.item_trash_put_back_parent_id, ci.item_alias_target, ci.item_creator, ci.item_processing_stamp, ci.item_bouncedname, ci.item_scope, ci.item_local_change_count, ci.item_old_version_identifier, ci.fp_creation_item_identifier, ci.version_name, ci.version_ckinfo, ci.version_mtime, ci.version_size, ci.version_thumb_size, ci.version_thumb_signature, ci.version_content_signature, ci.version_xattr_signature, ci.version_edited_since_shared, ci.version_device, ci.version_conflict_loser_etags, ci.version_quarantine_info, ci.version_uploaded_assets, ci.version_upload_error, ci.version_old_zone_item_id, ci.version_old_zone_rowid, ci.version_local_change_count, ci.version_old_version_identifier, ci.item_live_conflict_loser_etags, ci.item_file_id, ci.item_generation FROM client_items AS ci LEFT JOIN server_items AS si ON ci.item_id = si.item_id AND ci.zone_rowid = si.zone_rowid WHERE ci.zone_rowid != ci.item_parent_zone_rowid AND (ci.item_sharing_options & 4) = 0 AND (si.item_id IS NULL OR item_id_is_root(si.item_parent_id))"
+ "T@\"AppTelemetryStuckStatus\",&,N"
+ "T@\"FPImportProgressReport\",&,N,V_fpReport"
+ "T@\"NSDateFormatter\",R,N"
+ "TB,N,V_isStreamResetRunning"
+ "TB,N,V_itemPendingReconciliationIsLocked"
+ "TB,N,V_itemPendingReconciliationIsLockedInDB"
+ "TB,N,V_itemPendingScanningDiskHasMultiplePagesEnumeration"
+ "TB,N,V_itemPendingScanningProviderHasMultiplePagesEnumeration"
+ "TB,N,V_xpcActivityIsActive"
+ "TB,N,V_xpcActivityRegisteredWithDuet"
+ "Tq,N,V_durationBetweenDbCreationAndMigrationStart"
+ "Tq,N,V_hasMoreLinks"
+ "Tq,N,V_itemPendingReconciliationJobBlockingCode"
+ "Tq,N,V_itemPendingReconciliationJobCode"
+ "Tq,N,V_itemPendingReconciliationJobSchedulingState"
+ "Tq,N,V_itemPendingScanningDiskEnumerationStatus"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "Tq,N,V_itemPendingScanningProviderEnumerationStatus"
+ "Tq,N,V_itemPendingScanningProviderNumberOfChildren"
+ "Tq,N,V_itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "Tq,N,V_itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "Tq,N,V_itemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "Tq,N,V_numberOfItemsPendingReconciliation"
+ "Tq,N,V_numberOfItemsPendingScanningDisk"
+ "Tq,N,V_numberOfItemsPendingScanningProvider"
+ "Tq,N,V_numberOfItemsPendingSelection"
+ "Tq,N,V_stateOfDownloadJobs"
+ "Tq,N,V_stateOfOtherJobs"
+ "Tq,N,V_stateOfUploadJobs"
+ "Tq,N,V_xpcActivityDasdContext"
+ "Tq,N,V_xpcActivityTimeSinceLastActivation"
+ "Tq,N,V_xpcActivityTimeSinceLastRegistration"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for _br_addDomain retry%@"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for _br_removeDomain retry%@"
+ "[CRIT] UNREACHABLE: should have an account dsid%@"
+ "[DEBUG] Done Force Ingestion %@ container to update the contentPolicy - %@%@"
+ "[DEBUG] Done Force Ingestion root container to update the contentPolicy - %@%@"
+ "[DEBUG] Starting _recoverAndReportStateIntegrity%@"
+ "[DEBUG] Updating domain databaseID to %@%@"
+ "[DEBUG] Updating migration UUID %@%@"
+ "[DEBUG] Volume not supported by FPFS%@"
+ "[DEBUG] don't be greedy because document in trash%@"
+ "[ERROR] DatabaseID mismatch %@ vs %@. Signalling reimport%@"
+ "[ERROR] Waiting without success for FP to accept XPCs: %@%@"
+ "[NOTICE] Signalled reimport of all FP items%@"
+ "[WARNING] CKAsset for %@ is pointing to the wrong device ID%@"
+ "[WARNING] Couldn't continue activity%@"
+ "[WARNING] Couldn't finish activity%@"
+ "[WARNING] Item %@ is missing a shareID%@"
+ "[WARNING] Item is missing structure CKInfo so using the version CKInfo because they are the same record %@%@"
+ "[WARNING] Marking %@ as rejected because the server item is dead%@"
+ "_decorateFPFSDomainUserInfoWithError:"
+ "_durationBetweenDbCreationAndMigrationStart"
+ "_fileForUploadExistsInStage:record:"
+ "_fpReport"
+ "_initWithVersionIdentifier:size:contentSignature:"
+ "_isStreamResetRunning"
+ "_itemPendingReconciliationIsLocked"
+ "_itemPendingReconciliationIsLockedInDB"
+ "_itemPendingReconciliationJobBlockingCode"
+ "_itemPendingReconciliationJobCode"
+ "_itemPendingReconciliationJobSchedulingState"
+ "_itemPendingScanningDiskEnumerationStatus"
+ "_itemPendingScanningDiskHasMultiplePagesEnumeration"
+ "_itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "_itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "_itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "_itemPendingScanningProviderEnumerationStatus"
+ "_itemPendingScanningProviderHasMultiplePagesEnumeration"
+ "_itemPendingScanningProviderNumberOfChildren"
+ "_itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "_itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "_itemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "_locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:"
+ "_numberOfItemsPendingReconciliation"
+ "_numberOfItemsPendingScanningDisk"
+ "_numberOfItemsPendingScanningProvider"
+ "_numberOfItemsPendingSelection"
+ "_pacerQueue"
+ "_parseImportBookmark:templateItem:fileURL:ignoreImportBookmark:"
+ "_populateFPFSImportStatusTelemetryEventForEvent:withFPImportReport:"
+ "_processReportingBatch"
+ "_recoverAndReportBrokenShareOptions"
+ "_recoverAndReportContentPolicyWithCompletion:"
+ "_recoverAndReportStateIntegrityWithCompletion:"
+ "_reportingPacer"
+ "_sendItemsPendingReconciliation:event:"
+ "_sendItemsPendingScanningDisk:event:"
+ "_sendItemsPendingScanningProvider:event:"
+ "_sendTelemetryEventForPendingItemsWithFPReport:migrationUUID:daysSinceImportStarted:"
+ "_sendTelemetryEventWithDiagnosticAttributes:event:"
+ "_shouldTriggerTapToRadar:itemsNotMigrated:reconciledItems:"
+ "_stateOfDownloadJobs"
+ "_stateOfOtherJobs"
+ "_stateOfUploadJobs"
+ "_stuckStatus"
+ "_xpcActivityDasdContext"
+ "_xpcActivityIsActive"
+ "_xpcActivityRegisteredWithDuet"
+ "_xpcActivityTimeSinceLastActivation"
+ "_xpcActivityTimeSinceLastRegistration"
+ "com.apple.,iCloud.com.apple."
+ "com.apple.bird.disk-space-observer"
+ "com.apple.rtc.pacer.queue"
+ "contentPolicy"
+ "db.integrity-check-content-policy"
+ "db.integrity-check.share-options"
+ "dbCreationTimestamp"
+ "dbIntegrityCheckMissingShareOptions"
+ "dump.date.format"
+ "dumpDateFormat"
+ "dumpDateFormatter"
+ "durationBetweenDbCreationAndMigrationStart"
+ "equivalentVersions"
+ "fetchItemForItemID:completionHandler:"
+ "fpReport"
+ "fpfs.migration.pending-items-status-telemetry-count"
+ "hasDurationBetweenDbCreationAndMigrationStart"
+ "hasIsStreamResetRunning"
+ "hasItemPendingReconciliationIsLocked"
+ "hasItemPendingReconciliationIsLockedInDB"
+ "hasItemPendingReconciliationJobBlockingCode"
+ "hasItemPendingReconciliationJobCode"
+ "hasItemPendingReconciliationJobSchedulingState"
+ "hasItemPendingScanningDiskEnumerationStatus"
+ "hasItemPendingScanningDiskHasMultiplePagesEnumeration"
+ "hasItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "hasItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "hasItemPendingScanningProviderEnumerationStatus"
+ "hasItemPendingScanningProviderHasMultiplePagesEnumeration"
+ "hasItemPendingScanningProviderNumberOfChildren"
+ "hasItemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "hasItemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "hasItemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "hasNumberOfItemsPendingReconciliation"
+ "hasNumberOfItemsPendingScanningDisk"
+ "hasNumberOfItemsPendingScanningProvider"
+ "hasNumberOfItemsPendingSelection"
+ "hasStateOfDownloadJobs"
+ "hasStateOfOtherJobs"
+ "hasStateOfUploadJobs"
+ "hasStuckStatus"
+ "hasXpcActivityDasdContext"
+ "hasXpcActivityIsActive"
+ "hasXpcActivityRegisteredWithDuet"
+ "hasXpcActivityTimeSinceLastActivation"
+ "hasXpcActivityTimeSinceLastRegistration"
+ "initForTestingDevice:"
+ "integrityCheckContentPolicy"
+ "isPassbookMangledID"
+ "isStreamResetRunning"
+ "itemEnumerator"
+ "itemPendingReconciliationIsLocked"
+ "itemPendingReconciliationIsLockedInDB"
+ "itemPendingReconciliationJobBlockingCode"
+ "itemPendingReconciliationJobCode"
+ "itemPendingReconciliationJobSchedulingState"
+ "itemPendingScanningDiskEnumerationStatus"
+ "itemPendingScanningDiskHasMultiplePagesEnumeration"
+ "itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "itemPendingScanningProviderEnumerationStatus"
+ "itemPendingScanningProviderHasMultiplePagesEnumeration"
+ "itemPendingScanningProviderNumberOfChildren"
+ "itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "itemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "itemsPendingReconciliation"
+ "itemsPendingScanningDisk"
+ "itemsPendingScanningProvider"
+ "kBRCFPFSMigrationStatusLastItemsNotMigratedKey"
+ "kBRCFPFSMigrationStatusLastReconciledItemsKey"
+ "kBRCFPFSMigrationStatusMigrationStatsTakenAtKey"
+ "localEditCounterFromVersionIdentifier:"
+ "migrationStatusPendingItemsTelemetryLimit"
+ "newContentPolicyProblemCountWithProblemCount:"
+ "newCorruptSharingOptionsProblemWithProblemCount:"
+ "nonMigratedItemInvestigationWithFoundInfo:"
+ "numberOfItemsPendingReconciliation"
+ "numberOfItemsPendingScanningDisk"
+ "numberOfItemsPendingScanningProvider"
+ "numberOfItemsPendingSelection"
+ "postMultipleReports:type:userinfo:session:observer:"
+ "q2"
+ "reimportFPFSDomainWithError:"
+ "scheduleFlushWithCheckpoint:whenFlushed:"
+ "setDurationBetweenDbCreationAndMigrationStart:"
+ "setFpReport:"
+ "setHasDurationBetweenDbCreationAndMigrationStart:"
+ "setHasIsStreamResetRunning:"
+ "setHasItemPendingReconciliationIsLocked:"
+ "setHasItemPendingReconciliationIsLockedInDB:"
+ "setHasItemPendingReconciliationJobBlockingCode:"
+ "setHasItemPendingReconciliationJobCode:"
+ "setHasItemPendingReconciliationJobSchedulingState:"
+ "setHasItemPendingScanningDiskEnumerationStatus:"
+ "setHasItemPendingScanningDiskHasMultiplePagesEnumeration:"
+ "setHasItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingReconciliation:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingRejection:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingSyncDown:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingSyncUp:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:"
+ "setHasItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:"
+ "setHasItemPendingScanningProviderEnumerationStatus:"
+ "setHasItemPendingScanningProviderHasMultiplePagesEnumeration:"
+ "setHasItemPendingScanningProviderNumberOfChildren:"
+ "setHasItemPendingScanningProviderNumberOfChildrenFailingCreation:"
+ "setHasItemPendingScanningProviderNumberOfChildrenPendingCreation:"
+ "setHasItemPendingScanningProviderRemovalOfDatalessBitStatus:"
+ "setHasNumberOfItemsPendingReconciliation:"
+ "setHasNumberOfItemsPendingScanningDisk:"
+ "setHasNumberOfItemsPendingScanningProvider:"
+ "setHasNumberOfItemsPendingSelection:"
+ "setHasStateOfDownloadJobs:"
+ "setHasStateOfOtherJobs:"
+ "setHasStateOfUploadJobs:"
+ "setHasXpcActivityDasdContext:"
+ "setHasXpcActivityIsActive:"
+ "setHasXpcActivityRegisteredWithDuet:"
+ "setHasXpcActivityTimeSinceLastActivation:"
+ "setHasXpcActivityTimeSinceLastRegistration:"
+ "setIsStreamResetRunning:"
+ "setItemPendingReconciliationIsLocked:"
+ "setItemPendingReconciliationIsLockedInDB:"
+ "setItemPendingReconciliationJobBlockingCode:"
+ "setItemPendingReconciliationJobCode:"
+ "setItemPendingReconciliationJobSchedulingState:"
+ "setItemPendingScanningDiskEnumerationStatus:"
+ "setItemPendingScanningDiskHasMultiplePagesEnumeration:"
+ "setItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingReconciliation:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingRejection:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDown:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUp:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:"
+ "setItemPendingScanningProviderEnumerationStatus:"
+ "setItemPendingScanningProviderHasMultiplePagesEnumeration:"
+ "setItemPendingScanningProviderNumberOfChildren:"
+ "setItemPendingScanningProviderNumberOfChildrenFailingCreation:"
+ "setItemPendingScanningProviderNumberOfChildrenPendingCreation:"
+ "setItemPendingScanningProviderRemovalOfDatalessBitStatus:"
+ "setNumberOfItemsPendingReconciliation:"
+ "setNumberOfItemsPendingScanningDisk:"
+ "setNumberOfItemsPendingScanningProvider:"
+ "setNumberOfItemsPendingSelection:"
+ "setStateOfDownloadJobs:"
+ "setStateOfOtherJobs:"
+ "setStateOfUploadJobs:"
+ "setStuckStatus:"
+ "setXpcActivityDasdContext:"
+ "setXpcActivityIsActive:"
+ "setXpcActivityRegisteredWithDuet:"
+ "setXpcActivityTimeSinceLastActivation:"
+ "setXpcActivityTimeSinceLastRegistration:"
+ "stateOfDownloadJobs"
+ "stateOfOtherJobs"
+ "stateOfUploadJobs"
+ "stuckStatus"
+ "telemetry.rtc.min-fire-interval"
+ "telemetryRTCPacerMinFireInterval"
+ "v12@?0I8"
+ "volume not supported by FPFS"
+ "xpcActivityDasdContext"
+ "xpcActivityIsActive"
+ "xpcActivityRegisteredWithDuet"
+ "xpcActivityTimeSinceLastActivation"
+ "xpcActivityTimeSinceLastRegistration"
+ "yyyy-MM-dd HH:mm:ss.SSS"
+ "yyyy-MM-dd HH:mm:ss.SSSZ"
+ "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"durationBetweenDbCreationAndMigrationStart\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsReconciledInFileProvider\"b1\"numberOfItemsPendingReconciliation\"b1\"numberOfItemsPendingScanningDisk\"b1\"numberOfItemsPendingScanningProvider\"b1\"numberOfItemsPendingSelection\"b1\"stateOfDownloadJobs\"b1\"stateOfOtherJobs\"b1\"stateOfUploadJobs\"b1\"totalItemCount\"b1\"xpcActivityDasdContext\"b1\"xpcActivityTimeSinceLastActivation\"b1\"xpcActivityTimeSinceLastRegistration\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isStreamResetRunning\"b1\"isSuccessful\"b1\"xpcActivityIsActive\"b1\"xpcActivityRegisteredWithDuet\"b1}"
+ "{?=\"apfsAvailableSpace\"b1\"apfsBlockSize\"b1\"apfsFlags\"b1\"apfsRole\"b1\"bTime\"b1\"cloneErrorCode\"b1\"dbCapabilities\"b1\"dbEffectiveContentPolicy\"b1\"dbErrorCode\"b1\"dbFpContentStatus\"b1\"dbFpDeletionStatus\"b1\"dbFpImportStatus\"b1\"dbFsContentStatus\"b1\"dbFsDeletionStatus\"b1\"dbFsImportStatus\"b1\"dbGenCount\"b1\"dbSharingState\"b1\"dbTransferState\"b1\"diagErrorCode\"b1\"diagFailuresBitmap\"b1\"diagUnderlyingErrorCode\"b1\"fileNameLength\"b1\"fsGenCount\"b1\"gencountDiff\"b1\"hasMoreLinks\"b1\"itemNumber\"b1\"mTime\"b1\"pathDepth\"b1\"pathLength\"b1\"purgeATime\"b1\"purgeGenCount\"b1\"purgeSyncRoot\"b1\"readErrorCode\"b1\"stFlags\"b1\"stMode\"b1\"statDirEntryCount\"b1\"statDocID\"b1\"statLogicalSize\"b1\"statPhysicalSize\"b1\"sysPageSize\"b1\"sysUID\"b1\"compressionType\"b1\"dataProtectionClass\"b1\"itemType\"b1\"syncRootEnum\"b1\"xattrCount\"b1\"apfsEncrypted\"b1\"appLibraryMatches\"b1\"bTimeIsBusy\"b1\"dbIsApplibrary\"b1\"dbIsPackage\"b1\"dbIsSuper\"b1\"doGenCountsMatchInFileId\"b1\"docIDMatches\"b1\"hasAcls\"b1\"hasLocalChanges\"b1\"isAppleDouble\"b1\"isBundleBit\"b1\"isFileNameNonAscii\"b1\"isOwnedByLoggedInUser\"b1\"isOwnedByRoot\"b1\"isPurgable\"b1\"isQuarantined\"b1\"isResourceFork\"b1\"isSparseFile\"b1\"isUnderDirStatFolder\"b1\"isUrgent\"b1\"mTimeBeforeMigrationStarted\"b1\"nameIsTrashed\"b1\"parentHasAcls\"b1\"parentMatches\"b1\"sysDocIDResolutionOK\"b1\"xattrHasBeforeBounce\"b1\"xattrHasDemotion\"b1\"xattrHasPromotion\"b1}"
+ "{?=\"itemPendingReconciliationJobBlockingCode\"b1\"itemPendingReconciliationJobCode\"b1\"itemPendingReconciliationJobSchedulingState\"b1\"itemPendingScanningDiskEnumerationStatus\"b1\"itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation\"b1\"itemPendingScanningDiskNumberOfChildrenPendingReconciliation\"b1\"itemPendingScanningDiskNumberOfChildrenPendingRejection\"b1\"itemPendingScanningDiskNumberOfChildrenPendingSyncDown\"b1\"itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion\"b1\"itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent\"b1\"itemPendingScanningDiskNumberOfChildrenPendingSyncUp\"b1\"itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion\"b1\"itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent\"b1\"itemPendingScanningProviderEnumerationStatus\"b1\"itemPendingScanningProviderNumberOfChildren\"b1\"itemPendingScanningProviderNumberOfChildrenFailingCreation\"b1\"itemPendingScanningProviderNumberOfChildrenPendingCreation\"b1\"itemPendingScanningProviderRemovalOfDatalessBitStatus\"b1\"itemPendingReconciliationIsLocked\"b1\"itemPendingReconciliationIsLockedInDB\"b1\"itemPendingScanningDiskHasMultiplePagesEnumeration\"b1\"itemPendingScanningProviderHasMultiplePagesEnumeration\"b1}"
+ "\xe1"
+ "\xf0\x83"
+ "\xf0\xf0\xc5\x11\x11"
- "%@:%@;"
- "%@::"
- "+[BRCImportUtil reimportItemsBelowItemWithIdentifier:error:]_block_invoke"
- "-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke"
- "-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke_2"
- "-[BRCAccountSessionFPFS _recoverAndReportMissingJobs]"
- "-[BRCAppLibrary addClientUsingUbiquity:]"
- "-[BRCAppLibrary addClientUsingUbiquity:]_block_invoke"
- "-[BRCAppLibrary removeClientUsingUbiquity:]"
- "-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:]"
- "-[BRCFSImporter _parseImportBookmark:templateItem:fileURL:]"
- "-[BRCFSImporter _parseImportBookmark:templateItem:fileURL:]_block_invoke"
- "-[BRCXPCRegularIPCsClient checkinAskClientIfUsingUbiquity:]"
- "-[BRCXPCRegularIPCsClient checkinAskClientIfUsingUbiquity:]_block_invoke"
- "-[BRCXPCRegularIPCsClient queryEligibleAccountDescriptorsWithReply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) getDefaultAppContainerItemForContainerID:recreateDocumentsIfNeeded:reply:]_block_invoke_2"
- "-[BRCXPCTokenClient currentAccountCopyTokenWithBundleID:version:reply:]_block_invoke"
- "1.1"
- "5\"8\x11"
- "<%@:%p>, device:'%s' mounted-on:'%s' fstype:%s(%@)"
- "@104@0:8@16@24@32Q40@48^Q56^B64@72@80^Q88^@96"
- "BRCDeviceConfiguration"
- "BRCFileProviderDaemonUtils was interrupted while waiting for FP to accept xpc conections"
- "EDS"
- "SELECT 1 FROM client_items AS ci  WHERE ci.version_old_zone_rowid = %@     AND %@ IN (SELECT si.item_parent_id FROM server_items AS si WHERE si.item_id = ci.version_old_zone_item_id AND si.zone_rowid = ci.version_old_zone_rowid)"
- "T@\"NSDictionary\",R,N,V_configuration"
- "TB,N,V_hasMoreLinks"
- "TB,N,V_isUsingUbiquity"
- "TESTING"
- "Tq,N,V_reconciledItems"
- "[CRIT] Assertion failed: rootItem.isDirectory%@"
- "[CRIT] UNREACHABLE: We should never receive a file modified error because the file is in our local state for %@%@"
- "[CRIT] UNREACHABLE: should have an account session%@"
- "[DEBUG] %@ forces %@ to be greedy%@"
- "[DEBUG] %@ no longer forces %@ to be greedy%@"
- "[DEBUG] First ubiquity client using container, schedule each item for download (client: %@, container: %@).%@"
- "[DEBUG] Last ubiquity client exited, no longer greedy (container: %@)%@"
- "[DEBUG] Starting _recoverAndReportMissingJobs%@"
- "[DEBUG] greediness enforced because library has clients connected%@"
- "[ERROR] Failed adopting persona - cannot update domain %@: %@%@"
- "[ERROR] Waiting without succees for FP to accept XPCs: %@%@"
- "[WARNING] %@ - Failed updating (%d -> %d) domain %@: %@%@"
- "_XPCClientsUsingUbiquity"
- "_configuration"
- "_decorateFPFSDomainWithMigrationID"
- "_fileForUploadExistsInStage:"
- "_isUsingUbiquity"
- "_locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:stillPendingFields:error:"
- "_parseImportBookmark:templateItem:fileURL:"
- "_reconciledItems"
- "_recoverAndReportMissingJobs"
- "addClientUsingUbiquity:"
- "com.apple.,iCloud.com.apple.,57T9237FN3.net.whatsapp.WhatsApp"
- "flushWithCheckPoint:completionBlock:"
- "hasUbiquityClientsConnected"
- "isUsingUbiquity"
- "postReportWithCategory:type:payload:userinfo:error:decoratedPayload:session:observer:"
- "removeClientUsingUbiquity:"
- "setIsUsingUbiquity:"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "yyyy-MM-dd/HH:mm:ss"
- "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsReconciledInFileProvider\"b1\"totalItemCount\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isSuccessful\"b1}"
- "{?=\"apfsAvailableSpace\"b1\"apfsBlockSize\"b1\"apfsFlags\"b1\"apfsRole\"b1\"bTime\"b1\"cloneErrorCode\"b1\"dbCapabilities\"b1\"dbEffectiveContentPolicy\"b1\"dbErrorCode\"b1\"dbFpContentStatus\"b1\"dbFpDeletionStatus\"b1\"dbFpImportStatus\"b1\"dbFsContentStatus\"b1\"dbFsDeletionStatus\"b1\"dbFsImportStatus\"b1\"dbGenCount\"b1\"dbSharingState\"b1\"dbTransferState\"b1\"diagErrorCode\"b1\"diagFailuresBitmap\"b1\"diagUnderlyingErrorCode\"b1\"fileNameLength\"b1\"fsGenCount\"b1\"gencountDiff\"b1\"itemNumber\"b1\"mTime\"b1\"pathDepth\"b1\"pathLength\"b1\"purgeATime\"b1\"purgeGenCount\"b1\"purgeSyncRoot\"b1\"readErrorCode\"b1\"stFlags\"b1\"stMode\"b1\"statDirEntryCount\"b1\"statDocID\"b1\"statLogicalSize\"b1\"statPhysicalSize\"b1\"sysPageSize\"b1\"sysUID\"b1\"compressionType\"b1\"dataProtectionClass\"b1\"itemType\"b1\"syncRootEnum\"b1\"xattrCount\"b1\"apfsEncrypted\"b1\"appLibraryMatches\"b1\"bTimeIsBusy\"b1\"dbIsApplibrary\"b1\"dbIsPackage\"b1\"dbIsSuper\"b1\"doGenCountsMatchInFileId\"b1\"docIDMatches\"b1\"hasAcls\"b1\"hasLocalChanges\"b1\"hasMoreLinks\"b1\"isAppleDouble\"b1\"isBundleBit\"b1\"isFileNameNonAscii\"b1\"isOwnedByLoggedInUser\"b1\"isOwnedByRoot\"b1\"isPurgable\"b1\"isQuarantined\"b1\"isResourceFork\"b1\"isSparseFile\"b1\"isUnderDirStatFolder\"b1\"isUrgent\"b1\"mTimeBeforeMigrationStarted\"b1\"nameIsTrashed\"b1\"parentHasAcls\"b1\"parentMatches\"b1\"sysDocIDResolutionOK\"b1\"xattrHasBeforeBounce\"b1\"xattrHasDemotion\"b1\"xattrHasPromotion\"b1}"
- "\x812"
- "\xc3"
- "\xf0\xf0\xb5\x11\x11"
- "\xf1"

```
