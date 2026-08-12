## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-2215.0.16.0.0
-  __TEXT.__text: 0x262998
-  __TEXT.__objc_methlist: 0x12c54
-  __TEXT.__const: 0x15aa
-  __TEXT.__cstring: 0x3f116
-  __TEXT.__oslogstring: 0x5e7cd
-  __TEXT.__gcc_except_tab: 0xda74
+2215.0.20.0.0
+  __TEXT.__text: 0x26456c
+  __TEXT.__objc_methlist: 0x12d9c
+  __TEXT.__const: 0x159a
+  __TEXT.__cstring: 0x3f6f6
+  __TEXT.__oslogstring: 0x5efed
+  __TEXT.__gcc_except_tab: 0xd83c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x4828
+  __TEXT.__unwind_info: 0x4888
   __TEXT.__eh_frame: 0x10c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x31c8
-  __DATA_CONST.__objc_classlist: 0x488
+  __DATA_CONST.__const: 0x3230
+  __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf08
+  __DATA_CONST.__objc_selrefs: 0xaff0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0xef8
-  __DATA_CONST.__got: 0x1280
-  __AUTH_CONST.__const: 0x1060
-  __AUTH_CONST.__cfstring: 0x32860
-  __AUTH_CONST.__objc_const: 0x18f30
-  __AUTH_CONST.__objc_arrayobj: 0x348
+  __DATA_CONST.__objc_superrefs: 0x360
+  __DATA_CONST.__objc_arraydata: 0xf00
+  __DATA_CONST.__got: 0x12a0
+  __AUTH_CONST.__const: 0x1080
+  __AUTH_CONST.__cfstring: 0x32d00
+  __AUTH_CONST.__objc_const: 0x191a8
+  __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x1228
-  __AUTH.__objc_data: 0x878
+  __AUTH_CONST.__auth_got: 0x1238
+  __AUTH.__objc_data: 0x918
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x1818
-  __DATA.__data: 0x1118
+  __DATA.__objc_ivar: 0x1830
+  __DATA.__data: 0x1180
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x560
   __DATA_DIRTY.__objc_data: 0x2530

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7280
-  Symbols:   16440
-  CStrings:  10960
+  Functions: 7316
+  Symbols:   16525
+  CStrings:  11025
 
