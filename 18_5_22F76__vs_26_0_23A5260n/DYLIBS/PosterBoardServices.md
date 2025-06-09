## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-228.5.12.0.0
-  __TEXT.__text: 0x44c20
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x368c
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x44e3
-  __TEXT.__gcc_except_tab: 0x6c8
-  __TEXT.__oslogstring: 0x2470
-  __TEXT.__dlopen_cstrs: 0x1c2
-  __TEXT.__unwind_info: 0xf20
-  __TEXT.__objc_classname: 0x7bc
-  __TEXT.__objc_methname: 0x92dd
-  __TEXT.__objc_methtype: 0x18a0
-  __TEXT.__objc_stubs: 0x5b80
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0xf70
-  __DATA_CONST.__objc_classlist: 0x1d8
+276.105.0.0.0
+  __TEXT.__text: 0x45748
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x393c
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x44bf
+  __TEXT.__gcc_except_tab: 0x764
+  __TEXT.__oslogstring: 0x159b
+  __TEXT.__dlopen_cstrs: 0x203
+  __TEXT.__unwind_info: 0xf48
+  __TEXT.__objc_classname: 0x860
+  __TEXT.__objc_methname: 0x9e5e
+  __TEXT.__objc_methtype: 0x1a34
+  __TEXT.__objc_stubs: 0x5d60
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x1118
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cf8
+  __DATA_CONST.__objc_selrefs: 0x1de0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1b8
-  __AUTH_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__objc_superrefs: 0x1e0
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x32a0
-  __AUTH_CONST.__objc_const: 0xb000
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3b4
-  __DATA.__data: 0x560
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xd20
+  __AUTH_CONST.__cfstring: 0x3320
+  __AUTH_CONST.__objc_const: 0xb778
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x3ec
+  __DATA.__data: 0x5c0
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
+  - /System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit
+  - /System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 64247BD1-2427-330F-8DED-E437690BC7E3
-  Functions: 1622
-  Symbols:   5805
-  CStrings:  2684
+  UUID: D074CAE5-9175-3E68-8682-8C6E6463EB55
+  Functions: 1616
+  Symbols:   5772
+  CStrings:  2692
 
