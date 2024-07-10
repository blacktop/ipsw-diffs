## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/Versions/A/NewsCore`

```diff

-5559.0.0.0.0
-  __TEXT.__text: 0x3454b4
+5553.0.0.0.0
+  __TEXT.__text: 0x33e34c
   __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x2b54c
+  __TEXT.__objc_methlist: 0x2b1d0
   __TEXT.__swift5_typeref: 0x1c4
-  __TEXT.__const: 0x16a8
+  __TEXT.__const: 0x1648
   __TEXT.__swift5_capture: 0xc0
-  __TEXT.__cstring: 0x4fe35
+  __TEXT.__cstring: 0x4fb7d
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_reflstr: 0xa7
   __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x10
-  __TEXT.__oslogstring: 0x11d6f
-  __TEXT.__gcc_except_tab: 0x507c
+  __TEXT.__oslogstring: 0x11f94
+  __TEXT.__gcc_except_tab: 0x54dc
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x14a
-  __TEXT.__unwind_info: 0xa410
+  __TEXT.__unwind_info: 0xa380
   __TEXT.__eh_frame: 0x90
-  __TEXT.__objc_classname: 0x7208
-  __TEXT.__objc_methname: 0x7f157
-  __TEXT.__objc_methtype: 0xc404
-  __TEXT.__objc_stubs: 0x32460
-  __DATA_CONST.__got: 0x2298
-  __DATA_CONST.__const: 0x6158
-  __DATA_CONST.__objc_classlist: 0x1ad0
+  __TEXT.__objc_classname: 0x7153
+  __TEXT.__objc_methname: 0x7e675
+  __TEXT.__objc_methtype: 0xc320
+  __TEXT.__objc_stubs: 0x32160
+  __DATA_CONST.__got: 0x2268
+  __DATA_CONST.__const: 0x5fc8
+  __DATA_CONST.__objc_classlist: 0x1aa8
   __DATA_CONST.__objc_catlist: 0x268
-  __DATA_CONST.__objc_protolist: 0x720
+  __DATA_CONST.__objc_protolist: 0x718
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x131e8
+  __DATA_CONST.__objc_selrefs: 0x13050
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x1520
-  __DATA_CONST.__objc_arraydata: 0x1090
+  __DATA_CONST.__objc_superrefs: 0x14e8
+  __DATA_CONST.__objc_arraydata: 0x1070
   __AUTH_CONST.__auth_got: 0xa78
   __AUTH_CONST.__auth_ptr: 0xd0
-  __AUTH_CONST.__const: 0x10e20
-  __AUTH_CONST.__cfstring: 0x2bb00
-  __AUTH_CONST.__objc_const: 0x7aed8
-  __AUTH_CONST.__objc_intobj: 0x1398
-  __AUTH_CONST.__objc_arrayobj: 0x330
+  __AUTH_CONST.__const: 0x10bf0
+  __AUTH_CONST.__cfstring: 0x2b780
+  __AUTH_CONST.__objc_const: 0x7a378
+  __AUTH_CONST.__objc_intobj: 0x1380
+  __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xc58
-  __AUTH_CONST.__objc_doubleobj: 0x120
-  __AUTH.__objc_data: 0x9388
+  __AUTH_CONST.__objc_doubleobj: 0x130
+  __AUTH.__objc_data: 0x9158
   __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x5158
-  __DATA.__data: 0x5620
-  __DATA.__bss: 0x1088
+  __DATA.__objc_ivar: 0x50dc
+  __DATA.__data: 0x55c0
+  __DATA.__bss: 0x1098
   __DATA.__common: 0xaa
-  __DATA_DIRTY.__objc_data: 0x79e0
+  __DATA_DIRTY.__objc_data: 0x7a80
   __DATA_DIRTY.__common: 0x100
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19078
-  Symbols:   42743
-  CStrings:  8226
+  Functions: 18992
+  Symbols:   42513
+  CStrings:  8185
 
Symbols:
+ +[FCCKPrivateDatabase sensitiveSubscriptionsZoneSchema]
+ +[FCCKPrivateDatabase subscriptionFields]
+ +[FCCKPrivateDatabase subscriptionsZoneSchema]
+ +[FCCKPrivateDatabaseSchema databaseSchemaWithZones:]
+ +[FCCKRecordSchema recordWithClientType:serverType:fields:]
+ +[FCCKZoneSchema defaultZoneWithRecords:staticRecordNames:staticRecordNameMigrationBlacklist:shouldUseSecureContainer:]
+ +[FCCKZoneSchema zoneWithClientName:serverName:records:staticRecordNames:shouldEncryptRecordNames:shouldUseZoneWidePCS:shouldUseSecureContainer:]
+ +[FCMescalSignature signatureFromData:error:]
+ +[TCKDatabase tRecordsForQuery:zoneID:]
+ -[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]
+ -[FCAssetHandle fetchDataProviderWithPriority:completion:]
+ -[FCCKDatabaseEncryptedZoneMigrator _isEnabledForDatabase:]
+ -[FCCKDatabaseEncryptedZoneMigrator databaseMigrationRecordNamesToMigrateInZone:database:]
+ -[FCCKDatabaseEncryptedZoneMigrator databaseMigrationShouldMigrateEntireZone:database:]
+ -[FCCKDatabaseEncryptedZoneMigrator databaseMigrationZoneNamesForDatabase:]
+ -[FCCKDatabaseEncryptedZoneMigrator initWithSourceSchema:recordEncryptionMiddleware:deprecatedBlock:]
+ -[FCCKDatabaseEncryptionMiddleware _decryptedRecordIDWithOriginalRecordID:withEncryptionKey:error:]
+ -[FCCKDatabaseEncryptionMiddleware _encryptedRecordIDWithOriginalRecordID:withEncryptionKey:error:]
+ -[FCCKDatabaseEncryptionMiddleware _serverZoneIDFromClientZoneID:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware _secureZoneID]
+ -[FCCKDatabaseSubscriptionsMiddleware _shouldMapZoneID:inDatabase:]
+ -[FCCKDatabaseSubscriptionsMiddleware clientToServerRecord:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordID:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordType:withRecordID:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordZone:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordZoneID:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware serverToClientRecord:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware serverToClientRecordID:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware serverToClientRecordType:withRecordID:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware serverToClientRecordZone:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsMiddleware serverToClientRecordZoneID:inDatabase:error:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware .cxx_destruct]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseSentinelModificationWithDatabase:modification:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware _runChildOperation:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationDidFinishForDatabase:result:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationMigrateRecord:database:error:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationRecordNamesToMigrateInZone:database:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationShouldDropRecord:database:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationShouldMigrateEntireZone:database:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationZoneNamesForDatabase:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware initWithLegacyZoneSchema:secureZoneSchema:encryptionMiddlewawre:]
+ -[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]
+ -[FCCKPrivateDatabase _mapObjects:withRecordMiddlewareBlock:]
+ -[FCCKPrivateDatabaseSchema enumerateDefaultZoneSchemasWithBlock:]
+ -[FCCKPrivateDatabaseSchema schemaForZoneContainingClientRecordID:]
+ -[FCCKPrivateDatabaseSchema schemaForZoneContainingServerRecordID:]
+ -[FCCKPrivateDatabaseSchema schemaForZoneWithClientName:]
+ -[FCCKPrivateDatabaseSchema schemaForZoneWithServerName:]
+ -[FCCKRecordSchema hasEncryptedFields]
+ -[FCCKZoneSchema clientRecordNameForServerRecordName:]
+ -[FCCKZoneSchema initWithClientZoneName:serverZoneName:recordSchemas:staticRecordNames:staticRecordNameMigrationBlacklist:shouldEncryptRecordNames:shouldUseZoneWidePCS:shouldUseSecureContainer:]
+ -[FCCKZoneSchema isKnownClientRecordName:]
+ -[FCCKZoneSchema schemaForRecordWithClientType:]
+ -[FCCKZoneSchema serverRecordNameForClientRecordName:]
+ -[FCCKZoneSchema shouldDecryptServerRecordName:]
+ -[FCCKZoneSchema shouldEncryptClientRecordName:]
+ -[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]
+ -[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]
+ -[FCCloudContext fetchPrivateDataEncryptionIsRequiredForDatabase:completion:]
+ -[FCCloudContext fetchPrivateDataEncryptionMigrationIsDesiredForDatabase:completion:]
+ -[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]
+ -[FCNotificationsEndpointConnection _notificationEntityForTopicRequestFromChannelID:]
+ -[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleHistoryItemAndReturnExpectations]
+ -[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleTypeSettingsAndReturnExpectations]
+ -[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutCategoriesAndReturnExpectations]
+ -[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutsAndReturnExpectations]
+ -[FCPrivateDataEncryptionMigrationHealthCheck fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]
+ -[FCPrivateDataEncryptionMigrationHealthCheck fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]
+ -[FCPrivateDataEncryptionMigrationHealthCheck fetchPrivateDataEncryptionIsRequiredForDatabase:completion:]
+ -[FCPrivateDataEncryptionMigrationHealthCheck fetchPrivateDataEncryptionMigrationIsDesiredForDatabase:completion:]
+ -[FCPrivateDataEncryptionMigrationHealthCheck fetchShouldSecureSubscriptionsForDatabase:completion:]
+ -[FCPuzzleHistory _updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:]
+ -[FCPuzzleHistory updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:isSolved:]
+ -[FCPuzzleHistoryItem initWithEntryID:puzzleID:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:firstCompletedDate:firstPlayDuration:bestScore:]
+ -[FCReadablePrivateDataStorage readPrivateDataWithAccessor:]
+ -[TCKDatabase fetchRecordWithID:completionHandler:]
+ -[TCKDatabase performQuery:inZoneWithID:completionHandler:]
+ GCC_except_table117
+ GCC_except_table24
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table90
+ GCC_except_table94
+ OBJC_IVAR_$_FCCKDatabaseEncryptedZoneMigrator._sourceSchema
+ OBJC_IVAR_$_FCCKDatabaseEncryptedZoneMigrator._sourceZoneNames
+ OBJC_IVAR_$_FCCKDatabaseSubscriptionsStartUpMiddleware._encryptionMiddleware
+ OBJC_IVAR_$_FCCKDatabaseSubscriptionsStartUpMiddleware._legacyZoneSchema
+ OBJC_IVAR_$_FCCKDatabaseSubscriptionsStartUpMiddleware._secureZoneSchema
+ OBJC_IVAR_$_FCCKPrivateDatabase._encryptionEnabled
+ OBJC_IVAR_$_FCCKPrivateDatabase._secureSubscriptionsEnabled
+ OBJC_IVAR_$_FCCKPrivateDatabaseSchema._zoneSchemasByClientName
+ OBJC_IVAR_$_FCCKPrivateDatabaseSchema._zoneSchemasByServerName
+ OBJC_IVAR_$_FCCKRecordSchema._clientRecordType
+ OBJC_IVAR_$_FCCKRecordSchema._serverRecordType
+ OBJC_IVAR_$_FCCKZoneSchema._clientZoneID
+ OBJC_IVAR_$_FCCKZoneSchema._clientZoneName
+ OBJC_IVAR_$_FCCKZoneSchema._isDefaultZone
+ OBJC_IVAR_$_FCCKZoneSchema._recordSchemasByClientType
+ OBJC_IVAR_$_FCCKZoneSchema._recordSchemasByServerType
+ OBJC_IVAR_$_FCCKZoneSchema._serverZoneID
+ OBJC_IVAR_$_FCCKZoneSchema._serverZoneName
+ OBJC_IVAR_$_FCCKZoneSchema._staticClientRecordNamesByServerName
+ OBJC_IVAR_$_FCCKZoneSchema._staticRecordNamesEligibleForMigration
+ OBJC_IVAR_$_FCCKZoneSchema._staticServerRecordNamesByClientName
+ OBJC_IVAR_$_FCCKZoneSchema._supportsRecordFieldEncryption
+ OBJC_IVAR_$_FCCKZoneSchema._supportsRecordNameEncryption
+ _FCCKUserInfoStaticSecureRecordName
+ _FCEncryptionBehaviorOverrideKey
+ _FCEncryptionForceDeleteAfterMigrationKey
+ _FCEncryptionForceMigrationEveryLaunchKey
+ _FCEncryptionMigrationDisabledKey
+ _FCEncryptionRequiredBehaviorOverrideSharedPreferenceKey
+ _MergedGlobals.86
+ _OBJC_$_PROP_LIST_FCAppleAccount.251
+ _OBJC_$_PROP_LIST_FCMutableTodayPrivateData.247
+ _OBJC_$_PROP_LIST_FCNewsletterManager.320
+ _OBJC_$_PROP_LIST_FCTodayPrivateData.191
+ _OBJC_CLASS_$_FCCKDatabaseSubscriptionsMiddleware
+ _OBJC_CLASS_$_FCCKDatabaseSubscriptionsStartUpMiddleware
+ _OBJC_METACLASS_$_FCCKDatabaseSubscriptionsMiddleware
+ _OBJC_METACLASS_$_FCCKDatabaseSubscriptionsStartUpMiddleware
+ __105-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataWithSentinel:secureSentinel:database:completion:]_block_invoke.52
+ __105-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataWithSentinel:secureSentinel:database:completion:]_block_invoke.54
+ __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.30
+ __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.32
+ __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.38
+ __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.41
+ __185-[FCEndpointConnection performAuthenticatedHTTPRequestWithURL:valuesByHTTPHeaderField:method:data:contentType:priority:reauthenticateIfNeeded:networkEventType:callbackQueue:completion:]_block_invoke.38
+ __28-[TCKDatabase addOperation:]_block_invoke.15
+ __28-[TCKDatabase addOperation:]_block_invoke.17
+ __28-[TCKDatabase addOperation:]_block_invoke.23
+ __28-[TCKDatabase addOperation:]_block_invoke.26
+ __28-[TCKDatabase addOperation:]_block_invoke.34
+ __28-[TCKDatabase addOperation:]_block_invoke.38
+ __36-[FCCKPrivateDatabase addOperation:]_block_invoke.127
+ __36-[FCNewsletterManager optIntoSports]_block_invoke.51
+ __37-[FCNewsletterManager optOutOfIssues]_block_invoke.41
+ __37-[FCNewsletterManager optOutOfSports]_block_invoke.54
+ __38-[FCAppleAccount getNewGSTokenPromise]_block_invoke.79
+ __38-[FCAppleAccount getNewGSTokenPromise]_block_invoke_2.80
+ __39-[FCCKPrivateDatabase _continueStartUp]_block_invoke.165
+ __39-[FCHCZoneContentsExpectation validate]_block_invoke.456
+ __39-[FCHCZoneContentsExpectation validate]_block_invoke.463
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.21
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.23
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.25
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.31
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.37
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.39
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.52
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.56
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.57
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke_2.24
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke_2.38
+ __40-[FCUserVectorManager _fetchUserVector:]_block_invoke_2.40
+ __45-[FCNewsletterManager forceSubscriptionThen:]_block_invoke.45
+ __46-[FCNewsTabiConfiguration initWithDictionary:]_block_invoke.61
+ __48-[FCPersonalizationData _saveReadableAggregates]_block_invoke.88
+ __50-[FCAppleAccount getGSTokenWithCompletionHandler:]_block_invoke.70
+ __51-[FCResourceArchiveFetchOperation performOperation]_block_invoke.7
+ __51-[FCResourceArchiveFetchOperation performOperation]_block_invoke_2.8
+ __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.11
+ __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.14
+ __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.8
+ __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.9
+ __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2.10
+ __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2.12
+ __55-[FCPersonalizationData _applicationDidEnterBackground]_block_invoke.61
+ __55-[FCPersonalizationData _applicationDidEnterBackground]_block_invoke_2.62
+ __55-[FCPersonalizationData _applicationDidEnterBackground]_block_invoke_3.63
+ __56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke.81
+ __56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke_2.85
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.32
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.34
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.35
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.47
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke_2.33
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke_2.37
+ __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke_2.48
+ __60-[FCReadablePrivateDataStorage readPrivateDataWithAccessor:]_block_invoke.13
+ __60-[FCReadablePrivateDataStorage readPrivateDataWithAccessor:]_block_invoke.17
+ __61-[FCAVAssetKeyService _performHTTPRequest:keyURI:completion:]_block_invoke.81
+ __61-[FCAVAssetKeyService _performHTTPRequest:keyURI:completion:]_block_invoke.91
+ __61-[FCAVAssetKeyService _performHTTPRequest:keyURI:completion:]_block_invoke_2.80
+ __61-[FCAVAssetKeyService _performHTTPRequest:keyURI:completion:]_block_invoke_2.93
+ __67-[FCCKPrivateDatabase _preflightRecordsInDatabaseChangesOperation:]_block_invoke.224
+ __67-[FCPrivateDataEncryptionMigrationHealthCheck _eraseAllPrivateData]_block_invoke.23
+ __67-[FCPrivateDataEncryptionMigrationHealthCheck _eraseAllPrivateData]_block_invoke.28
+ __68-[FCFileCoordinatedTodayDropboxTransaction todayPrivateDataAccessor]_block_invoke.367
+ __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.202
+ __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.206
+ __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.210
+ __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.214
+ __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.218
+ __69-[FCTelemetryBasedOfflineNetworkTransitionOperation logNetworkEvent:]_block_invoke.24
+ __71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke.223
+ __71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke.224
+ __71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke_2.225
+ __74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke.12
+ __74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke.18
+ __74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke.9
+ __74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_2.19
+ __74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_3.20
+ __76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.185
+ __76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.196
+ __76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.198
+ __76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke.199
+ __76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2.186
+ __77-[FCCloudContext fetchPrivateDataEncryptionIsRequiredForDatabase:completion:]_block_invoke.207
+ __77-[FCResourceArchiveFetchOperation _ensureResourcesAreReadyForUse:completion:]_block_invoke.41
+ __77-[FCResourceArchiveFetchOperation _ensureResourcesAreReadyForUse:completion:]_block_invoke_2.42
+ __80-[FCCKDatabaseEncryptionStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.16
+ __80-[FCCKDatabaseEncryptionStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.3
+ __80-[FCCKDatabaseEncryptionStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_2.4
+ __80-[FCResourceArchiveFetchOperation _unzipResourcesFromArchiveFileURL:completion:]_block_invoke.32
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.1
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.13
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.18
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.21
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.5
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.6
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.7
+ __83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.9
+ __83-[FCPrivateDataEncryptionMigrationHealthCheck _prepareHistoryAndReturnExpectations]_block_invoke.53
+ __83-[FCPrivateDataEncryptionMigrationHealthCheck _prepareHistoryAndReturnExpectations]_block_invoke_2.54
+ __84-[FCPrivateDataEncryptionMigrationHealthCheck _prepareUserInfoAndReturnExpectations]_block_invoke.196
+ __84-[FCPrivateDataEncryptionMigrationHealthCheck _prepareUserInfoAndReturnExpectations]_block_invoke_2.197
+ __85-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationIsAllowedWithDatabase:]_block_invoke.37
+ __87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke.210
+ __87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke.211
+ __87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke_2.212
+ __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareReadingListAndReturnExpectations]_block_invoke.101
+ __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareReadingListAndReturnExpectations]_block_invoke_2.102
+ __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareTagSettingsAndReturnExpectations]_block_invoke.212
+ __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareTagSettingsAndReturnExpectations]_block_invoke_2.213
+ __88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke.26
+ __88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke.27
+ __88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke.29
+ __88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke_2.28
+ __88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke_2.30
+ __89-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSubscriptionsAndReturnExpectations]_block_invoke.150
+ __89-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSubscriptionsAndReturnExpectations]_block_invoke_2.151
+ __93-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleHistoryItemAndReturnExpectations]_block_invoke.292
+ __93-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleHistoryItemAndReturnExpectations]_block_invoke_2.293
+ __98-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSensitiveSubscriptionsAndReturnExpectations]_block_invoke.166
+ __98-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSensitiveSubscriptionsAndReturnExpectations]_block_invoke_2.167
+ __99-[FCCKDatabaseEncryptionStartUpMiddleware _migrateWithSentinel:secureSentinel:database:completion:]_block_invoke.35
+ __99-[FCCKDatabaseEncryptionStartUpMiddleware _migrateWithSentinel:secureSentinel:database:completion:]_block_invoke.42
+ __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.138
+ __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.142
+ __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.146
+ __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.152
+ __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke_2.154
+ __OBJC_$_CLASS_METHODS_TCKDatabase
+ __OBJC_$_INSTANCE_METHODS_FCCKDatabaseSubscriptionsMiddleware
+ __OBJC_$_INSTANCE_METHODS_FCCKDatabaseSubscriptionsStartUpMiddleware
+ __OBJC_$_INSTANCE_VARIABLES_FCCKDatabaseSubscriptionsStartUpMiddleware
+ __OBJC_$_PROP_LIST_FCCKDatabaseSubscriptionsMiddleware
+ __OBJC_$_PROP_LIST_FCCKDatabaseSubscriptionsStartUpMiddleware
+ __OBJC_CLASS_PROTOCOLS_$_FCCKDatabaseSubscriptionsMiddleware
+ __OBJC_CLASS_PROTOCOLS_$_FCCKDatabaseSubscriptionsStartUpMiddleware
+ __OBJC_CLASS_RO_$_FCCKDatabaseSubscriptionsMiddleware
+ __OBJC_CLASS_RO_$_FCCKDatabaseSubscriptionsStartUpMiddleware
+ __OBJC_METACLASS_RO_$_FCCKDatabaseSubscriptionsMiddleware
+ __OBJC_METACLASS_RO_$_FCCKDatabaseSubscriptionsStartUpMiddleware
+ ___100-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseSentinelModificationWithDatabase:modification:]_block_invoke_2
+ ___100-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseSentinelModificationWithDatabase:modification:]_block_invoke_3
+ ___100-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseSentinelModificationWithDatabase:modification:]_block_invoke_4
+ ___101-[FCCKDatabaseEncryptedZoneMigrator initWithSourceSchema:recordEncryptionMiddleware:deprecatedBlock:]_block_invoke
+ ___101-[FCCKDatabaseEncryptedZoneMigrator initWithSourceSchema:recordEncryptionMiddleware:deprecatedBlock:]_block_invoke_2
+ ___105-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataWithSentinel:secureSentinel:database:completion:]_block_invoke
+ ___105-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataWithSentinel:secureSentinel:database:completion:]_block_invoke_2
+ ___105-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataWithSentinel:secureSentinel:database:completion:]_block_invoke_3
+ ___105-[FCPrivateDataEncryptionMigrationHealthCheck fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke
+ ___139-[FCPuzzleHistory _updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:]_block_invoke
+ ___43-[FCPersonalizationData localStoreMigrator]_block_invoke_2
+ ___51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_3
+ ___51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_4
+ ___51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_5
+ ___52-[FCCKDatabaseSubscriptionsMiddleware _secureZoneID]_block_invoke
+ ___58-[FCAssetHandle fetchDataProviderWithPriority:completion:]_block_invoke
+ ___59-[TCKDatabase performQuery:inZoneWithID:completionHandler:]_block_invoke
+ ___60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke_3
+ ___60-[FCReadablePrivateDataStorage readPrivateDataWithAccessor:]_block_invoke
+ ___61-[FCAVAssetKeyService _performHTTPRequest:keyURI:completion:]_block_invoke_2
+ ___67-[FCCKPrivateDatabaseSchema schemaForZoneContainingClientRecordID:]_block_invoke
+ ___67-[FCCKPrivateDatabaseSchema schemaForZoneContainingServerRecordID:]_block_invoke
+ ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke
+ ___71-[FCCloudContext fetchShouldSecureSubscriptionsForDatabase:completion:]_block_invoke_2
+ ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke
+ ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_2
+ ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_3
+ ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_4
+ ___75-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseDeletionWithDatabase:]_block_invoke_2
+ ___75-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseDeletionWithDatabase:]_block_invoke_3
+ ___75-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseDeletionWithDatabase:]_block_invoke_4
+ ___76-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationWithDatabase:]_block_invoke_2
+ ___76-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationWithDatabase:]_block_invoke_3
+ ___76-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationWithDatabase:]_block_invoke_4
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke
+ ___76-[FCCloudContext fetchPrivateDataEncryptionIsAllowedForDatabase:completion:]_block_invoke_2
+ ___77-[FCCKDatabaseSubscriptionsMiddleware clientToServerRecord:inDatabase:error:]_block_invoke
+ ___77-[FCCloudContext fetchPrivateDataEncryptionIsRequiredForDatabase:completion:]_block_invoke
+ ___77-[FCCloudContext fetchPrivateDataEncryptionIsRequiredForDatabase:completion:]_block_invoke_2
+ ___79-[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordID:inDatabase:error:]_block_invoke
+ ___81-[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordZone:inDatabase:error:]_block_invoke
+ ___83-[FCCKDatabaseSubscriptionsMiddleware clientToServerRecordZoneID:inDatabase:error:]_block_invoke
+ ___83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke
+ ___83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_2
+ ___83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_3
+ ___83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_4
+ ___83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_5
+ ___83-[FCCKDatabaseSubscriptionsStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_6
+ ___85-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationIsAllowedWithDatabase:]_block_invoke
+ ___85-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationIsAllowedWithDatabase:]_block_invoke_2
+ ___85-[FCCKDatabaseSubscriptionsStartUpMiddleware _promiseMigrationIsAllowedWithDatabase:]_block_invoke_3
+ ___85-[FCCloudContext fetchPrivateDataEncryptionMigrationIsDesiredForDatabase:completion:]_block_invoke
+ ___85-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutsAndReturnExpectations]_block_invoke
+ ___85-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutsAndReturnExpectations]_block_invoke_2
+ ___85-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutsAndReturnExpectations]_block_invoke_3
+ ___85-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutsAndReturnExpectations]_block_invoke_4
+ ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke
+ ___87-[FCCloudContext fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:]_block_invoke_2
+ ___88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke
+ ___88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke_2
+ ___88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke_3
+ ___88-[FCCKDatabaseEncryptionStartUpMiddleware _tryToEnableEncryptionForDatabase:completion:]_block_invoke_4
+ ___90-[FCCKDatabaseEncryptedZoneMigrator databaseMigrationRecordNamesToMigrateInZone:database:]_block_invoke
+ ___90-[FCCKDatabaseEncryptedZoneMigrator databaseMigrationRecordNamesToMigrateInZone:database:]_block_invoke_2
+ ___93-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleHistoryItemAndReturnExpectations]_block_invoke
+ ___93-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleHistoryItemAndReturnExpectations]_block_invoke_2
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleTypeSettingsAndReturnExpectations]_block_invoke
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleTypeSettingsAndReturnExpectations]_block_invoke_2
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleTypeSettingsAndReturnExpectations]_block_invoke_3
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _preparePuzzleTypeSettingsAndReturnExpectations]_block_invoke_4
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutCategoriesAndReturnExpectations]_block_invoke
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutCategoriesAndReturnExpectations]_block_invoke_2
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutCategoriesAndReturnExpectations]_block_invoke_3
+ ___94-[FCPrivateDataEncryptionMigrationHealthCheck _prepareShortcutCategoriesAndReturnExpectations]_block_invoke_4
+ ___99-[FCCKDatabaseEncryptionStartUpMiddleware _migrateWithSentinel:secureSentinel:database:completion:]_block_invoke
+ ___99-[FCCKDatabaseEncryptionStartUpMiddleware _migrateWithSentinel:secureSentinel:database:completion:]_block_invoke_2
+ ___FCCKDatabaseRecordIDsToDeleteAfterMigration_block_invoke
+ ___block_descriptor_32_e18_v16?0"CKRecord"8l
+ ___block_descriptor_40_e8_32bs_e16_16?0"NFVoid"8l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40r_e38_v16?0"NSObject<FCTodayPrivateData>"8l
+ ___block_descriptor_48_e8_32s40r_e8_16?08l
+ ___block_descriptor_48_e8_32s40s_e24_B16?0"CKRecordZoneID"8l
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_56_e8_32s40s48bs_e5_8?0l
+ ___block_descriptor_64_e8_32bs40r48r_e8_16?08l
+ ___block_descriptor_64_e8_32s40s48bs56bs_e43_v32?0"CKRecord"8"CKRecord"16"NSError"24l
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24l
+ ___block_descriptor_80_e8_32s40s48bs56r64r_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e5_v8?0l
+ __block_literal_global.101
+ __block_literal_global.1251
+ __block_literal_global.1321
+ __block_literal_global.1399
+ __block_literal_global.1401
+ __block_literal_global.1403
+ __block_literal_global.1411
+ __block_literal_global.1427
+ __block_literal_global.1437
+ __block_literal_global.159
+ __block_literal_global.162
+ __block_literal_global.1757
+ __block_literal_global.1789
+ __block_literal_global.1841
+ __block_literal_global.1854
+ __block_literal_global.1867
+ __block_literal_global.1892
+ __block_literal_global.1902
+ __block_literal_global.1915
+ __block_literal_global.2051
+ __block_literal_global.2076
+ __block_literal_global.2161
+ __block_literal_global.2174
+ __block_literal_global.332
+ __block_literal_global.369
+ __block_literal_global.84
+ __block_literal_global.886
+ __block_literal_global.915
+ __block_literal_global.99
+ _objc_msgSend$_notificationEntityForTopicRequestFromChannelID:
+ _objc_msgSend$_preparePuzzleHistoryItemAndReturnExpectations
+ _objc_msgSend$_preparePuzzleTypeSettingsAndReturnExpectations
+ _objc_msgSend$_prepareShortcutCategoriesAndReturnExpectations
+ _objc_msgSend$_prepareShortcutsAndReturnExpectations
+ _objc_msgSend$checkAlliOSDevicesRunningMinimumOSVersion:orInactiveForTimeInterval:completionHandler:
+ _objc_msgSend$computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:
+ _objc_msgSend$databaseMigrationRecordNamesToMigrateInZone:database:
+ _objc_msgSend$databaseMigrationShouldMigrateEntireZone:database:
+ _objc_msgSend$databaseMigrationZoneNamesForDatabase:
+ _objc_msgSend$downloadTaskWithURL:completionHandler:
+ _objc_msgSend$fc_secureSubscriptionsDisallowedError
+ _objc_msgSend$fetchDataProviderWithPriority:completion:
+ _objc_msgSend$fetchOriginalDataShouldBeDeletedAfterMigrationForDatabase:completion:
+ _objc_msgSend$fetchPrivateDataEncryptionIsAllowedForDatabase:completion:
+ _objc_msgSend$fetchPrivateDataEncryptionIsRequiredForDatabase:completion:
+ _objc_msgSend$fetchPrivateDataEncryptionMigrationIsDesiredForDatabase:completion:
+ _objc_msgSend$fetchShouldSecureSubscriptionsForDatabase:completion:
+ _objc_msgSend$initWithEntryID:puzzleID:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:firstCompletedDate:firstPlayDuration:bestScore:
+ _objc_msgSend$isPrivateDataEncryptionRequired
+ _objc_msgSend$setTQueriedRecordTypes:
+ _objc_msgSend$setTQueriedRecordZonesNames:
+ _objc_msgSend$setTQueriedRecords:
+ _objc_msgSend$signatureFromData:error:
+ _objc_msgSend$signatureFromData:type:bag:error:
+ _objc_msgSend$tQueriedRecordTypes
+ _objc_msgSend$tQueriedRecordZonesNames
+ _objc_msgSend$tQueriedRecords
+ _objc_msgSend$tQueryHandler
+ _objc_msgSend$tRecordsForQuery:zoneID:
- +[FCCKPrivateDatabase recordSchemas]
- +[FCCKPrivateDatabaseSchema databaseSchemaWithZones:records:recordTypeVersionMapping:recordNameVersionMapping:]
- +[FCCKPrivateDatabaseVersionMapping mappingWithBaseValues:V2Changes:V3Changes:V4Changes:]
- +[FCCKRecordSchema recordWithType:fields:]
- +[FCCKZoneSchema defaultZoneWithStaticRecordNames:shouldUseSecureContainer:]
- +[FCCKZoneSchema zoneWithName:]
- +[FCCKZoneSchema zoneWithName:options:staticRecordNames:]
- +[FCMescalSignature signatureFromData:completion:]
- -[CKRecord fc_sentinel_databaseVersion]
- -[CKRecord fc_sentinel_deletedToDatabaseVersion]
- -[CKRecord fc_sentinel_finishedDeletionToVersion]
- -[CKRecord fc_sentinel_finishedMigrationToVersion]
- -[CKRecord setFc_sentinel_databaseVersion:]
- -[CKRecord setFc_sentinel_deletedToDatabaseVersion:]
- -[CKRecord setFc_sentinel_finishedDeletionToVersion:]
- -[CKRecord setFc_sentinel_finishedMigrationToVersion:]
- -[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]
- -[FCAppleAccount fetchMinimumDeviceVersionsActiveSinceInterval:completionHandler:]
- -[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]
- -[FCAssetHandle fetchDataProviderWithPriority:flags:completion:]
- -[FCAssetKeyService executeRequest:callbackQueue:completion:]
- -[FCCKDatabaseEncryptedZoneMigrator databaseMigrationRecordNamesToMigrateInZone:fromVersion:toVersion:]
- -[FCCKDatabaseEncryptedZoneMigrator databaseMigrationShouldMigrateEntireZone:]
- -[FCCKDatabaseEncryptedZoneMigrator databaseMigrationZoneNamesFromVersion:toVersion:]
- -[FCCKDatabaseEncryptedZoneMigrator initWithSchema:recordEncryptionMiddleware:deprecatedBlock:]
- -[FCCKDatabaseEncryptionMiddleware _decryptedRecordIDWithOriginalRecordID:withEncryptionKey:mapping:error:]
- -[FCCKDatabaseEncryptionMiddleware _encryptedRecordIDWithOriginalRecordID:withEncryptionKey:mapping:error:]
- -[FCCKDatabaseEncryptionMiddleware _serverZoneIDFromClientZoneID:database:error:]
- -[FCCKPrivateDatabase _mapObjects:toClient:withBlock:]
- -[FCCKPrivateDatabaseSchema enumerateZoneSchemasForVersion:withBlock:]
- -[FCCKPrivateDatabaseSchema mappingFromRecord:toVersion:]
- -[FCCKPrivateDatabaseSchema mappingFromRecordID:toVersion:]
- -[FCCKPrivateDatabaseSchema mappingFromRecordType:inZoneID:toVersion:]
- -[FCCKPrivateDatabaseSchema mappingFromRecordType:inZoneName:toVersion:]
- -[FCCKPrivateDatabaseSchema mappingFromRecordZoneID:toVersion:]
- -[FCCKPrivateDatabaseSchema mappingFromRecordZoneName:toVersion:]
- -[FCCKPrivateDatabaseSchema recordNamesInDefaultZoneChangedFromVersion:toVersion:]
- -[FCCKPrivateDatabaseSchema schemaForZoneContainingRecordID:]
- -[FCCKPrivateDatabaseSchema schemaForZoneWithName:]
- -[FCCKPrivateDatabaseSchema zoneNamesWithChangesFromVersion:toVersion:]
- -[FCCKPrivateDatabaseVersionMapping .cxx_destruct]
- -[FCCKPrivateDatabaseVersionMapping V2Changes]
- -[FCCKPrivateDatabaseVersionMapping V3Changes]
- -[FCCKPrivateDatabaseVersionMapping V4Changes]
- -[FCCKPrivateDatabaseVersionMapping allValuesForVersion:]
- -[FCCKPrivateDatabaseVersionMapping allValuesModifiedFromVersion:toVersion:]
- -[FCCKPrivateDatabaseVersionMapping baseValues]
- -[FCCKPrivateDatabaseVersionMapping containsValuePassingTest:]
- -[FCCKPrivateDatabaseVersionMapping forwardMapToV2]
- -[FCCKPrivateDatabaseVersionMapping forwardMapToV3]
- -[FCCKPrivateDatabaseVersionMapping forwardMapToV4]
- -[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]
- -[FCCKPrivateDatabaseVersionMapping mapValue:toVersion:]
- -[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]
- -[FCCKPrivateDatabaseVersionMapping reverseMap]
- -[FCCKRecordFieldSchema hash]
- -[FCCKRecordFieldSchema isEqual:]
- -[FCCKRecordIDMapping .cxx_destruct]
- -[FCCKRecordIDMapping fromRecordID]
- -[FCCKRecordIDMapping fromRecordName]
- -[FCCKRecordIDMapping fromZoneSchema]
- -[FCCKRecordIDMapping hasChanges]
- -[FCCKRecordIDMapping initWithFromZoneSchema:toZoneSchema:fromRecordName:toRecordName:]
- -[FCCKRecordIDMapping toRecordID]
- -[FCCKRecordIDMapping toRecordName]
- -[FCCKRecordIDMapping toZoneSchema]
- -[FCCKRecordMapping .cxx_destruct]
- -[FCCKRecordMapping fromRecordSchema]
- -[FCCKRecordMapping fromZoneSchema]
- -[FCCKRecordMapping hasChanges]
- -[FCCKRecordMapping initWithFromZoneSchema:toZoneSchema:fromRecordSchema:toRecordSchema:recordIDMapping:]
- -[FCCKRecordMapping recordIDMapping]
- -[FCCKRecordMapping toRecordSchema]
- -[FCCKRecordMapping toZoneSchema]
- -[FCCKRecordSchema hash]
- -[FCCKRecordSchema isEqual:]
- -[FCCKRecordTypeMapping .cxx_destruct]
- -[FCCKRecordTypeMapping fromRecordSchema]
- -[FCCKRecordTypeMapping fromZoneSchema]
- -[FCCKRecordTypeMapping hasChanges]
- -[FCCKRecordTypeMapping initWithFromZoneSchema:toZoneSchema:fromRecordSchema:toRecordSchema:]
- -[FCCKRecordTypeMapping toRecordSchema]
- -[FCCKRecordTypeMapping toZoneSchema]
- -[FCCKRecordZoneIDMapping .cxx_destruct]
- -[FCCKRecordZoneIDMapping fromZoneSchema]
- -[FCCKRecordZoneIDMapping hasChanges]
- -[FCCKRecordZoneIDMapping initWithFromZoneSchema:toZoneSchema:]
- -[FCCKRecordZoneIDMapping toZoneSchema]
- -[FCCKZoneSchema hash]
- -[FCCKZoneSchema initWithZoneName:options:staticRecordNames:]
- -[FCCKZoneSchema isEqual:]
- -[FCCloudContext fetchCleanupToVersionForDatabase:completion:]
- -[FCCloudContext fetchDesiredVersionForDatabase:completion:]
- -[FCCloudContext setTabiBasedUserVectorAggregateVectorProvider:]
- -[FCFileCoordinatedTodayDropbox depositSyncWithAccessor:]
- -[FCFileCoordinatedTodayDropbox peekSyncWithAccessor:]
- -[FCNewsAppConfig enableTabiAdSegments]
- -[FCNewsAppConfig liveActivityScheduleDelay]
- -[FCNewsAppConfig liveActivityScheduleRandomInitialDelay]
- -[FCNewsAppConfig liveActivityScheduleTimeWindow]
- -[FCNewsAppConfig liveActivityScheduledAlertsThreshold]
- -[FCNewsAppConfig privateDataShouldCleanupAfterSecureSubscriptions]
- -[FCNewsAppConfig privateDataShouldCleanupToV4]
- -[FCNewsAppConfig privateDataShouldMigrateToV4]
- -[FCNewsTabiAdSegmentsEndpoint .cxx_destruct]
- -[FCNewsTabiAdSegmentsEndpoint adSegmentsOutputName]
- -[FCNewsTabiAdSegmentsEndpoint description]
- -[FCNewsTabiAdSegmentsEndpoint eventAggregationOutputs]
- -[FCNewsTabiAdSegmentsEndpoint initWithDictionary:]
- -[FCNewsTabiAdSegmentsEndpoint init]
- -[FCNewsTabiAdSegmentsEndpoint packageAssetID]
- -[FCNewsTabiConfiguration adSegmentsEndpoint]
- -[FCNewsTabiConfiguration setAdSegmentsEndpoint:]
- -[FCOperation flags]
- -[FCOperation setFlags:]
- -[FCPersonalizationData _unsafeReloadTreatment]
- -[FCPersonalizationTreatment computeUserVectorWithTabi]
- -[FCPersonalizationTreatment setComputeUserVectorWithTabi:]
- -[FCPrivateDataEncryptionMigrationHealthCheck fetchCleanupToVersionForDatabase:completion:]
- -[FCPrivateDataEncryptionMigrationHealthCheck fetchDesiredVersionForDatabase:completion:]
- -[FCPrivateDataEncryptionMigrationHealthCheck setToVersion:]
- -[FCPrivateDataEncryptionMigrationHealthCheck toVersion]
- -[FCPuzzle behaviorFlags]
- -[FCPuzzleHistory _updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:difficulty:publishDate:behaviorFlags:]
- -[FCPuzzleHistory updatePuzzle:difficulty:publishDate:behaviorFlags:]
- -[FCPuzzleHistory updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:isSolved:difficulty:publishDate:behaviorFlags:]
- -[FCPuzzleHistoryItem behaviorFlags]
- -[FCPuzzleHistoryItem difficulty]
- -[FCPuzzleHistoryItem initWithEntryID:puzzleID:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:firstCompletedDate:firstPlayDuration:bestScore:difficulty:publishDate:behaviorFlags:]
- -[FCPuzzleHistoryItem publishDate]
- -[FCReadablePrivateDataStorage readPrivateDataSyncWithAccessor:]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider .cxx_destruct]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider aggregateStore]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider aggregateVectorForTags:]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider initWithReadonlyPersonalizationAggregateStore:personalizationTreatment:]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider personalizationTreatment]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider setAggregateStore:]
- -[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider setPersonalizationTreatment:]
- -[FCUserVector computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:]
- -[FCUserVectorManager setTabiBasedAggregateVectorProvider:]
- -[FCUserVectorManager tabiBasedAggregateVectorProvider]
- -[NSError(FCAdditions) fc_failedDueToTaskConstraints]
- -[TCKDatabase addRecord:]
- -[TCKDatabase init]
- -[TCKDatabase recordIDsInZoneName:]
- -[TCKDatabase recordWithID:]
- -[TCKDatabase recordsByID]
- -[TCKDatabase secureSentinelRecord]
- -[TCKDatabase sentinelRecord]
- GCC_except_table54
- GCC_except_table91
- GCC_except_table96
- OBJC_IVAR_$_FCCKDatabaseEncryptedZoneMigrator._schema
- OBJC_IVAR_$_FCCKPrivateDatabase._currentVersion
- OBJC_IVAR_$_FCCKPrivateDatabase._migratingFromVersion
- OBJC_IVAR_$_FCCKPrivateDatabaseSchema._recordNameVersionMapping
- OBJC_IVAR_$_FCCKPrivateDatabaseSchema._recordSchemasByType
- OBJC_IVAR_$_FCCKPrivateDatabaseSchema._recordTypeVersionMapping
- OBJC_IVAR_$_FCCKPrivateDatabaseSchema._zoneNameVersionMapping
- OBJC_IVAR_$_FCCKPrivateDatabaseSchema._zoneSchemasByName
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._V2Changes
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._V3Changes
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._V4Changes
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._baseValues
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._forwardMapToV2
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._forwardMapToV3
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._forwardMapToV4
- OBJC_IVAR_$_FCCKPrivateDatabaseVersionMapping._reverseMap
- OBJC_IVAR_$_FCCKRecordIDMapping._fromRecordName
- OBJC_IVAR_$_FCCKRecordIDMapping._fromZoneSchema
- OBJC_IVAR_$_FCCKRecordIDMapping._toRecordName
- OBJC_IVAR_$_FCCKRecordIDMapping._toZoneSchema
- OBJC_IVAR_$_FCCKRecordMapping._fromRecordSchema
- OBJC_IVAR_$_FCCKRecordMapping._fromZoneSchema
- OBJC_IVAR_$_FCCKRecordMapping._recordIDMapping
- OBJC_IVAR_$_FCCKRecordMapping._toRecordSchema
- OBJC_IVAR_$_FCCKRecordMapping._toZoneSchema
- OBJC_IVAR_$_FCCKRecordSchema._recordType
- OBJC_IVAR_$_FCCKRecordTypeMapping._fromRecordSchema
- OBJC_IVAR_$_FCCKRecordTypeMapping._fromZoneSchema
- OBJC_IVAR_$_FCCKRecordTypeMapping._toRecordSchema
- OBJC_IVAR_$_FCCKRecordTypeMapping._toZoneSchema
- OBJC_IVAR_$_FCCKRecordZoneIDMapping._fromZoneSchema
- OBJC_IVAR_$_FCCKRecordZoneIDMapping._toZoneSchema
- OBJC_IVAR_$_FCCKZoneSchema._shouldEncryptRecordNames
- OBJC_IVAR_$_FCCKZoneSchema._staticRecordNames
- OBJC_IVAR_$_FCCKZoneSchema._zoneID
- OBJC_IVAR_$_FCCKZoneSchema._zoneName
- OBJC_IVAR_$_FCNewsAppConfig._privateDataShouldCleanupAfterSecureSubscriptions
- OBJC_IVAR_$_FCNewsAppConfig._privateDataShouldCleanupToV4
- OBJC_IVAR_$_FCNewsAppConfig._privateDataShouldMigrateToV4
- OBJC_IVAR_$_FCNewsTabiAdSegmentsEndpoint._adSegmentsOutputName
- OBJC_IVAR_$_FCNewsTabiAdSegmentsEndpoint._eventAggregationOutputs
- OBJC_IVAR_$_FCNewsTabiAdSegmentsEndpoint._packageAssetID
- OBJC_IVAR_$_FCNewsTabiConfiguration._adSegmentsEndpoint
- OBJC_IVAR_$_FCPersonalizationTreatment._computeUserVectorWithTabi
- OBJC_IVAR_$_FCPrivateDataEncryptionMigrationHealthCheck._toVersion
- OBJC_IVAR_$_FCPuzzle._behaviorFlags
- OBJC_IVAR_$_FCPuzzleHistoryItem._behaviorFlags
- OBJC_IVAR_$_FCPuzzleHistoryItem._difficulty
- OBJC_IVAR_$_FCPuzzleHistoryItem._publishDate
- OBJC_IVAR_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider._aggregateStore
- OBJC_IVAR_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider._personalizationTreatment
- OBJC_IVAR_$_FCUserVectorManager._tabiBasedAggregateVectorProvider
- OBJC_IVAR_$_TCKDatabase._recordsByID
- _FCCKAudioPlaylistItemRecordTypeSecure
- _FCCKAudioPlaylistItemRecordTypeSecure2
- _FCCKAudioPlaylistRecordZoneNameSecure
- _FCCKAudioPlaylistRecordZoneNameSecure2
- _FCCKIssueReadingHistoryItemRecordTypeSecure
- _FCCKIssueReadingHistoryItemRecordTypeSecure2
- _FCCKIssueReadingHistoryRecordZoneNameSecure
- _FCCKIssueReadingHistoryRecordZoneNameSecure2
- _FCCKPersonalizationProfileRecordTypeSecure
- _FCCKPrivateDatabaseVersionDebutOS
- _FCCKPrivateDatabaseVersionMin
- _FCCKPrivateDatabaseVersionMin3
- _FCCKPrivateDatabaseVersionString
- _FCCKPrivateDatabaseVersionSupportedByOS
- _FCCKPuzzleHistoryItemBehaviorFlagsKey
- _FCCKPuzzleHistoryItemDifficultyKey
- _FCCKPuzzleHistoryItemPublishDateKey
- _FCCKPuzzleHistoryItemRecordTypeSecure
- _FCCKPuzzleHistoryItemRecordTypeSecure2
- _FCCKPuzzleHistoryRecordZoneNameSecure
- _FCCKPuzzleHistoryRecordZoneNameSecure2
- _FCCKPuzzleTypeSettingsRecordTypeSecure
- _FCCKReadingHistoryItemRecordTypeSecure
- _FCCKReadingHistoryItemRecordTypeSecure2
- _FCCKReadingHistoryRecordZoneNameSecure
- _FCCKReadingHistoryRecordZoneNameSecure2
- _FCCKReadingListEntryRecordTypeSecure
- _FCCKReadingListEntryRecordTypeSecure2
- _FCCKReadingListRecordZoneNameSecure
- _FCCKReadingListRecordZoneNameSecure2
- _FCCKSentinelFinishedDeletionToVersionKey
- _FCCKSentinelFinishedMigrationToVersionKey
- _FCCKShortcutRecordTypeSecure
- _FCCKShortcutRecordTypeSecure2
- _FCCKShortcutsRecordZoneNameSecure
- _FCCKShortcutsRecordZoneNameSecure2
- _FCCKSubscriptionRecordTypeEncrypted
- _FCCKSubscriptionRecordTypeSecure
- _FCCKSubscriptionRecordTypeSecure2
- _FCCKSubscriptionsRecordZoneNameEncrypted
- _FCCKSubscriptionsRecordZoneNameSecure
- _FCCKSubscriptionsRecordZoneNameSecure2
- _FCCKTagSettingsRecordTypeSecure
- _FCCKTagSettingsRecordTypeSecure2
- _FCCKUserEventHistoryRecordZoneNameSecure
- _FCCKUserEventHistorySessionRecordTypeSecure
- _FCCKUserInfoRecordTypeSecure
- _FCCKUserInfoRecordTypeSecure2
- _FCCKUserInfoRecordZoneNameSecure
- _FCCKUserInfoRecordZoneNameSecure2
- _FCCKUserInfoStaticRecordNameSecure
- _FCCKUserInfoStaticRecordNameSecure2
- _FCEncryptionCleanupToVersionOverrideKey
- _FCEncryptionDesiredVersionOverrideKey
- _FCOSVersionCompare
- _FCOperationFlagsApplyToURLRequest
- _FCStringFromOSVersion
- _FCStringFromOSVersions
- _MergedGlobals.88
- _MergedGlobals.9
- _NSURLErrorNetworkUnavailableReasonKey
- _OBJC_$_PROP_LIST_FCAppleAccount.267
- _OBJC_$_PROP_LIST_FCMutableTodayPrivateData.250
- _OBJC_$_PROP_LIST_FCNewsletterManager.322
- _OBJC_$_PROP_LIST_FCTodayPrivateData.194
- _OBJC_CLASS_$_FCCKPrivateDatabaseVersionMapping
- _OBJC_CLASS_$_FCCKRecordIDMapping
- _OBJC_CLASS_$_FCCKRecordMapping
- _OBJC_CLASS_$_FCCKRecordTypeMapping
- _OBJC_CLASS_$_FCCKRecordZoneIDMapping
- _OBJC_CLASS_$_FCNewsTabiAdSegmentsEndpoint
- _OBJC_CLASS_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- _OBJC_METACLASS_$_FCCKPrivateDatabaseVersionMapping
- _OBJC_METACLASS_$_FCCKRecordIDMapping
- _OBJC_METACLASS_$_FCCKRecordMapping
- _OBJC_METACLASS_$_FCCKRecordTypeMapping
- _OBJC_METACLASS_$_FCCKRecordZoneIDMapping
- _OBJC_METACLASS_$_FCNewsTabiAdSegmentsEndpoint
- _OBJC_METACLASS_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __105-[FCCKDatabaseEncryptionStartUpMiddleware _migrateToVersion:sentinel:secureSentinel:database:completion:]_block_invoke.25
- __105-[FCCKDatabaseEncryptionStartUpMiddleware _migrateToVersion:sentinel:secureSentinel:database:completion:]_block_invoke.29
- __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.39
- __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.40
- __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.48
- __106-[FCUserVector computePersonalizationVectorWithAggregateStore:personalizationTreatment:tagRanker:options:]_block_invoke.49
- __113-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataUpToVersion:sentinel:secureSentinel:database:completion:]_block_invoke.42
- __113-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataUpToVersion:sentinel:secureSentinel:database:completion:]_block_invoke.44
- __113-[FCCKPrivateDatabaseSchema initWithZoneSchemas:recordSchemas:recordTypeVersionMapping:recordNameVersionMapping:]_block_invoke.17
- __113-[FCCKPrivateDatabaseSchema initWithZoneSchemas:recordSchemas:recordTypeVersionMapping:recordNameVersionMapping:]_block_invoke.22
- __113-[FCCKPrivateDatabaseSchema initWithZoneSchemas:recordSchemas:recordTypeVersionMapping:recordNameVersionMapping:]_block_invoke.26
- __115-[FCUserVector computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:]_block_invoke.30
- __115-[FCUserVector computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:]_block_invoke.32
- __115-[FCUserVector computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:]_block_invoke.34
- __115-[FCUserVector computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:]_block_invoke.37
- __185-[FCEndpointConnection performAuthenticatedHTTPRequestWithURL:valuesByHTTPHeaderField:method:data:contentType:priority:reauthenticateIfNeeded:networkEventType:callbackQueue:completion:]_block_invoke.40
- __194-[FCEndpointConnection performHTTPRequestWithURL:valuesByHTTPHeaderField:method:data:contentType:priority:requiresMescalSigning:requiresAuthKitHeaders:networkEventType:callbackQueue:completion:]_block_invoke.30
- __28-[TCKDatabase addOperation:]_block_invoke.13
- __28-[TCKDatabase addOperation:]_block_invoke.19
- __28-[TCKDatabase addOperation:]_block_invoke.21
- __28-[TCKDatabase addOperation:]_block_invoke.28
- __28-[TCKDatabase addOperation:]_block_invoke.33
- __28-[TCKDatabase addOperation:]_block_invoke.6
- __28-[TCKDatabase addOperation:]_block_invoke.8
- __36-[FCCKPrivateDatabase addOperation:]_block_invoke.125
- __36-[FCNewsletterManager optIntoSports]_block_invoke.53
- __37-[FCNewsletterManager optOutOfIssues]_block_invoke.43
- __37-[FCNewsletterManager optOutOfSports]_block_invoke.56
- __38-[FCAppleAccount getNewGSTokenPromise]_block_invoke.90
- __38-[FCAppleAccount getNewGSTokenPromise]_block_invoke_2.91
- __39-[FCCKPrivateDatabase _continueStartUp]_block_invoke.163
- __39-[FCHCZoneContentsExpectation validate]_block_invoke.376
- __39-[FCHCZoneContentsExpectation validate]_block_invoke.383
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.30
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.32
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.34
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.40
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.46
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.48
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.65
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.66
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke.70
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke_2.33
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke_2.47
- __40-[FCUserVectorManager _fetchUserVector:]_block_invoke_2.49
- __45-[FCNewsletterManager forceSubscriptionThen:]_block_invoke.47
- __46-[FCNewsTabiConfiguration initWithDictionary:]_block_invoke.65
- __48-[FCPersonalizationData _saveReadableAggregates]_block_invoke.92
- __50-[FCAppleAccount getGSTokenWithCompletionHandler:]_block_invoke.81
- __51-[FCNewsTabiAdSegmentsEndpoint initWithDictionary:]_block_invoke.16
- __51-[FCResourceArchiveFetchOperation performOperation]_block_invoke.8
- __51-[FCResourceArchiveFetchOperation performOperation]_block_invoke_2.9
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.10
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.15
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.17
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.24
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.26
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke.6
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2.11
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2.14
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2.25
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2.7
- __51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_3.12
- __55-[FCPersonalizationData _applicationDidEnterBackground]_block_invoke.69
- __55-[FCPersonalizationData _applicationDidEnterBackground]_block_invoke_2.66
- __55-[FCPersonalizationData _applicationDidEnterBackground]_block_invoke_3.67
- __56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke.83
- __56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke_2.87
- __59-[FCCKPrivateDatabaseSchema mappingFromRecordID:toVersion:]_block_invoke.35
- __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.30
- __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.31
- __60-[FCAssetKeyService _performHTTPRequestWithData:completion:]_block_invoke.36
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.186
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.201
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.207
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.211
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.213
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.215
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke.217
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_2.187
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_2.202
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_2.214
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_3.188
- __60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_3.203
- __61-[FCAssetKeyService executeRequest:callbackQueue:completion:]_block_invoke.40
- __61-[FCAssetKeyService executeRequest:callbackQueue:completion:]_block_invoke.41
- __61-[FCAssetKeyService executeRequest:callbackQueue:completion:]_block_invoke_2.43
- __62-[FCCloudContext fetchCleanupToVersionForDatabase:completion:]_block_invoke.225
- __62-[FCCloudContext fetchCleanupToVersionForDatabase:completion:]_block_invoke.227
- __62-[FCCloudContext fetchCleanupToVersionForDatabase:completion:]_block_invoke_2.226
- __64-[FCReadablePrivateDataStorage readPrivateDataSyncWithAccessor:]_block_invoke.13
- __67-[FCCKPrivateDatabase _preflightRecordsInDatabaseChangesOperation:]_block_invoke.222
- __67-[FCPrivateDataEncryptionMigrationHealthCheck _eraseAllPrivateData]_block_invoke.22
- __67-[FCPrivateDataEncryptionMigrationHealthCheck _eraseAllPrivateData]_block_invoke.27
- __68-[FCFileCoordinatedTodayDropboxTransaction todayPrivateDataAccessor]_block_invoke.370
- __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.200
- __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.204
- __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.208
- __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.212
- __69-[FCCKPrivateDatabase _preflightRecordsInRecordZoneChangesOperation:]_block_invoke.216
- __69-[FCTelemetryBasedOfflineNetworkTransitionOperation logNetworkEvent:]_block_invoke.26
- __70-[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]_block_invoke.81
- __70-[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]_block_invoke.91
- __70-[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]_block_invoke_2.93
- __74-[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]_block_invoke.29
- __74-[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]_block_invoke_2.30
- __77-[FCResourceArchiveFetchOperation _ensureResourcesAreReadyForUse:completion:]_block_invoke.42
- __77-[FCResourceArchiveFetchOperation _ensureResourcesAreReadyForUse:completion:]_block_invoke_2.43
- __80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke.12
- __80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke.18
- __80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke.9
- __80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_2.19
- __80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_3.20
- __80-[FCCKDatabaseEncryptionStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.12
- __80-[FCCKDatabaseEncryptionStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke.6
- __80-[FCCKDatabaseEncryptionStartUpMiddleware performStartUpForDatabase:completion:]_block_invoke_2.13
- __80-[FCResourceArchiveFetchOperation _unzipResourcesFromArchiveFileURL:completion:]_block_invoke.33
- __83-[FCPrivateDataEncryptionMigrationHealthCheck _prepareHistoryAndReturnExpectations]_block_invoke.52
- __83-[FCPrivateDataEncryptionMigrationHealthCheck _prepareHistoryAndReturnExpectations]_block_invoke_2.53
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke.11
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke.13
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke.15
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke.6
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_2.12
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_2.14
- __86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_2.16
- __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareReadingListAndReturnExpectations]_block_invoke.94
- __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareReadingListAndReturnExpectations]_block_invoke_2.95
- __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareTagSettingsAndReturnExpectations]_block_invoke.164
- __87-[FCPrivateDataEncryptionMigrationHealthCheck _prepareTagSettingsAndReturnExpectations]_block_invoke_2.165
- __89-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSubscriptionsAndReturnExpectations]_block_invoke.116
- __89-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSubscriptionsAndReturnExpectations]_block_invoke_2.117
- __90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke.18
- __90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke.19
- __90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke.20
- __90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke_2.21
- __98-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSensitiveSubscriptionsAndReturnExpectations]_block_invoke.132
- __98-[FCPrivateDataEncryptionMigrationHealthCheck _prepareSensitiveSubscriptionsAndReturnExpectations]_block_invoke_2.133
- __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.136
- __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.140
- __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.144
- __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke.150
- __99-[FCCKPrivateDatabase enumeratePayloadsWithRecordIDs:records:zoneIDs:zones:options:payloadHandler:]_block_invoke_2.152
- __OBJC_$_CLASS_METHODS_FCCKPrivateDatabaseVersionMapping
- __OBJC_$_INSTANCE_METHODS_FCCKPrivateDatabaseVersionMapping
- __OBJC_$_INSTANCE_METHODS_FCCKRecordIDMapping
- __OBJC_$_INSTANCE_METHODS_FCCKRecordMapping
- __OBJC_$_INSTANCE_METHODS_FCCKRecordTypeMapping
- __OBJC_$_INSTANCE_METHODS_FCCKRecordZoneIDMapping
- __OBJC_$_INSTANCE_METHODS_FCNewsTabiAdSegmentsEndpoint
- __OBJC_$_INSTANCE_METHODS_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __OBJC_$_INSTANCE_VARIABLES_FCCKPrivateDatabaseVersionMapping
- __OBJC_$_INSTANCE_VARIABLES_FCCKRecordIDMapping
- __OBJC_$_INSTANCE_VARIABLES_FCCKRecordMapping
- __OBJC_$_INSTANCE_VARIABLES_FCCKRecordTypeMapping
- __OBJC_$_INSTANCE_VARIABLES_FCCKRecordZoneIDMapping
- __OBJC_$_INSTANCE_VARIABLES_FCNewsTabiAdSegmentsEndpoint
- __OBJC_$_INSTANCE_VARIABLES_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __OBJC_$_PROP_LIST_FCCKPrivateDatabaseVersionMapping
- __OBJC_$_PROP_LIST_FCCKRecordIDMapping
- __OBJC_$_PROP_LIST_FCCKRecordMapping
- __OBJC_$_PROP_LIST_FCCKRecordTypeMapping
- __OBJC_$_PROP_LIST_FCCKRecordZoneIDMapping
- __OBJC_$_PROP_LIST_FCNewsTabiAdSegmentsEndpoint
- __OBJC_$_PROP_LIST_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCUserVectorAggregateVectorProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_FCUserVectorAggregateVectorProvider
- __OBJC_CLASS_PROTOCOLS_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __OBJC_CLASS_RO_$_FCCKPrivateDatabaseVersionMapping
- __OBJC_CLASS_RO_$_FCCKRecordIDMapping
- __OBJC_CLASS_RO_$_FCCKRecordMapping
- __OBJC_CLASS_RO_$_FCCKRecordTypeMapping
- __OBJC_CLASS_RO_$_FCCKRecordZoneIDMapping
- __OBJC_CLASS_RO_$_FCNewsTabiAdSegmentsEndpoint
- __OBJC_CLASS_RO_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __OBJC_LABEL_PROTOCOL_$_FCUserVectorAggregateVectorProvider
- __OBJC_METACLASS_RO_$_FCCKPrivateDatabaseVersionMapping
- __OBJC_METACLASS_RO_$_FCCKRecordIDMapping
- __OBJC_METACLASS_RO_$_FCCKRecordMapping
- __OBJC_METACLASS_RO_$_FCCKRecordTypeMapping
- __OBJC_METACLASS_RO_$_FCCKRecordZoneIDMapping
- __OBJC_METACLASS_RO_$_FCNewsTabiAdSegmentsEndpoint
- __OBJC_METACLASS_RO_$_FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider
- __OBJC_PROTOCOL_$_FCUserVectorAggregateVectorProvider
- ___104-[FCReadonlyPersonalizationAggregateStoreBasedUserVectorAggregateVectorProvider aggregateVectorForTags:]_block_invoke
- ___105-[FCCKDatabaseEncryptionStartUpMiddleware _migrateToVersion:sentinel:secureSentinel:database:completion:]_block_invoke
- ___105-[FCCKDatabaseEncryptionStartUpMiddleware _migrateToVersion:sentinel:secureSentinel:database:completion:]_block_invoke_2
- ___105-[FCCKDatabaseEncryptionStartUpMiddleware _migrateToVersion:sentinel:secureSentinel:database:completion:]_block_invoke_3
- ___113-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataUpToVersion:sentinel:secureSentinel:database:completion:]_block_invoke
- ___113-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataUpToVersion:sentinel:secureSentinel:database:completion:]_block_invoke_2
- ___113-[FCCKDatabaseEncryptionStartUpMiddleware _deleteOldDataUpToVersion:sentinel:secureSentinel:database:completion:]_block_invoke_3
- ___113-[FCCKPrivateDatabaseSchema initWithZoneSchemas:recordSchemas:recordTypeVersionMapping:recordNameVersionMapping:]_block_invoke
- ___115-[FCUserVector computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:]_block_invoke
- ___176-[FCPuzzleHistory _updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:difficulty:publishDate:behaviorFlags:]_block_invoke
- ___24-[FCOperation setFlags:]_block_invoke
- ___35-[TCKDatabase recordIDsInZoneName:]_block_invoke
- ___50+[FCMescalSignature signatureFromData:completion:]_block_invoke
- ___50+[FCMescalSignature signatureFromData:completion:]_block_invoke_2
- ___51-[FCNewsTabiAdSegmentsEndpoint initWithDictionary:]_block_invoke
- ___51-[FCUserVectorManager _submitPersonalizationVector]_block_invoke_2
- ___53-[NSError(FCAdditions) fc_failedDueToTaskConstraints]_block_invoke
- ___54-[FCFileCoordinatedTodayDropbox peekSyncWithAccessor:]_block_invoke
- ___56-[FCCKPrivateDatabaseVersionMapping mapValue:toVersion:]_block_invoke
- ___57-[FCCKPrivateDatabaseVersionMapping allValuesForVersion:]_block_invoke
- ___57-[FCFileCoordinatedTodayDropbox depositSyncWithAccessor:]_block_invoke
- ___59-[FCCKPrivateDatabaseSchema mappingFromRecordID:toVersion:]_block_invoke
- ___60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke
- ___60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_2
- ___60-[FCCloudContext fetchDesiredVersionForDatabase:completion:]_block_invoke_3
- ___61-[FCAssetKeyService executeRequest:callbackQueue:completion:]_block_invoke
- ___61-[FCAssetKeyService executeRequest:callbackQueue:completion:]_block_invoke_2
- ___61-[FCCKPrivateDatabaseSchema schemaForZoneContainingRecordID:]_block_invoke
- ___62-[FCCloudContext fetchCleanupToVersionForDatabase:completion:]_block_invoke
- ___62-[FCCloudContext fetchCleanupToVersionForDatabase:completion:]_block_invoke_2
- ___62-[FCCloudContext fetchCleanupToVersionForDatabase:completion:]_block_invoke_3
- ___64-[FCAssetHandle fetchDataProviderWithPriority:flags:completion:]_block_invoke
- ___64-[FCReadablePrivateDataStorage readPrivateDataSyncWithAccessor:]_block_invoke
- ___64-[FCReadablePrivateDataStorage readPrivateDataSyncWithAccessor:]_block_invoke_2
- ___69-[FCPuzzleHistory updatePuzzle:difficulty:publishDate:behaviorFlags:]_block_invoke
- ___70-[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]_block_invoke
- ___70-[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]_block_invoke_2
- ___71-[FCCKPrivateDatabaseSchema zoneNamesWithChangesFromVersion:toVersion:]_block_invoke
- ___73-[FCPersonalizationTreatment initWithPersonalizationTreatmentDictionary:]_block_invoke
- ___74-[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]_block_invoke
- ___74-[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]_block_invoke_2
- ___74-[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]_block_invoke_3
- ___74-[FCCKPrivateDatabaseVersionMapping mappingByTransformingValuesWithBlock:]_block_invoke_4
- ___76-[FCCKPrivateDatabaseVersionMapping allValuesModifiedFromVersion:toVersion:]_block_invoke
- ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke
- ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_2
- ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_3
- ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_4
- ___82-[FCAppleAccount fetchMinimumDeviceVersionsActiveSinceInterval:completionHandler:]_block_invoke
- ___82-[FCAppleAccount fetchMinimumDeviceVersionsActiveSinceInterval:completionHandler:]_block_invoke_2
- ___82-[FCCKPrivateDatabaseSchema recordNamesInDefaultZoneChangedFromVersion:toVersion:]_block_invoke
- ___83-[FCCKDatabaseEncryptedZoneMigrator databaseMigrationMigrateRecord:database:error:]_block_invoke
- ___84-[FCPrivateDataEncryptionMigrationHealthCheck _prepareUserInfoAndReturnExpectations]_block_invoke_3
- ___84-[FCPrivateDataEncryptionMigrationHealthCheck _prepareUserInfoAndReturnExpectations]_block_invoke_4
- ___86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke
- ___86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_2
- ___86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_3
- ___86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_4
- ___86-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke_5
- ___89-[FCPrivateDataEncryptionMigrationHealthCheck fetchDesiredVersionForDatabase:completion:]_block_invoke
- ___90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke
- ___90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke_2
- ___90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke_3
- ___90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke_4
- ___90-[FCCKDatabaseEncryptionStartUpMiddleware _tryToStartUpDatabase:targetVersion:completion:]_block_invoke_5
- ___block_descriptor_112_e8_32s40bs_e5_v8?0l
- ___block_descriptor_32_e16_16?0"FCPair"8l
- ___block_descriptor_40_e8_32bs_e18_16?0"NSNumber"8l
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_40_e8_32r_e38_v16?0"NSObject<FCTodayPrivateData>"8l
- ___block_descriptor_40_e8_32s_e15_"CKRecord"8?0l
- ___block_descriptor_40_e8_32s_e16_B16?0"FCPair"8l
- ___block_descriptor_40_e8_32s_e33_B24?0"CKRecordID"8"CKRecord"16l
- ___block_descriptor_40_e8_32s_e37_B32?0"CKRecordID"8"CKRecord"16^B24l
- ___block_descriptor_48_e8_32bs40bs_e47_v80?0{?={?=qq}{?=qq}{?=qq}{?=qq}}8"NSError"72l
- ___block_descriptor_48_e8_32bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e18_16?0"NSNumber"8l
- ___block_descriptor_48_e8_32s40s_e16_B16?0"FCPair"8l
- ___block_descriptor_48_e8_32s40s_e24_v16?0"FCCKZoneSchema"8l
- ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSArray"8l
- ___block_descriptor_56_e8_32r40r48r_e18_16?0"NSNumber"8l
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16l
- ___block_descriptor_56_e8_32s_e22_v16?0"NSMutableSet"8l
- ___block_descriptor_56_e8_32s_e8_16?08l
- ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48bs56bs_e43_v32?0"CKRecord"8"CKRecord"16"NSError"24l
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56bs64r_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v24?0q8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56s64bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24l
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_88_e8_32s40s48bs56r64r_e5_v8?0l
- ___block_descriptor_96_e8_32s40s48s56s64bs72r80r_e5_v8?0l
- ___copy_helper_block_e8_32r40r48r
- ___destroy_helper_block_e8_32r40r48r
- __block_literal_global.116
- __block_literal_global.1260
- __block_literal_global.1342
- __block_literal_global.1420
- __block_literal_global.1424
- __block_literal_global.1443
- __block_literal_global.1448
- __block_literal_global.1453
- __block_literal_global.1458
- __block_literal_global.154
- __block_literal_global.169
- __block_literal_global.1769
- __block_literal_global.1813
- __block_literal_global.1883
- __block_literal_global.1908
- __block_literal_global.1933
- __block_literal_global.1958
- __block_literal_global.1980
- __block_literal_global.1999
- __block_literal_global.2144
- __block_literal_global.2175
- __block_literal_global.2281
- __block_literal_global.2297
- __block_literal_global.306
- __block_literal_global.372
- __block_literal_global.498
- __block_literal_global.896
- __block_literal_global.925
- _kFCNewsTabiAdSegmentsEndpointAdSegmentsOutputNameKey
- _kFCNewsTabiAdSegmentsEndpointEventAggregationOutputsKey
- _kFCNewsTabiAdSegmentsEndpointPackageAssetIDKey
- _kFCNewsTabiConfigurationAdSegmentsConfigurationKey
- _objc_msgSend$V2Changes
- _objc_msgSend$V3Changes
- _objc_msgSend$V4Changes
- _objc_msgSend$adSegmentsEndpoint
- _objc_msgSend$adSegmentsOutputName
- _objc_msgSend$aggregateVectorForTags:
- _objc_msgSend$allValuesForVersion:
- _objc_msgSend$allValuesModifiedFromVersion:toVersion:
- _objc_msgSend$baseValues
- _objc_msgSend$computePersonalizationVectorWithAggregateVectorProvider:personalizationTreatment:tagRanker:options:
- _objc_msgSend$computeUserVectorWithTabi
- _objc_msgSend$containsValuePassingTest:
- _objc_msgSend$databaseMigrationRecordNamesToMigrateInZone:fromVersion:toVersion:
- _objc_msgSend$databaseMigrationShouldMigrateEntireZone:
- _objc_msgSend$databaseMigrationZoneNamesFromVersion:toVersion:
- _objc_msgSend$fc_failedDueToTaskConstraints
- _objc_msgSend$fetchCleanupToVersionForDatabase:completion:
- _objc_msgSend$fetchDataProviderWithPriority:flags:completion:
- _objc_msgSend$fetchDesiredVersionForDatabase:completion:
- _objc_msgSend$fetchMinimumDeviceVersionsActiveSinceInterval:completionHandler:
- _objc_msgSend$forwardMapToV2
- _objc_msgSend$forwardMapToV3
- _objc_msgSend$forwardMapToV4
- _objc_msgSend$fromRecordName
- _objc_msgSend$fromRecordSchema
- _objc_msgSend$fromZoneSchema
- _objc_msgSend$hasChanges
- _objc_msgSend$initWithBaseValues:V2Changes:V3Changes:V4Changes:
- _objc_msgSend$initWithEntryID:puzzleID:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:firstCompletedDate:firstPlayDuration:bestScore:difficulty:publishDate:behaviorFlags:
- _objc_msgSend$initWithFromZoneSchema:toZoneSchema:
- _objc_msgSend$initWithFromZoneSchema:toZoneSchema:fromRecordName:toRecordName:
- _objc_msgSend$initWithFromZoneSchema:toZoneSchema:fromRecordSchema:toRecordSchema:
- _objc_msgSend$initWithFromZoneSchema:toZoneSchema:fromRecordSchema:toRecordSchema:recordIDMapping:
- _objc_msgSend$initWithReadonlyPersonalizationAggregateStore:personalizationTreatment:
- _objc_msgSend$mapValue:toVersion:
- _objc_msgSend$mappingByTransformingValuesWithBlock:
- _objc_msgSend$mappingWithBaseValues:V2Changes:V3Changes:V4Changes:
- _objc_msgSend$peekSyncWithAccessor:
- _objc_msgSend$privateDataShouldCleanupAfterSecureSubscriptions
- _objc_msgSend$privateDataShouldCleanupToV4
- _objc_msgSend$privateDataShouldMigrateToV4
- _objc_msgSend$recordIDMapping
- _objc_msgSend$reverseMap
- _objc_msgSend$setAllowsConstrainedNetworkAccess:
- _objc_msgSend$setAllowsExpensiveNetworkAccess:
- _objc_msgSend$setTabiBasedAggregateVectorProvider:
- _objc_msgSend$signatureFromData:completion:
- _objc_msgSend$signaturePromiseFromData:type:bag:
- _objc_msgSend$tabiBasedAggregateVectorProvider
- _objc_msgSend$toRecordID
- _objc_msgSend$toRecordName
- _objc_msgSend$toRecordSchema
- _objc_msgSend$toVersion
- _objc_msgSend$toZoneSchema
CStrings:
+ "%!@(MISSING).%!@(MISSING).%!@(MISSING)"
+ "+[FCCKZoneSchema zoneWithClientName:serverName:records:staticRecordNames:shouldEncryptRecordNames:shouldUseZoneWidePCS:shouldUseSecureContainer:]"
+ "-[FCAVAssetKeyService _performHTTPRequest:keyURI:completion:]_block_invoke"
+ "-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke"
+ "-[FCCKDatabaseEncryptedZoneMigrator _isEnabledForDatabase:]"
+ "-[FCCKDatabaseEncryptionStartUpMiddleware _migrateWithSentinel:secureSentinel:database:completion:]_block_invoke"
+ "-[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationMigrateRecord:database:error:]"
+ "-[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationRecordNamesToMigrateInZone:database:]"
+ "-[FCCKDatabaseSubscriptionsStartUpMiddleware databaseMigrationZoneNamesForDatabase:]"
+ "-[FCCKPrivateDatabaseSchema schemaForZoneContainingClientRecordID:]"
+ "-[FCCKPrivateDatabaseSchema schemaForZoneContainingServerRecordID:]"
+ "-[FCCKPrivateDatabaseSchema schemaForZoneWithClientName:]"
+ "-[FCCKPrivateDatabaseSchema schemaForZoneWithServerName:]"
+ "-[FCCKZoneSchema initWithClientZoneName:serverZoneName:recordSchemas:staticRecordNames:staticRecordNameMigrationBlacklist:shouldEncryptRecordNames:shouldUseZoneWidePCS:shouldUseSecureContainer:]"
+ "-[FCPuzzleHistory _updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:]"
+ "-[FCPuzzleHistoryItem initWithEntryID:puzzleID:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:firstCompletedDate:firstPlayDuration:bestScore:]"
+ "-[FCReadablePrivateDataStorage readPrivateDataWithAccessor:]"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCANEFFileDataProvider.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCANEFHeader.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAsset.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetCache.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetDownloadManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetFactory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetKeyManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetKeyService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetResourceLoader.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAccountActionQueue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAnalyticsEndpointConnection.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAppleAccount.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArrayStream.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticle.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleAudioTrack.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleClassification.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleContent.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleDownloadService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleDraftAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleHeadline.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleHeadlineUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleHeadlinesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleRecordSource.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleStreamingResults.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssertPreparedFeedPersonalizer.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetDownloadOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetHandle.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetKeyCache.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetStore.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetTransformer.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetURLUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAsyncBlockOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAsyncSerialQueue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAudioConfigurationOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAudioFeedConfigOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAudioUpsellConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBalancedCounter.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBiomeSignalProvider.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBlockUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBlockedExplicitContentAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBundleSubscriptionLookUpEntry.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBundleSubscriptionLookUpEntryManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBundleSubscriptionManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKBatchedMultiFetchQueryOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentBatchedFetchRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentBatchedRefreshRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentDatabase.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentQueryOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseEncryptedZoneMigrator.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseEncryptionMiddleware.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseEncryptionStartUpMiddleware.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseLoggingMiddleware.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseMigrationOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseSubscriptionsStartUpMiddleware.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseUserAuthenticationMiddleware.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseZoneMigrationOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDirectRequestOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKMultiFeedQueryOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKMultiFetchQueryOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKOrderFeedQueryOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKOrderFeedUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPredicateConversion.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateBatchedDeleteRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateBatchedSaveRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabase+Additions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabase.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseSchema.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseServerChangeToken.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDeleteRecordZonesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDeleteRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateFetchRecordZoneChangesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateFetchRecordZonesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateFetchRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateSaveDatabaseSubscriptionOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateSaveRecordZonesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateSaveRecordsOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKProtocolTranslator.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordFieldConversion.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordZone.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordZoneManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKSecureDatabaseResetOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKTagSearchQueryOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCacheCoordinator.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCast.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCChannelIssuesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCChannelMembershipController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCChannelSectionHeadlinesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCheckArticleStatusOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCheckDraftContentAccessOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCloudContext.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCColor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCColorGradient.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCommand.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCommandQueue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCContentArchive.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCContentContext.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCContextConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCoreConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentAudioContentFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentIssuesChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentIssuesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentMagazineContentFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCDateRange.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCDerivedPersonalizationData.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCDraftIssuesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCEditorialOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCEndpointConnection.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCExcerptURLProtocol.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFDBConnection.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFDBStorage.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFDBUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFaultableRecord.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeaturedArticlesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedBins.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedBuildingUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedCursor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedDatabase.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedGroupType.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItem.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemHeadlinesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemInventory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemServiceCursor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedPrewarmOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedRange.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedRequestOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationComposite.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationPersonalize.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationSort.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnconsumedOnly.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnreadFirst.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnreadOnly.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnseenOnly.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeldsparIDProvider.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedAppConfigurationManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedDictionary.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedDictionaryUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedNotificationDropbox.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedTodayDropbox.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedTodayPersonalizationUpdate.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedTodayPrivateDataTransactionQueue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileURLs.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFlintResourceManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCForYouConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCForYouConfigHeadlinesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCForYouQueryUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCGlobalCuratedESLArticlesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCGlobalESLService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadline.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlineClusterOrdering.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlineClusteringRules.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlineTemplate.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlinesUpdateOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeldRecords.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCInterestToken.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIntroductoryOffer.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueArticlesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueBookmark.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueDownloadService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueDraftAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueHeadlinesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueOverrides.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueReadingHistory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssuesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCJSONRecordSource.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCJSONUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCKeyValueStore.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCKeyValueStoreSavePolicy.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCKeyedOperationQueue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLegacyFeedPersonalizer.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalArea.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalAreasMapping.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalRegion.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalVersionedTag.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMagazineGenre.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMath.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyIssueHistoryCommand.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyPersonalizationOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyRecordsCommand.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyUserEventHistoryCommand.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiResolutionImage.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiSizeVideo.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiSourceHeadlinesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiStepFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMyArticlesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMyArticlesSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkBehaviorMonitor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkEvent.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkReachability.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsAppConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsAvailabilityMonitor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsIDUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsPersonalizationTrainingBias.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsTabiConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsVersionAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNonDestructivePrivateDataMigrationHandler.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNotificationArticleHeadline.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNotificationController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNotificationsEndpointConnection.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCObservable.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineANFArticlesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineArticleFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineAudioFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineIssueFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineIssueList.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflinePuzzleFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOnce.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOngoingPurchaseEntry.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOperationThrottler.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOrderedCollection.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaidALaCartePaywallConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaidBundleConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCParsecArticleSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaymentTransactionManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaywallConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaywallTopOffsetConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaywallVisualSpecConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationAggregate.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationBundleIDMapping.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationCohortConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationData.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationFeature.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationFunctionProvider.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationLowFlowEstimationConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationMappingUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationOntologyLevelConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationPublisherDampeningConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationScoringConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationTagScoringConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationTopicConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationTopicsConfig.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationURLMapping.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationWhitelist.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPostPurchaseOnboardingConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateChannelMembershipController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateDataContext.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateDataController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateRecordSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateZoneFeedDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateZoneSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseLookUpEntry.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseLookupFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseMetadataFetcher.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseProvider.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPushNotificationCenter.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzle.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleDownloadService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleHistory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleHistoryItem.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleRank.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleThumbnailURLProtocol.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleType.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeSettings.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeSettingsEntry.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRawFileDataProvider.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadablePrivateDataStorage.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingHistory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingHistoryUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingList.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingListEntry.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRecordChainFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRecordFieldURLProtocol.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRecordSource.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReferenceToMembership.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRemoteDefaults.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRemoveRecordsCommand.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCResource.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCResourceArchiveFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCResourcesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRestrictions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCShortcut.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCShortcutCategoryList.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCShortcutList.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSingleTagFeedDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSportsEventController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSportsEventsFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSportsPrivacyConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCStorefrontAccessChecker.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCStreamingResults.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscription.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscriptionButtonConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscriptionController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscriptionList.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTag.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagController.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagCuratedESLArticlesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagESLService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagFeedHeadlinesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagFeedPromotedHeadlinesFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagFilterUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagMetadata.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagRecordSource.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSettings.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSettingsEntry.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSubscriptionOrderAssigner.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSubscriptionSorter.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagsFetchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCThreadSafeCollections.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTodayFeedConfigOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTodayMarkAsReadTransaction.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTopKESLService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTopicTranslation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTransformedResultsStream.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTransformedStream.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTranslationMap.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUUIDUtilities.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserEventHistory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserEventHistorySession.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserEventHistoryStorage.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserFacingTagSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserInfo.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserVector.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserVectorManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCWebContent.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCWebURLResolutionEndpointConnection.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCWritablePrivateDataStorage.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCCoreConfigurationFetchedValueDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCFetchedValueDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCFetchedValueManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCFetchedValueObservable.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCHeldPBCodableFetchedValueDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCManagedResourceConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSArray+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSData+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDate+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDateFormatter+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDictionary+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDictionary+FCTodayPrivateDataTransactionQueue.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSEnumerator+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSMutableArray+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSOrderedSet+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSSet+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSString+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSURL+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBFeedConfiguration+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBIssueReadingHistoryItem+FCIssueReadingHistory.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBPersonalizationAggregateDelta+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBTagRecord+FCAdditions.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCAppActivationMonitor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCOfflineModeMonitor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCTelemetryBasedOfflineNetworkTransitionMonitor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCTelemetryBasedOfflineNetworkTransitionOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/People Also Read/FCPeopleAlsoReadArticlesOperation.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/People Also Read/FCPeopleAlsoReadFeedItemService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/People Also Read/FCPeopleAlsoReadInventoryManager.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Vanity URLs/FCVanityURLConfigurationFetchedValueDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Vanity URLs/FCVanityURLMapper.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Vanity URLs/FCVanityURLRedirectService.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Tests/FCCKTestContentDatabase.m"
+ "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Tests/FCMockFetchedValueDescriptor.m"
+ "5"
+ "Client record type is missing from the zone schema: %!@(MISSING), %!@(MISSING)"
+ "Client zone is missing from the schema: %!@(MISSING)"
+ "Client zone is missing from the schema: %!@(MISSING), %!@(MISSING)"
+ "Client zone schema failed to provide a server record name for: %!@(MISSING)"
+ "Failed to decrypt subscription during migration with record=%!@(MISSING), error=%!@(MISSING)"
+ "Failed to encrypt subscription during migration with record=%!@(MISSING), error=%!@(MISSING)"
+ "Secure"
+ "Server record type is missing from the zone schema: %!@(MISSING), %!@(MISSING)"
+ "Server zone is missing from the schema: %!@(MISSING)"
+ "Server zone is missing from the schema: %!@(MISSING), %!@(MISSING)"
+ "Server zone schema failed to provide a client record name for: %!@(MISSING)"
+ "_CK"
+ "all"
+ "allows"
+ "delete_after_encryption_migration"
+ "disable_encryption_migration"
+ "does not allow"
+ "encryption_behavior"
+ "encryption_required_behavior"
+ "error saving puzzle history item record: %!@(MISSING)"
+ "error saving puzzle history zone: %!@(MISSING)"
+ "error saving puzzle type settings record: %!@(MISSING)"
+ "error saving shortcut category record: %!@(MISSING)"
+ "error saving shortcut category zone: %!@(MISSING)"
+ "error saving shortcut record: %!@(MISSING)"
+ "error saving shortcut zone: %!@(MISSING)"
+ "force_encryption_migration_on_every_launch"
+ "history record schema has wrong record type"
+ "history record should have encrypted article ID"
+ "history zone schema has wrong zone name"
+ "issue history record schema has wrong record type"
+ "issue history record should have encrypted issue ID"
+ "issue history record should have encrypted last-visited article ID"
+ "issue history record should have encrypted last-visited page ID"
+ "issue history zone schema has wrong zone name"
+ "migrator must not be given a nil database"
+ "not all"
+ "operation produced unexpected zone IDs to delete; expected %!@(MISSING), got %!@(MISSING)"
+ "persoanlization profile record schema has wrong record type"
+ "personalization profile record should have encrypted data"
+ "puzzle history item record schema has wrong record type"
+ "puzzle history item record should have encrypted puzzleID"
+ "puzzle history zone schema has wrong zone name"
+ "puzzle type settings record schema has wrong record type"
+ "puzzle type settings record should have encrypted puzzleTypeID"
+ "rank-tiles-0"
+ "reading list record should have encrypted article ID"
+ "reference-to-membership schema has wrong zone name"
+ "sensitive subscriptions record should have encrypted tag ID"
+ "shortcut categories zone schema has wrong zone name"
+ "shortcut category record schema has wrong record type"
+ "shortcut record schema has wrong record type"
+ "shortcut zone schema has wrong zone name"
+ "shortcut-category-id"
+ "subscriptions record should have encrypted tag ID"
+ "to get the schema for the default zone, use schemaForZoneWithClientName:recordID:"
+ "to get the schema for the default zone, use schemaForZoneWithServerName:recordID:"
+ "user info record should have encrypted feldspar ID"
+ "v1"
+ "widgetTelemetrySamplingRate"
+ "{puzzleID=%!@(MISSING), puzzleTypeID=%!@(MISSING), progressData=%!@(MISSING), progressLevel=%!@(MISSING), score=%!@(MISSING), rankID=%!@(MISSING), usedReveal=%!@(MISSING) playDuration=%!@(MISSING), lastPlayedDate=%!@(MISSING), completedDate=%!@(MISSING) firstCompletedDate=%!@(MISSING) firstPlayDuration=%!@(MISSING) bestScore=%!@(MISSING)}"
- "\n\tadSegmentsEndpoint: %!@(MISSING);"
- "\n\tadSegmentsOutputName: %!@(MISSING);"
- "%!l(MISSING)d.%!l(MISSING)d"
- "+[FCCKZoneSchema zoneWithName:]"
- "+[FCCKZoneSchema zoneWithName:options:staticRecordNames:]"
- "-[FCAVAssetKeyService executeRequest:keyURI:callbackQueue:completion:]_block_invoke"
- "-[FCAppleAccount fetchMinimumDeviceVersionsActiveSinceInterval:completionHandler:]_block_invoke"
- "-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke"
- "-[FCCKDatabaseEncryptionMiddleware _encryptRecord:withEncryptionKey:mapping:error:]"
- "-[FCCKPrivateDatabaseSchema initWithZoneSchemas:recordSchemas:recordTypeVersionMapping:recordNameVersionMapping:]"
- "-[FCCKPrivateDatabaseSchema schemaForZoneContainingRecordID:]"
- "-[FCCKPrivateDatabaseSchema schemaForZoneWithName:]"
- "-[FCCKPrivateDatabaseVersionMapping initWithBaseValues:V2Changes:V3Changes:V4Changes:]_block_invoke"
- "-[FCCKZoneSchema initWithZoneName:options:staticRecordNames:]"
- "-[FCFileCoordinatedTodayDropbox depositSyncWithAccessor:]"
- "-[FCFileCoordinatedTodayDropbox peekSyncWithAccessor:]"
- "-[FCNewsTabiAdSegmentsEndpoint init]"
- "-[FCPersonalizationData localStoreMigrator]_block_invoke"
- "-[FCPuzzleHistory _updatePuzzle:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:difficulty:publishDate:behaviorFlags:]"
- "-[FCPuzzleHistory updatePuzzle:difficulty:publishDate:behaviorFlags:]"
- "-[FCPuzzleHistoryItem initWithEntryID:puzzleID:puzzleTypeID:progressData:progressLevel:score:rankID:usedReveal:playDuration:lastPlayedDate:completedDate:firstCompletedDate:firstPlayDuration:bestScore:difficulty:publishDate:behaviorFlags:]"
- "-[FCReadablePrivateDataStorage readPrivateDataSyncWithAccessor:]"
- "-[TCKDatabase addOperation:]"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCANEFFileDataProvider.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCANEFHeader.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAsset.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetCache.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetDownloadManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetFactory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetKeyManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetKeyService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAVAssetResourceLoader.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAccountActionQueue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAnalyticsEndpointConnection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAppleAccount.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArrayStream.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticle.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleAudioTrack.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleClassification.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleContent.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleDownloadService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleDraftAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleHeadline.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleHeadlineUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleHeadlinesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleRecordSource.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCArticleStreamingResults.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssertPreparedFeedPersonalizer.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetDownloadOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetHandle.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetKeyCache.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetStore.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetTransformer.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAssetURLUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAsyncBlockOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAsyncSerialQueue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAudioConfigurationOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAudioFeedConfigOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCAudioUpsellConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBalancedCounter.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBiomeSignalProvider.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBlockUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBlockedExplicitContentAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBundleSubscriptionLookUpEntry.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBundleSubscriptionLookUpEntryManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCBundleSubscriptionManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKBatchedMultiFetchQueryOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentBatchedFetchRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentBatchedRefreshRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentDatabase.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKContentQueryOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseEncryptionMiddleware.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseEncryptionStartUpMiddleware.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseLoggingMiddleware.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseMigrationOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseUserAuthenticationMiddleware.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDatabaseZoneMigrationOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKDirectRequestOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKMultiFeedQueryOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKMultiFetchQueryOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKOrderFeedQueryOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKOrderFeedUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPredicateConversion.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateBatchedDeleteRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateBatchedSaveRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabase+Additions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabase.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseSchema.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseServerChangeToken.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDatabaseVersionMapping.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDeleteRecordZonesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateDeleteRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateFetchRecordZoneChangesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateFetchRecordZonesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateFetchRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateSaveDatabaseSubscriptionOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateSaveRecordZonesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKPrivateSaveRecordsOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKProtocolTranslator.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordFieldConversion.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordSchema.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordZone.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKRecordZoneManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKSecureDatabaseResetOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKTagSearchQueryOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCKZoneSchema.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCacheCoordinator.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCast.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCChannelIssuesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCChannelMembershipController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCChannelSectionHeadlinesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCheckArticleStatusOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCheckDraftContentAccessOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCloudContext.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCColor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCColorGradient.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCommand.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCommandQueue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCContentArchive.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCContentContext.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCContextConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCoreConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentAudioContentFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentIssuesChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentIssuesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCCurrentMagazineContentFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCDateRange.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCDerivedPersonalizationData.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCDraftIssuesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCEditorialOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCEndpointConnection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCExcerptURLProtocol.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFDBConnection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFDBStorage.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFDBUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFaultableRecord.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeaturedArticlesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedBins.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedBuildingUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedCursor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedDatabase.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedGroupType.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItem.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemHeadlinesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemInventory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedItemServiceCursor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedPrewarmOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedRange.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedRequestOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationComposite.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationPersonalize.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationSort.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnconsumedOnly.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnreadFirst.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnreadOnly.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeedTransformationUnseenOnly.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFeldsparIDProvider.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedAppConfigurationManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedDictionary.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedDictionaryUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedNotificationDropbox.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedTodayDropbox.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedTodayPersonalizationUpdate.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileCoordinatedTodayPrivateDataTransactionQueue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFileURLs.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCFlintResourceManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCForYouConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCForYouConfigHeadlinesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCForYouQueryUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCGlobalCuratedESLArticlesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCGlobalESLService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadline.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlineClusterOrdering.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlineClusteringRules.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlineTemplate.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeadlinesUpdateOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCHeldRecords.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCInterestToken.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIntroductoryOffer.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueArticlesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueBookmark.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueDownloadService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueDraftAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueHeadlinesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueOverrides.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssueReadingHistory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCIssuesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCJSONRecordSource.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCJSONUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCKeyValueStore.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCKeyValueStoreSavePolicy.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCKeyedOperationQueue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLegacyFeedPersonalizer.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalArea.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalAreasMapping.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalRegion.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCLocalVersionedTag.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMagazineGenre.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMath.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyIssueHistoryCommand.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyPersonalizationOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyRecordsCommand.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCModifyUserEventHistoryCommand.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiResolutionImage.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiSizeVideo.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiSourceHeadlinesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMultiStepFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMyArticlesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCMyArticlesSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkBehaviorMonitor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkEvent.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNetworkReachability.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsAppConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsAvailabilityMonitor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsIDUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsPersonalizationTrainingBias.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsTabiAdSegmentsConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsTabiConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNewsVersionAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNonDestructivePrivateDataMigrationHandler.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNotificationArticleHeadline.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNotificationController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCNotificationsEndpointConnection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCObservable.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineANFArticlesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineArticleFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineAudioFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineIssueFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflineIssueList.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOfflinePuzzleFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOnce.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOngoingPurchaseEntry.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOperationThrottler.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCOrderedCollection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaidALaCartePaywallConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaidBundleConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCParsecArticleSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaymentTransactionManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaywallConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaywallTopOffsetConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPaywallVisualSpecConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationAggregate.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationBundleIDMapping.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationCohortConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationData.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationFeature.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationFunctionProvider.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationLowFlowEstimationConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationMappingUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationOntologyLevelConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationPublisherDampeningConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationScoringConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationTagScoringConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationTopicConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationTopicsConfig.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationURLMapping.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPersonalizationWhitelist.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPostPurchaseOnboardingConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateChannelMembershipController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateDataContext.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateDataController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateRecordSyncManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateZoneFeedDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPrivateZoneSyncManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseLookUpEntry.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseLookupFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseMetadataFetcher.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPurchaseProvider.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPushNotificationCenter.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzle.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleDownloadService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleHistory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleHistoryItem.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleRank.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleThumbnailURLProtocol.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleType.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeSettings.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCPuzzleTypeSettingsEntry.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRawFileDataProvider.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadablePrivateDataStorage.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingHistory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingHistoryUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingList.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReadingListEntry.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRecordChainFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRecordFieldURLProtocol.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRecordSource.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCReferenceToMembership.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRemoteDefaults.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRemoveRecordsCommand.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCResource.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCResourceArchiveFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCResourcesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCRestrictions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCShortcut.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCShortcutCategoryList.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCShortcutList.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSingleTagFeedDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSportsEventController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSportsEventsFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSportsPrivacyConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCStorefrontAccessChecker.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCStreamingResults.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscription.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscriptionButtonConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscriptionController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCSubscriptionList.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTag.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagController.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagCuratedESLArticlesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagESLService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagFeedHeadlinesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagFeedPromotedHeadlinesFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagFilterUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagMetadata.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagRecordSource.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSettings.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSettingsEntry.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSubscriptionOrderAssigner.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagSubscriptionSorter.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTagsFetchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCThreadSafeCollections.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTodayFeedConfigOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTodayMarkAsReadTransaction.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTopKESLService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTopicTranslation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTransformedResultsStream.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTransformedStream.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCTranslationMap.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUUIDUtilities.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserEventHistory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserEventHistorySession.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserEventHistoryStorage.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserFacingTagSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserInfo.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserVector.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCUserVectorManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCWebContent.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCWebURLResolutionEndpointConnection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/FCWritablePrivateDataStorage.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCCoreConfigurationFetchedValueDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCFetchedValueDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCFetchedValueManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCFetchedValueObservable.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCHeldPBCodableFetchedValueDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Fetched Value Management/FCManagedResourceConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSArray+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSData+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDate+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDateFormatter+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDictionary+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSDictionary+FCTodayPrivateDataTransactionQueue.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSEnumerator+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSMutableArray+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSOrderedSet+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSSet+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSString+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NSURL+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBFeedConfiguration+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBIssueReadingHistoryItem+FCIssueReadingHistory.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBPersonalizationAggregateDelta+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/NTPBTagRecord+FCAdditions.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCAppActivationMonitor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCOfflineModeMonitor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCTelemetryBasedOfflineNetworkTransitionMonitor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/OfflineDetection/FCTelemetryBasedOfflineNetworkTransitionOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/People Also Read/FCPeopleAlsoReadArticlesOperation.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/People Also Read/FCPeopleAlsoReadFeedItemService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/People Also Read/FCPeopleAlsoReadInventoryManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Vanity URLs/FCVanityURLConfigurationFetchedValueDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Vanity URLs/FCVanityURLMapper.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Classes/Vanity URLs/FCVanityURLRedirectService.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Tests/FCCKTestContentDatabase.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Tests/FCMockFetchedValueDescriptor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldsparcore/Tests/TCKDatabase.m"
- "<none>"
- "@\"CKRecord\"8@?0"
- "AudioPlaylistItemSecure"
- "AudioPlaylistItemSecure2"
- "AudioPlaylistSecure"
- "AudioPlaylistSecure2"
- "B24@?0@\"CKRecordID\"8@\"CKRecord\"16"
- "B32@?0@\"CKRecordID\"8@\"CKRecord\"16^B24"
- "Base"
- "CKQueryOperation is not supported"
- "IssueReadingHistoryItemSecure"
- "IssueReadingHistoryItemSecure2"
- "IssueReadingHistorySecure"
- "IssueReadingHistorySecure2"
- "PersonalizationProfileSecure"
- "PuzzleHistoryItemSecure"
- "PuzzleHistoryItemSecure2"
- "PuzzleHistorySecure"
- "PuzzleHistorySecure2"
- "PuzzleTypeSettingsSecure"
- "ReadingHistoryItemSecure"
- "ReadingHistoryItemSecure2"
- "ReadingHistorySecure"
- "ReadingHistorySecure2"
- "ReadingListEntrySecure"
- "ReadingListEntrySecure2"
- "ReadingListSecure"
- "ReadingListSecure2"
- "Record name is invalid: %!@(MISSING)"
- "SensitiveSubscriptionsSecure"
- "SensitiveSubscriptionsSecure2"
- "ShortcutSecure"
- "ShortcutSecure2"
- "ShortcutsSecure"
- "ShortcutsSecure2"
- "SubscriptionSecure"
- "SubscriptionSecure2"
- "Subscription_CK"
- "Subscriptions_CK"
- "TagSettingsSecure"
- "TagSettingsSecure2"
- "UserEventHistorySecure"
- "UserEventHistorySessionSecure"
- "UserInfoSecure"
- "UserInfoSecure2"
- "V2"
- "V3"
- "V4"
- "adSegmentsConfiguration"
- "adSegmentsOutputName"
- "computeUserVectorWithTabi"
- "deletedToVersion"
- "enableTabiAdSegments"
- "encryption_cleanup_to_version_override"
- "encryption_desired_version_override"
- "iOS=%!@(MISSING), macOS=%!@(MISSING), watchOS=%!@(MISSING), visionOS=%!@(MISSING)"
- "issue reading history record schema has wrong record type"
- "issue reading history record should have encrypted issueID"
- "issue reading history zone schema has wrong zone name"
- "liveActivityScheduleDelay"
- "liveActivityScheduleRandomInitialDelay"
- "liveActivityScheduleTimeWindow"
- "liveActivityScheduledAlertsThreshold"
- "migratedToVersion"
- "missing record type in schema: %!@(MISSING)"
- "missing record type in version mapping: %!@(MISSING)"
- "missing static record in name mapping: %!@(MISSING):%!@(MISSING)"
- "missing zone name in schema: %!@(MISSING)"
- "missing zone name in version mapping: %!@(MISSING)"
- "news.features.enableTabiBasedUserVector"
- "personalization record schema has wrong record type"
- "personalization record should have encrypted data"
- "privateDataCleanupToV4Level"
- "privateDataMigrateToV4Level"
- "privateDataSecureSubscriptionsCleanupLevel"
- "reading history record schema has wrong record type"
- "reading history record should have encrypted articleID"
- "reading history zone schema has wrong zone name"
- "reading list record should have encrypted articleID"
- "reference-to-membership zone schema has wrong zone name"
- "self.accessQueue"
- "sensitive subscriptions record should have encrypted tagID"
- "subscriptions record should have encrypted tagID"
- "tag settings zone schema has wrong zone name"
- "to get the schema for the default zone, use schemaForZoneContainingRecordID:"
- "user info record should have encrypted feldsparID"
- "user_info_static_record_name_secure2"
- "v24@?0q8@\"NSError\"16"
- "v80@?0{?={?=qq}{?=qq}{?=qq}{?=qq}}8@\"NSError\"72"
- "versioned changes should be keyed by base value"
- "visionOS"
- "watchOS"
- "widgetTelemetrySamplingRate2"
- "{puzzleID=%!@(MISSING), puzzleTypeID=%!@(MISSING), progressData=%!@(MISSING), progressLevel=%!@(MISSING), score=%!@(MISSING), rankID=%!@(MISSING), usedReveal=%!@(MISSING), playDuration=%!@(MISSING), lastPlayedDate=%!@(MISSING), completedDate=%!@(MISSING), firstCompletedDate=%!@(MISSING), firstPlayDuration=%!@(MISSING), bestScore=%!@(MISSING), difficulty=%!@(MISSING), publishDate=%!@(MISSING), behaviorFlags=%!@(MISSING)}"

```
