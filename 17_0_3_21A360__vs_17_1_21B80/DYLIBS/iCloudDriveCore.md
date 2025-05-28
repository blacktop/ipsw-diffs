## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-2461.2.1.0.0
-  __TEXT.__text: 0x2a9558
+2461.40.47.0.0
+  __TEXT.__text: 0x2b3d40
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x14a74
+  __TEXT.__objc_methlist: 0x1550c
   __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x6fdfd
-  __TEXT.__oslogstring: 0x36890
-  __TEXT.__gcc_except_tab: 0x12f80
+  __TEXT.__cstring: 0x706b3
+  __TEXT.__oslogstring: 0x36e25
+  __TEXT.__gcc_except_tab: 0x1305c
   __TEXT.__ustring: 0x2be
-  __TEXT.__unwind_info: 0x7f0c
-  __TEXT.__objc_classname: 0x2067
-  __TEXT.__objc_methname: 0x357d1
-  __TEXT.__objc_methtype: 0x6680
-  __TEXT.__objc_stubs: 0x26120
-  __DATA_CONST.__got: 0x980
-  __DATA_CONST.__const: 0x7d00
+  __TEXT.__unwind_info: 0x7f90
+  __TEXT.__objc_classname: 0x2070
+  __TEXT.__objc_methname: 0x372e5
+  __TEXT.__objc_methtype: 0x6a06
+  __TEXT.__objc_stubs: 0x26ae0
+  __DATA_CONST.__got: 0xaf0
+  __DATA_CONST.__const: 0x7d50
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2f670
-  __DATA_CONST.__objc_selrefs: 0xbba0
+  __DATA_CONST.__objc_const: 0x30438
+  __DATA_CONST.__objc_selrefs: 0xc2b8
   __DATA_CONST.__objc_arraydata: 0xe80
-  __AUTH_CONST.__cfstring: 0x1ec40
-  __AUTH_CONST.__objc_const: 0x6268
-  __AUTH_CONST.__const: 0x2320
+  __AUTH_CONST.__cfstring: 0x1f340
+  __AUTH_CONST.__objc_const: 0x62b0
+  __AUTH_CONST.__const: 0x2360
   __AUTH_CONST.__objc_intobj: 0xb88
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x190

   __AUTH.__objc_data: 0x2710
   __AUTH.__data: 0x18
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xc78
+  __DATA.__objc_classrefs: 0xc80
   __DATA.__objc_superrefs: 0x778
-  __DATA.__objc_ivar: 0x1acc
+  __DATA.__objc_ivar: 0x1bbc
   __DATA.__data: 0x1e08
-  __DATA.__bss: 0x200
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x2ad0
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x2e8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12483
-  Symbols:   37466
-  CStrings:  20033
+  Functions: 12717
+  Symbols:   38129
+  CStrings:  20467
 
