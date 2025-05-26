## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3624.2.0.0.0
-  __TEXT.__text: 0x17cdfc
+3630.0.0.0.0
+  __TEXT.__text: 0x17f19c
   __TEXT.__auth_stubs: 0x2e70
-  __TEXT.__objc_methlist: 0x15484
+  __TEXT.__objc_methlist: 0x157dc
   __TEXT.__const: 0x1140
-  __TEXT.__gcc_except_tab: 0x2690
-  __TEXT.__cstring: 0xcf8a
-  __TEXT.__oslogstring: 0x6491
+  __TEXT.__gcc_except_tab: 0x26b8
+  __TEXT.__cstring: 0xd04a
+  __TEXT.__oslogstring: 0x65f7
   __TEXT.__dlopen_cstrs: 0x33e
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xcec

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x344
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x797c
+  __TEXT.__unwind_info: 0x7a44
   __TEXT.__eh_frame: 0x1c88
-  __TEXT.__objc_classname: 0x37ea
-  __TEXT.__objc_methname: 0x24abd
-  __TEXT.__objc_methtype: 0x4513
-  __TEXT.__objc_stubs: 0x1a700
-  __DATA_CONST.__got: 0xd40
-  __DATA_CONST.__const: 0x59c0
-  __DATA_CONST.__objc_classlist: 0xe60
+  __TEXT.__objc_classname: 0x386e
+  __TEXT.__objc_methname: 0x2507f
+  __TEXT.__objc_methtype: 0x4558
+  __TEXT.__objc_stubs: 0x1aa20
+  __DATA_CONST.__got: 0xd58
+  __DATA_CONST.__const: 0x5a30
+  __DATA_CONST.__objc_classlist: 0xe80
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c070
-  __DATA_CONST.__objc_selrefs: 0x8110
+  __DATA_CONST.__objc_const: 0x1c498
+  __DATA_CONST.__objc_selrefs: 0x8208
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__cfstring: 0xc9e0
-  __AUTH_CONST.__const: 0x60b0
-  __AUTH_CONST.__objc_const: 0xbcc8
+  __AUTH_CONST.__cfstring: 0xcac0
+  __AUTH_CONST.__const: 0x6170
+  __AUTH_CONST.__objc_const: 0xbe78
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__auth_ptr: 0x88
   __AUTH_CONST.__auth_got: 0x1748
   __AUTH.__data: 0x5e8
-  __AUTH.__objc_data: 0x4a88
+  __AUTH.__objc_data: 0x4bc8
   __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x1118
-  __DATA.__objc_superrefs: 0x848
-  __DATA.__objc_ivar: 0xf74
+  __DATA.__objc_classrefs: 0x1138
+  __DATA.__objc_superrefs: 0x858
+  __DATA.__objc_ivar: 0xf9c
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x2bc8
-  __DATA.__bss: 0x20e0
+  __DATA.__data: 0x2bb8
+  __DATA.__bss: 0x2130
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x4f10
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10663
-  Symbols:   30707
-  CStrings:  9519
+  Functions: 10745
+  Symbols:   30962
+  CStrings:  9590
 
