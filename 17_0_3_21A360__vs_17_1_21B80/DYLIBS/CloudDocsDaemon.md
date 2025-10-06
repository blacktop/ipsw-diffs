## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-2461.2.1.0.0
-  __TEXT.__text: 0x320e04
+2461.40.47.0.0
+  __TEXT.__text: 0x32a27c
   __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0x169d4
+  __TEXT.__objc_methlist: 0x1743c
   __TEXT.__const: 0x3e0
-  __TEXT.__cstring: 0x7ae1f
-  __TEXT.__oslogstring: 0x4322c
-  __TEXT.__gcc_except_tab: 0x18394
+  __TEXT.__cstring: 0x7b43f
+  __TEXT.__oslogstring: 0x434df
+  __TEXT.__gcc_except_tab: 0x1844c
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x9144
-  __TEXT.__objc_classname: 0x22d7
-  __TEXT.__objc_methname: 0x3a7c3
-  __TEXT.__objc_methtype: 0x7b09
-  __TEXT.__objc_stubs: 0x2a900
-  __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0x88f8
+  __TEXT.__unwind_info: 0x91b0
+  __TEXT.__objc_classname: 0x22de
+  __TEXT.__objc_methname: 0x3c1e5
+  __TEXT.__objc_methtype: 0x7e61
+  __TEXT.__objc_stubs: 0x2b140
+  __DATA_CONST.__got: 0xb98
+  __DATA_CONST.__const: 0x8920
   __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35078
-  __DATA_CONST.__objc_selrefs: 0xcc88
+  __DATA_CONST.__objc_const: 0x35e30
+  __DATA_CONST.__objc_selrefs: 0xd380
   __DATA_CONST.__objc_arraydata: 0xdd0
-  __AUTH_CONST.__const: 0x24a8
-  __AUTH_CONST.__objc_const: 0x6908
-  __AUTH_CONST.__cfstring: 0x1fb20
+  __AUTH_CONST.__const: 0x24c8
+  __AUTH_CONST.__objc_const: 0x6950
+  __AUTH_CONST.__cfstring: 0x201e0
   __AUTH_CONST.__objc_intobj: 0xb10
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH.__objc_data: 0x2260
   __AUTH.__data: 0x18
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xd28
+  __DATA.__objc_classrefs: 0xd38
   __DATA.__objc_superrefs: 0x800
-  __DATA.__objc_ivar: 0x1e98
+  __DATA.__objc_ivar: 0x1f88
   __DATA.__data: 0x1ff0
-  __DATA.__bss: 0x320
+  __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x3480
   __DATA_DIRTY.__data: 0x2c8
   __DATA_DIRTY.__bss: 0x268

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 606B9FD9-622E-3933-833C-902253CD0F03
-  Functions: 14174
-  Symbols:   42241
-  CStrings:  26569
+  UUID: E18DF612-E343-35FE-A6FC-7D0A1A16955F
+  Functions: 14396
+  Symbols:   42866
+  CStrings:  27035
 
