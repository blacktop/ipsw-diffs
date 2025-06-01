## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1270.80.2.0.0
-  __TEXT.__text: 0x92a44
-  __TEXT.__auth_stubs: 0x1300
-  __TEXT.__objc_methlist: 0x40a0
-  __TEXT.__const: 0xdf70
-  __TEXT.__gcc_except_tab: 0x924
-  __TEXT.__cstring: 0x14aaa
+1270.102.7.0.0
+  __TEXT.__text: 0xa1088
+  __TEXT.__auth_stubs: 0x1310
+  __TEXT.__objc_methlist: 0x4360
+  __TEXT.__const: 0xf8a0
+  __TEXT.__gcc_except_tab: 0x97c
+  __TEXT.__cstring: 0x156d0
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x11a4
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x55e
-  __TEXT.__objc_methname: 0xc41b
-  __TEXT.__objc_methtype: 0x163f
-  __TEXT.__objc_stubs: 0x7a80
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x1190
+  __TEXT.__unwind_info: 0x21c8
+  __TEXT.__eh_frame: 0xe30
+  __TEXT.__objc_classname: 0x566
+  __TEXT.__objc_methname: 0xcc41
+  __TEXT.__objc_methtype: 0x169a
+  __TEXT.__objc_stubs: 0x80e0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0xc48
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5d60
-  __DATA_CONST.__objc_selrefs: 0x2438
-  __DATA_CONST.__objc_arraydata: 0x9a0
-  __AUTH_CONST.__cfstring: 0xb8e0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x4ad0
+  __DATA_CONST.__objc_const: 0x6168
+  __DATA_CONST.__objc_selrefs: 0x2600
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_arraydata: 0x978
+  __AUTH_CONST.__cfstring: 0xbe40
+  __AUTH_CONST.__objc_const: 0x1c88
+  __AUTH_CONST.__const: 0x56e8
   __AUTH_CONST.__objc_dictobj: 0x11a8
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x990
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x268
-  __DATA.__objc_superrefs: 0x150
-  __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0x10a8
-  __DATA.__bss: 0x80
-  __DATA.__common: 0x30
-  __DATA_DIRTY.__const: 0x200
-  __DATA_DIRTY.__objc_const: 0x1c88
+  __AUTH_CONST.__auth_got: 0x998
+  __DATA.__objc_ivar: 0x4f4
+  __DATA.__data: 0x1178
+  __DATA.__bss: 0x90
+  __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x190
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35225D2F-CA1F-32C5-90C7-B9A17864D8B6
-  Functions: 1723
-  Symbols:   6008
-  CStrings:  5518
+  UUID: 318857AA-1821-3419-BF4C-03D6D6A4B3C0
+  Functions: 1809
+  Symbols:   6245
+  CStrings:  5707
 