Symbols:
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:forAssetID:withFailureReason:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:ofAssetDescriptor:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:ofAssetDescriptor:forAssetID:ofAssetDirectory:withFailureReason:withFailureError:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:ofAssetDescriptor:withFailureError:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:ofAssetDescriptor:withFailureReason:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:ofAssetDirectory:withFailureReason:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:withFailureError:]
+ +[MADAutoAssetTelemetryReport telemetryReportPreinstalled:withFailureReason:]
+ -[ControlManager _bulkSAFOperations:doRegister:]
+ -[ControlManager bulkSAFRegister:]
+ -[ControlManager bulkSAFUnregister:]
+ -[ControlManager updateSAFArray:withPath:bundleID:]
+ -[MAAutoAssetMigrationManager .cxx_destruct]
+ -[MAAutoAssetMigrationManager assetMigrationResults]
+ -[MAAutoAssetMigrationManager convertMigrationCookieToMigrationResults:]
+ -[MAAutoAssetMigrationManager createMigrationInfoWithCookieFileKey:andValue:error:]
+ -[MAAutoAssetMigrationManager delegate]
+ -[MAAutoAssetMigrationManager initWithDelegate:]
+ -[MAAutoAssetMigrationManager initWithDelegate:migrationCookiePath:]
+ -[MAAutoAssetMigrationManager init]
+ -[MAAutoAssetMigrationManager migrationCookiePath]
+ -[MAAutoAssetMigrationManager parseMigrationCookie:]
+ -[MAAutoAssetMigrationManager parseMigrationCookieWithPath:andError:]
+ -[MAAutoAssetMigrationManager persistAssetMigrationResults:andError:]
+ -[MAAutoAssetMigrationManager persistedStateQueue]
+ -[MAAutoAssetMigrationManager persistedState]
+ -[MAAutoAssetMigrationManager preInstalledRelocateAutoAssets]
+ -[MAAutoAssetMigrationManager setAssetMigrationResults:]
+ -[MAAutoAssetMigrationManager writeLegacyCookieFileForMigrationResults:error:]
+ -[MADAutoAssetControlManager _clientRequestRequiresSetInstance:]
+ -[MADAutoAssetControlManager _removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:withSAFArray:]
+ -[MADAutoAssetControlManager autoAssetMigrated:]
+ -[MADAutoAssetControlManager handleClientMigrationResultsRequest:forAutoJob:]
+ -[MADAutoAssetControlManager locateCancelingSetJobForClientDomain:byIdentifier:fromLocation:]
+ -[MADAutoAssetControlManager migrationResults]
+ -[MADAutoAssetControlManager setMigrationResults:]
+ -[MADAutoAssetStager _removeStagedAssetFromFilesystem:forHistoryOperation:withSAFArray:]
+ GCC_except_table320
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table345
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table356
+ GCC_except_table359
+ GCC_except_table363
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table433
+ GCC_except_table443
+ GCC_except_table444
+ GCC_except_table523
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table623
+ GCC_except_table629
+ GCC_except_table644
+ GCC_except_table673
+ GCC_except_table799
+ GCC_except_table800
+ GCC_except_table801
+ GCC_except_table802
+ _OBJC_CLASS_$_MAAutoAssetMigrationInfo
+ _OBJC_CLASS_$_MAAutoAssetMigrationManager
+ _OBJC_CLASS_$_MAAutoAssetMigrationResults
+ _OBJC_CLASS_$_MADAutoAssetTelemetryReport
+ _OBJC_IVAR_$_MAAutoAssetMigrationManager._assetMigrationResults
+ _OBJC_IVAR_$_MAAutoAssetMigrationManager._delegate
+ _OBJC_IVAR_$_MAAutoAssetMigrationManager._migrationCookiePath
+ _OBJC_IVAR_$_MAAutoAssetMigrationManager._persistedState
+ _OBJC_IVAR_$_MAAutoAssetMigrationManager._persistedStateQueue
+ _OBJC_IVAR_$_MADAutoAssetControlManager._migrationResults
+ _OBJC_METACLASS_$_MAAutoAssetMigrationManager
+ _OBJC_METACLASS_$_MADAutoAssetTelemetryReport
+ __OBJC_$_CLASS_METHODS_MADAutoAssetTelemetryReport
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetMigrationManager
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetMigrationManager
+ __OBJC_$_PROP_LIST_MAAutoAssetMigrationManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MADAutoAssetMigrationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MADAutoAssetMigrationDelegate
+ __OBJC_$_PROTOCOL_REFS_MADAutoAssetMigrationDelegate
+ __OBJC_CLASS_RO_$_MAAutoAssetMigrationManager
+ __OBJC_CLASS_RO_$_MADAutoAssetTelemetryReport
+ __OBJC_LABEL_PROTOCOL_$_MADAutoAssetMigrationDelegate
+ __OBJC_METACLASS_RO_$_MAAutoAssetMigrationManager
+ __OBJC_METACLASS_RO_$_MADAutoAssetTelemetryReport
+ __OBJC_PROTOCOL_$_MADAutoAssetMigrationDelegate
+ ___48-[ControlManager _bulkSAFOperations:doRegister:]_block_invoke
+ ___68-[MAAutoAssetMigrationManager initWithDelegate:migrationCookiePath:]_block_invoke
+ ___68-[MAAutoAssetMigrationManager initWithDelegate:migrationCookiePath:]_block_invoke_2
+ ___69-[MAAutoAssetMigrationManager parseMigrationCookieWithPath:andError:]_block_invoke
+ ___69-[MAAutoAssetMigrationManager persistAssetMigrationResults:andError:]_block_invoke
+ ___77-[MADAutoAssetControlManager handleClientMigrationResultsRequest:forAutoJob:]_block_invoke
+ ___78-[MADAutoAssetJob autoAssetJobFinished:forJobFinishedReason:failingWithError:]_block_invoke
+ ___78-[MADAutoAssetJob autoAssetJobFinished:forJobFinishedReason:failingWithError:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ __isSeedBuild
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _kMobileAssetPreferencesInternalVariantAsSeed
+ _kSubscriptionQueueKey
+ _objc_msgSend$_bulkSAFOperations:doRegister:
+ _objc_msgSend$_clientRequestRequiresSetInstance:
+ _objc_msgSend$_removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:withSAFArray:
+ _objc_msgSend$_removeStagedAssetFromFilesystem:forHistoryOperation:withSAFArray:
+ _objc_msgSend$addFailedMigratedInfo:
+ _objc_msgSend$addFailedMigratedInfoForDescriptor:withError:
+ _objc_msgSend$addSetupError:
+ _objc_msgSend$addSuccessfullyMigratedInfo:
+ _objc_msgSend$addSuccessfullyMigratedInfoForDescriptor:
+ _objc_msgSend$assetMigrationResults
+ _objc_msgSend$autoAssetMigrated:
+ _objc_msgSend$bulkSAFUnregister:
+ _objc_msgSend$convertMigrationCookieToMigrationResults:
+ _objc_msgSend$createMigrationInfoWithCookieFileKey:andValue:error:
+ _objc_msgSend$failedMigratedAssetInfo
+ _objc_msgSend$handleClientMigrationResultsRequest:forAutoJob:
+ _objc_msgSend$initWithDelegate:migrationCookiePath:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$locateCancelingSetJobForClientDomain:byIdentifier:fromLocation:
+ _objc_msgSend$migrationCookiePath
+ _objc_msgSend$migrationResults
+ _objc_msgSend$migrationSucceeded
+ _objc_msgSend$parseMigrationCookie:
+ _objc_msgSend$parseMigrationCookieWithPath:andError:
+ _objc_msgSend$persistAssetMigrationResults:andError:
+ _objc_msgSend$preInstalledRelocateAutoAssets
+ _objc_msgSend$setAssetMigrationResults:
+ _objc_msgSend$setMigrationError:
+ _objc_msgSend$setMigrationResults:
+ _objc_msgSend$setMigrationSucceeded:
+ _objc_msgSend$successfullyMigratedAssetInfo
+ _objc_msgSend$updateSAFArray:withPath:bundleID:
+ _objc_msgSend$writeLegacyCookieFileForMigrationResults:error:
- -[MADAutoAssetControlManager _preInstalledRelocateAutoAssets]
- -[MADAutoAssetControlManager _removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:]
- -[MADAutoAssetControlManager locateCancelingSetJobForClientDomain:byIdentifier:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:forAssetID:withFailureReason:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:ofAssetDescriptor:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:ofAssetDescriptor:forAssetID:ofAssetDirectory:withFailureReason:withFailureError:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:ofAssetDescriptor:withFailureError:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:ofAssetDescriptor:withFailureReason:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:ofAssetDirectory:withFailureReason:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:withFailureError:]
- -[MADAutoAssetControlManager telemetryReportPreinstalled:withFailureReason:]
- -[MADAutoAssetStager _extendLookupByAssetTypeWithDownloadedDescriptors:limitingToSetTargets:]
- -[MADAutoAssetStager _removeStagedAssetFromFilesystem:forHistoryOperation:]
- GCC_except_table321
- GCC_except_table322
- GCC_except_table335
- GCC_except_table336
- GCC_except_table343
- GCC_except_table347
- GCC_except_table348
- GCC_except_table353
- GCC_except_table354
- GCC_except_table357
- GCC_except_table360
- GCC_except_table361
- GCC_except_table365
- GCC_except_table371
- GCC_except_table398
- GCC_except_table401
- GCC_except_table431
- GCC_except_table437
- GCC_except_table438
- GCC_except_table519
- GCC_except_table578
- GCC_except_table579
- GCC_except_table619
- GCC_except_table627
- GCC_except_table642
- GCC_except_table671
- GCC_except_table806
- GCC_except_table807
- GCC_except_table808
- GCC_except_table811
- _objc_msgSend$_blendOptionalCandidates:intoRequired:
- _objc_msgSend$_extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:createdClientDefinedSetEntries:createdNoClientSetEntries:appendedSetEntries:
- _objc_msgSend$_extendLookupByAssetTypeWithDownloadedDescriptors:limitingToSetTargets:
- _objc_msgSend$_maintainLatestCandidate:candidateDescriptor:
- _objc_msgSend$_preInstalledRelocateAutoAssets
- _objc_msgSend$_removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:
- _objc_msgSend$_removeStagedAssetFromFilesystem:forHistoryOperation:
- _objc_msgSend$_trimConsideringToLatestDownloaded:
- _objc_msgSend$arrayByAddingObject:
- _objc_msgSend$emptySetTargetForAssetType:
- _objc_msgSend$includesEntryForAssetType:
- _objc_msgSend$locateCancelingSetJobForClientDomain:byIdentifier:
- _objc_msgSend$logAlreadyDownloadedByAssetType:
CStrings:
+ "%@:_routeClientRequest"
+ "%@:locateCancelingSetJobForClientDomain"
+ "%{public}@ {%{public}@:autoAssetJobFinished} | SIMULATE_OPERATION(%lld) | call to _autoAssetJobFinished postponed"
+ "%{public}@ {%{public}@:autoAssetJobFinished} | SIMULATE_OPERATION(%{public}@) | added postponedJobFinishedTimer to run-loop"
+ "%{public}@ {%{public}@:autoAssetJobFinished} | SIMULATE_OPERATION(%{public}@) | call to _autoAssetJobFinished postponed"
+ "%{public}@ {%{public}@:autoAssetJobFinished} | SIMULATE_OPERATION(%{public}@) | postponedJobFinishedTimer fired"
+ "%{public}@ {%{public}@:autoAssetJobFinished} | SIMULATE_OPERATION(%{public}@) | unable to create postponedJobFinishedTimer"
+ "(%@)unknown auto-asset command request received (%@)"
+ "165413ff-a1b0-4e64-b0a0-25ca4fa99e4a"
+ "3.1.3"
+ "Auto-MigrationInfo"
+ "AutoControl-SetJobByIdentifier"
+ "AutoControl-SetJobCancel"
+ "Customer ADOS"
+ "DownloadAttemptTimestamp"
+ "EntryIdMigrationResults"
+ "Failed to allocate migrationDict"
+ "Failed to create MAAutoAssetMigrationInfo instance for migration cookie entry { %@ : %@ } - Error: %@"
+ "Failed to create migration results instance"
+ "Failed to create persisted state entry"
+ "Found preference kMobileAssetPreferencesInternalVariantAsSeed, overriding to seed build: %@"
+ "Initialized with assetMigrationResults:\n>>>\n%{public}@\n<<<"
+ "Internal Seed Build"
+ "Internal Seed Build (EPR Release Aligned Type)"
+ "Internal Seed Build (Release Aligned Type)"
+ "Internal Seed Build External Pre-Release"
+ "Internal Seed Build External Pre-Release ADOS"
+ "Loaded built-in MobileAssetDaemon_Framework Aug  4 2026 11:27:22"
+ "MA-AUTO-SET(REPLY):MIGRATION_RESULTS"
+ "MA-AUTO-SET:MIGRATION_RESULTS"
+ "MADAutoControl:handleClientMigrationResultsRequest"
+ "Migration cookie not found"
+ "MigrationInfoPersistedStateQueue"
+ "MigrationModule"
+ "No migration results found"
+ "Non-string key found in migration dict"
+ "Non-string value found for for key (%@) in migration dict"
+ "Saving migration info array"
+ "TIMEOUT-30"
+ "Unsubscribing from channel: %{public}@"
+ "[%{public}@] {%{public}@}\n[BY-SET-IDENTIFIER] removed from currentSetJobsByIdentifier | clientDomainName:%{public}@ | setJobIdentifier:%{public}@ | autoSetJob:%{public}@"
+ "[%{public}@] {%{public}@} | removalFlow:%{public}@"
+ "[%{public}@] {handleClientCurrentStatusRequest} migration results | results:%{public}@"
+ "[AUTO-MIGRATION-MANAGER] {convertMigrationCookieToMigrationResults} ...Failed to create assetMigrationResults instance"
+ "[AUTO-MIGRATION-MANAGER] {convertMigrationCookieToMigrationResults} ...Failed to persist assetMigrationResults object: %{public}@"
+ "[AUTO-MIGRATION-MANAGER] {convertMigrationCookieToMigrationResults} ...Legacy migration cookie has already been converted to a MigrationResults instance. Skipping converting"
+ "[AUTO-MIGRATION-MANAGER] {convertMigrationCookieToMigrationResults} ...Parsing legacy migration cookie failed"
+ "[AUTO-MIGRATION-MANAGER] {parseMigrationCookie} ...Failed to create MAAutoAssetMigrationInfo instance for migration cookie entry { %{public}@ : %{public}@ } - Error: %{public}@"
+ "[AUTO-MIGRATION-MANAGER] {parseMigrationCookie} ...initializing dictionary with migration file failed for file at path %{public}@"
+ "[AUTO-MIGRATION-MANAGER] {parseMigrationCookie} ...migration cookie not found at path %{public}@"
+ "[AUTO-MIGRATION-MANAGER] {parseMigrationCookie} ...migration file key is invalid type"
+ "[AUTO-MIGRATION-MANAGER] {parseMigrationCookie} ...migration file value is invalid type"
+ "[AUTO-MIGRATION-MANAGER] {parseMigrationFileKey:andValue:} ...unexpected migration cookie key format"
+ "[AUTO-MIGRATION-MANAGER] {persistAssetMigrationResults} ...Failed to create persisted state entry"
+ "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} Creating MAAutoAssetMigrationResults from cookie file"
+ "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} Failed to migrate off of legacy migration cookie file: %@"
+ "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} Failed to migrate pre-installed auto-assets"
+ "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} Migration cookie found. Already migrated assets, no need to run again"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} Failed to write legacy cookie file: %@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} added descriptor for pre-installed asset | path:%{public}@ | descriptor:%{public}@ "
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} attempted to move auto-asset but failed | descriptor:%{public}@ | fromPath:%{public}@ | toPath:%{public}@ | error:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} descriptor created for auto-asset metadata does not describe an auto-asset | path:%{public}@ | assetType:%{public}@ | descriptor:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} failed to decrypt contentEncrypted asset | path:%{public}@ | assetType:%{public}@ | descriptor:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} failed to delete pre-installed asset directory %{public}@ Error: %{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} failed to persist asset migration results: %@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} failed to read directories at path to pre-installed assets | path:%{public}@ | error:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} failed to set protection class D on migrated asset | descriptor:%{public}@ | toPath:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} no directories found at path to pre-installed assets | path:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} no pre-installed assets for asset-type | path:%{public}@ | assetType:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} not migrating since not an auto-asset | path:%{public}@ | assetType:%{public}@ | assetID:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} skipping malformed asset directory | assetDir:%{public}@ "
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} successfully migrated %ld | failed to migrated %ld | path: %{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} unable to create descriptor | path:%{public}@ | assetType:%{public}@"
+ "[AUTO-PRE-INSTALLED] {preInstalledRelocateAutoAssets} unable to create descriptor | path:%{public}@ | assetType:%{public}@ | reasons:%{public}@"
+ "[AUTO-PRE-INSTALLED] {writeLegacyCookieFileForMigrationResults} Failed to write legacy cookie file to disk"
+ "[BY-SET-IDENTIFIER] {%{public}@} removed set-job from jobs-by-identifier | setJobKey:%{public}@"
+ "[BY-SET-IDENTIFIER] {initialStatusForSetJob} added to set-jobs-by-identifier | setJobKey:%{public}@ | autoJob:%{public}@"
+ "_bulkSAFOperations: Did not find any asset paths to bulk %{public}@ with space attribution."
+ "_bulkSAFOperations: Failed to bulk %{public}@ assets with space attribution. Error: %{public}@"
+ "_bulkSAFOperations: Successfully bulk %{public}@ %lu assets with space attribution."
+ "_bulkSAFOperations: Will be bulk %{public}@ %lu assets with space attribution."
+ "attempted to move auto-asset but failed | descriptor:%@ | fromPath:%@ | toPath:%@ | error:%@"
+ "autoAssetMigrated"
+ "convertMigrationCookieToMigrationResults"
+ "createMigrationInfoWithCookieFileKey"
+ "descriptor created for auto-asset metadata does not describe an auto-asset | path:%@ | assetType:%@ | descriptor:%@"
+ "failed to decrypt contentEncrypted asset | path:%@ | assetType:%@ | descriptor:%@"
+ "failed to read directories at path to pre-installed assets"
+ "failed to set protection class D on migrated asset | descriptor:%@ | toPath:%@"
+ "handleClientMigrationResultsRequest"
+ "initWithDelegate"
+ "malformed asset directory: %@"
+ "migrationResults"
+ "no pre-installed assets for asset-type | path:%@ | assetType:%@"
+ "not migrating since not an auto-asset | path:%@ | assetType:%@ | assetID:%@"
+ "parseMigrationCookieWithPath"
+ "persistAssetMigrationResults"
+ "persistedMigrationResults"
+ "preInstalledRelocateAutoAssets"
+ "registering"
+ "unable to create descriptor | path:%@ | assetType:%@ | reasons:%@"
+ "unexpected migration cookie key format"
+ "unregistering"
+ "v32@?0@8@16^B24"
+ "{%@} missing required | clientDomainName:%@ | assetSetIdentifier:%@"
+ "{%{public}@}\n[BY_SET_IDENTIFIER] | still tracked in set-jobs-by-identifier (even though at 0 client-requests) | activeSetJob:%{public}@"
+ "{%{public}@} actively canceling set-job | setJobKey:%{public}@"
+ "{%{public}@} canceling set-job | setJobKey:%{public}@"
+ "{%{public}@} removed from canceling set-jobs | setJobKey:%{public}@"
+ "{ControlManager:updateSAFArray} Failed to create SAPathInfo object for path %{public}@.  Path is not added to provided array"
+ "{ControlManager:updateSAFArray} One of the arguments is empty.  Path is not added to provided array"
+ "{handleClientMigrationResultsRequest} Daemon failed to find migration results"
+ "{respondToCacheDelete} Initializing SAF arrays for register/unregister of assets after determine for volume %{public}@ at urgency %d ..."
+ "{respondToCacheDelete} Initializing SAF arrays for unregister of assets for reclaimSpace from volume %{public}@ at urgency %d ..."
+ "{respondToCacheDelete} performing cache-delete triggered operation for volume %{public}@ at urgency %d ..."
- "%@:_routeClientReuest"
- "%{public}@\n[%{public}@] {FormCandidatesDecideDetermine} [IGNORED(by-set-target)] candidateDescriptor:%{public}@ mode::%{public}@"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided %ld downloaded descriptor%{public}@ - potential candidate%{public}@ for staging"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided no downloaded descriptors - no candidate(s) for staging"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} candidate descriptors\n>>> Required:%{public}@\n>>> Optional:%{public}@\n>>> Ignored:%{public}@\n>>> AllMode:%{public}@"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} client-defined set-target for asset-type - not staging based on already-downloaded | candidateDescriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} nil encountered on consideringDescriptors array"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} no candidate descriptors for staging"
- "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} should have candidates yet unable to form set-lookup array"
- "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} nil asset-type for asset-descriptor | autoAssetDescriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} nil encountered on alreadyDownloadedDescriptors array"
- "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} | final candidate summary\n>>> created[Client:%{public}@][No:%{public}@]]\n>>> appended:%{public}@\n>>> addedRequired:%{public}@\n>>> addedOptional:%{public}@\n>>> setTargetRemoves:%{public}@\n>>> noSetConfiguration:%{public}@\n>>> ignored(bySetTarget:%{public}@,NoSupport:%{public}@,EmptySetTarget:%{public}@)"
- "%{public}@ {autoAssetJobFinished} | SIMULATE_OPERATION(%lld) | call to _autoAssetJobFinished postponed"
- "%{public}@ {autoAssetJobFinished} | SIMULATE_OPERATION(%{public}@) | call to _autoAssetJobFinished postponed"
- "3.1.2"
- "ADOS"
- "DESCRIPTOR"
- "Failed to write cookie file"
- "IGNORED"
- "Loaded built-in MobileAssetDaemon_Framework Jul 11 2026 05:39:25"
- "[%@] adding candidate (from downloaded that support staging)"
- "[%{public}@] {%{public}@}\n[ROUTING-TABLE-REMOVE] removed from currentSetJobsByIdentifier | clientDomainName:%{public}@ | setJobIdentifier:%{public}@ | autoSetJob:%{public}@"
- "[%{public}@] {removeCurrentSetJob} | removalFlow:%{public}@"
- "[AUTO-PRE-INSTALLED]"
- "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} ...Finishing pre-installed asset migration"
- "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} Already migrated assets, no need to run again"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} %ld pre-installed auto-asset%{public}@ successfully relocated | path:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} added descriptor for pre-installed asset | path:%{public}@ | descriptor:%{public}@ "
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} attempted to move auto-asset but failed | descriptor:%{public}@ | fromPath:%{public}@ | toPath:%{public}@ | error:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} descriptor created for auto-asset metadata does not describe an auto-asset | path:%{public}@ | assetType:%{public}@ | descriptor:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} failed to decrypt contentEncrypted asset | path:%{public}@ | assetType:%{public}@ | descriptor:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} failed to read directories at path to pre-installed assets | path:%{public}@ | error:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} failed to set protection class D on migrated asset | descriptor:%{public}@ | toPath:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} no directories found at path to pre-installed assets | path:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} no pre-installed assets for asset-type | path:%{public}@ | assetType:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} no pre-installed auto-assets were relocated | path:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} not migrating since not an auto-asset | path:%{public}@ | assetType:%{public}@ | assetID:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} skipping malformed asset directory | assetDir:%{public}@ "
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} unable to create descriptor | path:%{public}@ | assetType:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledRelocateAutoAssets} unable to create descriptor | path:%{public}@ | assetType:%{public}@ | reasons:%{public}@"
- "_preInstalledMigrateAssets"
- "_preInstalledRelocateAutoAssets"
- "dirs(MA_PATH_TO_INSTALL_WITH_OS)"
- "found candidate(s) for staging | totalCandidatesForStaging:%llu"
- "have downloaded auto-asset candidate(s) for staging"
- "unknown auto-asset command request received (%@)"
- "{FormCandidatesDecideDetermine} forming candidates yet not involving required or optional"
- "{locateCancelingSetJobForClientDomain} missing required | clientDomainName:%@ | assetSetIdentifier:%@"
- "{respondToCacheDelete} Initializing SAF arrays for register/unregister of assets after determine for volume %{public}@ at urgency %{public}d ..."
- "{respondToCacheDelete} performing cache-delete triggered operation for volume %{public}@ at urgency %{public}d ..."
```
