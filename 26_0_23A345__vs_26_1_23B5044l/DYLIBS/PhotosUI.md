## PhotosUI

> `/System/Library/Frameworks/PhotosUI.framework/PhotosUI`

```diff

-802.43.254.0.0
-  __TEXT.__text: 0x26d9c
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x31b4
-  __TEXT.__const: 0x1910
-  __TEXT.__swift5_typeref: 0x44a
-  __TEXT.__swift5_fieldmd: 0x538
-  __TEXT.__constg_swiftt: 0x728
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x4ca
-  __TEXT.__swift5_assocty: 0x258
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0xf0
-  __TEXT.__swift5_types: 0x84
+810.40.105.0.0
+  __TEXT.__text: 0x286c8
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x3264
+  __TEXT.__const: 0x1b80
+  __TEXT.__swift5_typeref: 0x51e
+  __TEXT.__swift5_fieldmd: 0x590
+  __TEXT.__constg_swiftt: 0x6fc
+  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_reflstr: 0x54a
+  __TEXT.__swift5_assocty: 0x288
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_proto: 0x108
+  __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__cstring: 0x417f
+  __TEXT.__cstring: 0x41fe
   __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__oslogstring: 0xb34
-  __TEXT.__unwind_info: 0xdb8
-  __TEXT.__objc_classname: 0x76d
-  __TEXT.__objc_methname: 0x87b8
-  __TEXT.__objc_methtype: 0x1489
-  __TEXT.__objc_stubs: 0x5200
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__const: 0xba0
-  __DATA_CONST.__objc_classlist: 0x190
+  __TEXT.__oslogstring: 0xb76
+  __TEXT.__unwind_info: 0xe58
+  __TEXT.__objc_classname: 0x76f
+  __TEXT.__objc_methname: 0x8aeb
+  __TEXT.__objc_methtype: 0x1463
+  __TEXT.__objc_stubs: 0x5220
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0xbd8
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d20
+  __DATA_CONST.__objc_selrefs: 0x1d90
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x638
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x1f40
-  __AUTH_CONST.__objc_const: 0x5710
+  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__const: 0xae0
+  __AUTH_CONST.__cfstring: 0x2040
+  __AUTH_CONST.__objc_const: 0x57c8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x13b0
-  __AUTH.__data: 0x438
-  __DATA.__objc_ivar: 0x2b8
-  __DATA.__data: 0xfa0
+  __AUTH.__objc_data: 0x13d0
+  __AUTH.__data: 0x288
+  __DATA.__objc_ivar: 0x2e0
+  __DATA.__data: 0x1090
   __DATA.__common: 0x241
-  __DATA.__bss: 0x1ea0
+  __DATA.__bss: 0x21a0
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4F6E652B-273A-32FB-A48D-60B9C6B35597
-  Functions: 1783
-  Symbols:   3946
-  CStrings:  2287
+  UUID: 00C29F14-4ABF-38C8-9405-3F4089AFAD3D
+  Functions: 1842
+  Symbols:   4010
+  CStrings:  2327
 
Symbols:
+ -[PHPickerConfiguration _primaryButtonType]
+ -[PHPickerConfiguration _secondaryButtonType]
+ -[PHPickerConfiguration _setPrimaryButtonType:]
+ -[PHPickerConfiguration _setSecondaryButtonType:]
+ -[PHPickerConfiguration prompt]
+ -[PHPickerConfiguration setPrompt:]
+ -[PHPickerUpdateConfiguration _didSetPrimaryButtonType]
+ -[PHPickerUpdateConfiguration _didSetPrompt]
+ -[PHPickerUpdateConfiguration _didSetSecondaryButtonType]
+ -[PHPickerUpdateConfiguration _didSetSharedAlbumSheetConfiguration]
+ -[PHPickerUpdateConfiguration _primaryButtonType]
+ -[PHPickerUpdateConfiguration _secondaryButtonType]
+ -[PHPickerUpdateConfiguration _setPrimaryButtonType:]
+ -[PHPickerUpdateConfiguration _setSecondaryButtonType:]
+ -[PHPickerUpdateConfiguration _setSharedAlbumSheetConfiguration:]
+ -[PHPickerUpdateConfiguration prompt]
+ -[PHPickerUpdateConfiguration setPrompt:]
+ -[PHPickerViewController _finishPickingWithResults:action:error:]
+ -[PHPickerViewController _overrideSelectedItemsWithIdentifiers:]
+ -[PHPickerViewController _pickerDidFinishPicking:action:error:]
+ -[PHPickerViewController deselectItemsWithIdentifiers:]
+ -[PHPickerViewController moveItemWithIdentifier:afterItemWithIdentifier:]
+ -[PUPickerExtensionHostContext _pickerDidFinishPicking:action:error:]
+ -[PUPickerExtensionVendorContext _deselectItemsWithIdentifiers:]
+ -[PUPickerExtensionVendorContext _moveItemWithIdentifier:afterIdentifier:]
+ -[PUPickerExtensionVendorContext _overrideSelectedItemsWithIdentifiers:]
+ GCC_except_table464
+ GCC_except_table487
+ GCC_except_table808
+ GCC_except_table811
+ GCC_except_table813
+ GCC_except_table888
+ _OBJC_IVAR_$_PHPickerConfiguration.__primaryButtonType
+ _OBJC_IVAR_$_PHPickerConfiguration.__secondaryButtonType
+ _OBJC_IVAR_$_PHPickerConfiguration._prompt
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__didSetPrimaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__didSetPrompt
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__didSetSecondaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__didSetSharedAlbumSheetConfiguration
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__primaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration.__secondaryButtonType
+ _OBJC_IVAR_$_PHPickerUpdateConfiguration._prompt
+ __OBJC_$_INSTANCE_METHODS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage(PhotosUI)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PHPickerViewControllerDelegate_Private
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PHPickerViewControllerDelegate_Private
+ __OBJC_$_PROTOCOL_REFS_PHPickerViewControllerDelegate_Private
+ __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage(PhotosUI)
+ __OBJC_LABEL_PROTOCOL_$_PHPickerViewControllerDelegate_Private
+ __OBJC_PROTOCOL_$_PHPickerViewControllerDelegate_Private
+ ___44-[PHPickerViewController _popViewController]_block_invoke.822
+ ___64-[PUPickerExtensionVendorContext _deselectItemsWithIdentifiers:]_block_invoke
+ ___69-[PUPickerExtensionHostContext _pickerDidFinishPicking:action:error:]_block_invoke
+ ___72-[PUPickerExtensionVendorContext _overrideSelectedItemsWithIdentifiers:]_block_invoke
+ ___74-[PUPickerExtensionVendorContext _moveItemWithIdentifier:afterIdentifier:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1011
+ ___block_literal_global.1066
+ ___block_literal_global.1166
+ ___block_literal_global.1302
+ ___block_literal_global.1436
+ ___block_literal_global.15.1431
+ ___block_literal_global.742
+ ___block_literal_global.821
+ ___block_literal_global.865
+ ___block_literal_global.871
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy104_8
+ ___swift_memcpy32_8
+ ___swift_memcpy560_8
+ __extensionAuxiliaryHostProtocol.__interface.1432
+ __extensionAuxiliaryHostProtocol.interface.861
+ __extensionAuxiliaryHostProtocol.onceToken.1163
+ __extensionAuxiliaryHostProtocol.onceToken.1430
+ __extensionAuxiliaryHostProtocol.onceToken.860
+ __extensionAuxiliaryVendorProtocol.__interface.1437
+ __extensionAuxiliaryVendorProtocol.interface.866
+ __extensionAuxiliaryVendorProtocol.onceToken.1165
+ __extensionAuxiliaryVendorProtocol.onceToken.1435
+ __extensionAuxiliaryVendorProtocol.onceToken.864
+ _associated conformance 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLVyxGSHAASQ
+ _associated conformance So26_PHPickerPrimaryButtonTypeVSHSCSQ
+ _associated conformance So28_PHPickerSecondaryButtonTypeVSHSCSQ
+ _bzero
+ _get_enum_tag_for_layout_string SSSgSg
+ _get_enum_tag_for_layout_string So37_PHPickerShareAlbumSheetConfigurationCSgSg
+ _objc_msgSend$_deselectItemsWithIdentifiers:
+ _objc_msgSend$_finishPickingWithResults:action:error:
+ _objc_msgSend$_moveItemWithIdentifier:afterIdentifier:
+ _objc_msgSend$_overrideSelectedItemsWithIdentifiers:
+ _objc_msgSend$_pickerDidFinishPicking:action:error:
+ _objc_msgSend$_primaryButtonType
+ _objc_msgSend$_secondaryButtonType
+ _objc_msgSend$deselectItemsWithIdentifiers:
+ _objc_msgSend$moveItemWithIdentifier:afterItemWithIdentifier:
+ _objc_msgSend$px_mainScreen
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getAssociatedTypeWitness
+ _swift_getGenericMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic $s8PhotosUI38_PHPickerViewControllerPrivateDelegateP
+ _symbolic 8RawValueSYQz
+ _symbolic SSSgSg
+ _symbolic So37_PHPickerShareAlbumSheetConfigurationCSgSg
+ _symbolic _____ 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV
+ _symbolic _____ So26_PHPickerPrimaryButtonTypeV
+ _symbolic _____ So28_PHPickerSecondaryButtonTypeV
+ _symbolic _____Sg So26_PHPickerPrimaryButtonTypeV
+ _symbolic _____Sg So28_PHPickerSecondaryButtonTypeV
+ _symbolic ______pSgXw 8PhotosUI38_PHPickerViewControllerPrivateDelegateP
+ _symbolic _____y_____G 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV So20PHPickerCapabilitiesV
+ _symbolic _____y_____G 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV So21NSDirectionalRectEdgeV
+ _symbolic _____y_____G 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV So23_PHPickerCollectionTypeV
+ _symbolic _____y_____G 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV So28_PHPickerPrivateCapabilitiesV
+ _symbolic _____y_____G 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV So33_PHPickerCollectionSuggestionTypeV
+ _symbolic _____y_____GSg 8PhotosUI24HashableRawRepresentable33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLV So21NSDirectionalRectEdgeV
+ _type_layout_string So21NSDirectionalRectEdgeV
- -[PHPickerUpdateConfiguration set_sharedAlbumSheetConfiguration:]
- -[PHPickerViewController _finishPickingWithResults:error:]
- -[PHPickerViewController _pickerDidFinishPicking:error:]
- -[PHPickerViewController _pickerDidPerformCancelAction]
- -[PHPickerViewController _pickerDidPerformConfirmationAction]
- -[PHPickerViewController _updateSelectedAssetsWithIdentifiers:]
- -[PUPickerExtensionHostContext _pickerDidFinishPicking:error:]
- -[PUPickerExtensionHostContext _pickerDidPerformCancelAction]
- -[PUPickerExtensionHostContext _pickerDidPerformConfirmationAction]
- -[PUPickerExtensionVendorContext _deselectAssetsWithIdentifiers:]
- -[PUPickerExtensionVendorContext _moveAssetWithIdentifier:afterIdentifier:]
- -[PUPickerExtensionVendorContext _updateSelectedAssetsWithIdentifiers:]
- GCC_except_table468
- GCC_except_table491
- GCC_except_table788
- GCC_except_table801
- GCC_except_table803
- GCC_except_table876
- _OUTLINED_FUNCTION_46
- __DATA__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF49_PHPickerConfigurationStorageForNonEquatableTypes
- __INSTANCE_METHODS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage
- __IVARS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF49_PHPickerConfigurationStorageForNonEquatableTypes
- __METACLASS_DATA__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF49_PHPickerConfigurationStorageForNonEquatableTypes
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PHPickerViewControllerDelegate_Internal
- __OBJC_$_PROTOCOL_METHOD_TYPES_PHPickerViewControllerDelegate_Internal
- __OBJC_$_PROTOCOL_REFS_PHPickerViewControllerDelegate_Internal
- __OBJC_LABEL_PROTOCOL_$_PHPickerViewControllerDelegate_Internal
- __OBJC_PROTOCOL_$_PHPickerViewControllerDelegate_Internal
- __OBJC_PROTOCOL_REFERENCE_$_PHPickerViewControllerDelegate_Internal
- __PROTOCOLS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage
- __PROTOCOLS__TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF23_PHPickerOverlayStorage.100
- ___44-[PHPickerViewController _popViewController]_block_invoke.767
- ___61-[PUPickerExtensionHostContext _pickerDidPerformCancelAction]_block_invoke
- ___62-[PUPickerExtensionHostContext _pickerDidFinishPicking:error:]_block_invoke
- ___65-[PUPickerExtensionVendorContext _deselectAssetsWithIdentifiers:]_block_invoke
- ___67-[PUPickerExtensionHostContext _pickerDidPerformConfirmationAction]_block_invoke
- ___71-[PUPickerExtensionVendorContext _updateSelectedAssetsWithIdentifiers:]_block_invoke
- ___75-[PUPickerExtensionVendorContext _moveAssetWithIdentifier:afterIdentifier:]_block_invoke
- ___block_literal_global.1012
- ___block_literal_global.1067
- ___block_literal_global.1167
- ___block_literal_global.1303
- ___block_literal_global.1447
- ___block_literal_global.15.1442
- ___block_literal_global.689
- ___block_literal_global.766
- ___block_literal_global.852
- ___block_literal_global.866
- ___swift_memcpy392_8
- ___swift_memcpy56_8
- __extensionAuxiliaryHostProtocol.__interface.1443
- __extensionAuxiliaryHostProtocol.interface.862
- __extensionAuxiliaryHostProtocol.onceToken.1164
- __extensionAuxiliaryHostProtocol.onceToken.1441
- __extensionAuxiliaryHostProtocol.onceToken.861
- __extensionAuxiliaryVendorProtocol.__interface.1448
- __extensionAuxiliaryVendorProtocol.interface.867
- __extensionAuxiliaryVendorProtocol.onceToken.1166
- __extensionAuxiliaryVendorProtocol.onceToken.1446
- __extensionAuxiliaryVendorProtocol.onceToken.865
- _associated conformance 8PhotosUI49_PHPickerConfigurationStorageForNonEquatableTypes33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLCSHAASQ
- _objc_msgSend$_deselectAssetsWithIdentifiers:
- _objc_msgSend$_finishPickingWithResults:error:
- _objc_msgSend$_moveAssetWithIdentifier:afterIdentifier:
- _objc_msgSend$_pickerDidFinishPicking:error:
- _objc_msgSend$_pickerDidPerformCancelAction
- _objc_msgSend$_pickerDidPerformConfirmationAction
- _objc_msgSend$_updateSelectedAssetsWithIdentifiers:
- _objc_msgSend$deselectAssetsWithIdentifiers:
- _objc_msgSend$moveAssetWithIdentifier:afterAssetWithIdentifier:
- _symbolic So37_PHPickerShareAlbumSheetConfigurationCSg
- _symbolic _____ 8PhotosUI49_PHPickerConfigurationStorageForNonEquatableTypes33_E2E20DF4EAC1FCE07E5336962A6E0BEFLLC
- _symbolic _____Sg So21NSDirectionalRectEdgeV
- _type_layout_string So33_PHPickerCollectionSuggestionTypeV
CStrings:
+ "-[PHPickerViewController _finishPickingWithResults:action:error:]"
+ "-[PHPickerViewController _overrideSelectedItemsWithIdentifiers:]"
+ "-[PHPickerViewController _pickerDidFinishPicking:action:error:]"
+ "-[PHPickerViewController deselectItemsWithIdentifiers:]"
+ "-[PHPickerViewController moveItemWithIdentifier:afterItemWithIdentifier:]"
+ "PHPickerConfigurationCoderDesiredCollectionSuggestionsKey"
+ "PHPickerConfigurationCoderPrimaryButtonTypeKey"
+ "PHPickerConfigurationCoderPromptKey"
+ "PHPickerConfigurationCoderSecondaryButtonTypeKey"
+ "PHPickerUpdateConfigurationCoderDidSetPrimaryButtonTypeKey"
+ "PHPickerUpdateConfigurationCoderDidSetPromptKey"
+ "PHPickerUpdateConfigurationCoderDidSetSecondaryButtonTypeKey"
+ "PHPickerUpdateConfigurationCoderDidSetSharedAlbumSheetConfigurationKey"
+ "PHPickerUpdateConfigurationCoderPrimaryButtonTypeKey"
+ "PHPickerUpdateConfigurationCoderPromptKey"
+ "PHPickerUpdateConfigurationCoderSecondaryButtonTypeKey"
+ "PHPickerViewControllerDelegate_Private"
+ "Q5V"
+ "T@\"NSString\",C,N,V_prompt"
+ "T@\"_PHPickerShareAlbumSheetConfiguration\",C,N,S_setSharedAlbumSheetConfiguration:,V__sharedAlbumSheetConfiguration"
+ "TB,R,N,V__didSetPrimaryButtonType"
+ "TB,R,N,V__didSetPrompt"
+ "TB,R,N,V__didSetSecondaryButtonType"
+ "TB,R,N,V__didSetSharedAlbumSheetConfiguration"
+ "Tq,N,S_setPrimaryButtonType:,V__primaryButtonType"
+ "Tq,N,S_setSecondaryButtonType:,V__secondaryButtonType"
+ "__didSetPrimaryButtonType"
+ "__didSetPrompt"
+ "__didSetSecondaryButtonType"
+ "__didSetSharedAlbumSheetConfiguration"
+ "__primaryButtonType"
+ "__secondaryButtonType"
+ "_deselectItemsWithIdentifiers:"
+ "_didSetPrimaryButtonType"
+ "_didSetPrompt"
+ "_didSetSecondaryButtonType"
+ "_didSetSharedAlbumSheetConfiguration"
+ "_finishPickingWithResults:action:error:"
+ "_moveItemWithIdentifier:afterIdentifier:"
+ "_overrideSelectedItemsWithIdentifiers:"
+ "_pickerDidFinishPicking:action:error:"
+ "_primaryButtonType"
+ "_prompt"
+ "_secondaryButtonType"
+ "_setPrimaryButtonType:"
+ "_setSecondaryButtonType:"
+ "_setSharedAlbumSheetConfiguration:"
+ "configuration._primaryButtonType >= 0"
+ "configuration._secondaryButtonType >= 0"
+ "deselectItemsWithIdentifiers:"
+ "moveItemWithIdentifier:afterItemWithIdentifier:"
+ "primary button type is negative"
+ "privateDelegate"
+ "prompt"
+ "px_mainScreen"
+ "secondary button type is negative"
+ "setPrompt:"
+ "v24@0:8@\"PHPickerViewController\"16"
+ "v40@0:8@\"NSArray\"16q24@\"NSError\"32"
- "-[PHPickerViewController _finishPickingWithResults:error:]"
- "-[PHPickerViewController _pickerDidFinishPicking:error:]"
- "-[PHPickerViewController _pickerDidPerformCancelAction]"
- "-[PHPickerViewController _pickerDidPerformConfirmationAction]"
- "-[PHPickerViewController _updateSelectedAssetsWithIdentifiers:]"
- "-[PHPickerViewController deselectAssetsWithIdentifiers:]"
- "-[PHPickerViewController moveAssetWithIdentifier:afterAssetWithIdentifier:]"
- "PHPickerCollectionConfigurationCoderAllowsEditingCollectionKey"
- "PHPickerCollectionConfigurationCoderPurposeKey"
- "PHPickerConfigurationCoderdesiredCollectionSuggestionsKey"
- "PHPickerViewControllerDelegate_Internal"
- "Q55"
- "T@\"_PHPickerShareAlbumSheetConfiguration\",C,N,V__sharedAlbumSheetConfiguration"
- "_TtC8PhotosUIP33_E2E20DF4EAC1FCE07E5336962A6E0BEF49_PHPickerConfigurationStorageForNonEquatableTypes"
- "_finishPickingWithResults:error:"
- "_pickerDidFinishPicking:error:"
- "_pickerDidPerformCancelAction"
- "_pickerDidPerformConfirmationAction"
- "_updateSelectedAssetsWithIdentifiers:"
- "v32@0:8@\"NSArray\"16@\"NSError\"24"
- "v40@0:8@\"PHPickerViewController\"16@\"NSArray\"24@\"NSError\"32"
- "v40@0:8@16@24@32"

```
