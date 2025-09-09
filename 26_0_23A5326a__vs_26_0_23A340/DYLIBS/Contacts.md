## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3804.100.1.0.0
-  __TEXT.__text: 0x1b632c
+3804.100.1.2.4
+  __TEXT.__text: 0x1b6d80
   __TEXT.__auth_stubs: 0x3280
-  __TEXT.__objc_methlist: 0x1ad40
+  __TEXT.__objc_methlist: 0x1ad68
   __TEXT.__const: 0x20c8
   __TEXT.__gcc_except_tab: 0x3b2c
   __TEXT.__cstring: 0xc982
   __TEXT.__dlopen_cstrs: 0x8de
-  __TEXT.__oslogstring: 0xbaca
+  __TEXT.__oslogstring: 0xbaea
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xdc4
   __TEXT.__swift5_typeref: 0xea1

   __TEXT.__swift5_capture: 0x5d4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x7e78
+  __TEXT.__unwind_info: 0x7e98
   __TEXT.__eh_frame: 0x25c0
   __TEXT.__objc_classname: 0x43df
-  __TEXT.__objc_methname: 0x2b24e
+  __TEXT.__objc_methname: 0x2b32e
   __TEXT.__objc_methtype: 0x53c2
-  __TEXT.__objc_stubs: 0x1e580
+  __TEXT.__objc_stubs: 0x1e5a0
   __DATA_CONST.__got: 0x1b50
-  __DATA_CONST.__const: 0x6198
+  __DATA_CONST.__const: 0x61c0
   __DATA_CONST.__objc_classlist: 0x10e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9618
+  __DATA_CONST.__objc_selrefs: 0x9638
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x9b0
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x1950
-  __AUTH_CONST.__const: 0x69c0
+  __AUTH_CONST.__const: 0x6a38
   __AUTH_CONST.__cfstring: 0xd9c0
-  __AUTH_CONST.__objc_const: 0x2bb08
+  __AUTH_CONST.__objc_const: 0x2bb38
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x5638
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0x1260
+  __DATA.__objc_ivar: 0x1264
   __DATA.__data: 0x2d20
-  __DATA.__bss: 0x2460
+  __DATA.__bss: 0x2920
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x5dc0
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x1028
+  __DATA_DIRTY.__bss: 0xb88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F34889D2-5284-353E-9289-047BC7D41131
-  Functions: 12426
-  Symbols:   36407
-  CStrings:  12759
+  UUID: 3102B528-C4D3-30C6-A202-9928344D087C
+  Functions: 12441
+  Symbols:   36437
+  CStrings:  12765
 
