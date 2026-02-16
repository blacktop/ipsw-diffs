## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-784.82.1.0.0
-  __TEXT.__text: 0x6cb74
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x4310
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xefcb
-  __TEXT.__oslogstring: 0x7e48
-  __TEXT.__gcc_except_tab: 0x1e90
+787.100.20.502.1
+  __TEXT.__text: 0x72a48
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x4568
+  __TEXT.__const: 0xf8
+  __TEXT.__cstring: 0xf8b3
+  __TEXT.__oslogstring: 0x8286
+  __TEXT.__gcc_except_tab: 0x1fe8
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1890
-  __TEXT.__objc_classname: 0x92d
-  __TEXT.__objc_methname: 0xb307
-  __TEXT.__objc_methtype: 0x252c
-  __TEXT.__objc_stubs: 0x6380
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x1c10
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__unwind_info: 0x1a08
+  __TEXT.__objc_classname: 0xa07
+  __TEXT.__objc_methname: 0xb815
+  __TEXT.__objc_methtype: 0x26a4
+  __TEXT.__objc_stubs: 0x6580
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x1cf0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21a0
+  __DATA_CONST.__objc_selrefs: 0x2268
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_arraydata: 0x120
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5b80
-  __AUTH_CONST.__objc_const: 0xb3e0
-  __AUTH_CONST.__objc_intobj: 0x2e8
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x22c
-  __DATA.__data: 0x9c8
-  __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0xf00
+  __AUTH_CONST.__cfstring: 0x5d60
+  __AUTH_CONST.__objc_const: 0xbf38
+  __AUTH_CONST.__objc_intobj: 0x330
+  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x238
+  __DATA.__data: 0xa88
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5ACACA95-962E-306D-8D35-CC8680152B87
-  Functions: 2018
-  Symbols:   6684
-  CStrings:  4282
+  UUID: 044A7171-8EEF-3B92-8CAC-1F85B85A817B
+  Functions: 2131
+  Symbols:   7044
+  CStrings:  4397
 
