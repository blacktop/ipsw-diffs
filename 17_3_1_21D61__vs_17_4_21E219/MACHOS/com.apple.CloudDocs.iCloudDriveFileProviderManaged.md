## com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

-2461.80.8.0.0
-  __TEXT.__text: 0x289dc
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x3580
-  __TEXT.__objc_methlist: 0x11a0
-  __TEXT.__cstring: 0x40aa
-  __TEXT.__objc_methname: 0x5415
-  __TEXT.__objc_classname: 0x74a
-  __TEXT.__objc_methtype: 0x2dc4
+2720.100.117.0.0
+  __TEXT.__text: 0x27640
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x2b80
+  __TEXT.__objc_methlist: 0x1100
+  __TEXT.__gcc_except_tab: 0x2224
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x21f4
-  __TEXT.__oslogstring: 0x25ea
-  __TEXT.__unwind_info: 0xa3c
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x1128
-  __DATA_CONST.__cfstring: 0x480
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__objc_methname: 0x4f0b
+  __TEXT.__cstring: 0x4225
+  __TEXT.__oslogstring: 0x2190
+  __TEXT.__objc_classname: 0x77b
+  __TEXT.__objc_methtype: 0x32e3
+  __TEXT.__unwind_info: 0x9fc
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0xf90
+  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x9ed0
-  __DATA.__objc_selrefs: 0x1040
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x250
-  __DATA.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA.__objc_const: 0x9f10
+  __DATA.__objc_selrefs: 0xde8
   __DATA.__objc_ivar: 0x13c
-  __DATA.__objc_data: 0xa00
+  __DATA.__objc_data: 0x9b0
   __DATA.__data: 0xb40
   __DATA.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 76894F17-5D80-31BD-97A5-EDDD30F533CB
-  Functions: 757
-  Symbols:   222
-  CStrings:  1547
+  UUID: 14D20655-4EED-3908-8851-EB777DF5D4B0
+  Functions: 708
+  Symbols:   206
+  CStrings:  1452
 