Symbols:
+ +[CN(PropertyDescription) contactCardIgnorableContactChangeProperties]
+ -[CNContact arePropertiesEqualToContact:ignoredProperties:]
+ -[CNContact isEqual:].cold.1
+ -[CNContact isEquivalent:ignoringProperties:]
+ -[CNFavoritesSyncStore setWantsRetryAfterMessageFailure:]
+ -[CNFavoritesSyncStore wantsRetryAfterMessageFailure]
+ -[CNMockFavoritesLogger failedToReadRemoteFavorites:willRetry:]
+ -[CNMockFavoritesLogger failedToWriteRemoteFavorites:willRetry:]
+ -[_CNFavoritesLogger failedToReadRemoteFavorites:willRetry:]
+ -[_CNFavoritesLogger failedToReadRemoteFavorites:willRetry:].cold.1
+ -[_CNFavoritesLogger failedToWriteRemoteFavorites:willRetry:]
+ -[_CNFavoritesLogger failedToWriteRemoteFavorites:willRetry:].cold.1
+ _OBJC_IVAR_$_CNFavoritesSyncStore._wantsRetryAfterMessageFailure
+ ___21-[CNContact isEqual:]_block_invoke_5
+ ___45-[CNContact isEquivalent:ignoringProperties:]_block_invoke
+ ___45-[CNContact isEquivalent:ignoringProperties:]_block_invoke_2
+ ___45-[CNContact isEquivalent:ignoringProperties:]_block_invoke_3
+ ___45-[CNContact isEquivalent:ignoringProperties:]_block_invoke_4
+ ___70+[CN(PropertyDescription) contactCardIgnorableContactChangeProperties]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
+ ___block_literal_global.320
+ ___block_literal_global.327
+ ___block_literal_global.338
+ ___block_literal_global.805
+ ___block_literal_global.856
+ ___block_literal_global.865
+ ___swift_memcpy4_4
+ _addressingGrammarsDescription.cn_once_object_71
+ _addressingGrammarsDescription.cn_once_token_71
+ _addressingGrammarsEncryptedDescription.cn_once_object_72
+ _addressingGrammarsEncryptedDescription.cn_once_token_72
+ _areAllAvailableKeysEqualToContact:ignoringIdentifiers:.cn_once_object_14
+ _areAllAvailableKeysEqualToContact:ignoringIdentifiers:.cn_once_token_14
+ _avatarRecipeDataDescription.cn_once_object_92
+ _avatarRecipeDataDescription.cn_once_token_92
+ _birthdayDescription.cn_once_object_44
+ _birthdayDescription.cn_once_token_44
+ _calendarURIsDescription.cn_once_object_73
+ _calendarURIsDescription.cn_once_token_73
+ _callAlertDescription.cn_once_object_81
+ _callAlertDescription.cn_once_token_81
+ _contactCardIgnorableContactChangeProperties.cn_once_object_22
+ _contactCardIgnorableContactChangeProperties.cn_once_token_22
+ _contactRelationsDescription.cn_once_object_68
+ _contactRelationsDescription.cn_once_token_68
+ _contactTypeDescription.cn_once_object_60
+ _contactTypeDescription.cn_once_token_60
+ _creationDateDescription.cn_once_object_46
+ _creationDateDescription.cn_once_token_46
+ _cropRectDescription.cn_once_object_50
+ _cropRectDescription.cn_once_token_50
+ _datesDescription.cn_once_object_66
+ _datesDescription.cn_once_token_66
+ _departmentDescription.cn_once_object_42
+ _departmentDescription.cn_once_token_42
+ _downtimeWhitelistDescription.cn_once_object_84
+ _downtimeWhitelistDescription.cn_once_token_84
+ _emailAddressesDescription.cn_once_object_64
+ _emailAddressesDescription.cn_once_token_64
+ _explicitDisplayNameDescription.cn_once_object_38
+ _explicitDisplayNameDescription.cn_once_token_38
+ _externalIdentifierDescription.cn_once_object_74
+ _externalIdentifierDescription.cn_once_token_74
+ _externalImageURIDescription.cn_once_object_78
+ _externalImageURIDescription.cn_once_token_78
+ _externalModificationTagDescription.cn_once_object_75
+ _externalModificationTagDescription.cn_once_token_75
+ _externalRepresentationDescription.cn_once_object_76
+ _externalRepresentationDescription.cn_once_token_76
+ _externalUUIDDescription.cn_once_object_77
+ _externalUUIDDescription.cn_once_token_77
+ _familyNameDescription.cn_once_object_28
+ _familyNameDescription.cn_once_token_28
+ _fullscreenImageDataDescription.cn_once_object_52
+ _fullscreenImageDataDescription.cn_once_token_52
+ _givenNameDescription.cn_once_object_26
+ _givenNameDescription.cn_once_token_26
+ _iOSLegacyIdentifierDescription.cn_once_object_24
+ _iOSLegacyIdentifierDescription.cn_once_token_24
+ _identifierDescription.cn_once_object_23
+ _identifierDescription.cn_once_token_23
+ _imageBackgroundColorsDataDescription.cn_once_object_93
+ _imageBackgroundColorsDataDescription.cn_once_token_93
+ _imageDataAvailableDescription.cn_once_object_54
+ _imageDataAvailableDescription.cn_once_token_54
+ _imageDataDescription.cn_once_object_49
+ _imageDataDescription.cn_once_token_49
+ _imageHash.cn_once_object_86
+ _imageHash.cn_once_token_86
+ _imageSyncFailedTimeDescription.cn_once_object_95
+ _imageSyncFailedTimeDescription.cn_once_token_95
+ _imageType.cn_once_object_85
+ _imageType.cn_once_token_85
+ _instantMessagAddressesDescription.cn_once_object_67
+ _instantMessagAddressesDescription.cn_once_token_67
+ _isEqual:.cn_once_object_13
+ _isEqual:.cn_once_token_13
+ _isUsingSharedPhotoDescription.cn_once_object_62
+ _isUsingSharedPhotoDescription.cn_once_token_62
+ _jobTitleDescription.cn_once_object_43
+ _jobTitleDescription.cn_once_token_43
+ _linkIdentifierDescription.cn_once_object_55
+ _linkIdentifierDescription.cn_once_token_55
+ _mapsDataDescription.cn_once_object_83
+ _mapsDataDescription.cn_once_token_83
+ _memojiMetadataDescription.cn_once_object_87
+ _memojiMetadataDescription.cn_once_token_87
+ _middleNameDescription.cn_once_object_27
+ _middleNameDescription.cn_once_token_27
+ _modificationDateDescription.cn_once_object_47
+ _modificationDateDescription.cn_once_token_47
+ _namePrefixDescription.cn_once_object_25
+ _namePrefixDescription.cn_once_token_25
+ _nameSuffixDescription.cn_once_object_29
+ _nameSuffixDescription.cn_once_token_29
+ _nicknameDescription.cn_once_object_31
+ _nicknameDescription.cn_once_token_31
+ _nonGregorianBirthdayDescription.cn_once_object_45
+ _nonGregorianBirthdayDescription.cn_once_token_45
+ _noteDescription.cn_once_object_48
+ _noteDescription.cn_once_token_48
+ _objc_msgSend$arePropertiesEqualToContact:ignoredProperties:
+ _objc_msgSend$failedToReadRemoteFavorites:willRetry:
+ _objc_msgSend$failedToWriteRemoteFavorites:willRetry:
+ _objc_msgSend$wantsRetryAfterMessageFailure
+ _organizationNameDescription.cn_once_object_41
+ _organizationNameDescription.cn_once_token_41
+ _phoneNumbersDescription.cn_once_object_63
+ _phoneNumbersDescription.cn_once_token_63
+ _phonemeDataDescription.cn_once_object_79
+ _phonemeDataDescription.cn_once_token_79
+ _phoneticFamilyNameDescription.cn_once_object_34
+ _phoneticFamilyNameDescription.cn_once_token_34
+ _phoneticGivenNameDescription.cn_once_object_32
+ _phoneticGivenNameDescription.cn_once_token_32
+ _phoneticMiddleNameDescription.cn_once_object_33
+ _phoneticMiddleNameDescription.cn_once_token_33
+ _phoneticOrganizationNameDescription.cn_once_object_35
+ _phoneticOrganizationNameDescription.cn_once_token_35
+ _postalAddressesDescription.cn_once_object_70
+ _postalAddressesDescription.cn_once_token_70
+ _preferredApplePersonaIdentifierDescription.cn_once_object_59
+ _preferredApplePersonaIdentifierDescription.cn_once_token_59
+ _preferredChannelDescription.cn_once_object_82
+ _preferredChannelDescription.cn_once_token_82
+ _preferredForImageDescription.cn_once_object_57
+ _preferredForImageDescription.cn_once_token_57
+ _preferredForNameDescription.cn_once_object_56
+ _preferredForNameDescription.cn_once_token_56
+ _preferredImageComparator.cn_once_object_15
+ _preferredImageComparator.cn_once_token_15
+ _preferredLikenessSourceDescription.cn_once_object_58
+ _preferredLikenessSourceDescription.cn_once_token_58
+ _previousFamilyNameDescription.cn_once_object_30
+ _previousFamilyNameDescription.cn_once_token_30
+ _pronunciationFamilyNameDescription.cn_once_object_37
+ _pronunciationFamilyNameDescription.cn_once_token_37
+ _pronunciationGivenNameDescription.cn_once_object_36
+ _pronunciationGivenNameDescription.cn_once_token_36
+ _sectionForSortingByFamilyNameDescription.cn_once_object_39
+ _sectionForSortingByFamilyNameDescription.cn_once_token_39
+ _sectionForSortingByGivenNameDescription.cn_once_object_40
+ _sectionForSortingByGivenNameDescription.cn_once_token_40
+ _sensitiveContentConfigurationDescription.cn_once_object_94
+ _sensitiveContentConfigurationDescription.cn_once_token_94
+ _sharedPhotoDisplayPreferenceDescription.cn_once_object_61
+ _sharedPhotoDisplayPreferenceDescription.cn_once_token_61
+ _socialProfilesDescription.cn_once_object_69
+ _socialProfilesDescription.cn_once_token_69
+ _syncImageDataDescription.cn_once_object_53
+ _syncImageDataDescription.cn_once_token_53
+ _textAlertDescription.cn_once_object_80
+ _textAlertDescription.cn_once_token_80
+ _thumbnailImageDataDescription.cn_once_object_51
+ _thumbnailImageDataDescription.cn_once_token_51
+ _urlAddressesDescription.cn_once_object_65
+ _urlAddressesDescription.cn_once_token_65
+ _wallpaperDescription.cn_once_object_88
+ _wallpaperDescription.cn_once_token_88
+ _wallpaperMetadataDescription.cn_once_object_89
+ _wallpaperMetadataDescription.cn_once_token_89
+ _wallpaperSyncFailedTimeDescription.cn_once_object_96
+ _wallpaperSyncFailedTimeDescription.cn_once_token_96
+ _wallpaperURIDescription.cn_once_object_91
+ _wallpaperURIDescription.cn_once_token_91
+ _watchWallpaperImageDataDescription.cn_once_object_90
+ _watchWallpaperImageDataDescription.cn_once_token_90
- -[CNContact areAllPropertiesButContactIdentifierEqualToContact:]
- -[CNMockFavoritesLogger failedToReadRemoteFavorites:]
- -[CNMockFavoritesLogger failedToWriteRemoteFavorites:]
- -[_CNFavoritesLogger failedToReadRemoteFavorites:]
- -[_CNFavoritesLogger failedToReadRemoteFavorites:].cold.1
- -[_CNFavoritesLogger failedToWriteRemoteFavorites:]
- -[_CNFavoritesLogger failedToWriteRemoteFavorites:].cold.1
- GCC_except_table188
- ___block_literal_global.802
- ___block_literal_global.853
- ___block_literal_global.862
- _addressingGrammarsDescription.cn_once_object_70
- _addressingGrammarsDescription.cn_once_token_70
- _addressingGrammarsEncryptedDescription.cn_once_object_71
- _addressingGrammarsEncryptedDescription.cn_once_token_71
- _areAllAvailableKeysEqualToContact:ignoringIdentifiers:.cn_once_object_13
- _areAllAvailableKeysEqualToContact:ignoringIdentifiers:.cn_once_token_13
- _avatarRecipeDataDescription.cn_once_object_91
- _avatarRecipeDataDescription.cn_once_token_91
- _birthdayDescription.cn_once_object_43
- _birthdayDescription.cn_once_token_43
- _calendarURIsDescription.cn_once_object_72
- _calendarURIsDescription.cn_once_token_72
- _callAlertDescription.cn_once_object_80
- _callAlertDescription.cn_once_token_80
- _contactRelationsDescription.cn_once_object_67
- _contactRelationsDescription.cn_once_token_67
- _contactTypeDescription.cn_once_object_59
- _contactTypeDescription.cn_once_token_59
- _creationDateDescription.cn_once_object_45
- _creationDateDescription.cn_once_token_45
- _cropRectDescription.cn_once_object_49
- _cropRectDescription.cn_once_token_49
- _datesDescription.cn_once_object_65
- _datesDescription.cn_once_token_65
- _departmentDescription.cn_once_object_41
- _departmentDescription.cn_once_token_41
- _downtimeWhitelistDescription.cn_once_object_83
- _downtimeWhitelistDescription.cn_once_token_83
- _emailAddressesDescription.cn_once_object_63
- _emailAddressesDescription.cn_once_token_63
- _explicitDisplayNameDescription.cn_once_object_37
- _explicitDisplayNameDescription.cn_once_token_37
- _externalIdentifierDescription.cn_once_object_73
- _externalIdentifierDescription.cn_once_token_73
- _externalImageURIDescription.cn_once_object_77
- _externalImageURIDescription.cn_once_token_77
- _externalModificationTagDescription.cn_once_object_74
- _externalModificationTagDescription.cn_once_token_74
- _externalRepresentationDescription.cn_once_object_75
- _externalRepresentationDescription.cn_once_token_75
- _externalUUIDDescription.cn_once_object_76
- _externalUUIDDescription.cn_once_token_76
- _familyNameDescription.cn_once_object_27
- _familyNameDescription.cn_once_token_27
- _fullscreenImageDataDescription.cn_once_object_51
- _fullscreenImageDataDescription.cn_once_token_51
- _givenNameDescription.cn_once_object_25
- _givenNameDescription.cn_once_token_25
- _iOSLegacyIdentifierDescription.cn_once_object_23
- _iOSLegacyIdentifierDescription.cn_once_token_23
- _identifierDescription.cn_once_object_22
- _identifierDescription.cn_once_token_22
- _imageBackgroundColorsDataDescription.cn_once_object_92
- _imageBackgroundColorsDataDescription.cn_once_token_92
- _imageDataAvailableDescription.cn_once_object_53
- _imageDataAvailableDescription.cn_once_token_53
- _imageDataDescription.cn_once_object_48
- _imageDataDescription.cn_once_token_48
- _imageHash.cn_once_object_85
- _imageHash.cn_once_token_85
- _imageSyncFailedTimeDescription.cn_once_object_94
- _imageSyncFailedTimeDescription.cn_once_token_94
- _imageType.cn_once_object_84
- _imageType.cn_once_token_84
- _instantMessagAddressesDescription.cn_once_object_66
- _instantMessagAddressesDescription.cn_once_token_66
- _isUsingSharedPhotoDescription.cn_once_object_61
- _isUsingSharedPhotoDescription.cn_once_token_61
- _jobTitleDescription.cn_once_object_42
- _jobTitleDescription.cn_once_token_42
- _linkIdentifierDescription.cn_once_object_54
- _linkIdentifierDescription.cn_once_token_54
- _mapsDataDescription.cn_once_object_82
- _mapsDataDescription.cn_once_token_82
- _memojiMetadataDescription.cn_once_object_86
- _memojiMetadataDescription.cn_once_token_86
- _middleNameDescription.cn_once_object_26
- _middleNameDescription.cn_once_token_26
- _modificationDateDescription.cn_once_object_46
- _modificationDateDescription.cn_once_token_46
- _namePrefixDescription.cn_once_object_24
- _namePrefixDescription.cn_once_token_24
- _nameSuffixDescription.cn_once_object_28
- _nameSuffixDescription.cn_once_token_28
- _nicknameDescription.cn_once_object_30
- _nicknameDescription.cn_once_token_30
- _nonGregorianBirthdayDescription.cn_once_object_44
- _nonGregorianBirthdayDescription.cn_once_token_44
- _noteDescription.cn_once_object_47
- _noteDescription.cn_once_token_47
- _objc_msgSend$areAllPropertiesButContactIdentifierEqualToContact:
- _objc_msgSend$failedToReadRemoteFavorites:
- _objc_msgSend$failedToWriteRemoteFavorites:
- _organizationNameDescription.cn_once_object_40
- _organizationNameDescription.cn_once_token_40
- _phoneNumbersDescription.cn_once_object_62
- _phoneNumbersDescription.cn_once_token_62
- _phonemeDataDescription.cn_once_object_78
- _phonemeDataDescription.cn_once_token_78
- _phoneticFamilyNameDescription.cn_once_object_33
- _phoneticFamilyNameDescription.cn_once_token_33
- _phoneticGivenNameDescription.cn_once_object_31
- _phoneticGivenNameDescription.cn_once_token_31
- _phoneticMiddleNameDescription.cn_once_object_32
- _phoneticMiddleNameDescription.cn_once_token_32
- _phoneticOrganizationNameDescription.cn_once_object_34
- _phoneticOrganizationNameDescription.cn_once_token_34
- _postalAddressesDescription.cn_once_object_69
- _postalAddressesDescription.cn_once_token_69
- _preferredApplePersonaIdentifierDescription.cn_once_object_58
- _preferredApplePersonaIdentifierDescription.cn_once_token_58
- _preferredChannelDescription.cn_once_object_81
- _preferredChannelDescription.cn_once_token_81
- _preferredForImageDescription.cn_once_object_56
- _preferredForImageDescription.cn_once_token_56
- _preferredForNameDescription.cn_once_object_55
- _preferredForNameDescription.cn_once_token_55
- _preferredImageComparator.cn_once_object_14
- _preferredImageComparator.cn_once_token_14
- _preferredLikenessSourceDescription.cn_once_object_57
- _preferredLikenessSourceDescription.cn_once_token_57
- _previousFamilyNameDescription.cn_once_object_29
- _previousFamilyNameDescription.cn_once_token_29
- _pronunciationFamilyNameDescription.cn_once_object_36
- _pronunciationFamilyNameDescription.cn_once_token_36
- _pronunciationGivenNameDescription.cn_once_object_35
- _pronunciationGivenNameDescription.cn_once_token_35
- _sectionForSortingByFamilyNameDescription.cn_once_object_38
- _sectionForSortingByFamilyNameDescription.cn_once_token_38
- _sectionForSortingByGivenNameDescription.cn_once_object_39
- _sectionForSortingByGivenNameDescription.cn_once_token_39
- _sensitiveContentConfigurationDescription.cn_once_object_93
- _sensitiveContentConfigurationDescription.cn_once_token_93
- _sharedPhotoDisplayPreferenceDescription.cn_once_object_60
- _sharedPhotoDisplayPreferenceDescription.cn_once_token_60
- _socialProfilesDescription.cn_once_object_68
- _socialProfilesDescription.cn_once_token_68
- _syncImageDataDescription.cn_once_object_52
- _syncImageDataDescription.cn_once_token_52
- _textAlertDescription.cn_once_object_79
- _textAlertDescription.cn_once_token_79
- _thumbnailImageDataDescription.cn_once_object_50
- _thumbnailImageDataDescription.cn_once_token_50
- _urlAddressesDescription.cn_once_object_64
- _urlAddressesDescription.cn_once_token_64
- _wallpaperDescription.cn_once_object_87
- _wallpaperDescription.cn_once_token_87
- _wallpaperMetadataDescription.cn_once_object_88
- _wallpaperMetadataDescription.cn_once_token_88
- _wallpaperSyncFailedTimeDescription.cn_once_object_95
- _wallpaperSyncFailedTimeDescription.cn_once_token_95
- _wallpaperURIDescription.cn_once_object_90
- _wallpaperURIDescription.cn_once_token_90
- _watchWallpaperImageDataDescription.cn_once_object_89
- _watchWallpaperImageDataDescription.cn_once_token_89
CStrings:
+ "Failed to read remote favorites with contactsd, error: %@, willRetry: %d"
+ "Failed to save remote favorites with contactsd, error: %@ willRetry: %d"
+ "TB,N,V_wantsRetryAfterMessageFailure"
+ "_wantsRetryAfterMessageFailure"
+ "arePropertiesEqualToContact:ignoredProperties:"
+ "contactCardIgnorableContactChangeProperties"
+ "failedToReadRemoteFavorites:willRetry:"
+ "failedToWriteRemoteFavorites:willRetry:"
+ "isEquivalent:ignoringProperties:"
+ "setWantsRetryAfterMessageFailure:"
+ "wantsRetryAfterMessageFailure"
- "Failed to read remote favorites with contactsd, error: %@"
- "Failed to save remote favorites with contactsd, error: %@"
- "areAllPropertiesButContactIdentifierEqualToContact:"
- "failedToReadRemoteFavorites:"
- "failedToWriteRemoteFavorites:"

```
