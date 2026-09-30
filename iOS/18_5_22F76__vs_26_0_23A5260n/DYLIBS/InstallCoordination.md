## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-699.100.10.0.0
-  __TEXT.__text: 0x64918
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x3d50
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xe017
-  __TEXT.__oslogstring: 0x76a6
-  __TEXT.__gcc_except_tab: 0x1af4
-  __TEXT.__unwind_info: 0x1660
-  __TEXT.__objc_classname: 0x84f
-  __TEXT.__objc_methname: 0x9ffb
-  __TEXT.__objc_methtype: 0x222d
-  __TEXT.__objc_stubs: 0x5ac0
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x1a70
-  __DATA_CONST.__objc_classlist: 0x188
+755.0.0.0.0
+  __TEXT.__text: 0x69418
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x4118
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0xe5fb
+  __TEXT.__oslogstring: 0x78b8
+  __TEXT.__gcc_except_tab: 0x1d80
+  __TEXT.__unwind_info: 0x1778
+  __TEXT.__objc_classname: 0x8ae
+  __TEXT.__objc_methname: 0xac33
+  __TEXT.__objc_methtype: 0x2389
+  __TEXT.__objc_stubs: 0x5fe0
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x1b60
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e90
+  __DATA_CONST.__objc_selrefs: 0x2060
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5600
-  __AUTH_CONST.__objc_const: 0xa5d8
+  __AUTH_CONST.__cfstring: 0x5980
+  __AUTH_CONST.__objc_const: 0xada0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x8a8
-  __DATA.__bss: 0x68
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x214
+  __DATA.__data: 0x908
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C820D10C-1F9D-3005-A65E-E1E4BB0C07BA
-  Functions: 1855
-  Symbols:   6169
-  CStrings:  3964
+  UUID: 9C0A74EF-E82C-318D-BCA5-0703789B8C83
+  Functions: 1952
+  Symbols:   6459
+  CStrings:  4132
 