Symbols:
+ +[ICLFeatureFlags systemAppDeletionEnabled]
+ +[MIBundle bundleIsInDenyList:]
+ +[MIBundleContainer updateiTunesMetadata:forAppWithIdentifier:error:]
+ +[MIStoreMetadata metadataForBundleContainerURL:error:]
+ -[ICLPlaceholderRecord isEligibleForWatchAppInstall]
+ -[ICLPlaceholderRecord isMarketplace]
+ -[ICLPlaceholderRecord setIsEligibleForWatchAppInstall:]
+ -[ICLPlaceholderRecord setIsMarketplace:]
+ -[MIAppExtensionBundle extensionPoint]
+ -[MIAppExtensionBundle setExtensionPoint:]
+ -[MIAppExtensionBundle targetsBrowserExtensionPoint]
+ -[MIAppExtensionBundle validateHasCorrespondingEntitlements:error:]
+ -[MIBundle displayName]
+ -[MIBundle isAppTypeBundle]
+ -[MIBundle mayContainAppExtensions]
+ -[MIBundle mayContainFrameworks]
+ -[MIBundle mayHaveExecutableProgram]
+ -[MIBundle relativePath]
+ -[MIBundle thisBundleAndAllContainedBundlesWithError:]
+ -[MIBundleContainer _writeRawiTunesMetadataData:error:]
+ -[MIBundleContainer captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
+ -[MIBundleContainer iTunesMetadataWithError:]
+ -[MIBundleContainer iTunesMetadata]
+ -[MIBundleContainer setITunesMetadata:]
+ -[MICodeSigningInfo initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:launchWarningData:]
+ -[MICodeSigningInfo launchWarningData]
+ -[MIExecutableBundle dataProtectionClass]
+ -[MIExecutableBundle enumerateDylibsWithBlock:]
+ -[MIExecutableBundle executableExistsWithError:]
+ -[MIExecutableBundle getSinfDataType:withError:]
+ -[MIExecutableBundle hasExecutableSliceForCPUType:subtype:error:]
+ -[MIExecutableBundle relativeExecutablePath]
+ -[MIExecutableBundle setLaunchWarningData:withError:]
+ -[MIExecutableBundle setSinfDataType:]
+ -[MIExecutableBundle setSinfDataType:withError:]
+ -[MIExecutableBundle setSinfDataTypeIsSet:]
+ -[MIExecutableBundle sinfDataTypeIsSet]
+ -[MIExecutableBundle sinfDataType]
+ -[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
+ -[MIFileManager removeExtendedAttributeNamed:fromURL:error:]
+ -[MIFilesystemScanner _scanExtensionKitLocations:withError:]
+ -[MIFilesystemScanner builtInExtensionKitExtensionsDirectories]
+ -[MIGlobalConfiguration _isInternalReleaseType]
+ -[MIGlobalConfiguration builtInExtensionKitExtensionsDirectories]
+ -[MIGlobalConfiguration cryptexExtensionKitExtensionsDirectories]
+ -[MIGlobalConfiguration cryptexExtensionKitExtensionsDirectory]
+ -[MIMachOImageSlice cpuSubtype]
+ -[MIMachOImageSlice cpuType]
+ -[MIMachOImageSlice initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:]
+ -[MIMachOImageSlice setCpuSubtype:]
+ -[MIMachOImageSlice setCpuType:]
+ -[MIPluginKitBundle mayContainFrameworks]
+ -[MIStoreMetadata distributorInfo]
+ -[MIStoreMetadata isEligibleForWatchAppInstall]
+ -[MIStoreMetadata propertyListDataWithError:]
+ -[MIStoreMetadata setDistributorInfo:]
+ -[MIStoreMetadataDistributor developerID]
+ -[MIStoreMetadataDistributor developerName]
+ -[MIStoreMetadataDistributor distributorIsFirstPartyApple]
+ -[MIStoreMetadataDistributor distributorIsThirdParty]
+ -[MIStoreMetadataDistributor distributorNameForCurrentLocale]
+ -[MIStoreMetadataDistributor distributorType]
+ -[MIStoreMetadataDistributor domain]
+ -[MIStoreMetadataDistributor localizedDistributorName]
+ -[MIStoreMetadataDistributor setDeveloperID:]
+ -[MIStoreMetadataDistributor setDeveloperName:]
+ -[MIStoreMetadataDistributor setDomain:]
+ -[MIStoreMetadataDistributor setLocalizedDistributorName:]
+ -[MIStoreMetadataDistributor setSourceURL:]
+ -[MIStoreMetadataDistributor setSupportPageURL:]
+ -[MIStoreMetadataDistributor sourceURL]
+ -[MIStoreMetadataDistributor supportPageURL]
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table86
+ GCC_except_table91
+ _CFBundleCopyLocalizationsForPreferences
+ _MIArrayFilteredToContainOnlyClass
+ _MICopyDataProtectionClassEntitlement
+ _MICopyDataProtectionIfAvailableEntitlement
+ _MICopyMemoryTransferAcceptEntitlement
+ _MICopyMemoryTransferSendEntitlement
+ _MIDistributorTypeIsFirstPartyApple
+ _MIDistributorTypeIsThirdParty
+ _MIGetFirstTrueBooleanEntitlement
+ _MIGetSinfDataType
+ _MIHasAllowJITEntitlement
+ _MIHasBrowserAppInstallationEntitlement
+ _MIHasBrowserEngineContentEntitlement
+ _MIHasBrowserEngineHostEntitlement
+ _MIHasBrowserEngineNetworkingEntitlement
+ _MIHasBrowserEngineRenderingEntitlement
+ _MIHasDefaultBrowserEntitlement
+ _MIHasEmbeddedBrowserEngineEntitlement
+ _MIHasMarketplaceEntitlement
+ _MISetSinfDataType
+ _NSFileProtectionCompleteWhenUserInactive
+ _OBJC_IVAR_$_ICLPlaceholderRecord._isEligibleForWatchAppInstall
+ _OBJC_IVAR_$_ICLPlaceholderRecord._isMarketplace
+ _OBJC_IVAR_$_MIAppExtensionBundle._extensionPoint
+ _OBJC_IVAR_$_MIBundleContainer._iTunesMetadata
+ _OBJC_IVAR_$_MICodeSigningInfo._launchWarningData
+ _OBJC_IVAR_$_MIExecutableBundle._sinfDataType
+ _OBJC_IVAR_$_MIExecutableBundle._sinfDataTypeIsSet
+ _OBJC_IVAR_$_MIMachOImageSlice._cpuSubtype
+ _OBJC_IVAR_$_MIMachOImageSlice._cpuType
+ _OBJC_IVAR_$_MIStoreMetadata._distributorInfo
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._developerID
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._developerName
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._domain
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._localizedDistributorName
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._sourceURL
+ _OBJC_IVAR_$_MIStoreMetadataDistributor._supportPageURL
+ __OBJC_$_CLASS_PROP_LIST_ICLFeatureFlags
+ __ProtectionClassForString
+ ___31+[MIBundle bundleIsInDenyList:]_block_invoke
+ ___47-[MIExecutableBundle enumerateDylibsWithBlock:]_block_invoke
+ ___47-[MIGlobalConfiguration _isInternalReleaseType]_block_invoke
+ ___48-[MIExecutableBundle setSinfDataType:withError:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e18_B20?0"NSURL"8C16ls32l8
+ ___block_descriptor_40_e8_32s_e20_B28?0i8i12I16I20I24ls32l8
+ ___block_descriptor_44_e8_32r_e15_B16?0"NSURL"8lr32l8
+ ___block_descriptor_56_e8_32bs40r_e14_v20?0I8I12I16lr40l8s32l8
+ ___block_literal_global.184
+ ___block_literal_global.198
+ ___block_literal_global.213
+ ___block_literal_global.317
+ ___block_literal_global.323
+ ___block_literal_global.369
+ ___block_literal_global.374
+ ___block_literal_global.519
+ ___block_literal_global.87
+ __isInternalReleaseType.isInternalReleaseType
+ __isInternalReleaseType.onceToken
+ __unnamed_array_storage.100
+ __unnamed_array_storage.101
+ __unnamed_array_storage.113
+ __unnamed_array_storage.118
+ __unnamed_array_storage.119
+ __unnamed_array_storage.126
+ __unnamed_array_storage.127
+ __unnamed_array_storage.132
+ __unnamed_array_storage.139
+ __unnamed_array_storage.14
+ __unnamed_array_storage.140
+ __unnamed_array_storage.145
+ __unnamed_array_storage.152
+ __unnamed_array_storage.153
+ __unnamed_array_storage.165
+ __unnamed_array_storage.166
+ __unnamed_array_storage.178
+ __unnamed_array_storage.179
+ __unnamed_array_storage.197
+ __unnamed_array_storage.198
+ __unnamed_array_storage.199
+ __unnamed_array_storage.200
+ __unnamed_array_storage.207
+ __unnamed_array_storage.208
+ __unnamed_array_storage.209
+ __unnamed_array_storage.210
+ __unnamed_array_storage.220
+ __unnamed_array_storage.221
+ __unnamed_array_storage.224
+ __unnamed_array_storage.229
+ __unnamed_array_storage.230
+ __unnamed_array_storage.234
+ __unnamed_array_storage.239
+ __unnamed_array_storage.240
+ __unnamed_array_storage.246
+ __unnamed_array_storage.247
+ __unnamed_array_storage.249
+ __unnamed_array_storage.250
+ __unnamed_array_storage.256
+ __unnamed_array_storage.257
+ __unnamed_array_storage.262
+ __unnamed_array_storage.263
+ __unnamed_array_storage.269
+ __unnamed_array_storage.270
+ __unnamed_array_storage.276
+ __unnamed_array_storage.277
+ __unnamed_array_storage.289
+ __unnamed_array_storage.290
+ __unnamed_array_storage.296
+ __unnamed_array_storage.297
+ __unnamed_array_storage.303
+ __unnamed_array_storage.304
+ __unnamed_array_storage.309
+ __unnamed_array_storage.310
+ __unnamed_array_storage.311
+ __unnamed_array_storage.319
+ __unnamed_array_storage.320
+ __unnamed_array_storage.34
+ __unnamed_array_storage.341
+ __unnamed_array_storage.36
+ __unnamed_array_storage.360
+ __unnamed_array_storage.385
+ __unnamed_array_storage.386
+ __unnamed_array_storage.392
+ __unnamed_array_storage.393
+ __unnamed_array_storage.40
+ __unnamed_array_storage.41
+ __unnamed_array_storage.421
+ __unnamed_array_storage.422
+ __unnamed_array_storage.428
+ __unnamed_array_storage.429
+ __unnamed_array_storage.46
+ __unnamed_array_storage.465
+ __unnamed_array_storage.475
+ __unnamed_array_storage.476
+ __unnamed_array_storage.498
+ __unnamed_array_storage.499
+ __unnamed_array_storage.505
+ __unnamed_array_storage.506
+ __unnamed_array_storage.512
+ __unnamed_array_storage.513
+ __unnamed_array_storage.52
+ __unnamed_array_storage.53
+ __unnamed_array_storage.56
+ __unnamed_array_storage.62
+ __unnamed_array_storage.641
+ __unnamed_array_storage.656
+ __unnamed_array_storage.66
+ __unnamed_array_storage.668
+ __unnamed_array_storage.669
+ __unnamed_array_storage.678
+ __unnamed_array_storage.679
+ __unnamed_array_storage.69
+ __unnamed_array_storage.70
+ __unnamed_array_storage.76
+ __unnamed_array_storage.83
+ __unnamed_array_storage.84
+ __unnamed_array_storage.909
+ __unnamed_array_storage.910
+ __unnamed_array_storage.917
+ __unnamed_array_storage.918
+ __unnamed_array_storage.927
+ __unnamed_array_storage.928
+ __unnamed_array_storage.94
+ __unnamed_array_storage.95
+ _bundleIsInDenyList:.denylist
+ _bundleIsInDenyList:.onceToken
+ _developerID
+ _developerName
+ _distributorInfo
+ _domain
+ _kMISValidationInfoLaunchWarningData
+ _kMISValidationOptionAllowLaunchWarning
+ _localizedDistributorName
+ _malloc
+ _objc_msgSend$_isInternalReleaseType
+ _objc_msgSend$_scanExtensionKitLocations:withError:
+ _objc_msgSend$_writeRawiTunesMetadataData:error:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$builtInExtensionKitExtensionsDirectories
+ _objc_msgSend$bundleIsInDenyList:
+ _objc_msgSend$captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:
+ _objc_msgSend$cpuSubtype
+ _objc_msgSend$cpuType
+ _objc_msgSend$cryptexExtensionKitExtensionsDirectories
+ _objc_msgSend$cryptexExtensionKitExtensionsDirectory
+ _objc_msgSend$dataForExtendedAttributeNamed:length:fromURL:error:
+ _objc_msgSend$dataProtectionClass
+ _objc_msgSend$developerID
+ _objc_msgSend$developerName
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$distributorIsFirstPartyApple
+ _objc_msgSend$distributorType
+ _objc_msgSend$enumerateDylibsWithBlock:
+ _objc_msgSend$extensionPoint
+ _objc_msgSend$firstObjectCommonWithArray:
+ _objc_msgSend$frameworkBundlesWithError:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getSinfDataType:withError:
+ _objc_msgSend$iTunesMetadata
+ _objc_msgSend$iTunesMetadataWithError:
+ _objc_msgSend$initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:
+ _objc_msgSend$initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:launchWarningData:
+ _objc_msgSend$isAppTypeBundle
+ _objc_msgSend$isEligibleForWatchAppInstall
+ _objc_msgSend$isMarketplace
+ _objc_msgSend$launchWarningData
+ _objc_msgSend$localizedDistributorName
+ _objc_msgSend$mayContainAppExtensions
+ _objc_msgSend$mayContainFrameworks
+ _objc_msgSend$mayHaveExecutableProgram
+ _objc_msgSend$metadataFromPlistAtURL:error:
+ _objc_msgSend$propertyListDataWithError:
+ _objc_msgSend$relativeExecutablePath
+ _objc_msgSend$relativePath
+ _objc_msgSend$removeExtendedAttributeNamed:fromURL:error:
+ _objc_msgSend$setCpuSubtype:
+ _objc_msgSend$setCpuType:
+ _objc_msgSend$setData:forExtendedAttributeNamed:onURL:error:
+ _objc_msgSend$setDeveloperID:
+ _objc_msgSend$setDeveloperName:
+ _objc_msgSend$setDistributorInfo:
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setITunesMetadata:
+ _objc_msgSend$setIsEligibleForWatchAppInstall:
+ _objc_msgSend$setIsMarketplace:
+ _objc_msgSend$setLocalizedDistributorName:
+ _objc_msgSend$setSinfDataType:
+ _objc_msgSend$setSinfDataTypeIsSet:
+ _objc_msgSend$setSourceURL:
+ _objc_msgSend$setSupportPageURL:
+ _objc_msgSend$sinfDataType
+ _objc_msgSend$sinfDataTypeIsSet
+ _objc_msgSend$sourceURL
+ _objc_msgSend$supportPageURL
+ _objc_msgSend$systemAppDeletionEnabled
+ _objc_msgSend$testFlagsAreSet:
+ _objc_msgSend$thisBundleAndAllContainedBundlesWithError:
+ _sourceURL
+ _supportPageURL
- +[MIBundle bundleIsBlacklisted:]
- +[MIBundleContainer updateSinfDataForAppWithIdentifier:sinfData:error:]
- +[MIBundleContainer updateiTunesMetadataForAppWithIdentifier:plistData:error:]
- -[MICodeSigningInfo initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:]
- -[MIContainer captureStoreDataFromDirectory:doCopy:failureIsFatal:withError:]
- -[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:]
- -[MIFilesystemScanner _scanExtensionKitLocationsWithError:]
- -[MIFilesystemScanner extensionKitExtensionsDirectories]
- -[MIInstallationIdentity _writeToBundle:fd:fdLocation:error:]
- -[MIMachOImageSlice initWithPlatform:sdkVersion:minOSVersion:]
- -[MIStoreMetadata distributor]
- -[MIStoreMetadata setDistributor:]
- -[MIStoreMetadataDistributor packageURL]
- -[MIStoreMetadataDistributor setPackageURL:]
- GCC_except_table30
- GCC_except_table33
- GCC_except_table39
- GCC_except_table52
- GCC_except_table53
- GCC_except_table54
- GCC_except_table59
- GCC_except_table73
- GCC_except_table90
- _OBJC_IVAR_$_MIStoreMetadata._distributor
- _OBJC_IVAR_$_MIStoreMetadataDistributor._packageURL
- ___32+[MIBundle bundleIsBlacklisted:]_block_invoke
- ___block_descriptor_40_e8_32s_e14_B20?0I8I12I16ls32l8
- ___block_descriptor_48_e8_32bs40r_e14_v20?0I8I12I16lr40l8s32l8
- ___block_literal_global.187
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.202
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.494
- ___block_literal_global.79
- __unnamed_array_storage.102
- __unnamed_array_storage.103
- __unnamed_array_storage.109
- __unnamed_array_storage.112
- __unnamed_array_storage.116
- __unnamed_array_storage.123
- __unnamed_array_storage.130
- __unnamed_array_storage.150
- __unnamed_array_storage.151
- __unnamed_array_storage.195
- __unnamed_array_storage.196
- __unnamed_array_storage.20
- __unnamed_array_storage.202
- __unnamed_array_storage.203
- __unnamed_array_storage.206
- __unnamed_array_storage.21
- __unnamed_array_storage.212
- __unnamed_array_storage.213
- __unnamed_array_storage.216
- __unnamed_array_storage.217
- __unnamed_array_storage.218
- __unnamed_array_storage.222
- __unnamed_array_storage.231
- __unnamed_array_storage.232
- __unnamed_array_storage.242
- __unnamed_array_storage.243
- __unnamed_array_storage.244
- __unnamed_array_storage.245
- __unnamed_array_storage.252
- __unnamed_array_storage.253
- __unnamed_array_storage.254
- __unnamed_array_storage.255
- __unnamed_array_storage.265
- __unnamed_array_storage.266
- __unnamed_array_storage.267
- __unnamed_array_storage.268
- __unnamed_array_storage.272
- __unnamed_array_storage.273
- __unnamed_array_storage.279
- __unnamed_array_storage.280
- __unnamed_array_storage.281
- __unnamed_array_storage.294
- __unnamed_array_storage.295
- __unnamed_array_storage.301
- __unnamed_array_storage.302
- __unnamed_array_storage.306
- __unnamed_array_storage.307
- __unnamed_array_storage.308
- __unnamed_array_storage.313
- __unnamed_array_storage.314
- __unnamed_array_storage.325
- __unnamed_array_storage.342
- __unnamed_array_storage.352
- __unnamed_array_storage.357
- __unnamed_array_storage.358
- __unnamed_array_storage.359
- __unnamed_array_storage.363
- __unnamed_array_storage.364
- __unnamed_array_storage.365
- __unnamed_array_storage.366
- __unnamed_array_storage.38
- __unnamed_array_storage.42
- __unnamed_array_storage.449
- __unnamed_array_storage.450
- __unnamed_array_storage.453
- __unnamed_array_storage.454
- __unnamed_array_storage.478
- __unnamed_array_storage.479
- __unnamed_array_storage.48
- __unnamed_array_storage.480
- __unnamed_array_storage.481
- __unnamed_array_storage.487
- __unnamed_array_storage.60
- __unnamed_array_storage.616
- __unnamed_array_storage.631
- __unnamed_array_storage.643
- __unnamed_array_storage.644
- __unnamed_array_storage.653
- __unnamed_array_storage.654
- __unnamed_array_storage.68
- __unnamed_array_storage.74
- __unnamed_array_storage.75
- __unnamed_array_storage.79
- __unnamed_array_storage.81
- __unnamed_array_storage.82
- __unnamed_array_storage.855
- __unnamed_array_storage.856
- __unnamed_array_storage.863
- __unnamed_array_storage.864
- __unnamed_array_storage.873
- __unnamed_array_storage.874
- __unnamed_array_storage.99
- _bundleIsBlacklisted:.blacklist
- _bundleIsBlacklisted:.onceToken
- _distributor
- _objc_msgSend$_scanExtensionKitLocationsWithError:
- _objc_msgSend$_writeToBundle:fd:fdLocation:error:
- _objc_msgSend$bundleIsBlacklisted:
- _objc_msgSend$captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:
- _objc_msgSend$distributor
- _objc_msgSend$extensionKitExtensionsDirectories
- _objc_msgSend$initWithPlatform:sdkVersion:minOSVersion:
- _objc_msgSend$initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:
- _objc_msgSend$packageURL
- _objc_msgSend$setDistributor:
- _objc_msgSend$setPackageURL:
- _objc_msgSend$updateAndValidateSinf:error:
- _packageURL
CStrings:
+ "\x01\x12"
+ "\x061"
+ "\b"
+ "!'"
+ "%@ is in the deny list"
+ "%@ is missing its bundle executable. Please check your build settings to make sure that a bundle executable is produced at the path \"%@\"."
+ "+[MIBundle bundleIsInDenyList:]"
+ "-[MIAppExtensionBundle validateHasCorrespondingEntitlements:error:]"
+ "-[MIBundleContainer _writeRawiTunesMetadataData:error:]"
+ "-[MIBundleContainer captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]"
+ "-[MIExecutableBundle dataProtectionClass]"
+ "-[MIExecutableBundle enumerateDylibsWithBlock:]"
+ "-[MIExecutableBundle executableExistsWithError:]"
+ "-[MIExecutableBundle hasExecutableSliceForCPUType:subtype:error:]"
+ "-[MIExecutableBundle setLaunchWarningData:withError:]"
+ "-[MIExecutableBundle setSinfDataType:withError:]"
+ "-[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]"
+ "-[MIFileManager removeExtendedAttributeNamed:fromURL:error:]"
+ "-[MIGlobalConfiguration allowsInternalSecurityPolicy]_block_invoke"
+ "-[MIGlobalConfiguration hasInternalContent]_block_invoke"
+ "1"
+ "@\"MIStoreMetadata\""
+ "@24@0:8@?16"
+ "@36@0:8i16i20I24I28I32"
+ "@96@0:8@16@24@32@40@48@56Q64Q72Q80@88"
+ "B28@?0i8i12I16I20I24"
+ "B32@0:8^I16^@24"
+ "B32@0:8i16i20^@24"
+ "B44@0:8@16B24B28B32^@36"
+ "CoreServices app"
+ "Couldn't get data from EA named %s on \"%s\": %s"
+ "Did not find at least one executable slice with CPU type %d and subtype %d in bundle %@"
+ "DriverKit extension"
+ "Failed to discover dylibs in directory %@"
+ "Failed to find any app with bundle ID %@"
+ "Failed to get all bundles within app %@"
+ "Failed to get iTunesMetadata from %@ : %@"
+ "Failed to read iTunesMetadata from %@ : %@"
+ "Failed to remove extended attribute named %@ from %s: %s"
+ "Got unknown value %u for %s extended attribute on %@"
+ "Got unknown value %u for Sinf data type to set on %@"
+ "Got value for %s extended attribute on %@ with unexpected length %lu"
+ "IMPORTANT: Detected Internal release type but os_variant_allows_internal_security_policies returned false"
+ "IMPORTANT: Detected Internal release type but os_variant_has_internal_content returned false"
+ "IsEligibleForWatchAppInstall"
+ "IsMarketplace"
+ "LaunchWarningData"
+ "MGCopyAnswer for kMGOCompatibleAppVariants returned NULL"
+ "MIGetSinfDataType"
+ "MISetSinfDataType"
+ "MOBILEINSTALLATION_TEST_LAUNCH_WARNING_DATA"
+ "System/Cryptexes/App"
+ "System/Cryptexes/OS"
+ "T@\"MIStoreMetadata\",C,N,V_iTunesMetadata"
+ "T@\"MIStoreMetadataDistributor\",C,N,V_distributorInfo"
+ "T@\"NSData\",R,C,N,V_launchWarningData"
+ "T@\"NSDictionary\",C,N,V_localizedDistributorName"
+ "T@\"NSString\",C,N,V_developerID"
+ "T@\"NSString\",C,N,V_developerName"
+ "T@\"NSString\",C,N,V_domain"
+ "T@\"NSURL\",C,N,V_sourceURL"
+ "T@\"NSURL\",C,N,V_supportPageURL"
+ "TB,N,V_isEligibleForWatchAppInstall"
+ "TB,N,V_isMarketplace"
+ "TB,N,V_sinfDataTypeIsSet"
+ "TEST MODE: Returning fake launch warning data for %@"
+ "TI,N,V_sinfDataType"
+ "TQ,N,V_extensionPoint"
+ "The app extension at \"%@\" has the entitlement \"%@\" which is not allowed for an extension targeting the extension point \"%@\"."
+ "The app extension at \"%@\" specifies the entitlement \"%@\" = \"%@\" where the value does not match the parent app bundle's CFBundleIdentifier, \"%@\". This entitlement, if set, must have a value that matches the bundle identifier of the parent app."
+ "The app extension at \"%@\" targets the extension point \"%@\" but is missing the corresponding required \"%@\" = TRUE (boolean) entitlement."
+ "The value of the UISupportedDevices key in this app's Info.plist key must contain only string values."
+ "This app is not compatibile with this device. This app specifies a value for UISupportedDevices in its Info.plist as [%@], but none of the identifiers in this device's compatibility list are present in this app's supported devices. This device is compatible with [%@]."
+ "Ti,N,V_cpuSubtype"
+ "Ti,N,V_cpuType"
+ "Ti,R,N"
+ "Unexpectedly asked to validate thinning on a non-app bundle %@"
+ "Unexpectedly found a second watch app, \"%@\", in this app's \"%@\" directory when we had already found \"%@\" in that directory. An iOS app may only have one embedded watch app."
+ "VuGdqp8UBpi9vPWHlPluVQ"
+ "_cpuSubtype"
+ "_cpuType"
+ "_developerID"
+ "_developerName"
+ "_distributorInfo"
+ "_domain"
+ "_extensionPoint"
+ "_iTunesMetadata"
+ "_isEligibleForWatchAppInstall"
+ "_isInternalReleaseType"
+ "_isMarketplace"
+ "_launchWarningData"
+ "_localizedDistributorName"
+ "_scanExtensionKitLocations:withError:"
+ "_sinfDataType"
+ "_sinfDataTypeIsSet"
+ "_sourceURL"
+ "_supportPageURL"
+ "_writeRawiTunesMetadataData:error:"
+ "app extension"
+ "arrayWithCapacity:"
+ "builtInExtensionKitExtensionsDirectories"
+ "bundleIsInDenyList:"
+ "captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
+ "captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
+ "com.apple.AppStore"
+ "com.apple.TestFlight"
+ "com.apple.developer.browser.app-installation"
+ "com.apple.developer.cs.allow-jit"
+ "com.apple.developer.default-data-protection-if-available"
+ "com.apple.developer.embedded-web-browser-engine"
+ "com.apple.developer.marketplace.app-installation"
+ "com.apple.developer.memory.transfer-accept"
+ "com.apple.developer.memory.transfer-send"
+ "com.apple.developer.web-browser"
+ "com.apple.developer.web-browser-engine.host"
+ "com.apple.developer.web-browser-engine.networking"
+ "com.apple.developer.web-browser-engine.rendering"
+ "com.apple.developer.web-browser-engine.webcontent"
+ "com.apple.managed_drm_id"
+ "com.apple.mis.warning"
+ "com.apple.web-browser-engine.content"
+ "com.apple.web-browser-engine.networking"
+ "com.apple.web-browser-engine.rendering"
+ "cpuSubtype"
+ "cpuType"
+ "cryptexExtensionKitExtensionsDirectories"
+ "cryptexExtensionKitExtensionsDirectory"
+ "dataProtectionClass"
+ "developerID"
+ "developerName"
+ "disk image app"
+ "displayName"
+ "distributorDomain"
+ "distributorInfo"
+ "distributorIsFirstPartyApple"
+ "distributorIsThirdParty"
+ "distributorNameForCurrentLocale"
+ "distributorType"
+ "dylib"
+ "embedded watch app"
+ "enumerateDylibsWithBlock:"
+ "executableExistsWithError:"
+ "extensionPoint"
+ "firstObjectCommonWithArray:"
+ "getBytes:length:"
+ "getSinfDataType:withError:"
+ "hasExecutableSliceForCPUType:subtype:error:"
+ "iTunesMetadata"
+ "iTunesMetadata.plist captured from %@ has distributorInfo set; this is not allowed. Found distributorInfo: %@"
+ "iTunesMetadata.plist was not a dictionary; found class %@"
+ "iTunesMetadataWithError:"
+ "initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:"
+ "initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:launchWarningData:"
+ "internal app"
+ "isAppTypeBundle"
+ "isEligibleForWatchAppInstall"
+ "isMarketplace"
+ "launchWarningData"
+ "libMIS returned launch warning for %@"
+ "localizedDistributorName"
+ "localizedDistributorName dictionary does not have expected type"
+ "mayContainAppExtensions"
+ "mayContainFrameworks"
+ "mayHaveExecutableProgram"
+ "metadataForBundleContainerURL:error:"
+ "propertyListDataWithError:"
+ "relativeExecutablePath"
+ "relativePath"
+ "removeExtendedAttributeNamed:fromURL:error:"
+ "setCpuSubtype:"
+ "setCpuType:"
+ "setDeveloperID:"
+ "setDeveloperName:"
+ "setDistributorInfo:"
+ "setDomain:"
+ "setExtensionPoint:"
+ "setITunesMetadata:"
+ "setIsEligibleForWatchAppInstall:"
+ "setIsMarketplace:"
+ "setLaunchWarningData:withError:"
+ "setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:"
+ "setLocalizedDistributorName:"
+ "setSinfDataType:"
+ "setSinfDataType:withError:"
+ "setSinfDataTypeIsSet:"
+ "setSourceURL:"
+ "setSupportPageURL:"
+ "sinfDataType"
+ "sinfDataTypeIsSet"
+ "sourceURL"
+ "supportPageURL"
+ "system app"
+ "system app placeholder"
+ "systemAppDeletionEnabled"
+ "targetsBrowserExtensionPoint"
+ "thisBundleAndAllContainedBundlesWithError:"
+ "unknown bundle type"
+ "updateiTunesMetadata:forAppWithIdentifier:error:"
+ "updateiTunesMetadataForIXWithIdentifier:metadata:completion:"
+ "user app"
+ "v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40"
+ "validateHasCorrespondingEntitlements:error:"
- "\x06"
- "\x11'"
- "+[MIBundle bundleIsBlacklisted:]"
- "+[MIBundleContainer updateSinfDataForAppWithIdentifier:sinfData:error:]"
- "-[MIBundleContainer writeiTunesMetadata:error:]"
- "-[MIContainer captureStoreDataFromDirectory:doCopy:failureIsFatal:withError:]"
- "-[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:]"
- "-[MIInstallationIdentity _writeToBundle:fd:fdLocation:error:]"
- "0+nc/Udy4WNG8S+Q7a/s1A"
- "@28@0:8I16I20I24"
- "@88@0:8@16@24@32@40@48@56Q64Q72Q80"
- "B20@?0I8I12I16"
- "B40@0:8@16B24B28^@32"
- "B44@0:8@16i24@28^@36"
- "B48@0:8@16@24B32B36^@40"
- "Blacklisting %@"
- "CompatibleDeviceFallback"
- "Core Services App"
- "Couldn't get install session UUID from EA named %s on \"%s\": %s"
- "Defaults override %@ did not match supported devices."
- "Device %@ not in SupportedDevices list for %@ : %@"
- "Disk Image App"
- "DriverKit Extension"
- "Embedded Watch App"
- "Failed to find app with bundle ID %@"
- "Failed to get artwork traits from gestalt."
- "Failed to get bundle from container %@"
- "Failed to set unique install ID on DriverKit extension %@"
- "Failed to set unique install ID on app extension %@"
- "Failed to set unique install ID on xpc service %@"
- "Fallback %@ did not match supported devices."
- "Found WatchKit 2.0 app bundle named %@ in %@ when we already found %@"
- "Internal App"
- "MGCopyAnswer for kMGOThinningProductType returned NULL"
- "Matched thinning based on fallback %@"
- "SupportedDevices Info.plist key does not contain only string values."
- "System App Placeholder"
- "System/Cryptexes/App/"
- "System/Cryptexes/OS/"
- "T@\"MIStoreMetadataDistributor\",C,N,V_distributor"
- "T@\"NSURL\",C,N,V_packageURL"
- "User App"
- "_GetDataProtectionClass"
- "_distributor"
- "_packageURL"
- "_scanExtensionKitLocationsWithError:"
- "_writeToBundle:fd:fdLocation:error:"
- "bundleIsBlacklisted:"
- "captureStoreDataFromDirectory:doCopy:failureIsFatal:withError:"
- "captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:"
- "distributor"
- "distributorPackageURL"
- "extensionKitExtensionsDirectories"
- "iTunesMetadata.plist was not a dictionary"
- "initWithPlatform:sdkVersion:minOSVersion:"
- "initWithSignerIdentity:signerOrganization:codeInfoIdentifier:teamIdentifier:signatureVersion:entitlements:signerType:profileType:signingInfoSource:"
- "oPeik/9e8lQWMszEjbPzng"
- "packageURL"
- "setDistributor:"
- "setPackageURL:"
- "updateSinfDataForAppWithIdentifier:sinfData:error:"
- "updateiTunesMetadataForAppWithIdentifier:plistData:error:"
- "updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"NSError\">40"

```
