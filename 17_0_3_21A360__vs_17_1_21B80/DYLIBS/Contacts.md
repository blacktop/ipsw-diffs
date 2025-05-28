## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3616.1.0.0.0
-  __TEXT.__text: 0x17a798
-  __TEXT.__auth_stubs: 0x2d00
-  __TEXT.__objc_methlist: 0x1519c
+3624.2.0.0.0
+  __TEXT.__text: 0x17cdfc
+  __TEXT.__auth_stubs: 0x2e70
+  __TEXT.__objc_methlist: 0x15484
   __TEXT.__const: 0x1140
-  __TEXT.__gcc_except_tab: 0x2624
-  __TEXT.__cstring: 0xceaa
-  __TEXT.__oslogstring: 0x626e
+  __TEXT.__gcc_except_tab: 0x2690
+  __TEXT.__cstring: 0xcf8a
+  __TEXT.__oslogstring: 0x6491
   __TEXT.__dlopen_cstrs: 0x33e
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xcec

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x344
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x78b0
+  __TEXT.__unwind_info: 0x797c
   __TEXT.__eh_frame: 0x1c88
-  __TEXT.__objc_classname: 0x3772
-  __TEXT.__objc_methname: 0x244af
-  __TEXT.__objc_methtype: 0x4409
-  __TEXT.__objc_stubs: 0x1a200
-  __DATA_CONST.__got: 0xd30
-  __DATA_CONST.__const: 0x5948
-  __DATA_CONST.__objc_classlist: 0xe48
+  __TEXT.__objc_classname: 0x37ea
+  __TEXT.__objc_methname: 0x24abd
+  __TEXT.__objc_methtype: 0x4513
+  __TEXT.__objc_stubs: 0x1a700
+  __DATA_CONST.__got: 0xd40
+  __DATA_CONST.__const: 0x59c0
+  __DATA_CONST.__objc_classlist: 0xe60
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1bcf8
-  __DATA_CONST.__objc_selrefs: 0x7fb8
+  __DATA_CONST.__objc_const: 0x1c070
+  __DATA_CONST.__objc_selrefs: 0x8110
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__cfstring: 0xc8a0
-  __AUTH_CONST.__const: 0x6010
-  __AUTH_CONST.__objc_const: 0xbb60
+  __AUTH_CONST.__cfstring: 0xc9e0
+  __AUTH_CONST.__const: 0x60b0
+  __AUTH_CONST.__objc_const: 0xbcc8
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__auth_ptr: 0x88
-  __AUTH_CONST.__auth_got: 0x1690
+  __AUTH_CONST.__auth_got: 0x1748
   __AUTH.__data: 0x5e8
-  __AUTH.__objc_data: 0x4998
+  __AUTH.__objc_data: 0x4a88
   __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x10f8
-  __DATA.__objc_superrefs: 0x838
-  __DATA.__objc_ivar: 0xf50
+  __DATA.__objc_classrefs: 0x1118
+  __DATA.__objc_superrefs: 0x848
+  __DATA.__objc_ivar: 0xf74
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x2bd8
-  __DATA.__bss: 0x20b0
+  __DATA.__data: 0x2bc8
+  __DATA.__bss: 0x20e0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x4f10
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10586
-  Symbols:   30441
-  CStrings:  9424
+  Functions: 10663
+  Symbols:   30707
+  CStrings:  9519
 
