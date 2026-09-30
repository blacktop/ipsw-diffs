## PhotosUI

> `/System/Library/Frameworks/PhotosUI.framework/Versions/A/PhotosUI`

```diff

-  __TEXT.__text: 0x5382c
-  __TEXT.__objc_methlist: 0x4cc4
-  __TEXT.__const: 0x33f8
-  __TEXT.__swift5_typeref: 0xe4e
-  __TEXT.__swift5_fieldmd: 0xd54
-  __TEXT.__constg_swiftt: 0xef4
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0xbf5
+  __TEXT.__text: 0x522b4
+  __TEXT.__objc_methlist: 0x4b9c
+  __TEXT.__const: 0x2ed8
+  __TEXT.__oslogstring: 0xfa8
+  __TEXT.__swift5_typeref: 0xd2c
+  __TEXT.__swift5_fieldmd: 0xa34
+  __TEXT.__constg_swiftt: 0xbac
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_reflstr: 0xa31
   __TEXT.__swift5_assocty: 0x330
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_proto: 0x1ac
-  __TEXT.__swift5_types: 0x12c
-  __TEXT.__cstring: 0x5980
-  __TEXT.__oslogstring: 0xcbd
-  __TEXT.__swift5_capture: 0x718
-  __TEXT.__swift_as_entry: 0x80
-  __TEXT.__swift_as_cont: 0xec
-  __TEXT.__swift_as_ret: 0x34
+  __TEXT.__cstring: 0x5a5a
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_proto: 0x194
+  __TEXT.__swift5_types: 0xec
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_capture: 0x978
+  __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_cont: 0x54
+  __TEXT.__swift_as_ret: 0x8
   __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__ustring: 0xd8
-  __TEXT.__unwind_info: 0x1fe0
-  __TEXT.__eh_frame: 0x1534
+  __TEXT.__unwind_info: 0x1d20
+  __TEXT.__eh_frame: 0xf28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7e8
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26e0
-  __DATA_CONST.__objc_protorefs: 0x148
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x26f0
+  __DATA_CONST.__objc_protorefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x630
-  __AUTH_CONST.__const: 0x3460
-  __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0x9460
+  __DATA_CONST.__got: 0x638
+  __AUTH_CONST.__const: 0x34a0
+  __AUTH_CONST.__cfstring: 0x3100
+  __AUTH_CONST.__objc_const: 0x8ef0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x850
-  __AUTH.__objc_data: 0x27b8
-  __AUTH.__data: 0x6a8
-  __DATA.__objc_ivar: 0x424
-  __DATA.__data: 0x1ec0
-  __DATA.__common: 0x150
-  __DATA.__bss: 0x3200
+  __AUTH_CONST.__auth_got: 0x810
+  __AUTH.__objc_data: 0x21a8
+  __AUTH.__data: 0x490
+  __DATA.__objc_ivar: 0x438
+  __DATA.__data: 0x17f0
+  __DATA.__common: 0x178
+  __DATA.__bss: 0x3180
   __DATA_DIRTY.__objc_data: 0x430
   __DATA_DIRTY.__data: 0xe8
   __DATA_DIRTY.__bss: 0x200

   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
-  - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
-  - /System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Photos.framework/Versions/A/Photos
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3527
-  Symbols:   4959
-  CStrings:  1042
+  Functions: 3406
+  Symbols:   4838
+  CStrings:  1057
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[PHPickerFilter _groupsPeopleQuantityFilterWithMinimumMemberCount:maximumMemberCount:]
+ +[PUPickerGroupsPeopleQuantityFilter supportsSecureCoding]
+ +[_PHPickerSuggestionGroup imagePlaygroundSuggestionGroupWithPinnedItemIdentifiers:defaultsToFaceMode:]
+ -[PUPickerCompoundFilter generatedMaximumSocialGroupMemberCount]
+ -[PUPickerCompoundFilter generatedMinimumSocialGroupMemberCount]
+ -[PUPickerGroupsPeopleQuantityFilter allowsAlbums]
+ -[PUPickerGroupsPeopleQuantityFilter containsFilter:]
+ -[PUPickerGroupsPeopleQuantityFilter copyWithZone:]
+ -[PUPickerGroupsPeopleQuantityFilter encodeWithCoder:]
+ -[PUPickerGroupsPeopleQuantityFilter generatedAssetPredicate]
+ -[PUPickerGroupsPeopleQuantityFilter generatedMaximumSocialGroupMemberCount]
+ -[PUPickerGroupsPeopleQuantityFilter generatedMinimumSocialGroupMemberCount]
+ -[PUPickerGroupsPeopleQuantityFilter generatedPossibleAssetTypes]
+ -[PUPickerGroupsPeopleQuantityFilter generatedRequiredAssetTypes]
+ -[PUPickerGroupsPeopleQuantityFilter hash]
+ -[PUPickerGroupsPeopleQuantityFilter initWithCoder:]
+ -[PUPickerGroupsPeopleQuantityFilter initWithMinimumMemberCount:maximumMemberCount:]
+ -[PUPickerGroupsPeopleQuantityFilter isEqual:]
+ -[PUPickerGroupsPeopleQuantityFilter isValidFilter]
+ -[PUPickerGroupsPeopleQuantityFilter maximumMemberCount]
+ -[PUPickerGroupsPeopleQuantityFilter minimumMemberCount]
+ -[_PHPickerCollectionConfiguration _customKeyAssetIdentifiers]
+ -[_PHPickerCollectionConfiguration _setCustomKeyAssetIdentifiers:]
+ -[_PHPickerSuggestionGroup _initWithSuggestions:defaultSuggestionIndex:isForWallpaper:defaultsToFaceMode:hasPinnedSuggestionItems:]
+ -[_PHPickerSuggestionGroup defaultsToFaceMode]
+ -[_PHPickerSuggestionGroup hasPinnedSuggestionItems]
+ GCC_except_table1153
+ GCC_except_table1166
+ GCC_except_table1171
+ GCC_except_table1174
+ GCC_except_table1254
+ GCC_except_table148
+ GCC_except_table157
+ GCC_except_table247
+ GCC_except_table274
+ GCC_except_table343
+ GCC_except_table540
+ GCC_except_table547
+ GCC_except_table555
+ GCC_except_table559
+ GCC_except_table759
+ OBJC_IVAR_$_PUPickerGroupsPeopleQuantityFilter._maximumMemberCount
+ OBJC_IVAR_$_PUPickerGroupsPeopleQuantityFilter._minimumMemberCount
+ OBJC_IVAR_$__PHPickerCollectionConfiguration.__customKeyAssetIdentifiers
+ OBJC_IVAR_$__PHPickerSuggestionGroup._defaultsToFaceMode
+ OBJC_IVAR_$__PHPickerSuggestionGroup._hasPinnedSuggestionItems
+ _OBJC_CLASS_$_NSRemoteViewControllerWithDelegate
+ _OBJC_CLASS_$_NSRemoteViewControllerWithDelegateParameters
+ _OBJC_CLASS_$_PHAssetCollection
+ _OBJC_CLASS_$_PUPickerGroupsPeopleQuantityFilter
+ _OBJC_METACLASS_$_PUPickerGroupsPeopleQuantityFilter
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_89
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
+ _PUPickerFilterGeneratedMaximumSocialGroupMemberCount
+ _PUPickerFilterGeneratedMinimumSocialGroupMemberCount
+ _PUPickerFilterUnionMaximumSocialGroupMemberCount
+ _PUPickerFilterUnionMinimumSocialGroupMemberCount
+ __INSTANCE_METHODS__TtC8PhotosUI27PVSViewBridgeViewController
+ __IVARS__TtC8PhotosUI27PVSViewBridgeViewController
+ __OBJC_$_CLASS_METHODS_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_$_CLASS_PROP_LIST_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_$_INSTANCE_METHODS_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_$_INSTANCE_METHODS__TtC8PhotosUI20PVSAlbumHostDelegate(PhotosUI)
+ __OBJC_$_INSTANCE_METHODS__TtC8PhotosUI22PVSSyncNowHostDelegate(PhotosUI)
+ __OBJC_$_INSTANCE_METHODS__TtC8PhotosUI25PVSPostAssetsHostDelegate(PhotosUI)
+ __OBJC_$_INSTANCE_METHODS__TtC8PhotosUI37PVSCreateSharedCollectionHostDelegate(PhotosUI)
+ __OBJC_$_INSTANCE_METHODS__TtC8PhotosUI40PVSCustomizeSharedCollectionHostDelegate(PhotosUI)
+ __OBJC_$_INSTANCE_VARIABLES_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_$_PROP_LIST_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSRemoteViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSRemoteViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PUPickerFilter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSRemoteViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_NSRemoteViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUI20PVSAlbumHostDelegate(PhotosUI)
+ __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUI22PVSSyncNowHostDelegate(PhotosUI)
+ __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUI25PVSPostAssetsHostDelegate(PhotosUI)
+ __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUI37PVSCreateSharedCollectionHostDelegate(PhotosUI)
+ __OBJC_CLASS_PROTOCOLS_$__TtC8PhotosUI40PVSCustomizeSharedCollectionHostDelegate(PhotosUI)
+ __OBJC_CLASS_RO_$_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_LABEL_PROTOCOL_$_NSRemoteViewControllerDelegate
+ __OBJC_METACLASS_RO_$_PUPickerGroupsPeopleQuantityFilter
+ __OBJC_PROTOCOL_$_NSRemoteViewControllerDelegate
+ ___swift_memcpy17_8
+ ___swift_project_boxed_opaque_existential_0
+ __swift__destructor
+ __swift_closure_destructor.17Tm
+ __swift_closure_destructor.28Tm
+ __swift_closure_destructor.46Tm
+ __swift_closure_destructor.8Tm
+ _associated conformance 8PhotosUI26PVSViewBridgeConfigurationVyxGSHAASQ
+ _objc_msgSend$_groupsPeopleQuantityFilterWithMinimumMemberCount:maximumMemberCount:
+ _objc_msgSend$_initWithSuggestions:defaultSuggestionIndex:isForWallpaper:defaultsToFaceMode:hasPinnedSuggestionItems:
+ _objc_msgSend$_setCustomKeyAssetIdentifiers:
+ _objc_msgSend$canPerformEditOperation:
+ _objc_msgSend$fetchAssetCollectionsWithLocalIdentifiers:options:
+ _objc_msgSend$generatedMaximumSocialGroupMemberCount
+ _objc_msgSend$generatedMinimumSocialGroupMemberCount
+ _objc_msgSend$imagePlaygroundSuggestionGroupWithPinnedItemIdentifiers:defaultsToFaceMode:
+ _objc_msgSend$initWithMinimumMemberCount:maximumMemberCount:
+ _objc_msgSend$initWithPinnedItemIdentifiers:
+ _objc_msgSend$isViewLoaded
+ _objc_msgSend$librarySpecificFetchOptions
+ _objc_msgSend$maximumMemberCount
+ _objc_msgSend$minimumMemberCount
+ _objc_msgSend$openPhotoLibraryWithWellKnownIdentifier:error:
+ _objc_msgSend$setPostedToAlbumIdentifier:
+ _objc_msgSend$setServiceViewControllerClassName:
+ _swift_bridgeObjectRelease_n
+ _swift_dynamicCastObjCProtocolUnconditional
+ _swift_getDynamicType
+ _swift_getErrorValue
+ _swift_getMetatypeMetadata
+ _symbolic B0
+ _symbolic SDyS2SG
+ _symbolic SNySiG
+ _symbolic SS12delegateType_t
+ _symbolic SaySo8NSStringCG
+ _symbolic SnySiG
+ _symbolic So16NSViewControllerCSg
+ _symbolic So34NSRemoteViewControllerWithDelegateC
+ _symbolic So8NSObjectCIego_
+ _symbolic So8NSObjectCSgIego_
+ _symbolic _____ 8PhotosUI26PVSViewBridgeConfigurationV
+ _symbolic _____ 8PhotosUI27PVSViewBridgeViewControllerC
+ _symbolic ______p s5ErrorP
+ _symbolic ______p10underlying_t s5ErrorP
+ _symbolic ______pIego_ s5ErrorP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySiG s16PartialRangeFromV
+ _symbolic _____ySiG s16PartialRangeUpToV
+ _symbolic _____ySiG s19PartialRangeThroughV
+ _symbolic _____y_____G 8PhotosUI26PVSViewBridgeConfigurationV AA20PVSAlbumHostDelegateC
+ _symbolic _____y_____G 8PhotosUI26PVSViewBridgeConfigurationV AA22PVSSyncNowHostDelegateC
+ _symbolic _____y_____G 8PhotosUI26PVSViewBridgeConfigurationV AA25PVSPostAssetsHostDelegateC
+ _symbolic _____y_____G 8PhotosUI26PVSViewBridgeConfigurationV AA37PVSCreateSharedCollectionHostDelegateC
+ _symbolic _____y_____G 8PhotosUI26PVSViewBridgeConfigurationV AA40PVSCustomizeSharedCollectionHostDelegateC
+ _symbolic _____y_____G 8PhotosUI27PVSViewBridgeViewControllerC AA20PVSAlbumHostDelegateC
+ _symbolic _____y_____G 8PhotosUI27PVSViewBridgeViewControllerC AA22PVSSyncNowHostDelegateC
+ _symbolic _____y_____G 8PhotosUI27PVSViewBridgeViewControllerC AA25PVSPostAssetsHostDelegateC
+ _symbolic _____y_____G 8PhotosUI27PVSViewBridgeViewControllerC AA37PVSCreateSharedCollectionHostDelegateC
+ _symbolic _____y_____G 8PhotosUI27PVSViewBridgeViewControllerC AA40PVSCustomizeSharedCollectionHostDelegateC
+ _symbolic _____y_____GSg 8PhotosUI26PVSViewBridgeConfigurationV AA20PVSAlbumHostDelegateC
+ _symbolic _____y_____GSg 8PhotosUI26PVSViewBridgeConfigurationV AA22PVSSyncNowHostDelegateC
+ _symbolic _____y_____GSg 8PhotosUI26PVSViewBridgeConfigurationV AA25PVSPostAssetsHostDelegateC
+ _symbolic _____y_____GSg 8PhotosUI26PVSViewBridgeConfigurationV AA37PVSCreateSharedCollectionHostDelegateC
+ _symbolic _____y_____GSg 8PhotosUI26PVSViewBridgeConfigurationV AA40PVSCustomizeSharedCollectionHostDelegateC
+ _symbolic _____y_____GSgXw 8PhotosUI27PVSViewBridgeViewControllerC AA20PVSAlbumHostDelegateC
+ _symbolic _____y_____GSgXw 8PhotosUI27PVSViewBridgeViewControllerC AA22PVSSyncNowHostDelegateC
+ _symbolic _____y_____GSgXw 8PhotosUI27PVSViewBridgeViewControllerC AA25PVSPostAssetsHostDelegateC
+ _symbolic _____y_____GSgXw 8PhotosUI27PVSViewBridgeViewControllerC AA37PVSCreateSharedCollectionHostDelegateC
+ _symbolic _____y_____GSgXw 8PhotosUI27PVSViewBridgeViewControllerC AA40PVSCustomizeSharedCollectionHostDelegateC
+ _symbolic _____yxGSg 8PhotosUI26PVSViewBridgeConfigurationV
+ _symbolic _____yxGSgXw 8PhotosUI27PVSViewBridgeViewControllerC
+ _symbolic _____yxGSgXwz____________RzlXX 8PhotosUI27PVSViewBridgeViewControllerC AA20PVSAlbumHostDelegateC AA07PVSHostI0P
+ _symbolic _____yxGSgXwz____________RzlXX 8PhotosUI27PVSViewBridgeViewControllerC AA22PVSSyncNowHostDelegateC AA07PVSHostJ0P
+ _symbolic _____yxGSgXwz____________RzlXX 8PhotosUI27PVSViewBridgeViewControllerC AA25PVSPostAssetsHostDelegateC AA07PVSHostJ0P
+ _symbolic _____yxGSgXwz____________RzlXX 8PhotosUI27PVSViewBridgeViewControllerC AA37PVSCreateSharedCollectionHostDelegateC AA07PVSHostK0P
+ _symbolic _____yxGSgXwz____________RzlXX 8PhotosUI27PVSViewBridgeViewControllerC AA40PVSCustomizeSharedCollectionHostDelegateC AA07PVSHostK0P
+ _symbolic _____yxGSgXwz_x______RzlXX 8PhotosUI27PVSViewBridgeViewControllerC AA15PVSHostDelegateP
+ _symbolic yp
- -[_PHPickerSuggestionGroup _initWithSuggestions:defaultSuggestionIndex:isForWallpaper:]
- GCC_except_table1124
- GCC_except_table1137
- GCC_except_table1142
- GCC_except_table1145
- GCC_except_table1225
- GCC_except_table125
- GCC_except_table134
- GCC_except_table224
- GCC_except_table251
- GCC_except_table320
- GCC_except_table517
- GCC_except_table524
- GCC_except_table532
- GCC_except_table536
- GCC_except_table736
- _OBJC_CLASS_$_EXHostViewController
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$__TtC8PhotosUI17PVSConcreteClient
- _OBJC_CLASS_$__TtC8PhotosUI22PVSAlbumConcreteClient
- _OBJC_CLASS_$__TtC8PhotosUI23PVSClientViewController
- _OBJC_CLASS_$__TtC8PhotosUI24PVSSyncNowConcreteClient
- _OBJC_CLASS_$__TtC8PhotosUI27PVSPostAssetsConcreteClient
- _OBJC_CLASS_$__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- _OBJC_CLASS_$__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- _OBJC_METACLASS_$__TtC8PhotosUI17PVSConcreteClient
- _OBJC_METACLASS_$__TtC8PhotosUI22PVSAlbumConcreteClient
- _OBJC_METACLASS_$__TtC8PhotosUI23PVSClientViewController
- _OBJC_METACLASS_$__TtC8PhotosUI24PVSSyncNowConcreteClient
- _OBJC_METACLASS_$__TtC8PhotosUI27PVSPostAssetsConcreteClient
- _OBJC_METACLASS_$__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- _OBJC_METACLASS_$__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- _PROTOCOLS__TtC8PhotosUI17PVSConcreteClient
- _PROTOCOLS__TtC8PhotosUI20PVSAlbumHostDelegate
- _PROTOCOLS__TtC8PhotosUI22PVSAlbumConcreteClient
- _PROTOCOLS__TtC8PhotosUI22PVSSyncNowHostDelegate
- _PROTOCOLS__TtC8PhotosUI24PVSSyncNowConcreteClient
- _PROTOCOLS__TtC8PhotosUI25PVSPostAssetsHostDelegate
- _PROTOCOLS__TtC8PhotosUI27PVSPostAssetsConcreteClient
- _PROTOCOLS__TtC8PhotosUI37PVSCreateSharedCollectionHostDelegate
- _PROTOCOLS__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- _PROTOCOLS__TtC8PhotosUI40PVSCustomizeSharedCollectionHostDelegate
- _PROTOCOLS__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- __DATA__TtC8PhotosUI17PVSConcreteClient
- __DATA__TtC8PhotosUI22PVSAlbumConcreteClient
- __DATA__TtC8PhotosUI23PVSClientViewController
- __DATA__TtC8PhotosUI24PVSSyncNowConcreteClient
- __DATA__TtC8PhotosUI26PVSClientConnectionManager
- __DATA__TtC8PhotosUI27PVSPostAssetsConcreteClient
- __DATA__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- __DATA__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- __INSTANCE_METHODS__TtC8PhotosUI17PVSConcreteClient
- __INSTANCE_METHODS__TtC8PhotosUI17PVSViewController
- __INSTANCE_METHODS__TtC8PhotosUI20PVSAlbumHostDelegate
- __INSTANCE_METHODS__TtC8PhotosUI22PVSAlbumConcreteClient
- __INSTANCE_METHODS__TtC8PhotosUI22PVSSyncNowHostDelegate
- __INSTANCE_METHODS__TtC8PhotosUI23PVSClientViewController
- __INSTANCE_METHODS__TtC8PhotosUI24PVSSyncNowConcreteClient
- __INSTANCE_METHODS__TtC8PhotosUI25PVSPostAssetsHostDelegate
- __INSTANCE_METHODS__TtC8PhotosUI27PVSPostAssetsConcreteClient
- __INSTANCE_METHODS__TtC8PhotosUI37PVSCreateSharedCollectionHostDelegate
- __INSTANCE_METHODS__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- __INSTANCE_METHODS__TtC8PhotosUI40PVSCustomizeSharedCollectionHostDelegate
- __INSTANCE_METHODS__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- __IVARS__TtC8PhotosUI17PVSConcreteClient
- __IVARS__TtC8PhotosUI17PVSViewController
- __IVARS__TtC8PhotosUI22PVSAlbumConcreteClient
- __IVARS__TtC8PhotosUI23PVSClientViewController
- __IVARS__TtC8PhotosUI24PVSSyncNowConcreteClient
- __IVARS__TtC8PhotosUI26PVSClientConnectionManager
- __IVARS__TtC8PhotosUI27PVSPostAssetsConcreteClient
- __IVARS__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- __IVARS__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- __METACLASS_DATA__TtC8PhotosUI17PVSConcreteClient
- __METACLASS_DATA__TtC8PhotosUI22PVSAlbumConcreteClient
- __METACLASS_DATA__TtC8PhotosUI23PVSClientViewController
- __METACLASS_DATA__TtC8PhotosUI24PVSSyncNowConcreteClient
- __METACLASS_DATA__TtC8PhotosUI26PVSClientConnectionManager
- __METACLASS_DATA__TtC8PhotosUI27PVSPostAssetsConcreteClient
- __METACLASS_DATA__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- __METACLASS_DATA__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EXHostViewControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSAlbumClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSAlbumServer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSharedAlbumCreationClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSharedAlbumCreationServer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSharedAlbumCustomizationClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSharedAlbumCustomizationServer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSharedAlbumPostingClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSharedAlbumPostingServer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSyncNowClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PVSSyncNowServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_EXHostViewControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSAlbumClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSAlbumServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSharedAlbumCreationClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSharedAlbumCreationServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSharedAlbumCustomizationClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSharedAlbumCustomizationServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSharedAlbumPostingClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSharedAlbumPostingServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSyncNowClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_PVSSyncNowServer
- __OBJC_$_PROTOCOL_REFS_EXHostViewControllerDelegate
- __OBJC_$_PROTOCOL_REFS_PVSAlbumClient
- __OBJC_$_PROTOCOL_REFS_PVSAlbumServer
- __OBJC_$_PROTOCOL_REFS_PVSClient
- __OBJC_$_PROTOCOL_REFS_PVSServer
- __OBJC_$_PROTOCOL_REFS_PVSSharedAlbumCreationClient
- __OBJC_$_PROTOCOL_REFS_PVSSharedAlbumCreationServer
- __OBJC_$_PROTOCOL_REFS_PVSSharedAlbumCustomizationClient
- __OBJC_$_PROTOCOL_REFS_PVSSharedAlbumCustomizationServer
- __OBJC_$_PROTOCOL_REFS_PVSSharedAlbumPostingClient
- __OBJC_$_PROTOCOL_REFS_PVSSharedAlbumPostingServer
- __OBJC_$_PROTOCOL_REFS_PVSSyncNowClient
- __OBJC_$_PROTOCOL_REFS_PVSSyncNowServer
- __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionClient
- __OBJC_LABEL_PROTOCOL_$_EXHostViewControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_PVSAlbumClient
- __OBJC_LABEL_PROTOCOL_$_PVSAlbumServer
- __OBJC_LABEL_PROTOCOL_$_PVSClient
- __OBJC_LABEL_PROTOCOL_$_PVSServer
- __OBJC_LABEL_PROTOCOL_$_PVSSharedAlbumCreationClient
- __OBJC_LABEL_PROTOCOL_$_PVSSharedAlbumCreationServer
- __OBJC_LABEL_PROTOCOL_$_PVSSharedAlbumCustomizationClient
- __OBJC_LABEL_PROTOCOL_$_PVSSharedAlbumCustomizationServer
- __OBJC_LABEL_PROTOCOL_$_PVSSharedAlbumPostingClient
- __OBJC_LABEL_PROTOCOL_$_PVSSharedAlbumPostingServer
- __OBJC_LABEL_PROTOCOL_$_PVSSyncNowClient
- __OBJC_LABEL_PROTOCOL_$_PVSSyncNowServer
- __OBJC_PROTOCOL_$_BSServiceConnectionClient
- __OBJC_PROTOCOL_$_EXHostViewControllerDelegate
- __OBJC_PROTOCOL_$_PVSAlbumClient
- __OBJC_PROTOCOL_$_PVSAlbumServer
- __OBJC_PROTOCOL_$_PVSClient
- __OBJC_PROTOCOL_$_PVSServer
- __OBJC_PROTOCOL_$_PVSSharedAlbumCreationClient
- __OBJC_PROTOCOL_$_PVSSharedAlbumCreationServer
- __OBJC_PROTOCOL_$_PVSSharedAlbumCustomizationClient
- __OBJC_PROTOCOL_$_PVSSharedAlbumCustomizationServer
- __OBJC_PROTOCOL_$_PVSSharedAlbumPostingClient
- __OBJC_PROTOCOL_$_PVSSharedAlbumPostingServer
- __OBJC_PROTOCOL_$_PVSSyncNowClient
- __OBJC_PROTOCOL_$_PVSSyncNowServer
- __PROTOCOLS__TtC8PhotosUI17PVSConcreteClient
- __PROTOCOLS__TtC8PhotosUI20PVSAlbumHostDelegate
- __PROTOCOLS__TtC8PhotosUI22PVSAlbumConcreteClient
- __PROTOCOLS__TtC8PhotosUI22PVSSyncNowHostDelegate
- __PROTOCOLS__TtC8PhotosUI24PVSSyncNowConcreteClient
- __PROTOCOLS__TtC8PhotosUI25PVSPostAssetsHostDelegate
- __PROTOCOLS__TtC8PhotosUI27PVSPostAssetsConcreteClient
- __PROTOCOLS__TtC8PhotosUI37PVSCreateSharedCollectionHostDelegate
- __PROTOCOLS__TtC8PhotosUI39PVSCreateSharedCollectionConcreteClient
- __PROTOCOLS__TtC8PhotosUI40PVSCustomizeSharedCollectionHostDelegate
- __PROTOCOLS__TtC8PhotosUI42PVSCustomizeSharedCollectionConcreteClient
- ___swift_memcpy10_8
- ___swift_memcpy37_8
- ___swift_memcpy40_8
- ___swift_memcpy64_8
- ___swift_memcpy72_8
- _associated conformance 8PhotosUI16PVSInterfaceTypeOSHAASQ
- _associated conformance 8PhotosUI20PVSHostConfigurationVyxGSHAASQ
- _flat unique 8PhotosUI16PVSAlbumProtocol_p
- _flat unique 8PhotosUI18PVSSyncNowProtocol_p
- _flat unique 8PhotosUI21PVSPostAssetsProtocol_p
- _flat unique 8PhotosUI33PVSCreateSharedCollectionProtocol_p
- _flat unique 8PhotosUI36PVSCustomizeSharedCollectionProtocol_p
- _flat unique So25BSServiceConnectionClient_p
- _flat unique So9PVSServer_p
- _get_enum_tag_for_layout_string Ieg_Sg
- _get_enum_tag_for_layout_string SbIegy_Sg
- _objc_msgSend$_initWithSuggestions:defaultSuggestionIndex:isForWallpaper:
- _objc_msgSend$activate
- _objc_msgSend$boolValue
- _objc_msgSend$makeXPCConnectionWithError:
- _objc_msgSend$provide:uuid:
- _objc_msgSend$provideAlbumType:hasHeaderEverBeenDismissed:uuid:
- _objc_msgSend$provideAssetCollectionLocalIdentifier:assetIdentifiers:uuid:
- _objc_msgSend$provideAssetCollectionLocalIdentifier:uuid:
- _objc_msgSend$provideDefaultTitle:defaultSharingPolicy:uuid:
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _symbolic $s8PhotosUI22PVSClientConfigurationP
- _symbolic Ieg_
- _symbolic SSSg_____Sg______pSgIeggng_ 10Foundation3URLV s5ErrorP
- _symbolic SSSg______pSgIeggg_ s5ErrorP
- _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
- _symbolic So15NSXPCConnectionCSg
- _symbolic So17OS_dispatch_queueC
- _symbolic So20EXHostViewControllerC
- _symbolic So20EXHostViewControllerCSg
- _symbolic So8ProtocolC
- _symbolic So8ProtocolCSg
- _symbolic _____ 19ExtensionFoundation03AppA8IdentityV
- _symbolic _____ 8PhotosUI16PVSInterfaceTypeO
- _symbolic _____ 8PhotosUI17PVSConcreteClientC
- _symbolic _____ 8PhotosUI17PVSViewControllerC
- _symbolic _____ 8PhotosUI19PVSInterfaceFactoryV
- _symbolic _____ 8PhotosUI19PVSInterfaceFactoryV13ConfigurationV
- _symbolic _____ 8PhotosUI20PVSHostConfigurationV
- _symbolic _____ 8PhotosUI22PVSAlbumConcreteClientC
- _symbolic _____ 8PhotosUI23PVSClientViewControllerC
- _symbolic _____ 8PhotosUI24PVSSyncNowConcreteClientC
- _symbolic _____ 8PhotosUI26PVSClientConnectionManagerC
- _symbolic _____ 8PhotosUI27PVSClientAlbumConfigurationV
- _symbolic _____ 8PhotosUI27PVSPostAssetsConcreteClientC
- _symbolic _____ 8PhotosUI29PVSClientSyncNowConfigurationV
- _symbolic _____ 8PhotosUI39PVSCreateSharedCollectionConcreteClientC
- _symbolic _____ 8PhotosUI40PVSClientSharedAlbumPostingConfigurationV
- _symbolic _____ 8PhotosUI41PVSClientSharedAlbumCreationConfigurationV
- _symbolic _____ 8PhotosUI42PVSCustomizeSharedCollectionConcreteClientC
- _symbolic _____ 8PhotosUI46PVSClientSharedAlbumCustomizationConfigurationV
- _symbolic _____Sg 19ExtensionFoundation03AppA8IdentityV
- _symbolic _____Sg 8PhotosUI0A16AlbumViewContentO
- _symbolic _____Sg 8PhotosUI26PVSClientConnectionManagerC
- _symbolic _____Sg So20EXHostViewControllerC12ExtensionKitE13ConfigurationV
- _symbolic _____SgXwz_Xx 8PhotosUI22PVSSyncNowHostDelegateC
- _symbolic _____SgXwz_Xx 8PhotosUI25PVSPostAssetsHostDelegateC
- _symbolic _____SgXwz_Xx 8PhotosUI37PVSCreateSharedCollectionHostDelegateC
- _symbolic _____SgXwz_Xx 8PhotosUI40PVSCustomizeSharedCollectionHostDelegateC
- _symbolic ______p 8PhotosUI16PVSAlbumProtocolP
- _symbolic ______p 8PhotosUI18PVSSyncNowProtocolP
- _symbolic ______p 8PhotosUI21PVSPostAssetsProtocolP
- _symbolic ______p 8PhotosUI33PVSCreateSharedCollectionProtocolP
- _symbolic ______p 8PhotosUI36PVSCustomizeSharedCollectionProtocolP
- _symbolic ______pSg So9PVSServerP
- _symbolic _____y_____G 8PhotosUI17PVSViewControllerC AA20PVSAlbumHostDelegateC
- _symbolic _____y_____G 8PhotosUI17PVSViewControllerC AA22PVSSyncNowHostDelegateC
- _symbolic _____y_____G 8PhotosUI17PVSViewControllerC AA25PVSPostAssetsHostDelegateC
- _symbolic _____y_____G 8PhotosUI17PVSViewControllerC AA37PVSCreateSharedCollectionHostDelegateC
- _symbolic _____y_____G 8PhotosUI17PVSViewControllerC AA40PVSCustomizeSharedCollectionHostDelegateC
- _symbolic _____y_____G 8PhotosUI20PVSHostConfigurationV AA20PVSAlbumHostDelegateC
- _symbolic _____y_____G 8PhotosUI20PVSHostConfigurationV AA22PVSSyncNowHostDelegateC
- _symbolic _____y_____G 8PhotosUI20PVSHostConfigurationV AA25PVSPostAssetsHostDelegateC
- _symbolic _____y_____G 8PhotosUI20PVSHostConfigurationV AA37PVSCreateSharedCollectionHostDelegateC
- _symbolic _____y_____G 8PhotosUI20PVSHostConfigurationV AA40PVSCustomizeSharedCollectionHostDelegateC
- _symbolic _____y_____GSg 8PhotosUI20PVSHostConfigurationV AA20PVSAlbumHostDelegateC
- _symbolic _____y_____GSg 8PhotosUI20PVSHostConfigurationV AA22PVSSyncNowHostDelegateC
- _symbolic _____y_____GSg 8PhotosUI20PVSHostConfigurationV AA25PVSPostAssetsHostDelegateC
- _symbolic _____y_____GSg 8PhotosUI20PVSHostConfigurationV AA37PVSCreateSharedCollectionHostDelegateC
- _symbolic _____y_____GSg 8PhotosUI20PVSHostConfigurationV AA40PVSCustomizeSharedCollectionHostDelegateC
- _symbolic _____y_____SgG 2os21OSAllocatedUnfairLockV 8PhotosUI17PVSConcreteClientC
- _symbolic _____y______So19BSServiceConnectionCXcSgG 2os21OSAllocatedUnfairLockV So25BSServiceConnectionClientP
- _symbolic _____yxGSg 8PhotosUI20PVSHostConfigurationV
- _symbolic ySSSg______Sg______pSgtc 10Foundation3URLV s5ErrorP
- _symbolic ySSSg_______pSgtc s5ErrorP
- _symbolic ySbc
- _symbolic ytIegr_
- _type_layout_string 8PhotosUI19PVSInterfaceFactoryV13ConfigurationV
- _type_layout_string 8PhotosUI27PVSClientAlbumConfigurationV
- _type_layout_string 8PhotosUI29PVSClientSyncNowConfigurationV
- _type_layout_string 8PhotosUI40PVSClientSharedAlbumPostingConfigurationV
- _type_layout_string 8PhotosUI41PVSClientSharedAlbumCreationConfigurationV
- _type_layout_string 8PhotosUI46PVSClientSharedAlbumCustomizationConfigurationV
CStrings:
+ " doesn't conform to NSRemoteViewControllerDelegate"
+ "%s: %@"
+ "%s: %s"
+ "%s: Remote view controller did activate."
+ "%s: XPC proxy error: %@"
+ "(%s: %s): loadExtension already invoked (existing requestUUID %s); ignoring."
+ "(%s: %s): remote view controller activation failed: %@."
+ "(Shared album asset posting: "
+ "(Shared album creation: "
+ "(Shared album customization: "
+ "+[PHPickerFilter _groupsPeopleQuantityFilterWithMinimumMemberCount:maximumMemberCount:]"
+ "-[PUPickerGroupsPeopleQuantityFilter isEqual:]"
+ "-[_PHPickerSuggestionGroup _initWithSuggestions:defaultSuggestionIndex:isForWallpaper:defaultsToFaceMode:hasPinnedSuggestionItems:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BIgrnf/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PHPicker.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BIgrnf/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PUPickerFilter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BIgrnf/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PUPickerRemoteViewController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BIgrnf/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PUPickerUnavailableViewController.m"
+ "Completion was called for posting to shared album with identifier: %s, error: %s."
+ "Failed to open the system photo library while validating add-content permission: %@"
+ "NSRemoteViewControllerWithDelegate.request failed: "
+ "NSRemoteViewControllerWithDelegate.request returned an unexpected controller type"
+ "PHPickerCollectionConfigurationCoderCustomKeyAssetIdentifiersKey"
+ "PHPickerSuggestionGroupCoderDefaultsToFaceModeKey"
+ "PHPickerSuggestionGroupCoderHasPinnedSuggestionItemsKey"
+ "PUPickerGroupsPeopleQuantityFilter: invalid member count range: [%ld, %ld]"
+ "PUPickerGroupsPeopleQuantityFilterDictionaryMaximumMemberCountKey"
+ "PUPickerGroupsPeopleQuantityFilterDictionaryMinimumMemberCountKey"
+ "PVSAlbumHostDelegate: remote controller terminated with error: %@"
+ "PVSAlbumHostDelegate: remote controller terminated."
+ "PVSAssetCollectionServiceViewController"
+ "PVSCreateSharedCollectionHostDelegate: remote controller terminated with error: %@"
+ "PVSCreateSharedCollectionHostDelegate: remote controller terminated."
+ "PVSCreateSharedCollectionServiceViewController"
+ "PVSCustomizeSharedCollectionHostDelegate: remote controller terminated with error: %@"
+ "PVSCustomizeSharedCollectionHostDelegate: remote controller terminated."
+ "PVSCustomizeSharedCollectionServiceViewController"
+ "PVSPostAssetsHostDelegate: remote controller terminated with error: %@"
+ "PVSPostAssetsHostDelegate: remote controller terminated."
+ "PVSPostAssetsServiceViewController"
+ "PVSSyncNowHostDelegate: remote controller terminated with error: %@"
+ "PVSSyncNowHostDelegate: remote controller terminated."
+ "PVSSyncNowServiceViewController"
+ "PhotosUI/PHPickerOverlay.swift"
+ "PhotosUI/PVSViewBridgeViewController.swift"
+ "Shared album asset posting"
+ "Shared album creation"
+ "Shared album customization"
+ "Unsupported RangeExpression type: "
+ "User does not have permission to add content to the shared album with identifier: "
+ "com.apple.PhotosViewService.hiddenAlbum.header"
+ "com.apple.PhotosViewService.recentlyDeletedAlbum.header"
+ "host PVSViewBridgeViewController was deallocated before the remote view could attach"
+ "maximumMemberCount == 0 || minimumMemberCount <= maximumMemberCount"
+ "minimumMemberCount > 0 || maximumMemberCount > 0"
+ "minimumMemberCount >= 0 && maximumMemberCount >= 0"
+ "pinnedItemIdentifiersKey"
- "%s: Error connecting to extension: %@"
- "%s: Failed to make XPC connection."
- "%s: Host view controller did activate."
- "%s: XPC Connection was interrupted."
- "%s: XPC Connection was invalidated."
- "%s: XPC connection failed with error: %@"
- "-[_PHPickerSuggestionGroup _initWithSuggestions:defaultSuggestionIndex:isForWallpaper:]"
- ".assetCollection"
- ".createSharedCollection"
- ".customizeSharedCollection"
- ".hiddenAlbum.header"
- ".recentlyDeletedAlbum.header"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lTqPjG/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PHPicker.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lTqPjG/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PUPickerFilter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lTqPjG/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PUPickerRemoteViewController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lTqPjG/Sources/Photos_UI/Projects/PhotosUI/PhotosUI/macOS+iOS/PHPicker/PUPickerUnavailableViewController.m"
- ": Connection doesn't exist; not attempting to connect to proxy."
- ": Proxy object doesn't conform to PVSAlbumProtocol."
- ": Proxy object doesn't conform to PVSCreateSharedCollectionProtocol."
- ": Proxy object doesn't conform to PVSCustomizeSharedCollectionProtocol."
- ": Proxy object doesn't conform to PVSPostAssetsProtocol."
- ": Proxy object doesn't conform to PVSSyncNowProtocol."
- ": Unexpected number of identities: "
- "Completion was called for posting to shared album with identifier: %s."
- "Invalid service name."
- "PhotosUI.PVSAlbumConcreteClient"
- "PhotosUI.PVSClientViewController"
- "PhotosUI.PVSCreateSharedCollectionConcreteClient"
- "PhotosUI.PVSCustomizeSharedCollectionConcreteClient"
- "PhotosUI.PVSPostAssetsConcreteClient"
- "PhotosUI.PVSSyncNowConcreteClient"
- "PhotosUI/PVSAlbumHostDelegate.swift"
- "PhotosUI/PVSClientViewController.swift"
- "PhotosUI/PVSCreateSharedCollectionHostDelegate.swift"
- "PhotosUI/PVSCustomizeSharedCollectionHostDelegate.swift"
- "PhotosUI/PVSInterfaceType.swift"
- "PhotosUI/PVSPostAssetsHostDelegate.swift"
- "PhotosUI/PVSSyncNowHostDelegate.swift"
- "PhotosUI/PVSUtilities.swift"
- "PhotosUI/PVSViewController.swift"
- "PhotosViewService as an angel isn't supported on Mac yet. See rdar://168168707."
- "Unexpected album view content value."
- "Unexpectedly nil album view content."
- "com.apple.photos.photosViewService"
- "didBecomeReadyForPresentation is unexpectedly nil; not presenting."
- "init(nibName:bundle:)"

```