Symbols:
+ +[PRSCodableImage createCGImageFromCPBitmapData:error:]
+ +[PRSCodableImage createCGImageFromData:error:].cold.2
+ +[PRSCodableImage createCGImageFromURL:error:].cold.2
+ +[PRSControl supportsBSXPCSecureCoding]
+ +[PRSControl supportsSecureCoding]
+ +[PRSGadget supportsBSXPCSecureCoding]
+ +[PRSGadget supportsSecureCoding]
+ +[PRSMutablePosterConfiguration mutableConfigurationWithProvider:descriptorIdentifier:role:]
+ +[PRSMutablePosterConfiguration mutableConfigurationWithProvider:descriptorIdentifier:role:].cold.1
+ +[PRSPosterCollection postersAtProviderURL:type:fileManager:error:]
+ +[PRSPosterCollection postersAtURL:error:]
+ +[PRSPosterCollection specificType]
+ +[PRSPosterCollection validatePoster:]
+ +[PRSPosterConfigurationCollection specificType]
+ +[PRSPosterDescriptorCollection specificType]
+ +[PRSPosterDescriptorCollection validatePoster:]
+ +[PRSPosterStaticDescriptorCollection specificType]
+ +[PRSPosterUpdate posterUpdateHomeScreenIconTintSource:]
+ +[PRSPosterUpdate posterUpdateHomeScreenIconUserInterfaceStyleVariant:]
+ +[PRSPosterUpdate posterUpdateHomeScreenTintWithVariation:saturation:luminance:alpha:]
+ +[PRSPosterUpdate posterUpdateUserSelectedHomeScreenIconStyleVariantsForTypes:]
+ -[PRSControl controlIdentity]
+ -[PRSControl controlType]
+ -[PRSControl copyWithZone:]
+ -[PRSControl descriptionBuilderWithMultilinePrefix:]
+ -[PRSControl encodeWithBSXPCCoder:]
+ -[PRSControl encodeWithCoder:]
+ -[PRSControl hash]
+ -[PRSControl initWithBSXPCCoder:]
+ -[PRSControl initWithCoder:]
+ -[PRSControl initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:controlType:intent:]
+ -[PRSControl initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:controlType:intent:].cold.1
+ -[PRSControl initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:controlType:intent:].cold.2
+ -[PRSControl isEqual:]
+ -[PRSControl setControlType:]
+ -[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:]
+ -[PRSExternalSystemService fetchHomeScreenWallpaperForOrientation:completion:]
+ -[PRSExternalSystemService fetchHomeScreenWallpaperWithCompletion:]
+ -[PRSExternalSystemService fetchLockScreenWallpaperForOrientation:completion:]
+ -[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]
+ -[PRSExternalSystemService fetchLockScreenWallpaperForType:variant:options:orientation:completion:]
+ -[PRSExternalSystemService fetchLockScreenWallpaperForType:variant:options:orientation:completion:].cold.1
+ -[PRSExternalSystemService fetchLockScreenWallpaperWithCompletion:]
+ -[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:completion:]
+ -[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]
+ -[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:].cold.1
+ -[PRSGadget .cxx_destruct]
+ -[PRSGadget containerBundleIdentifier]
+ -[PRSGadget copyWithZone:]
+ -[PRSGadget descriptionBuilderWithMultilinePrefix:]
+ -[PRSGadget descriptionWithMultilinePrefix:]
+ -[PRSGadget description]
+ -[PRSGadget encodeWithBSXPCCoder:]
+ -[PRSGadget encodeWithCoder:]
+ -[PRSGadget extensionBundleIdentifier]
+ -[PRSGadget hash]
+ -[PRSGadget initWithBSXPCCoder:]
+ -[PRSGadget initWithCoder:]
+ -[PRSGadget initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:intent:]
+ -[PRSGadget intent]
+ -[PRSGadget isEqual:]
+ -[PRSGadget kind]
+ -[PRSGadget setContainerBundleIdentifier:]
+ -[PRSGadget setExtensionBundleIdentifier:]
+ -[PRSGadget setIntent:]
+ -[PRSGadget setKind:]
+ -[PRSGadget setUniqueIdentifier:]
+ -[PRSGadget succinctDescriptionBuilder]
+ -[PRSGadget succinctDescription]
+ -[PRSGadget uniqueIdentifier]
+ -[PRSMigrationDescriptor homeScreenIconStyleVariant]
+ -[PRSMigrationDescriptor homeScreenIconStyleVariantsForStyles]
+ -[PRSMigrationDescriptor homeScreenIconTintSource]
+ -[PRSMigrationDescriptor setHomeScreenIconStyleVariant:]
+ -[PRSMigrationDescriptor setHomeScreenIconStyleVariantsForStyles:]
+ -[PRSMigrationDescriptor setHomeScreenIconTintSource:]
+ -[PRSPosterConfigurationAttributes descriptorIdentifier]
+ -[PRSPosterDescriptor descriptorIdentifier]
+ -[PRSPosterDescriptorCollection dealloc]
+ -[PRSPosterDescriptorCollection mutableDescriptors]
+ -[PRSPosterDescriptorCollectionDiff initWithCollection:otherCollection:]
+ -[PRSPosterGalleryLayout description]
+ -[PRSPosterRoleActivePosterObserverState description]
+ -[PRSPosterRoleActivePosterObserverState initWithRole:activePoster:suggestions:]
+ -[PRSPosterRoleActivePosterObserverState isEqual:]
+ -[PRSPosterRoleActivePosterObserverState suggestions]
+ -[PRSPosterSnapshot writePNGToURL:error:]
+ -[PRSPosterSnapshot writePNGToURL:error:].cold.1
+ -[PRSPosterSnapshotCollection _populateSalientContentRectFromSurfacesIfPossible]
+ -[PRSPosterSnapshotCollection initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayIdentity:salientContentRectangle:]
+ -[PRSPosterSnapshotCollection salientContentRectangle]
+ -[PRSPosterSnapshotRequest initWithConfigurationType:variantType:options:orientation:requestOptions:]
+ -[PRSPosterUpdateDiscreteStylePayload alpha]
+ -[PRSPosterUpdateDiscreteStylePayload initWithVariation:saturation:luminance:alpha:]
+ -[PRSPosterUpdateSessionInfo assetURLs]
+ -[PRSPosterUpdateSessionInfo context]
+ -[PRSPosterUpdateSessionInfo setAssetURLs:]
+ -[PRSPosterUpdateSessionInfo setContext:]
+ -[PRSRoleActivePosterObserverUpdate initWithRole:activePath:suggestionDescriptors:]
+ -[PRSRoleActivePosterObserverUpdate suggestionDescriptors]
+ -[PRSServer commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:]
+ -[PRSServer fetchExtendedContentCutoutBoundsForOrientation:completion:]
+ -[PRSServer fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:]
+ -[PRSServer refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:]
+ -[PRSService commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:]
+ -[PRSService commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:].cold.1
+ -[PRSService commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:].cold.2
+ -[PRSService deleteDataStoreWithCompletion:].cold.2
+ -[PRSService fetchExtendedContentCutoutBoundsForOrientation:completionHandler:]
+ -[PRSService fetchExtendedContentCutoutBoundsForOrientation:completionHandler:].cold.1
+ -[PRSService fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:]
+ -[PRSService fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:].cold.1
+ -[PRSService fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:].cold.2
+ -[PRSService refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:]
+ -[PRSService refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:].cold.1
+ -[PRSService refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:].cold.2
+ -[PRSWallpaperPublisher _lock_buildActivePosterObserverUpdatesForClient:updatedRoles:clientSpecificSuggestionsToPosterUUID:]
+ -[PRSWallpaperPublisher _lock_issueUpdateForRoles:suggestionsToPosterUUID:]
+ -[PRSWallpaperPublisher _lock_issueUpdateForRoles:suggestionsToPosterUUID:].cold.1
+ -[PRSWallpaperPublisher initializeRoles:suggestions:]
+ -[PRSWallpaperPublisher initializeRoles:suggestions:].cold.1
+ -[PRSWallpaperPublisher initializeRoles:suggestions:].cold.2
+ -[PRSWallpaperPublisher issueUpdateForRoles:suggestions:]
+ -[PRSWallpaperPublisher issueUpdateForSuggestions:]
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table15
+ GCC_except_table18
+ GCC_except_table50
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table7
+ GCC_except_table77
+ GCC_except_table9
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table97
+ _CFArrayGetValueAtIndex
+ _CFRetain
+ _CGImageGetImageSource
+ _CGRectIsEmpty
+ _CGRectIsInfinite
+ _CGRectIsNull
+ _CGRectNull
+ _CPBitmapCreateImagesFromData
+ _OBJC_CLASS_$_CHSControlIdentity
+ _OBJC_CLASS_$_CHSExtensionIdentity
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_PFPosterArchiver
+ _OBJC_CLASS_$_PFPosterCollection
+ _OBJC_CLASS_$_PFPosterCollectionDiff
+ _OBJC_CLASS_$_PFTFuture
+ _OBJC_CLASS_$_PFTPromise
+ _OBJC_CLASS_$_PRSControl
+ _OBJC_CLASS_$_PRSGadget
+ _OBJC_CLASS_$_PRSPosterCollection
+ _OBJC_CLASS_$_PRSPosterConfigurationCollection
+ _OBJC_CLASS_$_PRSPosterDescriptorCollection
+ _OBJC_CLASS_$_PRSPosterDescriptorCollectionDiff
+ _OBJC_CLASS_$_PRSPosterStaticDescriptorCollection
+ _OBJC_CLASS_$_PUIImageOnDiskFormat
+ _OBJC_IVAR_$_PRSCodableImage._bitmapSourceData
+ _OBJC_IVAR_$_PRSControl._controlType
+ _OBJC_IVAR_$_PRSGadget._containerBundleIdentifier
+ _OBJC_IVAR_$_PRSGadget._extensionBundleIdentifier
+ _OBJC_IVAR_$_PRSGadget._intent
+ _OBJC_IVAR_$_PRSGadget._kind
+ _OBJC_IVAR_$_PRSGadget._uniqueIdentifier
+ _OBJC_IVAR_$_PRSMigrationDescriptor._homeScreenIconStyleVariant
+ _OBJC_IVAR_$_PRSMigrationDescriptor._homeScreenIconStyleVariantsForStyles
+ _OBJC_IVAR_$_PRSMigrationDescriptor._homeScreenIconTintSource
+ _OBJC_IVAR_$_PRSPosterArchiver._underlyingArchiver
+ _OBJC_IVAR_$_PRSPosterConfigurationAttributes._descriptorIdentifier
+ _OBJC_IVAR_$_PRSPosterRoleActivePosterObserverState._suggestions
+ _OBJC_IVAR_$_PRSPosterSnapshotCollection._salientContentRectangle
+ _OBJC_IVAR_$_PRSPosterUpdateDiscreteStylePayload._alpha
+ _OBJC_IVAR_$_PRSPosterUpdateSessionInfo._assetSandboxHandles
+ _OBJC_IVAR_$_PRSPosterUpdateSessionInfo._assetSandboxTokens
+ _OBJC_IVAR_$_PRSPosterUpdateSessionInfo._assetURLs
+ _OBJC_IVAR_$_PRSPosterUpdateSessionInfo._context
+ _OBJC_IVAR_$_PRSRoleActivePosterObserverUpdate._suggestionDescriptors
+ _OBJC_IVAR_$_PRSWallpaperObserver._conn_activePosterRoles
+ _OBJC_IVAR_$_PRSWallpaperObserver._conn_posterUUIDToSuggestions
+ _OBJC_IVAR_$_PRSWallpaperPublisher._lock_posterUUIDToSuggestionDescriptorPaths
+ _OBJC_METACLASS_$_PFPosterCollection
+ _OBJC_METACLASS_$_PFPosterCollectionDiff
+ _OBJC_METACLASS_$_PRSControl
+ _OBJC_METACLASS_$_PRSGadget
+ _OBJC_METACLASS_$_PRSPosterCollection
+ _OBJC_METACLASS_$_PRSPosterConfigurationCollection
+ _OBJC_METACLASS_$_PRSPosterDescriptorCollection
+ _OBJC_METACLASS_$_PRSPosterDescriptorCollectionDiff
+ _OBJC_METACLASS_$_PRSPosterStaticDescriptorCollection
+ _PFFunctionNameForAddress
+ _PFGeneralErrorFromObjectWithLocalizedFailureReason
+ _PFPathComponent_RoleIdentifier
+ _PFPosterArchiverFormatForPRSPosterArchiverFormat
+ _PFPosterRolesSupportedForCurrentDeviceClass
+ _PFServerPosterTypeEnumerate
+ _PRSPosterArchiverFormatForPFPosterArchiverFormat
+ _PRSPosterRoleBackdrop
+ _PUIIOSurfaceFromCGImage
+ _PUIImageEncoderErrorDomain
+ _PUIRendererServiceErrorDomain
+ _UIKitLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_PRSControl
+ __OBJC_$_CLASS_METHODS_PRSGadget
+ __OBJC_$_CLASS_METHODS_PRSPosterCollection
+ __OBJC_$_CLASS_METHODS_PRSPosterConfigurationCollection
+ __OBJC_$_CLASS_METHODS_PRSPosterDescriptorCollection
+ __OBJC_$_CLASS_METHODS_PRSPosterStaticDescriptorCollection
+ __OBJC_$_CLASS_PROP_LIST_PRSGadget
+ __OBJC_$_INSTANCE_METHODS_PRSControl
+ __OBJC_$_INSTANCE_METHODS_PRSGadget
+ __OBJC_$_INSTANCE_METHODS_PRSPosterDescriptorCollection
+ __OBJC_$_INSTANCE_METHODS_PRSPosterDescriptorCollectionDiff
+ __OBJC_$_INSTANCE_VARIABLES_PRSControl
+ __OBJC_$_INSTANCE_VARIABLES_PRSGadget
+ __OBJC_$_PROP_LIST_PFPosterContents
+ __OBJC_$_PROP_LIST_PRSControl
+ __OBJC_$_PROP_LIST_PRSGadget
+ __OBJC_$_PROP_LIST_PRSPosterDescriptorCollection
+ __OBJC_$_PROP_LIST_PRSPosterDescriptorCollectionDiff
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PFPosterContents
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFPosterContents
+ __OBJC_$_PROTOCOL_REFS_PFPosterContents
+ __OBJC_CLASS_PROTOCOLS_$_PRSGadget
+ __OBJC_CLASS_RO_$_PRSControl
+ __OBJC_CLASS_RO_$_PRSGadget
+ __OBJC_CLASS_RO_$_PRSPosterCollection
+ __OBJC_CLASS_RO_$_PRSPosterConfigurationCollection
+ __OBJC_CLASS_RO_$_PRSPosterDescriptorCollection
+ __OBJC_CLASS_RO_$_PRSPosterDescriptorCollectionDiff
+ __OBJC_CLASS_RO_$_PRSPosterStaticDescriptorCollection
+ __OBJC_LABEL_PROTOCOL_$_PFPosterContents
+ __OBJC_METACLASS_RO_$_PRSControl
+ __OBJC_METACLASS_RO_$_PRSGadget
+ __OBJC_METACLASS_RO_$_PRSPosterCollection
+ __OBJC_METACLASS_RO_$_PRSPosterConfigurationCollection
+ __OBJC_METACLASS_RO_$_PRSPosterDescriptorCollection
+ __OBJC_METACLASS_RO_$_PRSPosterDescriptorCollectionDiff
+ __OBJC_METACLASS_RO_$_PRSPosterStaticDescriptorCollection
+ __OBJC_PROTOCOL_$_PFPosterContents
+ ___101-[PRSServer commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:]_block_invoke
+ ___102-[PRSService commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:]_block_invoke
+ ___102-[PRSService commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:]_block_invoke.cold.1
+ ___124-[PRSWallpaperPublisher _lock_buildActivePosterObserverUpdatesForClient:updatedRoles:clientSpecificSuggestionsToPosterUUID:]_block_invoke
+ ___18-[PRSService init]_block_invoke.8
+ ___18-[PRSService init]_block_invoke.8.cold.1
+ ___21-[PRSGadget isEqual:]_block_invoke
+ ___21-[PRSGadget isEqual:]_block_invoke_2
+ ___21-[PRSGadget isEqual:]_block_invoke_3
+ ___21-[PRSGadget isEqual:]_block_invoke_4
+ ___21-[PRSGadget isEqual:]_block_invoke_5
+ ___37-[PRSPosterUpdateSessionInfo dealloc]_block_invoke
+ ___42+[PRSPosterCollection postersAtURL:error:]_block_invoke
+ ___43-[PRSPosterUpdateSessionInfo setAssetURLs:]_block_invoke
+ ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.24
+ ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.24.cold.1
+ ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.cold.1
+ ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke.174
+ ___51-[PRSPosterDescriptorCollection mutableDescriptors]_block_invoke
+ ___54-[PRSWallpaperObserver notifyRoleActivePosterUpdates:]_block_invoke
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.138
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.138.cold.1
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.134
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.136
+ ___79-[PRSServer fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:]_block_invoke
+ ___79-[PRSService fetchExtendedContentCutoutBoundsForOrientation:completionHandler:]_block_invoke
+ ___79-[PRSService fetchExtendedContentCutoutBoundsForOrientation:completionHandler:]_block_invoke.cold.1
+ ___80-[PRSService fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:]_block_invoke
+ ___80-[PRSService fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:]_block_invoke.cold.1
+ ___93-[PRSServer refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke
+ ___94-[PRSService refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke
+ ___94-[PRSService refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.cold.1
+ ___96-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:]_block_invoke
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_2
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_3
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_4
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_5
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_6
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_7
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_8
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___PFServerPosterPathFromPFPosterContents
+ ___UIKitLibraryCore_block_invoke
+ ____consumeSandboxExtensions_block_invoke
+ ____decodeSandboxToken_block_invoke
+ ____encodeSandboxTokens_block_invoke
+ ___block_descriptor_32_e29_B16?0"PRSPosterDescriptor"8l
+ ___block_descriptor_32_e49_"PRSPosterDescriptor"16?0"PFServerPosterPath"8l
+ ___block_descriptor_40_e8_32bs_e32_v16?0"PRSPosterConfiguration"8ls32l8
+ ___block_descriptor_40_e8_32r_e35_v32?0"NSString"8"NSString"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSString"8"NSURL"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e44_v24?0"PRSPosterConfiguration"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e45_"<PFTFuture>"16?0"PRSPosterConfiguration"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e43_"PFTFuture"16?0"PRSPosterConfiguration"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e70_v32?0"PRSPosterConfiguration"8"PRSPosterUpdateResult"16"NSError"24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e47_v24?0"PRSPosterSnapshotResponse"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e56_v24?0"NSArray<__PRSPosterUpdateResult__>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e32_v32?0"NSString"8"NSURL"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e28_16?0"PFServerPosterPath"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56r_e12_v24?0q8^B16ls32l8s40l8r56l8s48l8
+ ___block_literal_global.3
+ ___block_literal_global.348
+ ___getCGRectFromStringSymbolLoc_block_invoke
+ ___getCGRectFromStringSymbolLoc_block_invoke.cold.1
+ ___getPUIWritePNGFromCGImageRefSymbolLoc_block_invoke
+ ___getPUIWritePNGFromCGImageRefSymbolLoc_block_invoke.cold.1
+ ___getkPaperboardIOSurfaceSalientContentRectPropertiesKeySymbolLoc_block_invoke
+ __consumeSandboxExtensions
+ __decodeContextDictionary
+ __encodeContextDictionary
+ _audit_stringUIKit
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _getCGRectFromStringSymbolLoc.ptr
+ _getPUIWritePNGFromCGImageRefSymbolLoc.ptr
+ _getkPaperboardIOSurfaceSalientContentRectPropertiesKey
+ _getkPaperboardIOSurfaceSalientContentRectPropertiesKey.cold.1
+ _getkPaperboardIOSurfaceSalientContentRectPropertiesKeySymbolLoc.ptr
+ _objc_msgSend$_initWithProvider:type:role:posterUUID:version:supplement:descriptorIdentifier:
+ _objc_msgSend$_lock_buildActivePosterObserverUpdatesForClient:updatedRoles:clientSpecificSuggestionsToPosterUUID:
+ _objc_msgSend$_lock_issueUpdateForRoles:suggestionsToPosterUUID:
+ _objc_msgSend$_populateSalientContentRectFromSurfacesIfPossible
+ _objc_msgSend$activePoster
+ _objc_msgSend$addIndex:
+ _objc_msgSend$addSuccessBlock:andFailureBlock:
+ _objc_msgSend$archivePath:format:error:
+ _objc_msgSend$bs_filter:
+ _objc_msgSend$commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$controlType
+ _objc_msgSend$createCGImageFromCPBitmapData:error:
+ _objc_msgSend$createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:
+ _objc_msgSend$createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:
+ _objc_msgSend$decodeCGRectForKey:
+ _objc_msgSend$decodeDictionaryOfClass:forKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$encodeCGRect:forKey:
+ _objc_msgSend$encodeDictionary:forKey:
+ _objc_msgSend$fetchExtendedContentCutoutBoundsForOrientation:completion:
+ _objc_msgSend$fetchHomeScreenWallpaperForOrientation:completion:
+ _objc_msgSend$fetchLockScreenWallpaperForOrientation:completion:
+ _objc_msgSend$fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:
+ _objc_msgSend$fetchLockScreenWallpaperForType:variant:options:orientation:completion:
+ _objc_msgSend$fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:
+ _objc_msgSend$finishWithResult:
+ _objc_msgSend$finishWithResult:error:
+ _objc_msgSend$flatMap:
+ _objc_msgSend$future
+ _objc_msgSend$futureWithResult:
+ _objc_msgSend$homeScreenConfigurationPath
+ _objc_msgSend$homeScreenIconStyleVariant
+ _objc_msgSend$homeScreenIconStyleVariantsForStyles
+ _objc_msgSend$homeScreenIconTintSource
+ _objc_msgSend$image
+ _objc_msgSend$initWithConfigurationType:variantType:options:orientation:requestOptions:
+ _objc_msgSend$initWithContentsOfURL:options:error:
+ _objc_msgSend$initWithExtensionBundleIdentifier:containerBundleIdentifier:deviceIdentifier:
+ _objc_msgSend$initWithExtensionIdentity:kind:intent:
+ _objc_msgSend$initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayIdentity:salientContentRectangle:
+ _objc_msgSend$initWithRole:activePath:suggestionDescriptors:
+ _objc_msgSend$initWithRole:activePoster:suggestions:
+ _objc_msgSend$initWithSet:
+ _objc_msgSend$initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:intent:
+ _objc_msgSend$initWithVariation:saturation:luminance:alpha:
+ _objc_msgSend$lastIndex
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$mutableConfigurationWithProvider:descriptorIdentifier:role:
+ _objc_msgSend$mutableDescriptors
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$pf_descriptorIdentifierURLForType:identifierURL:
+ _objc_msgSend$pf_posterPathInstanceURLForVersionsURL:version:
+ _objc_msgSend$pf_posterPathSupplementContainerURLForInstanceURL:
+ _objc_msgSend$pf_posterPathTypeURLForProviderURL:type:
+ _objc_msgSend$pf_posterPathVersionsURLForIdentifierURL:
+ _objc_msgSend$pf_roleIdentifierURLForType:identifierURL:
+ _objc_msgSend$pf_sanitizeWithAllowedKeyClasses:allowedValueClasses:
+ _objc_msgSend$pf_temporaryDirectoryURLWithBasenamePrefix:
+ _objc_msgSend$posterUpdateHomeScreenTintWithVariation:saturation:luminance:alpha:
+ _objc_msgSend$posters
+ _objc_msgSend$postersAtProviderURL:type:fileManager:error:
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:
+ _objc_msgSend$removeAllIndexes
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:
+ _objc_msgSend$server:commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:
+ _objc_msgSend$server:fetchExtendedContentCutoutBoundsForOrientation:completion:
+ _objc_msgSend$server:fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:
+ _objc_msgSend$server:refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:
+ _objc_msgSend$setControlType:
+ _objc_msgSend$setFamily:
+ _objc_msgSend$setHomeScreenIconStyleVariant:
+ _objc_msgSend$setHomeScreenIconStyleVariantsForStyles:
+ _objc_msgSend$setHomeScreenIconTintSource:
+ _objc_msgSend$snapshots
+ _objc_msgSend$specificType
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$suggestionDescriptors
+ _objc_msgSend$suggestions
+ _objc_msgSend$switcherConfigurationPath
+ _objc_msgSend$temporaryServerPathForProvider:descriptorIdentifier:role:
+ _objc_msgSend$unarchivePathAtURL:format:error:
+ _objc_msgSend$unarchivePathFromData:format:error:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$writePNGToURL:error:
+ _objc_retain_x6
+ _soft_CGRectFromString
+ _soft_CGRectFromString.cold.1
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_value
- +[PRSMutablePosterConfiguration mutableConfigurationWithRole:].cold.1
- +[PRSPosterArchiveManifest isManifestDictionaryValid:]
- +[PRSPosterArchiveManifest manifestVersion]
- +[PRSPosterArchiveManifest unsupportedVersions]
- +[PRSPosterArchiver archiveExtensionForFormat:]
- +[PRSPosterArchiver formatForData:]
- +[PRSPosterArchiver formatForDataAtURL:].cold.1
- +[PRSPosterArchiver formatForDataAtURL:].cold.2
- +[PRSPosterArchiver markURLPurgableAfterOneHour:error:]
- +[PRSPosterArchiver markURLPurgableAfterOneHour:error:].cold.1
- +[PRSPosterArchiver minSupportedArchiveVersion]
- -[NSURL(PRSAdditions) prs_URLExists:]
- -[NSURL(PRSAdditions) prs_URLExists:].cold.1
- -[NSURL(PRSAdditions) prs_isDirectory]
- -[NSURL(PRSAdditions) prs_isPurgable]
- -[NSURL(PRSAdditions) prs_setPurgable:afterDate:error:]
- -[NSURL(PRSAdditions) prs_unmarkAsPurgable]
- -[NSURL(PRSAdditions) prs_unmarkAsPurgable].cold.1
- -[PRSPosterArchiveManifest .cxx_destruct]
- -[PRSPosterArchiveManifest archiveVersion]
- -[PRSPosterArchiveManifest configurationUUID]
- -[PRSPosterArchiveManifest dataRepresentationWithError:]
- -[PRSPosterArchiveManifest dataStoreVersion]
- -[PRSPosterArchiveManifest dictionaryRepresentation]
- -[PRSPosterArchiveManifest extensionIdentifier]
- -[PRSPosterArchiveManifest initWithConfigurationAttributes:]
- -[PRSPosterArchiveManifest initWithDataRepresentation:]
- -[PRSPosterArchiveManifest initWithDictionaryRepresentation:]
- -[PRSPosterArchiveManifest latestConfigurationSupplement]
- -[PRSPosterArchiveManifest latestConfigurationVersion]
- -[PRSPosterArchiveManifest role]
- -[PRSPosterArchiveManifest setDictionaryRepresentation:]
- -[PRSPosterArchiveManifest(Deprecated) buildVersion]
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:]
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.1
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.2
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.3
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.4
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.5
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.6
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.7
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.8
- -[PRSPosterArchiver _unarchiveWithHandler:manifest:error:].cold.9
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.1
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.2
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.3
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.4
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.5
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.6
- -[PRSPosterArchiver archiveConfiguration:format:error:].cold.7
- -[PRSPosterArchiver fileManager]
- -[PRSPosterArchiver processHandle]
- -[PRSPosterArchiver setFileManager:]
- -[PRSPosterArchiver setProcessHandle:]
- -[PRSPosterArchiver setUnarchivingContainerURL:]
- -[PRSPosterArchiver unarchiveConfigurationAppleArchiveAtURL:manifest:error:]
- -[PRSPosterArchiver unarchiveConfigurationAppleArchiveData:manifest:error:]
- -[PRSPosterArchiver unarchiveConfigurationAtURL:format:error:].cold.2
- -[PRSPosterArchiver unarchiveConfigurationFromData:format:error:].cold.2
- -[PRSPosterArchiver unarchiveConfigurationZipArchiveAtURL:manifest:error:]
- -[PRSPosterArchiver unarchiveConfigurationZipArchiveData:manifest:error:]
- -[PRSPosterArchiver unarchivingContainerURL]
- -[PRSPosterRoleActivePosterObserverState initWithRole:activePoster:]
- -[PRSPosterUpdateDiscreteStylePayload initWithVariation:saturation:luminance:]
- -[PRSRoleActivePosterObserverUpdate initWithRole:activePath:]
- -[PRSService refreshSnapshotForPosterConfiguration:completion:].cold.1
- -[PRSService serviceNotificationCenterWithError:]
- -[PRSService serviceNotificationCenterWithError:].cold.1
- -[PRSWallpaperPublisher _lock_buildActivePosterObserverUpdatesForClient:updatedRoles:]
- -[PRSWallpaperPublisher _lock_issueUpdateForRoles:]
- -[PRSWallpaperPublisher _lock_issueUpdateForRoles:].cold.1
- -[PRSWallpaperPublisher initializeRoles:]
- -[PRSWallpaperPublisher initializeRoles:].cold.1
- -[PRSWallpaperPublisher issueUpdateForRoles:]
- -[PRSWidget .cxx_destruct]
- -[PRSWidget containerBundleIdentifier]
- -[PRSWidget descriptionWithMultilinePrefix:]
- -[PRSWidget description]
- -[PRSWidget extensionBundleIdentifier]
- -[PRSWidget intent]
- -[PRSWidget kind]
- -[PRSWidget setContainerBundleIdentifier:]
- -[PRSWidget setExtensionBundleIdentifier:]
- -[PRSWidget setIntent:]
- -[PRSWidget setKind:]
- -[PRSWidget setUniqueIdentifier:]
- -[PRSWidget succinctDescriptionBuilder]
- -[PRSWidget succinctDescription]
- -[PRSWidget uniqueIdentifier]
- GCC_except_table11
- GCC_except_table12
- GCC_except_table14
- GCC_except_table25
- GCC_except_table26
- GCC_except_table51
- GCC_except_table65
- GCC_except_table66
- GCC_except_table74
- GCC_except_table85
- GCC_except_table86
- GCC_except_table87
- _AAArchiveStreamClose
- _AAArchiveStreamProcess
- _AAArchiveStreamWritePathList
- _AAByteStreamClose
- _AADecodeArchiveInputStreamOpen
- _AADecompressionInputStreamOpen
- _AAEncodeArchiveOutputStreamOpen
- _AAExtractArchiveOutputStreamOpen
- _AAFieldKeySetCreateWithString
- _AAFieldKeySetDestroy
- _AAFileStreamOpenWithFD
- _AAFileStreamOpenWithPath
- _AAPathListCreateWithDirectoryContents
- _AAPathListDestroy
- _BSDispatchQueueCreateSerial
- _NSFilePosixPermissions
- _NSPageSize
- _NSURLFileResourceTypeDirectory
- _OBJC_CLASS_$_NSCalendar
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSDateComponents
- _OBJC_CLASS_$_NSFileHandle
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_NSPipe
- _OBJC_CLASS_$_PRSPosterArchiveManifest
- _OBJC_IVAR_$_PRSPosterArchiveManifest._dictionaryRepresentation
- _OBJC_IVAR_$_PRSPosterArchiver._fileManager
- _OBJC_IVAR_$_PRSPosterArchiver._processHandle
- _OBJC_IVAR_$_PRSPosterArchiver._unarchivingContainerURL
- _OBJC_IVAR_$_PRSWidget._containerBundleIdentifier
- _OBJC_IVAR_$_PRSWidget._extensionBundleIdentifier
- _OBJC_IVAR_$_PRSWidget._intent
- _OBJC_IVAR_$_PRSWidget._kind
- _OBJC_IVAR_$_PRSWidget._uniqueIdentifier
- _OBJC_METACLASS_$_PRSPosterArchiveManifest
- _PBUIRendererServiceErrorDomain
- _PFFileProtectionNoneAttributes
- _PFPosterPathFileAttributes
- _PRSAppleArchiveCompressDirectory
- _PRSAppleArchiveDecompressStream
- _PRSPosterArchiverErrorDomain
- _PRSServiceDidUpdateActivePosterConfigurationNotification
- _PRSServiceDidUpdateAssociatedHomeScreenPosterConfigurationNotification
- _PRSServiceDidUpdatePosterConfigurationNotification
- _PRSServiceDidUpdateSelectedPosterConfigurationNotification
- _PRSServiceFromActivePosterConfigurationUserInfoKey
- _PRSServiceFromSelectedPosterConfigurationUserInfoKey
- _PRSServiceHomeScreenAssociatedPosterConfigurationUserInfoKey
- _PRSServiceToActivePosterConfigurationUserInfoKey
- _PRSServiceToSelectedPosterConfigurationUserInfoKey
- _PRSServiceUpdatedPosterConfigurationUserInfoKey
- _PRSServiceWillUpdateActivePosterConfigurationNotification
- _PRSServiceWillUpdateSelectedPosterConfigurationNotification
- _PRSZipArchiverCompressDirectory
- _PRSZipArchiverCompressDirectory.cold.1
- _PRSZipArchiverCompressDirectory.cold.2
- _PRSZipArchiverCompressDirectory.cold.3
- _PRSZipCreateReadArchive
- _PRSZipCreateReadArchive.cold.1
- _PRSZipCreateReadArchive.cold.2
- _PRSZipCreateReadArchive.cold.3
- _PRSZipUnarchive
- _PRSZipUnarchive.cold.1
- _PRSZipUnarchive.cold.10
- _PRSZipUnarchive.cold.11
- _PRSZipUnarchive.cold.12
- _PRSZipUnarchive.cold.13
- _PRSZipUnarchive.cold.14
- _PRSZipUnarchive.cold.15
- _PRSZipUnarchive.cold.16
- _PRSZipUnarchive.cold.2
- _PRSZipUnarchive.cold.3
- _PRSZipUnarchive.cold.4
- _PRSZipUnarchive.cold.5
- _PRSZipUnarchive.cold.6
- _PRSZipUnarchive.cold.7
- _PRSZipUnarchive.cold.8
- _PRSZipUnarchive.cold.9
- __OBJC_$_CLASS_METHODS_PRSPosterArchiveManifest
- __OBJC_$_CLASS_PROP_LIST_PRSWidget
- __OBJC_$_INSTANCE_METHODS_PRSPosterArchiveManifest(Deprecated)
- __OBJC_$_INSTANCE_VARIABLES_PRSPosterArchiveManifest
- __OBJC_$_PROP_LIST_PRSPosterArchiver
- __OBJC_CLASS_PROTOCOLS_$_PRSWidget
- __OBJC_CLASS_RO_$_PRSPosterArchiveManifest
- __OBJC_METACLASS_RO_$_PRSPosterArchiveManifest
- __Z16PRSUnarchiverZipP5NSURLS0_
- __Z16PRSUnarchiverZipP5NSURLS0_.cold.1
- __Z16PRSUnarchiverZipP5NSURLS0_.cold.2
- __Z16PRSUnarchiverZipP5NSURLS0_.cold.3
- __Z16PRSUnarchiverZipP6NSDataP5NSURL
- __Z16PRSUnarchiverZipPKvmP5NSURL
- __Z16PRSUnarchiverZipPKvmP5NSURLm
- __Z16PRSUnarchiverZipPKvmP5NSURLm.cold.1
- __Z16PRSUnarchiverZipPKvmP5NSURLm.cold.2
- __Z16PRSUnarchiverZipPKvmP5NSURLm.cold.3
- __Z16PRSUnarchiverZipiP5NSURL
- __Z16PRSUnarchiverZipiP5NSURLm
- __Z16PRSUnarchiverZipiP5NSURLm.cold.1
- __Z16PRSUnarchiverZipiP5NSURLm.cold.2
- __Z16PRSUnarchiverZipiP5NSURLm.cold.3
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.1
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.10
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.11
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.12
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.13
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.14
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.15
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.16
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.17
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.18
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.19
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.2
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.20
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.21
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.22
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.23
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.24
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.25
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.3
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.4
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.5
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.6
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.7
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.8
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.9
- ___18-[PRSService init]_block_invoke.38
- ___18-[PRSService init]_block_invoke.38.cold.1
- ___21-[PRSWidget isEqual:]_block_invoke
- ___21-[PRSWidget isEqual:]_block_invoke_2
- ___21-[PRSWidget isEqual:]_block_invoke_3
- ___21-[PRSWidget isEqual:]_block_invoke_4
- ___21-[PRSWidget isEqual:]_block_invoke_5
- ___21-[PRSWidget isEqual:]_block_invoke_6
- ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke_2
- ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke_2.cold.1
- ___49-[PRSService serviceNotificationCenterWithError:]_block_invoke
- ___49-[PRSService serviceNotificationCenterWithError:]_block_invoke_2
- ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke.176
- ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke_4
- ___58-[PRSPosterArchiver _unarchiveWithHandler:manifest:error:]_block_invoke
- ___58-[PRSPosterArchiver _unarchiveWithHandler:manifest:error:]_block_invoke_2
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.175
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.175.cold.1
- ___73-[PRSPosterArchiver unarchiveConfigurationZipArchiveData:manifest:error:]_block_invoke
- ___74-[PRSPosterArchiver unarchiveConfigurationZipArchiveAtURL:manifest:error:]_block_invoke
- ___75-[PRSPosterArchiver unarchiveConfigurationAppleArchiveData:manifest:error:]_block_invoke
- ___75-[PRSPosterArchiver unarchiveConfigurationAppleArchiveData:manifest:error:]_block_invoke_2
- ___76-[PRSPosterArchiver unarchiveConfigurationAppleArchiveAtURL:manifest:error:]_block_invoke
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.170
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.172
- ____Z18PRSArchiverZipDataP5NSURLP13NSFileManager_block_invoke
- ____Z18PRSArchiverZipDataP5NSURLP13NSFileManager_block_invoke.cold.1
- ___assert_rtn
- ___block_descriptor_32_e70_v24?0"PRSWallpaperObserverState"8"PRSWallpaperObserverTransition"16l
- ___block_descriptor_40_e8_32s_e15_B16?0"NSURL"8ls32l8
- ___block_descriptor_40_e8_32s_e22_v32?0"NSURL"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e49_v32?0"NSString"8"PRSPosterConfiguration"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e5_Q8?0ls32l8
- ___block_descriptor_48_e12_v24?0^v8Q16l
- ___block_literal_global.33
- ___block_literal_global.45
- ___getPUIIOSurfaceFromCGImageSymbolLoc_block_invoke
- ___getPUIImageEncoderErrorDomainSymbolLoc_block_invoke
- ___getPUIImageOnDiskFormatClass_block_invoke
- ___getPUIImageOnDiskFormatClass_block_invoke.cold.1
- ___getkPaperboardIOSurfaceDeviceOrientationPropertiesKeySymbolLoc_block_invoke.cold.1
- _archive_entry_filetype
- _archive_entry_pathname_utf8
- _archive_entry_perm
- _archive_entry_set_perm
- _archive_entry_size
- _archive_entry_size_is_set
- _archive_entry_sourcepath
- _archive_entry_update_pathname_utf8
- _archive_error_string
- _archive_read_close
- _archive_read_data_block
- _archive_read_disk_descend
- _archive_read_disk_new
- _archive_read_disk_open
- _archive_read_disk_set_standard_lookup
- _archive_read_disk_set_symlink_physical
- _archive_read_free
- _archive_read_new
- _archive_read_next_header
- _archive_read_open_fd
- _archive_read_open_memory
- _archive_read_support_filter_all
- _archive_read_support_format_zip
- _archive_write_close
- _archive_write_data
- _archive_write_data_block
- _archive_write_disk_new
- _archive_write_disk_set_options
- _archive_write_disk_set_standard_lookup
- _archive_write_finish_entry
- _archive_write_free
- _archive_write_header
- _archive_write_new
- _archive_write_open_fd
- _archive_write_set_format_option
- _archive_write_set_format_zip
- _close
- _fsctl
- _fstat
- _getPUIIOSurfaceFromCGImageSymbolLoc.ptr
- _getPUIImageEncoderErrorDomain
- _getPUIImageEncoderErrorDomain.cold.1
- _getPUIImageEncoderErrorDomainSymbolLoc.ptr
- _getPUIImageOnDiskFormatClass.softClass
- _malloc_type_malloc
- _mmap
- _munmap
- _objc_msgSend$URLByAppendingPathExtension:
- _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
- _objc_msgSend$_lock_buildActivePosterObserverUpdatesForClient:updatedRoles:
- _objc_msgSend$_lock_issueUpdateForRoles:
- _objc_msgSend$_unarchiveWithHandler:manifest:error:
- _objc_msgSend$activateWithConfiguration:
- _objc_msgSend$activeHome
- _objc_msgSend$activeLock
- _objc_msgSend$appendUnsignedInteger:
- _objc_msgSend$appendUnsignedInteger:counterpart:
- _objc_msgSend$archiveExtensionForFormat:
- _objc_msgSend$archiveVersion
- _objc_msgSend$bytes
- _objc_msgSend$closeFile
- _objc_msgSend$configurationUUID
- _objc_msgSend$copyItemAtURL:toURL:error:
- _objc_msgSend$createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:completion:
- _objc_msgSend$currentCalendar
- _objc_msgSend$dataRepresentationWithError:
- _objc_msgSend$date
- _objc_msgSend$dateByAddingComponents:toDate:options:
- _objc_msgSend$domain
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$fetchPosterConfigurations:
- _objc_msgSend$fileDescriptor
- _objc_msgSend$fileExistsAtPath:isDirectory:
- _objc_msgSend$fileHandleForReading
- _objc_msgSend$fileHandleForReadingFromURL:error:
- _objc_msgSend$fileHandleForWriting
- _objc_msgSend$fileManager
- _objc_msgSend$formatForData:
- _objc_msgSend$initWithBytesNoCopy:length:deallocator:
- _objc_msgSend$initWithConfiguration:
- _objc_msgSend$initWithConfigurationAttributes:
- _objc_msgSend$initWithDataRepresentation:
- _objc_msgSend$initWithDictionaryRepresentation:
- _objc_msgSend$initWithExplanation:
- _objc_msgSend$initWithRole:activePath:
- _objc_msgSend$initWithRole:activePoster:
- _objc_msgSend$initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:family:intent:
- _objc_msgSend$initWithVariation:saturation:luminance:
- _objc_msgSend$isFileURL
- _objc_msgSend$isManifestDictionaryValid:
- _objc_msgSend$latestConfigurationSupplement
- _objc_msgSend$latestConfigurationVersion
- _objc_msgSend$manifestVersion
- _objc_msgSend$markURLPurgableAfterOneHour:error:
- _objc_msgSend$minSupportedArchiveVersion
- _objc_msgSend$moveItemAtURL:toURL:error:
- _objc_msgSend$pathComponents
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$pipe
- _objc_msgSend$postNotificationName:object:userInfo:
- _objc_msgSend$prs_isDirectory
- _objc_msgSend$prs_setPurgable:afterDate:error:
- _objc_msgSend$prs_unmarkAsPurgable
- _objc_msgSend$readDataUpToLength:error:
- _objc_msgSend$refreshSnapshotForPosterConfigurationMatchingUUID:completion:
- _objc_msgSend$setHour:
- _objc_msgSend$setQueue:
- _objc_msgSend$subarrayWithRange:
- _objc_msgSend$temporaryDirectory
- _objc_msgSend$timeIntervalSince1970
- _objc_msgSend$unarchiveConfigurationAppleArchiveAtURL:manifest:error:
- _objc_msgSend$unarchiveConfigurationAppleArchiveData:manifest:error:
- _objc_msgSend$unarchiveConfigurationZipArchiveAtURL:manifest:error:
- _objc_msgSend$unarchiveConfigurationZipArchiveData:manifest:error:
- _objc_msgSend$unarchivingContainerURL
- _objc_msgSend$unsignedLongLongValue
- _objc_msgSend$unsupportedVersions
- _objc_msgSend$updateToSelectedConfiguration:completion:
- _objc_msgSend$writeData:error:
- _objc_msgSend$writeToURL:atomically:
- _open
- _read
- _realpath$DARWIN_EXTSN
- _serviceNotificationCenterWithError:.__notificationCenter
- _serviceNotificationCenterWithError:.__observer
- _serviceNotificationCenterWithError:.onceToken
- _soft_PUIIOSurfaceFromCGImage
- _soft_PUIIOSurfaceFromCGImage.cold.1
- _strerror
- _strlen
- _unlink
CStrings:
+ "(Unknown Location)"
+ "<%@(%p): %lu sections, %lu items, locale=%@, source=%@>"
+ "<%{public}@:%p> failed to prepare suggestion descriptor sandbox extension for update of %{public}@ for client %{public}@ due to bad auditToken %{public}@"
+ "<%{public}@:%p> failed to prepare suggestion descriptor sandbox extension for update of %{public}@/%{public}@ for client %{public}@ due to bad auditToken %{public}@"
+ "@\"<PFTFuture>\"16@?0@\"PRSPosterConfiguration\"8"
+ "@\"PFPosterArchiver\""
+ "@\"PFPosterPath\"16@0:8"
+ "@\"PFTFuture\"16@?0@\"PRSPosterConfiguration\"8"
+ "@\"PRSPosterDescriptor\"16@?0@\"PFServerPosterPath\"8"
+ "@104@0:8@16@24d32q40q48q56@64{CGRect={CGPoint=dd}{CGSize=dd}}72"
+ "@48@0:8@16q24@32o^@40"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8q16q24Q32q40@48"
+ "B16@?0@\"PRSPosterDescriptor\"8"
+ "BOOL soft_PUIWritePNGFromCGImageRef(CGImageRef, NSURL *__strong, NSError *__autoreleasing *)"
+ "CGRect soft_CGRectFromString(NSString *__strong)"
+ "CGRectFromString"
+ "CPBitmap file contained no images."
+ "DF"
+ "Data store invalidation failed with error: %{public}@"
+ "Data store is being deleted by process %@"
+ "Deprecated."
+ "ExternalSystemServiceFetchLockScreen"
+ "Failed unarchive PFPosterPath from URL: %@"
+ "Failed unarchive PFPosterPath from archiveData: %@"
+ "NSString *getkPaperboardIOSurfaceSalientContentRectPropertiesKey(void)"
+ "OSMigration"
+ "PFPosterContents"
+ "PRPosterRoleBackdrop"
+ "PRSControl"
+ "PRSControl.m"
+ "PRSGadget"
+ "PRSPosterCollection"
+ "PRSPosterConfigurationCollection"
+ "PRSPosterDescriptorCollection"
+ "PRSPosterDescriptorCollectionDiff"
+ "PRSPosterStaticDescriptorCollection"
+ "PRSPosterUpdateTypeHomeScreenIconSize"
+ "PRSPosterUpdateTypeHomeScreenIconTintSource"
+ "PRSPosterUpdateTypeHomeScreenIconUserInterfaceStyle"
+ "PRSPosterUpdateTypeHomeScreenIconUserInterfaceStyleVariant"
+ "PRSPosterUpdateTypeHomeScreenUserSelectedVariantsForIconUserInterfaceStyle"
+ "PUICodableImage BSXPCDecoding failed: %@"
+ "PUICodableImage.m"
+ "PUIWritePNGFromCGImageRef"
+ "Proactive"
+ "Provider is not PhotosPosterProvider; will not return data"
+ "Somehow a PUICodableImage was made that had no actual source or image."
+ "T@\"NSArray\",R,C,N,V_suggestionDescriptors"
+ "T@\"NSArray\",R,N,V_suggestions"
+ "T@\"NSDictionary\",&,N,V_assetURLs"
+ "T@\"NSDictionary\",&,N,V_context"
+ "T@\"NSDictionary\",C,D,N"
+ "T@\"NSDictionary\",C,N,V_homeScreenIconStyleVariantsForStyles"
+ "T@\"NSNumber\",R,N,V_alpha"
+ "T@\"NSString\",C,N,V_homeScreenIconStyleVariant"
+ "T@\"NSString\",C,N,V_homeScreenIconTintSource"
+ "T@\"NSString\",R,N,V_descriptorIdentifier"
+ "T@\"PFPosterPath\",R,N"
+ "T@\"PRSPosterDescriptorCollection\",R,D,N"
+ "TQ,N,V_controlType"
+ "The bitmap file was valid, it just had no images."
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_salientContentRectangle"
+ "Unable to create incoming poster configuration from URL: %@"
+ "Unable to create incoming poster configuration from archiveData: %@"
+ "Unknown"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">24"
+ "Vv40@0:8@\"NSUUID\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">32"
+ "[Possibly Expected Error] CPBitmap read failed will fallback to ImageIO. The source data is unlikely a cpbitmap so you can normally ignore this: %@"
+ "[Possibly Expected Error] CPBitmap read failed. The source data is unlikely a cpbitmap so you can normally ignore this: %@"
+ "[asset] failed to consume sandboxToken %@ from bsxpc with errno=%i (%{public}s) : <PRSPosterUpdateSessionInfo assetURLs=%{public}@>"
+ "_alpha"
+ "_assetSandboxHandles"
+ "_assetSandboxTokens"
+ "_assetURLs"
+ "_bitmapSourceData"
+ "_conn_activePosterRoles"
+ "_conn_posterUUIDToSuggestions"
+ "_context"
+ "_controlType"
+ "_homeScreenIconStyleVariant"
+ "_homeScreenIconStyleVariantsForStyles"
+ "_homeScreenIconTintSource"
+ "_initWithProvider:type:role:posterUUID:version:supplement:descriptorIdentifier:"
+ "_lock_buildActivePosterObserverUpdatesForClient:updatedRoles:clientSpecificSuggestionsToPosterUUID:"
+ "_lock_issueUpdateForRoles:suggestionsToPosterUUID:"
+ "_lock_posterUUIDToSuggestionDescriptorPaths"
+ "_populateSalientContentRectFromSurfacesIfPossible"
+ "_salientContentRectangle"
+ "_suggestionDescriptors"
+ "_suggestions"
+ "_underlyingArchiver"
+ "addIndex:"
+ "addSuccessBlock:andFailureBlock:"
+ "alpha"
+ "archivePath:format:error:"
+ "assetURLs"
+ "asts"
+ "asus"
+ "bs_filter:"
+ "com.apple.PosterUIFoundation.RendererService"
+ "commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:"
+ "containsValueForKey:"
+ "context"
+ "controlIdentity"
+ "controlType"
+ "createCGImageFromCPBitmapData:error:"
+ "createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:"
+ "ctx"
+ "decodeCGRectForKey:"
+ "decodeDictionaryOfClass:forKey:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "encodeCGRect:forKey:"
+ "encodeDictionary:forKey:"
+ "fetchExtendedContentCutoutBoundsForOrientation:completion:"
+ "fetchExtendedContentCutoutBoundsForOrientation:completionHandler:"
+ "fetchHomeScreenWallpaperForOrientation:completion:"
+ "fetchHomeScreenWallpaperWithCompletion:"
+ "fetchLockScreenWallpaperForOrientation:completion:"
+ "fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:"
+ "fetchLockScreenWallpaperForType:variant:options:orientation:completion:"
+ "fetchLockScreenWallpaperWithCompletion:"
+ "fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:"
+ "fetchedWallpaper.png"
+ "finishWithResult:"
+ "finishWithResult:error:"
+ "flatMap:"
+ "future"
+ "futureWithResult:"
+ "homeScreenIconStyleVariant"
+ "homeScreenIconStyleVariantsForStyles"
+ "homeScreenIconTintSource"
+ "homeScreenWallpaperURL is not reachable"
+ "initWithCollection:otherCollection:"
+ "initWithConfigurationType:variantType:options:orientation:requestOptions:"
+ "initWithContentsOfURL:options:error:"
+ "initWithExtensionBundleIdentifier:containerBundleIdentifier:deviceIdentifier:"
+ "initWithExtensionIdentity:kind:intent:"
+ "initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayIdentity:salientContentRectangle:"
+ "initWithRole:activePath:suggestionDescriptors:"
+ "initWithRole:activePoster:suggestions:"
+ "initWithSet:"
+ "initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:controlType:intent:"
+ "initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:intent:"
+ "initWithVariation:saturation:luminance:alpha:"
+ "initializeRoles:suggestions:"
+ "invalid role: %@, supported roles for device class: %@"
+ "issueUpdateForRoles:suggestions:"
+ "issueUpdateForSuggestions:"
+ "kPaperboardIOSurfaceSalientContentRectPropertiesKey"
+ "lastIndex"
+ "lhsCollection"
+ "localeIdentifier"
+ "lockScreenImageURL is not reachable"
+ "mutableConfigurationWithProvider:descriptorIdentifier:role:"
+ "mutableDescriptors"
+ "objectEnumerator"
+ "pf_descriptorIdentifierURLForType:identifierURL:"
+ "pf_posterPathInstanceURLForVersionsURL:version:"
+ "pf_posterPathSupplementContainerURLForInstanceURL:"
+ "pf_posterPathTypeURLForProviderURL:type:"
+ "pf_posterPathVersionsURLForIdentifierURL:"
+ "pf_roleIdentifierURLForType:identifierURL:"
+ "pf_sanitizeWithAllowedKeyClasses:allowedValueClasses:"
+ "pf_temporaryDirectoryURLWithBasenamePrefix:"
+ "posterUpdateHomeScreenIconTintSource:"
+ "posterUpdateHomeScreenIconUserInterfaceStyleVariant:"
+ "posterUpdateHomeScreenTintWithVariation:saturation:luminance:alpha:"
+ "posterUpdateUserSelectedHomeScreenIconStyleVariantsForTypes:"
+ "posters"
+ "postersAtProviderURL:type:fileManager:error:"
+ "postersAtURL:error:"
+ "processInfo"
+ "processName"
+ "refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:"
+ "removeAllIndexes"
+ "removeObjectForKey:"
+ "resetLockScreenWallpapersToImageAtURL:completion:"
+ "resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:"
+ "rhsCollection"
+ "salientContentRectangle"
+ "sd"
+ "server:commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:"
+ "server:fetchExtendedContentCutoutBoundsForOrientation:completion:"
+ "server:fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:"
+ "server:refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:"
+ "setAssetURLs:"
+ "setContext:"
+ "setControlType:"
+ "setHomeScreenIconStyleVariant:"
+ "setHomeScreenIconStyleVariantsForStyles:"
+ "setHomeScreenIconTintSource:"
+ "softlink:r:path:/System/Library/Frameworks/UIKit.framework/UIKit"
+ "specificType"
+ "stringWithContentsOfURL:encoding:error:"
+ "suggestionDescriptors"
+ "suggestions"
+ "suggestionsToPosterUUID"
+ "temporaryServerPathForProvider:descriptorIdentifier:role:"
+ "unarchivePathAtURL:format:error:"
+ "unarchivePathFromData:format:error:"
+ "unionSet:"
+ "v16@?0@\"PRSPosterConfiguration\"8"
+ "v24@?0@\"NSArray<__PRSPosterUpdateResult__>\"8@\"NSError\"16"
+ "v24@?0q8^B16"
+ "v32@0:8q16@?24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSURL\"16^B24"
+ "v56@0:8q16q24Q32q40@?48"
+ "validatePoster:"
+ "void *UIKitLibrary(void)"
+ "writePNGToURL:error:"
+ "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "%@.zip"
- "-%@"
- "<%@: role=(%@) activePath=(%@)>"
- "@\"BSProcessHandle\""
- "@40@0:8@16o^@24o^@32"
- "@40@0:8@?16o^@24o^@32"
- "Archive is unsupported"
- "Archive version %lu is older than min supported %lu"
- "B16@?0@\"NSURL\"8"
- "B24@0:8^B16"
- "B36@0:8B16@20o^@28"
- "Cannot archive to unknown format"
- "Class getPUIImageOnDiskFormatClass(void)_block_invoke"
- "Could not open file handle for reading from URL %@: %@"
- "Could not read data from file handle %@: %@"
- "DE"
- "Error marking '%@' as purgable %@ - %d"
- "Error marking '%@' as purgable - %d"
- "Failed to get final archive URL"
- "Failed to mark URL as purgable: %{public}@"
- "IOSurface *soft_PUIIOSurfaceFromCGImage(CGImageRef, BOOL)"
- "Manifest data failed to load from URL %@, error: %@"
- "Manifest is nil due to prior errors (or not found), bailing."
- "NO"
- "NSString *getPUIImageEncoderErrorDomain(void)"
- "NSURL_PRSAdditions.m"
- "No manifest found, Unsupported archive"
- "PBUICodableImage BSXPCDecoding failed: %@"
- "PBUICodableImage.m"
- "PFPosterRoleIsValid(role)"
- "PRSArchiverZipData_block_invoke"
- "PRSPosterArchiveManifest"
- "PRSPosterArchiver.m"
- "PRSPosterArchiver: archive_entry greater than allowed size of %{public}zu."
- "PRSPosterArchiver: archive_entry with absolute path encountered...ignoring leading %zu of %zu bytes."
- "PRSPosterArchiver: archive_entry with no path after sanitization encountered."
- "PRSPosterArchiver: archive_entry with no path encountered."
- "PRSPosterArchiver: archive_read unable to set supported compression formats - %{public}s."
- "PRSPosterArchiver: archive_read unable to set supported formats - %{public}s."
- "PRSPosterArchiver: archive_read_data_block failed - %{public}s."
- "PRSPosterArchiver: archive_read_disk unable to set lookup functions - %{public}s."
- "PRSPosterArchiver: archive_read_disk unable to set reader symlink mode - %{public}s."
- "PRSPosterArchiver: archive_read_next_header failed - %{public}s."
- "PRSPosterArchiver: archive_write unable to open file descriptor %{public}d - %{public}s."
- "PRSPosterArchiver: archive_write_data failed - %{public}s."
- "PRSPosterArchiver: archive_write_data_block failed - %{public}s."
- "PRSPosterArchiver: archive_write_disk unable to set lookup functions - %{public}s."
- "PRSPosterArchiver: archive_write_disk unable to set options - %{public}s."
- "PRSPosterArchiver: archive_write_finish_entry failed - %{public}s."
- "PRSPosterArchiver: archive_write_header failed - %{public}s."
- "PRSPosterArchiver: data for %@ is nil"
- "PRSPosterArchiver: failed to create directory at %@ - %@."
- "PRSPosterArchiver: failed to create temporary directory at %{public}@ - %@."
- "PRSPosterArchiver: failed to open file for header of type %{public}ud - %{public}s."
- "PRSPosterArchiver: non-directory archive target path %@."
- "PRSPosterArchiver: not writing archive_entry with unknown size"
- "PRSPosterArchiver: unable to close archive_read - %{public}s."
- "PRSPosterArchiver: unable to close archive_write - %{public}s."
- "PRSPosterArchiver: unable to close archive_write_disk - %{public}s."
- "PRSPosterArchiver: unable to close file descriptor %{public}d for %@ (leaking) - %{public}s."
- "PRSPosterArchiver: unable to close file descriptor %{public}d for header (leaking) - %{public}s."
- "PRSPosterArchiver: unable to close read disk archive - %{public}s."
- "PRSPosterArchiver: unable to create directory for URL %@"
- "PRSPosterArchiver: unable to create output file %@ - %{public}s."
- "PRSPosterArchiver: unable to free archive_read (leaking) - %p."
- "PRSPosterArchiver: unable to free archive_read_disk (leaking) - %p."
- "PRSPosterArchiver: unable to free archive_write (leaking) - %p."
- "PRSPosterArchiver: unable to free archive_write_disk (leaking) - %p."
- "PRSPosterArchiver: unable to free read disk archive (leaking) - %p."
- "PRSPosterArchiver: unable to fstat %{public}d for %@ - %{public}s."
- "PRSPosterArchiver: unable to mmap file descriptor %{public}d for %@ - %{public}s."
- "PRSPosterArchiver: unable to open archive_read - %{public}s."
- "PRSPosterArchiver: unable to open file %@ - %{public}s."
- "PRSPosterArchiver: unable to open non-file URL %@."
- "PRSPosterArchiver: unable to open read disk archive - %{public}s."
- "PRSPosterArchiver: unable to read file data from descriptor %{public}d for header - %{public}s."
- "PRSPosterArchiver: unable to resolve physical path for destination path %@ - %s."
- "PRSPosterArchiver: unable to set archive_write supported compression formats - %{public}s."
- "PRSPosterArchiver: unable to set archive_write supported formats - %{public}s."
- "PRSPosterArchiver: unable to write data to url %@"
- "PRSPosterArchiver: unable to write to non-file URL %@."
- "PRSPosterArchiverErrorDomain"
- "PRSService-serviceNotificationCenter"
- "PRSServiceDidUpdateActivePosterConfigurationNotification"
- "PRSServiceDidUpdateAssociatedHomeScreenPosterConfigurationNotification"
- "PRSServiceDidUpdatePosterConfigurationNotification"
- "PRSServiceDidUpdateSelectedPosterConfigurationNotification;"
- "PRSServiceFromSelectedPosterConfigurationUserInfoKey"
- "PRSServiceHomeScreenAssociatedPosterConfigurationUserInfoKey"
- "PRSServiceToSelectedPosterConfigurationUserInfoKey"
- "PRSServiceUpdatedPosterConfigurationUserInfoKey"
- "PRSServiceWillUpdateActivePosterConfigurationNotification"
- "PRSServiceWillUpdateSelectedPosterConfigurationNotification;"
- "PRSZipArchive"
- "PUIIOSurfaceFromCGImage"
- "PUIImageEncoderErrorDomain"
- "PUIImageOnDiskFormat"
- "PosterConfigurations"
- "Process has disallow AppleArchive entitlement and thus cannot archive to that format"
- "Process has disallow AppleArchive entitlement and thus cannot unarchive that format"
- "Q8@?0"
- "Somehow a PBUICodableImage was made that had no actual source or image."
- "T@\"BSProcessHandle\",&,N,V_processHandle"
- "T@\"NSDictionary\",C,N,V_dictionaryRepresentation"
- "T@\"NSFileManager\",&,N,V_fileManager"
- "T@\"NSURL\",C,N,V_unarchivingContainerURL"
- "TQ,R,N"
- "TYP,PAT,LNK,DEV,DAT,MOD,FLG,MTM,BTM,CTM,HLC,CLC"
- "Tq,R,N"
- "URLByAppendingPathExtension:"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "Unable to copy configuration contents to container URL %@ : %@"
- "Unable to copy contents for poster configuration: %@"
- "Unable to create container directory for archiving: %@"
- "Unable to create directory for poster configuration: %@"
- "Unable to create incoming poster configuration: %@"
- "Unable to create placement URL: %@"
- "Unable to create poster manifest data: %@"
- "Unable to resolve format for file to be unarchived"
- "Unable to write manifest data to URL %@: %@"
- "[self isFileURL]"
- "_dictionaryRepresentation"
- "_lock_buildActivePosterObserverUpdatesForClient:updatedRoles:"
- "_lock_issueUpdateForRoles:"
- "_processHandle"
- "_unarchiveWithHandler:manifest:error:"
- "_unarchivingContainerURL"
- "apa"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:counterpart:"
- "archiveExtensionForFormat:"
- "archiveVersion"
- "buildVersion"
- "bytes"
- "closeFile"
- "com.apple.PaperBoardUI.RendererService"
- "com.apple.PosterBoardServices.UnarchiveConfigurationStore"
- "com.apple.posterkit.role.identifier"
- "compression"
- "copyItemAtURL:toURL:error:"
- "currentCalendar"
- "dataRepresentationWithError:"
- "dataStoreVersion"
- "date"
- "dateByAddingComponents:toDate:options:"
- "deflate"
- "domain"
- "enumerateObjectsUsingBlock:"
- "fileDescriptor"
- "fileExistsAtPath:isDirectory:"
- "fileHandleForReading"
- "fileHandleForReadingFromURL:error:"
- "fileHandleForWriting"
- "fileManager"
- "formatForData:"
- "initWithBytesNoCopy:length:deallocator:"
- "initWithDataRepresentation:"
- "initWithDictionaryRepresentation:"
- "initWithRole:activePath:"
- "initWithRole:activePoster:"
- "initWithVariation:saturation:luminance:"
- "initializeRoles:"
- "isFileURL"
- "isManifestDictionaryValid:"
- "issueUpdateForRoles:"
- "latestConfigurationSupplement"
- "latestConfigurationVersion"
- "manifest"
- "manifestVersion"
- "markURLPurgableAfterOneHour:error:"
- "minSupportedArchiveVersion"
- "moveItemAtURL:toURL:error:"
- "pathComponents"
- "pathWithComponents:"
- "pipe"
- "plist"
- "postNotificationName:object:userInfo:"
- "posting PRSServiceDidUpdateActivePosterConfigurationNotification with userInfo=%{public}@"
- "posting PRSServiceDidUpdateAssociatedHomeScreenPosterConfigurationNotification with userInfo=%{public}@"
- "processHandle"
- "prs_URLExists:"
- "prs_isDirectory"
- "prs_isPurgable"
- "prs_setPurgable:afterDate:error:"
- "prs_unmarkAsPurgable"
- "readDataUpToLength:error:"
- "serviceNotificationCenterWithError:"
- "setDictionaryRepresentation:"
- "setFileManager:"
- "setHour:"
- "setProcessHandle:"
- "setUnarchivingContainerURL:"
- "subarrayWithRange:"
- "temporaryDirectory"
- "timeIntervalSince1970"
- "unarchiveConfigurationAppleArchiveAtURL:manifest:error:"
- "unarchiveConfigurationAppleArchiveData:manifest:error:"
- "unarchiveConfigurationZipArchiveAtURL:manifest:error:"
- "unarchiveConfigurationZipArchiveData:manifest:error:"
- "unarchivingContainerURL"
- "unarchivingContainerURL %@ is not reachable URL : %@"
- "unsignedLongLongValue"
- "unsupportedVersions"
- "v24@?0@\"PRSWallpaperObserverState\"8@\"PRSWallpaperObserverTransition\"16"
- "v24@?0^v8Q16"
- "v32@?0@\"NSString\"8@\"PRSPosterConfiguration\"16^B24"
- "v32@?0@\"NSURL\"8Q16^B24"
- "writeData:error:"
- "writeToURL:atomically:"
- "zapa"
- "zip"

```
