## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-2461.40.47.0.0
-  __TEXT.__text: 0x32a27c
+2461.62.1.0.0
+  __TEXT.__text: 0x331298
   __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0x1743c
+  __TEXT.__objc_methlist: 0x17bdc
   __TEXT.__const: 0x3e0
-  __TEXT.__cstring: 0x7b43f
-  __TEXT.__oslogstring: 0x434df
-  __TEXT.__gcc_except_tab: 0x1844c
+  __TEXT.__cstring: 0x7c259
+  __TEXT.__oslogstring: 0x436ba
+  __TEXT.__gcc_except_tab: 0x1849c
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x91b0
-  __TEXT.__objc_classname: 0x22de
-  __TEXT.__objc_methname: 0x3c1e5
-  __TEXT.__objc_methtype: 0x7e61
-  __TEXT.__objc_stubs: 0x2b140
+  __TEXT.__unwind_info: 0x9214
+  __TEXT.__objc_classname: 0x22e3
+  __TEXT.__objc_methname: 0x3eaab
+  __TEXT.__objc_methtype: 0x84eb
+  __TEXT.__objc_stubs: 0x2b2a0
   __DATA_CONST.__got: 0xb98
-  __DATA_CONST.__const: 0x8920
+  __DATA_CONST.__const: 0x8948
   __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35e30
-  __DATA_CONST.__objc_selrefs: 0xd380
+  __DATA_CONST.__objc_const: 0x36850
+  __DATA_CONST.__objc_selrefs: 0xd870
   __DATA_CONST.__objc_arraydata: 0xdd0
-  __AUTH_CONST.__const: 0x24c8
+  __AUTH_CONST.__const: 0x24e8
   __AUTH_CONST.__objc_const: 0x6950
-  __AUTH_CONST.__cfstring: 0x201e0
-  __AUTH_CONST.__objc_intobj: 0xb10
+  __AUTH_CONST.__cfstring: 0x206e0
+  __AUTH_CONST.__objc_intobj: 0xaf8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__auth_got: 0xe98
-  __AUTH.__objc_data: 0x2260
+  __AUTH.__objc_data: 0x22b0
   __AUTH.__data: 0x18
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xd38
+  __DATA.__objc_classrefs: 0xd40
   __DATA.__objc_superrefs: 0x800
-  __DATA.__objc_ivar: 0x1f88
+  __DATA.__objc_ivar: 0x2028
   __DATA.__data: 0x1ff0