Symbols:
+ +[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]
+ +[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:].cold.1
+ +[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]
+ +[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:].cold.1
+ +[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]
+ +[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:].cold.1
+ +[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]
+ +[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:].cold.1
+ +[IXAppInstallCoordinator(IXTesting) fetchDuplicatedClassInfoWithError:]
+ +[IXFeatureFlags osAppMigrationEnabled]
+ +[IXFeatureFlags scheduledUpdatesEnabled]
+ +[IXRootContentOperationOptions supportsSecureCoding]
+ +[IXUpdatingDemotedAppInstallCoordinator intent]
+ -[IXLSApplicationRecordEnumerator _enumerateApplicationRecordsOnModuleAtURL:enumeratorBlock:error:]
+ -[IXLSApplicationRecordEnumerator _enumerateApplicationRecordsOnModuleAtURL:enumeratorBlock:error:].cold.1
+ -[IXLSApplicationRecordEnumerator bundleIDsForModuleAtURL:error:]
+ -[IXRootContentOperationOptions copyWithZone:]
+ -[IXRootContentOperationOptions deferUntilNextBoot]
+ -[IXRootContentOperationOptions description]
+ -[IXRootContentOperationOptions encodeWithCoder:]
+ -[IXRootContentOperationOptions hash]
+ -[IXRootContentOperationOptions initWithCoder:]
+ -[IXRootContentOperationOptions init]
+ -[IXRootContentOperationOptions isEqual:]
+ -[IXRootContentOperationOptions setDeferUntilNextBoot:]
+ -[IXTerminationAssertion acquireWithCompletion:]
+ -[IXTerminationAssertion acquireWithCompletion:].cold.1
+ -[IXTerminationAssertion acquireWithError:]
+ -[IXTerminationAssertion acquisitionBlock]
+ -[IXTerminationAssertion initWithBundleID:description:terminationResistance:]
+ -[IXTerminationAssertion initWithBundleID:description:terminationResistance:allowLaunchPredicate:]
+ -[IXTerminationAssertion initWithBundleID:description:terminationResistance:allowLaunchPredicate:creationBlock:]
+ -[IXTerminationAssertion initWithBundleIDs:description:terminationResistance:]
+ -[IXTerminationAssertion initWithBundleIDs:description:terminationResistance:allowLaunchPredicate:]
+ -[IXTerminationAssertion initWithBundleIDs:description:terminationResistance:allowLaunchPredicate:creationBlock:]
+ -[IXTerminationAssertion invalidate].cold.1
+ -[IXTerminationAssertion isEqual:]
+ -[IXTerminationAssertion setAcquisitionBlock:]
+ -[IXTerminationAssertion setTerminationAssertion:]
+ -[IXTerminationAssertion terminationAssertion]
+ -[IXUnregisterOSModuleToken applicationEnumerator]
+ -[IXUnregisterOSModuleToken initWithModuleURL:options:applicationEnumerator:terminationAssertionCreationBlock:]
+ -[IXUnregisterOSModuleToken invalidate].cold.1
+ -[IXUnregisterOSModuleToken setApplicationEnumerator:]
+ -[IXUnregisterOSModuleToken setTerminationAssertionCreationBlock:]
+ -[IXUnregisterOSModuleToken terminationAssertionCreationBlock]
+ -[IXUpdatingDemotedAppInstallCoordinator validInstallTypes]
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table439
+ _CacheDeleteCopyPurgeableSpaceWithInfo
+ _CacheDeletePurgeSpaceWithInfo
+ _CacheDeletePurgeSpaceWithInfoSync
+ _IXAppURLFromExtractedPayloadDir
+ _IXAppURLFromExtractedPayloadDir.cold.1
+ _IXCopyAppRemovabilityDictionary
+ _IXCopyAppRemovabilityDictionary.cold.1
+ _IXCopyAppRemovabilityDictionary.cold.2
+ _IXCopyDuplicatedClassInfo
+ _IXCopyLegacyRemovabilityStorageURL
+ _IXCopyLegacyRemovabilityStorageURL.cold.1
+ _IXCopyRemovabilityStorageWithoutChangeClockURL
+ _IXCopyRemovabilityStorageWithoutChangeClockURL.cold.1
+ _IXCopySerializedAppRemovabilityData
+ _IXCopySerializedAppRemovabilityData.cold.1
+ _IXCopySerializedAppRemovabilityDataWithoutChangeClock
+ _IXCopySerializedAppRemovabilityDataWithoutChangeClock.cold.1
+ _IXLoadInfoPlistFromBundle
+ _IXLoadInfoPlistFromBundle.cold.1
+ _IXLoadInfoPlistFromBundle.cold.2
+ _IXLoadInfoPlistFromBundle.cold.3
+ _IXLoadInfoPlistFromBundleAtURL
+ _IXLoadInfoPlistFromBundleAtURL.cold.1
+ _IXPreflightWithCacheDelete
+ _IXSetLegacyRemovabilityStorageURLOverride
+ _IXSetRemovabilityStorageWithoutChangeClockURLOverride
+ _NSHashGet
+ _NSHashInsertKnownAbsent
+ _OBJC_CLASS_$_IXFeatureFlags
+ _OBJC_CLASS_$_IXLSApplicationRecordEnumerator
+ _OBJC_CLASS_$_IXRootContentOperationOptions
+ _OBJC_CLASS_$_IXUpdatingDemotedAppInstallCoordinator
+ _OBJC_IVAR_$_IXRootContentOperationOptions._deferUntilNextBoot
+ _OBJC_IVAR_$_IXTerminationAssertion._acquisitionBlock
+ _OBJC_IVAR_$_IXTerminationAssertion._terminationAssertion
+ _OBJC_IVAR_$_IXUnregisterOSModuleToken._applicationEnumerator
+ _OBJC_IVAR_$_IXUnregisterOSModuleToken._terminationAssertionCreationBlock
+ _OBJC_METACLASS_$_IXFeatureFlags
+ _OBJC_METACLASS_$_IXLSApplicationRecordEnumerator
+ _OBJC_METACLASS_$_IXRootContentOperationOptions
+ _OBJC_METACLASS_$_IXUpdatingDemotedAppInstallCoordinator
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ __CopyRemovabilityData
+ __CreateTerminationAssertionWithPredicate
+ __ExtractObjectsFromDeserializedRemovabilityPlist
+ __ExtractObjectsFromDeserializedRemovabilityPlist.cold.1
+ __ExtractObjectsFromDeserializedRemovabilityPlist.cold.2
+ __ExtractObjectsFromDeserializedRemovabilityPlist.cold.3
+ __ExtractObjectsFromDeserializedRemovabilityPlist.cold.4
+ __ExtractObjectsFromDeserializedRemovabilityPlist.cold.5
+ __ExtractObjectsFromDeserializedRemovabilityPlist.cold.6
+ __GatherBundleIDsFromSetOfBundles
+ __GatherBundleIDsFromSetOfBundles.cold.1
+ __IXCreateError
+ __IXCreateErrorV
+ __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXRootContentRegistration|IXSimpleInstaller|IXSimpleInstallerPrivate|IXOSModuleRegistration|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
+ __OBJC_$_CLASS_METHODS_IXFeatureFlags
+ __OBJC_$_CLASS_METHODS_IXRootContentOperationOptions
+ __OBJC_$_CLASS_METHODS_IXUpdatingDemotedAppInstallCoordinator
+ __OBJC_$_CLASS_PROP_LIST_IXFeatureFlags
+ __OBJC_$_CLASS_PROP_LIST_IXRootContentOperationOptions
+ __OBJC_$_INSTANCE_METHODS_IXLSApplicationRecordEnumerator
+ __OBJC_$_INSTANCE_METHODS_IXRootContentOperationOptions
+ __OBJC_$_INSTANCE_METHODS_IXUpdatingDemotedAppInstallCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_IXRootContentOperationOptions
+ __OBJC_$_PROP_LIST_IXLSApplicationRecordEnumerator
+ __OBJC_$_PROP_LIST_IXRootContentOperationOptions
+ __OBJC_$_PROP_LIST_IXUpdatingDemotedAppInstallCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IXApplicationRecordEnumeratorProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IXTerminationAssertionWrapperProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IXApplicationRecordEnumeratorProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IXTerminationAssertionWrapperProtocol
+ __OBJC_$_PROTOCOL_REFS_IXApplicationRecordEnumeratorProtocol
+ __OBJC_$_PROTOCOL_REFS_IXTerminationAssertionWrapperProtocol
+ __OBJC_CLASS_PROTOCOLS_$_IXLSApplicationRecordEnumerator
+ __OBJC_CLASS_PROTOCOLS_$_IXRootContentOperationOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXUpdatingDemotedAppInstallCoordinator
+ __OBJC_CLASS_RO_$_IXFeatureFlags
+ __OBJC_CLASS_RO_$_IXLSApplicationRecordEnumerator
+ __OBJC_CLASS_RO_$_IXRootContentOperationOptions
+ __OBJC_CLASS_RO_$_IXUpdatingDemotedAppInstallCoordinator
+ __OBJC_LABEL_PROTOCOL_$_IXApplicationRecordEnumeratorProtocol
+ __OBJC_LABEL_PROTOCOL_$_IXTerminationAssertionWrapperProtocol
+ __OBJC_METACLASS_RO_$_IXFeatureFlags
+ __OBJC_METACLASS_RO_$_IXLSApplicationRecordEnumerator
+ __OBJC_METACLASS_RO_$_IXRootContentOperationOptions
+ __OBJC_METACLASS_RO_$_IXUpdatingDemotedAppInstallCoordinator
+ __OBJC_PROTOCOL_$_IXApplicationRecordEnumeratorProtocol
+ __OBJC_PROTOCOL_$_IXTerminationAssertionWrapperProtocol
+ __StringFromClassName
+ ___100+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]_block_invoke
+ ___100+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]_block_invoke.13
+ ___100+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]_block_invoke.13.cold.1
+ ___100+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]_block_invoke.cold.1
+ ___102+[IXAppInstallCoordinator cancelCoordinatorsForAppsWithApplicationIdentities:withReason:client:error:]_block_invoke.76
+ ___103+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke
+ ___103+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke.9
+ ___103+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke.9.cold.1
+ ___103+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke_2
+ ___103+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke_2.cold.1
+ ___105+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke
+ ___105+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke.14
+ ___105+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke.14.cold.1
+ ___105+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke_2
+ ___105+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke_2.cold.1
+ ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.703
+ ___107+[IXAppInstallCoordinator cancelCoordinatorsForAppsWithApplicationIdentities:withReason:client:completion:]_block_invoke.79
+ ___32-[IXAppInstallCoordinator error]_block_invoke.289
+ ___32-[IXAppInstallCoordinator error]_block_invoke_2.290
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.294
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.306
+ ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.307
+ ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.308
+ ___43-[IXTerminationAssertion acquireWithError:]_block_invoke
+ ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.317
+ ___44-[IXAppInstallCoordinator hasInstallOptions]_block_invoke.217
+ ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.199
+ ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.249
+ ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.309
+ ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.696
+ ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.221
+ ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.310
+ ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.220
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.291
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.292
+ ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.189
+ ___48-[IXTerminationAssertion acquireWithCompletion:]_block_invoke
+ ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.286
+ ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.280
+ ___51-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke.218
+ ___51-[IXAppInstallCoordinator setInstallOptions:error:]_block_invoke.216
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.191
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.191.cold.1
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.191.cold.2
+ ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.190
+ ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.240
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.241
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.241.cold.1
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.241.cold.2
+ ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.283
+ ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.239
+ ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.288
+ ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.250
+ ___55-[IXAppInstallCoordinator dataImportPromisesWithError:]_block_invoke.272
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.177
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.177.cold.1
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.177.cold.2
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.251
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.251.cold.1
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.251.cold.2
+ ___55-[IXAppInstallCoordinator setDataImportPromises:error:]_block_invoke.271
+ ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.176
+ ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.700
+ ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.163
+ ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.263
+ ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.262
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.706
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.687
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.690
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.694
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.257
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.257.cold.1
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.257.cold.2
+ ___58-[IXAppInstallCoordinator getHasDataImportPromises:error:]_block_invoke.276
+ ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.256
+ ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.279
+ ___59+[IXAppInstallCoordinator defaultAppMetadataListWithError:]_block_invoke.121
+ ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.266
+ ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.282
+ ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.265
+ ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.281
+ ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.255
+ ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.224
+ ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.223
+ ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.261
+ ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.270
+ ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.264
+ ___64+[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]_block_invoke.123
+ ___64+[IXAppInstallCoordinator removabilityForAppWithIdentity:error:]_block_invoke.112
+ ___65+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke.117
+ ___65-[IXLSApplicationRecordEnumerator bundleIDsForModuleAtURL:error:]_block_invoke
+ ___66+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]_block_invoke.119
+ ___68+[IXAppInstallCoordinator pauseCoordinatorForAppWithIdentity:error:]_block_invoke.80
+ ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.200
+ ___69+[IXAppInstallCoordinator removabilityForAppWithIdentity:completion:]_block_invoke.114
+ ___69+[IXAppInstallCoordinator resumeCoordinatorForAppWithIdentity:error:]_block_invoke.81
+ ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.205
+ ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.204
+ ___71+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]_block_invoke.122
+ ___71+[IXAppInstallCoordinator uninstallAppWithIdentity:options:completion:]_block_invoke.107
+ ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.285
+ ___72+[IXAppInstallCoordinator(IXTesting) fetchDuplicatedClassInfoWithError:]_block_invoke
+ ___72+[IXAppInstallCoordinator(IXTesting) fetchDuplicatedClassInfoWithError:]_block_invoke.707
+ ___73+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:error:]_block_invoke.82
+ ___73+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:error:]_block_invoke.113
+ ___73+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke.132
+ ___78+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:completion:]_block_invoke.83
+ ___78+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:completion:]_block_invoke.115
+ ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.697
+ ___79+[IXAppInstallCoordinator updateSINFForAppWithIdentity:sinfData:options:error:]_block_invoke.127
+ ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.686
+ ___81+[IXAppInstallCoordinator revertAppWithIdentity:completionWithApplicationRecord:]_block_invoke.111
+ ___82+[IXAppInstallCoordinator revertAppWithIdentity:resultingApplicationRecord:error:]_block_invoke.109
+ ___82+[IXAppInstallCoordinator setRemovability:forAppWithIdentity:byClient:completion:]_block_invoke.116
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.47
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.51
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.51.cold.1
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.51.cold.2
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.51.cold.3
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.51.cold.4
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.48
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.55
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.60
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.64
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_3.65
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_4.66
+ ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_4.66.cold.1
+ ___85+[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]_block_invoke.155
+ ___87+[IXAppInstallCoordinator cancelCoordinatorForAppWithIdentity:withReason:client:error:]_block_invoke.72
+ ___88+[IXAppInstallCoordinator stagingLocationForInstallLocation:withSandboxExtension:error:]_block_invoke.277
+ ___89+[IXAppInstallCoordinator _synchronouslyEnumerateCoordinatorsForIntent:error:usingBlock:]_block_invoke.71
+ ___92+[IXAppInstallCoordinator cancelCoordinatorForAppWithIdentity:withReason:client:completion:]_block_invoke.75
+ ___98+[IXAppInstallCoordinator uninstallAppWithIdentity:options:disposition:error:legacyProgressBlock:]_block_invoke.97
+ ___98+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]_block_invoke
+ ___98+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]_block_invoke.7
+ ___98+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]_block_invoke.7.cold.1
+ ___98+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]_block_invoke.cold.1
+ ___Block_byref_object_copy_.49
+ ___Block_byref_object_dispose_.50
+ ___IXCopySerializedAppRemovabilityDataWithoutChangeClock_block_invoke
+ ___IXCopySerializedAppRemovabilityData_block_invoke
+ ___IXPreflightWithCacheDelete_block_invoke
+ ____LegacyRemovabilityPListToMetadata_block_invoke
+ ____LegacyRemovabilityPListToMetadata_block_invoke.cold.1
+ ____RemovabilityPListWithoutChangeClockToMetadata_block_invoke
+ ____RemovabilityPListWithoutChangeClockToMetadata_block_invoke.cold.1
+ ____RemovabilityPListWithoutChangeClockToMetadata_block_invoke.cold.2
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e29_v16?0"LSApplicationRecord"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
+ ___block_descriptor_72_e8_32s40bs_e25_v16?0^{__CFDictionary=}8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64w_e17_v16?0"NSError"8ls48l8r56l8s32l8s40l8w64l8
+ ___block_literal_global.692
+ ___block_literal_global.699
+ ___block_literal_global.702
+ __os_feature_enabled_impl
+ __sLegacyRemovabilityStorageURLOverride
+ __sRemovabilityStorageURLWithoutChangeClockOverride
+ _class_getImageName
+ _interface.weakInterface.346
+ _kCFBundleIdentifierKey
+ _objc_copyClassList
+ _objc_msgSend$_enumerateApplicationRecordsOnModuleAtURL:enumeratorBlock:error:
+ _objc_msgSend$_remote_fetchDuplicatedClassInfo:
+ _objc_msgSend$_remote_registerRootContentForBundles:options:completion:
+ _objc_msgSend$_remote_unregisterRootContentForBundles:options:completion:
+ _objc_msgSend$acquireWithCompletion:
+ _objc_msgSend$acquisitionBlock
+ _objc_msgSend$applicationEnumerator
+ _objc_msgSend$bundleIDsForModuleAtURL:error:
+ _objc_msgSend$deferUntilNextBoot
+ _objc_msgSend$initWithBundleID:description:terminationResistance:allowLaunchPredicate:creationBlock:
+ _objc_msgSend$initWithBundleIDs:description:terminationResistance:allowLaunchPredicate:
+ _objc_msgSend$initWithBundleIDs:description:terminationResistance:allowLaunchPredicate:creationBlock:
+ _objc_msgSend$initWithInitialRemovability:client:
+ _objc_msgSend$initWithModuleURL:options:applicationEnumerator:terminationAssertionCreationBlock:
+ _objc_msgSend$initWithPredicate:context:allowLaunch:
+ _objc_msgSend$newClock
+ _objc_msgSend$propertyListRepresentation
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$set
+ _objc_msgSend$setAcquisitionBlock:
+ _objc_msgSend$setDeferUntilNextBoot:
+ _objc_msgSend$terminationAssertionCreationBlock
+ _object_getClassName
+ _statfs
- +[IXAppInstallCoordinator _validatePreconditionForIntent:matchesCurrentInstallStateForBundleID:].cold.3
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.20
- -[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:]
- -[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:].cold.1
- -[IXTerminationAssertion acquireAssertion:]
- -[IXTerminationAssertion acquireAssertion:].cold.1
- -[IXTerminationAssertion assertionTargetProcessDidExit:].cold.1
- -[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:]
- -[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:].cold.1
- -[IXTerminationAssertion setTermAssertion:]
- -[IXTerminationAssertion setTermAssertion:].cold.1
- -[IXTerminationAssertion termAssertion]
- -[IXTerminationAssertion waitForAssertionSemaphore]
- -[IXUnregisterOSModuleToken acquireTerminationAssertionsWithError:].cold.1
- _AppURLFromExtractedPayloadDir
- _AppURLFromExtractedPayloadDir.cold.1
- _IXGetUncachedRemovabilityDataStore.cold.3
- _IXGetUncachedRemovabilityDataStore.cold.4
- _IXGetUncachedRemovabilityDataStore.cold.5
- _IXGetUncachedRemovabilityDataStore.cold.6
- _IXGetUncachedRemovabilityDataStore.cold.7
- _IXGetUncachedRemovabilityDataStore.cold.8
- _LoadInfoPlistFromBundle
- _LoadInfoPlistFromBundle.cold.1
- _LoadInfoPlistFromBundle.cold.2
- _LoadInfoPlistFromBundle.cold.3
- _LoadInfoPlistFromBundleAtURL
- _LoadInfoPlistFromBundleAtURL.cold.1
- _OBJC_IVAR_$_IXTerminationAssertion._termAssertion
- _OBJC_IVAR_$_IXTerminationAssertion._waitForAssertionSemaphore
- __CreateError
- __CreateErrorV
- __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXSimpleInstaller|IXSimpleInstallerPrivate|IXOSModuleRegistration|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
- ___102+[IXAppInstallCoordinator cancelCoordinatorsForAppsWithApplicationIdentities:withReason:client:error:]_block_invoke.75
- ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.702
- ___107+[IXAppInstallCoordinator cancelCoordinatorsForAppsWithApplicationIdentities:withReason:client:completion:]_block_invoke.78
- ___32-[IXAppInstallCoordinator error]_block_invoke.288
- ___32-[IXAppInstallCoordinator error]_block_invoke_2.289
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.292
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.304
- ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.306
- ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.307
- ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.316
- ___44-[IXAppInstallCoordinator hasInstallOptions]_block_invoke.216
- ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.198
- ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.248
- ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.308
- ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.695
- ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.220
- ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.309
- ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.219
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.290
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.291
- ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.188
- ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.285
- ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.279
- ___51-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke.217
- ___51-[IXAppInstallCoordinator setInstallOptions:error:]_block_invoke.215
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.190
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.190.cold.1
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.190.cold.2
- ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.189
- ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.239
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.240
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.240.cold.1
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.240.cold.2
- ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.282
- ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.238
- ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.287
- ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.249
- ___55-[IXAppInstallCoordinator dataImportPromisesWithError:]_block_invoke.271
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.176
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.176.cold.1
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.176.cold.2
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.250
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.250.cold.1
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.250.cold.2
- ___55-[IXAppInstallCoordinator setDataImportPromises:error:]_block_invoke.270
- ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.175
- ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.699
- ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.161
- ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.262
- ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.261
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.703
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.686
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.688
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.692
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.256
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.256.cold.1
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.256.cold.2
- ___58-[IXAppInstallCoordinator getHasDataImportPromises:error:]_block_invoke.275
- ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.255
- ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.278
- ___59+[IXAppInstallCoordinator defaultAppMetadataListWithError:]_block_invoke.120
- ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.265
- ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.281
- ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.264
- ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.280
- ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.254
- ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.223
- ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.222
- ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.260
- ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.269
- ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.263
- ___64+[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]_block_invoke.122
- ___64+[IXAppInstallCoordinator removabilityForAppWithIdentity:error:]_block_invoke.111
- ___65+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke.116
- ___66+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]_block_invoke.118
- ___68+[IXAppInstallCoordinator pauseCoordinatorForAppWithIdentity:error:]_block_invoke.79
- ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.199
- ___69+[IXAppInstallCoordinator removabilityForAppWithIdentity:completion:]_block_invoke.113
- ___69+[IXAppInstallCoordinator resumeCoordinatorForAppWithIdentity:error:]_block_invoke.80
- ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.204
- ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.203
- ___71+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]_block_invoke.121
- ___71+[IXAppInstallCoordinator uninstallAppWithIdentity:options:completion:]_block_invoke.105
- ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.284
- ___73+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:error:]_block_invoke.81
- ___73+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:error:]_block_invoke.112
- ___73+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke.131
- ___78+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:completion:]_block_invoke.82
- ___78+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:completion:]_block_invoke.114
- ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.696
- ___79+[IXAppInstallCoordinator updateSINFForAppWithIdentity:sinfData:options:error:]_block_invoke.126
- ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.685
- ___81+[IXAppInstallCoordinator revertAppWithIdentity:completionWithApplicationRecord:]_block_invoke.110
- ___82+[IXAppInstallCoordinator revertAppWithIdentity:resultingApplicationRecord:error:]_block_invoke.108
- ___82+[IXAppInstallCoordinator setRemovability:forAppWithIdentity:byClient:completion:]_block_invoke.115
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.46
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.50
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.50.cold.1
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.50.cold.2
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.50.cold.3
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke.50.cold.4
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.47
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.54
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.58
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_2.63
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_3.64
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_4.65
- ___84+[IXAppInstallCoordinator _asynchronouslyEnumerateCoordinatorsForIntent:usingBlock:]_block_invoke_4.65.cold.1
- ___85+[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]_block_invoke.154
- ___87+[IXAppInstallCoordinator cancelCoordinatorForAppWithIdentity:withReason:client:error:]_block_invoke.71
- ___88+[IXAppInstallCoordinator stagingLocationForInstallLocation:withSandboxExtension:error:]_block_invoke.276
- ___89+[IXAppInstallCoordinator _synchronouslyEnumerateCoordinatorsForIntent:error:usingBlock:]_block_invoke.70
- ___92+[IXAppInstallCoordinator cancelCoordinatorForAppWithIdentity:withReason:client:completion:]_block_invoke.74
- ___98+[IXAppInstallCoordinator uninstallAppWithIdentity:options:disposition:error:legacyProgressBlock:]_block_invoke.96
- ___Block_byref_object_copy_.48
- ___Block_byref_object_dispose_.49
- ___block_literal_global.691
- ___block_literal_global.698
- ___block_literal_global.701
- _interface.weakInterface.338
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_terminationAssertionForBundleIDs:description:terminationResistance:error:
- _objc_msgSend$acquireAssertion:
- _objc_msgSend$initForBundleIDs:description:terminationResistance:error:
- _objc_msgSend$setTermAssertion:
- _objc_msgSend$termAssertion
- _objc_msgSend$waitForAssertionSemaphore
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%@: %c"
+ "%p: %s"
+ "%s: %@ : %llu bytes needed, %llu bytes available.  %llu bytes can be purged, requesting %llu bytes be purged."
+ "%s: Expected a non-nil callback block"
+ "%s: Failed to acquire a termination assertion without an error : %@"
+ "%s: Failed to create dictionary from deserialized removability data: %@"
+ "%s: Failed to create enumerator for applications at module URL: %@ : %@"
+ "%s: Failed to create removability data from dictionary: %@"
+ "%s: Failed to deserialize removability data: %@"
+ "%s: Failed to get available space on device for %@: %s"
+ "%s: Failed to get data directory URL: %@"
+ "%s: Failed to get purgable space from Cache Delete: %@"
+ "%s: Failed to register bundles on darwinup root %@ : %@"
+ "%s: Failed to unregister bundles on darwinup root %@ : %@"
+ "%s: Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, %llu purgable). : %@"
+ "%s: Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, purgable unavailable). : %@"
+ "%s: Not enough space for for %@ : %llu bytes needed, %llu bytes available (%llu bytes were purged). : %@"
+ "%s: Path %@ : %llu bytes purged, enough available"
+ "%s: Preflight for %@: %llu bytes needed, %llu bytes available."
+ "%s: Preflight for %@: bytes consumed (%llu) greater than total bytes needed (%llu): space needed cannot be determined."
+ "%s: RBS Termination observer called: %@"
+ "%s: Termination assertion has already been invalidated!"
+ "%s: The options parameter passed to %s was nil. : %@"
+ "%s: Unexpectedly the bundleID for the bundle at %@ was not a valid string : %@"
+ "%s: Warning: client is attempting to create a %@ coordinator for %@, which is not currently a placeholder (%@)."
+ "%s: Warning: client is attempting to create a %@ coordinator for %@, which is not currently installed at all."
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:completion:]_block_invoke_2"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) registerRootContentForBundles:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:completion:]_block_invoke_2"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]"
+ "+[IXAppInstallCoordinator(IXRootContentRegistration) unregisterRootContentForBundles:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXTesting) fetchDuplicatedClassInfoWithError:]_block_invoke"
+ "-[IXLSApplicationRecordEnumerator _enumerateApplicationRecordsOnModuleAtURL:enumeratorBlock:error:]"
+ "-[IXTerminationAssertion acquireWithCompletion:]"
+ "-[IXTerminationAssertion invalidate]"
+ "@\"<IXApplicationRecordEnumeratorProtocol>\""
+ "@\"<IXTerminationAssertionProtocol>\""
+ "@\"<IXTerminationAssertionWrapperProtocol>\""
+ "@\"NSSet\"32@0:8@\"NSURL\"16^@24"
+ "@36@0:8@16@24C32"
+ "@44@0:8@\"NSSet\"16@\"NSString\"24C32@\"RBSProcessPredicate\"36"
+ "@44@0:8@\"NSString\"16@\"NSString\"24C32@\"RBSProcessPredicate\"36"
+ "@44@0:8@16@24C32@36"
+ "@48@0:8@16@24@32@?40"
+ "@52@0:8@16@24C32@36@?44"
+ "B40@0:8@16@?24^@32"
+ "CACHE_DELETE_AMOUNT"
+ "CACHE_DELETE_ERROR"
+ "CACHE_DELETE_VOLUME"
+ "Failed to acquire a termination assertion without an error"
+ "Failed to authenticate screen time pin."
+ "Failed to create enumerator for applications at module URL: %@"
+ "IXAppURLFromExtractedPayloadDir"
+ "IXApplicationRecordEnumeratorProtocol"
+ "IXCoordinatorIntentUpdatingDemoted"
+ "IXCopyAppRemovabilityDictionary"
+ "IXCopyLegacyRemovabilityStorageURL"
+ "IXCopyRemovabilityStorageWithoutChangeClockURL"
+ "IXCopySerializedAppRemovabilityData"
+ "IXCopySerializedAppRemovabilityDataWithoutChangeClock"
+ "IXFeatureFlags"
+ "IXLSApplicationRecordEnumerator"
+ "IXLoadInfoPlistFromBundle"
+ "IXLoadInfoPlistFromBundleAtURL"
+ "IXPreflightWithCacheDelete"
+ "IXPreflightWithCacheDelete_block_invoke"
+ "IXRootContentOperationOptions"
+ "IXRootContentRegistration"
+ "IXTerminationAssertionWrapperProtocol"
+ "IXUpdatingDemotedAppInstallCoordinator"
+ "IX_BACKGROUND_UPDATE_SCHEDULING"
+ "MigrationKit"
+ "Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, %llu purgable)."
+ "Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, purgable unavailable)."
+ "Not enough space for for %@ : %llu bytes needed, %llu bytes available (%llu bytes were purged)."
+ "OSMigration"
+ "RemovabilityMetadata.plist"
+ "T@\"<IXApplicationRecordEnumeratorProtocol>\",&,N,V_applicationEnumerator"
+ "T@\"<IXTerminationAssertionProtocol>\",&,N,V_terminationAssertion"
+ "T@\"<IXTerminationAssertionWrapperProtocol>\",&,N,V_terminationAssertion"
+ "T@?,C,N,V_acquisitionBlock"
+ "T@?,C,N,V_terminationAssertionCreationBlock"
+ "TB,N,V_deferUntilNextBoot"
+ "The options parameter passed to %s was nil."
+ "Unexpectedly the bundleID for the bundle at %@ was not a valid string"
+ "_GatherBundleIDsFromSetOfBundles"
+ "_LegacyRemovabilityPListToMetadata_block_invoke"
+ "_RemovabilityPListWithoutChangeClockToMetadata_block_invoke"
+ "_acquisitionBlock"
+ "_applicationEnumerator"
+ "_deferUntilNextBoot"
+ "_enumerateApplicationRecordsOnModuleAtURL:enumeratorBlock:error:"
+ "_remote_fetchDuplicatedClassInfo:"
+ "_remote_registerRootContentForBundles:options:completion:"
+ "_remote_unregisterRootContentForBundles:options:completion:"
+ "_terminationAssertionCreationBlock"
+ "acquireWithCompletion:"
+ "acquisitionBlock"
+ "applicationEnumerator"
+ "bundleIDsForModuleAtURL:error:"
+ "deferUntilNextBoot"
+ "fetchDuplicatedClassInfoWithError:"
+ "initWithBundleID:description:terminationResistance:"
+ "initWithBundleID:description:terminationResistance:allowLaunchPredicate:"
+ "initWithBundleID:description:terminationResistance:allowLaunchPredicate:creationBlock:"
+ "initWithBundleIDs:description:terminationResistance:"
+ "initWithBundleIDs:description:terminationResistance:allowLaunchPredicate:"
+ "initWithBundleIDs:description:terminationResistance:allowLaunchPredicate:creationBlock:"
+ "initWithModuleURL:options:applicationEnumerator:terminationAssertionCreationBlock:"
+ "initWithPredicate:context:allowLaunch:"
+ "installcoordinationd root-content-registration bundleURLs:%@"
+ "installcoordinationd root-content-unregistration bundleURLs:%@"
+ "osAppMigrationEnabled"
+ "registerRootContentForBundles:options:completion:"
+ "registerRootContentForBundles:options:error:"
+ "removability.plist"
+ "removeObserver:"
+ "scheduledUpdatesEnabled"
+ "set"
+ "setAcquisitionBlock:"
+ "setApplicationEnumerator:"
+ "setDeferUntilNextBoot:"
+ "setTerminationAssertionCreationBlock:"
+ "terminationAssertionCreationBlock"
+ "unregisterRootContentForBundles:options:completion:"
+ "unregisterRootContentForBundles:options:error:"
+ "v16@?0@\"LSApplicationRecord\"8"
+ "v16@?0^{__CFDictionary=}8"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v40@0:8@\"NSSet\"16@\"IXRootContentOperationOptions\"24@?<v@?B@\"NSError\">32"
- "%s failed in init"
- "%s: %s failed in init : %@"
- "%s: Attempting to set the same termination assertion for %@"
- "%s: Failed to acquire termination assertion %@ : %@"
- "%s: Failed to create termination assertion for predicate %@ : %@"
- "%s: Failed to enumerate apps on module at %@ : %@"
- "%s: RBS termination assertion observer called for %@"
- "%s: Warning: client is attempting to create a promoting coordinator for %@, which is not currently a placeholder (%@)."
- "%s: Warning: client is attempting to create a promoting coordinator for %@, which is not currently installed at all."
- "%s: We didn't have a termination assertion that we're tracking, so not acting on the callback from RBS"
- "-[IXTerminationAssertion _terminationAssertionForBundleIDs:description:terminationResistance:error:]"
- "-[IXTerminationAssertion acquireAssertion:]"
- "-[IXTerminationAssertion initForBundleIDs:description:terminationResistance:error:]"
- "-[IXTerminationAssertion setTermAssertion:]"
- "-[IXUnregisterOSModuleToken acquireTerminationAssertionsWithError:]"
- "@\"IXTerminationAssertion\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"RBSTerminationAssertion\""
- "@44@0:8@16@24C32^@36"
- "AppURLFromExtractedPayloadDir"
- "Failed to acquire termination assertion %@"
- "Failed to create termination assertion for predicate %@"
- "Failed to enumerate apps on module at %@"
- "LoadInfoPlistFromBundle"
- "LoadInfoPlistFromBundleAtURL"
- "T@\"IXTerminationAssertion\",&,N,V_terminationAssertion"
- "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_waitForAssertionSemaphore"
- "T@\"RBSTerminationAssertion\",&,N,V_termAssertion"
- "_termAssertion"
- "_terminationAssertionForBundleIDs:description:terminationResistance:error:"
- "_waitForAssertionSemaphore"
- "acquireAssertion:"
- "initForBundleIDs:description:terminationResistance:error:"
- "setTermAssertion:"
- "termAssertion"
- "waitForAssertionSemaphore"

```