Symbols:
+ +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:]
+ +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:].cold.1
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.1
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.2
+ +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]
+ +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:].cold.1
+ +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.3
+ +[BRCFileProviderDaemonUtils sharedInstance]
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
+ -[BRCAccountHandler _tryToOpenSession:error:].cold.5
+ -[BRCAccountSession fpDomain]
+ -[BRCAccountSession setFpDomain:]
+ -[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:]
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
+ -[BRCDaemon _resumeSignals]
+ -[BRCDaemon shouldRejectXPCCalls]
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
+ -[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]
+ -[BRCStageRegistry purgeAllUploads]
+ -[BRCStageRegistry purgeAllUploads].cold.1
+ -[BRCUserDefaults ignoreCKMMCSItemNotAvailableErrorForABC]
+ -[BRCUserDefaults setupAssistantReadyMaxWaitTimeInSec]
+ -[BRCUserDefaults shouldPurgeUploadsOnDeviceIDChange]
+ -[NSError(BRCAdditions) brc_isCloudKitMMCSItemNotAvailable]
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
+ OBJC_IVAR_$_BRCAccountSession._fpDomain
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
+ _OBJC_CLASS_$_FPDaemonConnection
+ _OBJC_IVAR_$_BRCAccountsManager._maintainFPDomainsQueue
+ _OBJC_IVAR_$_BRCAccountsManager._maintainedExistingFPDomains
+ _OBJC_IVAR_$_BRCDaemon._shouldRejectXPCCalls
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._fileProviderReadyQueue
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._fpReady
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._fpReadyError
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._interrupted
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._shouldBoostFileProvider
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._startedWaitingForFP
+ _OBJC_IVAR_$_BRCFileProviderDaemonUtils._waitForFPSemaphore
+ __OBJC_$_CLASS_METHODS_BRCFileProviderDaemonUtils
+ ___166+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke
+ ___166+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke.cold.1
+ ___18-[BRCDaemon start]_block_invoke_4
+ ___23-[BRCDaemon selfCheck:]_block_invoke.145
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.47
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.50
+ ___44+[BRCFileProviderDaemonUtils sharedInstance]_block_invoke
+ ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.80
+ ___47-[BRCFileProviderDaemonUtils boostFileProvider]_block_invoke
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.131
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.131.cold.1
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.137
+ ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke
+ ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke.cold.1
+ ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke_2
+ ___69-[BRCFileProviderDaemonUtils waitForFPToBeReadyToAcceptXPCWithError:]_block_invoke.14
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.19
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.19.cold.1
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.21
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.21.cold.1
+ ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.6
+ ___74-[BRCAccountsManager createSessionWithACAccountID:dsid:completionHandler:]_block_invoke_3
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.64.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.65
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.66
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40r_e44_v24?0"NSError"8"<FPDWakeupTransaction>"16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e24_"BRCAccountHandler"8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8s40l8r48l8
+ ___block_descriptor_90_e8_32s40s48s56r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8r56l8
+ ___block_literal_global.124
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.53
+ ___block_literal_global.61
+ ___block_literal_global.788
+ ___block_literal_global.86
+ __unnamed_array_storage.2619
+ __unnamed_array_storage.2631
+ __unnamed_array_storage.2717
+ _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:
+ _objc_msgSend$_createAccountHandlerForAccountID:
+ _objc_msgSend$_garbageCollectUploadsIncludingActiveUploads:
+ _objc_msgSend$_getEnterpriseProviderManager
+ _objc_msgSend$_initWithSyncBubble:isFPFS:
+ _objc_msgSend$_maintainExistingFileProviderDomainsIfNeededWithAccounts:
+ _objc_msgSend$_registerForBYSetupAssistantFinishedNotification
+ _objc_msgSend$_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:
+ _objc_msgSend$_resumeSignals
+ _objc_msgSend$_scheduleExistingFileProviderDomainsMaintenanceWithAccounts:
+ _objc_msgSend$_signalFPReady
+ _objc_msgSend$_unregisterForBYSetupAssistantFinishedNotification
+ _objc_msgSend$_waitIsOver
+ _objc_msgSend$_waitUntilFileProviderIsReady:
+ _objc_msgSend$boostFileProvider
+ _objc_msgSend$br_getPrimaryProviderManager
+ _objc_msgSend$brc_isCloudKitMMCSItemNotAvailable
+ _objc_msgSend$callStackSymbols
+ _objc_msgSend$enableFileProviderBoosting
+ _objc_msgSend$exitProcess:
+ _objc_msgSend$fpDomain
+ _objc_msgSend$ignoreCKMMCSItemNotAvailableErrorForABC
+ _objc_msgSend$interrupt
+ _objc_msgSend$openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:deviceIDChanged:error:
+ _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:
+ _objc_msgSend$setApfsAvailableSpace:
+ _objc_msgSend$setApfsBlockSize:
+ _objc_msgSend$setApfsEncrypted:
+ _objc_msgSend$setApfsFlags:
+ _objc_msgSend$setApfsRole:
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
+ _objc_msgSend$setFileNameExtension:
+ _objc_msgSend$setFpDomain:
+ _objc_msgSend$setIsQuarantined:
+ _objc_msgSend$setMTime:
+ _objc_msgSend$setNameIsTrashed:
+ _objc_msgSend$setNameUnicodeNorm:
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
+ _objc_msgSend$shouldRejectXPCCalls
+ _objc_msgSend$synchronousSharedConnectionProxy
+ _objc_msgSend$wakeUpForURL:completionHandler:
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
- +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:error:]
- +[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:error:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:]
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:].cold.2
- +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]
- +[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:].cold.1
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation hasIsQuerantined]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation isQuerantined]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setHasIsQuerantined:]
- -[AppTelemetryFPFSMigrationNonMigratedItemInvestigation setIsQuerantined:]
- -[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:error:]
- -[BRCBuddyFlowObserver _registerForSetupAssistantFinishedNotification]
- -[BRCBuddyFlowObserver _registerForSetupAssistantFinishedNotification].cold.1
- -[BRCBuddyFlowObserver _stopObservingBuddyAndExecuteCallbacks].cold.1
- -[BRCBuddyFlowObserver _stopObservingBuddyAndExecuteCallbacks].cold.2
- -[BRCBuddyFlowObserver _unregisterForSetupAssistantFinishedNotification]
- -[BRCBuddyFlowObserver _unregisterForSetupAssistantFinishedNotification].cold.1
- -[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:].cold.1
- -[BRCFileProviderDaemonUtils initWithSyncBubble:isFPFS:]
- GCC_except_table75
- GCC_except_table83
- OBJC_IVAR_$_AppTelemetryFPFSMigrationNonMigratedItemInvestigation._isQuerantined
- _OBJC_IVAR_$_BRCBuddyFlowObserver._notificationQueue
- ___150+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]_block_invoke
- ___150+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]_block_invoke.cold.1
- ___18-[BRCDaemon start]_block_invoke.cold.2
- ___18-[BRCDaemon start]_block_invoke_2.97
- ___18-[BRCDaemon start]_block_invoke_2.cold.1
- ___23-[BRCDaemon selfCheck:]_block_invoke.149
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.46
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.52
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.cold.3
- ___42-[BRCStageRegistry _garbageCollectUploads]_block_invoke
- ___42-[BRCStageRegistry _garbageCollectUploads]_block_invoke.cold.1
- ___42-[BRCStageRegistry _garbageCollectUploads]_block_invoke_2
- ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.77
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.136
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.136.cold.1
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.141
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.18
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.18.cold.1
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.20
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.20.cold.1
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.cold.4
- ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.7
- ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.7.cold.1
- ___73-[BRCBuddyFlowObserver observeBuddyIfNecessaryWithKey:block:description:]_block_invoke.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.62
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.63.cold.1
- ____buddyHasFinished_block_invoke
- ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e24_"BRCAccountHandler"8?0ls32l8s40l8
- ___block_descriptor_82_e8_32s40s48s56r_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.132
- ___block_literal_global.145
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.194
- ___block_literal_global.196
- ___block_literal_global.199
- ___block_literal_global.55
- ___block_literal_global.60
- ___block_literal_global.71
- ___block_literal_global.776
- ___block_literal_global.80
- __buddyHasFinished.cold.1
- __unnamed_array_storage.2616
- __unnamed_array_storage.2628
- __unnamed_array_storage.2714
- _objc_msgSend$_checkIntegrity:serverTruth:session:skipControlFiles:error:
- _objc_msgSend$_registerForSetupAssistantFinishedNotification
- _objc_msgSend$_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:
- _objc_msgSend$_unregisterForSetupAssistantFinishedNotification
- _objc_msgSend$br_getDomainForDataSeparated:withIdentifier:withError:
- _objc_msgSend$initWithSyncBubble:isFPFS:
- _objc_msgSend$openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:error:
- _objc_msgSend$openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:
- _objc_msgSend$setIsQuerantined:
CStrings:
+ "\x04\x12"
+ "\x05\x14\x15\x11\x11\x11"
+ "\t\x158\xf0/5\x11\x14\x1f\n"
+ "\x11\x12"
+ "+[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:deviceIDChanged:error:]"
+ "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]"
+ "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]"
+ "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:deviceIDChanged:error:]_block_invoke"
+ "-[BRCAccountsManager _maintainExistingFileProviderDomainsIfNeededWithAccounts:]"
+ "-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke"
+ "-[BRCAccountsManager _waitUntilFileProviderIsReady:]"
+ "-[BRCBuddyFlowObserver _registerForBYSetupAssistantFinishedNotification]"
+ "-[BRCBuddyFlowObserver _unregisterForBYSetupAssistantFinishedNotification]"
+ "-[BRCDaemon shouldRejectXPCCalls]"
+ "-[BRCDaemon start]_block_invoke_5"
+ "-[BRCFileProviderDaemonUtils _signalFPReady]"
+ "-[BRCFileProviderDaemonUtils boostFileProvider]"
+ "-[BRCFileProviderDaemonUtils interrupt]"
+ "-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke"
+ "-[BRCStageRegistry purgeAllUploads]"
+ "@\"NSFileProviderDomain\""
+ "B56@0:8@16B24@28B36^B40^@48"
+ "B60@0:8@16B24^I28^I36^B44^@52"
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
+ "[CRIT] UNREACHABLE: FP is not ready but we don't have an error%@"
+ "[DEBUG] FP is already ready to connect after boosting%@"
+ "[DEBUG] Ignoring CloudKit open error (Operation not permitted) protected class error %ld%@"
+ "[DEBUG] Insering alias tombstone for %@%@"
+ "[DEBUG] Purging all uploads and live items%@"
+ "[DEBUG] Starting to wait for FP to be ready to accept xpc connections%@"
+ "[DEBUG] ┏%llx received new XPC connection: %@, for uid: %u%@"
+ "[ERROR] Failed waiting for File Provider to be ready: %@%@"
+ "[ERROR] Waiting without succees for FP to accept XPCs: %@%@"
+ "[NOTICE] BYSetupAssistantFinishedDarwinNotification was received%@"
+ "[NOTICE] BYSetupAssistantNeedsToRun --> pausing daemon startup until done.%@"
+ "[NOTICE] Buddy has finished. Execute block [%@]%@"
+ "[NOTICE] FP is now ready to accept xpc connections%@"
+ "[NOTICE] Key %@ already registered%@"
+ "[NOTICE] Register for BYSetupAssistantFinishedDarwinNotification%@"
+ "[NOTICE] Rejecting all XPC connections%@"
+ "[NOTICE] Trigger %@%@"
+ "[NOTICE] Unregister for BYSetupAssistantFinishedDarwinNotification%@"
+ "[NOTICE] We are in Buddy. Register block [%@] with key [%@]%@"
+ "[NOTICE] We are running as Root user. We should reject all XPC connections%@"
+ "[NOTICE] got interrupted%@"
+ "[WARNING] Can't find Mobile Documents path for current persona%@"
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
+ "_diagErrorCode"
+ "_diagErrorDomain"
+ "_diagFailuresBitmap"
+ "_diagUnderlyingErrorCode"
+ "_diagUnderlyingErrorDomain"
+ "_docIDMatches"
+ "_fileNameExtension"
+ "_fileProviderReadyQueue"
+ "_fpDomain"
+ "_fpReady"
+ "_fpReadyError"
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
+ "br_getPrimaryProviderManager"
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
+ "file-provider-ready-queue"
+ "fileNameExtension"
+ "fpDomain"
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
+ "shouldPurgeUploadsOnDeviceIDChange"
+ "shouldRejectXPCCalls"
+ "statDirEntryCount"
+ "statDocID"
+ "statLogicalSize"
+ "statPhysicalSize"
+ "synchronousSharedConnectionProxy"
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
- "\x03\x12"
- "\x05\x14\x16\x11\x11"
- "\t\x157\xf0/5\x11\x14\x1f\n"
- "+[BRCAccountSession(BRCDatabaseManager) _checkIntegrity:serverTruth:session:skipControlFiles:error:]"
- "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:]"
- "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]"
- "+[BRCAccountSession(BRCDatabaseManager) openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:]_block_invoke"
- "-[BRCBuddyFlowObserver _registerForSetupAssistantFinishedNotification]"
- "-[BRCBuddyFlowObserver _unregisterForSetupAssistantFinishedNotification]"
- "-[BRCDaemon start]_block_invoke_2"
- "-[BRCDaemon start]_block_invoke_4"
- "-[BRCStageRegistry _garbageCollectUploads]_block_invoke"
- "B48@0:8@16B24@28B36^@40"
- "B52@0:8@16B24^I28^I36^@44"
- "B72@0:8@16B24@28@36B44^I48^I56^@64"
- "TB,N,V_isQuerantined"
- "Waiting without succees for FP to accept XPCs: %@"
- "[DEBUG] Buddy has finished. Execute block [%@]%@"
- "[DEBUG] Key %@ already registered%@"
- "[DEBUG] Register for BYSetupAssistantFinishedDarwinNotification%@"
- "[DEBUG] SetupAssistantNeedsToRun --> pausing daemon startup until done.%@"
- "[DEBUG] Trigger %@%@"
- "[DEBUG] Unregister for BYSetupAssistantFinishedDarwinNotification%@"
- "[DEBUG] Unregister for SetupAssistantFinishedNotification%@"
- "[DEBUG] We are in Buddy. Register block [%@] with key [%@]%@"
- "[DEBUG] received BYSetupAssistantFinishedDarwinNotification%@"
- "[DEBUG] ┏%llx received new XPC connection: %@%@"
- "[ERROR] Got an error when trying to find a domain to remove: %@%@"
- "[WARNING] Not waiting for account %@ loading synchronously since we did not yet kick loadAccounts request%@"
- "_checkIntegrity:serverTruth:session:skipControlFiles:error:"
- "_isQuerantined"
- "_registerForSetupAssistantFinishedNotification"
- "_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:"
- "_unregisterForSetupAssistantFinishedNotification"
- "br_getDomainForDataSeparated:withIdentifier:withError:"
- "buddy-finished-notification-queue"
- "hasIsQuerantined"
- "initWithSyncBubble:isFPFS:"
- "isQuerantined"
- "openAndValidateDatabase:serverTruth:initialVersion:lastCurrentVersion:error:"
- "openAndValidateDatabase:serverTruth:session:baseURL:skipControlFiles:initialVersion:lastCurrentVersion:error:"
- "setHasIsQuerantined:"
- "setIsQuerantined:"
- "v40@0:8@16@24B32B36"
- "{?=\"cloneErrorCode\"b1\"dbGenCount\"b1\"fileNameLength\"b1\"fsGenCount\"b1\"itemNumber\"b1\"pathLength\"b1\"readErrorCode\"b1\"stFlags\"b1\"stMode\"b1\"compressionType\"b1\"dataProtectionClass\"b1\"itemType\"b1\"syncRootEnum\"b1\"xattrCount\"b1\"doGenCountsMatchInFileId\"b1\"hasAcls\"b1\"hasLocalChanges\"b1\"hasMoreLinks\"b1\"isAppleDouble\"b1\"isBundleBit\"b1\"isFileNameNonAscii\"b1\"isOwnedByLoggedInUser\"b1\"isOwnedByRoot\"b1\"isPurgable\"b1\"isQuerantined\"b1\"isResourceFork\"b1\"isSparseFile\"b1\"isUnderDirStatFolder\"b1\"isUrgent\"b1\"parentHasAcls\"b1}"
- "\xa1\x11"

```
