## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/CloudPhotoLibrary`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x1a95fc
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x11a40
-  __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0x40a0
-  __TEXT.__oslogstring: 0x13c7a
-  __TEXT.__cstring: 0x144d7
-  __TEXT.__unwind_info: 0x5a68
-  __TEXT.__objc_classname: 0x1d56
-  __TEXT.__objc_methname: 0x2960a
-  __TEXT.__objc_methtype: 0x448c
-  __TEXT.__objc_stubs: 0x19120
-  __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0xd78
+751.0.104.0.0
+  __TEXT.__text: 0x1ad044
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_methlist: 0x12b5c
+  __TEXT.__const: 0x2e8
+  __TEXT.__gcc_except_tab: 0x41e8
+  __TEXT.__oslogstring: 0x13fce
+  __TEXT.__cstring: 0x14817
+  __TEXT.__unwind_info: 0x5b30
+  __TEXT.__objc_classname: 0x1d5b
+  __TEXT.__objc_methname: 0x29d21
+  __TEXT.__objc_methtype: 0x44bc
+  __TEXT.__objc_stubs: 0x19680
+  __DATA_CONST.__got: 0xa10
+  __DATA_CONST.__const: 0xdf0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8108
+  __DATA_CONST.__objc_selrefs: 0x8308
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x7f0
-  __DATA_CONST.__objc_arraydata: 0x12b0
-  __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x7f40
-  __AUTH_CONST.__cfstring: 0x14080
-  __AUTH_CONST.__objc_const: 0x1ed90
+  __DATA_CONST.__objc_superrefs: 0x7f8
+  __DATA_CONST.__objc_arraydata: 0x12d0
+  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__const: 0x80d0
+  __AUTH_CONST.__cfstring: 0x14620
+  __AUTH_CONST.__objc_const: 0x1d558
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH.__objc_data: 0x5230
-  __DATA.__objc_ivar: 0x1704
+  __DATA.__objc_ivar: 0x1734
   __DATA.__data: 0xed0
-  __DATA.__bss: 0xd30
+  __DATA.__bss: 0xd50
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/MMCS.framework/Versions/A/MMCS
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
+  - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E34F552-80A1-3475-BAA0-F5E7B39418A6
-  Functions: 8171
-  Symbols:   16966
-  CStrings:  14202
+  UUID: 3F241692-4846-3D2E-82C5-9A2F1E5D0E2E
+  Functions: 8380
+  Symbols:   17313
+  CStrings:  14376
 