Symbols:
+ +[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]
+ +[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]
+ +[IXAppInstallCoordinator(IXSimpleInstaller) _temporaryStagingLocationForInstallLocation:error:]
+ +[IXOwnedDataPromiseSeed _locationClassCluster]
+ +[IXPlaceholder _iconContentForBundleAtURL:infoPlistIconContent:withStagingPath:error:]
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:]
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.1
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.10
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.11
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.12
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.13
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.14
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.15
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.16
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.17
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.18
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.19
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.2
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.20
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.3
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.4
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.5
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.6
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.7
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.8
+ +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:].cold.9
+ +[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:location:error:]
+ +[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:location:error:].cold.1
+ +[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:location:error:].cold.2
+ +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:]
+ +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:].cold.1
+ +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:].cold.2
+ +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:].cold.3
+ +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:].cold.4
+ +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:].cold.5
+ +[IXPlaceholder placeholderForInstallable:client:installType:metadata:location:error:]
+ +[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:location:error:]
+ +[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:location:error:].cold.1
+ +[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:location:error:].cold.2
+ +[IXRefreshContainerOptions supportsSecureCoding]
+ -[IXAppInstallCoordinator dataImportPromisesWithError:]
+ -[IXAppInstallCoordinator dataImportPromisesWithError:].cold.1
+ -[IXAppInstallCoordinator dataImportPromisesWithError:].cold.2
+ -[IXAppInstallCoordinator dataImportPromisesWithError:].cold.3
+ -[IXAppInstallCoordinator getHasDataImportPromises:error:]
+ -[IXAppInstallCoordinator setDataImportPromises:error:]
+ -[IXAppInstallCoordinator setPreserveTargetBundleNameOnUpdate:error:]
+ -[IXAppInstallCoordinator setPreserveTargetBundleNameOnUpdate:error:].cold.1
+ -[IXApplicationIdentity initFromDelimitedString:]
+ -[IXApplicationIdentity initFromDelimitedString:].cold.1
+ -[IXApplicationIdentity initFromPlistDictionary:]
+ -[IXApplicationIdentity initFromPlistDictionary:].cold.1
+ -[IXApplicationIdentity initFromPlistDictionary:].cold.2
+ -[IXApplicationIdentity initFromPlistDictionary:].cold.3
+ -[IXApplicationIdentity initFromPlistDictionary:].cold.4
+ -[IXApplicationIdentity initFromPlistDictionary:].cold.5
+ -[IXApplicationIdentity initWithBundleID:]
+ -[IXApplicationIdentity initWithBundleID:persona:]
+ -[IXApplicationIdentity initWithBundleID:personaUniqueString:location:]
+ -[IXApplicationIdentity initWithBundleIdentifier:personaUniqueString:location:]
+ -[IXFileManager realPathForURL:]
+ -[IXFileManager standardizeOwnershipAtURL:toUID:toGID:error:]
+ -[IXGlobalConfiguration promiseStagingRootAbortingOnErrorForInstallLocation:usingUniqueName:]
+ -[IXGlobalConfiguration promiseStagingRootForInstallLocation:usingUniqueName:error:]
+ -[IXOwnedDataPromise initWithName:client:diskSpaceNeeded:location:]
+ -[IXOwnedDataPromise location]
+ -[IXOwnedDataPromiseSeed init]
+ -[IXOwnedDataPromiseSeed location]
+ -[IXOwnedDataPromiseSeed setLocation:]
+ -[IXPlaceholder _doInitWithSpecification:error:]
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.1
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.2
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.3
+ -[IXPlaceholder _doInitWithSpecification:error:].cold.4
+ -[IXPlaceholder _initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:location:error:]
+ -[IXPlaceholder _initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:location:error:].cold.1
+ -[IXPlaceholder bundleDirectoryName]
+ -[IXPlaceholder initAppPlaceholderWithBundleName:bundleID:installType:client:location:error:]
+ -[IXPlaceholder initExtensionKitPlaceholderWithBundleName:bundleID:parentPlaceholder:client:location:error:]
+ -[IXPlaceholder initPlugInPlaceholderWithBundleName:bundleID:parentPlaceholder:client:location:error:]
+ -[IXPlaceholder initWithSpecification:error:]
+ -[IXPlaceholderAttributes cfBundleSupportedPlatforms]
+ -[IXPlaceholderAttributes dtPlatformName]
+ -[IXPlaceholderAttributes lsRequiresIPhoneOS]
+ -[IXPlaceholderAttributes setCfBundleSupportedPlatforms:]
+ -[IXPlaceholderAttributes setDtPlatformName:]
+ -[IXPlaceholderAttributes setLsRequiresIPhoneOS:]
+ -[IXPlaceholderSeed bundleDirectoryName]
+ -[IXPlaceholderSeed setBundleDirectoryName:]
+ -[IXPlaceholderSpecification .cxx_destruct]
+ -[IXPlaceholderSpecification bundleDirectoryName]
+ -[IXPlaceholderSpecification bundleID]
+ -[IXPlaceholderSpecification client]
+ -[IXPlaceholderSpecification initWithLocalizedBundleName:bundleID:type:client:location:]
+ -[IXPlaceholderSpecification installType]
+ -[IXPlaceholderSpecification localizedBundleName]
+ -[IXPlaceholderSpecification location]
+ -[IXPlaceholderSpecification parentPlaceholder]
+ -[IXPlaceholderSpecification placeholderType]
+ -[IXPlaceholderSpecification setBundleDirectoryName:]
+ -[IXPlaceholderSpecification setInstallType:]
+ -[IXPlaceholderSpecification setParentPlaceholder:]
+ -[IXProgressHint setTotalExpectedDataImportSizeInBytes:]
+ -[IXProgressHint totalExpectedDataImportSizeInBytes]
+ -[IXPromisedInMemoryData initWithName:client:data:location:]
+ -[IXPromisedInMemoryDictionary initWithName:client:dictionary:location:]
+ -[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:]
+ -[IXPromisedTransferToPath _doInitWithError:]
+ -[IXPromisedTransferToPath initWithName:client:diskSpaceNeeded:location:]
+ -[IXPromisedTransferToPath initWithName:client:transferPath:diskSpaceNeeded:location:]
+ -[IXPromisedTransferToPath initWithName:client:transferPath:diskSpaceNeeded:location:error:]
+ -[IXRefreshContainerOptions .cxx_destruct]
+ -[IXRefreshContainerOptions allowRefreshDuringPostProcessing]
+ -[IXRefreshContainerOptions containerTypes]
+ -[IXRefreshContainerOptions copyWithZone:]
+ -[IXRefreshContainerOptions description]
+ -[IXRefreshContainerOptions encodeWithCoder:]
+ -[IXRefreshContainerOptions forceTerminateApp]
+ -[IXRefreshContainerOptions hash]
+ -[IXRefreshContainerOptions initWithCoder:]
+ -[IXRefreshContainerOptions initWithReason:containerTypes:]
+ -[IXRefreshContainerOptions isEqual:]
+ -[IXRefreshContainerOptions reason]
+ -[IXRefreshContainerOptions setAllowRefreshDuringPostProcessing:]
+ -[IXRefreshContainerOptions setForceTerminateApp:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table16
+ GCC_except_table170
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table329
+ GCC_except_table34
+ GCC_except_table353
+ GCC_except_table355
+ GCC_except_table358
+ GCC_except_table361
+ GCC_except_table364
+ GCC_except_table37
+ GCC_except_table371
+ GCC_except_table40
+ GCC_except_table408
+ GCC_except_table411
+ GCC_except_table416
+ GCC_except_table420
+ GCC_except_table423
+ GCC_except_table426
+ GCC_except_table429
+ GCC_except_table43
+ GCC_except_table433
+ GCC_except_table436
+ GCC_except_table46
+ GCC_except_table52
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table96
+ GCC_except_table99
+ _IXStringForPlaceholderType
+ _OBJC_CLASS_$_IXPlaceholderSpecification
+ _OBJC_CLASS_$_IXRefreshContainerOptions
+ _OBJC_CLASS_$_MIHelperServiceFrameworkClient
+ _OBJC_CLASS_$_MILocation
+ _OBJC_CLASS_$_MILocationSystemDefinedBase
+ _OBJC_CLASS_$_MILocationSystemDefinedCommon
+ _OBJC_CLASS_$_MILocationUserDefined
+ _OBJC_CLASS_$_MILocationUserDefinedDirectory
+ _OBJC_IVAR_$_IXOwnedDataPromiseSeed._location
+ _OBJC_IVAR_$_IXPlaceholderAttributes._cfBundleSupportedPlatforms
+ _OBJC_IVAR_$_IXPlaceholderAttributes._dtPlatformName
+ _OBJC_IVAR_$_IXPlaceholderAttributes._lsRequiresIPhoneOS
+ _OBJC_IVAR_$_IXPlaceholderSeed._bundleDirectoryName
+ _OBJC_IVAR_$_IXPlaceholderSpecification._bundleDirectoryName
+ _OBJC_IVAR_$_IXPlaceholderSpecification._bundleID
+ _OBJC_IVAR_$_IXPlaceholderSpecification._client
+ _OBJC_IVAR_$_IXPlaceholderSpecification._installType
+ _OBJC_IVAR_$_IXPlaceholderSpecification._localizedBundleName
+ _OBJC_IVAR_$_IXPlaceholderSpecification._location
+ _OBJC_IVAR_$_IXPlaceholderSpecification._parentPlaceholder
+ _OBJC_IVAR_$_IXPlaceholderSpecification._placeholderType
+ _OBJC_IVAR_$_IXProgressHint._totalExpectedDataImportSizeInBytes
+ _OBJC_IVAR_$_IXRefreshContainerOptions._allowRefreshDuringPostProcessing
+ _OBJC_IVAR_$_IXRefreshContainerOptions._containerTypes
+ _OBJC_IVAR_$_IXRefreshContainerOptions._forceTerminateApp
+ _OBJC_IVAR_$_IXRefreshContainerOptions._reason
+ _OBJC_METACLASS_$_IXPlaceholderSpecification
+ _OBJC_METACLASS_$_IXRefreshContainerOptions
+ _OUTLINED_FUNCTION_17
+ __OBJC_$_CLASS_METHODS_IXRefreshContainerOptions
+ __OBJC_$_CLASS_PROP_LIST_IXRefreshContainerOptions
+ __OBJC_$_INSTANCE_METHODS_IXPlaceholderSpecification
+ __OBJC_$_INSTANCE_METHODS_IXRefreshContainerOptions
+ __OBJC_$_INSTANCE_VARIABLES_IXPlaceholderSpecification
+ __OBJC_$_INSTANCE_VARIABLES_IXRefreshContainerOptions
+ __OBJC_$_PROP_LIST_IXPlaceholderSpecification
+ __OBJC_$_PROP_LIST_IXRefreshContainerOptions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IXCoordinatorWithDataImportPromises
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IXCoordinatorWithDataImportPromises
+ __OBJC_$_PROTOCOL_REFS_IXCoordinatorWithDataImportPromises
+ __OBJC_CLASS_PROTOCOLS_$_IXRefreshContainerOptions
+ __OBJC_CLASS_RO_$_IXPlaceholderSpecification
+ __OBJC_CLASS_RO_$_IXRefreshContainerOptions
+ __OBJC_LABEL_PROTOCOL_$_IXCoordinatorWithDataImportPromises
+ __OBJC_METACLASS_RO_$_IXPlaceholderSpecification
+ __OBJC_METACLASS_RO_$_IXRefreshContainerOptions
+ __OBJC_PROTOCOL_$_IXCoordinatorWithDataImportPromises
+ ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.701
+ ___107+[IXAppInstallCoordinator cancelCoordinatorsForAppsWithApplicationIdentities:withReason:client:completion:]_block_invoke.78
+ ___111-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:]_block_invoke
+ ___111-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:]_block_invoke.8
+ ___113+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:]_block_invoke
+ ___113+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:]_block_invoke.1
+ ___113+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:]_block_invoke.1.cold.1
+ ___113+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:]_block_invoke.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.2
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.3
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.4
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.5
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.6
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.7
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.124
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.124.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.124.cold.2
+ ___31-[IXPlaceholder hasIconPromise]_block_invoke.239
+ ___32-[IXAppInstallCoordinator error]_block_invoke.288
+ ___32-[IXAppInstallCoordinator error]_block_invoke_2.289
+ ___32-[IXOwnedDataPromise stagedPath]_block_invoke.7
+ ___35-[IXPlaceholder setMetadata:error:]_block_invoke.317
+ ___35-[IXPlaceholder setSinfData:error:]_block_invoke.328
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.292
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.293
+ ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.227
+ ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.227.cold.1
+ ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.227.cold.2
+ ___38-[IXPlaceholder setIconPromise:error:]_block_invoke.226
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.304
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.305
+ ___39-[IXPlaceholder hasEntitlementsPromise]_block_invoke.281
+ ___40-[IXPlaceholder hasIconResourcesPromise]_block_invoke.259
+ ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.306
+ ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.307
+ ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.316
+ ___44-[IXAppInstallCoordinator hasInstallOptions]_block_invoke.216
+ ___44-[IXPlaceholder hasInfoPlistLoctablePromise]_block_invoke.287
+ ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.198
+ ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.248
+ ___45-[IXPlaceholder hasPlugInPlaceholderPromises]_block_invoke.306
+ ___45-[IXPromisedTransferToPath _doInitWithError:]_block_invoke
+ ___45-[IXPromisedTransferToPath _doInitWithError:]_block_invoke.3
+ ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.308
+ ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.277
+ ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.277.cold.1
+ ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.277.cold.2
+ ___46-[IXPlaceholder setEntitlementsPromise:error:]_block_invoke.276
+ ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.694
+ ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.220
+ ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.309
+ ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.219
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.290
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.291
+ ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.188
+ ___48-[IXPlaceholder _doInitWithSpecification:error:]_block_invoke
+ ___48-[IXPlaceholder _doInitWithSpecification:error:]_block_invoke.217
+ ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.285
+ ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.279
+ ___49-[IXPlaceholder infoPlistLocalizationsWithError:]_block_invoke.271
+ ___49-[IXPlaceholder setInfoPlistLocalizations:error:]_block_invoke.270
+ ___51-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke.217
+ ___51-[IXAppInstallCoordinator setInstallOptions:error:]_block_invoke.215
+ ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.283
+ ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.283.cold.1
+ ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.283.cold.2
+ ___51-[IXPlaceholder setConfigurationCompleteWithError:]_block_invoke.307
+ ___51-[IXPlaceholder setInfoPlistLoctablePromise:error:]_block_invoke.282
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.190
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.190.cold.1
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.190.cold.2
+ ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.189
+ ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.239
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.240
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.240.cold.1
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.240.cold.2
+ ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.282
+ ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.238
+ ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.287
+ ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.249
+ ___55-[IXAppInstallCoordinator dataImportPromisesWithError:]_block_invoke
+ ___55-[IXAppInstallCoordinator dataImportPromisesWithError:]_block_invoke.271
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.176
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.176.cold.1
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.176.cold.2
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.250
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.250.cold.1
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.250.cold.2
+ ___55-[IXAppInstallCoordinator setDataImportPromises:error:]_block_invoke
+ ___55-[IXAppInstallCoordinator setDataImportPromises:error:]_block_invoke.270
+ ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.175
+ ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.21
+ ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.21.cold.1
+ ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.22
+ ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.22.cold.1
+ ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.698
+ ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.161
+ ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.262
+ ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.261
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.702
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.703
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.704
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.685
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.687
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.688
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.691
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.692
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.256
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.256.cold.1
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.256.cold.2
+ ___58-[IXAppInstallCoordinator getHasDataImportPromises:error:]_block_invoke
+ ___58-[IXAppInstallCoordinator getHasDataImportPromises:error:]_block_invoke.275
+ ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.255
+ ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.278
+ ___58-[IXPlaceholder appExtensionPlaceholderPromisesWithError:]_block_invoke.298
+ ___58-[IXPlaceholder setAppExtensionPlaceholderPromises:error:]_block_invoke.297
+ ___59+[IXAppInstallCoordinator defaultAppMetadataListWithError:]_block_invoke.120
+ ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.265
+ ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.281
+ ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.264
+ ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.280
+ ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.254
+ ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.223
+ ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.222
+ ___60-[IXPromisedInMemoryData initWithName:client:data:location:]_block_invoke
+ ___60-[IXPromisedInMemoryData initWithName:client:data:location:]_block_invoke.6
+ ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.260
+ ___61-[IXFileManager standardizeOwnershipAtURL:toUID:toGID:error:]_block_invoke
+ ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.269
+ ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.263
+ ___64+[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]_block_invoke.122
+ ___64+[IXAppInstallCoordinator removabilityForAppWithIdentity:error:]_block_invoke.111
+ ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.251
+ ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.251.cold.1
+ ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.251.cold.2
+ ___65+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke.116
+ ___66+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]_block_invoke.118
+ ___66-[IXPromisedStreamingZipTransfer finishStreamWithCompletionBlock:]_block_invoke.26
+ ___67+[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]_block_invoke
+ ___67+[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]_block_invoke.276
+ ___68+[IXAppInstallCoordinator pauseCoordinatorForAppWithIdentity:error:]_block_invoke.79
+ ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.199
+ ___68-[IXPlaceholder setIconResourcesPromise:withInfoPlistContent:error:]_block_invoke.250
+ ___69+[IXAppInstallCoordinator removabilityForAppWithIdentity:completion:]_block_invoke.113
+ ___69+[IXAppInstallCoordinator resumeCoordinatorForAppWithIdentity:error:]_block_invoke.80
+ ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.204
+ ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.203
+ ___71+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]_block_invoke.121
+ ___71+[IXAppInstallCoordinator uninstallAppWithIdentity:options:completion:]_block_invoke.105
+ ___71+[IXAppInstallCoordinator uninstallAppWithIdentity:options:completion:]_block_invoke.106
+ ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.284
+ ___72-[IXPromisedInMemoryDictionary initWithName:client:dictionary:location:]_block_invoke
+ ___72-[IXPromisedInMemoryDictionary initWithName:client:dictionary:location:]_block_invoke.7
+ ___73+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:error:]_block_invoke.81
+ ___73+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:error:]_block_invoke.112
+ ___73+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke.131
+ ___75-[IXPromisedStreamingZipTransfer terminateStreamWithError:completionBlock:]_block_invoke.30
+ ___78+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:completion:]_block_invoke.82
+ ___78+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:completion:]_block_invoke.114
+ ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.695
+ ___79+[IXAppInstallCoordinator updateSINFForAppWithIdentity:sinfData:options:error:]_block_invoke.126
+ ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.684
+ ___81+[IXAppInstallCoordinator revertAppWithIdentity:completionWithApplicationRecord:]_block_invoke.110
+ ___82+[IXAppInstallCoordinator revertAppWithIdentity:resultingApplicationRecord:error:]_block_invoke.108
+ ___82+[IXAppInstallCoordinator setRemovability:forAppWithIdentity:byClient:completion:]_block_invoke.115
+ ___85+[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]_block_invoke
+ ___85+[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]_block_invoke.154
+ ___85+[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]_block_invoke.cold.1
+ ___92+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:]_block_invoke
+ ___92+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:]_block_invoke.4
+ ___92+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:]_block_invoke.4.cold.1
+ ___92+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:]_block_invoke.cold.1
+ ___97+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:]_block_invoke
+ ___97+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:]_block_invoke.5
+ ___97+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:]_block_invoke.5.cold.1
+ ___97+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:]_block_invoke.cold.1
+ ___98+[IXAppInstallCoordinator uninstallAppWithIdentity:options:disposition:error:legacyProgressBlock:]_block_invoke.96
+ ___block_descriptor_40_e79_B24?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8^16l
+ ___block_descriptor_40_e8_32r_e27_v24?0"NSSet"8"NSError"16lr32l8
+ ___block_descriptor_56_e8_32s40r48r_e27_v24?0"NSURL"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e50_v24?0"IXPromisedTransferToPathSeed"8"NSError"16lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e20_v20?0B8"NSError"12ls32l8s40l8r48l8r56l8
+ ___block_descriptor_81_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s56l8s48l8s64l8
+ ___block_literal_global.12
+ ___block_literal_global.37
+ ___block_literal_global.690
+ ___block_literal_global.697
+ ___block_literal_global.700
+ __kCFBundleSupportedPlatformsKey
+ _interface.weakInterface.330
+ _lchown
+ _objc_msgSend$_doInitWithError:
+ _objc_msgSend$_doInitWithSpecification:error:
+ _objc_msgSend$_iconContentForBundleAtURL:infoPlistIconContent:withStagingPath:error:
+ _objc_msgSend$_initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:location:error:
+ _objc_msgSend$_locationClassCluster
+ _objc_msgSend$_placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:
+ _objc_msgSend$_placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:location:error:
+ _objc_msgSend$_remote_IXSCoordinatedAppInstall:getDataImportPromises:
+ _objc_msgSend$_remote_IXSCoordinatedAppInstall:hasDataImportPromises:
+ _objc_msgSend$_remote_IXSCoordinatedAppInstall:setDataImportPromiseUUIDs:completion:
+ _objc_msgSend$_remote_addBundleIDs:toMappingsForPersona:completion:
+ _objc_msgSend$_remote_associateMultiPersonaAppsWithBundleIDs:withPersona:completion:
+ _objc_msgSend$_remote_refreshContainersWithOptions:forAppWithIdentity:completion:
+ _objc_msgSend$_remote_removeBundleIDs:fromMappingsForPersona:completion:
+ _objc_msgSend$_remote_stagingLocationForInstallLocation:completion:
+ _objc_msgSend$_setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:
+ _objc_msgSend$_temporaryStagingLocationForInstallLocation:error:
+ _objc_msgSend$allowRefreshDuringPostProcessing
+ _objc_msgSend$bundleDirectoryName
+ _objc_msgSend$cfBundleSupportedPlatforms
+ _objc_msgSend$containerTypes
+ _objc_msgSend$dtPlatformName
+ _objc_msgSend$firstObject
+ _objc_msgSend$forceTerminateApp
+ _objc_msgSend$initAppPlaceholderWithBundleName:bundleID:installType:client:location:error:
+ _objc_msgSend$initExtensionKitPlaceholderWithBundleName:bundleID:parentPlaceholder:client:location:error:
+ _objc_msgSend$initFromDelimitedString:
+ _objc_msgSend$initFromPlistDictionary:
+ _objc_msgSend$initPlugInPlaceholderWithBundleName:bundleID:parentPlaceholder:client:location:error:
+ _objc_msgSend$initWithBundleIdentifier:personaUniqueString:location:
+ _objc_msgSend$initWithLocalizedBundleName:bundleID:type:client:location:
+ _objc_msgSend$initWithName:client:data:location:
+ _objc_msgSend$initWithName:client:dictionary:location:
+ _objc_msgSend$initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:
+ _objc_msgSend$initWithName:client:transferPath:diskSpaceNeeded:location:error:
+ _objc_msgSend$initWithReason:containerTypes:
+ _objc_msgSend$initWithSpecification:error:
+ _objc_msgSend$localizedBundleName
+ _objc_msgSend$location
+ _objc_msgSend$locationFromPlistDictionary:error:
+ _objc_msgSend$lsRequiresIPhoneOS
+ _objc_msgSend$parentPlaceholder
+ _objc_msgSend$placeholderForInstallable:client:installType:metadata:location:error:
+ _objc_msgSend$placeholderFromSerializedPlaceholder:client:installType:location:error:
+ _objc_msgSend$promiseStagingRootForInstallLocation:usingUniqueName:error:
+ _objc_msgSend$reason
+ _objc_msgSend$refreshContainersWithOptions:forApplicationIdentity:error:
+ _objc_msgSend$setAllowRefreshDuringPostProcessing:
+ _objc_msgSend$setBundleDirectoryName:
+ _objc_msgSend$setCfBundleSupportedPlatforms:
+ _objc_msgSend$setDtPlatformName:
+ _objc_msgSend$setForceTerminateApp:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setLsRequiresIPhoneOS:
+ _objc_msgSend$setParentPlaceholder:
+ _objc_msgSend$setTotalExpectedDataImportSizeInBytes:
+ _objc_msgSend$stagingLocationForInstallLocation:error:
+ _objc_msgSend$stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:
+ _objc_msgSend$totalExpectedDataImportSizeInBytes
- +[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:].cold.1
- +[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:].cold.1
- +[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:].cold.1
- +[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:].cold.1
- +[IXPlaceholder _iconContentForBundleAtURL:infoPlistIconContent:error:]
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:]
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.1
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.10
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.11
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.12
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.13
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.14
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.15
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.16
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.17
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.18
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.19
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.2
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.20
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.21
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.22
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.23
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.3
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.4
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.5
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.6
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.7
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.8
- +[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:].cold.9
- +[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:error:]
- +[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:error:].cold.1
- +[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:error:].cold.2
- +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:]
- +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:].cold.1
- +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:].cold.2
- +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:].cold.3
- +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:].cold.4
- +[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:].cold.5
- +[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:error:].cold.1
- +[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:error:].cold.2
- -[IXFileManager createTemporaryIconsDirectoryWithError:]
- -[IXGlobalConfiguration createDirectories].cold.4
- -[IXGlobalConfiguration promiseStagingRootDirectoryAbortingOnError]
- -[IXGlobalConfiguration promiseStagingRootDirectoryAbortingOnError].cold.1
- -[IXGlobalConfiguration promiseStagingRootDirectoryWithError:]
- -[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:]
- -[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:].cold.1
- -[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:].cold.2
- -[IXPlaceholder _initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:error:]
- -[IXPlaceholder _initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:error:].cold.1
- -[IXPlaceholder _internalInitAppExtensionPlaceholderWithBundleName:bundleID:parentPlaceholder:placeholderType:client:error:]
- -[IXPlaceholder _internalInitAppExtensionPlaceholderWithBundleName:bundleID:parentPlaceholder:placeholderType:client:error:].cold.1
- -[IXPlaceholder _internalInitAppExtensionPlaceholderWithBundleName:bundleID:parentPlaceholder:placeholderType:client:error:].cold.2
- -[IXPlaceholder setBundleID:]
- -[IXPlaceholder setBundleName:]
- -[IXPromisedTransferToPath _doInit]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table107
- GCC_except_table110
- GCC_except_table169
- GCC_except_table173
- GCC_except_table177
- GCC_except_table180
- GCC_except_table183
- GCC_except_table186
- GCC_except_table189
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table201
- GCC_except_table204
- GCC_except_table207
- GCC_except_table210
- GCC_except_table213
- GCC_except_table216
- GCC_except_table219
- GCC_except_table222
- GCC_except_table225
- GCC_except_table228
- GCC_except_table23
- GCC_except_table231
- GCC_except_table234
- GCC_except_table237
- GCC_except_table240
- GCC_except_table243
- GCC_except_table246
- GCC_except_table249
- GCC_except_table252
- GCC_except_table255
- GCC_except_table258
- GCC_except_table261
- GCC_except_table264
- GCC_except_table267
- GCC_except_table270
- GCC_except_table284
- GCC_except_table287
- GCC_except_table29
- GCC_except_table290
- GCC_except_table293
- GCC_except_table296
- GCC_except_table299
- GCC_except_table302
- GCC_except_table305
- GCC_except_table308
- GCC_except_table315
- GCC_except_table32
- GCC_except_table339
- GCC_except_table341
- GCC_except_table344
- GCC_except_table347
- GCC_except_table35
- GCC_except_table357
- GCC_except_table39
- GCC_except_table394
- GCC_except_table397
- GCC_except_table402
- GCC_except_table405
- GCC_except_table406
- GCC_except_table409
- GCC_except_table41
- GCC_except_table412
- GCC_except_table415
- GCC_except_table422
- GCC_except_table44
- GCC_except_table47
- GCC_except_table53
- GCC_except_table56
- GCC_except_table59
- GCC_except_table62
- GCC_except_table69
- GCC_except_table73
- GCC_except_table76
- GCC_except_table92
- GCC_except_table95
- GCC_except_table98
- ___102-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:]_block_invoke
- ___102-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:]_block_invoke.7
- ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.689
- ___107+[IXAppInstallCoordinator cancelCoordinatorsForAppsWithApplicationIdentities:withReason:client:completion:]_block_invoke.76
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.1
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.2
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.3
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.4
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.5
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.6
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.7
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.8
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.121
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.121.cold.1
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.121.cold.2
- ___31-[IXPlaceholder hasIconPromise]_block_invoke.228
- ___32-[IXAppInstallCoordinator error]_block_invoke.282
- ___32-[IXAppInstallCoordinator error]_block_invoke_2.283
- ___32-[IXOwnedDataPromise stagedPath]_block_invoke.5
- ___35-[IXPlaceholder setMetadata:error:]_block_invoke.306
- ___35-[IXPlaceholder setSinfData:error:]_block_invoke.317
- ___35-[IXPromisedTransferToPath _doInit]_block_invoke
- ___35-[IXPromisedTransferToPath _doInit]_block_invoke.3
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.286
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.287
- ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.216
- ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.216.cold.1
- ___38-[IXPlaceholder iconPromiseWithError:]_block_invoke.216.cold.2
- ___38-[IXPlaceholder setIconPromise:error:]_block_invoke.215
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.298
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.299
- ___39-[IXPlaceholder hasEntitlementsPromise]_block_invoke.270
- ___40-[IXPlaceholder hasIconResourcesPromise]_block_invoke.248
- ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.300
- ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.301
- ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.310
- ___44-[IXAppInstallCoordinator hasInstallOptions]_block_invoke.218
- ___44-[IXPlaceholder hasInfoPlistLoctablePromise]_block_invoke.276
- ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.200
- ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.250
- ___45-[IXPlaceholder hasPlugInPlaceholderPromises]_block_invoke.295
- ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.302
- ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.266
- ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.266.cold.1
- ___46-[IXPlaceholder entitlementsPromiseWithError:]_block_invoke.266.cold.2
- ___46-[IXPlaceholder setEntitlementsPromise:error:]_block_invoke.265
- ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.682
- ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.222
- ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.303
- ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.221
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.284
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.285
- ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.190
- ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.279
- ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.273
- ___49-[IXPlaceholder infoPlistLocalizationsWithError:]_block_invoke.260
- ___49-[IXPlaceholder setInfoPlistLocalizations:error:]_block_invoke.259
- ___51-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke.219
- ___51-[IXAppInstallCoordinator setInstallOptions:error:]_block_invoke.217
- ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.272
- ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.272.cold.1
- ___51-[IXPlaceholder infoPlistLoctablePromiseWithError:]_block_invoke.272.cold.2
- ___51-[IXPlaceholder setConfigurationCompleteWithError:]_block_invoke.296
- ___51-[IXPlaceholder setInfoPlistLoctablePromise:error:]_block_invoke.271
- ___51-[IXPromisedInMemoryData initWithName:client:data:]_block_invoke
- ___51-[IXPromisedInMemoryData initWithName:client:data:]_block_invoke.5
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.192
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.192.cold.1
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.192.cold.2
- ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.191
- ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.241
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.242
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.242.cold.1
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.242.cold.2
- ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.276
- ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.240
- ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.281
- ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.251
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.178
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.178.cold.1
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.178.cold.2
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.252
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.252.cold.1
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.252.cold.2
- ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.177
- ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.20
- ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.20.cold.1
- ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.21
- ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.21.cold.1
- ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.686
- ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.163
- ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.264
- ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.263
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.690
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.691
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.692
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.673
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.675
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.676
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.679
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.680
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.258
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.258.cold.1
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.258.cold.2
- ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.257
- ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.272
- ___58-[IXPlaceholder appExtensionPlaceholderPromisesWithError:]_block_invoke.287
- ___58-[IXPlaceholder setAppExtensionPlaceholderPromises:error:]_block_invoke.286
- ___59+[IXAppInstallCoordinator defaultAppMetadataListWithError:]_block_invoke.118
- ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.267
- ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.275
- ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.266
- ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.274
- ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.256
- ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.225
- ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.224
- ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.262
- ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.271
- ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.265
- ___63-[IXPromisedInMemoryDictionary initWithName:client:dictionary:]_block_invoke
- ___63-[IXPromisedInMemoryDictionary initWithName:client:dictionary:]_block_invoke.6
- ___64+[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]_block_invoke.121
- ___64+[IXAppInstallCoordinator removabilityForAppWithIdentity:error:]_block_invoke.109
- ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.240
- ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.240.cold.1
- ___64-[IXPlaceholder iconResourcesPromiseWithInfoPlistContent:error:]_block_invoke.240.cold.2
- ___65+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke.114
- ___66+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]_block_invoke.116
- ___66-[IXPromisedStreamingZipTransfer finishStreamWithCompletionBlock:]_block_invoke.25
- ___68+[IXAppInstallCoordinator pauseCoordinatorForAppWithIdentity:error:]_block_invoke.77
- ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.201
- ___68-[IXPlaceholder setIconResourcesPromise:withInfoPlistContent:error:]_block_invoke.239
- ___69+[IXAppInstallCoordinator removabilityForAppWithIdentity:completion:]_block_invoke.111
- ___69+[IXAppInstallCoordinator resumeCoordinatorForAppWithIdentity:error:]_block_invoke.78
- ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.206
- ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.205
- ___71+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]_block_invoke.120
- ___71+[IXAppInstallCoordinator uninstallAppWithIdentity:options:completion:]_block_invoke.103
- ___71+[IXAppInstallCoordinator uninstallAppWithIdentity:options:completion:]_block_invoke.104
- ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.278
- ___73+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:error:]_block_invoke.79
- ___73+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:error:]_block_invoke.110
- ___73+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke.130
- ___75-[IXPromisedStreamingZipTransfer terminateStreamWithError:completionBlock:]_block_invoke.29
- ___78+[IXAppInstallCoordinator prioritizeCoordinatorForAppWithIdentity:completion:]_block_invoke.80
- ___78+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:completion:]_block_invoke.112
- ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.683
- ___79+[IXAppInstallCoordinator updateSINFForAppWithIdentity:sinfData:options:error:]_block_invoke.125
- ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.672
- ___81+[IXAppInstallCoordinator revertAppWithIdentity:completionWithApplicationRecord:]_block_invoke.108
- ___82+[IXAppInstallCoordinator revertAppWithIdentity:resultingApplicationRecord:error:]_block_invoke.106
- ___82+[IXAppInstallCoordinator setRemovability:forAppWithIdentity:byClient:completion:]_block_invoke.113
- ___82-[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:]_block_invoke
- ___82-[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:]_block_invoke.209
- ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke
- ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke.155
- ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke.cold.1
- ___98+[IXAppInstallCoordinator uninstallAppWithIdentity:options:disposition:error:legacyProgressBlock:]_block_invoke.94
- ___block_descriptor_48_e8_32s40r_e50_v24?0"IXPromisedTransferToPathSeed"8"NSError"16lr40l8s32l8
- ___block_descriptor_81_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s56l8s40l8s48l8s64l8
- ___block_literal_global.36
- ___block_literal_global.678
- ___block_literal_global.685
- ___block_literal_global.688
- ___block_literal_global.8
- _interface.weakInterface.315
- _objc_msgSend$_doInit
- _objc_msgSend$_doInitWithBundleName:bundleID:installType:placeholderType:error:
- _objc_msgSend$_iconContentForBundleAtURL:infoPlistIconContent:error:
- _objc_msgSend$_initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:error:
- _objc_msgSend$_internalInitAppExtensionPlaceholderWithBundleName:bundleID:parentPlaceholder:placeholderType:client:error:
- _objc_msgSend$_placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:
- _objc_msgSend$_placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:error:
- _objc_msgSend$_remote_refreshContainerTypes:forAppWithIdentity:reason:completion:
- _objc_msgSend$_setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:
- _objc_msgSend$createTemporaryIconsDirectoryWithError:
- _objc_msgSend$iconStagingDirectoryWithError:
- _objc_msgSend$initAppPlaceholderWithBundleName:bundleID:installType:client:error:
- _objc_msgSend$initWithBundleID:persona:
- _objc_msgSend$initWithName:client:data:
- _objc_msgSend$initWithName:client:dictionary:
- _objc_msgSend$initWithName:client:transferPath:diskSpaceNeeded:
- _objc_msgSend$promiseStagingRootDirectoryWithError:
- _objc_msgSend$refreshContainerTypes:forApplicationIdentity:reason:error:
CStrings:
+ "\t"
+ "%@ Placeholder: %@ (%@)"
+ "%s: App extension placeholder %@ did not specify a parent placeholder; this is not allowed. : %@"
+ "%s: App extension placeholder for %@ specified another app extension, %@, as its parent. App extension placeholders must have an app placeholder as their parent. : %@"
+ "%s: App placeholder %@ specified parent placeholder; this is not allowed. : %@"
+ "%s: Daemon returned error from setting up placeholder promise: %@"
+ "%s: Failed to add data separated apps: %@ with persona %@ : %@"
+ "%s: Failed to check if %@ has data import promises: %@"
+ "%s: Failed to clean up staged content at %@ : %@"
+ "%s: Failed to create temporary staging directory for installation : %@"
+ "%s: Failed to get data import promises: %@"
+ "%s: Failed to get temporary staging directory for install location %@: %@"
+ "%s: Failed to remove data separated apps: %@ with persona %@ : %@"
+ "%s: Failed to set data import promises on %@ : %@"
+ "%s: Failed to set data separated apps: %@ with persona %@ : %@"
+ "%s: Invalid placeholder type %lu : %@"
+ "%s: No install type was specified for placeholder %@. This value is required. : %@"
+ "%s: Plist key [%@] faled to decode; error = %@"
+ "%s: Plist key [%@] is missing or of the wrong type; expected = [NSDictionary], got = %@"
+ "%s: Plist key [%@] is missing or of the wrong type; expected = [NSString], got = %@"
+ "%s: Plist key is of the wrong type; expected = [NSString|NSDictionary], got = %@"
+ "+[IXAppInstallCoordinator refreshContainersWithOptions:forApplicationIdentity:error:]_block_invoke"
+ "+[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:]_block_invoke"
+ "+[IXPlaceholder _iconContentForBundleAtURL:infoPlistIconContent:withStagingPath:error:]"
+ "+[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:]"
+ "+[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:location:error:]"
+ "+[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:]"
+ "+[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:location:error:]"
+ "-[IXAppInstallCoordinator dataImportPromisesWithError:]"
+ "-[IXAppInstallCoordinator dataImportPromisesWithError:]_block_invoke"
+ "-[IXAppInstallCoordinator getHasDataImportPromises:error:]_block_invoke"
+ "-[IXAppInstallCoordinator setDataImportPromises:error:]_block_invoke"
+ "-[IXAppInstallCoordinator setPreserveTargetBundleNameOnUpdate:error:]"
+ "-[IXApplicationIdentity initFromDelimitedString:]"
+ "-[IXApplicationIdentity initFromPlistDictionary:]"
+ "-[IXFileManager standardizeOwnershipAtURL:toUID:toGID:error:]_block_invoke"
+ "-[IXPlaceholder _doInitWithSpecification:error:]"
+ "-[IXPlaceholder _doInitWithSpecification:error:]_block_invoke"
+ "-[IXPlaceholder _initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:location:error:]"
+ "-[IXPromisedInMemoryData initWithName:client:data:location:]_block_invoke"
+ "-[IXPromisedInMemoryDictionary initWithName:client:dictionary:location:]"
+ "-[IXPromisedInMemoryDictionary initWithName:client:dictionary:location:]_block_invoke"
+ "-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:]"
+ "-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:]_block_invoke"
+ "-[IXPromisedTransferToPath _doInitWithError:]_block_invoke"
+ "<%@<%p> : %@ containerTypes=%lx allowRefreshDuringPostProcessing=%d forceTerminateApp=%d>"
+ "@\"<MILocationProtocol>\""
+ "@\"IXPlaceholder\""
+ "@40@0:8@16@24^@32"
+ "@48@0:8@16Q24@32@40"
+ "@48@0:8@16Q24Q32@40"
+ "@48@0:8@16^@24@32^@40"
+ "@56@0:8@16@24Q32Q40@48"
+ "@56@0:8@16Q24@32Q40@48"
+ "@64@0:8@16@24@32Q40@48^@56"
+ "@64@0:8@16@24Q32Q40@48^@56"
+ "@64@0:8@16Q24@32Q40Q48@56"
+ "@64@0:8@16Q24Q32@40@48^@56"
+ "@68@0:8@16Q24Q32@40B48@52^@60"
+ "@72@0:8@16@24@32@40Q48@56^@64"
+ "@88@0:8@16Q24@32Q40@48Q56B64B68@72^@80"
+ "App"
+ "App extension placeholder %@ did not specify a parent placeholder; this is not allowed."
+ "App extension placeholder for %@ specified another app extension, %@, as its parent. App extension placeholders must have an app placeholder as their parent."
+ "App placeholder %@ specified parent placeholder; this is not allowed."
+ "B40@0:8@16I24I28^@32"
+ "B64@0:8@16@24Q32@40@48^@56"
+ "Cross-platform Migration"
+ "DTPlatformName"
+ "Duplicate app extension bundle directory names."
+ "ExtensionKit"
+ "Extracted"
+ "Failed to create temporary staging directory for installation"
+ "Failed to get icon content for bundle with identifier %@ at %@ : %@; skipping icon resources promise"
+ "Failed to get promise staging directory for install location %@ with uniqueName %@: %@"
+ "Failed to lchown %s with uid/gid %d/%d : %s"
+ "IXAppCoordinationStateDataImportPromisesIncomplete"
+ "IXAppCoordinationStateDataImportPromisesNotSet"
+ "IXCoordinatorWithDataImportPromises"
+ "IXPlaceholderSpecification"
+ "IXRefreshContainerOptions"
+ "Invalid placeholder type %lu"
+ "LSRequiresIPhoneOS"
+ "Mismatched location."
+ "No data import promises are currently set."
+ "No icon found for bundle %@ at %@; skipping icon resources promise"
+ "No install type was specified for placeholder %@. This value is required."
+ "PlugInKit"
+ "T@\"<MILocationProtocol>\",&,N,V_location"
+ "T@\"<MILocationProtocol>\",R,C,N,V_location"
+ "T@\"<MILocationProtocol>\",R,N"
+ "T@\"IXPlaceholder\",W,N,V_parentPlaceholder"
+ "T@\"NSArray\",C,N,V_cfBundleSupportedPlatforms"
+ "T@\"NSNumber\",&,N,V_totalExpectedDataImportSizeInBytes"
+ "T@\"NSString\",C,N,V_bundleDirectoryName"
+ "T@\"NSString\",C,N,V_dtPlatformName"
+ "T@\"NSString\",R,C,N,V_bundleID"
+ "T@\"NSString\",R,C,N,V_localizedBundleName"
+ "T@\"NSString\",R,N,V_reason"
+ "TB,N,V_allowRefreshDuringPostProcessing"
+ "TB,N,V_forceTerminateApp"
+ "TB,N,V_lsRequiresIPhoneOS"
+ "TQ,R,N,V_containerTypes"
+ "TQ,R,N,V_placeholderType"
+ "Target install volume has been unmounted."
+ "Unknown IXPlaceholderType value %lu"
+ "_allowRefreshDuringPostProcessing"
+ "_bundleDirectoryName"
+ "_cfBundleSupportedPlatforms"
+ "_containerTypes"
+ "_doInitWithError:"
+ "_doInitWithSpecification:error:"
+ "_dtPlatformName"
+ "_forceTerminateApp"
+ "_iconContentForBundleAtURL:infoPlistIconContent:withStagingPath:error:"
+ "_initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:location:error:"
+ "_localizedBundleName"
+ "_location"
+ "_locationClassCluster"
+ "_lsRequiresIPhoneOS"
+ "_parentPlaceholder"
+ "_placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:location:error:"
+ "_placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:location:error:"
+ "_reason"
+ "_remote_IXSCoordinatedAppInstall:getDataImportPromises:"
+ "_remote_IXSCoordinatedAppInstall:hasDataImportPromises:"
+ "_remote_IXSCoordinatedAppInstall:setDataImportPromiseUUIDs:completion:"
+ "_remote_addBundleIDs:toMappingsForPersona:completion:"
+ "_remote_associateMultiPersonaAppsWithBundleIDs:withPersona:completion:"
+ "_remote_refreshContainersWithOptions:forAppWithIdentity:completion:"
+ "_remote_removeBundleIDs:fromMappingsForPersona:completion:"
+ "_remote_stagingLocationForInstallLocation:completion:"
+ "_setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:location:error:"
+ "_temporaryStagingLocationForInstallLocation:error:"
+ "_totalExpectedDataImportSizeInBytes"
+ "allowRefreshDuringPostProcessing"
+ "bundleDirectoryName"
+ "cfBundleSupportedPlatforms"
+ "containerTypes"
+ "dataImportPromisesWithError:"
+ "dtPlatformName"
+ "firstObject"
+ "forceTerminateApp"
+ "getHasDataImportPromises:error:"
+ "initAppPlaceholderWithBundleName:bundleID:installType:client:location:error:"
+ "initExtensionKitPlaceholderWithBundleName:bundleID:parentPlaceholder:client:location:error:"
+ "initFromDelimitedString:"
+ "initFromPlistDictionary:"
+ "initPlugInPlaceholderWithBundleName:bundleID:parentPlaceholder:client:location:error:"
+ "initWithBundleID:"
+ "initWithBundleID:personaUniqueString:location:"
+ "initWithBundleIdentifier:personaUniqueString:location:"
+ "initWithLocalizedBundleName:bundleID:type:client:location:"
+ "initWithName:client:data:location:"
+ "initWithName:client:dictionary:location:"
+ "initWithName:client:diskSpaceNeeded:location:"
+ "initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:"
+ "initWithName:client:transferPath:diskSpaceNeeded:location:"
+ "initWithName:client:transferPath:diskSpaceNeeded:location:error:"
+ "initWithReason:containerTypes:"
+ "initWithSpecification:error:"
+ "localizedBundleName"
+ "location"
+ "locationFromPlistDictionary:error:"
+ "locationType"
+ "lsRequiresIPhoneOS"
+ "parentPlaceholder"
+ "personaString"
+ "placeholderForInstallable:client:installType:metadata:location:error:"
+ "placeholderFromSerializedPlaceholder:client:installType:location:error:"
+ "promiseStagingRootAbortingOnErrorForInstallLocation:usingUniqueName:"
+ "promiseStagingRootForInstallLocation:usingUniqueName:error:"
+ "realPathForURL:"
+ "reason"
+ "refreshContainersWithOptions:forApplicationIdentity:error:"
+ "setAllowRefreshDuringPostProcessing:"
+ "setBundleDirectoryName:"
+ "setCfBundleSupportedPlatforms:"
+ "setDataImportPromises:error:"
+ "setDtPlatformName:"
+ "setForceTerminateApp:"
+ "setLocation:"
+ "setLsRequiresIPhoneOS:"
+ "setParentPlaceholder:"
+ "setPreserveTargetBundleNameOnUpdate:error:"
+ "setTotalExpectedDataImportSizeInBytes:"
+ "stagingLocationForInstallLocation:error:"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
+ "standardizeOwnershipAtURL:toUID:toGID:error:"
+ "totalExpectedDataImportSizeInBytes"
+ "v32@0:8@\"<MILocationProtocol>\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v40@0:8@\"IXRefreshContainerOptions\"16@\"IXApplicationIdentity\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"NSArray\"16@\"NSError\"24Q32@?<v@?@\"NSSet\"@\"NSError\">40"
- "%s is not available on this platform."
- "%s: %s is not available on this platform. : %@"
- "%s: Bundle ID argument was nil. : %@"
- "%s: Bundle Name argument was nil. : %@"
- "%s: Failed tell daemon to set up placeholder promise: %@"
- "%s: Failed to clean up extracted content at %@ : %@"
- "%s: Failed to create IXPromisedTransferToPath for entitlements for %@ : %@"
- "%s: Failed to create IXPromisedTransferToPath for icon resources at %@ for %@ : %@"
- "%s: Failed to create IXPromisedTransferToPath for loctable for %@ : %@"
- "%s: Failed to create app asset promise : %@"
- "%s: Failed to get icon content for bundle with identifier %@ at %@ : %@"
- "%s: No icon found for bundle %@ at %@"
- "%s: Reason passed to %s was nil : %@"
- "%s: parentPlaceholder argument must be an app placeholder but was an app extension placeholder"
- "%s: parentPlaceholder argument was unexpectedly nil!"
- "+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]"
- "+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke"
- "+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) addBundleIDs:toMappingsForPersona:error:]"
- "+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) associateMultiPersonaAppsWithBundleIDs:withPersona:withError:]"
- "+[IXAppInstallCoordinator(IXPersonaBasedMultiUser) removeBundleIDs:fromMappingsForPersona:error:]"
- "+[IXPlaceholder _iconContentForBundleAtURL:infoPlistIconContent:error:]"
- "+[IXPlaceholder _placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:]"
- "+[IXPlaceholder _placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:error:]"
- "+[IXPlaceholder _setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:]"
- "+[IXPlaceholder placeholderFromSerializedPlaceholder:client:installType:error:]"
- "-[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:]"
- "-[IXPlaceholder _doInitWithBundleName:bundleID:installType:placeholderType:error:]_block_invoke"
- "-[IXPlaceholder _initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:error:]"
- "-[IXPlaceholder _internalInitAppExtensionPlaceholderWithBundleName:bundleID:parentPlaceholder:placeholderType:client:error:]"
- "-[IXPromisedInMemoryData initWithName:client:data:]_block_invoke"
- "-[IXPromisedInMemoryDictionary initWithName:client:dictionary:]"
- "-[IXPromisedInMemoryDictionary initWithName:client:dictionary:]_block_invoke"
- "-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:]"
- "-[IXPromisedStreamingZipTransfer initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:]_block_invoke"
- "-[IXPromisedTransferToPath _doInit]_block_invoke"
- "@40@0:8@16^@24^@32"
- "@60@0:8@16Q24Q32@40B48^@52"
- "@64@0:8@16@24@32@40Q48^@56"
- "@80@0:8@16Q24@32Q40@48Q56B64B68^@72"
- "B56@0:8@16@24Q32@40^@48"
- "B56@0:8@16@24Q32Q40^@48"
- "B64@0:8@16@24@32Q40Q48^@56"
- "Bundle ID argument was nil."
- "Bundle Name argument was nil."
- "Failed to create IXPromisedTransferToPath for entitlements for %@"
- "Failed to create IXPromisedTransferToPath for icon resources at %@ for %@"
- "Failed to create IXPromisedTransferToPath for loctable for %@"
- "Failed to create app asset promise"
- "Failed to create staging root at %@ : %@"
- "Failed to get promise staging directory: %@"
- "Failed to get staging root path: %@"
- "PromiseStaging"
- "Reason passed to %s was nil"
- "_doInit"
- "_doInitWithBundleName:bundleID:installType:placeholderType:error:"
- "_iconContentForBundleAtURL:infoPlistIconContent:error:"
- "_initAppExtensionPlaceholderWithBundleURL:bundleName:bundleID:parentPlaceholder:client:error:"
- "_internalInitAppExtensionPlaceholderWithBundleName:bundleID:parentPlaceholder:placeholderType:client:error:"
- "_placeholderForBundle:client:withParent:installType:metadata:placeholderType:mayBeDeltaPackage:isFromSerializedPlaceholder:error:"
- "_placeholderForInstallable:client:installType:metadata:isFromSerializedPlaceholder:error:"
- "_remote_refreshContainerTypes:forAppWithIdentity:reason:completion:"
- "_setEntitlementsFromBundleExecutableURL:withBundleID:client:onPlaceholder:error:"
- "createTemporaryIconsDirectoryWithError:"
- "promiseStagingRootDirectoryAbortingOnError"
- "promiseStagingRootDirectoryWithError:"
- "v48@0:8@\"NSArray\"16@\"NSError\"24Q32@?<v@?B@\"NSError\">40"
- "v48@0:8Q16@\"IXApplicationIdentity\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8Q16@24@32@?40"

```
