## PhotosUI

> `/System/Library/Frameworks/PhotosUI.framework/PhotosUI`

```diff

-920.7.110.0.0
-  __TEXT.__text: 0x44a74
-  __TEXT.__objc_methlist: 0x4074
-  __TEXT.__const: 0x30d8
-  __TEXT.__constg_swiftt: 0xe04
-  __TEXT.__swift5_typeref: 0xd1a
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0xbe6
-  __TEXT.__swift5_fieldmd: 0xcc0
-  __TEXT.__swift5_assocty: 0x348
-  __TEXT.__swift5_proto: 0x1a0
-  __TEXT.__swift5_types: 0x128
-  __TEXT.__cstring: 0x4e17
+920.12.210.0.0
+  __TEXT.__text: 0x471b4
+  __TEXT.__objc_methlist: 0x41c4
+  __TEXT.__const: 0x2fa8
+  __TEXT.__constg_swiftt: 0xe5c
+  __TEXT.__swift5_typeref: 0xd66
+  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__swift5_reflstr: 0xce6
+  __TEXT.__swift5_fieldmd: 0xd60
+  __TEXT.__swift5_assocty: 0x300
+  __TEXT.__swift5_proto: 0x184
+  __TEXT.__swift5_types: 0x124
+  __TEXT.__cstring: 0x508d
   __TEXT.__oslogstring: 0x1665
-  __TEXT.__swift5_capture: 0x5a0
-  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift5_capture: 0x608
+  __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__swift_as_cont: 0x3c
+  __TEXT.__swift_as_cont: 0x40
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__unwind_info: 0x2210
-  __TEXT.__eh_frame: 0x8b4
+  __TEXT.__unwind_info: 0x2350
+  __TEXT.__eh_frame: 0x974
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd70
-  __DATA_CONST.__objc_classlist: 0x238
+  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2260
-  __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x22f0
+  __DATA_CONST.__objc_protorefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x680
-  __AUTH_CONST.__const: 0x2358
-  __AUTH_CONST.__cfstring: 0x2340
-  __AUTH_CONST.__objc_const: 0x7400
+  __DATA_CONST.__got: 0x688
+  __AUTH_CONST.__const: 0x24b0
+  __AUTH_CONST.__cfstring: 0x2380
+  __AUTH_CONST.__objc_const: 0x75f8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH.__objc_data: 0x2110
-  __AUTH.__data: 0x818
-  __DATA.__objc_ivar: 0x348
-  __DATA.__data: 0x1d80
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH.__objc_data: 0x2200
+  __AUTH.__data: 0x808
+  __DATA.__objc_ivar: 0x350
+  __DATA.__data: 0x1d70
   __DATA.__common: 0x241
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3102
-  Symbols:   3051
-  CStrings:  578
+  Functions: 3254
+  Symbols:   3102
+  CStrings:  599
 
Symbols:
+ +[PHPickerAspectRatio deviceAspectRatio]
+ +[PHPickerAspectRatio supportsSecureCoding]
+ +[PHPickerFilter landscapeAspectRatioFilter]
+ -[PHPickerAspectRatio _aspectRatio]
+ -[PHPickerAspectRatio _initWithAspectRatio:]
+ -[PHPickerAspectRatio copyWithZone:]
+ -[PHPickerAspectRatio encodeWithCoder:]
+ -[PHPickerAspectRatio hash]
+ -[PHPickerAspectRatio initWithAspectRatio:]
+ -[PHPickerAspectRatio initWithCoder:]
+ -[PHPickerAspectRatio init]
+ -[PHPickerAspectRatio isEqual:]
+ -[PHPickerConfiguration aspectRatio]
+ -[PHPickerConfiguration containerIdentifier]
+ -[PHPickerConfiguration primaryButtonType]
+ -[PHPickerConfiguration secondaryButtonType]
+ -[PHPickerConfiguration setAspectRatio:]
+ -[PHPickerConfiguration setContainerIdentifier:]
+ -[PHPickerConfiguration setPrimaryButtonType:]
+ -[PHPickerConfiguration setSecondaryButtonType:]
+ -[PHPickerResult requestThumbnailImageURLForPreferredSize:resultHandler:]
+ -[PHPickerSearchText prefersAutomaticFocus]
+ -[PHPickerSearchText setPrefersAutomaticFocus:]
+ -[PHPickerUpdateConfiguration containerIdentifier]
+ -[PHPickerUpdateConfiguration primaryButtonType]
+ -[PHPickerUpdateConfiguration secondaryButtonType]
+ -[PHPickerUpdateConfiguration setContainerIdentifier:]
+ -[PHPickerUpdateConfiguration setPrimaryButtonType:]
+ -[PHPickerUpdateConfiguration setSecondaryButtonType:]
+ GCC_except_table518
+ GCC_except_table528
+ GCC_except_table531
+ GCC_except_table533
+ GCC_except_table700
+ GCC_except_table791
+ GCC_except_table796
+ GCC_except_table800
+ GCC_except_table804
+ GCC_except_table981
+ _OBJC_CLASS_$_PHPickerAspectRatio
+ _OBJC_IVAR_$_PHPickerAspectRatio.__aspectRatio
+ _OBJC_IVAR_$_PHPickerConfiguration._aspectRatio
+ _OBJC_IVAR_$_PHPickerConfiguration._containerIdentifier
+ _OBJC_IVAR_$_PHPickerConfiguration._primaryButtonType
+ _OBJC_IVAR_$_PHPickerConfiguration._secondaryButtonType
+ _OBJC_IVAR_$_PHPickerSearchText._prefersAutomaticFocus
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration._containerIdentifier
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration._primaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration._secondaryButtonType
+ _OBJC_METACLASS_$_PHPickerAspectRatio
+ _OUTLINED_FUNCTION_100
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
+ _PHPhotosUIErrorDomain
+ __INSTANCE_METHODS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage
+ __OBJC_$_CLASS_METHODS_PHPickerAspectRatio
+ __OBJC_$_CLASS_PROP_LIST_PHPickerAspectRatio
+ __OBJC_$_INSTANCE_METHODS_PHPickerAspectRatio
+ __OBJC_$_INSTANCE_VARIABLES_PHPickerAspectRatio
+ __OBJC_$_PROP_LIST_PHPickerAspectRatio
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PHPickerViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PHPickerAspectRatio
+ __OBJC_CLASS_RO_$_PHPickerAspectRatio
+ __OBJC_METACLASS_RO_$_PHPickerAspectRatio
+ __PROTOCOLS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage
+ ___73-[PHPickerResult requestThumbnailImageURLForPreferredSize:resultHandler:]_block_invoke
+ ___swift_memcpy137_8
+ ___swift_memcpy608_8
+ __swiftEmptyDictionarySingleton
+ _associated conformance 8PhotosUI19PHPickerAspectRatioVSHAASQ
+ _dynamic_cast_existential_1_conditional
+ _swift_conformsToProtocol2
+ _symbolic SiSgSg
+ _symbolic So19PHPickerAspectRatioC
+ _symbolic _____ 8PhotosUI19PHPickerAspectRatioV
+ _symbolic _____ 8PhotosUI23_PHPickerOverlayStorage33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLC15PrivateDelegateV
+ _symbolic _____Sg 8PhotosUI23_PHPickerOverlayStorage33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLC15PrivateDelegateV
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySS_SSSgtG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic ySo22PHPickerViewControllerCScMYcc
+ _symbolic yXlSgXw
+ _type_layout_string 8PhotosUI19PHPickerAspectRatioV
+ _type_layout_string 8PhotosUI23_PHPickerOverlayStorage33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLC15PrivateDelegateV
- +[_PHPickerAspectRatio supportsSecureCoding]
- -[_PHPickerAspectRatio encodeWithCoder:]
- -[_PHPickerAspectRatio initWithCoder:]
- GCC_except_table492
- GCC_except_table502
- GCC_except_table505
- GCC_except_table507
- GCC_except_table674
- GCC_except_table765
- GCC_except_table770
- GCC_except_table774
- GCC_except_table778
- GCC_except_table955
- _OBJC_IVAR_$_PHPickerConfiguration.__aspectRatio
- _OBJC_IVAR_$_PHPickerConfiguration.__containerIdentifier
- _OBJC_IVAR_$_PHPickerConfiguration.__primaryButtonType
- _OBJC_IVAR_$_PHPickerConfiguration.__secondaryButtonType
- _OBJC_IVAR_$_PHPickerUpdateConfiguration.__containerIdentifier
- _OBJC_IVAR_$_PHPickerUpdateConfiguration.__primaryButtonType
- _OBJC_IVAR_$_PHPickerUpdateConfiguration.__secondaryButtonType
- _PHLocalIdentifiersErrorKey
- __OBJC_$_INSTANCE_METHODS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage(PhotosUI)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PHPickerViewControllerDelegate_Private
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PHPickerViewControllerDelegate_Private
- __OBJC_$_PROTOCOL_METHOD_TYPES_PHPickerViewControllerDelegate_Private
- __OBJC_$_PROTOCOL_REFS_PHPickerViewControllerDelegate_Private
- __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage(PhotosUI)
- __OBJC_LABEL_PROTOCOL_$_PHPickerViewControllerDelegate_Private
- __OBJC_PROTOCOL_$_PHPickerViewControllerDelegate_Private
- ___74-[PHPickerResult _requestThumbnailImageURLForPreferredSize:resultHandler:]_block_invoke
- ___swift_memcpy144_8
- ___swift_memcpy632_8
- _associated conformance 8PhotosUI8PVSErrorO18SanitizedErrorCodeOSHAASQ
- _associated conformance So26_PHPickerPrimaryButtonTypeVSHSCSQ
- _associated conformance So28_PHPickerSecondaryButtonTypeVSHSCSQ
- _symbolic _____ 8PhotosUI8PVSErrorO18SanitizedErrorCodeO
- _symbolic _____ So26_PHPickerPrimaryButtonTypeV
- _symbolic _____ So28_PHPickerSecondaryButtonTypeV
- _symbolic _____Sg So26_PHPickerPrimaryButtonTypeV
- _symbolic _____Sg So28_PHPickerSecondaryButtonTypeV
- _symbolic _____ySSypG s17_NativeDictionaryV
CStrings:
+ "-[PHPickerAspectRatio initWithAspectRatio:]"
+ "-[PHPickerAspectRatio init]"
+ "-[PHPickerAspectRatio isEqual:]"
+ "-[PHPickerResult requestThumbnailImageURLForPreferredSize:resultHandler:]"
+ "PHOTOSUI_ERROR_ASSET_COLLECTION_CREATION_FAILED"
+ "PHOTOSUI_ERROR_ASSET_COLLECTION_NOT_FOUND"
+ "PHOTOSUI_ERROR_ASSET_COLLECTION_NOT_WRITABLE"
+ "PHOTOSUI_ERROR_ICLOUD_PHOTOS_NOT_ENABLED"
+ "PHOTOSUI_ERROR_SHARED_ALBUM_MIGRATION_IN_PROGRESS"
+ "PHPhotosUIErrorDomain"
+ "PHPickerSearchTextPrefersAutomaticFocusKey"
+ "S\""
+ "aA(3"
+ "collectionCreationFailed"
+ "collectionIsMigrating("
+ "collectionNotFound("
+ "collectionNotWritable("
+ "com.apple.PhotosUIPrivate"
+ "configuration.primaryButtonType >= 0"
+ "configuration.secondaryButtonType >= 0"
+ "iCloudPhotosNotEnabled"
+ "nilAssetCollectionType"
+ "nilPhotoKitObject("
+ "presenting the scene failed: "
+ "unavailableSystemPhotoLibrary"
+ "unknownAssetCollectionType"
+ "unsupportedPlatform"
- "-[PHPickerResult _requestThumbnailImageURLForPreferredSize:resultHandler:]"
- "QEg"
- "The target shared album is currently migrating. Operation not allowed."
- "User does not have permission to add content to the shared album with identifier: "
- "configuration._primaryButtonType >= 0"
- "configuration._secondaryButtonType >= 0"
```