Symbols:
+ +[CPLCallObserver observeAsyncCallWithFunction:block:]
+ +[CPLCallObserver observeSyncCallWithFunction:block:]
+ +[CPLFingerprintContext defaultAccountEPPCapabilityInUniverseName:]
+ +[CPLFingerprintContext initialize]
+ +[CPLFingerprintContext setupFingerprintContextForTests]
+ +[CPLFingerprintScheme initialize]
+ +[CPLFingerprintScheme isStableHash:]
+ +[CPLFingerprintScheme supportsEPPAutoEnable]
+ +[CPLRecordChange descriptionForSupportedFeatureCompatibleVersion:]
+ +[CPLRecordChange supportedFeatureCompatibleVersion]
+ +[CPLStatus descriptionForAccountEPPCapability:]
+ -[CPLAlbumChange setUserModificationDate:]
+ -[CPLAlbumChange userModificationDate]
+ -[CPLAssetChange isEPPRecord]
+ -[CPLBeforeUploadCheckItem fingerprintContext]
+ -[CPLBeforeUploadCheckItems fingerprintContext]
+ -[CPLBeforeUploadCheckItems initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:fingerprintContext:provider:]
+ -[CPLCallObserver _callDescription]
+ -[CPLCallObserver initWithObject:selector:functionName:]
+ -[CPLConfiguration(CPLSyncSessionConfiguration) shouldCheckEPPCapability]
+ -[CPLConfiguration(CPLSyncSessionConfiguration) shouldDisableEPP]
+ -[CPLEngineForceSyncTask shouldCheckEPPCapability]
+ -[CPLEngineLibrary _beginChangeSessionWithSessionToken:completionHandler:]
+ -[CPLEngineLibrary _requestUpdateOfMainScopeFromTransport]
+ -[CPLEngineLibrary beginChangeSessionWithSessionToken:completionHandler:]
+ -[CPLEngineLibrary endChangeSessionWithSessionToken:]
+ -[CPLEngineLibrary setAccountEPPCapability:]
+ -[CPLEngineQuarantinedRecords _addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:]
+ -[CPLEngineQuarantinedRecords performMaintenanceWithError:]
+ -[CPLEngineScopeStorage _doesScopeContributeToGlobalStatus:]
+ -[CPLEngineScopeStorage _fixGlobalStatus]
+ -[CPLEngineScopeStorage _updateGlobalStatusWithScopeChange:forScope:]
+ -[CPLEngineScopeStorage performMaintenanceWithError:]
+ -[CPLEngineScopeStorage performUpgradeWithError:]
+ -[CPLEngineScopeStorage setHasUpdatedScope:fromTransportWithError:]
+ -[CPLEngineStorage performUpgradeWithError:]
+ -[CPLFingerprintContext _sourceDescriptionForSource:]
+ -[CPLFingerprintContext _usesMMCSv2AsDefault]
+ -[CPLFingerprintContext initWithBoundaryKey:]
+ -[CPLFingerprintContext initWithFingerprintSchemeV1:fingerprintSchemeV2:]
+ -[CPLFingerprintContext refreshBoundaryKeyWithSource:completionHandler:]
+ -[CPLFingerprintContext setBoundaryKey:]
+ -[CPLFingerprintContext updateWithAccountEPPCapability:source:]
+ -[CPLFingerprintContext updateWithStatus:configuration:]
+ -[CPLFingerprintScheme isCompatibleWithFingerprintScheme:]
+ -[CPLFingerprintScheme isValidFingerprint:]
+ -[CPLFingerprintScheme providesEnhancedPrivacy]
+ -[CPLFingerprintSchemeInvalid boundaryKeyDescription]
+ -[CPLFingerprintSchemeInvalid boundaryKey]
+ -[CPLFingerprintSchemeInvalid initForMMCSv2:]
+ -[CPLFingerprintSchemeInvalid isValidFingerprint:]
+ -[CPLFingerprintSchemeInvalid isValidSignature:]
+ -[CPLFingerprintSchemeV1 isValidFingerprint:]
+ -[CPLFingerprintSchemeV1 isValidSignature:]
+ -[CPLFingerprintSchemeV2 boundaryKeyDescription]
+ -[CPLFingerprintSchemeV2 isValidFingerprint:]
+ -[CPLFingerprintSchemeV2 isValidSignature:]
+ -[CPLHardcodedFingerprintSchemeV2 boundaryKeyDescription]
+ -[CPLLibraryManager _beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]
+ -[CPLLibraryManager _beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]
+ -[CPLLibraryManager _fetchBoundaryKeyIfNecessaryWithSource:completionHandler:]
+ -[CPLLibraryManager _fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:]
+ -[CPLLibraryManager _fingerprintContext]
+ -[CPLLibraryManager _updateFingerprintContext]
+ -[CPLLibraryManager disableBoundaryKeyFetching]
+ -[CPLLibraryManager isSystemLibrary]
+ -[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]
+ -[CPLLibraryManager willBeginPushSession]
+ -[CPLLibraryManager(CPLManagement) getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]
+ -[CPLMasterChange isEPPRecord]
+ -[CPLMemoryAsset hasMasterIdentifier]
+ -[CPLMemoryAsset masterIdentifier]
+ -[CPLMemoryAsset setMasterIdentifier:]
+ -[CPLProxyLibraryManager _dispatchBlockWhenOpen:].cold.2
+ -[CPLProxyLibraryManager _dispatchBlockWhenOpen:].cold.3
+ -[CPLProxyLibraryManager _dispatchBlockWhenOpen:].cold.4
+ -[CPLProxyLibraryManager _invokeOutstandingInvocationsWithTaskIdentifier:].cold.2
+ -[CPLProxyLibraryManager _invokeSyncOutstandingInvocationsWithTaskIdentifier:].cold.2
+ -[CPLProxyLibraryManager _markConnectionAsInvalid].cold.1
+ -[CPLProxyLibraryManager fingerprintContextIfKnown]
+ -[CPLProxyLibraryManager getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]
+ -[CPLProxyLibraryManager provideLocalResource:recordClassString:completionHandler:].cold.1
+ -[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]
+ -[CPLPushSessionTracker _checkFingerPrint:ofResource:inChange:localScopedIdentifier:fingerprintContext:fingerprintScheme:]
+ -[CPLRecordChange isEPPRecord]
+ -[CPLResource stableHash]
+ -[CPLResourceIdentity realStableHash]
+ -[CPLStatus accountEPPCapability]
+ -[CPLStatus maximumAccountEPPCapability]
+ -[CPLStatus setAccountEPPCapability:]
+ -[CPLSuggestionAsset hasMasterIdentifier]
+ -[CPLSuggestionAsset masterIdentifier]
+ -[CPLSuggestionAsset setMasterIdentifier:]
+ -[CPLSyncSession shouldCheckEPPCapability]
+ -[CPLTransportScopeMapping addConcreteScope:forScope:]
+ -[CPLTransportScopeMapping addTransportScope:forScope:]
+ -[CPLTransportScopeMapping scopeForScopeIdentifier:]
+ -[CPLUploadPushedChangesTask _willNeedToAccessScopeWithIdentifier:error:]
+ GCC_except_table1159
+ GCC_except_table1205
+ GCC_except_table1210
+ GCC_except_table1214
+ GCC_except_table1222
+ GCC_except_table1225
+ GCC_except_table1228
+ GCC_except_table1234
+ GCC_except_table1236
+ GCC_except_table1316
+ GCC_except_table1402
+ GCC_except_table1932
+ GCC_except_table2041
+ GCC_except_table2047
+ GCC_except_table2087
+ GCC_except_table2173
+ GCC_except_table2183
+ GCC_except_table2317
+ GCC_except_table2404
+ GCC_except_table2625
+ GCC_except_table2627
+ GCC_except_table2713
+ GCC_except_table2776
+ GCC_except_table2778
+ GCC_except_table2915
+ GCC_except_table2918
+ GCC_except_table2939
+ GCC_except_table3015
+ GCC_except_table3019
+ GCC_except_table3021
+ GCC_except_table3023
+ GCC_except_table3027
+ GCC_except_table3147
+ GCC_except_table3196
+ GCC_except_table3428
+ GCC_except_table3502
+ GCC_except_table3506
+ GCC_except_table3508
+ GCC_except_table3517
+ GCC_except_table3790
+ GCC_except_table3820
+ GCC_except_table3853
+ GCC_except_table3870
+ GCC_except_table3883
+ GCC_except_table3891
+ GCC_except_table3893
+ GCC_except_table3907
+ GCC_except_table3909
+ GCC_except_table3911
+ GCC_except_table4249
+ GCC_except_table4292
+ GCC_except_table4380
+ GCC_except_table4390
+ GCC_except_table4448
+ GCC_except_table4451
+ GCC_except_table4622
+ GCC_except_table4632
+ GCC_except_table4714
+ GCC_except_table4718
+ GCC_except_table4722
+ GCC_except_table4728
+ GCC_except_table4745
+ GCC_except_table4746
+ GCC_except_table4750
+ GCC_except_table4794
+ GCC_except_table4803
+ GCC_except_table4858
+ GCC_except_table4860
+ GCC_except_table4862
+ GCC_except_table4875
+ GCC_except_table5010
+ GCC_except_table5051
+ GCC_except_table5060
+ GCC_except_table5061
+ GCC_except_table511
+ GCC_except_table5118
+ GCC_except_table5121
+ GCC_except_table5391
+ GCC_except_table5420
+ GCC_except_table544
+ GCC_except_table5462
+ GCC_except_table5484
+ GCC_except_table5519
+ GCC_except_table5531
+ GCC_except_table5560
+ GCC_except_table5587
+ GCC_except_table5591
+ GCC_except_table5617
+ GCC_except_table5649
+ GCC_except_table5690
+ GCC_except_table5749
+ GCC_except_table5790
+ GCC_except_table5803
+ GCC_except_table5814
+ GCC_except_table5821
+ GCC_except_table5878
+ GCC_except_table6004
+ GCC_except_table6017
+ GCC_except_table6020
+ GCC_except_table6496
+ GCC_except_table650
+ GCC_except_table6535
+ GCC_except_table6539
+ GCC_except_table6541
+ GCC_except_table6556
+ GCC_except_table6562
+ GCC_except_table6570
+ GCC_except_table6576
+ GCC_except_table6580
+ GCC_except_table6588
+ GCC_except_table6591
+ GCC_except_table6611
+ GCC_except_table6618
+ GCC_except_table6641
+ GCC_except_table6675
+ GCC_except_table6699
+ GCC_except_table6708
+ GCC_except_table6728
+ GCC_except_table6731
+ GCC_except_table6733
+ GCC_except_table6735
+ GCC_except_table6767
+ GCC_except_table680
+ GCC_except_table6837
+ GCC_except_table684
+ GCC_except_table693
+ GCC_except_table6974
+ GCC_except_table6996
+ GCC_except_table7026
+ GCC_except_table7202
+ GCC_except_table7211
+ GCC_except_table7216
+ GCC_except_table7230
+ GCC_except_table724
+ GCC_except_table7245
+ GCC_except_table7257
+ GCC_except_table7262
+ GCC_except_table7341
+ GCC_except_table739
+ GCC_except_table7422
+ GCC_except_table7431
+ GCC_except_table7487
+ GCC_except_table750
+ GCC_except_table7532
+ GCC_except_table7540
+ GCC_except_table7541
+ GCC_except_table7554
+ GCC_except_table764
+ GCC_except_table770
+ GCC_except_table779
+ GCC_except_table786
+ GCC_except_table801
+ GCC_except_table894
+ GCC_except_table966
+ GCC_except_table986
+ GCC_except_table988
+ OBJC_IVAR_$_CPLAlbumChange._userModificationDate
+ OBJC_IVAR_$_CPLBeforeUploadCheckItems._fingerprintContext
+ OBJC_IVAR_$_CPLCallObserver._callDescription
+ OBJC_IVAR_$_CPLCallObserver._functionName
+ OBJC_IVAR_$_CPLEngineLibrary._currentChangeSessionToken
+ OBJC_IVAR_$_CPLEngineLibrary._pendingChangeSessionCompletionHandler
+ OBJC_IVAR_$_CPLEngineLibrary._pendingChangeSessionToken
+ OBJC_IVAR_$_CPLEngineScopeStorage._serverFeatureCompatibleVersionToUpdate
+ OBJC_IVAR_$_CPLEngineScopeStorage._shouldUpdateGlobalStatusAtEndOfTransaction
+ OBJC_IVAR_$_CPLFingerprintContext._lock
+ OBJC_IVAR_$_CPLFingerprintSchemeInvalid._isMMCSv2
+ OBJC_IVAR_$_CPLLibraryManager._forManagement
+ OBJC_IVAR_$_CPLLibraryManager._hasFetchedBoundaryKey
+ OBJC_IVAR_$_CPLMemoryAsset._masterIdentifier
+ OBJC_IVAR_$_CPLSuggestionAsset._masterIdentifier
+ OBJC_IVAR_$_CPLSyncSession._shouldCheckEPPCapability
+ OBJC_IVAR_$_CPLTransportScopeMapping._concreteScopeMapping
+ OBJC_IVAR_$_CPLTransportScopeMapping._scopeMapping
+ _CPLAppBundleIdentifierForContainerIdentifier
+ _CPLFeatureNameEPP
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_9
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _PCSGetAppBoundaryKey
+ __105-[CPLLibraryManager startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.440
+ __106-[CPLProxyLibraryManager cloudCacheGetDescriptionForRecordWithScopedIdentifier:related:completionHandler:]_block_invoke_2.cold.1
+ __109-[CPLProxyLibraryManager getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]_block_invoke_2.cold.1
+ __109-[CPLProxyLibraryManager getStreamingURLForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.360
+ __109-[CPLProxyLibraryManager getStreamingURLForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke_2.361
+ __110-[CPLLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.328
+ __115-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.449
+ __115-[CPLProxyLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.352
+ __116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.137
+ __116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.139
+ __120-[CPLLibraryManager getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.338
+ __122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.576
+ __127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.476
+ __127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2.477
+ __127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2.cold.1
+ __35-[CPLMingleChangesScopeTask launch]_block_invoke.97
+ __36-[CPLEngineLibrary startSyncSession]_block_invoke.70
+ __36-[CPLEngineLibrary startSyncSession]_block_invoke.71
+ __37-[CPLUploadPushedChangesTask cancel:]_block_invoke.185
+ __41-[CPLProxyLibraryManager disableMingling]_block_invoke_2.cold.1
+ __42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.101
+ __42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.102
+ __42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.95
+ __42-[CPLLibraryManager discardCurrentSession]_block_invoke.288
+ __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.270
+ __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.271
+ __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.278
+ __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.279
+ __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.283
+ __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.cold.1
+ __43-[CPLRecordChange propertiesForChangeType:]_block_invoke.164
+ __43-[CPLRecordChange propertiesForChangeType:]_block_invoke.195
+ __44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.276
+ __46-[CPLMingleChangesScopeTask _mingleRemappings]_block_invoke.92
+ __47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.186
+ __47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.190
+ __47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.193
+ __48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke.79
+ __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.297
+ __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.298
+ __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.301
+ __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.304
+ __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.cold.1
+ __49-[CPLUploadPushedChangesTask _prepareUploadBatch]_block_invoke.155
+ __49-[CPLUploadPushedChangesTask _prepareUploadBatch]_block_invoke_2.156
+ __50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1667
+ __50-[CPLEngineStore testKey:value:completionHandler:]_block_invoke.555
+ __51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.353
+ __51-[CPLLibraryManager createScope:completionHandler:]_block_invoke.362
+ __52-[CPLEngineSystemMonitor openWithCompletionHandler:]_block_invoke.14
+ __52-[CPLMingleChangesScopeTask _mingleSharedRemappings]_block_invoke.91
+ __52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.315
+ __52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.319
+ __52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.320
+ __53-[CPLMingleChangesScopeTask _acknownledgeFixUpTasks:]_block_invoke.86
+ __53-[CPLMingleChangesScopeTask _unstashRecordsForScope:]_block_invoke.95
+ __53-[CPLProxyLibraryManager closeWithCompletionHandler:]_block_invoke.327
+ __54-[CPLLibraryManager forceBackupWithCompletionHandler:]_block_invoke.561
+ __55-[CPLEngineLibrary attachObject:withCompletionHandler:]_block_invoke.85
+ __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.165
+ __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.169
+ __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.170
+ __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.171
+ __56-[CPLEngineStore _closeAndDeactivate:completionHandler:]_block_invoke.328
+ __57-[CPLEngineStore _reallyPerformBatchedTransactionsLocked]_block_invoke.300
+ __57-[CPLEngineStore _reallyPerformBatchedTransactionsLocked]_block_invoke_2.301
+ __57-[CPLLibraryManager acceptSharedScope:completionHandler:]_block_invoke.470
+ __58-[CPLEngineLibrary _requestUpdateOfMainScopeFromTransport]_block_invoke.61
+ __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.202
+ __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.205
+ __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.206
+ __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_2.207
+ __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.330
+ __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.331
+ __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.335
+ __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.332
+ __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.336
+ __58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke.408
+ __58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke_2.cold.1
+ __58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke_2.cold.2
+ __59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.137
+ __59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.138
+ __59-[CPLLibraryManager updateShareForScope:completionHandler:]_block_invoke.366
+ __59-[CPLProxyLibraryManager _reallyOpenWithCompletionHandler:]_block_invoke.289
+ __59-[CPLProxyLibraryManager disableSynchronizationWithReason:]_block_invoke_2.cold.1
+ __59-[CPLProxyPullSession getChangeBatchWithCompletionHandler:]_block_invoke_2.2.cold.1
+ __60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.191
+ __60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.197
+ __62-[CPLProxyLibraryManager noteClientIsBeginningSignificantWork]_block_invoke_2.cold.1
+ __62-[CPLProxyLibraryManager pushAllChangesWithCompletionHandler:]_block_invoke_2.cold.1
+ __62-[CPLProxyLibraryManager pushAllChangesWithCompletionHandler:]_block_invoke_2.cold.2
+ __63-[CPLProxyLibraryManager forceSyncDidFinishForTask:withErrors:]_block_invoke.457
+ __63-[CPLProxyPushSession commitChangeBatch:withCompletionHandler:]_block_invoke_2.2.cold.1
+ __64-[CPLProxyLibraryManager attachComputeStates:completionHandler:]_block_invoke_2.cold.1
+ __64-[CPLProxyLibraryManager compactFileCacheWithCompletionHandler:]_block_invoke_2.cold.1
+ __65-[CPLLibraryManager sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.457
+ __65-[CPLProcessStagedScopesScopeTask _deleteStagingScopeIfNecessary]_block_invoke.27
+ __65-[CPLProcessStagedScopesScopeTask _deleteStagingScopeIfNecessary]_block_invoke.33
+ __65-[CPLProcessStagedScopesScopeTask _deleteStagingScopeIfNecessary]_block_invoke_2.28
+ __65-[CPLProxyLibraryManager provideCloudResource:completionHandler:]_block_invoke_2.cold.1
+ __66-[CPLLibraryManager refreshScopeWithIdentifier:completionHandler:]_block_invoke.385
+ __66-[CPLProxyLibraryManager getChangedStatusesWithCompletionHandler:]_block_invoke_2.cold.1
+ __66-[CPLRecordChange mergeRecordChangeWithNewRecordChange:direction:]_block_invoke.158
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.304
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.307
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.311
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.305
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.308
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.312
+ __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_3.306
+ __67-[CPLProxyLibraryManager getListOfComponentsWithCompletionHandler:]_block_invoke_2.cold.1
+ __67-[CPLProxyLibraryManager getStatusForComponents:completionHandler:]_block_invoke_2.cold.1
+ __68-[CPLLibraryManager fetchSharedScopeFromShareURL:completionHandler:]_block_invoke.466
+ __68-[CPLProxyPullSession acknowledgeChangeBatch:withCompletionHandler:]_block_invoke_2.11.cold.1
+ __70-[CPLRecordChange changeIsOnlyAddingResourcesToRecord:addedResources:]_block_invoke.280
+ __71-[CPLDerivativesFilter _enumerateDropDerivativeRules:ofType:withBlock:]_block_invoke.217
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.147
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.154
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.156
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.160
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.162
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.173
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.161
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.163
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.174
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.164
+ __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.175
+ __72-[CPLFingerprintContext refreshBoundaryKeyWithSource:completionHandler:]_block_invoke.38
+ __72-[CPLLibraryManager deleteScopeWithIdentifier:forced:completionHandler:]_block_invoke.377
+ __72-[CPLLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.565
+ __72-[CPLProxyLibraryManager getStatusArrayForComponents:completionHandler:]_block_invoke_2.cold.1
+ __72-[CPLProxyLibraryManager resetCacheWithOption:reason:completionHandler:]_block_invoke_2.cold.1
+ __74-[CPLLibraryManager fetchExistingSharedLibraryScopeWithCompletionHandler:]_block_invoke.474
+ __76-[CPLEngineLibrary provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke.136
+ __76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke.754
+ __76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_2.755
+ __76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_3.765
+ __76-[CPLLibraryManager queryUserDetailsForShareParticipants:completionHandler:]_block_invoke.485
+ __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.236
+ __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.242
+ __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.249
+ __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke_2.243
+ __78-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.492
+ __78-[CPLMingleChangesScopeTask _filteredBatchByStashingRecordsIfNecessary:error:]_block_invoke.60
+ __78-[CPLMingleChangesScopeTask _filteredBatchByStashingRecordsIfNecessary:error:]_block_invoke.62
+ __79-[CPLEngineLibrary provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke.133
+ __79-[CPLLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke.528
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.217
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.223
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.232
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.213
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.224
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.233
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.214
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.225
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.234
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_4.226
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_4.235
+ __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_5.227
+ __82-[CPLLibraryManager rampingRequestForResourceType:numRequested:completionHandler:]_block_invoke.348
+ __82-[CPLProxyLibraryManager provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke_2.cold.1
+ __83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.427
+ __83-[CPLProxyLibraryManager provideLocalResource:recordClassString:completionHandler:]_block_invoke_2.cold.1
+ __83-[CPLProxyLibraryManager provideLocalResource:recordClassString:completionHandler:]_block_invoke_2.cold.2
+ __84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.293
+ __84-[CPLProxyLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke_2.cold.1
+ __84-[CPLProxyLibraryManager getResourcesForItemWithScopedIdentifier:completionHandler:]_block_invoke_2.cold.1
+ __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.120
+ __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.122
+ __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.123
+ __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_2.124
+ __85-[CPLProxyLibraryManager getStatusForRecordsWithScopedIdentifiers:completionHandler:]_block_invoke_2.cold.1
+ __85-[CPLProxyLibraryManager provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke_2.cold.1
+ __86-[CPLLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.356
+ __87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke.569
+ __87-[CPLProxyLibraryManager getScopeStatusCountsForScopeWithIdentifier:completionHandler:]_block_invoke_2.cold.1
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.255
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.261
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.263
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.265
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.267
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.273
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.283
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.286
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.289
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.256
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.262
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.264
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.266
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.275
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.287
+ __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.290
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.179
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.185
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.191
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.193
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.199
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.200
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.203
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.180
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.186
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.192
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.194
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.196
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.204
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.187
+ __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.205
+ __90-[CPLUploadPushedChangesTask _generateNeededDerivativesWithFetchCache:fingerprintContext:]_block_invoke.142
+ __91-[CPLProxyLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.374
+ __91-[CPLProxyLibraryManager providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_3.cold.1
+ __93-[CPLProxyLibraryManager addDropDerivativesRecipe:writeToUserDefaults:withCompletionHandler:]_block_invoke_2.cold.1
+ __95-[CPLRecordChange applyChange:copyPropertiesToFinalChange:forChangeType:direction:diffTracker:]_block_invoke.139
+ __95-[CPLRecordChange applyChange:copyPropertiesToFinalChange:forChangeType:direction:diffTracker:]_block_invoke.141
+ __96-[CPLProxyLibraryManager getStatusesForScopesWithIdentifiers:includeStorages:completionHandler:]_block_invoke_2.cold.1
+ __Block_byref_object_copy_.10697
+ __Block_byref_object_copy_.10987
+ __Block_byref_object_copy_.1151
+ __Block_byref_object_copy_.11775
+ __Block_byref_object_copy_.12710
+ __Block_byref_object_copy_.1296
+ __Block_byref_object_copy_.13264
+ __Block_byref_object_copy_.13590
+ __Block_byref_object_copy_.13778
+ __Block_byref_object_copy_.14582
+ __Block_byref_object_copy_.15202
+ __Block_byref_object_copy_.15923
+ __Block_byref_object_copy_.16193
+ __Block_byref_object_copy_.16668
+ __Block_byref_object_copy_.1691
+ __Block_byref_object_copy_.17270
+ __Block_byref_object_copy_.19505
+ __Block_byref_object_copy_.19648
+ __Block_byref_object_copy_.1991
+ __Block_byref_object_copy_.20175
+ __Block_byref_object_copy_.20772
+ __Block_byref_object_copy_.21244
+ __Block_byref_object_copy_.21594
+ __Block_byref_object_copy_.22599
+ __Block_byref_object_copy_.22901
+ __Block_byref_object_copy_.23654
+ __Block_byref_object_copy_.2448
+ __Block_byref_object_copy_.2523
+ __Block_byref_object_copy_.2840
+ __Block_byref_object_copy_.3140
+ __Block_byref_object_copy_.5505
+ __Block_byref_object_copy_.6076
+ __Block_byref_object_copy_.6226
+ __Block_byref_object_copy_.6777
+ __Block_byref_object_copy_.7163
+ __Block_byref_object_copy_.7430
+ __Block_byref_object_copy_.7850
+ __Block_byref_object_copy_.882
+ __Block_byref_object_copy_.9226
+ __Block_byref_object_copy_.9476
+ __Block_byref_object_dispose_.10698
+ __Block_byref_object_dispose_.10988
+ __Block_byref_object_dispose_.1152
+ __Block_byref_object_dispose_.11776
+ __Block_byref_object_dispose_.12711
+ __Block_byref_object_dispose_.1297
+ __Block_byref_object_dispose_.13265
+ __Block_byref_object_dispose_.13591
+ __Block_byref_object_dispose_.13779
+ __Block_byref_object_dispose_.14583
+ __Block_byref_object_dispose_.15203
+ __Block_byref_object_dispose_.15924
+ __Block_byref_object_dispose_.16194
+ __Block_byref_object_dispose_.16669
+ __Block_byref_object_dispose_.1692
+ __Block_byref_object_dispose_.17271
+ __Block_byref_object_dispose_.19506
+ __Block_byref_object_dispose_.19649
+ __Block_byref_object_dispose_.1992
+ __Block_byref_object_dispose_.20176
+ __Block_byref_object_dispose_.20773
+ __Block_byref_object_dispose_.21245
+ __Block_byref_object_dispose_.21595
+ __Block_byref_object_dispose_.22600
+ __Block_byref_object_dispose_.22902
+ __Block_byref_object_dispose_.23655
+ __Block_byref_object_dispose_.2449
+ __Block_byref_object_dispose_.2524
+ __Block_byref_object_dispose_.2841
+ __Block_byref_object_dispose_.3141
+ __Block_byref_object_dispose_.5506
+ __Block_byref_object_dispose_.6077
+ __Block_byref_object_dispose_.6227
+ __Block_byref_object_dispose_.6778
+ __Block_byref_object_dispose_.7164
+ __Block_byref_object_dispose_.7431
+ __Block_byref_object_dispose_.7851
+ __Block_byref_object_dispose_.883
+ __Block_byref_object_dispose_.9227
+ __Block_byref_object_dispose_.9477
+ __CPLConfigurationOSLogDomain.18867
+ __CPLConfigurationOSLogDomain.onceToken.18873
+ __CPLConfigurationOSLogDomain.result.18875
+ __CPLForceSyncOSLogDomain.20305
+ __CPLForceSyncOSLogDomain.onceToken.20314
+ __CPLForceSyncOSLogDomain.result.20315
+ __CPLManagerOSLogDomain.cold.1
+ __CPLProxyPullSessionOSLogDomain.cold.1
+ __CPLProxyPushSessionOSLogDomain.cold.1
+ __CPLSchedulerOSLogDomain.7104
+ __CPLSchedulerOSLogDomain.onceToken.7105
+ __CPLSchedulerOSLogDomain.result.7106
+ __CPLSessionOSLogDomain.15782
+ __CPLSessionOSLogDomain.17650
+ __CPLSessionOSLogDomain.22206
+ __CPLSessionOSLogDomain.cold.1
+ __CPLSessionOSLogDomain.onceToken.15839
+ __CPLSessionOSLogDomain.onceToken.17655
+ __CPLSessionOSLogDomain.onceToken.22208
+ __CPLSessionOSLogDomain.result.15840
+ __CPLSessionOSLogDomain.result.17656
+ __CPLSessionOSLogDomain.result.22210
+ __CPLStorageOSLogDomain.10660
+ __CPLStorageOSLogDomain.10753
+ __CPLStorageOSLogDomain.17238
+ __CPLStorageOSLogDomain.19628
+ __CPLStorageOSLogDomain.1971
+ __CPLStorageOSLogDomain.20922
+ __CPLStorageOSLogDomain.21581
+ __CPLStorageOSLogDomain.21837
+ __CPLStorageOSLogDomain.5849
+ __CPLStorageOSLogDomain.7387
+ __CPLStorageOSLogDomain.8106
+ __CPLStorageOSLogDomain.8524
+ __CPLStorageOSLogDomain.8694
+ __CPLStorageOSLogDomain.8885
+ __CPLStorageOSLogDomain.904
+ __CPLStorageOSLogDomain.onceToken.10671
+ __CPLStorageOSLogDomain.onceToken.10756
+ __CPLStorageOSLogDomain.onceToken.14123
+ __CPLStorageOSLogDomain.onceToken.17240
+ __CPLStorageOSLogDomain.onceToken.19630
+ __CPLStorageOSLogDomain.onceToken.1973
+ __CPLStorageOSLogDomain.onceToken.19917
+ __CPLStorageOSLogDomain.onceToken.20926
+ __CPLStorageOSLogDomain.onceToken.21586
+ __CPLStorageOSLogDomain.onceToken.21845
+ __CPLStorageOSLogDomain.onceToken.5851
+ __CPLStorageOSLogDomain.onceToken.7389
+ __CPLStorageOSLogDomain.onceToken.8112
+ __CPLStorageOSLogDomain.onceToken.8530
+ __CPLStorageOSLogDomain.onceToken.8696
+ __CPLStorageOSLogDomain.onceToken.8887
+ __CPLStorageOSLogDomain.onceToken.913
+ __CPLStorageOSLogDomain.result.10673
+ __CPLStorageOSLogDomain.result.10758
+ __CPLStorageOSLogDomain.result.14125
+ __CPLStorageOSLogDomain.result.17242
+ __CPLStorageOSLogDomain.result.19632
+ __CPLStorageOSLogDomain.result.1975
+ __CPLStorageOSLogDomain.result.19918
+ __CPLStorageOSLogDomain.result.20928
+ __CPLStorageOSLogDomain.result.21588
+ __CPLStorageOSLogDomain.result.21847
+ __CPLStorageOSLogDomain.result.5853
+ __CPLStorageOSLogDomain.result.7390
+ __CPLStorageOSLogDomain.result.8113
+ __CPLStorageOSLogDomain.result.8532
+ __CPLStorageOSLogDomain.result.8697
+ __CPLStorageOSLogDomain.result.8888
+ __CPLStorageOSLogDomain.result.915
+ __CPLStoreOSLogDomain.2929
+ __CPLStoreOSLogDomain.onceToken.2930
+ __CPLStoreOSLogDomain.result.2931
+ __CPLTaskOSLogDomain.10931
+ __CPLTaskOSLogDomain.1294
+ __CPLTaskOSLogDomain.13560
+ __CPLTaskOSLogDomain.14028
+ __CPLTaskOSLogDomain.15097
+ __CPLTaskOSLogDomain.16572
+ __CPLTaskOSLogDomain.20717
+ __CPLTaskOSLogDomain.22526
+ __CPLTaskOSLogDomain.23611
+ __CPLTaskOSLogDomain.2510
+ __CPLTaskOSLogDomain.5236
+ __CPLTaskOSLogDomain.6698
+ __CPLTaskOSLogDomain.onceToken.10970
+ __CPLTaskOSLogDomain.onceToken.1311
+ __CPLTaskOSLogDomain.onceToken.13562
+ __CPLTaskOSLogDomain.onceToken.14030
+ __CPLTaskOSLogDomain.onceToken.15106
+ __CPLTaskOSLogDomain.onceToken.16579
+ __CPLTaskOSLogDomain.onceToken.20759
+ __CPLTaskOSLogDomain.onceToken.22538
+ __CPLTaskOSLogDomain.onceToken.23619
+ __CPLTaskOSLogDomain.onceToken.2512
+ __CPLTaskOSLogDomain.onceToken.5241
+ __CPLTaskOSLogDomain.onceToken.6712
+ __CPLTaskOSLogDomain.result.10972
+ __CPLTaskOSLogDomain.result.1312
+ __CPLTaskOSLogDomain.result.13564
+ __CPLTaskOSLogDomain.result.14031
+ __CPLTaskOSLogDomain.result.15108
+ __CPLTaskOSLogDomain.result.16580
+ __CPLTaskOSLogDomain.result.20761
+ __CPLTaskOSLogDomain.result.22540
+ __CPLTaskOSLogDomain.result.23620
+ __CPLTaskOSLogDomain.result.2514
+ __CPLTaskOSLogDomain.result.5243
+ __CPLTaskOSLogDomain.result.6714
+ __OBJC_$_CLASS_METHODS_CPLStatus
+ __OBJC_$_INSTANCE_VARIABLES_CPLFingerprintSchemeInvalid
+ __OBJC_$_PROP_LIST_CPLLibraryManagerImplementation
+ ___109-[CPLProxyLibraryManager getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]_block_invoke
+ ___109-[CPLProxyLibraryManager getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]_block_invoke_2
+ ___109-[CPLProxyLibraryManager getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]_block_invoke_3
+ ___119-[CPLLibraryManager(CPLManagement) getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:]_block_invoke
+ ___33-[CPLStatus accountEPPCapability]_block_invoke
+ ___35-[CPLCallObserver _callDescription]_block_invoke
+ ___37-[CPLStatus setAccountEPPCapability:]_block_invoke
+ ___40-[CPLFingerprintContext setBoundaryKey:]_block_invoke
+ ___40-[CPLStatus maximumAccountEPPCapability]_block_invoke
+ ___41-[CPLLibraryManager willBeginPushSession]_block_invoke
+ ___44-[CPLEngineLibrary setAccountEPPCapability:]_block_invoke
+ ___44-[CPLFingerprintContext usesMMCSv2AsDefault]_block_invoke
+ ___45+[CPLFingerprintScheme supportsEPPAutoEnable]_block_invoke
+ ___48-[CPLFingerprintContext mmcsv2FingerprintScheme]_block_invoke
+ ___53-[CPLEngineLibrary endChangeSessionWithSessionToken:]_block_invoke
+ ___55-[CPLFingerprintContext fingerprintSchemeForSignature:]_block_invoke
+ ___56-[CPLCallObserver initWithObject:selector:functionName:]_block_invoke
+ ___56-[CPLEngineLibrary setICloudLibraryClientVersionTooOld:]_block_invoke_3
+ ___58-[CPLEngineLibrary _requestUpdateOfMainScopeFromTransport]_block_invoke
+ ___58-[CPLEngineLibrary _requestUpdateOfMainScopeFromTransport]_block_invoke_2
+ ___59-[CPLFingerprintContext fingerprintSchemeForNewMasterAsset]_block_invoke
+ ___63-[CPLFingerprintContext updateWithAccountEPPCapability:source:]_block_invoke
+ ___69-[CPLEngineScopeStorage _updateGlobalStatusWithScopeChange:forScope:]_block_invoke
+ ___72-[CPLFingerprintContext refreshBoundaryKeyWithSource:completionHandler:]_block_invoke
+ ___73-[CPLEngineLibrary beginChangeSessionWithSessionToken:completionHandler:]_block_invoke
+ ___78-[CPLLibraryManager _fetchBoundaryKeyIfNecessaryWithSource:completionHandler:]_block_invoke
+ ___84-[CPLLibraryManager _fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:]_block_invoke
+ ___84-[CPLLibraryManager _fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:]_block_invoke_2
+ ___87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke
+ ___87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke_2
+ ___92-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke
+ ___92-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke_2
+ ___92-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke_3
+ ___92-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke_4
+ ___92-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke_5
+ ___99-[CPLLibraryManager _beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke
+ ___99-[CPLLibraryManager _beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke_2
+ ___99-[CPLLibraryManager _beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke
+ ___99-[CPLLibraryManager _beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke_2
+ ____CPLConfigurationOSLogDomain_block_invoke.18878
+ ____CPLForceSyncOSLogDomain_block_invoke.20317
+ ____CPLSchedulerOSLogDomain_block_invoke.7108
+ ____CPLSessionOSLogDomain_block_invoke.15842
+ ____CPLSessionOSLogDomain_block_invoke.17658
+ ____CPLSessionOSLogDomain_block_invoke.22213
+ ____CPLStorageOSLogDomain_block_invoke.10676
+ ____CPLStorageOSLogDomain_block_invoke.10761
+ ____CPLStorageOSLogDomain_block_invoke.14130
+ ____CPLStorageOSLogDomain_block_invoke.17245
+ ____CPLStorageOSLogDomain_block_invoke.19635
+ ____CPLStorageOSLogDomain_block_invoke.1978
+ ____CPLStorageOSLogDomain_block_invoke.19924
+ ____CPLStorageOSLogDomain_block_invoke.20931
+ ____CPLStorageOSLogDomain_block_invoke.21591
+ ____CPLStorageOSLogDomain_block_invoke.21850
+ ____CPLStorageOSLogDomain_block_invoke.5856
+ ____CPLStorageOSLogDomain_block_invoke.7392
+ ____CPLStorageOSLogDomain_block_invoke.8115
+ ____CPLStorageOSLogDomain_block_invoke.8535
+ ____CPLStorageOSLogDomain_block_invoke.8699
+ ____CPLStorageOSLogDomain_block_invoke.8890
+ ____CPLStorageOSLogDomain_block_invoke.918
+ ____CPLStoreOSLogDomain_block_invoke.2933
+ ____CPLTaskOSLogDomain_block_invoke.10975
+ ____CPLTaskOSLogDomain_block_invoke.1314
+ ____CPLTaskOSLogDomain_block_invoke.13567
+ ____CPLTaskOSLogDomain_block_invoke.14033
+ ____CPLTaskOSLogDomain_block_invoke.15111
+ ____CPLTaskOSLogDomain_block_invoke.16582
+ ____CPLTaskOSLogDomain_block_invoke.20764
+ ____CPLTaskOSLogDomain_block_invoke.22543
+ ____CPLTaskOSLogDomain_block_invoke.23622
+ ____CPLTaskOSLogDomain_block_invoke.2517
+ ____CPLTaskOSLogDomain_block_invoke.5246
+ ____CPLTaskOSLogDomain_block_invoke.6717
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80r88r96r_e32_v32?0"CPLRecordChange"8Q16^B24l
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48bs_e25_v16?0"CPLCallObserver"8l
+ ___block_descriptor_56_e8_32s40s48r_e32_v32?0"CPLRecordChange"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48r_e48_v36?0"CPLScopedIdentifier"8B16"NSString"20#28l
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v24?0"_CPLResourcesMutableArray"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e46_v32?0"CPLScopedIdentifier"8"NSString"16^B24l
+ ___block_descriptor_80_e8_32s40s48s56r64r_e46_v32?0"CPLScopedIdentifier"8"NSNumber"16^B24l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r
+ __block_literal_global.1018
+ __block_literal_global.10283
+ __block_literal_global.105
+ __block_literal_global.10519
+ __block_literal_global.1053
+ __block_literal_global.1056
+ __block_literal_global.10672
+ __block_literal_global.10757
+ __block_literal_global.109
+ __block_literal_global.10971
+ __block_literal_global.110.20464
+ __block_literal_global.1155
+ __block_literal_global.117.20465
+ __block_literal_global.11936
+ __block_literal_global.12216
+ __block_literal_global.12737
+ __block_literal_global.1355
+ __block_literal_global.13563
+ __block_literal_global.13827
+ __block_literal_global.14.14064
+ __block_literal_global.14.6046
+ __block_literal_global.14.8936
+ __block_literal_global.14063
+ __block_literal_global.14124
+ __block_literal_global.14288
+ __block_literal_global.1437
+ __block_literal_global.145
+ __block_literal_global.146.12712
+ __block_literal_global.146.3420
+ __block_literal_global.148.20760
+ __block_literal_global.14818
+ __block_literal_global.14838
+ __block_literal_global.149
+ __block_literal_global.14902
+ __block_literal_global.15107
+ __block_literal_global.1517
+ __block_literal_global.15645
+ __block_literal_global.158.9002
+ __block_literal_global.15859
+ __block_literal_global.161
+ __block_literal_global.16378
+ __block_literal_global.1651
+ __block_literal_global.1664
+ __block_literal_global.16690
+ __block_literal_global.1678
+ __block_literal_global.1680
+ __block_literal_global.1682
+ __block_literal_global.1688
+ __block_literal_global.17035
+ __block_literal_global.171.20467
+ __block_literal_global.1715
+ __block_literal_global.1717
+ __block_literal_global.1719
+ __block_literal_global.17241
+ __block_literal_global.1727
+ __block_literal_global.1729
+ __block_literal_global.1737
+ __block_literal_global.1745
+ __block_literal_global.1747
+ __block_literal_global.1752
+ __block_literal_global.1754
+ __block_literal_global.176
+ __block_literal_global.17670
+ __block_literal_global.17849
+ __block_literal_global.17986
+ __block_literal_global.18093
+ __block_literal_global.1831
+ __block_literal_global.18504
+ __block_literal_global.18874
+ __block_literal_global.1908
+ __block_literal_global.192
+ __block_literal_global.19262
+ __block_literal_global.19631
+ __block_literal_global.197.14659
+ __block_literal_global.1974
+ __block_literal_global.19798
+ __block_literal_global.19920
+ __block_literal_global.2.23894
+ __block_literal_global.201
+ __block_literal_global.201.14660
+ __block_literal_global.20460
+ __block_literal_global.20783
+ __block_literal_global.20927
+ __block_literal_global.21090
+ __block_literal_global.21587
+ __block_literal_global.21846
+ __block_literal_global.22.7521
+ __block_literal_global.22006
+ __block_literal_global.22209
+ __block_literal_global.2235
+ __block_literal_global.22595
+ __block_literal_global.23155
+ __block_literal_global.23298
+ __block_literal_global.23370
+ __block_literal_global.23766
+ __block_literal_global.23888
+ __block_literal_global.2390
+ __block_literal_global.24.13780
+ __block_literal_global.24013
+ __block_literal_global.24202
+ __block_literal_global.2447
+ __block_literal_global.2513
+ __block_literal_global.27.15878
+ __block_literal_global.270
+ __block_literal_global.282
+ __block_literal_global.289
+ __block_literal_global.290
+ __block_literal_global.2917
+ __block_literal_global.30
+ __block_literal_global.302
+ __block_literal_global.303
+ __block_literal_global.306
+ __block_literal_global.311
+ __block_literal_global.3159
+ __block_literal_global.32.21974
+ __block_literal_global.322.22539
+ __block_literal_global.34.9473
+ __block_literal_global.3427
+ __block_literal_global.355
+ __block_literal_global.3664
+ __block_literal_global.38
+ __block_literal_global.3872
+ __block_literal_global.406
+ __block_literal_global.42.6828
+ __block_literal_global.42.7526
+ __block_literal_global.4289
+ __block_literal_global.43
+ __block_literal_global.441
+ __block_literal_global.4431
+ __block_literal_global.4588
+ __block_literal_global.46
+ __block_literal_global.47.7528
+ __block_literal_global.5
+ __block_literal_global.50
+ __block_literal_global.5012
+ __block_literal_global.5099
+ __block_literal_global.5242
+ __block_literal_global.54.4992
+ __block_literal_global.5401
+ __block_literal_global.5502
+ __block_literal_global.555
+ __block_literal_global.558
+ __block_literal_global.58
+ __block_literal_global.5852
+ __block_literal_global.6052
+ __block_literal_global.6337
+ __block_literal_global.647
+ __block_literal_global.66
+ __block_literal_global.6713
+ __block_literal_global.6827
+ __block_literal_global.7223
+ __block_literal_global.7516
+ __block_literal_global.754
+ __block_literal_global.77.15640
+ __block_literal_global.8.23904
+ __block_literal_global.8220
+ __block_literal_global.8423
+ __block_literal_global.8531
+ __block_literal_global.8633
+ __block_literal_global.878
+ __block_literal_global.881
+ __block_literal_global.884
+ __block_literal_global.887
+ __block_literal_global.8938
+ __block_literal_global.91
+ __block_literal_global.9116
+ __block_literal_global.914
+ __block_literal_global.93.18393
+ __block_literal_global.9371
+ __block_literal_global.939
+ __block_literal_global.9583
+ __block_literal_global.9897
+ __cpl_dispatch_async_block_invoke.10927
+ __cpl_dispatch_async_block_invoke.11584
+ __cpl_dispatch_async_block_invoke.1316
+ __cpl_dispatch_async_block_invoke.13573
+ __cpl_dispatch_async_block_invoke.13949
+ __cpl_dispatch_async_block_invoke.14025
+ __cpl_dispatch_async_block_invoke.15190
+ __cpl_dispatch_async_block_invoke.16150
+ __cpl_dispatch_async_block_invoke.16637
+ __cpl_dispatch_async_block_invoke.16986
+ __cpl_dispatch_async_block_invoke.17478
+ __cpl_dispatch_async_block_invoke.1752
+ __cpl_dispatch_async_block_invoke.17982
+ __cpl_dispatch_async_block_invoke.18853
+ __cpl_dispatch_async_block_invoke.20159
+ __cpl_dispatch_async_block_invoke.20715
+ __cpl_dispatch_async_block_invoke.21098
+ __cpl_dispatch_async_block_invoke.22545
+ __cpl_dispatch_async_block_invoke.23660
+ __cpl_dispatch_async_block_invoke.6276
+ __cpl_dispatch_async_block_invoke.6696
+ __cpl_dispatch_async_block_invoke.675
+ __cpl_dispatch_async_block_invoke.6970
+ __cpl_dispatch_async_block_invoke.7400
+ __cpl_dispatch_async_block_invoke.9223
+ __cpl_dispatch_async_block_invoke.9559
+ __os_feature_enabled_impl
+ __sharedDefaults
+ __shouldUseRealBoundaryKey
+ _connectedLibraryManagerRegisterQueue.cold.1
+ _doProtected:.onceToken.14837
+ _isKnownICloudHost.knownHosts
+ _kPCSSetupDSID
+ _kPCSSetupDSIDAny
+ _objc_msgSend$_addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:
+ _objc_msgSend$_beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:
+ _objc_msgSend$_beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:
+ _objc_msgSend$_callDescription
+ _objc_msgSend$_doesScopeContributeToGlobalStatus:
+ _objc_msgSend$_fetchBoundaryKeyIfNecessaryWithSource:completionHandler:
+ _objc_msgSend$_fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:
+ _objc_msgSend$_fingerprintContext
+ _objc_msgSend$_fixGlobalStatus
+ _objc_msgSend$_requestUpdateOfMainScopeFromTransport
+ _objc_msgSend$_updateFingerprintContext
+ _objc_msgSend$_updateGlobalStatusWithScopeChange:forScope:
+ _objc_msgSend$_willNeedToAccessScopeWithIdentifier:error:
+ _objc_msgSend$accountEPPCapability
+ _objc_msgSend$addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:
+ _objc_msgSend$addTransportScope:forScope:
+ _objc_msgSend$defaultAccountEPPCapabilityInUniverseName:
+ _objc_msgSend$descriptionForAccountEPPCapability:
+ _objc_msgSend$descriptionForSupportedFeatureCompatibleVersion:
+ _objc_msgSend$featureCompatibleVersion
+ _objc_msgSend$fingerprintContextIfKnown
+ _objc_msgSend$fingerprintSchemeDescription
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:
+ _objc_msgSend$initForMMCSv2:
+ _objc_msgSend$initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:fingerprintContext:provider:
+ _objc_msgSend$initWithFingerprintSchemeV1:fingerprintSchemeV2:
+ _objc_msgSend$initWithObject:selector:functionName:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$isCompatibleWithFingerprintScheme:
+ _objc_msgSend$isMMCSv1Fingerprint:
+ _objc_msgSend$isMMCSv1Signature:
+ _objc_msgSend$isMMCSv2Fingerprint:
+ _objc_msgSend$isTransientDerivativeGenerationError:
+ _objc_msgSend$isValid
+ _objc_msgSend$isValidSignature:
+ _objc_msgSend$maximumAccountEPPCapability
+ _objc_msgSend$observeAsyncCallWithFunction:block:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$performUpgradeWithError:
+ _objc_msgSend$realStableHash
+ _objc_msgSend$refreshBoundaryKeyWithSource:completionHandler:
+ _objc_msgSend$removeRelatedRecordsFromQuarantineWithError:
+ _objc_msgSend$requestClientToPullAllChangesInScopeIdentifiers:completionHandler:
+ _objc_msgSend$scheme
+ _objc_msgSend$setAccountEPPCapability:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setBoundaryKey:
+ _objc_msgSend$setHasUpdatedScope:fromTransportWithError:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$setSharedContext:
+ _objc_msgSend$shouldCheckEPPCapability
+ _objc_msgSend$shouldDisableEPP
+ _objc_msgSend$storeVersionHasChanged
+ _objc_msgSend$supportedFeatureCompatibleVersion
+ _objc_msgSend$supportsEPP
+ _objc_msgSend$supportsEPPAutoEnable
+ _objc_msgSend$syncStatus
+ _objc_msgSend$updateWithAccountEPPCapability:source:
+ _objc_msgSend$updateWithStatus:configuration:
+ _statusDidChange.11792
+ copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18411
+ descriptionForSupportedFeatureCompatibleVersion:.descriptions
+ initWithCPLArchiver:.onceToken.1905
+ initWithCPLArchiver:.stringClass.1906
+ initWithCoder:.logOnceToken.19800
+ initWithCoder:.onceToken.10221
+ initWithCoder:.onceToken.13826
+ initWithCoder:.onceToken.17669
+ initWithCoder:.onceToken.19797
+ initWithCoder:.onceToken.22005
+ initWithCoder:.onceToken.24201
+ initWithCoder:.onceToken.4991
+ initWithCoder:.onceToken.5098
+ initWithCoder:.onceToken.6045
+ initWithCoder:.pushContextsClasses.22007
+ initWithCoder:.stringClass.10222
+ propertiesForChangeType:.onceToken.14658
+ propertiesForChangeType:.onceToken.18426
+ propertiesForChangeType:.onceToken.194
+ propertiesForChangeType:.onceToken.199
+ propertiesForChangeType:.onceToken.23297
+ propertiesForChangeType:.properties.23299
+ supportsEPPAutoEnable.onceToken
+ supportsEPPAutoEnable.result
- +[CPLFingerprintContext usesMMCSv2AsDefaultInUniverseName:]
- +[CPLFingerprintScheme defaultFingerprintSchemeForUnknownRecord]
- +[CPLFingerprintScheme isMMCSv1SignatureBytes:]
- +[CPLFingerprintScheme isMMCSv1SignatureBytesKnownNotMMCSv2:]
- +[CPLFingerprintScheme isMMCSv2SignatureBytes:]
- -[CPLBeforeUploadCheckItems initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:provider:]
- -[CPLCallObserver initWithObject:selector:]
- -[CPLEngineScopeStorage _doesScopeContributeToAssetCounts:]
- -[CPLEngineScopeStorage _updateAssetCountsWithScopeChange:forScope:]
- -[CPLFingerprintContext initWithBoundaryKey:usesMMCSv2AsDefault:]
- -[CPLFingerprintContext initWithFingerprintSchemeV1:fingerprintSchemeV2:usesMMCSv2AsDefault:]
- -[CPLFingerprintScheme isValidSignatureBytes:]
- -[CPLFingerprintSchemeV1 isValidSignatureBytes:]
- -[CPLFingerprintSchemeV2 isValidSignatureBytes:]
- -[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]
- -[CPLMemoryAsset hasMasterFingerprint]
- -[CPLMemoryAsset masterFingerprint]
- -[CPLMemoryAsset setMasterFingerprint:]
- -[CPLProxyLibraryManager getCloudCacheForRecordWithScopedIdentifier:completionHandler:]
- -[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]
- -[CPLResourceIdentity stableHashForMasterWithManager:]
- -[CPLSuggestionAsset hasMasterFingerprint]
- -[CPLSuggestionAsset masterFingerprint]
- -[CPLSuggestionAsset setMasterFingerprint:]
- -[CPLTransportScopeMapping addConcreteScope:forScopeWithIdentifier:]
- -[CPLTransportScopeMapping addTransportScope:forScopeWithIdentifier:]
- -[CPLTransportScopeMapping setObject:forKeyedSubscript:]
- -[CPLTransportScopeMapping setSharedScopeIdentifier:forScopeWithIdentifier:]
- -[CPLTransportScopeMapping sharedScopeIdentifierForScopeWithIdentifier:]
- -[CPLTransportScopeMapping shouldSetSharedScopeIdentifierForScopeWithIdentifier:]
- GCC_except_table1150
- GCC_except_table1207
- GCC_except_table1209
- GCC_except_table1290
- GCC_except_table1375
- GCC_except_table1898
- GCC_except_table2007
- GCC_except_table2013
- GCC_except_table2053
- GCC_except_table2139
- GCC_except_table2149
- GCC_except_table2283
- GCC_except_table2364
- GCC_except_table2584
- GCC_except_table2586
- GCC_except_table2672
- GCC_except_table2735
- GCC_except_table2737
- GCC_except_table2875
- GCC_except_table2878
- GCC_except_table2899
- GCC_except_table2975
- GCC_except_table2979
- GCC_except_table2981
- GCC_except_table2983
- GCC_except_table2987
- GCC_except_table3106
- GCC_except_table3155
- GCC_except_table3384
- GCC_except_table3458
- GCC_except_table3462
- GCC_except_table3464
- GCC_except_table3473
- GCC_except_table3744
- GCC_except_table3774
- GCC_except_table3807
- GCC_except_table3824
- GCC_except_table3837
- GCC_except_table3845
- GCC_except_table3847
- GCC_except_table3861
- GCC_except_table3863
- GCC_except_table3865
- GCC_except_table4198
- GCC_except_table4232
- GCC_except_table4316
- GCC_except_table4326
- GCC_except_table4384
- GCC_except_table4387
- GCC_except_table4558
- GCC_except_table4568
- GCC_except_table4650
- GCC_except_table4654
- GCC_except_table4658
- GCC_except_table4664
- GCC_except_table4681
- GCC_except_table4682
- GCC_except_table4686
- GCC_except_table4727
- GCC_except_table4736
- GCC_except_table4791
- GCC_except_table4793
- GCC_except_table4795
- GCC_except_table4808
- GCC_except_table4941
- GCC_except_table4981
- GCC_except_table4990
- GCC_except_table4991
- GCC_except_table5047
- GCC_except_table5050
- GCC_except_table5320
- GCC_except_table5348
- GCC_except_table5382
- GCC_except_table5407
- GCC_except_table543
- GCC_except_table5442
- GCC_except_table5454
- GCC_except_table5483
- GCC_except_table5510
- GCC_except_table5514
- GCC_except_table5540
- GCC_except_table5572
- GCC_except_table5613
- GCC_except_table5666
- GCC_except_table5707
- GCC_except_table5720
- GCC_except_table5731
- GCC_except_table5738
- GCC_except_table5795
- GCC_except_table5921
- GCC_except_table5934
- GCC_except_table5937
- GCC_except_table6411
- GCC_except_table6449
- GCC_except_table6453
- GCC_except_table6455
- GCC_except_table6470
- GCC_except_table6476
- GCC_except_table6484
- GCC_except_table649
- GCC_except_table6490
- GCC_except_table6494
- GCC_except_table6502
- GCC_except_table6505
- GCC_except_table6525
- GCC_except_table6532
- GCC_except_table6555
- GCC_except_table6589
- GCC_except_table6613
- GCC_except_table6622
- GCC_except_table6642
- GCC_except_table6645
- GCC_except_table6647
- GCC_except_table6649
- GCC_except_table6681
- GCC_except_table6751
- GCC_except_table678
- GCC_except_table682
- GCC_except_table685
- GCC_except_table6887
- GCC_except_table6909
- GCC_except_table6938
- GCC_except_table702
- GCC_except_table7113
- GCC_except_table7122
- GCC_except_table7127
- GCC_except_table7141
- GCC_except_table7156
- GCC_except_table7168
- GCC_except_table7173
- GCC_except_table7252
- GCC_except_table729
- GCC_except_table7333
- GCC_except_table7342
- GCC_except_table7397
- GCC_except_table7441
- GCC_except_table7449
- GCC_except_table7450
- GCC_except_table746
- GCC_except_table7463
- GCC_except_table762
- GCC_except_table768
- GCC_except_table777
- GCC_except_table784
- GCC_except_table799
- GCC_except_table958
- GCC_except_table978
- GCC_except_table980
- OBJC_IVAR_$_CPLEngineScopeStorage._shouldUpdateAssetCountsAtEndOfTransaction
- OBJC_IVAR_$_CPLFingerprintContext._isUsingFingerprintSchemeSubclasses
- OBJC_IVAR_$_CPLMemoryAsset._masterFingerprint
- OBJC_IVAR_$_CPLSuggestionAsset._masterFingerprint
- OBJC_IVAR_$_CPLTransportScopeMapping._mapping
- OBJC_IVAR_$_CPLTransportScopeMapping._sharedScopeIdentifierMapping
- _MMCSSignatureIsValid
- _MMCSSignatureIsValidV2
- __105-[CPLLibraryManager startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.417
- __109-[CPLProxyLibraryManager getStreamingURLForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.358
- __109-[CPLProxyLibraryManager getStreamingURLForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke_2.359
- __110-[CPLLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.310
- __115-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.426
- __115-[CPLProxyLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.350
- __116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.129
- __120-[CPLLibraryManager getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.320
- __122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.553
- __127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.475
- __127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2.476
- __35-[CPLMingleChangesScopeTask launch]_block_invoke.87
- __36-[CPLEngineLibrary startSyncSession]_block_invoke.65
- __36-[CPLEngineLibrary startSyncSession]_block_invoke.66
- __37-[CPLUploadPushedChangesTask cancel:]_block_invoke.176
- __42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.90
- __42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.92
- __42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.96
- __42-[CPLLibraryManager discardCurrentSession]_block_invoke.279
- __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.268
- __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.269
- __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.275
- __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.276
- __42-[CPLProxyLibraryManager _setupConnection]_block_invoke.281
- __43-[CPLRecordChange propertiesForChangeType:]_block_invoke.144
- __43-[CPLRecordChange propertiesForChangeType:]_block_invoke.175
- __46-[CPLMingleChangesScopeTask _mingleRemappings]_block_invoke.82
- __47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.182
- __47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.183
- __48-[CPLMingleChangesScopeTask _mingleOtherChanges]_block_invoke.69
- __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.295
- __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.296
- __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.299
- __49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.302
- __49-[CPLUploadPushedChangesTask _prepareUploadBatch]_block_invoke.145
- __49-[CPLUploadPushedChangesTask _prepareUploadBatch]_block_invoke_2.146
- __50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1661
- __50-[CPLEngineStore testKey:value:completionHandler:]_block_invoke.554
- __51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.352
- __51-[CPLLibraryManager createScope:completionHandler:]_block_invoke.342
- __52-[CPLEngineSystemMonitor openWithCompletionHandler:]_block_invoke.13
- __52-[CPLMingleChangesScopeTask _mingleSharedRemappings]_block_invoke.81
- __52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.313
- __52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.317
- __52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.318
- __53-[CPLMingleChangesScopeTask _acknownledgeFixUpTasks:]_block_invoke.76
- __53-[CPLMingleChangesScopeTask _unstashRecordsForScope:]_block_invoke.85
- __53-[CPLProxyLibraryManager closeWithCompletionHandler:]_block_invoke.323
- __54-[CPLLibraryManager forceBackupWithCompletionHandler:]_block_invoke.538
- __55-[CPLEngineLibrary attachObject:withCompletionHandler:]_block_invoke.80
- __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.155
- __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.159
- __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.160
- __55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.161
- __56-[CPLEngineLibrary setICloudLibraryClientVersionTooOld:]_block_invoke.61
- __56-[CPLEngineStore _closeAndDeactivate:completionHandler:]_block_invoke.327
- __57-[CPLEngineStore _reallyPerformBatchedTransactionsLocked]_block_invoke.299
- __57-[CPLEngineStore _reallyPerformBatchedTransactionsLocked]_block_invoke_2.300
- __57-[CPLLibraryManager acceptSharedScope:completionHandler:]_block_invoke.447
- __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.190
- __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.196
- __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.197
- __58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_2.198
- __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.328
- __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.329
- __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.333
- __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.330
- __58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.334
- __58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke.406
- __59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.132
- __59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.133
- __59-[CPLLibraryManager updateShareForScope:completionHandler:]_block_invoke.346
- __59-[CPLProxyLibraryManager _reallyOpenWithCompletionHandler:]_block_invoke.287
- __60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.182
- __60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.188
- __63-[CPLProxyLibraryManager forceSyncDidFinishForTask:withErrors:]_block_invoke.455
- __65-[CPLLibraryManager sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.434
- __65-[CPLProcessStagedScopesScopeTask _deleteStagingScopeIfNecessary]_block_invoke.26
- __65-[CPLProcessStagedScopesScopeTask _deleteStagingScopeIfNecessary]_block_invoke.32
- __65-[CPLProcessStagedScopesScopeTask _deleteStagingScopeIfNecessary]_block_invoke_2.27
- __66-[CPLLibraryManager refreshScopeWithIdentifier:completionHandler:]_block_invoke.365
- __66-[CPLRecordChange mergeRecordChangeWithNewRecordChange:direction:]_block_invoke.138
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.299
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.302
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.306
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.300
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.303
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.307
- __67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_3.301
- __68-[CPLLibraryManager fetchSharedScopeFromShareURL:completionHandler:]_block_invoke.443
- __70-[CPLRecordChange changeIsOnlyAddingResourcesToRecord:addedResources:]_block_invoke.261
- __71-[CPLDerivativesFilter _enumerateDropDerivativeRules:ofType:withBlock:]_block_invoke.215
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.142
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.149
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.150
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.151
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.157
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.168
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.156
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.158
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.169
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.159
- __71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.170
- __72-[CPLLibraryManager deleteScopeWithIdentifier:forced:completionHandler:]_block_invoke.357
- __72-[CPLLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.542
- __74-[CPLLibraryManager fetchExistingSharedLibraryScopeWithCompletionHandler:]_block_invoke.451
- __76-[CPLEngineLibrary provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke.131
- __76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke.726
- __76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_2.727
- __76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_3.737
- __76-[CPLLibraryManager queryUserDetailsForShareParticipants:completionHandler:]_block_invoke.462
- __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.231
- __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.237
- __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.244
- __78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke_2.238
- __78-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.469
- __79-[CPLEngineLibrary provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke.128
- __79-[CPLLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke.505
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.207
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.218
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.227
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.208
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.219
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.228
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.209
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.220
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.229
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_4.221
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_4.230
- __80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_5.222
- __82-[CPLLibraryManager rampingRequestForResourceType:numRequested:completionHandler:]_block_invoke.330
- __83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.425
- __84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.292
- __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.115
- __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.117
- __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.118
- __85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_2.119
- __86-[CPLLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.338
- __86-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke.546
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.250
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.256
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.258
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.260
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.262
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.268
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.276
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.278
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.284
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.251
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.257
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.259
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.261
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.270
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.277
- __88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.285
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.174
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.180
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.186
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.188
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.190
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.194
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.198
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.175
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.181
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.187
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.189
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.191
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.199
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.182
- __88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.200
- __90-[CPLUploadPushedChangesTask _generateNeededDerivativesWithFetchCache:fingerprintContext:]_block_invoke.132
- __91-[CPLProxyLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.372
- __95-[CPLRecordChange applyChange:copyPropertiesToFinalChange:forChangeType:direction:diffTracker:]_block_invoke.119
- __95-[CPLRecordChange applyChange:copyPropertiesToFinalChange:forChangeType:direction:diffTracker:]_block_invoke.121
- __98-[CPLLibraryManager beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke.308
- __98-[CPLLibraryManager beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke.296
- __Block_byref_object_copy_.10589
- __Block_byref_object_copy_.10883
- __Block_byref_object_copy_.1150
- __Block_byref_object_copy_.11636
- __Block_byref_object_copy_.12524
- __Block_byref_object_copy_.1295
- __Block_byref_object_copy_.13092
- __Block_byref_object_copy_.13416
- __Block_byref_object_copy_.13591
- __Block_byref_object_copy_.14380
- __Block_byref_object_copy_.15006
- __Block_byref_object_copy_.15727
- __Block_byref_object_copy_.16005
- __Block_byref_object_copy_.16513
- __Block_byref_object_copy_.17116
- __Block_byref_object_copy_.19327
- __Block_byref_object_copy_.19470
- __Block_byref_object_copy_.1971
- __Block_byref_object_copy_.19993
- __Block_byref_object_copy_.20574
- __Block_byref_object_copy_.21034
- __Block_byref_object_copy_.21383
- __Block_byref_object_copy_.22389
- __Block_byref_object_copy_.22692
- __Block_byref_object_copy_.23451
- __Block_byref_object_copy_.2420
- __Block_byref_object_copy_.2495
- __Block_byref_object_copy_.2809
- __Block_byref_object_copy_.3067
- __Block_byref_object_copy_.5415
- __Block_byref_object_copy_.6024
- __Block_byref_object_copy_.6175
- __Block_byref_object_copy_.6699
- __Block_byref_object_copy_.7089
- __Block_byref_object_copy_.7345
- __Block_byref_object_copy_.7772
- __Block_byref_object_copy_.876
- __Block_byref_object_copy_.9152
- __Block_byref_object_copy_.9410
- __Block_byref_object_dispose_.10590
- __Block_byref_object_dispose_.10884
- __Block_byref_object_dispose_.1151
- __Block_byref_object_dispose_.11637
- __Block_byref_object_dispose_.12525
- __Block_byref_object_dispose_.1296
- __Block_byref_object_dispose_.13093
- __Block_byref_object_dispose_.13417
- __Block_byref_object_dispose_.13592
- __Block_byref_object_dispose_.14381
- __Block_byref_object_dispose_.15007
- __Block_byref_object_dispose_.15728
- __Block_byref_object_dispose_.16006
- __Block_byref_object_dispose_.16514
- __Block_byref_object_dispose_.17117
- __Block_byref_object_dispose_.19328
- __Block_byref_object_dispose_.19471
- __Block_byref_object_dispose_.1972
- __Block_byref_object_dispose_.19994
- __Block_byref_object_dispose_.20575
- __Block_byref_object_dispose_.21035
- __Block_byref_object_dispose_.21384
- __Block_byref_object_dispose_.22390
- __Block_byref_object_dispose_.22693
- __Block_byref_object_dispose_.23452
- __Block_byref_object_dispose_.2421
- __Block_byref_object_dispose_.2496
- __Block_byref_object_dispose_.2810
- __Block_byref_object_dispose_.3068
- __Block_byref_object_dispose_.5416
- __Block_byref_object_dispose_.6025
- __Block_byref_object_dispose_.6176
- __Block_byref_object_dispose_.6700
- __Block_byref_object_dispose_.7090
- __Block_byref_object_dispose_.7346
- __Block_byref_object_dispose_.7773
- __Block_byref_object_dispose_.877
- __Block_byref_object_dispose_.9153
- __Block_byref_object_dispose_.9411
- __CPLConfigurationOSLogDomain.18714
- __CPLConfigurationOSLogDomain.onceToken.18720
- __CPLConfigurationOSLogDomain.result.18722
- __CPLForceSyncOSLogDomain.20107
- __CPLForceSyncOSLogDomain.onceToken.20116
- __CPLForceSyncOSLogDomain.result.20117
- __CPLSchedulerOSLogDomain.7029
- __CPLSchedulerOSLogDomain.onceToken.7030
- __CPLSchedulerOSLogDomain.result.7031
- __CPLSessionOSLogDomain.15588
- __CPLSessionOSLogDomain.17494
- __CPLSessionOSLogDomain.21993
- __CPLSessionOSLogDomain.onceToken.15645
- __CPLSessionOSLogDomain.onceToken.17499
- __CPLSessionOSLogDomain.onceToken.21995
- __CPLSessionOSLogDomain.result.15646
- __CPLSessionOSLogDomain.result.17500
- __CPLSessionOSLogDomain.result.21997
- __CPLStorageOSLogDomain.10552
- __CPLStorageOSLogDomain.10645
- __CPLStorageOSLogDomain.17084
- __CPLStorageOSLogDomain.19449
- __CPLStorageOSLogDomain.1951
- __CPLStorageOSLogDomain.20723
- __CPLStorageOSLogDomain.21370
- __CPLStorageOSLogDomain.21624
- __CPLStorageOSLogDomain.5797
- __CPLStorageOSLogDomain.7302
- __CPLStorageOSLogDomain.8009
- __CPLStorageOSLogDomain.8446
- __CPLStorageOSLogDomain.8616
- __CPLStorageOSLogDomain.8807
- __CPLStorageOSLogDomain.898
- __CPLStorageOSLogDomain.onceToken.10563
- __CPLStorageOSLogDomain.onceToken.10648
- __CPLStorageOSLogDomain.onceToken.13935
- __CPLStorageOSLogDomain.onceToken.17086
- __CPLStorageOSLogDomain.onceToken.19451
- __CPLStorageOSLogDomain.onceToken.1953
- __CPLStorageOSLogDomain.onceToken.19739
- __CPLStorageOSLogDomain.onceToken.20727
- __CPLStorageOSLogDomain.onceToken.21375
- __CPLStorageOSLogDomain.onceToken.21632
- __CPLStorageOSLogDomain.onceToken.5799
- __CPLStorageOSLogDomain.onceToken.7304
- __CPLStorageOSLogDomain.onceToken.8015
- __CPLStorageOSLogDomain.onceToken.8452
- __CPLStorageOSLogDomain.onceToken.8618
- __CPLStorageOSLogDomain.onceToken.8809
- __CPLStorageOSLogDomain.onceToken.907
- __CPLStorageOSLogDomain.result.10565
- __CPLStorageOSLogDomain.result.10650
- __CPLStorageOSLogDomain.result.13937
- __CPLStorageOSLogDomain.result.17088
- __CPLStorageOSLogDomain.result.19453
- __CPLStorageOSLogDomain.result.1955
- __CPLStorageOSLogDomain.result.19740
- __CPLStorageOSLogDomain.result.20729
- __CPLStorageOSLogDomain.result.21377
- __CPLStorageOSLogDomain.result.21634
- __CPLStorageOSLogDomain.result.5801
- __CPLStorageOSLogDomain.result.7305
- __CPLStorageOSLogDomain.result.8016
- __CPLStorageOSLogDomain.result.8454
- __CPLStorageOSLogDomain.result.8619
- __CPLStorageOSLogDomain.result.8810
- __CPLStorageOSLogDomain.result.909
- __CPLStoreOSLogDomain.2856
- __CPLStoreOSLogDomain.onceToken.2857
- __CPLStoreOSLogDomain.result.2858
- __CPLTaskOSLogDomain.10824
- __CPLTaskOSLogDomain.1293
- __CPLTaskOSLogDomain.13388
- __CPLTaskOSLogDomain.13840
- __CPLTaskOSLogDomain.14902
- __CPLTaskOSLogDomain.16416
- __CPLTaskOSLogDomain.20519
- __CPLTaskOSLogDomain.22316
- __CPLTaskOSLogDomain.23402
- __CPLTaskOSLogDomain.2482
- __CPLTaskOSLogDomain.5130
- __CPLTaskOSLogDomain.6620
- __CPLTaskOSLogDomain.onceToken.10865
- __CPLTaskOSLogDomain.onceToken.1310
- __CPLTaskOSLogDomain.onceToken.13390
- __CPLTaskOSLogDomain.onceToken.13842
- __CPLTaskOSLogDomain.onceToken.14911
- __CPLTaskOSLogDomain.onceToken.16423
- __CPLTaskOSLogDomain.onceToken.20561
- __CPLTaskOSLogDomain.onceToken.22328
- __CPLTaskOSLogDomain.onceToken.23410
- __CPLTaskOSLogDomain.onceToken.2484
- __CPLTaskOSLogDomain.onceToken.5135
- __CPLTaskOSLogDomain.onceToken.6634
- __CPLTaskOSLogDomain.result.10867
- __CPLTaskOSLogDomain.result.1311
- __CPLTaskOSLogDomain.result.13392
- __CPLTaskOSLogDomain.result.13843
- __CPLTaskOSLogDomain.result.14913
- __CPLTaskOSLogDomain.result.16424
- __CPLTaskOSLogDomain.result.20563
- __CPLTaskOSLogDomain.result.22330
- __CPLTaskOSLogDomain.result.23411
- __CPLTaskOSLogDomain.result.2486
- __CPLTaskOSLogDomain.result.5137
- __CPLTaskOSLogDomain.result.6636
- ___43-[CPLCallObserver initWithObject:selector:]_block_invoke
- ___68-[CPLEngineScopeStorage _updateAssetCountsWithScopeChange:forScope:]_block_invoke
- ___86-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke
- ___86-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke_2
- ___87-[CPLProxyLibraryManager getCloudCacheForRecordWithScopedIdentifier:completionHandler:]_block_invoke
- ___87-[CPLProxyLibraryManager getCloudCacheForRecordWithScopedIdentifier:completionHandler:]_block_invoke_2
- ___87-[CPLProxyLibraryManager getCloudCacheForRecordWithScopedIdentifier:completionHandler:]_block_invoke_3
- ___91-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke
- ___91-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke_2
- ___91-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke_3
- ___91-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke_4
- ___91-[CPLProxyLibraryManager requestClientToPullAllChangesInScopeIdentifier:completionHandler:]_block_invoke_5
- ___98-[CPLLibraryManager beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke_2
- ___98-[CPLLibraryManager beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:]_block_invoke_2
- ____CPLConfigurationOSLogDomain_block_invoke.18725
- ____CPLForceSyncOSLogDomain_block_invoke.20119
- ____CPLSchedulerOSLogDomain_block_invoke.7033
- ____CPLSessionOSLogDomain_block_invoke.15648
- ____CPLSessionOSLogDomain_block_invoke.17502
- ____CPLSessionOSLogDomain_block_invoke.22000
- ____CPLStorageOSLogDomain_block_invoke.10568
- ____CPLStorageOSLogDomain_block_invoke.10653
- ____CPLStorageOSLogDomain_block_invoke.13942
- ____CPLStorageOSLogDomain_block_invoke.17091
- ____CPLStorageOSLogDomain_block_invoke.19456
- ____CPLStorageOSLogDomain_block_invoke.1958
- ____CPLStorageOSLogDomain_block_invoke.19746
- ____CPLStorageOSLogDomain_block_invoke.20732
- ____CPLStorageOSLogDomain_block_invoke.21380
- ____CPLStorageOSLogDomain_block_invoke.21637
- ____CPLStorageOSLogDomain_block_invoke.5804
- ____CPLStorageOSLogDomain_block_invoke.7307
- ____CPLStorageOSLogDomain_block_invoke.8018
- ____CPLStorageOSLogDomain_block_invoke.8457
- ____CPLStorageOSLogDomain_block_invoke.8621
- ____CPLStorageOSLogDomain_block_invoke.8812
- ____CPLStorageOSLogDomain_block_invoke.912
- ____CPLStoreOSLogDomain_block_invoke.2860
- ____CPLTaskOSLogDomain_block_invoke.10870
- ____CPLTaskOSLogDomain_block_invoke.1313
- ____CPLTaskOSLogDomain_block_invoke.13395
- ____CPLTaskOSLogDomain_block_invoke.13845
- ____CPLTaskOSLogDomain_block_invoke.14916
- ____CPLTaskOSLogDomain_block_invoke.16426
- ____CPLTaskOSLogDomain_block_invoke.20566
- ____CPLTaskOSLogDomain_block_invoke.22333
- ____CPLTaskOSLogDomain_block_invoke.23413
- ____CPLTaskOSLogDomain_block_invoke.2489
- ____CPLTaskOSLogDomain_block_invoke.5140
- ____CPLTaskOSLogDomain_block_invoke.6639
- ___block_descriptor_112_e8_32s40s48s56s64s72s80r88r_e32_v32?0"CPLRecordChange"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e45_v32?0"CPLScopedIdentifier"8"NSString"16#24l
- ___block_descriptor_64_e8_32s40s48s56bs_e47_v24?0"_CPLResourcesMutableArray"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56r64r_e46_v32?0"CPLScopedIdentifier"8"NSString"16^B24l
- __block_literal_global.1014
- __block_literal_global.10200
- __block_literal_global.104.18235
- __block_literal_global.10411
- __block_literal_global.1052
- __block_literal_global.1055
- __block_literal_global.10564
- __block_literal_global.10649
- __block_literal_global.108.18236
- __block_literal_global.10866
- __block_literal_global.110.20267
- __block_literal_global.1154
- __block_literal_global.117.20268
- __block_literal_global.11765
- __block_literal_global.12030
- __block_literal_global.12549
- __block_literal_global.128
- __block_literal_global.13391
- __block_literal_global.1354
- __block_literal_global.13638
- __block_literal_global.13875
- __block_literal_global.13936
- __block_literal_global.14.13876
- __block_literal_global.14.5994
- __block_literal_global.14.8858
- __block_literal_global.140
- __block_literal_global.14100
- __block_literal_global.1436
- __block_literal_global.144
- __block_literal_global.146.12526
- __block_literal_global.14623
- __block_literal_global.14643
- __block_literal_global.14707
- __block_literal_global.148.20270
- __block_literal_global.148.20562
- __block_literal_global.14912
- __block_literal_global.151
- __block_literal_global.1516
- __block_literal_global.15451
- __block_literal_global.15665
- __block_literal_global.158.8923
- __block_literal_global.16197
- __block_literal_global.1645
- __block_literal_global.16536
- __block_literal_global.1658
- __block_literal_global.1672
- __block_literal_global.1674
- __block_literal_global.1676
- __block_literal_global.1679
- __block_literal_global.1681
- __block_literal_global.1683
- __block_literal_global.1685.5404
- __block_literal_global.16881
- __block_literal_global.17087
- __block_literal_global.171.20271
- __block_literal_global.1721
- __block_literal_global.1723
- __block_literal_global.1731
- __block_literal_global.1739
- __block_literal_global.1741
- __block_literal_global.1746
- __block_literal_global.1748
- __block_literal_global.17514
- __block_literal_global.17692
- __block_literal_global.177.20272
- __block_literal_global.17829
- __block_literal_global.17937
- __block_literal_global.181
- __block_literal_global.1814
- __block_literal_global.18352
- __block_literal_global.186
- __block_literal_global.18721
- __block_literal_global.1896
- __block_literal_global.19101
- __block_literal_global.19452
- __block_literal_global.1954
- __block_literal_global.19620
- __block_literal_global.19742
- __block_literal_global.2.23684
- __block_literal_global.20264
- __block_literal_global.20585
- __block_literal_global.20728
- __block_literal_global.20889
- __block_literal_global.21376
- __block_literal_global.21633
- __block_literal_global.21793
- __block_literal_global.21996
- __block_literal_global.22.7437
- __block_literal_global.2212
- __block_literal_global.22385
- __block_literal_global.22946
- __block_literal_global.23089
- __block_literal_global.23161
- __block_literal_global.23557
- __block_literal_global.2364
- __block_literal_global.23678
- __block_literal_global.23798
- __block_literal_global.23987
- __block_literal_global.2419
- __block_literal_global.2485
- __block_literal_global.250
- __block_literal_global.263.14382
- __block_literal_global.27.15685
- __block_literal_global.281
- __block_literal_global.2844
- __block_literal_global.287
- __block_literal_global.29
- __block_literal_global.3.3331
- __block_literal_global.301
- __block_literal_global.304
- __block_literal_global.3086
- __block_literal_global.310
- __block_literal_global.32.21761
- __block_literal_global.322.22329
- __block_literal_global.3338
- __block_literal_global.354
- __block_literal_global.3555
- __block_literal_global.37.7441
- __block_literal_global.3763
- __block_literal_global.402
- __block_literal_global.41
- __block_literal_global.4184
- __block_literal_global.42.18274
- __block_literal_global.42.7443
- __block_literal_global.431
- __block_literal_global.4321
- __block_literal_global.4478
- __block_literal_global.45
- __block_literal_global.47.7445
- __block_literal_global.49
- __block_literal_global.4906
- __block_literal_global.4993
- __block_literal_global.5136
- __block_literal_global.5294
- __block_literal_global.53
- __block_literal_global.5412
- __block_literal_global.549
- __block_literal_global.552
- __block_literal_global.57.7448
- __block_literal_global.5800
- __block_literal_global.6000
- __block_literal_global.6275
- __block_literal_global.637
- __block_literal_global.6635
- __block_literal_global.6747
- __block_literal_global.7148
- __block_literal_global.7432
- __block_literal_global.750
- __block_literal_global.77.15446
- __block_literal_global.8.23694
- __block_literal_global.8124
- __block_literal_global.8345
- __block_literal_global.8453
- __block_literal_global.850
- __block_literal_global.853
- __block_literal_global.8555
- __block_literal_global.856
- __block_literal_global.859
- __block_literal_global.86.16156
- __block_literal_global.8860
- __block_literal_global.899
- __block_literal_global.9040
- __block_literal_global.908
- __block_literal_global.92
- __block_literal_global.9297
- __block_literal_global.9517
- __block_literal_global.9818
- __cpl_dispatch_async_block_invoke.10820
- __cpl_dispatch_async_block_invoke.11449
- __cpl_dispatch_async_block_invoke.1315
- __cpl_dispatch_async_block_invoke.13400
- __cpl_dispatch_async_block_invoke.13761
- __cpl_dispatch_async_block_invoke.13837
- __cpl_dispatch_async_block_invoke.14994
- __cpl_dispatch_async_block_invoke.15978
- __cpl_dispatch_async_block_invoke.16481
- __cpl_dispatch_async_block_invoke.16832
- __cpl_dispatch_async_block_invoke.17322
- __cpl_dispatch_async_block_invoke.1735
- __cpl_dispatch_async_block_invoke.17825
- __cpl_dispatch_async_block_invoke.18700
- __cpl_dispatch_async_block_invoke.19978
- __cpl_dispatch_async_block_invoke.20517
- __cpl_dispatch_async_block_invoke.20897
- __cpl_dispatch_async_block_invoke.22335
- __cpl_dispatch_async_block_invoke.23458
- __cpl_dispatch_async_block_invoke.6214
- __cpl_dispatch_async_block_invoke.6619
- __cpl_dispatch_async_block_invoke.674
- __cpl_dispatch_async_block_invoke.6885
- __cpl_dispatch_async_block_invoke.7315
- __cpl_dispatch_async_block_invoke.9149
- __cpl_dispatch_async_block_invoke.9493
- _doProtected:.onceToken.14642
- _fmod
- _objc_msgSend$_doesScopeContributeToAssetCounts:
- _objc_msgSend$_updateAssetCountsWithScopeChange:forScope:
- _objc_msgSend$addTransportScope:forScopeWithIdentifier:
- _objc_msgSend$alwaysCreateEPPMomentShares
- _objc_msgSend$fingerprintSchemeForNewMasterAsset
- _objc_msgSend$getCloudCacheForRecordWithScopedIdentifier:completionHandler:
- _objc_msgSend$initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:provider:
- _objc_msgSend$initWithFingerprintSchemeV1:fingerprintSchemeV2:usesMMCSv2AsDefault:
- _objc_msgSend$initWithObject:selector:
- _objc_msgSend$isMMCSv1SignatureBytes:
- _objc_msgSend$isMMCSv1SignatureBytesKnownNotMMCSv2:
- _objc_msgSend$isMMCSv2SignatureBytes:
- _objc_msgSend$isValidSignatureBytes:
- _objc_msgSend$mmcsv1FingerprintScheme
- _objc_msgSend$requestClientToPullAllChangesInScopeIdentifier:completionHandler:
- _objc_msgSend$setMasterFingerprint:
- _objc_msgSend$setSharedScopeIdentifier:forScopeWithIdentifier:
- _objc_msgSend$shouldSetSharedScopeIdentifierForScopeWithIdentifier:
- _objc_msgSend$usesMMCSv2AsDefault
- _objc_msgSend$usesMMCSv2AsDefaultInUniverseName:
- _statusDidChange.11656
- copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18258
- initWithCPLArchiver:.onceToken.1899
- initWithCPLArchiver:.stringClass.1900
- initWithCoder:.logOnceToken.19622
- initWithCoder:.onceToken.10139
- initWithCoder:.onceToken.13637
- initWithCoder:.onceToken.17513
- initWithCoder:.onceToken.19619
- initWithCoder:.onceToken.21792
- initWithCoder:.onceToken.23986
- initWithCoder:.onceToken.4885
- initWithCoder:.onceToken.4992
- initWithCoder:.onceToken.5993
- initWithCoder:.pushContextsClasses.21794
- initWithCoder:.stringClass.10140
- propertiesForChangeType:.onceToken.14462
- propertiesForChangeType:.onceToken.174
- propertiesForChangeType:.onceToken.179
- propertiesForChangeType:.onceToken.18273
- propertiesForChangeType:.onceToken.23088
- propertiesForChangeType:.properties.23090
CStrings:
+ "%@ has an invalid fingerprint scheme"
+ "%@ is trying to begin a session twice"
+ "%@ saving CPLStatus %p (changed keys: %{public}@) to %@: %@"
+ "%@()"
+ "%ld (%@ + 0x%lx)"
+ "%ld (%@)"
+ "%s[%@ %@]"
+ "%{public}@ completed in %.3fs"
+ "%{public}@ has not completed after %.0fs"
+ ".icloud.com"
+ "/%@"
+ "/%@/%@"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBackgroundActivity.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBeforeUploadCheckItems.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBrokenScope.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineLibrary.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineScheduler.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSystemMonitor.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineTransport.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLFileWatcher.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleChangesTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleUtility.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLNetworkWatcher.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPowerAssertion.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLProcessStagedScopesTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPullFromTransportTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPushToTransportTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLScopeUpdateTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncSession.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncStep.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransaction.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransportScopeMapping.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadPushedChangesTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLEngineFeedbackManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLFeedbackMessage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStep.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStrategy.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeBatchChangeStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeSessionUpdate.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangedRecordStorageView.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLClientCacheView_Extensions.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineCloudCache.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineFileStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineIDMapping.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineOutgoingResources.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEnginePushRepository.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceDownloadQueue.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScope.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScopeStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorageViews.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStore.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepository.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepositoryBatchStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLExtractedBatch.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLFeature.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLRecordStorageView.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLSharedBatchStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesAccumulator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAlbumChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLArchiver.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAssetChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeBatch.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeSession.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfigurationDictionary.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLContainerChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLErrors.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceAnalysisReference.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceCropChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintContext.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintScheme.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLForceSyncTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLItemChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLMasterChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPersonChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPlatform.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPullChangeSession.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushChangeSession.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushSessionTracker.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordTarget.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResource.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceIdentity.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceTransferTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopeChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopedIdentifier.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSocialGroupChange.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLStatus.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/NSObject+CPLCodingProxy.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxyLibraryManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxySession.m"
+ "<%@ %ld/%ld/%ld>"
+ "@\"CPLFingerprintContext\""
+ "@\"CPLFingerprintContext\"16@0:8"
+ "@40@0:8@16:24@32"
+ "@64@0:8@16@24q32Q40@48@56"
+ "Account capability is %{public}@ (%{public}@) - switching EPP enabled to %@"
+ "Asset for %@ has been stashed - stashing changes"
+ "B52@0:8@16B24#28@36^@44"
+ "BeforePushSession"
+ "Beginning change session for %@"
+ "Blocking change session for %@ until %@ is done"
+ "CPLAlwaysAutoEnableEPP"
+ "CPLDisableEPPCapabilityCheck"
+ "CPLDisableInvalidFingerprintScheme"
+ "CPLEPPEnabled"
+ "CPLEPPEnabledSource"
+ "CPLForceEPPSupport"
+ "CPLUseRealBoundaryKey"
+ "Change session for %@ has been ended before it even began"
+ "Client pushed %@ changing from %@ to %@"
+ "Client pushed a record with mismatched fingerprint scheme resources %@: %@"
+ "CloudPhotoLibrary-751.0.104"
+ "Derivative generation error is transient, will retry: %@"
+ "EPP"
+ "EPPAutoEnable"
+ "EPPCapable"
+ "Ending change session for %@"
+ "Ending unknown change session for %@"
+ "Error trying to generate derivatives for unsupported input video from %@: %@"
+ "Failed to refresh boundary key for %{public}@: %@"
+ "Invalid fingerprint scheme"
+ "Invalid fingerprint scheme for %@ (related identifier '%{public}@')"
+ "Open"
+ "PCSGetAppBoundaryKey"
+ "Photos"
+ "PullSession"
+ "PushSession"
+ "Refreshing boundary key for %{public}@"
+ "Rejecting %@ as it changes from %@ to %@"
+ "Requesting update of %@ for Account EPP capability"
+ "Resuming change session for %@"
+ "Successfully refreshed boundary key for %{public}@"
+ "T@\"CPLFingerprintContext\",R,N"
+ "T@\"CPLFingerprintContext\",R,N,V_fingerprintContext"
+ "T@\"CPLFingerprintSchemeV1\",R,V_mmcsv1FingerprintScheme"
+ "T@\"CPLFingerprintSchemeV2\",R,V_mmcsv2FingerprintScheme"
+ "T@\"NSData\",C"
+ "T@\"NSDate\",C,N,V_userModificationDate"
+ "T@\"NSString\",&,N,V_masterIdentifier"
+ "TB,R,N,V_shouldCheckEPPCapability"
+ "TB,R,V_usesMMCSv2AsDefault"
+ "Trying to refresh fingerprint context while the library is not open"
+ "Trying to use %@ with an invalid fingerprint scheme"
+ "Unable to find master %@ to stash"
+ "_addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "_beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
+ "_beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
+ "_callDescription"
+ "_concreteScopeMapping"
+ "_currentChangeSessionToken"
+ "_doesScopeContributeToGlobalStatus:"
+ "_fetchBoundaryKeyIfNecessaryWithSource:completionHandler:"
+ "_fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:"
+ "_fingerprintContext"
+ "_fixGlobalStatus"
+ "_forManagement"
+ "_functionName"
+ "_hasFetchedBoundaryKey"
+ "_isMMCSv2"
+ "_pendingChangeSessionCompletionHandler"
+ "_pendingChangeSessionToken"
+ "_requestUpdateOfMainScopeFromTransport"
+ "_scopeMapping"
+ "_serverFeatureCompatibleVersionToUpdate"
+ "_shouldCheckEPPCapability"
+ "_shouldUpdateGlobalStatusAtEndOfTransaction"
+ "_updateFingerprintContext"
+ "_updateGlobalStatusWithScopeChange:forScope:"
+ "_userModificationDate"
+ "_willNeedToAccessScopeWithIdentifier:error:"
+ "accountEPPCapability"
+ "accountEPPCapabilityMaximum"
+ "addConcreteScope:forScope:"
+ "addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
+ "addTransportScope:forScope:"
+ "beginChangeSessionWithSessionToken:completionHandler:"
+ "boundaryKeyDescription"
+ "capable"
+ "changing asset from %@ to %@"
+ "clientFeatureCompatibleVersion = %@"
+ "com.apple.cpl.hashed-boundary-key"
+ "com.apple.photos.client-side-encryption-manager"
+ "deactivated-engine"
+ "defaultAccountEPPCapabilityInUniverseName:"
+ "defaults"
+ "descriptionForAccountEPPCapability:"
+ "descriptionForSupportedFeatureCompatibleVersion:"
+ "disableBoundaryKeyFetching"
+ "disabled-features"
+ "endChangeSessionWithSessionToken:"
+ "epp-assets"
+ "epp.auto-enable"
+ "epp.capability-check"
+ "fingerprintContextIfKnown"
+ "getBytes:length:"
+ "getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:"
+ "hardcoded"
+ "hasMasterIdentifier"
+ "https"
+ "initForMMCSv2:"
+ "initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:fingerprintContext:provider:"
+ "initWithFingerprintSchemeV1:fingerprintSchemeV2:"
+ "initWithObject:selector:functionName:"
+ "initWithSuiteName:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "isCompatibleWithFingerprintScheme:"
+ "isEPPRecord"
+ "isStableHash:"
+ "isTransientDerivativeGenerationError:"
+ "isValidFingerprint:"
+ "maximumAccountEPPCapability"
+ "not-capable"
+ "observeAsyncCallWithFunction:block:"
+ "observeSyncCallWithFunction:block:"
+ "pathComponents"
+ "performUpgradeWithError:"
+ "providesEnhancedPrivacy"
+ "realStableHash"
+ "record %@ is not known to cloud cache"
+ "redacted"
+ "redacted."
+ "refreshBoundaryKeyWithSource:completionHandler:"
+ "removeRelatedRecordsFromQuarantineWithError:"
+ "requestClientToPullAllChangesInScopeIdentifiers:completionHandler:"
+ "scheme"
+ "scopeForScopeIdentifier:"
+ "session has been superseded"
+ "setAccountEPPCapability:"
+ "setBool:forKey:"
+ "setBoundaryKey:"
+ "setHasUpdatedScope:fromTransportWithError:"
+ "setHost:"
+ "setPath:"
+ "setScheme:"
+ "setUserModificationDate:"
+ "setupFingerprintContextForTests"
+ "share.icloud.com"
+ "shared-library"
+ "shouldCheckEPPCapability"
+ "shouldDisableEPP"
+ "storeVersionHasChanged"
+ "supportedFeatureCompatibleVersion"
+ "supportsEPPAutoEnable"
+ "umod"
+ "unsupported"
+ "updateWithAccountEPPCapability:source:"
+ "updateWithStatus:configuration:"
+ "userModificationDate"
+ "v36@?0@\"CPLScopedIdentifier\"8B16@\"NSString\"20#28"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "willBeginPushSession"
+ "www.icloud.com"
+ "\xf0\xe1"
- "%@ saving CPLStatus %p (changed keys: %@) to %@: %@"
- "%s[%{public}@ %{public}@] completed in %.3fs"
- "%s[%{public}@ %{public}@] has not completed after %.0fs"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBackgroundActivity.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBeforeUploadCheckItems.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBrokenScope.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineLibrary.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineScheduler.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSystemMonitor.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineTransport.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLFileWatcher.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleChangesTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleUtility.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLNetworkWatcher.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPowerAssertion.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLProcessStagedScopesTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPullFromTransportTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPushToTransportTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLScopeUpdateTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncSession.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncStep.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransaction.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransportScopeMapping.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadPushedChangesTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLEngineFeedbackManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLFeedbackMessage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStep.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStrategy.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeBatchChangeStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeSessionUpdate.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangedRecordStorageView.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLClientCacheView_Extensions.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineCloudCache.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineFileStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineIDMapping.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineOutgoingResources.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEnginePushRepository.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceDownloadQueue.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScope.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScopeStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorageViews.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStore.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepository.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepositoryBatchStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLExtractedBatch.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLFeature.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLRecordStorageView.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLSharedBatchStorage.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesAccumulator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAlbumChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLArchiver.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAssetChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeBatch.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeSession.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfiguration.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfigurationDictionary.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLContainerChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLErrors.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceAnalysisReference.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceCropChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintContext.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintScheme.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLForceSyncTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLItemChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLMasterChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPersonChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPlatform.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPullChangeSession.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushChangeSession.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushSessionTracker.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordTarget.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResource.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceIdentity.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceTransferTask.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopeChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopedIdentifier.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSocialGroupChange.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLStatus.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/NSObject+CPLCodingProxy.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxyLibraryManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxySession.m"
- "<%@ %@ %ld/%ld/%ld>"
- "@32@0:8@16:24"
- "@56@0:8@16@24q32Q40@48"
- "B24@0:8r^v16"
- "CPLForceMMCSv2Support"
- "CloudPhotoLibrary-741.0.130"
- "Error trying to generate unsupported video derivatives from %@"
- "No error but no transport scope available for %@"
- "T@\"CPLFingerprintSchemeV1\",R,N,V_mmcsv1FingerprintScheme"
- "T@\"CPLFingerprintSchemeV2\",R,N,V_mmcsv2FingerprintScheme"
- "T@\"NSString\",&,N,V_masterFingerprint"
- "TB,R,N,V_usesMMCSv2AsDefault"
- "Trying to compute stable hash for master without a fingerprint"
- "Trying to user %@ with an invalid fingerprint scheme"
- "^{os_unfair_lock_s=I}"
- "_doesScopeContributeToAssetCounts:"
- "_isUsingFingerprintSchemeSubclasses"
- "_masterFingerprint"
- "_sharedScopeIdentifierMapping"
- "_shouldUpdateAssetCountsAtEndOfTransaction"
- "_updateAssetCountsWithScopeChange:forScope:"
- "addConcreteScope:forScopeWithIdentifier:"
- "addTransportScope:forScopeWithIdentifier:"
- "clientFeatureCompatibleVersion = %ld"
- "defaultFingerprintSchemeForUnknownRecord"
- "hasMasterFingerprint"
- "https://redacted.icloud.com/photos"
- "initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:provider:"
- "initWithBoundaryKey:usesMMCSv2AsDefault:"
- "initWithFingerprintSchemeV1:fingerprintSchemeV2:usesMMCSv2AsDefault:"
- "initWithObject:selector:"
- "isMMCSv1SignatureBytes:"
- "isMMCSv1SignatureBytesKnownNotMMCSv2:"
- "isMMCSv2SignatureBytes:"
- "isValidSignatureBytes:"
- "masterFingerprint"
- "requestClientToPullAllChangesInScopeIdentifier:completionHandler:"
- "setMasterFingerprint:"
- "setSharedScopeIdentifier:forScopeWithIdentifier:"
- "sharedScopeIdentifierForScopeWithIdentifier:"
- "shouldSetSharedScopeIdentifierForScopeWithIdentifier:"
- "stableHashForMasterWithManager:"
- "usesMMCSv2AsDefaultInUniverseName:"
- "v32@0:8@\"CPLScopedIdentifier\"16@?<v@?@\"CPLRecordChange\"@\"NSError\">24"
- "v32@?0@\"CPLScopedIdentifier\"8@\"NSString\"16#24"
- "\xf0\xb1"

```