Symbols:
+ _ICDClientSideCollaborationServiceName
+ _OBJC_CLASS_$_BRCDeviceConfiguration
+ _OBJC_CLASS_$_BRCDocumentSignatureCalculator
+ _OBJC_CLASS_$_ICDCollaborationVersion
+ __os_feature_enabled_impl
- _BRCIsBusyDate
- _BRCiconiaServiceName
- _BREnableCiconiaContext
- _BREntitlementCiconia
- _BRUbiquitousDefaultContainerID
- _FPNotSupportedError
- _NSFileModificationDate
- _NSFileProviderErrorSpeculativeCanceledByProvider
- _OBJC_CLASS_$_BRCAccountSessionFPFS
- _OBJC_CLASS_$_BRCImportBookmark
- _OBJC_CLASS_$_BRCNotification
- _OBJC_CLASS_$_BRDSIDString
- _OBJC_CLASS_$_BRDeviceConfiguration
- _OBJC_CLASS_$_BRMangledID
- _OBJC_CLASS_$_BRQueryItem
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSXPCConnection
- _access
- _dispatch_async_and_wait
- _objc_release_x1
- _objc_storeWeak
CStrings:
+ "\x02\x12"
+ "\x05D"
+ "-[ICDFileEnumerator initWithFileObjectID:itemIdentifier:recursive:]_block_invoke"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy calculateCollaborationVersionForContents:reply:]"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy fetchLatestRevisionIntoURL:reply:]"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy fetchLatestRevisionIntoURL:reply:]_block_invoke"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy fetchLatestRevisionWithReply:]"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy fetchLatestRevisionWithReply:]_block_invoke"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:reply:]"
+ "-[ICDFileProviderClientSideCollaborationServiceSource listener:shouldAcceptNewConnection:]_block_invoke"
+ "-[ICDFileProviderExtension _getQueryItemForFileObjectID:completionHandler:]"
+ "-[ICDFileProviderExtension enumeratorForVersionsOfItemWithIdentifier:request:error:]"
+ "-[ICDFileProviderExtension waitForStabilizationWithCompletionHandler:]"
+ "-[ICDFileProviderExtension waitForStabilizationWithCompletionHandler:]_block_invoke"
+ "-[ICDFileProviderExtension(Thumbnails) _fetchThumbnailsForItemIdentifiersWithVersionMap:requestedSize:perThumbnailCompletionHandler:completionHandler:]_block_invoke_2"
+ "-[ICDFileProviderItemServiceProxy getSaltingVerificationKeys:]"
+ "-[ICDFileProviderItemServiceProxy getSaltingVerificationKeys:]_block_invoke"
+ "-[ICDFileProviderItemServiceProxy refreshSharingState:]"
+ "-[ICDFileProviderItemServiceProxy refreshSharingState:]_block_invoke"
+ "<%@ d:%@ i:%@>"
+ "@\"<NSFileProviderItem>\"32@0:8@\"NSURL\"16^@24"
+ "@\"NSArray\"16@0:8"
+ "@\"NSProgress\"32@0:8@\"NSString\"16@?<v@?@\"<NSFileProviderItem>\"@\"NSError\">24"
+ "@\"NSProgress\"32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "@\"NSProgress\"32@0:8Q16@?<v@?@\"NSError\">24"
+ "@\"NSProgress\"40@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSFileProviderItemVersion\"24@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">32"
+ "@\"NSProgress\"56@0:8@\"NSArray\"16{CGSize=dd}24@?<v@?@\"NSString\"@\"NSData\"@\"NSString\"@\"NSError\">40@?<v@?@\"NSError\">48"
+ "@32@0:8@16^@24"
+ "@32@0:8Q16@?24"
+ "ICDFileProviderClientSideCollaborationProtocol"
+ "ICDFileProviderClientSideCollaborationServiceProxy"
+ "ICDFileProviderClientSideCollaborationServiceSource"
+ "NSFileProviderExtension_Private"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N,GisRestricted"
+ "[DEBUG] FPFS is not enabled%@"
+ "[DEBUG] Failed creating proxy with %@%@"
+ "[DEBUG] fetchLatestRevisionIntoURL for item with identifier %@%@"
+ "[DEBUG] fetchLatestRevisionWithReply for item with identifier %@%@"
+ "[DEBUG] generating thumbnail for small file %@ using download%@"
+ "[DEBUG] waitForStabilizationWithCompletionHandler called while not in sync bubble. Nothing to do%@"
+ "[ERROR] %@ - Failed calculating signature for contents at '%@'. Error: %@%@"
+ "[INFO] %s: reply(%@, %@, %@, %d, %@)%@"
+ "[INFO] ┏%llx %s calculating collaboration version for %@%@"
+ "[WARNING] Initialized with a Ciconia domain %@. This is not supported%@"
+ "_additionalDumpInfoWithCompletionHandler:"
+ "_dumpInternalStateToTermDumper:completionHandler:"
+ "_getAsyncProxyWithErrorHandler:"
+ "_isCiconiaDomain"
+ "_propertiesForItemAtURL:error:"
+ "_removeTrashedItemsOlderThanDate:completionHandler:"
+ "attemptRecoveryFromError:optionIndex:completionHandler:"
+ "backupDatabaseWithURLWrapper:reply:"
+ "br_isInSyncBubble"
+ "br_prettyDescription"
+ "brc_errorMethodNotImplemented:"
+ "calculateCollaborationVersionForContents:reply:"
+ "calculateSignatureForURL:error:"
+ "changeItem:baseVersion:changedFields:contents:options:completionHandler:"
+ "clientSideCollaboration"
+ "cloneLatestContentRevisionForItemIdentifier:reply:"
+ "customPushTopics"
+ "disconnectWithOptions:completionHandler:"
+ "dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:"
+ "evictItemWithIdentifier:completionHandler:"
+ "fetchLatestRevisionIntoURL:reply:"
+ "fetchLatestRevisionWithReply:"
+ "fetchPublishingURLForItemIdentifier:completionHandler:"
+ "fetchTrashIdentifiersWithCompletionHandler:"
+ "generateSmallItemThumbnailForFileObject:reply:"
+ "getSaltingVerificationKeys:"
+ "getSaltingVerificationKeysAtItemIdentifier:reply:"
+ "handleEventsForBackgroundURLSession:completionHandler:"
+ "iCloudDrive"
+ "initWithCollaborationSignature:"
+ "lastPathComponent"
+ "moveItemAtURL:toURL:error:"
+ "movingItemAtURL:requiresProvidingWithDestinationURL:completionHandler:"
+ "preflightReparentItemWithIdentifier:toParentItemWithIdentifier:completionHandler:"
+ "preflightTrashItemWithIdentifier:completionHandler:"
+ "refreshSharingState:"
+ "reparentItemWithIdentifier:toParentItemWithIdentifier:completionHandler:"
+ "setAdvancedDataProtectionEnabled:forContainer:reply:"
+ "startProvidingItemAtURL:readingOptions:completionHandler:"
+ "uploadContents:baseVersion:reply:"
+ "v24@0:8@?<v@?@\"ICDCollaborationVersion\"@\"NSFileProviderItemVersion\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"I@\"NSError\">16"
+ "v24@?0@\"NSArray\"8@?<v@?@\"BRFileObjectID\"@\"NSURL\"@\"NSData\"@\"NSError\">16"
+ "v32@0:8@\"BRFileObjectID\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"FPCTLTermDumper\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"NSDate\"16@?<v@?>24"
+ "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?@\"ICDCollaborationVersion\"@\"NSError\">24"
+ "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?@\"NSURL\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"<NSFileProviderItem>\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"I@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v32@?0@\"NSData\"8@\"NSFileProviderItemVersion\"16@\"NSError\"24"
+ "v32@?0@\"NSURL\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0@\"NSURL\"8@\"NSFileProviderItemVersion\"16@\"NSError\"24"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@\"NSError\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"<NSFileProviderItem>\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16Q24@?<v@?@\"NSError\">32"
+ "v40@?0@\"BRFileObjectID\"8@\"NSURL\"16@\"NSData\"24@\"NSError\"32"
+ "v56@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40B44@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32B40B44@?48"
+ "v64@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"NSURL\"40Q48@?<v@?@\"<NSFileProviderItem>\"QB@\"NSError\">56"
+ "v64@0:8@16@24Q32@40Q48@?56"
+ "waitForStabilizationWithCompletionHandler:"
+ "waitForStabilizationWithReply:"
- "\x01\x12"
- "\x05"
- "\x05E"
- "\x11"
- "+[ICDCiconia failExtensionInitWithError:workDir:]"
- "-[ICDCiconia _notifyLastContact]"
- "-[ICDCiconia createItemBasedOnTemplate:fields:contents:options:request:completionHandler:]"
- "-[ICDCiconia createItemBasedOnTemplate:fields:contents:options:request:completionHandler:]_block_invoke"
- "-[ICDCiconia enumerateItemsInFolder:sortOrder:offset:limit:completion:]"
- "-[ICDCiconia enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke_2"
- "-[ICDCiconia enumerateTrashItemsFromRank:limit:completion:]"
- "-[ICDCiconia fetchContentsForItemWithIdentifier:version:request:completionHandler:]"
- "-[ICDCiconia getQueryItemForFileObjectID:]"
- "-[ICDCiconia getQueryItemForFileObjectID:]_block_invoke"
- "-[ICDCiconia initWithDomain:]"
- "-[ICDCiconia initWithDomain:]_block_invoke"
- "-[ICDCiconia invalidate]"
- "-[ICDCiconia notifyImportFinished]"
- "-[ICDCiconiaServiceSource listener:shouldAcceptNewConnection:]_block_invoke"
- "-[ICDFileEnumerator initWithFileObjectID:itemIdentifier:recursive:ciconiaDomain:]_block_invoke"
- "-[ICDFileEnumerator invalidate]"
- "-[ICDFileProviderExtension dealloc]"
- ".importFinished"
- ".initError"
- ".lastContact"
- "@\"BRCAccountSessionFPFS\""
- "@\"ICDCiconia\""
- "@40@0:8@\"NSString\"16@\"NSFileProviderDomain\"24@\"<NSFileProviderServicing>\"32"
- "@44@0:8@16@24B32@36"
- "B16@?0@\"PQLConnection\"8"
- "Cannot open and validate DB"
- "CiconiaService"
- "ICDCiconia"
- "ICDCiconiaService"
- "ICDCiconiaServiceSource"
- "ICDCiconiaStubWorkingSet"
- "NSFileProviderServiceSource_Private"
- "SELECT COUNT(1) FROM client_state"
- "T@\"NSString\",R,VdomainID"
- "T@\"NSURL\",R,VworkDir"
- "TB,R,N,GisRestricted"
- "[CRIT] Assertion failed: _ciconiaDomain == nil%@"
- "[CRIT] Assertion failed: url == nil%@"
- "[CRIT] UNREACHABLE: Failed to parse bookmark data on %@%@"
- "[DEBUG] Closing session for %@%@"
- "[DEBUG] Denying speculative download on Ciconia%@"
- "[DEBUG] Domain %@ removed%@"
- "[DEBUG] FPFS is not enabled - only Ciconia will be accepted%@"
- "[DEBUG] Item is in: %@ (%@) - %@%@"
- "[DEBUG] Notification file created at: %@%@"
- "[DEBUG] Parent Item of trashed item is %@%@"
- "[DEBUG] Query ID for the object: %@ (%llu)%@"
- "[DEBUG] Returning failure for bookmark - expected call%@"
- "[DEBUG] Starting new session for %@%@"
- "[DEBUG] Tearing down extension%@"
- "[DEBUG] We're asked to enumerate %@ (%llu)%@"
- "[DEBUG] downloading file %@ because quicklook can generate its thumbnail%@"
- "[DEBUG] enumerating children of %@%@"
- "[DEBUG] localItem: %@%@"
- "[DEBUG] session is: %@%@"
- "[DEBUG] signalErrorResolved: %@%@"
- "[DEBUG] ┏%llx creating item based on template %@ at '%@' fields:%llu options:%llu xattr:%@%@"
- "[ERROR] Couldn't load account.1 at: %@%@"
- "[ERROR] Unexpected call to createItemBasedOnTemplate%@"
- "[ERROR] Unexpected call to deleteItemWithIdentifier%@"
- "[ERROR] Unexpected call to enumerateItemsInFolder%@"
- "[ERROR] Unexpected call to enumerateTrashItemsFromRank%@"
- "[ERROR] Unexpected call to fetchContentsForItemWithIdentifier%@"
- "[ERROR] Unexpected call to modifyItem%@"
- "[ERROR] can't start downloading %@: %@%@"
- "[ERROR] could not finish DB setup: %@%@"
- "[ERROR] could not open and validate db at path %@/client.db: %@%@"
- "[NOTICE] Dangling domain %@ found - removing%@"
- "[WARNING] Failed persisting error %@ to %@: %@%@"
- "[WARNING] Last contact file creation at %@ failed%@"
- "[WARNING] Notification file creation at %@ failed%@"
- "[WARNING] deallocation with Ciconia live... That's not a good idea%@"
- "_ciconiaDomain"
- "_extension"
- "_handleTrashedItemsMigration"
- "_loadClientZonesFromDisk"
- "_markDBOpened"
- "_notifyLastContact"
- "_queueOrCallCompletionBlock:"
- "_session"
- "_tearingDown"
- "appLibrary"
- "appLibraryByID:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "asDirectory"
- "backupDatabaseWithURLWrapper:forCiconia:reply:"
- "br_isDirectoryType"
- "br_makeNextFlushCheckpoint"
- "brc_accountIDPathForAccountPath:"
- "brc_ciconiaWorkDirForCurrentPersona"
- "brc_dbAccountDSIDForPath:"
- "brc_errorCiconiaAborted:"
- "brc_errorExcludedFromSyncUnderRoot"
- "brc_errorNotOnDisk:"
- "client.db"
- "clientDB"
- "clientTruthWorkloop"
- "clientZoneByMangledID:"
- "client_state is empty in the extension"
- "closeOfflineSession"
- "cloudDocsClientZone"
- "containerItemForContainer:withRepresentativeItem:"
- "containerMetadata"
- "contentType"
- "createFileAtPath:contents:attributes:"
- "creationDate"
- "currentConnection"
- "db"
- "domainID"
- "dumpDatabaseTo:containerID:personaID:includeAllItems:reply:"
- "enumerateChildrenOfItemGlobalID:sortOrder:offset:limit:db:"
- "enumerateContainersWithDB:handler:"
- "extendedAttributes"
- "extractBookmarkDataFromTemplateItem:isTrashBookmark:"
- "failExtensionInitWithError:workDir:"
- "fetchRootItemInDB:"
- "fetchZoneRootItemInDB:"
- "fileSystemRepresentation"
- "forceBatchStart"
- "fp_prettyDescription"
- "fp_prettyPath"
- "fsImporter"
- "getOrCreateAppLibraryAndPrivateZonesIfNecessary:"
- "getOrCreateSharedZones:"
- "getQueryItemForFileObjectID:"
- "importAppLibraryRootFromTemplateItem:"
- "importNewItemAtURL:logicalName:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:"
- "initForTestingDevice:"
- "initRootContainerNotificationWithOptimizeStorage:isDataSeparated:"
- "initWithBookmarkData:isTrashBookmark:session:"
- "initWithCiconiaDomain:"
- "initWithFileObjectID:itemIdentifier:recursive:ciconiaDomain:"
- "initWithItemIdentifier:domain:extension:"
- "initWithLocalItem:itemDiffs:"
- "initializeOfflineDatabaseWhileUpgrading:error:"
- "isCloudDocsRoot"
- "isDataSeparated"
- "isDirectory"
- "isFSRoot"
- "isFinderBookmark"
- "isGreedy"
- "isRootContainerItem"
- "isShared"
- "itemByFileObjectID:"
- "itemByFileObjectID:db:"
- "itemByItemID:"
- "itemGlobalID"
- "itemID"
- "longValue"
- "mangledID"
- "notificationFromItem:"
- "notifsRank"
- "notifyImportFinished"
- "now"
- "numberWithSQL:"
- "openDBForNewDomain:deviceIDChanged:withError:"
- "parentItemIdentifier"
- "performWithFlags:action:whenFlushed:"
- "queryLastCiconiaVersion:"
- "rawID"
- "readOnlyDB"
- "readOnlyWorkloop"
- "removeDomain:completionHandler:"
- "reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:"
- "reportDummyCiconiaMigration:reply:"
- "reportFinishedMigration:uuid:reply:"
- "reportItemMismatchDuringSilentMigration:information:uuid:reply:"
- "requestDownloadForItemWithIdentifier:requestedRange:completionHandler:"
- "requiredEntitlement"
- "resumeIfNecessary"
- "scheduleSendBarrierBlock:"
- "server.db"
- "sessionForDumpingDatabasesAtURL:with:"
- "setStageDirectoryForXattr:"
- "signalErrorResolved:completionHandler:"
- "signalStartOfSilentTelemetry:uuid:manual:version:reply:"
- "stageRegistry"
- "tearDown:"
- "timeIntervalSince1970"
- "trashedItemsEnumeratorFromNotifRank:batchSize:db:"
- "v16@?0@\"PQLConnection\"8"
- "v24@?0@\"BRFileObjectID\"8@\"NSError\"16"
- "v24@?0@\"BRQueryItem\"8@\"BRCDirectoryItem\"16"
- "v24@?0@\"NSArray\"8@?<v@?@\"BRFileObjectID\"@\"NSError\">16"
- "v32@0:8@\"BRCMigrationReport\"16@?<v@?@\"NSError\">24"
- "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
- "v36@?0@\"<NSFileProviderItem>\"8Q16B24@\"NSError\"28"
- "v40@0:8@\"BRCMigrationReport\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSError\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v52@0:8@\"NSDate\"16@\"NSUUID\"24B32Q36@?<v@?@\"NSError\">44"
- "v52@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40@?<v@?B@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16@24B32Q36@?44"
- "v56@0:8@\"NSError\"16@\"NSString\"24@\"NSUUID\"32Q40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32Q40@?48"
- "validateMangledIDString:strict:"
- "workDir"
- "writeToURL:atomically:"
- "x"

```
