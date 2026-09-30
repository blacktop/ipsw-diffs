## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

```diff

-  __TEXT.__text: 0x102530
-  __TEXT.__objc_methlist: 0x107c8
+  __TEXT.__text: 0x100338
+  __TEXT.__objc_methlist: 0x10500
   __TEXT.__const: 0x214
-  __TEXT.__gcc_except_tab: 0x38d0
-  __TEXT.__cstring: 0x2339a
+  __TEXT.__gcc_except_tab: 0x38a0
+  __TEXT.__cstring: 0x2324a
   __TEXT.__oslogstring: 0x402
-  __TEXT.__ustring: 0x12ee
+  __TEXT.__ustring: 0x147c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x31e8
+  __TEXT.__unwind_info: 0x31d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc50
+  __DATA_CONST.__const: 0xc38
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8508
+  __DATA_CONST.__objc_selrefs: 0x8300
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x4b8
-  __DATA_CONST.__objc_arraydata: 0x6a0
-  __DATA_CONST.__got: 0xf50
-  __AUTH_CONST.__const: 0x1bf0
-  __AUTH_CONST.__cfstring: 0x198e0
-  __AUTH_CONST.__objc_const: 0x17190
+  __DATA_CONST.__objc_superrefs: 0x4b0
+  __DATA_CONST.__objc_arraydata: 0x6b8
+  __DATA_CONST.__got: 0xec0
+  __AUTH_CONST.__const: 0x1bd0
+  __AUTH_CONST.__cfstring: 0x19380
+  __AUTH_CONST.__objc_const: 0x16d18
   __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH_CONST.__auth_got: 0x9a8
   __AUTH.__objc_data: 0x3a10
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x1274
+  __DATA.__objc_ivar: 0x1214
   __DATA.__data: 0x1308
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x158
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x78
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5668
-  Symbols:   13467
-  CStrings:  7269
+  Functions: 5606
+  Symbols:   13301
+  CStrings:  7182
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[SMMacUser_Daemon excludedUserHomePaths]
+ +[SMSandboxTools _logPreShoveDiagnosticsForDestination:]
+ -[SMHomeDirectoryCopiersPlanEntry .cxx_destruct]
+ -[SMHomeDirectoryCopiersPlanEntry relativeHomeDir]
+ -[SMHomeDirectoryCopiersPlanEntry setRelativeHomeDir:]
+ -[SMHomeDirectoryCopiersPlanEntry setSourceUser:]
+ -[SMHomeDirectoryCopiersPlanEntry sourceUser]
+ -[SMLegacyNetworkDirectoryEnumerator isCurrentPathDataless]
+ -[SMLocalDiskPathEnumerator isCurrentPathDataless]
+ -[SMMigrateUserHomesStep homeDirectoryCopiersPlan]
+ -[SMNetworkDirectoryEnumerator isCurrentPathDataless]
+ GCC_except_table158
+ OBJC_IVAR_$_SMHomeDirectoryCopiersPlanEntry._relativeHomeDir
+ OBJC_IVAR_$_SMHomeDirectoryCopiersPlanEntry._sourceUser
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_SMHomeDirectoryCopiersPlanEntry
+ _OBJC_METACLASS_$_SMHomeDirectoryCopiersPlanEntry
+ __OBJC_$_INSTANCE_METHODS_SMHomeDirectoryCopiersPlanEntry
+ __OBJC_$_INSTANCE_VARIABLES_SMHomeDirectoryCopiersPlanEntry
+ __OBJC_$_PROP_LIST_SMHomeDirectoryCopiersPlanEntry
+ __OBJC_CLASS_RO_$_SMHomeDirectoryCopiersPlanEntry
+ __OBJC_METACLASS_RO_$_SMHomeDirectoryCopiersPlanEntry
+ ___56+[SMSandboxTools _logPreShoveDiagnosticsForDestination:]_block_invoke
+ _logPreShoveDiagnosticsForDestination:.didCheck
+ _objc_msgSend$_logPreShoveDiagnosticsForDestination:
+ _objc_msgSend$excludedUserHomePaths
+ _objc_msgSend$homeDirectoryCopiersPlan
+ _objc_msgSend$isCurrentPathDataless
+ _objc_msgSend$setRelativeHomeDir:
- +[SMMacUser_Daemon pathsToNeverCopy]
- +[SMMessageTracing activeConnectionBenchmarkForSystem:]
- +[SMMessageTracing dominantConnectionForSystem:]
- +[SMMessageTracing mediaTypeForSystem:]
- +[SMMessageTracing mediumTypeForSystem:]
- +[SMMessageTracing sharedInstance]
- +[SMMessageTracing stringForMigrationClientError:]
- +[SMMessageTracing stringForPathDescription:]
- +[SMMessageTracing stringForWirelessError:]
- +[SMMessageTracing versionForSystem:]
- -[SMEngine gatherCompletionMessageTracerData]
- -[SMEngine messageTraceCancellation]
- -[SMEngine messageTraceStateCompletion]
- -[SMEngine setupMessageTracing]
- -[SMMessageTracing .cxx_destruct]
- -[SMMessageTracing attemptedSWAP]
- -[SMMessageTracing currentPhaseDetails]
- -[SMMessageTracing engineWaitedOnPather]
- -[SMMessageTracing error]
- -[SMMessageTracing estimatedTimeRemaining]
- -[SMMessageTracing expectedQuantityOfData]
- -[SMMessageTracing expectedTotalMigrationTime]
- -[SMMessageTracing fractionCompleted]
- -[SMMessageTracing init]
- -[SMMessageTracing messageTraceMigrationCancelled]
- -[SMMessageTracing messageTraceMigrationFinished]
- -[SMMessageTracing migratedMultipleUsers]
- -[SMMessageTracing numberOfDisconnects]
- -[SMMessageTracing numberOfFilesPathed]
- -[SMMessageTracing numberOfNetworkChanges]
- -[SMMessageTracing numberOfNetworkConfigurationChanges]
- -[SMMessageTracing quantityOfData]
- -[SMMessageTracing request]
- -[SMMessageTracing sendAnalyticsForOverallResults]
- -[SMMessageTracing setAttemptedSWAP:]
- -[SMMessageTracing setCurrentPhaseDetails:]
- -[SMMessageTracing setEngineWaitedOnPather:]
- -[SMMessageTracing setError:]
- -[SMMessageTracing setEstimatedTimeRemaining:]
- -[SMMessageTracing setExpectedQuantityOfData:]
- -[SMMessageTracing setExpectedTotalMigrationTime:]
- -[SMMessageTracing setFractionCompleted:]
- -[SMMessageTracing setMigratedMultipleUsers:]
- -[SMMessageTracing setNumberOfDisconnects:]
- -[SMMessageTracing setNumberOfFilesPathed:]
- -[SMMessageTracing setNumberOfNetworkChanges:]
- -[SMMessageTracing setNumberOfNetworkConfigurationChanges:]
- -[SMMessageTracing setQuantityOfData:]
- -[SMMessageTracing setRequest:]
- -[SMMessageTracing setSuccess:]
- -[SMMessageTracing setSwapAssociationDuration:]
- -[SMMessageTracing setSwapBenchmark:]
- -[SMMessageTracing setSwapComparisonToInfrastructure:]
- -[SMMessageTracing setSwapError:]
- -[SMMessageTracing setSystemConnected:]
- -[SMMessageTracing setTimeSinceOneMinuteRemaining:]
- -[SMMessageTracing setTotalMigrationTime:]
- -[SMMessageTracing setTotalPathingTime:]
- -[SMMessageTracing setTotalTimeMigrationDelayedByPathing:]
- -[SMMessageTracing setTransferRate:]
- -[SMMessageTracing success]
- -[SMMessageTracing swapAssociationDuration]
- -[SMMessageTracing swapBenchmark]
- -[SMMessageTracing swapComparisonToInfrastructure]
- -[SMMessageTracing swapError]
- -[SMMessageTracing systemConnected]
- -[SMMessageTracing timeSinceOneMinuteRemaining]
- -[SMMessageTracing totalMigrationTime]
- -[SMMessageTracing totalPathingTime]
- -[SMMessageTracing totalTimeMigrationDelayedByPathing]
- -[SMMessageTracing transferRate]
- -[SMMessageTracing usedSWAP]
- GCC_except_table162
- OBJC_IVAR_$_SMMessageTracing._attemptedSWAP
- OBJC_IVAR_$_SMMessageTracing._currentPhaseDetails
- OBJC_IVAR_$_SMMessageTracing._engineWaitedOnPather
- OBJC_IVAR_$_SMMessageTracing._error
- OBJC_IVAR_$_SMMessageTracing._estimatedTimeRemaining
- OBJC_IVAR_$_SMMessageTracing._expectedQuantityOfData
- OBJC_IVAR_$_SMMessageTracing._expectedTotalMigrationTime
- OBJC_IVAR_$_SMMessageTracing._fractionCompleted
- OBJC_IVAR_$_SMMessageTracing._migratedMultipleUsers
- OBJC_IVAR_$_SMMessageTracing._numberOfDisconnects
- OBJC_IVAR_$_SMMessageTracing._numberOfFilesPathed
- OBJC_IVAR_$_SMMessageTracing._numberOfNetworkChanges
- OBJC_IVAR_$_SMMessageTracing._numberOfNetworkConfigurationChanges
- OBJC_IVAR_$_SMMessageTracing._quantityOfData
- OBJC_IVAR_$_SMMessageTracing._request
- OBJC_IVAR_$_SMMessageTracing._success
- OBJC_IVAR_$_SMMessageTracing._swapAssociationDuration
- OBJC_IVAR_$_SMMessageTracing._swapBenchmark
- OBJC_IVAR_$_SMMessageTracing._swapComparisonToInfrastructure
- OBJC_IVAR_$_SMMessageTracing._swapError
- OBJC_IVAR_$_SMMessageTracing._systemConnected
- OBJC_IVAR_$_SMMessageTracing._timeSinceOneMinuteRemaining
- OBJC_IVAR_$_SMMessageTracing._totalMigrationTime
- OBJC_IVAR_$_SMMessageTracing._totalPathingTime
- OBJC_IVAR_$_SMMessageTracing._totalTimeMigrationDelayedByPathing
- OBJC_IVAR_$_SMMessageTracing._transferRate
- _OBJC_CLASS_$_IASMessageTracing
- _OBJC_CLASS_$_SMAnalyticsManager
- _OBJC_CLASS_$_SMMessageTracing
- _OBJC_METACLASS_$_SMMessageTracing
- _SMAnalyticsCAEventPayloadKeyErrorSignature
- _SMAnalyticsCAEventPayloadKeyMigrationID
- _SMAnalyticsCAEventPayloadKeyOriginatingApp
- _SMAnalyticsCAEventPayloadKeyOverallThroughput
- _SMAnalyticsCAEventPayloadKeyPhase
- _SMAnalyticsCAEventPayloadKeyPreferredTransferMode
- _SMAnalyticsCAEventPayloadKeyRequestState_1
- _SMAnalyticsCAEventPayloadKeyResult
- _SMAnalyticsCAEventPayloadKeySizeExpected
- _SMAnalyticsCAEventPayloadKeySizeTransferred
- _SMAnalyticsCAEventPayloadKeySourceType_1
- _SMAnalyticsCAEventPayloadKeyTimeExpected
- _SMAnalyticsCAEventPayloadKeyTimeTaken
- _SMAnalyticsCAEventPayloadKeyWireThroughput
- _SMAnalyticsCAEventPayloadKeyWireThroughputExpected
- __OBJC_$_CLASS_METHODS_SMMessageTracing
- __OBJC_$_INSTANCE_METHODS_SMMessageTracing
- __OBJC_$_INSTANCE_VARIABLES_SMMessageTracing
- __OBJC_$_PROP_LIST_SMMessageTracing
- __OBJC_CLASS_RO_$_SMMessageTracing
- __OBJC_METACLASS_RO_$_SMMessageTracing
- ___34+[SMMessageTracing sharedInstance]_block_invoke
- _objc_msgSend$activeConnectionBenchmarkForSystem:
- _objc_msgSend$attemptedSWAP
- _objc_msgSend$currentPhaseDetails
- _objc_msgSend$dominantConnectionForSystem:
- _objc_msgSend$engineWaitedOnPather
- _objc_msgSend$expectedQuantityOfData
- _objc_msgSend$expectedTotalMigrationTime
- _objc_msgSend$formatNumberForPrivacy:
- _objc_msgSend$gatherCompletionMessageTracerData
- _objc_msgSend$localConnectionMethod
- _objc_msgSend$mediaTypeForSystem:
- _objc_msgSend$mediumTypeForSystem:
- _objc_msgSend$messageTraceCancellation
- _objc_msgSend$messageTraceMigrationCancelled
- _objc_msgSend$messageTraceMigrationFinished
- _objc_msgSend$messageTraceStateCompletion
- _objc_msgSend$migratedMultipleUsers
- _objc_msgSend$numberOfDisconnects
- _objc_msgSend$numberOfFilesPathed
- _objc_msgSend$numberOfNetworkChanges
- _objc_msgSend$numberOfNetworkConfigurationChanges
- _objc_msgSend$originalUnderlyingErrorForError:
- _objc_msgSend$pathsToNeverCopy
- _objc_msgSend$quantityOfData
- _objc_msgSend$request
- _objc_msgSend$sendAnalyticsForOverallResults
- _objc_msgSend$setAttemptedSWAP:
- _objc_msgSend$setCurrentPhaseDetails:
- _objc_msgSend$setEngineWaitedOnPather:
- _objc_msgSend$setExpectedQuantityOfData:
- _objc_msgSend$setExpectedTotalMigrationTime:
- _objc_msgSend$setMigratedMultipleUsers:
- _objc_msgSend$setNumberOfDisconnects:
- _objc_msgSend$setNumberOfFilesPathed:
- _objc_msgSend$setNumberOfNetworkChanges:
- _objc_msgSend$setNumberOfNetworkConfigurationChanges:
- _objc_msgSend$setQuantityOfData:
- _objc_msgSend$setRequest:
- _objc_msgSend$setSuccess:
- _objc_msgSend$setSwapAssociationDuration:
- _objc_msgSend$setSwapBenchmark:
- _objc_msgSend$setSwapComparisonToInfrastructure:
- _objc_msgSend$setSwapError:
- _objc_msgSend$setSystemConnected:
- _objc_msgSend$setTimeSinceOneMinuteRemaining:
- _objc_msgSend$setTotalMigrationTime:
- _objc_msgSend$setTotalPathingTime:
- _objc_msgSend$setTotalTimeMigrationDelayedByPathing:
- _objc_msgSend$setupMessageTracing
- _objc_msgSend$stringForMigrationClientError:
- _objc_msgSend$stringForWirelessError:
- _objc_msgSend$success
- _objc_msgSend$swapAssociationDuration
- _objc_msgSend$swapComparisonToInfrastructure
- _objc_msgSend$swapError
- _objc_msgSend$timeDelayedByPathing
- _objc_msgSend$timeSinceOneMinuteRemaining
- _objc_msgSend$totalMigrationTime
- _objc_msgSend$totalPathingTime
- _objc_msgSend$totalTimeMigrationDelayedByPathing
- _objc_msgSend$traceEventOverallResults1_0:
- _objc_msgSend$traceMigrationCompleted:
- _objc_msgSend$traceMigrationTransferStatus:
- _objc_msgSend$traceODTokenIssuingSuccess:afterRetries:
- _objc_msgSend$traceQuarantinedPath:
- _objc_msgSend$versionForSystem:
- sharedInstance.messageTracing
CStrings:
+ "  - /%@: MISSING (errno=%d: %@)\n"
+ "  - /%@: OK\n"
+ "+[SMSandboxTools _logPreShoveDiagnosticsForDestination:]"
+ "-[SMMigrateUserHomesStep homeDirectoryCopiersPlan]"
+ "/Data/Library/Caches/"
+ "/Data/tmp/"
+ "/Library/Caches/"
+ "AllContexts"
+ "Analytics rollover: FAILED"
+ "Analytics rollover: SUCCESS"
+ "Library/Containers/"
+ "Library/Group Containers/"
+ "Library/IdentityServices/TetraDB-identityservicesd.db"
+ "Library/IdentityServices/TetraDB-identityservicesd.db-shm"
+ "Library/IdentityServices/TetraDB-identityservicesd.db-wal"
+ "ShoveVerboseLogging"
+ "Skipping duplicate home directory copier for %@ (source %@ already scheduled)"
+ "[%s] Pre-shove data template well-formedness check on %@:\n"
+ "[%s] Pre-shove diagnostic: %@ exists but is NOT traversable: %@."
+ "[%s] Pre-shove diagnostic: %@ — DOES NOT EXIST on data volume (stat errno=%d: %@)."
+ "[%s] Pre-shove diagnostic: %@ — OK (directory with %lu items)"
+ "[%s] Pre-shove diagnostic: could not read firmlink manifest from system volume — skipping well-formedness check."
+ "[SMPaths] Skipping Group Container cache in user home: %@"
+ "[SMPaths] Skipping container cache/tmp in user home: %@"
+ "[SMPaths] Skipping dataless directory in user home: %@"
+ "[SMPaths] Skipping dataless directory: %@"
+ "com.apple.PackageKit"
- " - %@"
- " - Underlying error is %@ (%ld)"
- "+[SMMessageTracing versionForSystem:]"
- "-[SMMigrateUserHomesStep createHomeDirectoryCopiersForUsers]"
- "Already Hosting"
- "Analytics rollover: FAILED ❌"
- "Analytics rollover: SUCCESS ✅"
- "Association Failed"
- "Association Timeout"
- "Both"
- "CopiedRelocatedHomes"
- "CurrentPhaseDetails"
- "DataQuantity"
- "DidAttemptSWAP"
- "DidSpotlightFinishIndexing"
- "DidWaitOnPather"
- "Excluding paths by configuration: %@"
- "HadIncompatibleApps"
- "HadRelocatedHomes"
- "Hosting Failed"
- "Hosting Timeout"
- "IsOSUpgrade"
- "Mac"
- "Multiple Users"
- "NWMedia"
- "Network Action Failure"
- "No Common Channels"
- "No Error"
- "No Networks Found"
- "No connection type"
- "No data quantity"
- "No error description"
- "No id"
- "No originating app"
- "No overall throughput"
- "No phase"
- "No phase details"
- "No request state"
- "No source system"
- "No time taken"
- "No wire throughput"
- "NoContext"
- "Not Supported"
- "NumberOFNWChanges"
- "NumberOFNWConfigurationChanges"
- "NumberOFNWDisconnects"
- "NumberOfFilesPathed"
- "NumberOfUsers"
- "One User"
- "Other Wireless Error (%ld)"
- "PathingDelay"
- "Processing"
- "SWAPAssociationDuration"
- "SWAPComparison"
- "SWAPError"
- "Scan Failed"
- "Source System Refused Connection"
- "Source System Unavailable"
- "SourceModelID"
- "SourceOSType"
- "SourceType"
- "SpotlightingDelay"
- "Success"
- "TimeSinceOneMinuteRemaining"
- "TransferRate"
- "Unable to determine system version for usage data for system: %@"
- "Unknown (%@)"
- "Unknown (No Migration Request)"
- "Unknown Error"
- "oldShortName != %@"

```