Symbols:
+ +[CN(MultiValueTransforms) sensitiveContentConfigurationFromDataTransform]
+ +[CN(PropertyDescription) sensitiveContentConfigurationDescription]
+ +[CN(PropertyDescription) wallpaperURIDescription]
+ +[CN(UnifiedContacts) _unifyContacts:options:]
+ +[CN(UnifiedContacts) contactUnifyingContacts:options:]
+ +[CN(UnifiedContacts) unifyMultivalues:forProperty:options:]
+ +[CNCalculatesContactDiff clearWallpaperURIInUpdates:forContact:]
+ +[CNContactUnificationOptions sharedInstance]
+ +[CNSensitiveContentConfiguration configurationWithOverride:]
+ +[CNSensitiveContentConfiguration log]
+ +[CNSensitiveContentConfiguration supportsSecureCoding]
+ +[CNSharedProfileStateOracle shouldSaveCurrentPoster:toRecentsForContact:]
+ +[CNUnifiedContacts _unifyContactsSortedByPreference:options:]
+ +[CNUnifiedContacts unifyMultiValuesOfContacts:intoContact:availableKeyDescriptor:options:]
+ +[CNUnifiedContacts unifyMultivalues:forProperty:options:]
+ -[CNContact sensitiveContentConfiguration]
+ -[CNContact wallpaperURI]
+ -[CNContactFetchRequest alwaysUnifyLabeledValues]
+ -[CNContactFetchRequest contactBatchCount]
+ -[CNContactFetchRequest setAlwaysUnifyLabeledValues:]
+ -[CNContactFetchRequest setContactBatchCount:]
+ -[CNContactPoster contentIsSensitive]
+ -[CNContactPoster setContentIsSensitive:]
+ -[CNContactUnificationOptions copyWithZone:]
+ -[CNContactUnificationOptions initWithContactFetchRequest:]
+ -[CNContactUnificationOptions init]
+ -[CNContactUnificationOptions labeledValueUnificationThreshold]
+ -[CNContactUnificationOptions setLabeledValueUnificationThreshold:]
+ -[CNContactUnificationOptions setShouldFreezeMutableContacts:]
+ -[CNContactUnificationOptions setShouldIncludeMainStoreContacts:]
+ -[CNContactUnificationOptions shouldFreezeMutableContacts]
+ -[CNContactUnificationOptions shouldIncludeMainStoreContacts]
+ -[CNContactVCardWritingAdapter sensitiveContentConfiguration]
+ -[CNMutableContact _setSensitiveContentConfiguration:]
+ -[CNMutableContact _setWallpaperURI:]
+ -[CNMutableContact sensitiveContentConfiguration]
+ -[CNMutableContact setSensitiveContentConfiguration:]
+ -[CNMutableContact setWallpaperURI:]
+ -[CNMutableContact wallpaperURI]
+ -[CNSensitiveContentConfiguration copyWithZone:]
+ -[CNSensitiveContentConfiguration dataRepresentation]
+ -[CNSensitiveContentConfiguration encodeWithCoder:]
+ -[CNSensitiveContentConfiguration hash]
+ -[CNSensitiveContentConfiguration initWithCoder:]
+ -[CNSensitiveContentConfiguration initWithCoder:].cold.1
+ -[CNSensitiveContentConfiguration initWithDataRepresentation:]
+ -[CNSensitiveContentConfiguration initWithSensitiveContentOverride:]
+ -[CNSensitiveContentConfiguration isEqual:]
+ -[CNSensitiveContentConfiguration override]
+ -[CNSensitiveContentConfiguration setOverride:]
+ -[CNSensitiveContentConfiguration updatedWithOverride:]
+ -[CNSensitiveContentConfigurationDescription CNValueForContact:]
+ -[CNSensitiveContentConfigurationDescription decodeUsingCoder:contact:]
+ -[CNSensitiveContentConfigurationDescription encodeUsingCoder:contact:]
+ -[CNSensitiveContentConfigurationDescription init]
+ -[CNSensitiveContentConfigurationDescription isEqualForContact:other:]
+ -[CNSensitiveContentConfigurationDescription setCNValue:onContact:]
+ -[CNSensitiveContentConfigurationDescription valueClass]
+ -[CNSensitiveContentConfigurationDescription(iOSAB) ABValueFromCNValue:]
+ -[CNSensitiveContentConfigurationDescription(iOSAB) CNValueFromABValue:]
+ -[CNSensitiveContentConfigurationDescription(iOSAB) abPropertyID:]
+ -[CNSensitiveContentConfigurationDescription(iOSBuffers) CNValueFromABBytes:length:]
+ -[CNWallpaperURIDescription CNValueForContact:]
+ -[CNWallpaperURIDescription decodeUsingCoder:contact:]
+ -[CNWallpaperURIDescription encodeUsingCoder:contact:]
+ -[CNWallpaperURIDescription init]
+ -[CNWallpaperURIDescription isEqualForContact:other:]
+ -[CNWallpaperURIDescription resetGuardianManagedValueOnContact:]
+ -[CNWallpaperURIDescription setCNValue:onContact:]
+ -[CNWallpaperURIDescription(iOSAB) abPropertyID:]
+ -[CNiOSABContactBuffersDecoder initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:]
+ -[CNiOSABContactBuffersDecoder unificationOptions]
+ GCC_except_table114
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table145
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table201
+ GCC_except_table211
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table221
+ GCC_except_table230
+ GCC_except_table56
+ GCC_except_table68
+ GCC_except_table74
+ GCC_except_table75
+ _CNContactFetchRequestAPIMisuseExceptionName
+ _CNContactPosterAttributeNameContentIsSensitive
+ _CNContactSensitiveContentConfigurationKey
+ _CNContactWallpaperURIKey
+ _CNIsArrayNonEmpty
+ _OBJC_CLASS_$_CNContactUnificationOptions
+ _OBJC_CLASS_$_CNSensitiveContentConfiguration
+ _OBJC_CLASS_$_CNSensitiveContentConfigurationDescription
+ _OBJC_CLASS_$_CNWallpaperURIDescription
+ _OBJC_IVAR_$_CNContact._sensitiveContentConfiguration
+ _OBJC_IVAR_$_CNContact._wallpaperURI
+ _OBJC_IVAR_$_CNContactFetchRequest._alwaysUnifyLabeledValues
+ _OBJC_IVAR_$_CNContactFetchRequest._contactBatchCount
+ _OBJC_IVAR_$_CNContactPoster._contentIsSensitive
+ _OBJC_IVAR_$_CNContactUnificationOptions._labeledValueUnificationThreshold
+ _OBJC_IVAR_$_CNContactUnificationOptions._shouldFreezeMutableContacts
+ _OBJC_IVAR_$_CNContactUnificationOptions._shouldIncludeMainStoreContacts
+ _OBJC_IVAR_$_CNSensitiveContentConfiguration._override
+ _OBJC_IVAR_$_CNiOSABContactBuffersDecoder._unificationOptions
+ _OBJC_METACLASS_$_CNContactUnificationOptions
+ _OBJC_METACLASS_$_CNSensitiveContentConfiguration
+ _OBJC_METACLASS_$_CNSensitiveContentConfigurationDescription
+ _OBJC_METACLASS_$_CNWallpaperURIDescription
+ __OBJC_$_CLASS_METHODS_CNContactUnificationOptions
+ __OBJC_$_CLASS_METHODS_CNSensitiveContentConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CNContactUnificationOptions
+ __OBJC_$_CLASS_PROP_LIST_CNSensitiveContentConfiguration
+ __OBJC_$_INSTANCE_METHODS_CNContactUnificationOptions
+ __OBJC_$_INSTANCE_METHODS_CNSensitiveContentConfiguration
+ __OBJC_$_INSTANCE_METHODS_CNSensitiveContentConfigurationDescription(iOSBuffers|iOSAB)
+ __OBJC_$_INSTANCE_METHODS_CNWallpaperURIDescription(iOSAB)
+ __OBJC_$_INSTANCE_VARIABLES_CNContactUnificationOptions
+ __OBJC_$_INSTANCE_VARIABLES_CNSensitiveContentConfiguration
+ __OBJC_$_PROP_LIST_CNContactUnificationOptions
+ __OBJC_$_PROP_LIST_CNSensitiveContentConfiguration
+ __OBJC_$_PROP_LIST_CNSensitiveContentConfigurationDescription
+ __OBJC_$_PROP_LIST_CNWallpaperURIDescription
+ __OBJC_CLASS_PROTOCOLS_$_CNContactUnificationOptions
+ __OBJC_CLASS_PROTOCOLS_$_CNSensitiveContentConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CNSensitiveContentConfigurationDescription
+ __OBJC_CLASS_PROTOCOLS_$_CNWallpaperURIDescription
+ __OBJC_CLASS_RO_$_CNContactUnificationOptions
+ __OBJC_CLASS_RO_$_CNSensitiveContentConfiguration
+ __OBJC_CLASS_RO_$_CNSensitiveContentConfigurationDescription
+ __OBJC_CLASS_RO_$_CNWallpaperURIDescription
+ __OBJC_METACLASS_RO_$_CNContactUnificationOptions
+ __OBJC_METACLASS_RO_$_CNSensitiveContentConfiguration
+ __OBJC_METACLASS_RO_$_CNSensitiveContentConfigurationDescription
+ __OBJC_METACLASS_RO_$_CNWallpaperURIDescription
+ ___38+[CNSensitiveContentConfiguration log]_block_invoke
+ ___45+[CNContactUnificationOptions sharedInstance]_block_invoke
+ ___46-[CNMutableContact overwriteStateFromContact:]_block_invoke.221
+ ___50+[CN(PropertyDescription) wallpaperURIDescription]_block_invoke
+ ___57-[CNiOSABContactBuffersDecoder unifyContacts:moreComing:]_block_invoke.13
+ ___58+[CNUnifiedContacts unifyMultivalues:forProperty:options:]_block_invoke
+ ___58-[CNiOSAddressBookDataMapper policyWithDescription:error:]_block_invoke_3
+ ___60-[CNiOSAddressBookDataMapper groupsMatchingPredicate:error:]_block_invoke_3
+ ___62-[CNiOSAddressBookDataMapper accountsMatchingPredicate:error:]_block_invoke_4
+ ___65+[CNCalculatesContactDiff clearWallpaperURIInUpdates:forContact:]_block_invoke
+ ___65+[CNCalculatesContactDiff clearWallpaperURIInUpdates:forContact:]_block_invoke_2
+ ___65-[CNiOSAddressBookDataMapper usedLabelsForPropertyWithKey:error:]_block_invoke_2
+ ___67+[CN(PropertyDescription) sensitiveContentConfigurationDescription]_block_invoke
+ ___67-[CNiOSAddressBookDataMapper sectionListOffsetsForSortOrder:error:]_block_invoke_3
+ ___72-[CNiOSAddressBookDataMapper _containersMatchingPredicate:remote:error:]_block_invoke_4
+ ___75-[CNiOSAddressBookDataMapper moveContacts:fromContainer:toContainer:error:]_block_invoke_2
+ ___block_descriptor_40_e17_B16?0"NSArray"8l
+ ___block_descriptor_40_e8_32r_e14_"NSError"8?0lr32l8
+ ___block_descriptor_40_e8_32s_e14_"NSError"8?0ls32l8
+ ___block_descriptor_41_e8_32s_e28_"CNContact"16?0"NSArray"8ls32l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e26_v32?0"CNContact"8Q16^B24lr56l8r64l8s32l8s48l8s40l8
+ ___block_literal_global.151
+ ___block_literal_global.156
+ ___block_literal_global.179
+ ___block_literal_global.220
+ ___block_literal_global.223
+ ___block_literal_global.242
+ ___block_literal_global.290
+ ___block_literal_global.305
+ ___block_literal_global.314
+ ___block_literal_global.390
+ ___block_literal_global.393
+ ___block_literal_global.52
+ ___block_literal_global.758
+ ___block_literal_global.78
+ ___block_literal_global.809
+ ___block_literal_global.818
+ ___block_literal_global.82
+ ___block_literal_global.84
+ __block_invoke_20
+ _backgroundColorRelatedKeys.cn_once_object_4
+ _backgroundColorRelatedKeys.cn_once_token_4
+ _imageBackgroundColorsDataDescription.cn_once_object_92
+ _imageBackgroundColorsDataDescription.cn_once_token_92
+ _kABPersonSensitiveContentConfigurationProperty
+ _kABPersonWallpaperURIProperty
+ _objc_msgSend$_setSensitiveContentConfiguration:
+ _objc_msgSend$_setWallpaperURI:
+ _objc_msgSend$_unifyContacts:options:
+ _objc_msgSend$alwaysUnifyLabeledValues
+ _objc_msgSend$clearWallpaperURIInUpdates:forContact:
+ _objc_msgSend$configurationWithOverride:
+ _objc_msgSend$contactUnifyingContacts:options:
+ _objc_msgSend$initWithContactFetchRequest:
+ _objc_msgSend$initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:
+ _objc_msgSend$initWithSensitiveContentOverride:
+ _objc_msgSend$labeledValueUnificationThreshold
+ _objc_msgSend$override
+ _objc_msgSend$sensitiveContentConfiguration
+ _objc_msgSend$sensitiveContentConfigurationDescription
+ _objc_msgSend$setBatchSize:
+ _objc_msgSend$setDecoderBatchSize:
+ _objc_msgSend$setOverride:
+ _objc_msgSend$setSensitiveContentConfiguration:
+ _objc_msgSend$setShouldFreezeMutableContacts:
+ _objc_msgSend$setShouldIncludeMainStoreContacts:
+ _objc_msgSend$setWallpaperURI:
+ _objc_msgSend$shouldFreezeMutableContacts
+ _objc_msgSend$shouldIncludeMainStoreContacts
+ _objc_msgSend$unificationOptions
+ _objc_msgSend$unifyMultiValue:intoMultiValue:forProperty:
+ _objc_msgSend$unifyMultivalues:forProperty:options:
+ _objc_msgSend$wallpaperURI
+ _objc_msgSend$wallpaperURIDescription
+ _sensitiveContentConfigurationDescription.cn_once_object_93
+ _sensitiveContentConfigurationDescription.cn_once_token_93
+ _wallpaperURIDescription.cn_once_object_91
+ _wallpaperURIDescription.cn_once_token_91
- +[CN(UnifiedContacts) _unifyContacts:includingMainStoreContacts:]
- +[CNUnifiedContacts _unifyContactsSortedByPreference:includingMainStoreContacts:]
- +[CNUnifiedContacts unifyMultiValuesOfContacts:intoContact:availableKeyDescriptor:]
- -[CNiOSABContactBuffersDecoder initWithDecoder:unifyResults:mutableResults:decodeBatchLimit:]
- GCC_except_table112
- GCC_except_table126
- GCC_except_table139
- GCC_except_table150
- GCC_except_table155
- GCC_except_table159
- GCC_except_table170
- GCC_except_table182
- GCC_except_table194
- GCC_except_table204
- GCC_except_table209
- GCC_except_table212
- GCC_except_table214
- GCC_except_table224
- GCC_except_table37
- GCC_except_table43
- GCC_except_table54
- GCC_except_table66
- GCC_except_table70
- ___46-[CNMutableContact overwriteStateFromContact:]_block_invoke.215
- ___83+[CNUnifiedContacts unifyMultiValuesOfContacts:intoContact:availableKeyDescriptor:]_block_invoke
- ___block_descriptor_32_e31_"CNContact"20?0"NSArray"8B16l
- ___block_descriptor_48_e8_32s40s_e26_v32?0"CNContact"8Q16^B24ls32l8s40l8
- ___block_descriptor_65_e8_32s40s48r56r_e26_v32?0"CNContact"8Q16^B24lr48l8r56l8s32l8s40l8
- ___block_literal_global.155
- ___block_literal_global.158
- ___block_literal_global.214
- ___block_literal_global.217
- ___block_literal_global.236
- ___block_literal_global.284
- ___block_literal_global.299
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.47
- ___block_literal_global.744
- ___block_literal_global.795
- ___block_literal_global.804
- _backgroundColorRelatedKeys.cn_once_object_3
- _backgroundColorRelatedKeys.cn_once_token_3
- _imageBackgroundColorsDataDescription.cn_once_object_91
- _imageBackgroundColorsDataDescription.cn_once_token_91
- _objc_msgSend$_unifyContacts:includingMainStoreContacts:
- _objc_msgSend$initWithDecoder:unifyResults:mutableResults:decodeBatchLimit:
- _objc_msgSend$unifyMultivalues:forProperty:
- _unifyContacts
- _unifyContacts_block_invoke
CStrings:
+ "\x01/\x0eC\x11\x11O\x0f\v"
+ "\x11\x13"
+ "@\"CNContact\"16@?0@\"NSArray\"8"
+ "@\"CNContactUnificationOptions\""
+ "@\"CNSensitiveContentConfiguration\""
+ "@\"NSError\"8@?0"
+ "@48@0:8@16B24@28B36q40"
+ "@68@0:8@16@24B32I36B40q44@52Q60"
+ "CNContactUnificationOptions"
+ "CNSensitiveContentConfiguration"
+ "CNSensitiveContentConfiguration has a higher version number than we know how to handle: %ld"
+ "CNSensitiveContentConfigurationDescription"
+ "CNWallpaperURIDescription"
+ "Cleared wallpaper URI for contact identifier %{public}@"
+ "Error archiving CNSensitiveContentConfiguration: %@"
+ "Error unarchiving Core Data value into CNSensitiveContentConfiguration: %@"
+ "Poster should be saved to recents: %d | sensitive: %d, emptyData: %d, override: %d"
+ "T@\"CNContactUnificationOptions\",R,C,N,V_unificationOptions"
+ "T@\"CNContactUnificationOptions\",R,N"
+ "T@\"CNSensitiveContentConfiguration\",C,D,N"
+ "T@\"CNSensitiveContentConfiguration\",R,C,N"
+ "TB,N,V_alwaysUnifyLabeledValues"
+ "TB,N,V_shouldFreezeMutableContacts"
+ "TB,N,V_shouldIncludeMainStoreContacts"
+ "Tq,N,V_batchSize"
+ "Tq,N,V_contactBatchCount"
+ "Tq,N,V_decoderBatchSize"
+ "Tq,N,V_labeledValueUnificationThreshold"
+ "Tq,N,V_override"
+ "Tq,R,N,V_decodeBatchSize"
+ "Tq,R,V_batchSize"
+ "_alwaysUnifyLabeledValues"
+ "_contactBatchCount"
+ "_labeledValueUnificationThreshold"
+ "_override"
+ "_sensitiveContentConfiguration"
+ "_setSensitiveContentConfiguration:"
+ "_setWallpaperURI:"
+ "_shouldFreezeMutableContacts"
+ "_shouldIncludeMainStoreContacts"
+ "_unificationOptions"
+ "_unifyContacts:options:"
+ "_wallpaperURI"
+ "alwaysUnifyLabeledValues"
+ "clearWallpaperURIInUpdates:forContact:"
+ "configurationWithOverride:"
+ "contactBatchCount"
+ "contactUnifyingContacts:options:"
+ "initWithContactFetchRequest:"
+ "initWithDecoder:unifyResults:unificationOptions:mutableResults:decodeBatchLimit:"
+ "initWithSensitiveContentOverride:"
+ "labeledValueUnificationThreshold"
+ "override"
+ "sensitiveContentConfiguration"
+ "sensitiveContentConfigurationDescription"
+ "sensitiveContentConfigurationFromDataTransform"
+ "setAlwaysUnifyLabeledValues:"
+ "setContactBatchCount:"
+ "setLabeledValueUnificationThreshold:"
+ "setOverride:"
+ "setSensitiveContentConfiguration:"
+ "setShouldFreezeMutableContacts:"
+ "setShouldIncludeMainStoreContacts:"
+ "setWallpaperURI:"
+ "shouldFreezeMutableContacts"
+ "shouldIncludeMainStoreContacts"
+ "shouldSaveCurrentPoster:toRecentsForContact:"
+ "unificationOptions"
+ "unifyMultiValue:intoMultiValue:forProperty:"
+ "unifyMultivalues:forProperty:options:"
+ "updatedWithOverride:"
+ "wallpaperURI"
+ "wallpaperURIDescription"
- "\x01/\x0eC\x11\x11O\x0f\t"
- "@\"CNContact\"20@?0@\"NSArray\"8B16"
- "@40@0:8@16B24B28Q32"
- "@68@0:8@16@24B32I36B40Q44@52Q60"
- "TQ,N,V_batchSize"
- "TQ,N,V_decoderBatchSize"
- "TQ,R,N,V_decodeBatchSize"
- "TQ,R,V_batchSize"
- "_unifyContacts:includingMainStoreContacts:"
- "initWithDecoder:unifyResults:mutableResults:decodeBatchLimit:"

```