-  __DATA.__bss: 0x330
-  __DATA_DIRTY.__objc_data: 0x3480
+  __DATA.__bss: 0x360
+  __DATA_DIRTY.__objc_data: 0x3430
   __DATA_DIRTY.__data: 0x2c8
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14396
-  Symbols:   42866
-  CStrings:  22924
+  Functions: 14583
+  Symbols:   43302
+  CStrings:  23212
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newContentPolicyProblemCountWithProblemCount:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newCorruptSharingOptionsProblemWithProblemCount:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) nonMigratedItemInvestigationWithFoundInfo:]
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
+ -[BRCAccountSession _recoverAndReportBrokenShareOptions]
+ -[BRCAccountSession _recoverAndReportStateIntegrityWithCompletion:]
+ -[BRCAccountSession _recoverAndReportStateIntegrityWithCompletion:].cold.1
+ -[BRCAppLibrary(LegacyAdditions) addClientUsingUbiquity:]
+ -[BRCAppLibrary(LegacyAdditions) hasUbiquityClientsConnected]
+ -[BRCAppLibrary(LegacyAdditions) removeClientUsingUbiquity:]
+ -[BRCAppLibrary(LegacyAdditions) removeClientUsingUbiquity:].cold.1
+ -[BRCPQLConnection scheduleFlushWithCheckpoint:whenFlushed:]
+ -[BRCRTCReporter _processReportingBatch]
+ -[BRCUserDefaults dbIntegrityCheckMissingShareOptions]
+ -[BRCUserDefaults dumpDateFormat]
+ -[BRCUserDefaults dumpDateFormatter]
+ -[BRCUserDefaults integrityCheckContentPolicy]
+ -[BRCUserDefaults telemetryRTCPacerMinFireInterval]
+ GCC_except_table104
+ GCC_except_table116
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table154
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table216
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table239
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table250
+ GCC_except_table255
+ GCC_except_table272
+ GCC_except_table279
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table317
+ GCC_except_table323
+ GCC_except_table334
+ GCC_except_table337
+ GCC_except_table341
+ GCC_except_table344
+ GCC_except_table348
+ GCC_except_table352
+ GCC_except_table357
+ GCC_except_table362
+ GCC_except_table367
+ GCC_except_table373
+ GCC_except_table378
+ GCC_except_table381
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table397
+ GCC_except_table402
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table414
+ GCC_except_table418
+ GCC_except_table425
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table434
+ GCC_except_table442
+ GCC_except_table445
+ GCC_except_table448
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table83
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
+ OBJC_IVAR_$_BRCLocalVersion._previousItemGlobalID
+ OBJC_IVAR_$_BRCLocalVersion._uploadError
+ OBJC_IVAR_$_BRCLocalVersion._uploadedAssets
+ _AppTelemetryStuckStatusReadFrom
+ _OBJC_CLASS_$_AppTelemetryStuckStatus
+ _OBJC_CLASS_$_BRDeviceConfiguration
+ _OBJC_IVAR_$_BRCRTCReporter._events
+ _OBJC_IVAR_$_BRCRTCReporter._pacerQueue
+ _OBJC_IVAR_$_BRCRTCReporter._reportingPacer
+ _OBJC_METACLASS_$_AppTelemetryStuckStatus
+ __OBJC_$_INSTANCE_METHODS_AppTelemetryStuckStatus
+ __OBJC_$_INSTANCE_VARIABLES_AppTelemetryStuckStatus
+ __OBJC_$_PROP_LIST_AppTelemetryStuckStatus
+ __OBJC_CLASS_PROTOCOLS_$_AppTelemetryStuckStatus
+ __OBJC_CLASS_RO_$_AppTelemetryStuckStatus
+ __OBJC_METACLASS_RO_$_AppTelemetryStuckStatus
+ ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.257
+ ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.257.cold.1
+ ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.260
+ ___104-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke.279
+ ___112-[BRCSideCarSyncUpOperation _syncUpRecordBatchWithModifiedRecords:deletedRecordIDs:recordIDToZoneMap:requestID:]_block_invoke.13
+ ___112-[BRCSideCarSyncUpOperation _syncUpRecordBatchWithModifiedRecords:deletedRecordIDs:recordIDToZoneMap:requestID:]_block_invoke_2
+ ___26-[BRCAccountSession close]_block_invoke.231
+ ___26-[BRCAccountSession close]_block_invoke.233
+ ___36-[BRCUserDefaults dumpDateFormatter]_block_invoke
+ ___40-[BRCAccountSession closeOfflineSession]_block_invoke.236
+ ___40-[BRCAccountSession closeOfflineSession]_block_invoke.236.cold.1
+ ___40-[BRCAccountSession closeOfflineSession]_block_invoke.237
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.203
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.204
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.207
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.218
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.206
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.206.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.208
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.208.cold.1
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.153.cold.1
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.1
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.2
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.3
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.4
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.156
+ ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.160
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.268
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.268.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.271
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.283
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.283.cold.1
+ ___48-[BRCRTCReporter initWithFPRTCReportingSession:]_block_invoke
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.188
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.195
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.199
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196.cold.3
+ ___56-[BRCAccountSession _recoverAndReportBrokenShareOptions]_block_invoke
+ ___57-[BRCAccountSession(BRCDatabaseManager) openDBWithError:]_block_invoke
+ ___57-[BRCAccountSession(BRCDatabaseManager) openDBWithError:]_block_invoke_2
+ ___57-[BRCAppLibrary(LegacyAdditions) addClientUsingUbiquity:]_block_invoke
+ ___57-[BRCAppLibrary(LegacyAdditions) addClientUsingUbiquity:]_block_invoke.cold.1
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.299
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.300
+ ___60-[BRCPQLConnection scheduleFlushWithCheckpoint:whenFlushed:]_block_invoke
+ ___60-[BRCPQLConnection scheduleFlushWithCheckpoint:whenFlushed:]_block_invoke_2
+ ___64-[BRCClientZone(BRCZoneReset) _finishedReset:completionHandler:]_block_invoke
+ ___65-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke.13
+ ___65-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke_2
+ ___65-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke_2.cold.1
+ ___67-[BRCAccountSession _recoverAndReportStateIntegrityWithCompletion:]_block_invoke
+ ___67-[BRCAccountSession _recoverAndReportStateIntegrityWithCompletion:]_block_invoke_2
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.1
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.2
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.3
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke.cold.4
+ ___79-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke_2
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.292
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.292.cold.1
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8
+ ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.8.cold.1
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.1
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.2
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.3
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke.cold.4
+ ___90-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e8_v12?0I8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e17_v16?0"NSError"8ls48l8w56l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56w_e27_v24?0"NSURL"8"NSError"16ls48l8w56l8s32l8s40l8
+ ___block_literal_global.136
+ ___block_literal_global.1721
+ ___block_literal_global.1733
+ ___block_literal_global.181
+ ___block_literal_global.1884
+ ___block_literal_global.190
+ ___block_literal_global.198
+ ___block_literal_global.2067
+ ___block_literal_global.2099
+ ___block_literal_global.2105
+ ___block_literal_global.2110
+ ___block_literal_global.235
+ ___block_literal_global.2377
+ ___block_literal_global.239
+ ___block_literal_global.2392
+ ___block_literal_global.246
+ ___block_literal_global.2477
+ ___block_literal_global.259
+ ___block_literal_global.270
+ ___block_literal_global.317
+ ___block_literal_global.794
+ __unnamed_array_storage.2453
+ __unnamed_array_storage.2471
+ __unnamed_array_storage.2628
+ __unnamed_array_storage.2640
+ __unnamed_array_storage.2726
+ _dumpDateFormatter.df
+ _dumpDateFormatter.onceToken
+ _objc_msgSend$_processReportingBatch
+ _objc_msgSend$_recoverAndReportBrokenShareOptions
+ _objc_msgSend$_recoverAndReportStateIntegrityWithCompletion:
+ _objc_msgSend$dbIntegrityCheckMissingShareOptions
+ _objc_msgSend$dumpDateFormat
+ _objc_msgSend$dumpDateFormatter
+ _objc_msgSend$initForTestingDevice:
+ _objc_msgSend$newCorruptSharingOptionsProblemWithProblemCount:
+ _objc_msgSend$nonMigratedItemInvestigationWithFoundInfo:
+ _objc_msgSend$postMultipleReports:type:userinfo:session:observer:
+ _objc_msgSend$scheduleFlushWithCheckpoint:whenFlushed:
+ _objc_msgSend$setStuckStatus:
+ _objc_msgSend$telemetryRTCPacerMinFireInterval
- -[BRCAccountSession _recoverAndReportMissingJobs]
- -[BRCAccountSession _recoverAndReportMissingJobs].cold.1
- -[BRCAppLibrary addClientUsingUbiquity:]
- -[BRCAppLibrary hasUbiquityClientsConnected]
- -[BRCAppLibrary removeClientUsingUbiquity:]
- -[BRCAppLibrary removeClientUsingUbiquity:].cold.1
- -[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:].cold.3
- -[BRCDeviceConfiguration .cxx_destruct]
- -[BRCDeviceConfiguration configuration]
- -[BRCDeviceConfiguration getDeviceConfigurationString]
- -[BRCDeviceConfiguration init]
- -[BRCPQLConnection flushWithCheckPoint:completionBlock:]
- GCC_except_table101
- GCC_except_table125
- GCC_except_table131
- GCC_except_table134
- GCC_except_table141
- GCC_except_table142
- GCC_except_table166
- GCC_except_table168
- GCC_except_table192
- GCC_except_table201
- GCC_except_table206
- GCC_except_table209
- GCC_except_table214
- GCC_except_table222
- GCC_except_table226
- GCC_except_table229
- GCC_except_table236
- GCC_except_table241
- GCC_except_table245
- GCC_except_table274
- GCC_except_table283
- GCC_except_table286
- GCC_except_table309
- GCC_except_table312
- GCC_except_table315
- GCC_except_table319
- GCC_except_table322
- GCC_except_table325
- GCC_except_table336
- GCC_except_table339
- GCC_except_table343
- GCC_except_table346
- GCC_except_table350
- GCC_except_table354
- GCC_except_table359
- GCC_except_table364
- GCC_except_table369
- GCC_except_table375
- GCC_except_table380
- GCC_except_table385
- GCC_except_table390
- GCC_except_table393
- GCC_except_table396
- GCC_except_table399
- GCC_except_table404
- GCC_except_table408
- GCC_except_table411
- GCC_except_table416
- GCC_except_table424
- GCC_except_table427
- GCC_except_table430
- GCC_except_table433
- GCC_except_table436
- GCC_except_table444
- GCC_except_table447
- GCC_except_table454
- GCC_except_table457
- GCC_except_table458
- GCC_except_table69
- GCC_except_table91
- _OBJC_CLASS_$_BRCDeviceConfiguration
- _OBJC_IVAR_$_BRCDeviceConfiguration._configuration
- _OBJC_IVAR_$_BRCLocalVersion._previousItemGlobalID
- _OBJC_IVAR_$_BRCLocalVersion._uploadError
- _OBJC_IVAR_$_BRCLocalVersion._uploadedAssets
- _OBJC_METACLASS_$_BRCDeviceConfiguration
- __OBJC_$_INSTANCE_METHODS_BRCDeviceConfiguration
- __OBJC_$_INSTANCE_VARIABLES_BRCDeviceConfiguration
- __OBJC_$_PROP_LIST_BRCDeviceConfiguration
- __OBJC_CLASS_RO_$_BRCDeviceConfiguration
- __OBJC_METACLASS_RO_$_BRCDeviceConfiguration
- ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.252
- ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.252.cold.1
- ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.255
- ___104-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke.276
- ___26-[BRCAccountSession close]_block_invoke.226
- ___26-[BRCAccountSession close]_block_invoke.228
- ___40-[BRCAccountSession closeOfflineSession]_block_invoke.231
- ___40-[BRCAccountSession closeOfflineSession]_block_invoke.231.cold.1
- ___40-[BRCAccountSession closeOfflineSession]_block_invoke.232
- ___40-[BRCAppLibrary addClientUsingUbiquity:]_block_invoke
- ___40-[BRCAppLibrary addClientUsingUbiquity:]_block_invoke.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.198
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.199
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.202
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.208
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.201
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.201.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.203
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.203.cold.1
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.150
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.150.cold.1
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.151
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.151.cold.1
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.151.cold.2
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.151.cold.3
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.151.cold.4
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.157
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.256
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.256.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.256.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.256.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.256.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.263
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.263.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.266
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.278
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.278.cold.1
- ___47-[BRCServerChangeState descriptionWithContext:]_block_invoke
- ___49-[BRCAccountSession _recoverAndReportMissingJobs]_block_invoke
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.176
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.176.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.176.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.176.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.176.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.184
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.184.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.184.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.184.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.184.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.185
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.192
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.193
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.193.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.193.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.193.cold.3
- ___54-[BRCDeviceConfiguration getDeviceConfigurationString]_block_invoke
- ___56-[BRCPQLConnection flushWithCheckPoint:completionBlock:]_block_invoke
- ___56-[BRCPQLConnection flushWithCheckPoint:completionBlock:]_block_invoke_2
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.294
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.295
- ___68-[BRCXPCRegularIPCsClient queryEligibleAccountDescriptorsWithReply:]_block_invoke
- ___71-[BRCXPCTokenClient currentAccountCopyTokenWithBundleID:version:reply:]_block_invoke
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.287
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.287.cold.1
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.3
- ___86-[NSFileProviderManager(BRCAdditions) br_removeDomain:options:sync:completionHandler:]_block_invoke.3.cold.1
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
- ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
- ___block_descriptor_72_e8_32s40bs48w_e27_v24?0"NSURL"8"NSError"16ls40l8w48l8s32l8
- ___block_literal_global.133
- ___block_literal_global.1718
- ___block_literal_global.1730
- ___block_literal_global.178
- ___block_literal_global.187
- ___block_literal_global.1881
- ___block_literal_global.195
- ___block_literal_global.2064
- ___block_literal_global.2096
- ___block_literal_global.2102
- ___block_literal_global.2107
- ___block_literal_global.230
- ___block_literal_global.234
- ___block_literal_global.2374
- ___block_literal_global.2389
- ___block_literal_global.241
- ___block_literal_global.2474
- ___block_literal_global.254
- ___block_literal_global.265
- ___block_literal_global.312
- ___block_literal_global.782
- __unnamed_array_storage.2450
- __unnamed_array_storage.2468
- __unnamed_array_storage.2619
- __unnamed_array_storage.2631
- __unnamed_array_storage.2717
- _descriptionWithContext:.df
- _descriptionWithContext:.onceToken
- _objc_msgSend$_recoverAndReportMissingJobs
- _objc_msgSend$postReportWithCategory:type:payload:userinfo:error:decoratedPayload:session:observer:
CStrings:
+ "-[BRCAccountSession _recoverAndReportBrokenShareOptions]"
+ "-[BRCAccountSession _recoverAndReportStateIntegrityWithCompletion:]"
+ "-[BRCAppLibrary(LegacyAdditions) addClientUsingUbiquity:]"
+ "-[BRCAppLibrary(LegacyAdditions) addClientUsingUbiquity:]_block_invoke"
+ "-[BRCAppLibrary(LegacyAdditions) removeClientUsingUbiquity:]"
+ "-[BRCContainerMetadataSyncUpOperation performAfterSavingRecords:]_block_invoke_2"
+ "-[NSFileProviderManager(BRCAdditions) _br_addDomain:retries:completionHandler:]_block_invoke"
+ "-[NSFileProviderManager(BRCAdditions) _br_removeDomain:options:retries:completionHandler:]_block_invoke"
+ "/\x01"
+ "@\"AppTelemetryStuckStatus\""
+ "AppTelemetryStuckStatus"
+ "BRCFileProviderDaemonUtils was interrupted while waiting for FP to accept xpc connections"
+ "CORRUPT_BASEHASH_SALT_COUNT"
+ "FPFS_MIGRATION_STUCK_STATUS"
+ "INCORRECT_CONTENT_POLICY_COUNT"
+ "SELECT 1 FROM client_items AS ci INNER JOIN server_items AS si ON ci.version_old_zone_item_id = si.item_id AND ci.version_old_zone_rowid = si.zone_rowid  WHERE si.item_parent_id = %@ AND si.zone_rowid = %@ LIMIT 1"
+ "SELECT ci.rowid, ci.zone_rowid, ci.item_id, ci.item_creator_id, ci.item_sharing_options, ci.item_side_car_ckinfo, ci.item_parent_zone_rowid, ci.item_localsyncupstate, ci.item_local_diffs, ci.item_notifs_rank, ci.app_library_rowid, ci.item_min_supported_os_rowid, ci.item_user_visible, ci.item_stat_ckinfo, ci.item_state, ci.item_type, ci.item_mode, ci.item_birthtime, ci.item_lastusedtime, ci.item_favoriterank,ci.item_parent_id, ci.item_filename, ci.item_hidden_ext, ci.item_finder_tags, ci.item_xattr_signature, ci.item_trash_put_back_path, ci.item_trash_put_back_parent_id, ci.item_alias_target, ci.item_creator, ci.item_doc_id, ci.item_file_id, ci.item_generation, ci.item_localname, ci.item_processing_stamp, ci.item_staged_file_id, ci.item_staged_generation, ci.item_bouncedname, ci.item_scope, ci.item_tmpbounceno, ci.version_name, ci.version_ckinfo, ci.version_mtime, ci.version_size, ci.version_thumb_size, ci.version_thumb_signature, ci.version_content_signature, ci.version_xattr_signature, ci.version_edited_since_shared, ci.version_device, ci.version_conflict_loser_etags, ci.version_quarantine_info, ci.version_uploaded_assets, ci.version_upload_error, ci.version_old_zone_item_id, ci.version_old_zone_rowid, ci.desired_version, ci.item_live_conflict_loser_etags, ci.item_thumb_live_signature, ci.item_thumb_greedy, ci.version_block_sync_until_bundle_id, ci.version_block_sync_until_timestamp FROM client_items AS ci LEFT JOIN server_items AS si ON ci.item_id = si.item_id AND ci.zone_rowid = si.zone_rowid WHERE ci.zone_rowid != ci.item_parent_zone_rowid AND (ci.item_sharing_options & 4) = 0 AND (si.item_id IS NULL OR item_id_is_root(si.item_parent_id))"
+ "T@\"AppTelemetryStuckStatus\",&,N"
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
+ "[DEBUG] Starting _recoverAndReportStateIntegrity%@"
+ "[DEBUG] Volume not supported by FPFS%@"
+ "[ERROR] Waiting without success for FP to accept XPCs: %@%@"
+ "[WARNING] Couldn't continue activity%@"
+ "[WARNING] Couldn't finish activity%@"
+ "[WARNING] Item %@ is missing a shareID%@"
+ "[WARNING] Item is missing structure CKInfo so using the version CKInfo because they are the same record %@%@"
+ "[WARNING] Marking %@ as rejected because the server item is dead%@"
+ "_durationBetweenDbCreationAndMigrationStart"
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
+ "_numberOfItemsPendingReconciliation"
+ "_numberOfItemsPendingScanningDisk"
+ "_numberOfItemsPendingScanningProvider"
+ "_numberOfItemsPendingSelection"
+ "_pacerQueue"
+ "_processReportingBatch"
+ "_recoverAndReportBrokenShareOptions"
+ "_recoverAndReportStateIntegrityWithCompletion:"
+ "_reportingPacer"
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
+ "com.apple.rtc.pacer.queue"
+ "db.integrity-check-content-policy"
+ "db.integrity-check.share-options"
+ "dbIntegrityCheckMissingShareOptions"
+ "dump.date.format"
+ "dumpDateFormat"
+ "dumpDateFormatter"
+ "durationBetweenDbCreationAndMigrationStart"
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
+ "isStreamResetRunning"
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
+ "newContentPolicyProblemCountWithProblemCount:"
+ "newCorruptSharingOptionsProblemWithProblemCount:"
+ "nonMigratedItemInvestigationWithFoundInfo:"
+ "numberOfItemsPendingReconciliation"
+ "numberOfItemsPendingScanningDisk"
+ "numberOfItemsPendingScanningProvider"
+ "numberOfItemsPendingSelection"
+ "postMultipleReports:type:userinfo:session:observer:"
+ "scheduleFlushWithCheckpoint:whenFlushed:"
+ "setDurationBetweenDbCreationAndMigrationStart:"
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
+ "\xf0\x83"
+ "\xf0\xf0\xc5\x11\x11"
- "%@:%@;"
- "%@::"
- "-[BRCAccountSession _recoverAndReportMissingJobs]"
- "-[BRCAppLibrary addClientUsingUbiquity:]"
- "-[BRCAppLibrary addClientUsingUbiquity:]_block_invoke"
- "-[BRCAppLibrary removeClientUsingUbiquity:]"
- "-[BRCXPCRegularIPCsClient queryEligibleAccountDescriptorsWithReply:]_block_invoke"
- "-[BRCXPCTokenClient currentAccountCopyTokenWithBundleID:version:reply:]_block_invoke"
- "1.1"
- "BRCDeviceConfiguration"
- "BRCFileProviderDaemonUtils was interrupted while waiting for FP to accept xpc conections"
- "EDS"
- "SELECT 1 FROM client_items AS ci  WHERE ci.version_old_zone_rowid = %@     AND %@ IN (SELECT si.item_parent_id FROM server_items AS si WHERE si.item_id = ci.version_old_zone_item_id AND si.zone_rowid = ci.version_old_zone_rowid)"
- "T@\"NSDictionary\",R,N,V_configuration"
- "TB,N,V_hasMoreLinks"
- "TESTING"
- "[CRIT] UNREACHABLE: should have an account session%@"
- "[DEBUG] Starting _recoverAndReportMissingJobs%@"
- "[ERROR] Waiting without succees for FP to accept XPCs: %@%@"
- "_configuration"
- "_recoverAndReportMissingJobs"
- "com.apple.,iCloud.com.apple.,57T9237FN3.net.whatsapp.WhatsApp"
- "flushWithCheckPoint:completionBlock:"
- "postReportWithCategory:type:payload:userinfo:error:decoratedPayload:session:observer:"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "yyyy-MM-dd/HH:mm:ss"
- "{?=\"accountQuotaUsage\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"busyDateNotMigratedCount\"b1\"childItemsNotMigratedCount\"b1\"ignoredFromSyncItemsNotMigratedCount\"b1\"importTime\"b1\"itemsMigratedWithoutAlreadyMayExistFlag\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"itemsReconciledInFileProvider\"b1\"totalItemCount\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"isAccountDataSeparated\"b1\"isSuccessful\"b1}"
- "{?=\"apfsAvailableSpace\"b1\"apfsBlockSize\"b1\"apfsFlags\"b1\"apfsRole\"b1\"bTime\"b1\"cloneErrorCode\"b1\"dbCapabilities\"b1\"dbEffectiveContentPolicy\"b1\"dbErrorCode\"b1\"dbFpContentStatus\"b1\"dbFpDeletionStatus\"b1\"dbFpImportStatus\"b1\"dbFsContentStatus\"b1\"dbFsDeletionStatus\"b1\"dbFsImportStatus\"b1\"dbGenCount\"b1\"dbSharingState\"b1\"dbTransferState\"b1\"diagErrorCode\"b1\"diagFailuresBitmap\"b1\"diagUnderlyingErrorCode\"b1\"fileNameLength\"b1\"fsGenCount\"b1\"gencountDiff\"b1\"itemNumber\"b1\"mTime\"b1\"pathDepth\"b1\"pathLength\"b1\"purgeATime\"b1\"purgeGenCount\"b1\"purgeSyncRoot\"b1\"readErrorCode\"b1\"stFlags\"b1\"stMode\"b1\"statDirEntryCount\"b1\"statDocID\"b1\"statLogicalSize\"b1\"statPhysicalSize\"b1\"sysPageSize\"b1\"sysUID\"b1\"compressionType\"b1\"dataProtectionClass\"b1\"itemType\"b1\"syncRootEnum\"b1\"xattrCount\"b1\"apfsEncrypted\"b1\"appLibraryMatches\"b1\"bTimeIsBusy\"b1\"dbIsApplibrary\"b1\"dbIsPackage\"b1\"dbIsSuper\"b1\"doGenCountsMatchInFileId\"b1\"docIDMatches\"b1\"hasAcls\"b1\"hasLocalChanges\"b1\"hasMoreLinks\"b1\"isAppleDouble\"b1\"isBundleBit\"b1\"isFileNameNonAscii\"b1\"isOwnedByLoggedInUser\"b1\"isOwnedByRoot\"b1\"isPurgable\"b1\"isQuarantined\"b1\"isResourceFork\"b1\"isSparseFile\"b1\"isUnderDirStatFolder\"b1\"isUrgent\"b1\"mTimeBeforeMigrationStarted\"b1\"nameIsTrashed\"b1\"parentHasAcls\"b1\"parentMatches\"b1\"sysDocIDResolutionOK\"b1\"xattrHasBeforeBounce\"b1\"xattrHasDemotion\"b1\"xattrHasPromotion\"b1}"
- "\xc3"
- "\xf0\xf0\xb5\x11\x11"

```