Symbols:
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:]
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:].cold.1
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.1
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.2
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:].cold.1
+ +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.3
+ +[BRCFileProviderDaemonUtils sharedInstance]
+ +[BRCImportUtil shouldFileIDBeIgnoredAsNonMigrated:docID:deviceID:isRegFile:rowid:outItemURL:isBusyDate:isIgnoredFromSync:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation apfsAvailableSpace]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation apfsBlockSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation apfsEncrypted]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation apfsFlags]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation apfsRole]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation appLibraryMatches]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation bTimeIsBusy]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation bTime]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbCapabilities]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbEffectiveContentPolicy]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbErrorCode]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbErrorDomain]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbFpContentStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbFpDeletionStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbFpImportStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbFsContentStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbFsDeletionStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbFsImportStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbIsApplibrary]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbIsPackage]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbIsSuper]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbSharingState]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation dbTransferState]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation diagErrorCode]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation diagErrorDomain]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation diagFailuresBitmap]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation diagUnderlyingErrorCode]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation diagUnderlyingErrorDomain]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation docIDMatches]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation fileNameExtension]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation gencountDiff]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasApfsAvailableSpace]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasApfsBlockSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasApfsEncrypted]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasApfsFlags]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasApfsRole]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasAppLibraryMatches]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasBTimeIsBusy]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasBTime]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbCapabilities]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbEffectiveContentPolicy]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbErrorCode]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbErrorDomain]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbFpContentStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbFpDeletionStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbFpImportStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbFsContentStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbFsDeletionStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbFsImportStatus]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbIsApplibrary]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbIsPackage]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbIsSuper]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbSharingState]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDbTransferState]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDiagErrorCode]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDiagErrorDomain]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDiagFailuresBitmap]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDiagUnderlyingErrorCode]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDiagUnderlyingErrorDomain]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasDocIDMatches]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasFileNameExtension]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasGencountDiff]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasIsQuarantined]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasMTimeBeforeMigrationStarted]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasMTime]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasNameIsTrashed]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasNameUnicodeNorm]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasParentMatches]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasPathDepth]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasPurgeATime]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasPurgeGenCount]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasPurgeSyncRoot]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasStatDirEntryCount]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasStatDocID]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasStatLogicalSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasStatPhysicalSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasSysDocIDResolutionOK]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasSysPageSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasSysUID]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasXattrHasBeforeBounce]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasXattrHasDemotion]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasXattrHasPromotion]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation isQuarantined]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation mTimeBeforeMigrationStarted]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation mTime]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation nameIsTrashed]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation nameUnicodeNorm]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation parentMatches]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation pathDepth]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation purgeATime]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation purgeGenCount]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation purgeSyncRoot]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setApfsAvailableSpace:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setApfsBlockSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setApfsEncrypted:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setApfsFlags:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setApfsRole:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setAppLibraryMatches:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setBTime:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setBTimeIsBusy:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbCapabilities:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbEffectiveContentPolicy:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbErrorCode:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbErrorDomain:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbFpContentStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbFpDeletionStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbFpImportStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbFsContentStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbFsDeletionStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbFsImportStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbIsApplibrary:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbIsPackage:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbIsSuper:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbSharingState:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDbTransferState:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDiagErrorCode:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDiagErrorDomain:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDiagFailuresBitmap:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDiagUnderlyingErrorCode:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDiagUnderlyingErrorDomain:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setDocIDMatches:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setFileNameExtension:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setGencountDiff:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasApfsAvailableSpace:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasApfsBlockSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasApfsEncrypted:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasApfsFlags:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasApfsRole:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasAppLibraryMatches:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasBTime:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasBTimeIsBusy:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbCapabilities:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbEffectiveContentPolicy:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbErrorCode:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbFpContentStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbFpDeletionStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbFpImportStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbFsContentStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbFsDeletionStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbFsImportStatus:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbIsApplibrary:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbIsPackage:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbIsSuper:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbSharingState:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDbTransferState:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDiagErrorCode:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDiagFailuresBitmap:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDiagUnderlyingErrorCode:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasDocIDMatches:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasGencountDiff:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasIsQuarantined:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasMTime:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasMTimeBeforeMigrationStarted:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasNameIsTrashed:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasParentMatches:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasPathDepth:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasPurgeATime:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasPurgeGenCount:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasPurgeSyncRoot:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasStatDirEntryCount:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasStatDocID:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasStatLogicalSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasStatPhysicalSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasSysDocIDResolutionOK:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasSysPageSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasSysUID:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasXattrHasBeforeBounce:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasXattrHasDemotion:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasXattrHasPromotion:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setIsQuarantined:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setMTime:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setMTimeBeforeMigrationStarted:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setNameIsTrashed:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setNameUnicodeNorm:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setParentMatches:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setPathDepth:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setPurgeATime:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setPurgeGenCount:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setPurgeSyncRoot:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setStatDirEntryCount:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setStatDocID:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setStatLogicalSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setStatPhysicalSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setSysDocIDResolutionOK:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setSysPageSize:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setSysUID:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setXattrHasBeforeBounce:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setXattrHasDemotion:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setXattrHasPromotion:]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation statDirEntryCount]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation statDocID]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation statLogicalSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation statPhysicalSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation sysDocIDResolutionOK]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation sysPageSize]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation sysUID]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation xattrHasBeforeBounce]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation xattrHasDemotion]
+ -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation xattrHasPromotion]
+ -[BRCAccountHandler _tryToOpenSession:error:].cold.4
+ -[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]
+ -[BRCAccountSessionFPFS _unlinkContainersWithPristineContainerIDs:containersActualRoot:containers:]
+ -[BRCAccountSessionFPFS _unlinkContainersWithRootURL:containers:]
+ -[BRCAccountSessionFPFS _unlinkContainersWithRootURL:containers:].cold.1
+ -[BRCAccountSessionFPFS _unlinkContainersWithRootURL:containers:].cold.2
+ -[BRCAccountSessionFPFS fpDomain]
+ -[BRCAccountSessionFPFS setFpDomain:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:]
+ -[BRCAccountsManager _createAccountHandlerForAccountID:]
+ -[BRCAccountsManager _getEnterpriseProviderManager]
+ -[BRCAccountsManager _getPrimaryProviderManager]
+ -[BRCAccountsManager _maintainExistingFileProviderDomainsIfNeededWithAccounts:]
+ -[BRCAccountsManager _maintainExistingFileProviderDomainsIfNeededWithAccounts:].cold.1
+ -[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]
+ -[BRCAccountsManager _waitUntilFileProviderIsReady:]
+ -[BRCAccountsManager _waitUntilFileProviderIsReady:].cold.1
+ -[BRCAccountsManager createAndLoadSessionWithACAccountID:createBlock:].cold.2
+ -[BRCAccountsManager getMaintainFPDomainsQueue]
+ -[BRCAccountsManager getQueue]
+ -[BRCBuddyFlowObserver _registerForBYSetupAssistantFinishedNotification]
+ -[BRCBuddyFlowObserver _unregisterForBYSetupAssistantFinishedNotification]
+ -[BRCDaemonFPFS _resumeSignals]
+ -[BRCDaemonFPFS shouldRejectXPCCalls]
+ -[BRCFSImporter _doesAppLibraryMatchWithItemURL:appLibraryRowID:]
+ -[BRCFSUploader _fileForUploadExistsInStage:]
+ -[BRCFileProviderDaemonUtils .cxx_destruct]
+ -[BRCFileProviderDaemonUtils _initWithSyncBubble:isFPFS:]
+ -[BRCFileProviderDaemonUtils _signalFPReady]
+ -[BRCFileProviderDaemonUtils _waitIsOver]
+ -[BRCFileProviderDaemonUtils boostFileProvider]
+ -[BRCFileProviderDaemonUtils dealloc]
+ -[BRCFileProviderDaemonUtils enableFileProviderBoosting]
+ -[BRCFileProviderDaemonUtils interrupt]
+ -[BRCFileProviderDaemonUtils waitForFPToBeReadyToAcceptXPCWithError:].cold.1
+ -[BRCFileProviderDaemonUtils waitForFPToBeReadyToAcceptXPCWithError:].cold.2
+ -[BRCFileProviderDaemonUtils waitForFPToBeReadyToAcceptXPCWithError:].cold.3
+ -[BRCLocalItem(BRCSharedToMeTopLevel) insertTombstoneAliasRecordInZone:].cold.4
+ -[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]
+ -[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]
+ -[BRCStageRegistry purgeAllUploads]
+ -[BRCStageRegistry purgeAllUploads].cold.1
+ -[BRCUserDefaults failModifyRequestsWhenInFlightUnAckedChanges]
+ -[BRCUserDefaults ignoreCKMMCSItemNotAvailableErrorForABC]
+ -[BRCUserDefaults setupAssistantReadyMaxWaitTimeInSec]
+ -[BRCUserDefaults shouldPurgeUploadsOnDeviceIDChange]
+ -[NSError(BRCAdditions) brc_isCloudKitMMCSItemNotAvailable]
+ GCC_except_table101
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table170
+ GCC_except_table179
+ GCC_except_table98
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._apfsAvailableSpace
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._apfsBlockSize
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._apfsEncrypted
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._apfsFlags
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._apfsRole
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._appLibraryMatches
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._bTime
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._bTimeIsBusy
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbCapabilities
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbEffectiveContentPolicy
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbErrorCode
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbErrorDomain
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbFpContentStatus
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbFpDeletionStatus
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbFpImportStatus
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbFsContentStatus
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbFsDeletionStatus
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbFsImportStatus
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbIsApplibrary
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbIsPackage
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbIsSuper
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbSharingState
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._dbTransferState
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._diagErrorCode
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._diagErrorDomain
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._diagFailuresBitmap
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._diagUnderlyingErrorCode
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._diagUnderlyingErrorDomain
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._docIDMatches
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._fileNameExtension
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._gencountDiff
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._isQuarantined
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._mTime
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._mTimeBeforeMigrationStarted
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._nameIsTrashed
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._nameUnicodeNorm
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._parentMatches
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._pathDepth
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._purgeATime
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._purgeGenCount
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._purgeSyncRoot
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._statDirEntryCount
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._statDocID
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._statLogicalSize
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._statPhysicalSize
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._sysDocIDResolutionOK
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._sysPageSize
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._sysUID
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._xattrHasBeforeBounce
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._xattrHasDemotion
+ OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._xattrHasPromotion
+ OBJC_IVAR_$_BRCAccountSessionFPFS._fpDomain
+ _BRDomainMigrationIDKey
+ _FPDiagnosticAttributeKeyAPFSAvailableSpace
+ _FPDiagnosticAttributeKeyAPFSBlockSize
+ _FPDiagnosticAttributeKeyAPFSEncrypted
+ _FPDiagnosticAttributeKeyAPFSFlags
+ _FPDiagnosticAttributeKeyAPFSRole
+ _FPDiagnosticAttributeKeyDBCapabilities
+ _FPDiagnosticAttributeKeyDBEffectiveContentPolicy
+ _FPDiagnosticAttributeKeyDBErrorCode
+ _FPDiagnosticAttributeKeyDBErrorDomain
+ _FPDiagnosticAttributeKeyDBFPContentStatus
+ _FPDiagnosticAttributeKeyDBFPDeletionStatus
+ _FPDiagnosticAttributeKeyDBFPImportStatus
+ _FPDiagnosticAttributeKeyDBFParentItemID
+ _FPDiagnosticAttributeKeyDBFSContentStatus
+ _FPDiagnosticAttributeKeyDBFSDeletionStatus
+ _FPDiagnosticAttributeKeyDBFSImportStatus
+ _FPDiagnosticAttributeKeyDBIsAppLibrary
+ _FPDiagnosticAttributeKeyDBIsPackage
+ _FPDiagnosticAttributeKeyDBSharingState
+ _FPDiagnosticAttributeKeyDBTransferState
+ _FPDiagnosticAttributeKeyDiagErrorCode
+ _FPDiagnosticAttributeKeyDiagErrorDomain
+ _FPDiagnosticAttributeKeyDiagFailuresBitmap
+ _FPDiagnosticAttributeKeyDiagUnderlyingErrorCode
+ _FPDiagnosticAttributeKeyDiagUnderlyingErrorDomain
+ _FPDiagnosticAttributeKeyNameExtension
+ _FPDiagnosticAttributeKeyNameIsTrashed
+ _FPDiagnosticAttributeKeyNamePathDepth
+ _FPDiagnosticAttributeKeyNameUnicodeNorm
+ _FPDiagnosticAttributeKeyPurgeAtime
+ _FPDiagnosticAttributeKeyPurgeGencount
+ _FPDiagnosticAttributeKeyPurgeSyncroot
+ _FPDiagnosticAttributeKeyStatBtime
+ _FPDiagnosticAttributeKeyStatBtimeIsBusy
+ _FPDiagnosticAttributeKeyStatDirEntryCount
+ _FPDiagnosticAttributeKeyStatDocID
+ _FPDiagnosticAttributeKeyStatLogicalSize
+ _FPDiagnosticAttributeKeyStatMtime
+ _FPDiagnosticAttributeKeyStatPhysicalSize
+ _FPDiagnosticAttributeKeySysDocIDResolutionOK
+ _FPDiagnosticAttributeKeySysPageSize
+ _FPDiagnosticAttributeKeySysUID
+ _FPDiagnosticAttributeKeyXattrHasBeforeBounce
+ _FPDiagnosticAttributeKeyXattrHasDemotion
+ _FPDiagnosticAttributeKeyXattrHasPromotion
+ _OBJC_CLASS_$_BRPosixOperationsWrapper
+ _OBJC_IVAR_$_BRCAccountsManager._maintainFPDomainsQueue
+ _OBJC_IVAR_$_BRCAccountsManager._maintainedExistingFPDomains
+ _OBJC_IVAR_$_BRCDaemonFPFS._shouldRejectXPCCalls
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._fileProviderReadyQueue
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._fpReady
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._fpReadyError
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._interrupted
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._shouldBoostFileProvider
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._startedWaitingForFP
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._waitForFPSemaphore
+ __OBJC_$_CLASS_METHODS_BRCFileProviderDaemonUtils
+ ___170+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke
+ ___170+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke.cold.1
+ ___22-[BRCDaemonFPFS start]_block_invoke_4
+ ___26-[BRCStageRegistry resume]_block_invoke.152
+ ___26-[BRCStageRegistry resume]_block_invoke.160
+ ___26-[BRCStageRegistry resume]_block_invoke.161
+ ___26-[BRCStageRegistry resume]_block_invoke.161.cold.1
+ ___26-[BRCStageRegistry resume]_block_invoke.161.cold.2
+ ___26-[BRCStageRegistry resume]_block_invoke.161.cold.3
+ ___27-[BRCDaemonFPFS selfCheck:]_block_invoke.145
+ ___30-[BRCAccountSessionFPFS close]_block_invoke.245
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.29
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.33
+ ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.269
+ ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.269.cold.1
+ ___44+[BRCFileProviderDaemonUtils sharedInstance]_block_invoke
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.154
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.154.cold.1
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke_2.159
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.214
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.217
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.230
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.216
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.216.cold.1
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.218
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.218.cold.1
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_3.222
+ ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.61
+ ___47-[BRCFileProviderDaemonUtils boostFileProvider]_block_invoke
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.2
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.3
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.270.cold.4
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.277
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.277.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.280
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.292
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.292.cold.1
+ ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke.165
+ ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.131
+ ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.131.cold.1
+ ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke_2.137
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.167.cold.1
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.168
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.175.cold.1
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.176
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke_2.177
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.199
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.208
+ ___59-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke
+ ___59-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke.115
+ ___59-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke_2
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.309
+ ___65-[BRCAccountSessionFPFS _unlinkContainersWithRootURL:containers:]_block_invoke
+ ___65-[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]_block_invoke
+ ___65-[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]_block_invoke.144
+ ___65-[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]_block_invoke.cold.1
+ ___65-[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]_block_invoke.cold.2
+ ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke
+ ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke.cold.1
+ ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke_2
+ ___69-[BRCFileProviderDaemonUtils waitForFPToBeReadyToAcceptXPCWithError:]_block_invoke.14
+ ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.6
+ ___74-[BRCAccountsManager createSessionWithACAccountID:dsid:completionHandler:]_block_invoke_3
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.48.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.51.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.52
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.53
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.cold.1
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.301
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.301.cold.1
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.300
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.300.cold.1
+ ___block_descriptor_112_e8_32s40s48s56r64r72r80r88r_e33_v32?0"NSNumber"8"BRPair"16^B24ls32l8r56l8s40l8r64l8r72l8r80l8s48l8r88l8
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8r88l8r96l8s64l8s72l8r104l8r112l8r120l8s80l8r128l8
+ ___block_descriptor_42_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e44_v24?0"NSError"8"<FPDWakeupTransaction>"16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e24_"BRCAccountHandler"8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8s40l8r48l8
+ ___block_descriptor_81_e8_32s40s48s56r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr56l8s32l8s40l8s48l8
+ ___block_descriptor_90_e8_32s40s48s56r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8r56l8
+ ___block_literal_global.122
+ ___block_literal_global.127
+ ___block_literal_global.141
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.157
+ ___block_literal_global.162
+ ___block_literal_global.164
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.181
+ ___block_literal_global.201
+ ___block_literal_global.2050
+ ___block_literal_global.2076
+ ___block_literal_global.2098
+ ___block_literal_global.210
+ ___block_literal_global.247
+ ___block_literal_global.249
+ ___block_literal_global.256
+ ___block_literal_global.268
+ ___block_literal_global.279
+ ___block_literal_global.306
+ ___block_literal_global.36
+ ___block_literal_global.44
+ ___block_literal_global.67
+ ___block_literal_global.749
+ ___block_literal_global.755
+ __unnamed_array_storage.2622
+ __unnamed_array_storage.2634
+ __unnamed_array_storage.2713
+ __unnamed_array_storage.2759
+ _br_update_tables_30_014
+ _br_update_tables_30_015
+ _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:
+ _objc_msgSend$_createAccountHandlerForAccountID:
+ _objc_msgSend$_decorateFPFSDomainWithMigrationID
+ _objc_msgSend$_doesAppLibraryMatchWithItemURL:appLibraryRowID:
+ _objc_msgSend$_fileForUploadExistsInStage:
+ _objc_msgSend$_garbageCollectLiveItemsIncludingActiveItems:
+ _objc_msgSend$_garbageCollectUploadsIncludingActiveUploads:
+ _objc_msgSend$_getEnterpriseProviderManager
+ _objc_msgSend$_getPrimaryProviderManager
+ _objc_msgSend$_initWithSyncBubble:isFPFS:
+ _objc_msgSend$_maintainExistingFileProviderDomainsIfNeededWithAccounts:
+ _objc_msgSend$_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:
+ _objc_msgSend$_registerForBYSetupAssistantFinishedNotification
+ _objc_msgSend$_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:
+ _objc_msgSend$_resumeSignals
+ _objc_msgSend$_scheduleExistingFileProviderDomainsMaintenanceWithAccounts:
+ _objc_msgSend$_signalFPReady
+ _objc_msgSend$_unlinkContainersWithPristineContainerIDs:containersActualRoot:containers:
+ _objc_msgSend$_unregisterForBYSetupAssistantFinishedNotification
+ _objc_msgSend$_waitIsOver
+ _objc_msgSend$_waitUntilFileProviderIsReady:
+ _objc_msgSend$boostFileProvider
+ _objc_msgSend$brc_errorItemBusy
+ _objc_msgSend$brc_isCloudKitMMCSItemNotAvailable
+ _objc_msgSend$callStackSymbols
+ _objc_msgSend$enableFileProviderBoosting
+ _objc_msgSend$exitProcess:
+ _objc_msgSend$failModifyRequestsWhenInFlightUnAckedChanges
+ _objc_msgSend$fpDomain
+ _objc_msgSend$ignoreCKMMCSItemNotAvailableErrorForABC
+ _objc_msgSend$interrupt
+ _objc_msgSend$mTime
+ _objc_msgSend$openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:
+ _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:
+ _objc_msgSend$openDBForNewDomain:deviceIDChanged:withError:
+ _objc_msgSend$purgeAllUploads
+ _objc_msgSend$setApfsAvailableSpace:
+ _objc_msgSend$setApfsBlockSize:
+ _objc_msgSend$setApfsEncrypted:
+ _objc_msgSend$setApfsFlags:
+ _objc_msgSend$setApfsRole:
+ _objc_msgSend$setAppLibraryMatches:
+ _objc_msgSend$setBTime:
+ _objc_msgSend$setBTimeIsBusy:
+ _objc_msgSend$setDbCapabilities:
+ _objc_msgSend$setDbEffectiveContentPolicy:
+ _objc_msgSend$setDbErrorCode:
+ _objc_msgSend$setDbErrorDomain:
+ _objc_msgSend$setDbFpContentStatus:
+ _objc_msgSend$setDbFpDeletionStatus:
+ _objc_msgSend$setDbFpImportStatus:
+ _objc_msgSend$setDbFsContentStatus:
+ _objc_msgSend$setDbFsDeletionStatus:
+ _objc_msgSend$setDbFsImportStatus:
+ _objc_msgSend$setDbIsApplibrary:
+ _objc_msgSend$setDbIsPackage:
+ _objc_msgSend$setDbSharingState:
+ _objc_msgSend$setDbTransferState:
+ _objc_msgSend$setDiagErrorCode:
+ _objc_msgSend$setDiagErrorDomain:
+ _objc_msgSend$setDiagFailuresBitmap:
+ _objc_msgSend$setDiagUnderlyingErrorCode:
+ _objc_msgSend$setDiagUnderlyingErrorDomain:
+ _objc_msgSend$setDocIDMatches:
+ _objc_msgSend$setFileNameExtension:
+ _objc_msgSend$setGencountDiff:
+ _objc_msgSend$setIsQuarantined:
+ _objc_msgSend$setMTime:
+ _objc_msgSend$setMTimeBeforeMigrationStarted:
+ _objc_msgSend$setNameIsTrashed:
+ _objc_msgSend$setNameUnicodeNorm:
+ _objc_msgSend$setParentMatches:
+ _objc_msgSend$setPathDepth:
+ _objc_msgSend$setPurgeATime:
+ _objc_msgSend$setPurgeGenCount:
+ _objc_msgSend$setPurgeSyncRoot:
+ _objc_msgSend$setStatDirEntryCount:
+ _objc_msgSend$setStatDocID:
+ _objc_msgSend$setStatLogicalSize:
+ _objc_msgSend$setStatPhysicalSize:
+ _objc_msgSend$setSysDocIDResolutionOK:
+ _objc_msgSend$setSysPageSize:
+ _objc_msgSend$setSysUID:
+ _objc_msgSend$setXattrHasBeforeBounce:
+ _objc_msgSend$setXattrHasDemotion:
+ _objc_msgSend$setXattrHasPromotion:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$shouldFileIDBeIgnoredAsNonMigrated:docID:deviceID:isRegFile:rowid:outItemURL:isBusyDate:isIgnoredFromSync:
+ _objc_msgSend$shouldPurgeUploadsOnDeviceIDChange
+ _objc_msgSend$shouldRejectXPCCalls
+ _objc_msgSend$wakeUpForURL:completionHandler:
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:error:]
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:error:].cold.1
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:]
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:].cold.1
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:].cold.2
- +[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]
- +[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:].cold.1
- +[BRCImportUtil shouldFileIDBeIgnoredAsNonMigrated:deviceID:isRegFile:rowid:isBusyDate:isIgnoredFromSync:]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasIsQuerantined]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation isQuerantined]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasIsQuerantined:]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setIsQuerantined:]
- -[BRCAccountSessionFPFS _unlinkContainersWithPristineContainerIDs:containersActualRoot:]
- -[BRCAccountSessionFPFS _unlinkContainersWithRootURL:]
- -[BRCAccountSessionFPFS _unlinkContainersWithRootURL:].cold.1
- -[BRCAccountSessionFPFS _unlinkContainersWithRootURL:].cold.2
- -[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:error:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) openDBForNewDomain:withError:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:]
- -[BRCBuddyFlowObserver _registerForSetupAssistantFinishedNotification]
- -[BRCBuddyFlowObserver _registerForSetupAssistantFinishedNotification].cold.1
- -[BRCBuddyFlowObserver _stopObservingBuddyAndExecuteCallbacks].cold.1
- -[BRCBuddyFlowObserver _stopObservingBuddyAndExecuteCallbacks].cold.2
- -[BRCBuddyFlowObserver _unregisterForSetupAssistantFinishedNotification]
- -[BRCBuddyFlowObserver _unregisterForSetupAssistantFinishedNotification].cold.1
- -[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:].cold.1
- -[BRCFileProviderDaemonUtils initWithSyncBubble:isFPFS:]
- GCC_except_table151
- GCC_except_table154
- GCC_except_table160
- GCC_except_table171
- OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._isQuerantined
- _OBJC_IVAR_$_BRCBuddyFlowObserver._notificationQueue
- ___154+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]_block_invoke
- ___154+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]_block_invoke.cold.1
- ___22-[BRCDaemonFPFS start]_block_invoke.cold.2
- ___22-[BRCDaemonFPFS start]_block_invoke_2.97
- ___22-[BRCDaemonFPFS start]_block_invoke_2.cold.1
- ___26-[BRCStageRegistry resume]_block_invoke.150
- ___26-[BRCStageRegistry resume]_block_invoke.158
- ___26-[BRCStageRegistry resume]_block_invoke.159
- ___26-[BRCStageRegistry resume]_block_invoke.159.cold.1
- ___26-[BRCStageRegistry resume]_block_invoke.159.cold.2
- ___26-[BRCStageRegistry resume]_block_invoke.159.cold.3
- ___27-[BRCDaemonFPFS selfCheck:]_block_invoke.149
- ___30-[BRCAccountSessionFPFS close]_block_invoke.244
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.28
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.35
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.cold.3
- ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.268
- ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.268.cold.1
- ___42-[BRCStageRegistry _garbageCollectUploads]_block_invoke
- ___42-[BRCStageRegistry _garbageCollectUploads]_block_invoke.cold.1
- ___42-[BRCStageRegistry _garbageCollectUploads]_block_invoke_2
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.158.cold.1
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.162
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke_2.163
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.212
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.216
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.229
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.215
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.215.cold.1
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.217
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.217.cold.1
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_3.221
- ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.58
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.269
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.269.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.269.cold.2
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.269.cold.3
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.269.cold.4
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.276
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.276.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.279
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.291
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.291.cold.1
- ___50-[BRCStageRegistry _garbageCollectUnusedLiveItems]_block_invoke
- ___50-[BRCStageRegistry _garbageCollectUnusedLiveItems]_block_invoke_2
- ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke.164
- ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.136
- ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.136.cold.1
- ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke_2.141
- ___54-[BRCAccountSessionFPFS _unlinkContainersWithRootURL:]_block_invoke
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.166
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.166.cold.1
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.174
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.174.cold.1
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke_2.176
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.198
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.207
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.307
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.cold.4
- ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.7
- ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.7.cold.1
- ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.46
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.47.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.50.cold.1
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.300
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.300.cold.1
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.299
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.299.cold.1
- ____buddyHasFinished_block_invoke
- ___block_descriptor_104_e8_32s40s48r56r64r72r80r_e33_v32?0"NSNumber"8"BRPair"16^B24ls32l8r48l8s40l8r56l8r64l8r72l8r80l8
- ___block_descriptor_160_e8_32s40s48s56s64s72s80r88r96r104r112r120r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8r80l8r88l8s64l8s72l8r96l8r104l8r112l8r120l8
- ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e24_"BRCAccountHandler"8?0ls32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8s40l8s48l8r56l8
- ___block_descriptor_82_e8_32s40s48s56r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.128
- ___block_literal_global.145
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.200
- ___block_literal_global.2047
- ___block_literal_global.2073
- ___block_literal_global.209
- ___block_literal_global.2092
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.267
- ___block_literal_global.278
- ___block_literal_global.305
- ___block_literal_global.43
- ___block_literal_global.740
- ___block_literal_global.746
- __buddyHasFinished.cold.1
- __unnamed_array_storage.2619
- __unnamed_array_storage.2631
- __unnamed_array_storage.2710
- __unnamed_array_storage.2753
- _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:error:
- _objc_msgSend$_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:
- _objc_msgSend$_registerForSetupAssistantFinishedNotification
- _objc_msgSend$_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:
- _objc_msgSend$_unlinkContainersWithPristineContainerIDs:containersActualRoot:
- _objc_msgSend$_unregisterForSetupAssistantFinishedNotification
- _objc_msgSend$br_getDomainForDataSeparated:withIdentifier:withError:
- _objc_msgSend$initWithSyncBubble:isFPFS:
- _objc_msgSend$openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:error:
- _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:
- _objc_msgSend$openDBForNewDomain:withError:
- _objc_msgSend$setIsQuerantined:
- _objc_msgSend$shouldFileIDBeIgnoredAsNonMigrated:deviceID:isRegFile:rowid:isBusyDate:isIgnoredFromSync:
CStrings:
+ "\x03\x11"
+ "\t\x15\x18\xf0/\x01\x11\x12\x1f\b"
+ "\x11\x12"
+ "+[BRCAccountSessionFPFS(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:]"
+ "+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]"
+ "+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]"
+ "+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke"
+ "+[BRCImportUtil shouldFileIDBeIgnoredAsNonMigrated:docID:deviceID:isRegFile:rowid:outItemURL:isBusyDate:isIgnoredFromSync:]"
+ "-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke"
+ "-[BRCAccountSessionFPFS _decorateFPFSDomainWithMigrationID]_block_invoke_2"
+ "-[BRCAccountSessionFPFS _unlinkContainersWithRootURL:containers:]"
+ "-[BRCAccountSessionFPFS(BRCDatabaseManager) openDBForNewDomain:deviceIDChanged:withError:]"
+ "-[BRCAccountsManager _maintainExistingFileProviderDomainsIfNeededWithAccounts:]"
+ "-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke"
+ "-[BRCAccountsManager _waitUntilFileProviderIsReady:]"
+ "-[BRCBuddyFlowObserver _registerForBYSetupAssistantFinishedNotification]"
+ "-[BRCBuddyFlowObserver _unregisterForBYSetupAssistantFinishedNotification]"
+ "-[BRCDaemonFPFS shouldRejectXPCCalls]"
+ "-[BRCDaemonFPFS start]_block_invoke_5"
+ "-[BRCFileProviderDaemonUtils _signalFPReady]"
+ "-[BRCFileProviderDaemonUtils boostFileProvider]"
+ "-[BRCFileProviderDaemonUtils interrupt]"
+ "-[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]_block_invoke"
+ "-[BRCStageRegistry _garbageCollectLiveItemsIncludingActiveItems:]_block_invoke_2"
+ "-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke"
+ "-[BRCStageRegistry purgeAllUploads]"
+ "@\"NSFileProviderDomain\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "B36@0:8B16^B20^@28"
+ "B56@0:8@16B24@28B36^B40^@48"
+ "B60@0:8@16B24^I28^I36^B44^@52"
+ "B76@0:8@16@24@32B40@44^@52^B60^B68"
+ "B80@0:8@16B24@28@36B44^I48^I56^B64^@72"
+ "BRCFileProviderDaemonUtils was interrupted while waiting for FP to accept xpc conections"
+ "T@\"NSFileProviderDomain\",&,N,V_fpDomain"
+ "T@\"NSString\",&,N,V_dbErrorDomain"
+ "T@\"NSString\",&,N,V_diagErrorDomain"
+ "T@\"NSString\",&,N,V_diagUnderlyingErrorDomain"
+ "T@\"NSString\",&,N,V_fileNameExtension"
+ "T@\"NSString\",&,N,V_nameUnicodeNorm"
+ "TB,N,V_apfsEncrypted"
+ "TB,N,V_appLibraryMatches"
+ "TB,N,V_bTimeIsBusy"
+ "TB,N,V_dbIsApplibrary"
+ "TB,N,V_dbIsPackage"
+ "TB,N,V_dbIsSuper"
+ "TB,N,V_docIDMatches"
+ "TB,N,V_isQuarantined"
+ "TB,N,V_mTimeBeforeMigrationStarted"
+ "TB,N,V_nameIsTrashed"
+ "TB,N,V_parentMatches"
+ "TB,N,V_sysDocIDResolutionOK"
+ "TB,N,V_xattrHasBeforeBounce"
+ "TB,N,V_xattrHasDemotion"
+ "TB,N,V_xattrHasPromotion"
+ "Tq,N,V_apfsAvailableSpace"
+ "Tq,N,V_apfsBlockSize"
+ "Tq,N,V_apfsFlags"
+ "Tq,N,V_apfsRole"
+ "Tq,N,V_bTime"
+ "Tq,N,V_dbCapabilities"
+ "Tq,N,V_dbEffectiveContentPolicy"
+ "Tq,N,V_dbErrorCode"
+ "Tq,N,V_dbFpContentStatus"
+ "Tq,N,V_dbFpDeletionStatus"
+ "Tq,N,V_dbFpImportStatus"
+ "Tq,N,V_dbFsContentStatus"
+ "Tq,N,V_dbFsDeletionStatus"
+ "Tq,N,V_dbFsImportStatus"
+ "Tq,N,V_dbSharingState"
+ "Tq,N,V_dbTransferState"
+ "Tq,N,V_diagErrorCode"
+ "Tq,N,V_diagFailuresBitmap"
+ "Tq,N,V_diagUnderlyingErrorCode"
+ "Tq,N,V_gencountDiff"
+ "Tq,N,V_mTime"
+ "Tq,N,V_pathDepth"
+ "Tq,N,V_purgeATime"
+ "Tq,N,V_purgeGenCount"
+ "Tq,N,V_purgeSyncRoot"
+ "Tq,N,V_statDirEntryCount"
+ "Tq,N,V_statDocID"
+ "Tq,N,V_statLogicalSize"
+ "Tq,N,V_statPhysicalSize"
+ "Tq,N,V_sysPageSize"
+ "Tq,N,V_sysUID"
+ "UPDATE client_items SET item_file_id = call_block(%p, item_file_id, item_type, item_localsyncupstate, rowid, item_generation, item_local_diffs, item_doc_id, app_library_rowid), item_generation = call_block(%p, item_generation, item_type, item_localsyncupstate), item_localsyncupstate = call_block(%p, item_localsyncupstate, rowid, item_stat_ckinfo IS NULL, item_type, item_birthtime, item_id, item_filename, version_content_signature, item_parent_zone_rowid, item_parent_id), item_doc_id = NULL WHERE rowid > %llu ORDER BY rowid ASC LIMIT %llu"
+ "UPDATE client_uploads SET transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL WHERE throttle_state = 1 AND upload_error LIKE '%%(16/3002)%%'"
+ "[CRIT] Assertion failed: argc == 3 || argc == 8%@"
+ "[CRIT] UNREACHABLE: Can't match items of different kind! %@ vs %@%@"
+ "[CRIT] UNREACHABLE: FP is not ready but we don't have an error%@"
+ "[CRIT] UNREACHABLE: Items dont have the same kind so can't be matched! %@ vs %@%@"
+ "[CRIT] UNREACHABLE: Items have the same creation identifier but are of differnt kinds %@ vs %@%@"
+ "[DEBUG] FP is already ready to connect after boosting%@"
+ "[DEBUG] Ignoring CloudKit open error (Operation not permitted) protected class error %ld%@"
+ "[DEBUG] Insering alias tombstone for %@%@"
+ "[DEBUG] Purging all uploads and live items%@"
+ "[DEBUG] Starting to wait for FP to be ready to accept xpc connections%@"
+ "[DEBUG] We received an asset unavailable error but it exists in the correct place. This must be a file protected file or a rapid edit after the first edit%@"
+ "[DEBUG] removing staged live item: %@%@"
+ "[DEBUG] removing staged live item: %s%@"
+ "[DEBUG] ┏%llx received new XPC connection: %@, for uid: %u%@"
+ "[ERROR] Failed adopting persona - cannot update domain %@: %@%@"
+ "[ERROR] Failed waiting for File Provider to be ready: %@%@"
+ "[ERROR] Waiting without succees for FP to accept XPCs: %@%@"
+ "[ERROR] failed getting URL of item with rowID %@ docID %@ and fileID %@: %@%@"
+ "[ERROR] item with rowID %@ docID %@ and fileID %@ got left behind when migrating: %@%@"
+ "[NOTICE] BYSetupAssistantFinishedDarwinNotification was received%@"
+ "[NOTICE] BYSetupAssistantNeedsToRun --> pausing daemon startup until done.%@"
+ "[NOTICE] Buddy has finished. Execute block [%@]%@"
+ "[NOTICE] FP is now ready to accept xpc connections%@"
+ "[NOTICE] Key %@ already registered%@"
+ "[NOTICE] Recovered %lld stuck upload jobs%@"
+ "[NOTICE] Register for BYSetupAssistantFinishedDarwinNotification%@"
+ "[NOTICE] Rejecting all XPC connections%@"
+ "[NOTICE] Trigger %@%@"
+ "[NOTICE] Unregister for BYSetupAssistantFinishedDarwinNotification%@"
+ "[NOTICE] We are in Buddy. Register block [%@] with key [%@]%@"
+ "[NOTICE] We are running as Root user. We should reject all XPC connections%@"
+ "[NOTICE] got interrupted%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ is busy date: %@%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ is ignored by FP: %@%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ is ignored from sync: %@%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ is located in an invalid container: %@%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ is not located in synced location: %@%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ is root owned: %@%@"
+ "[NOTICE] item with rowID %@ docID %@ and fileID %@ was not found on disk%@"
+ "[WARNING] %@ - Failed updating (%d -> %d) domain %@: %@%@"
+ "[WARNING] Can't find Mobile Documents path for current persona%@"
+ "[WARNING] Received modify item request while we have un-acked in-flight diffs for %@. Returning with an error to retry later%@"
+ "[WARNING] We still aren't in a state where load accounts was requested%@"
+ "[WARNING] We were unsuccessful in boosting FP during the startup flow%@"
+ "_apfsAvailableSpace"
+ "_apfsBlockSize"
+ "_apfsEncrypted"
+ "_apfsFlags"
+ "_apfsRole"
+ "_appLibraryMatches"
+ "_bTime"
+ "_bTimeIsBusy"
+ "_checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:"
+ "_createAccountHandlerForAccountID:"
+ "_dbCapabilities"
+ "_dbEffectiveContentPolicy"
+ "_dbErrorCode"
+ "_dbErrorDomain"
+ "_dbFpContentStatus"
+ "_dbFpDeletionStatus"
+ "_dbFpImportStatus"
+ "_dbFsContentStatus"
+ "_dbFsDeletionStatus"
+ "_dbFsImportStatus"
+ "_dbIsApplibrary"
+ "_dbIsPackage"
+ "_dbIsSuper"
+ "_dbSharingState"
+ "_dbTransferState"
+ "_decorateFPFSDomainWithMigrationID"
+ "_diagErrorCode"
+ "_diagErrorDomain"
+ "_diagFailuresBitmap"
+ "_diagUnderlyingErrorCode"
+ "_diagUnderlyingErrorDomain"
+ "_docIDMatches"
+ "_doesAppLibraryMatchWithItemURL:appLibraryRowID:"
+ "_fileForUploadExistsInStage:"
+ "_fileNameExtension"
+ "_fileProviderReadyQueue"
+ "_fpDomain"
+ "_fpReady"
+ "_fpReadyError"
+ "_garbageCollectLiveItemsIncludingActiveItems:"
+ "_garbageCollectUploadsIncludingActiveUploads:"
+ "_gencountDiff"
+ "_getEnterpriseProviderManager"
+ "_getPrimaryProviderManager"
+ "_initWithSyncBubble:isFPFS:"
+ "_interrupted"
+ "_isQuarantined"
+ "_mTime"
+ "_mTimeBeforeMigrationStarted"
+ "_maintainExistingFileProviderDomainsIfNeededWithAccounts:"
+ "_maintainFPDomainsQueue"
+ "_maintainedExistingFPDomains"
+ "_nameIsTrashed"
+ "_nameUnicodeNorm"
+ "_parentMatches"
+ "_pathDepth"
+ "_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:diagnosticDescriptor:"
+ "_purgeATime"
+ "_purgeGenCount"
+ "_purgeSyncRoot"
+ "_registerForBYSetupAssistantFinishedNotification"
+ "_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:"
+ "_resumeSignals"
+ "_scheduleExistingFileProviderDomainsMaintenanceWithAccounts:"
+ "_shouldBoostFileProvider"
+ "_shouldRejectXPCCalls"
+ "_signalFPReady"
+ "_startedWaitingForFP"
+ "_statDirEntryCount"
+ "_statDocID"
+ "_statLogicalSize"
+ "_statPhysicalSize"
+ "_sysDocIDResolutionOK"
+ "_sysPageSize"
+ "_sysUID"
+ "_unlinkContainersWithPristineContainerIDs:containersActualRoot:containers:"
+ "_unlinkContainersWithRootURL:containers:"
+ "_unregisterForBYSetupAssistantFinishedNotification"
+ "_waitForFPSemaphore"
+ "_waitIsOver"
+ "_waitUntilFileProviderIsReady:"
+ "_xattrHasBeforeBounce"
+ "_xattrHasDemotion"
+ "_xattrHasPromotion"
+ "abc.ignore-ck-mmcs-item-not-available-error"
+ "account-session.should.purge.uploads.on.deviceid.change"
+ "apfsAvailableSpace"
+ "apfsBlockSize"
+ "apfsEncrypted"
+ "apfsFlags"
+ "apfsRole"
+ "appLibraryMatches"
+ "bTime"
+ "bTimeIsBusy"
+ "boostFileProvider"
+ "br_update_tables_30_015"
+ "brc_errorItemBusy"
+ "brc_isCloudKitMMCSItemNotAvailable"
+ "callStackSymbols"
+ "daemon-start.setup-assistant-ready.max-wait-time-in-sec"
+ "dbCapabilities"
+ "dbEffectiveContentPolicy"
+ "dbErrorCode"
+ "dbErrorDomain"
+ "dbFpContentStatus"
+ "dbFpDeletionStatus"
+ "dbFpImportStatus"
+ "dbFsContentStatus"
+ "dbFsDeletionStatus"
+ "dbFsImportStatus"
+ "dbIsApplibrary"
+ "dbIsPackage"
+ "dbIsSuper"
+ "dbSharingState"
+ "dbTransferState"
+ "diagErrorCode"
+ "diagErrorDomain"
+ "diagFailuresBitmap"
+ "diagUnderlyingErrorCode"
+ "diagUnderlyingErrorDomain"
+ "docIDMatches"
+ "enableFileProviderBoosting"
+ "exitProcess:"
+ "failModifyRequestsWhenInFlightUnAckedChanges"
+ "file-provider-ready-queue"
+ "fileNameExtension"
+ "fpDomain"
+ "fpfs.sync.fail-modify-requests-with-in-flight-un-acked-changes"
+ "gencountDiff"
+ "getMaintainFPDomainsQueue"
+ "getQueue"
+ "hasApfsAvailableSpace"
+ "hasApfsBlockSize"
+ "hasApfsEncrypted"
+ "hasApfsFlags"
+ "hasApfsRole"
+ "hasAppLibraryMatches"
+ "hasBTime"
+ "hasBTimeIsBusy"
+ "hasDbCapabilities"
+ "hasDbEffectiveContentPolicy"
+ "hasDbErrorCode"
+ "hasDbErrorDomain"
+ "hasDbFpContentStatus"
+ "hasDbFpDeletionStatus"
+ "hasDbFpImportStatus"
+ "hasDbFsContentStatus"
+ "hasDbFsDeletionStatus"
+ "hasDbFsImportStatus"
+ "hasDbIsApplibrary"
+ "hasDbIsPackage"
+ "hasDbIsSuper"
+ "hasDbSharingState"
+ "hasDbTransferState"
+ "hasDiagErrorCode"
+ "hasDiagErrorDomain"
+ "hasDiagFailuresBitmap"
+ "hasDiagUnderlyingErrorCode"
+ "hasDiagUnderlyingErrorDomain"
+ "hasDocIDMatches"
+ "hasFileNameExtension"
+ "hasGencountDiff"
+ "hasIsQuarantined"
+ "hasMTime"
+ "hasMTimeBeforeMigrationStarted"
+ "hasNameIsTrashed"
+ "hasNameUnicodeNorm"
+ "hasParentMatches"
+ "hasPathDepth"
+ "hasPurgeATime"
+ "hasPurgeGenCount"
+ "hasPurgeSyncRoot"
+ "hasStatDirEntryCount"
+ "hasStatDocID"
+ "hasStatLogicalSize"
+ "hasStatPhysicalSize"
+ "hasSysDocIDResolutionOK"
+ "hasSysPageSize"
+ "hasSysUID"
+ "hasXattrHasBeforeBounce"
+ "hasXattrHasDemotion"
+ "hasXattrHasPromotion"
+ "ignoreCKMMCSItemNotAvailableErrorForABC"
+ "interrupt"
+ "isQuarantined"
+ "mTime"
+ "mTimeBeforeMigrationStarted"
+ "maintain-fp-domains"
+ "nameIsTrashed"
+ "nameUnicodeNorm"
+ "openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:"
+ "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:"
+ "openDBForNewDomain:deviceIDChanged:withError:"
+ "parentMatches"
+ "pathDepth"
+ "purgeATime"
+ "purgeAllUploads"
+ "purgeGenCount"
+ "purgeSyncRoot"
+ "setApfsAvailableSpace:"
+ "setApfsBlockSize:"
+ "setApfsEncrypted:"
+ "setApfsFlags:"
+ "setApfsRole:"
+ "setAppLibraryMatches:"
+ "setBTime:"
+ "setBTimeIsBusy:"
+ "setDbCapabilities:"
+ "setDbEffectiveContentPolicy:"
+ "setDbErrorCode:"
+ "setDbErrorDomain:"
+ "setDbFpContentStatus:"
+ "setDbFpDeletionStatus:"
+ "setDbFpImportStatus:"
+ "setDbFsContentStatus:"
+ "setDbFsDeletionStatus:"
+ "setDbFsImportStatus:"
+ "setDbIsApplibrary:"
+ "setDbIsPackage:"
+ "setDbIsSuper:"
+ "setDbSharingState:"
+ "setDbTransferState:"
+ "setDiagErrorCode:"
+ "setDiagErrorDomain:"
+ "setDiagFailuresBitmap:"
+ "setDiagUnderlyingErrorCode:"
+ "setDiagUnderlyingErrorDomain:"
+ "setDocIDMatches:"
+ "setFileNameExtension:"
+ "setFpDomain:"
+ "setGencountDiff:"
+ "setHasApfsAvailableSpace:"
+ "setHasApfsBlockSize:"
+ "setHasApfsEncrypted:"
+ "setHasApfsFlags:"
+ "setHasApfsRole:"
+ "setHasAppLibraryMatches:"
+ "setHasBTime:"
+ "setHasBTimeIsBusy:"
+ "setHasDbCapabilities:"
+ "setHasDbEffectiveContentPolicy:"
+ "setHasDbErrorCode:"
+ "setHasDbFpContentStatus:"
+ "setHasDbFpDeletionStatus:"
+ "setHasDbFpImportStatus:"
+ "setHasDbFsContentStatus:"
+ "setHasDbFsDeletionStatus:"
+ "setHasDbFsImportStatus:"
+ "setHasDbIsApplibrary:"
+ "setHasDbIsPackage:"
+ "setHasDbIsSuper:"
+ "setHasDbSharingState:"
+ "setHasDbTransferState:"
+ "setHasDiagErrorCode:"
+ "setHasDiagFailuresBitmap:"
+ "setHasDiagUnderlyingErrorCode:"
+ "setHasDocIDMatches:"
+ "setHasGencountDiff:"
+ "setHasIsQuarantined:"
+ "setHasMTime:"
+ "setHasMTimeBeforeMigrationStarted:"
+ "setHasNameIsTrashed:"
+ "setHasParentMatches:"
+ "setHasPathDepth:"
+ "setHasPurgeATime:"
+ "setHasPurgeGenCount:"
+ "setHasPurgeSyncRoot:"
+ "setHasStatDirEntryCount:"
+ "setHasStatDocID:"
+ "setHasStatLogicalSize:"
+ "setHasStatPhysicalSize:"
+ "setHasSysDocIDResolutionOK:"
+ "setHasSysPageSize:"
+ "setHasSysUID:"
+ "setHasXattrHasBeforeBounce:"
+ "setHasXattrHasDemotion:"
+ "setHasXattrHasPromotion:"
+ "setIsQuarantined:"
+ "setMTime:"
+ "setMTimeBeforeMigrationStarted:"
+ "setNameIsTrashed:"
+ "setNameUnicodeNorm:"
+ "setParentMatches:"
+ "setPathDepth:"
+ "setPurgeATime:"
+ "setPurgeGenCount:"
+ "setPurgeSyncRoot:"
+ "setStatDirEntryCount:"
+ "setStatDocID:"
+ "setStatLogicalSize:"
+ "setStatPhysicalSize:"
+ "setSysDocIDResolutionOK:"
+ "setSysPageSize:"
+ "setSysUID:"
+ "setXattrHasBeforeBounce:"
+ "setXattrHasDemotion:"
+ "setXattrHasPromotion:"
+ "setupAssistantReadyMaxWaitTimeInSec"
+ "sharedInstance"
+ "shouldFileIDBeIgnoredAsNonMigrated:docID:deviceID:isRegFile:rowid:outItemURL:isBusyDate:isIgnoredFromSync:"
+ "shouldPurgeUploadsOnDeviceIDChange"
+ "shouldRejectXPCCalls"
+ "statDirEntryCount"
+ "statDocID"
+ "statLogicalSize"
+ "statPhysicalSize"
+ "sysDocIDResolutionOK"
+ "sysPageSize"
+ "sysUID"
+ "unreachable: FP is not ready but we don't have an error"
+ "v24@?0@\"NSError\"8@\"<FPDWakeupTransaction>\"16"
+ "v48@0:8@16@24B32B36^B40"
+ "wakeUpForURL:completionHandler:"
+ "xattrHasBeforeBounce"
+ "xattrHasDemotion"
+ "xattrHasPromotion"
+ "{?=\"apfsAvailableSpace\"b1\"apfsBlockSize\"b1\"apfsFlags\"b1\"apfsRole\"b1\"bTime\"b1\"cloneErrorCode\"b1\"dbCapabilities\"b1\"dbEffectiveContentPolicy\"b1\"dbErrorCode\"b1\"dbFpContentStatus\"b1\"dbFpDeletionStatus\"b1\"dbFpImportStatus\"b1\"dbFsContentStatus\"b1\"dbFsDeletionStatus\"b1\"dbFsImportStatus\"b1\"dbGenCount\"b1\"dbSharingState\"b1\"dbTransferState\"b1\"diagErrorCode\"b1\"diagFailuresBitmap\"b1\"diagUnderlyingErrorCode\"b1\"fileNameLength\"b1\"fsGenCount\"b1\"gencountDiff\"b1\"itemNumber\"b1\"mTime\"b1\"pathDepth\"b1\"pathLength\"b1\"purgeATime\"b1\"purgeGenCount\"b1\"purgeSyncRoot\"b1\"readErrorCode\"b1\"stFlags\"b1\"stMode\"b1\"statDirEntryCount\"b1\"statDocID\"b1\"statLogicalSize\"b1\"statPhysicalSize\"b1\"sysPageSize\"b1\"sysUID\"b1\"compressionType\"b1\"dataProtectionClass\"b1\"itemType\"b1\"syncRootEnum\"b1\"xattrCount\"b1\"apfsEncrypted\"b1\"appLibraryMatches\"b1\"bTimeIsBusy\"b1\"dbIsApplibrary\"b1\"dbIsPackage\"b1\"dbIsSuper\"b1\"doGenCountsMatchInFileId\"b1\"docIDMatches\"b1\"hasAcls\"b1\"hasLocalChanges\"b1\"hasMoreLinks\"b1\"isAppleDouble\"b1\"isBundleBit\"b1\"isFileNameNonAscii\"b1\"isOwnedByLoggedInUser\"b1\"isOwnedByRoot\"b1\"isPurgable\"b1\"isQuarantined\"b1\"isResourceFork\"b1\"isSparseFile\"b1\"isUnderDirStatFolder\"b1\"isUrgent\"b1\"mTimeBeforeMigrationStarted\"b1\"nameIsTrashed\"b1\"parentHasAcls\"b1\"parentMatches\"b1\"sysDocIDResolutionOK\"b1\"xattrHasBeforeBounce\"b1\"xattrHasDemotion\"b1\"xattrHasPromotion\"b1}"
+ "\xf0\xf0\xb5\x11\x11"
- "\t\x15\x17\xf0/\x01\x11\x12\x1f\b"
- "+[BRCAccountSessionFPFS(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:error:]"
- "+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:]"
- "+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]"
- "+[BRCAccountSessionFPFS(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]_block_invoke"
- "+[BRCImportUtil shouldFileIDBeIgnoredAsNonMigrated:deviceID:isRegFile:rowid:isBusyDate:isIgnoredFromSync:]"
- "-[BRCAccountSessionFPFS _unlinkContainersWithRootURL:]"
- "-[BRCAccountSessionFPFS(BRCDatabaseManager) openDBForNewDomain:withError:]"
- "-[BRCBuddyFlowObserver _registerForSetupAssistantFinishedNotification]"
- "-[BRCBuddyFlowObserver _unregisterForSetupAssistantFinishedNotification]"
- "-[BRCDaemonFPFS start]_block_invoke_2"
- "-[BRCDaemonFPFS start]_block_invoke_4"
- "-[BRCStageRegistry _garbageCollectUploads]_block_invoke"
- "B48@0:8@16B24@28B36^@40"
- "B52@0:8@16B24^I28^I36^@44"
- "B60@0:8@16@24B32@36^B44^B52"
- "B72@0:8@16B24@28@36B44^I48^I56^@64"
- "TB,N,V_isQuerantined"
- "UPDATE client_items SET item_file_id = call_block(%p, item_file_id, item_type, item_localsyncupstate, rowid, item_generation, item_local_diffs), item_generation = call_block(%p, item_generation, item_type, item_localsyncupstate), item_localsyncupstate = call_block(%p, item_localsyncupstate, rowid, item_stat_ckinfo IS NULL, item_type, item_birthtime, item_id, item_filename, version_content_signature, item_parent_zone_rowid, item_parent_id), item_doc_id = NULL WHERE rowid > %llu ORDER BY rowid ASC LIMIT %llu"
- "Waiting without succees for FP to accept XPCs: %@"
- "[CRIT] Assertion failed: argc == 3 || argc == 6%@"
- "[DEBUG] Buddy has finished. Execute block [%@]%@"
- "[DEBUG] Key %@ already registered%@"
- "[DEBUG] Register for BYSetupAssistantFinishedDarwinNotification%@"
- "[DEBUG] SetupAssistantNeedsToRun --> pausing daemon startup until done.%@"
- "[DEBUG] Trigger %@%@"
- "[DEBUG] Unregister for BYSetupAssistantFinishedDarwinNotification%@"
- "[DEBUG] Unregister for SetupAssistantFinishedNotification%@"
- "[DEBUG] We are in Buddy. Register block [%@] with key [%@]%@"
- "[DEBUG] We received an asset unavailable error but it exists in the correct place. This must be a file protected file%@"
- "[DEBUG] received BYSetupAssistantFinishedDarwinNotification%@"
- "[DEBUG] ┏%llx received new XPC connection: %@%@"
- "[ERROR] Got an error when trying to find a domain to remove: %@%@"
- "[ERROR] failed getting URL of item with rowID %@ and fileID %@: %@%@"
- "[ERROR] item with rowID %@ and fileID %@ got left behind when migrating: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ is busy date: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ is ignored by FP: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ is ignored from sync: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ is located in an invalid container: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ is not located in synced location: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ is root owned: %@%@"
- "[NOTICE] item with rowID %@ and fileID %@ was not found on disk%@"
- "[WARNING] Not waiting for account %@ loading synchronously since we did not yet kick loadAccounts request%@"
- "_checkIntegrity:serverTruth:session:skipControlFiles:error:"
- "_isQuerantined"
- "_populateNonMigratedItemEventForLocalDataWithEvent:fileIDData:"
- "_registerForSetupAssistantFinishedNotification"
- "_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:"
- "_unlinkContainersWithPristineContainerIDs:containersActualRoot:"
- "_unlinkContainersWithRootURL:"
- "_unregisterForSetupAssistantFinishedNotification"
- "br_getDomainForDataSeparated:withIdentifier:withError:"
- "buddy-finished-notification-queue"
- "hasIsQuerantined"
- "initWithSyncBubble:isFPFS:"
- "isQuerantined"
- "openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:error:"
- "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:"
- "openDBForNewDomain:withError:"
- "setHasIsQuerantined:"
- "setIsQuerantined:"
- "shouldFileIDBeIgnoredAsNonMigrated:deviceID:isRegFile:rowid:isBusyDate:isIgnoredFromSync:"
- "v32@0:8@16^@24"
- "v40@0:8@16@24B32B36"
- "{?=\"cloneErrorCode\"b1\"dbGenCount\"b1\"fileNameLength\"b1\"fsGenCount\"b1\"itemNumber\"b1\"pathLength\"b1\"readErrorCode\"b1\"stFlags\"b1\"stMode\"b1\"compressionType\"b1\"dataProtectionClass\"b1\"itemType\"b1\"syncRootEnum\"b1\"xattrCount\"b1\"doGenCountsMatchInFileId\"b1\"hasAcls\"b1\"hasLocalChanges\"b1\"hasMoreLinks\"b1\"isAppleDouble\"b1\"isBundleBit\"b1\"isFileNameNonAscii\"b1\"isOwnedByLoggedInUser\"b1\"isOwnedByRoot\"b1\"isPurgable\"b1\"isQuerantined\"b1\"isResourceFork\"b1\"isSparseFile\"b1\"isUnderDirStatFolder\"b1\"isUrgent\"b1\"parentHasAcls\"b1}"
- "\xa1\x11"

```
