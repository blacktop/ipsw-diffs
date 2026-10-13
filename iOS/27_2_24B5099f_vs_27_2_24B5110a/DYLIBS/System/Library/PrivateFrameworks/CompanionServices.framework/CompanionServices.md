## CompanionServices

> `/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices`

```diff

-524.10.109.0.1
-  __TEXT.__text: 0x55d5c
-  __TEXT.__objc_methlist: 0x16e4
-  __TEXT.__const: 0x8908
+524.11.6.0.0
+  __TEXT.__text: 0x57708
+  __TEXT.__objc_methlist: 0x1b9c
+  __TEXT.__const: 0x88d8
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__swift5_typeref: 0x19c3
-  __TEXT.__cstring: 0x24ff
+  __TEXT.__cstring: 0x261b
   __TEXT.__constg_swiftt: 0x1300
   __TEXT.__swift5_reflstr: 0x9d5
   __TEXT.__swift5_fieldmd: 0x1470

   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift_as_cont: 0x150
   __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__unwind_info: 0x23b8
+  __TEXT.__unwind_info: 0x2498
   __TEXT.__eh_frame: 0x2958
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x538
-  __DATA_CONST.__objc_classlist: 0x148
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xb80
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__got: 0x510
   __AUTH_CONST.__const: 0x4458
-  __AUTH_CONST.__cfstring: 0x14c0
-  __AUTH_CONST.__objc_const: 0x3738
+  __AUTH_CONST.__cfstring: 0x16c0
+  __AUTH_CONST.__objc_const: 0x4130
   __AUTH_CONST.__auth_got: 0xb70
-  __AUTH.__objc_data: 0xcd0
+  __AUTH.__objc_data: 0xeb0
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x178
-  __DATA.__data: 0x1b18
+  __DATA.__objc_ivar: 0x1c4
+  __DATA.__data: 0x1b78
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2581
-  Symbols:   2000
-  CStrings:  403
+  Functions: 2665
+  Symbols:   2170
+  CStrings:  420
 
Symbols:
+ +[CPSPhotosAppConfiguration defaultConfiguration]
+ +[CPSPhotosAppConfiguration supportsSecureCoding]
+ +[CPSPhotosAssetCollection supportsSecureCoding]
+ +[CPSPhotosConfigurationRequest supportsSecureCoding]
+ +[CPSPhotosConfigurationResponse supportsSecureCoding]
+ +[CPSPhotosMemoriesSlideshowsConfiguration activityConfiguration]
+ +[CPSPhotosMemoriesSlideshowsConfiguration collectionsConfigurationWithAssetCollections:]
+ +[CPSPhotosMemoriesSlideshowsConfiguration dailyMemoriesConfiguration]
+ +[CPSPhotosMemoriesSlideshowsConfiguration defaultConfiguration]
+ +[CPSPhotosMemoriesSlideshowsConfiguration favoriteMemoriesConfiguration]
+ +[CPSPhotosMemoriesSlideshowsConfiguration supportsSecureCoding]
+ +[CPSPhotosPortraitsConfiguration defaultConfiguration]
+ +[CPSPhotosPortraitsConfiguration supportsSecureCoding]
+ -[CPSPhotosAppConfiguration albumsTabEnabled]
+ -[CPSPhotosAppConfiguration configurationType]
+ -[CPSPhotosAppConfiguration copyWithZone:]
+ -[CPSPhotosAppConfiguration description]
+ -[CPSPhotosAppConfiguration encodeWithCoder:]
+ -[CPSPhotosAppConfiguration initWithCoder:]
+ -[CPSPhotosAppConfiguration init]
+ -[CPSPhotosAppConfiguration libraryTabEnabled]
+ -[CPSPhotosAppConfiguration memoriesTabEnabled]
+ -[CPSPhotosAppConfiguration setAlbumsTabEnabled:]
+ -[CPSPhotosAppConfiguration setLibraryTabEnabled:]
+ -[CPSPhotosAppConfiguration setMemoriesTabEnabled:]
+ -[CPSPhotosAppConfiguration setSharedAlbumsTabEnabled:]
+ -[CPSPhotosAppConfiguration setSharedLibraryFilter:]
+ -[CPSPhotosAppConfiguration sharedAlbumsTabEnabled]
+ -[CPSPhotosAppConfiguration sharedLibraryFilter]
+ -[CPSPhotosAssetCollection .cxx_destruct]
+ -[CPSPhotosAssetCollection cloudIdentifier]
+ -[CPSPhotosAssetCollection copyWithZone:]
+ -[CPSPhotosAssetCollection description]
+ -[CPSPhotosAssetCollection encodeWithCoder:]
+ -[CPSPhotosAssetCollection initWithCloudIdentifier:localizedTitle:sharedCollection:]
+ -[CPSPhotosAssetCollection initWithCoder:]
+ -[CPSPhotosAssetCollection isSharedCollection]
+ -[CPSPhotosAssetCollection localizedTitle]
+ -[CPSPhotosConfigurationRequest .cxx_destruct]
+ -[CPSPhotosConfigurationRequest authType]
+ -[CPSPhotosConfigurationRequest configuration]
+ -[CPSPhotosConfigurationRequest description]
+ -[CPSPhotosConfigurationRequest encodeWithCoder:]
+ -[CPSPhotosConfigurationRequest initWithAppConfiguration:]
+ -[CPSPhotosConfigurationRequest initWithCoder:]
+ -[CPSPhotosConfigurationRequest initWithConfiguration:]
+ -[CPSPhotosConfigurationResponse .cxx_destruct]
+ -[CPSPhotosConfigurationResponse appConfiguration]
+ -[CPSPhotosConfigurationResponse configuration]
+ -[CPSPhotosConfigurationResponse encodeWithCoder:]
+ -[CPSPhotosConfigurationResponse initWithCoder:]
+ -[CPSPhotosConfigurationResponse initWithConfiguration:]
+ -[CPSPhotosMemoriesSlideshowsConfiguration .cxx_destruct]
+ -[CPSPhotosMemoriesSlideshowsConfiguration assetCollections]
+ -[CPSPhotosMemoriesSlideshowsConfiguration configurationType]
+ -[CPSPhotosMemoriesSlideshowsConfiguration copyWithZone:]
+ -[CPSPhotosMemoriesSlideshowsConfiguration description]
+ -[CPSPhotosMemoriesSlideshowsConfiguration encodeWithCoder:]
+ -[CPSPhotosMemoriesSlideshowsConfiguration initWithActivity]
+ -[CPSPhotosMemoriesSlideshowsConfiguration initWithAssetCollections:]
+ -[CPSPhotosMemoriesSlideshowsConfiguration initWithCoder:]
+ -[CPSPhotosMemoriesSlideshowsConfiguration initWithDailyMemories]
+ -[CPSPhotosMemoriesSlideshowsConfiguration initWithFavoriteMemories]
+ -[CPSPhotosMemoriesSlideshowsConfiguration setSharedLibraryFilter:]
+ -[CPSPhotosMemoriesSlideshowsConfiguration sharedLibraryFilter]
+ -[CPSPhotosMemoriesSlideshowsConfiguration type]
+ -[CPSPhotosPortraitsConfiguration .cxx_destruct]
+ -[CPSPhotosPortraitsConfiguration assetCollections]
+ -[CPSPhotosPortraitsConfiguration configurationType]
+ -[CPSPhotosPortraitsConfiguration copyWithZone:]
+ -[CPSPhotosPortraitsConfiguration description]
+ -[CPSPhotosPortraitsConfiguration encodeWithCoder:]
+ -[CPSPhotosPortraitsConfiguration initWithAllCollections]
+ -[CPSPhotosPortraitsConfiguration initWithAssetCollections:]
+ -[CPSPhotosPortraitsConfiguration initWithCoder:]
+ -[CPSPhotosPortraitsConfiguration initWithSmartCategories:personIdentifiers:]
+ -[CPSPhotosPortraitsConfiguration personIdentifiers]
+ -[CPSPhotosPortraitsConfiguration setSharedLibraryFilter:]
+ -[CPSPhotosPortraitsConfiguration sharedLibraryFilter]
+ -[CPSPhotosPortraitsConfiguration smartCategories]
+ -[CPSPhotosPortraitsConfiguration type]
+ -[CPSViewServicePresentationContext photosConfigurationRequest]
+ -[CPSViewServicePresentationContext setPhotosConfigurationRequest:]
+ GCC_except_table306
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table320
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table329
+ GCC_except_table486
+ _CPSAllowedClassesForPhotosConfiguration
+ _OBJC_CLASS_$_CPSPhotosAppConfiguration
+ _OBJC_CLASS_$_CPSPhotosAssetCollection
+ _OBJC_CLASS_$_CPSPhotosConfigurationRequest
+ _OBJC_CLASS_$_CPSPhotosConfigurationResponse
+ _OBJC_CLASS_$_CPSPhotosMemoriesSlideshowsConfiguration
+ _OBJC_CLASS_$_CPSPhotosPortraitsConfiguration
+ _OBJC_IVAR_$_CPSPhotosAppConfiguration._albumsTabEnabled
+ _OBJC_IVAR_$_CPSPhotosAppConfiguration._libraryTabEnabled
+ _OBJC_IVAR_$_CPSPhotosAppConfiguration._memoriesTabEnabled
+ _OBJC_IVAR_$_CPSPhotosAppConfiguration._sharedAlbumsTabEnabled
+ _OBJC_IVAR_$_CPSPhotosAppConfiguration._sharedLibraryFilter
+ _OBJC_IVAR_$_CPSPhotosAssetCollection._cloudIdentifier
+ _OBJC_IVAR_$_CPSPhotosAssetCollection._localizedTitle
+ _OBJC_IVAR_$_CPSPhotosAssetCollection._sharedCollection
+ _OBJC_IVAR_$_CPSPhotosConfigurationRequest._configuration
+ _OBJC_IVAR_$_CPSPhotosConfigurationResponse._configuration
+ _OBJC_IVAR_$_CPSPhotosMemoriesSlideshowsConfiguration._assetCollections
+ _OBJC_IVAR_$_CPSPhotosMemoriesSlideshowsConfiguration._sharedLibraryFilter
+ _OBJC_IVAR_$_CPSPhotosMemoriesSlideshowsConfiguration._type
+ _OBJC_IVAR_$_CPSPhotosPortraitsConfiguration._assetCollections
+ _OBJC_IVAR_$_CPSPhotosPortraitsConfiguration._personIdentifiers
+ _OBJC_IVAR_$_CPSPhotosPortraitsConfiguration._sharedLibraryFilter
+ _OBJC_IVAR_$_CPSPhotosPortraitsConfiguration._smartCategories
+ _OBJC_IVAR_$_CPSPhotosPortraitsConfiguration._type
+ _OBJC_IVAR_$_CPSViewServicePresentationContext._photosConfigurationRequest
+ _OBJC_METACLASS_$_CPSPhotosAppConfiguration
+ _OBJC_METACLASS_$_CPSPhotosAssetCollection
+ _OBJC_METACLASS_$_CPSPhotosConfigurationRequest
+ _OBJC_METACLASS_$_CPSPhotosConfigurationResponse
+ _OBJC_METACLASS_$_CPSPhotosMemoriesSlideshowsConfiguration
+ _OBJC_METACLASS_$_CPSPhotosPortraitsConfiguration
+ __OBJC_$_CLASS_METHODS_CPSPhotosAppConfiguration
+ __OBJC_$_CLASS_METHODS_CPSPhotosAssetCollection
+ __OBJC_$_CLASS_METHODS_CPSPhotosConfigurationRequest
+ __OBJC_$_CLASS_METHODS_CPSPhotosConfigurationResponse
+ __OBJC_$_CLASS_METHODS_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_$_CLASS_METHODS_CPSPhotosPortraitsConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CPSPhotosAppConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CPSPhotosAssetCollection
+ __OBJC_$_CLASS_PROP_LIST_CPSPhotosConfigurationRequest
+ __OBJC_$_CLASS_PROP_LIST_CPSPhotosConfigurationResponse
+ __OBJC_$_CLASS_PROP_LIST_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CPSPhotosPortraitsConfiguration
+ __OBJC_$_INSTANCE_METHODS_CPSPhotosAppConfiguration
+ __OBJC_$_INSTANCE_METHODS_CPSPhotosAssetCollection
+ __OBJC_$_INSTANCE_METHODS_CPSPhotosConfigurationRequest
+ __OBJC_$_INSTANCE_METHODS_CPSPhotosConfigurationResponse
+ __OBJC_$_INSTANCE_METHODS_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_$_INSTANCE_METHODS_CPSPhotosPortraitsConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CPSPhotosAppConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CPSPhotosAssetCollection
+ __OBJC_$_INSTANCE_VARIABLES_CPSPhotosConfigurationRequest
+ __OBJC_$_INSTANCE_VARIABLES_CPSPhotosConfigurationResponse
+ __OBJC_$_INSTANCE_VARIABLES_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CPSPhotosPortraitsConfiguration
+ __OBJC_$_PROP_LIST_CPSPhotosAppConfiguration
+ __OBJC_$_PROP_LIST_CPSPhotosAssetCollection
+ __OBJC_$_PROP_LIST_CPSPhotosConfiguration
+ __OBJC_$_PROP_LIST_CPSPhotosConfigurationRequest
+ __OBJC_$_PROP_LIST_CPSPhotosConfigurationResponse
+ __OBJC_$_PROP_LIST_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_$_PROP_LIST_CPSPhotosPortraitsConfiguration
+ __OBJC_$_PROTOCOL_CLASS_METHODS_CPSPhotosConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPSPhotosConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPSPhotosConfiguration
+ __OBJC_$_PROTOCOL_REFS_CPSPhotosConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CPSPhotosAppConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CPSPhotosAssetCollection
+ __OBJC_CLASS_PROTOCOLS_$_CPSPhotosConfigurationRequest
+ __OBJC_CLASS_PROTOCOLS_$_CPSPhotosConfigurationResponse
+ __OBJC_CLASS_PROTOCOLS_$_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CPSPhotosPortraitsConfiguration
+ __OBJC_CLASS_RO_$_CPSPhotosAppConfiguration
+ __OBJC_CLASS_RO_$_CPSPhotosAssetCollection
+ __OBJC_CLASS_RO_$_CPSPhotosConfigurationRequest
+ __OBJC_CLASS_RO_$_CPSPhotosConfigurationResponse
+ __OBJC_CLASS_RO_$_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_CLASS_RO_$_CPSPhotosPortraitsConfiguration
+ __OBJC_LABEL_PROTOCOL_$_CPSPhotosConfiguration
+ __OBJC_METACLASS_RO_$_CPSPhotosAppConfiguration
+ __OBJC_METACLASS_RO_$_CPSPhotosAssetCollection
+ __OBJC_METACLASS_RO_$_CPSPhotosConfigurationRequest
+ __OBJC_METACLASS_RO_$_CPSPhotosConfigurationResponse
+ __OBJC_METACLASS_RO_$_CPSPhotosMemoriesSlideshowsConfiguration
+ __OBJC_METACLASS_RO_$_CPSPhotosPortraitsConfiguration
+ __OBJC_PROTOCOL_$_CPSPhotosConfiguration
- GCC_except_table224
- GCC_except_table225
- GCC_except_table227
- GCC_except_table229
- GCC_except_table231
- GCC_except_table236
- GCC_except_table238
- GCC_except_table240
- GCC_except_table241
- GCC_except_table247
- GCC_except_table402
CStrings:
+ "2"
+ "PhotosConfiguration"
+ "albumsTabEnabled"
+ "assetCollections"
+ "cloudIdentifier"
+ "configuration"
+ "configurationType"
+ "libraryTabEnabled"
+ "localizedTitle"
+ "memoriesTabEnabled"
+ "person.badge.waveform.fill"
+ "personIdentifiers"
+ "photosConfigurationRequest"
+ "sharedAlbumsTabEnabled"
+ "sharedCollection"
+ "sharedLibraryFilter"
+ "smartCategories"
+ "type"
- "recognize-my-voice-icon"
```