Symbols:
+ +[CNContact(Predicates_Private) predicateForContactsWithWallpaperMetadata]
+ +[CNContactMetadataPersistentStoreManager performLightweightMigrationIfNeededError:]
+ +[CNContactMetadataPersistentStoreManager performLightweightMigrationIfNeededError:].cold.1
+ +[CNContactMetadataPersistentStoreManager performLightweightMigrationIfNeededError:].cold.2
+ +[CNContactMetadataPersistentStoreManager sharedPersistentContainerForModel:storeLocation:]
+ +[CNContactMetadataPersistentStoreManager storeFileURLForLocation:]
+ +[CNContactStore(Favorites) isXPCDataMapperStore:]
+ +[CNContactStoreContactsFetchResultSharedAvatarDecorator allNicknamesForContact:]
+ +[CNImageUtilsBitmapFormat bitmapFormatWithBitmapImage:]
+ +[CNImageUtilsBitmapFormat supportsSecureCoding]
+ +[CNUnifiedContacts indexOfPreferredContactForImage:]
+ +[CNUnifiedContacts indexOfPreferredContactForWallpaper:prefersSharedImage:]
+ +[CNUnifiedContacts sortedContacts:withPreferredContact:]
+ +[CNUnifiedContacts unifyWallpaperOfContacts:intoContact:availableKeyDescriptor:]
+ +[CNUnifiedContacts wallpaperValuePropertiesByKey]
+ +[CNUnifiedContacts wallpaperValuePropertyKeys]
+ +[CNVisualSimilarity fingerprintForImageRequestHandler:]
+ +[CNVisualSimilarity fingerprintForImageRequestHandler:].cold.1
+ +[CNWithWallpaperMetadataContactPredicate supportsSecureCoding]
+ -[CNAggregateContactStore getBackgroundColorOnImageData:bitmapFormat:error:]
+ -[CNAggregateContactStore(Favorites) XPCDataMapperStore]
+ -[CNContactImageStore countForFetchRequest:error:]
+ -[CNContactMetadataPersistentStoreManager loadPersistentStoresError]
+ -[CNContactMetadataPersistentStoreManager setLoadPersistentStoresError:]
+ -[CNContactMetadataPersistentStoreManager setupIfNeeded]
+ -[CNContactMetadataPersistentStoreManager setupIfNeeded].cold.1
+ -[CNContactStoreContactsFetchResultSharedAvatarDecorator doesKeysToFetchContainRequiredKeys]
+ -[CNDataMapperContactStore getBackgroundColorOnImageData:bitmapFormat:error:]
+ -[CNFavorites XPCDataMapper]
+ -[CNImageUtilsBitmapFormat bitmapInfo]
+ -[CNImageUtilsBitmapFormat bitsPerComponent]
+ -[CNImageUtilsBitmapFormat bitsPerPixel]
+ -[CNImageUtilsBitmapFormat bytesPerRow]
+ -[CNImageUtilsBitmapFormat colorSpace]
+ -[CNImageUtilsBitmapFormat encodeWithCoder:]
+ -[CNImageUtilsBitmapFormat height]
+ -[CNImageUtilsBitmapFormat initWithBitmapContext:]
+ -[CNImageUtilsBitmapFormat initWithCoder:]
+ -[CNImageUtilsBitmapFormat isEqual:]
+ -[CNImageUtilsBitmapFormat isEqualToFormat:]
+ -[CNImageUtilsBitmapFormat setBitmapInfo:]
+ -[CNImageUtilsBitmapFormat setBitsPerComponent:]
+ -[CNImageUtilsBitmapFormat setBitsPerPixel:]
+ -[CNImageUtilsBitmapFormat setBytesPerRow:]
+ -[CNImageUtilsBitmapFormat setColorSpace:]
+ -[CNImageUtilsBitmapFormat setHeight:]
+ -[CNImageUtilsBitmapFormat setWidth:]
+ -[CNImageUtilsBitmapFormat width]
+ -[CNSharedProfileStateOracle currentNicknameHasValidVisualIdentityData]
+ -[CNSharedProfileStateOracle nicknameHasValidVisualIdentityData:]
+ -[CNSharedProfileStateOracle pendingNicknameHasValidVisualIdentityData]
+ -[CNWallpaper contentIsSensitive]
+ -[CNWallpaper initWithPosterArchiveData:contentIsSensitive:]
+ -[CNWallpaper initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:contentIsSensitive:]
+ -[CNWallpaper initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:contentIsSensitive:].cold.1
+ -[CNWallpaper initWithPosterArchiveData:metadata:contentIsSensitive:]
+ -[CNWallpaper setContentIsSensitive:]
+ -[CNWithWallpaperMetadataContactPredicate description]
+ -[CNWithWallpaperMetadataContactPredicate encodeWithCoder:]
+ -[CNWithWallpaperMetadataContactPredicate hash]
+ -[CNWithWallpaperMetadataContactPredicate initWithCoder:]
+ -[CNWithWallpaperMetadataContactPredicate isEqual:]
+ -[CNWithWallpaperMetadataContactPredicate shortDebugDescription]
+ -[CNXPCDataMapper getBackgroundColorOnImageData:bitmapFormat:error:]
+ -[CNiOSABWithWallpaperMetadataContactPredicate cn_ABQSLPredicateForAddressBook:fetchRequest:error:]
+ -[CNiOSABWithWallpaperMetadataContactPredicate cn_copyPeopleInAddressBook:fetchRequest:matchInfos:environment:error:]
+ -[CNiOSABWithWallpaperMetadataContactPredicate cn_supportsEncodedFetching]
+ -[CNiOSABWithWallpaperMetadataContactPredicate cn_supportsNativeBatchFetch]
+ -[CNiOSABWithWallpaperMetadataContactPredicate cn_supportsNativeSorting]
+ -[CNiOSAddressBookDataMapper _logIngoringImplicitAugmentationLinkedSetContactIdentifier:]
+ -[_CNContactsLogger gettingBackgroundColor:]
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table170
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table204
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table214
+ _ABOSLogImageMetadata
+ _CGBitmapContextCreate
+ _CGBitmapContextGetBitmapInfo
+ _CGBitmapContextGetBitsPerComponent
+ _CGBitmapContextGetBitsPerPixel
+ _CGBitmapContextGetBytesPerRow
+ _CGBitmapContextGetColorSpace
+ _CGBitmapContextGetHeight
+ _CGBitmapContextGetWidth
+ _CGBitmapGetAlignedBytesPerRow
+ _CGColorSpaceCopyPropertyList
+ _CGColorSpaceCreateDeviceRGB
+ _CGColorSpaceCreateWithPropertyList
+ _CGColorSpaceGetNumberOfComponents
+ _CGColorSpaceRelease
+ _CGImageGetBitmapInfo
+ _CGImageGetBitsPerComponent
+ _CGImageGetBitsPerPixel
+ _CGImageGetBytesPerRow
+ _CGImageGetColorSpace
+ _CGImageGetHeight
+ _CGImageGetWidth
+ _CNImageUtilsCreateMmappedBitmapContext
+ _CNImageUtilsCreateMmappedBitmapContext.cold.1
+ _NSPersistentStoreCoordinatorResourceBundlesForMigration
+ _OBJC_CLASS_$_CNImageUtilsBitmapFormat
+ _OBJC_CLASS_$_CNWithWallpaperMetadataContactPredicate
+ _OBJC_CLASS_$_CNiOSABWithWallpaperMetadataContactPredicate
+ _OBJC_CLASS_$_NSPersistentStoreCoordinator
+ _OBJC_IVAR_$_CNContactMetadataPersistentStoreManager._loadPersistentStoresError
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._bitmapInfo
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._bitsPerComponent
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._bitsPerPixel
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._bytesPerRow
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._colorSpace
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._height
+ _OBJC_IVAR_$_CNImageUtilsBitmapFormat._width
+ _OBJC_IVAR_$_CNWallpaper._contentIsSensitive
+ _OBJC_METACLASS_$_CNImageUtilsBitmapFormat
+ _OBJC_METACLASS_$_CNWithWallpaperMetadataContactPredicate
+ _OBJC_METACLASS_$_CNiOSABWithWallpaperMetadataContactPredicate
+ __OBJC_$_CLASS_METHODS_CNContactStore(FamilyCircle|UnitTesting|Spotlight|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|Favorites|Suggestions)
+ __OBJC_$_CLASS_METHODS_CNImageUtilsBitmapFormat
+ __OBJC_$_CLASS_METHODS_CNWithWallpaperMetadataContactPredicate
+ __OBJC_$_CLASS_PROP_LIST_CNImageUtilsBitmapFormat
+ __OBJC_$_INSTANCE_METHODS_CNAggregateContactStore(Spotlight|iOSAB|Favorites|Suggestions)
+ __OBJC_$_INSTANCE_METHODS_CNContactStore(FamilyCircle|UnitTesting|Spotlight|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|Favorites|Suggestions)
+ __OBJC_$_INSTANCE_METHODS_CNImageUtilsBitmapFormat
+ __OBJC_$_INSTANCE_METHODS_CNWithWallpaperMetadataContactPredicate
+ __OBJC_$_INSTANCE_METHODS_CNiOSABWithWallpaperMetadataContactPredicate
+ __OBJC_$_INSTANCE_VARIABLES_CNImageUtilsBitmapFormat
+ __OBJC_$_PROP_LIST_CNImageUtilsBitmapFormat
+ __OBJC_$_PROP_LIST_CNiOSABWithWallpaperMetadataContactPredicate
+ __OBJC_CLASS_PROTOCOLS_$_CNImageUtilsBitmapFormat
+ __OBJC_CLASS_PROTOCOLS_$_CNiOSABWithWallpaperMetadataContactPredicate
+ __OBJC_CLASS_RO_$_CNImageUtilsBitmapFormat
+ __OBJC_CLASS_RO_$_CNWithWallpaperMetadataContactPredicate
+ __OBJC_CLASS_RO_$_CNiOSABWithWallpaperMetadataContactPredicate
+ __OBJC_METACLASS_RO_$_CNImageUtilsBitmapFormat
+ __OBJC_METACLASS_RO_$_CNWithWallpaperMetadataContactPredicate
+ __OBJC_METACLASS_RO_$_CNiOSABWithWallpaperMetadataContactPredicate
+ ___44-[_CNContactsLogger gettingBackgroundColor:]_block_invoke
+ ___44-[_CNContactsLogger gettingBackgroundColor:]_block_invoke_2
+ ___47+[CNUnifiedContacts wallpaperValuePropertyKeys]_block_invoke
+ ___50+[CNUnifiedContacts wallpaperValuePropertiesByKey]_block_invoke
+ ___50+[CNUnifiedContacts wallpaperValuePropertiesByKey]_block_invoke_2
+ ___50-[CNContactImageStore countForFetchRequest:error:]_block_invoke
+ ___51-[CNWithWallpaperMetadataContactPredicate isEqual:]_block_invoke
+ ___53+[CNUnifiedContacts indexOfPreferredContactForImage:]_block_invoke
+ ___56-[CNAggregateContactStore(Favorites) XPCDataMapperStore]_block_invoke
+ ___56-[CNContactMetadataPersistentStoreManager setupIfNeeded]_block_invoke
+ ___56-[CNContactMetadataPersistentStoreManager setupIfNeeded]_block_invoke.cold.1
+ ___65-[CNContactMetadataPersistentStoreManager initWithStoreLocation:]_block_invoke
+ ___76+[CNUnifiedContacts indexOfPreferredContactForWallpaper:prefersSharedImage:]_block_invoke
+ ___76+[CNUnifiedContacts indexOfPreferredContactForWallpaper:prefersSharedImage:]_block_invoke_2
+ ___77-[CNDataMapperContactStore getBackgroundColorOnImageData:bitmapFormat:error:]_block_invoke
+ ___block_descriptor_40_e8_32w_e50_v24?0"NSPersistentStoreDescription"8"NSError"16lw32l8
+ ___block_descriptor_56_e8_32s40r48r_e32_v16?0"NSManagedObjectContext"8ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e14_v16?0?<v?>8lr56l8s32l8s40l8s48l8r64l8
+ ___block_literal_global.416
+ ___block_literal_global.420
+ ___block_literal_global.47
+ _imageValuePropertyKeys.cn_once_object_3
+ _imageValuePropertyKeys.cn_once_token_3
+ _initWithStoreLocation:.cn_once_object_5
+ _initWithStoreLocation:.cn_once_token_5
+ _mmap
+ _nonNameSingleValuePropertiesByKey.cn_once_object_5
+ _nonNameSingleValuePropertiesByKey.cn_once_token_5
+ _objc_msgSend$XPCDataMapper
+ _objc_msgSend$XPCDataMapperStore
+ _objc_msgSend$bitmapInfo
+ _objc_msgSend$bitsPerComponent
+ _objc_msgSend$bytesPerRow
+ _objc_msgSend$colorSpace
+ _objc_msgSend$contentIsSensitive
+ _objc_msgSend$countForFetchRequest:error:
+ _objc_msgSend$doesKeysToFetchContainRequiredKeys
+ _objc_msgSend$fingerprintForImageRequestHandler:
+ _objc_msgSend$getBackgroundColorOnImageData:bitmapFormat:error:
+ _objc_msgSend$gettingBackgroundColor:
+ _objc_msgSend$height
+ _objc_msgSend$indexOfPreferredContactForImage:
+ _objc_msgSend$indexOfPreferredContactForWallpaper:prefersSharedImage:
+ _objc_msgSend$initWithPosterArchiveData:contentIsSensitive:
+ _objc_msgSend$initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:contentIsSensitive:
+ _objc_msgSend$initWithPosterArchiveData:metadata:contentIsSensitive:
+ _objc_msgSend$isConfiguration:compatibleWithStoreMetadata:
+ _objc_msgSend$isEqualToFormat:
+ _objc_msgSend$isImplicitAugmentation
+ _objc_msgSend$load:
+ _objc_msgSend$loadPersistentStoresError
+ _objc_msgSend$loadPersistentStoresWithCompletionHandler:
+ _objc_msgSend$metadataForPersistentStoreOfType:URL:options:error:
+ _objc_msgSend$nicknameHasValidVisualIdentityData:
+ _objc_msgSend$persistentStoreDescriptionWithURL:
+ _objc_msgSend$predicateForContactsWithWallpaperMetadata
+ _objc_msgSend$setBitmapInfo:
+ _objc_msgSend$setBitsPerComponent:
+ _objc_msgSend$setBitsPerPixel:
+ _objc_msgSend$setBytesPerRow:
+ _objc_msgSend$setColorSpace:
+ _objc_msgSend$setContentIsSensitive:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setLoadPersistentStoresError:
+ _objc_msgSend$setOption:forKey:
+ _objc_msgSend$setPersistentStoreDescriptions:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$setupIfNeeded
+ _objc_msgSend$sharedPersistentContainerForModel:storeLocation:
+ _objc_msgSend$sortedContacts:withPreferredContact:
+ _objc_msgSend$storeFileURLForLocation:
+ _objc_msgSend$unifyWallpaperOfContacts:intoContact:availableKeyDescriptor:
+ _objc_msgSend$wallpaperValuePropertiesByKey
+ _objc_msgSend$wallpaperValuePropertyKeys
+ _objc_msgSend$width
+ _vm_page_size
+ _wallpaperValuePropertiesByKey.cn_once_object_2
+ _wallpaperValuePropertiesByKey.cn_once_token_2
+ _wallpaperValuePropertyKeys.cn_once_object_4
+ _wallpaperValuePropertyKeys.cn_once_token_4
- +[CNContactMetadataPersistentStoreManager sharedPersistentContainer]
- +[CNUnifiedContacts indexOfPreferredContactForImage:prefersSharedImage:]
- +[CNVisualSimilarity fingerprintForData:].cold.1
- -[CNContactMetadataPersistentStoreManager setupIfNeeded:]
- -[CNContactMetadataPersistentStoreManager setupIfNeeded:].cold.1
- -[CNContactStoreContactsFetchResultSharedAvatarDecorator doesKeysToFetchContainRequiredImageKeys]
- -[CNWallpaper initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:]
- -[CNWallpaper initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:].cold.1
- -[CNWallpaper initWithPosterArchiveData:metadata:]
- GCC_except_table111
- GCC_except_table125
- GCC_except_table140
- GCC_except_table142
- GCC_except_table149
- GCC_except_table152
- GCC_except_table154
- GCC_except_table158
- GCC_except_table169
- GCC_except_table176
- GCC_except_table178
- GCC_except_table181
- GCC_except_table183
- GCC_except_table188
- GCC_except_table193
- GCC_except_table203
- GCC_except_table208
- GCC_except_table211
- GCC_except_table213
- GCC_except_table29
- GCC_except_table55
- __OBJC_$_CLASS_METHODS_CNContactStore(FamilyCircle|UnitTesting|Spotlight|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|Suggestions)
- __OBJC_$_INSTANCE_METHODS_CNAggregateContactStore(Spotlight|iOSAB|Suggestions)
- __OBJC_$_INSTANCE_METHODS_CNContactStore(FamilyCircle|UnitTesting|Spotlight|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|Suggestions)
- ___68+[CNContactMetadataPersistentStoreManager sharedPersistentContainer]_block_invoke
- ___72+[CNUnifiedContacts indexOfPreferredContactForImage:prefersSharedImage:]_block_invoke
- ___72+[CNUnifiedContacts indexOfPreferredContactForImage:prefersSharedImage:]_block_invoke_2
- ___block_literal_global.407
- ___block_literal_global.41
- ___block_literal_global.411
- _imageValuePropertyKeys.cn_once_object_2
- _imageValuePropertyKeys.cn_once_token_2
- _nonNameSingleValuePropertiesByKey.cn_once_object_3
- _nonNameSingleValuePropertiesByKey.cn_once_token_3
- _objc_msgSend$addPersistentStoreWithType:configuration:URL:options:error:
- _objc_msgSend$doesKeysToFetchContainRequiredImageKeys
- _objc_msgSend$indexOfPreferredContactForImage:prefersSharedImage:
- _objc_msgSend$initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:
- _objc_msgSend$initWithPosterArchiveData:metadata:
- _objc_msgSend$setupIfNeeded:
- _objc_msgSend$sharedPersistentContainer
- _sharedPersistentContainer.cn_once_object_5
- _sharedPersistentContainer.cn_once_token_5
CStrings:
+ "%04llx Contact: %{public}@"
+ "%04llx Predicate: %{public}@ %{private}@"
+ "-[CNContact predicateForContactsWithWallpaperMetadata]"
+ "@\"NSArray\"40@0:8@\"NSData\"16@\"CNImageUtilsBitmapFormat\"24^@32"
+ "@24@0:8^{CGContext=}16"
+ "@24@0:8^{CGImage=}16"
+ "@72@0:8@16@24@32@40@48B56@60B68"
+ "CNImageUtilities.m"
+ "CNImageUtilsBitmapFormat"
+ "CNImageUtilsCreateMmappedBitmapContext"
+ "CNWithWallpaperMetadataContactPredicate"
+ "CNiOSABWithWallpaperMetadataContactPredicate"
+ "Did not perform migration, existing model is already compatible with store metadata"
+ "Did not perform migration, failed to load persistent stores: %@"
+ "Did not perform migration, no existing managed object model found"
+ "Did not perform migration, no store metadata found, %@"
+ "Failed to load persistent stores: %@"
+ "Failed to setup store: %@"
+ "GettingBackgroundColor"
+ "Loaded container with description: %@"
+ "No recent avatar or poster available for contact %@"
+ "Q32@0:8@16^@24"
+ "T@\"NSError\",&,N,V_loadPersistentStoresError"
+ "TB,N,V_contentIsSensitive"
+ "TI,V_bitmapInfo"
+ "TQ,V_bitsPerComponent"
+ "TQ,V_bitsPerPixel"
+ "TQ,V_bytesPerRow"
+ "TQ,V_height"
+ "TQ,V_width"
+ "T^{CGColorSpace=},&,V_colorSpace"
+ "WithWallpaperMetadataPredicate"
+ "XPCDataMapper"
+ "XPCDataMapperStore"
+ "[CNContactBufferDecoder _applyImageDataFromByteCursor:end:] reading image format %d of length %lu into NSData"
+ "^{CGColorSpace=}"
+ "^{CGColorSpace=}16@0:8"
+ "_bitmapInfo"
+ "_bitsPerComponent"
+ "_bitsPerPixel"
+ "_bytesPerRow"
+ "_colorSpace"
+ "_contentIsSensitive"
+ "_height"
+ "_loadPersistentStoresError"
+ "_processContactsFromSaveContext delete, ignoring augmented contact identifier : %{public}@"
+ "_width"
+ "bitmapFormatWithBitmapImage:"
+ "bitmapInfo"
+ "bitsPerComponent"
+ "bitsPerComponent == 5 || bitsPerComponent == 8"
+ "bitsPerPixel"
+ "bpc"
+ "bpp"
+ "bpr"
+ "bytesPerRow"
+ "colorSpace"
+ "contentIsSensitive"
+ "cs"
+ "currentNicknameHasValidVisualIdentityData"
+ "doesKeysToFetchContainRequiredKeys"
+ "fingerprintForImageRequestHandler:"
+ "getBackgroundColorOnImageData:bitmapFormat:error:"
+ "getBackgroundColorOnImageData:bitmapFormat:withReply:"
+ "gettingBackgroundColor:"
+ "h"
+ "height"
+ "indexOfPreferredContactForImage:"
+ "indexOfPreferredContactForWallpaper:prefersSharedImage:"
+ "initWithBitmapContext:"
+ "initWithPosterArchiveData:contentIsSensitive:"
+ "initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:contentIsSensitive:"
+ "initWithPosterArchiveData:metadata:contentIsSensitive:"
+ "isConfiguration:compatibleWithStoreMetadata:"
+ "isEqualToFormat:"
+ "load:"
+ "loadPersistentStoresError"
+ "metadataForPersistentStoreOfType:URL:options:error:"
+ "nicknameHasValidVisualIdentityData:"
+ "pendingNicknameHasValidVisualIdentityData"
+ "performLightweightMigrationIfNeededError:"
+ "persistentStoreDescriptionWithURL:"
+ "predicateForContactsWithWallpaperMetadata"
+ "setBitmapInfo:"
+ "setBitsPerComponent:"
+ "setBitsPerPixel:"
+ "setBytesPerRow:"
+ "setColorSpace:"
+ "setContentIsSensitive:"
+ "setHeight:"
+ "setLoadPersistentStoresError:"
+ "setPersistentStoreDescriptions:"
+ "setWidth:"
+ "setupIfNeeded"
+ "sharedPersistentContainerForModel:storeLocation:"
+ "sortedContacts:withPreferredContact:"
+ "storeFileURLForLocation:"
+ "unifyWallpaperOfContacts:intoContact:availableKeyDescriptor:"
+ "userMightHaveUnconfiguredPersistenceStack"
+ "v24@0:8^{CGColorSpace=}16"
+ "v40@0:8@\"NSData\"16@\"CNImageUtilsBitmapFormat\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "w"
+ "wallpaperValuePropertiesByKey"
+ "wallpaperValuePropertyKeys"
+ "width"
- "%04llx Contact: %@"
- "%04llx Predicate: %{private}@"
- "@68@0:8@16@24@32@40@48B56@60"
- "ContactMetadata store couldn't be added to the coordinator: %@"
- "No recent avatar or poster available to for contact %@"
- "addPersistentStoreWithType:configuration:URL:options:error:"
- "doesKeysToFetchContainRequiredImageKeys"
- "indexOfPreferredContactForImage:prefersSharedImage:"
- "initWithPosterArchiveData:fontDescription:fontColorDescription:backgroundColorDescription:extensionBundleID:vertical:visualFingerprintData:"
- "initWithPosterArchiveData:metadata:"
- "setupIfNeeded:"
- "sharedPersistentContainer"

```
