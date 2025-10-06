## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-535.2.4.0.0
-  __TEXT.__text: 0xc8f30
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0xf63c
-  __TEXT.__const: 0xe14
-  __TEXT.__gcc_except_tab: 0x7e4
-  __TEXT.__cstring: 0x33a7
-  __TEXT.__oslogstring: 0x1af7
+535.4.4.0.0
+  __TEXT.__text: 0xcaa64
+  __TEXT.__auth_stubs: 0x1b50
+  __TEXT.__objc_methlist: 0xf754
+  __TEXT.__const: 0xee4
+  __TEXT.__gcc_except_tab: 0x7f8
+  __TEXT.__cstring: 0x36d7
+  __TEXT.__oslogstring: 0x1b4b
   __TEXT.__ustring: 0x102
   __TEXT.__dlopen_cstrs: 0x222
-  __TEXT.__constg_swiftt: 0x3ac
-  __TEXT.__swift5_typeref: 0xf40
-  __TEXT.__swift5_fieldmd: 0x230
-  __TEXT.__swift5_capture: 0x1f0
-  __TEXT.__swift5_types: 0x34
+  __TEXT.__constg_swiftt: 0x4ac
+  __TEXT.__swift5_typeref: 0xf60
+  __TEXT.__swift5_fieldmd: 0x270
+  __TEXT.__swift5_capture: 0x270
+  __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_reflstr: 0x1d6
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_assocty: 0xb0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3dbc
-  __TEXT.__eh_frame: 0x720
-  __TEXT.__objc_classname: 0x352a
-  __TEXT.__objc_methname: 0x28f2f
-  __TEXT.__objc_methtype: 0x7191
-  __TEXT.__objc_stubs: 0x205c0
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x23e8
-  __DATA_CONST.__objc_classlist: 0xb00
-  __DATA_CONST.__objc_catlist: 0x438
+  __TEXT.__unwind_info: 0x4150
+  __TEXT.__eh_frame: 0x9d8
+  __TEXT.__objc_classname: 0x356a
+  __TEXT.__objc_methname: 0x291ad
+  __TEXT.__objc_methtype: 0x71d2
+  __TEXT.__objc_stubs: 0x20720
+  __DATA_CONST.__got: 0x788
+  __DATA_CONST.__const: 0x2450
+  __DATA_CONST.__objc_classlist: 0xb28
+  __DATA_CONST.__objc_catlist: 0x440
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17450
-  __DATA_CONST.__objc_selrefs: 0x8f68
+  __DATA_CONST.__objc_const: 0x17540
+  __DATA_CONST.__objc_selrefs: 0x8fd8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x1978
+  __DATA_CONST.__objc_superrefs: 0x7f0
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__objc_const: 0xaf38
-  __AUTH_CONST.__const: 0x1468
+  __AUTH_CONST.__objc_const: 0xb0e0
+  __AUTH_CONST.__const: 0x15a0
   __AUTH_CONST.__cfstring: 0x30c0
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xd88
-  __AUTH.__objc_data: 0x2b60
-  __AUTH.__data: 0x208
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x1940
-  __DATA.__objc_superrefs: 0x7e8
-  __DATA.__objc_ivar: 0xd48
-  __DATA.__data: 0x28e8
-  __DATA.__bss: 0x650
+  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH.__objc_data: 0x2b98
+  __AUTH.__data: 0x2d8
+  __DATA.__objc_ivar: 0xd50
+  __DATA.__data: 0x2948
+  __DATA.__bss: 0x640
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x4468
-  __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__bss: 0x378
+  __DATA_DIRTY.__objc_data: 0x4750
+  __DATA_DIRTY.__data: 0xd0
+  __DATA_DIRTY.__bss: 0x390
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/WeatherKit.framework/WeatherKit
   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI
+  - /System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7B9C7163-B90F-3370-9AE2-A928D1E6AD4A
-  Functions: 5711
-  Symbols:   20522
-  CStrings:  8809
+  UUID: 6CC237B5-DA91-3B92-88B0-DFF78164DAC7
+  Functions: 5761
+  Symbols:   20612
+  CStrings:  8851
 
Symbols:
+ +[SearchUIShortcutsImage imageFromContexualActionIcon:]
+ -[BMDeviceWiFiAvailabilityStatus(SearchUIExtension) getEnabledStatusWithCompletion:]
+ -[SFRequestProductPageCommand(SearchUICommandClass) _searchUICommandHandlerClass]
+ -[SearchUICollectionViewCell hostedSnippetUIView]
+ -[SearchUICollectionViewCell setHostedSnippetUIView:]
+ -[SearchUIRequestProductPageCommandHandler destination]
+ -[SearchUIRequestProductPageCommandHandler performCommand:triggerEvent:environment:]
+ -[SearchUIShortcutsImage .cxx_destruct]
+ -[SearchUIShortcutsImage icon]
+ -[SearchUIShortcutsImage initWithSFImage:]
+ -[SearchUIShortcutsImage loadImageWithScale:isDarkStyle:completionHandler:]
+ -[SearchUIShortcutsImage setIcon:]
+ _OBJC_CLASS_$_BMDeviceWiFiAvailabilityStatus
+ _OBJC_CLASS_$_SFRequestProductPageCommand
+ _OBJC_CLASS_$_SFShortcutsImage
+ _OBJC_CLASS_$_SearchUIArchivedRowModel
+ _OBJC_CLASS_$_SearchUIContentConfigurator
+ _OBJC_CLASS_$_SearchUIRequestProductPageCommandHandler
+ _OBJC_CLASS_$_SearchUIRequestUserReportUtility
+ _OBJC_CLASS_$_SearchUIShortcutsImage
+ _OBJC_CLASS_$_SearchUIWeatherColor
+ _OBJC_CLASS_$_WFContextualActionIcon
+ _OBJC_CLASS_$__TtC8SearchUI32SearchUIAppDistributionUtilities
+ _OBJC_IVAR_$_SearchUICollectionViewCell._hostedSnippetUIView
+ _OBJC_IVAR_$_SearchUIShortcutsImage._icon
+ _OBJC_METACLASS_$_SearchUIArchivedRowModel
+ _OBJC_METACLASS_$_SearchUIContentConfigurator
+ _OBJC_METACLASS_$_SearchUIRequestProductPageCommandHandler
+ _OBJC_METACLASS_$_SearchUIRequestUserReportUtility
+ _OBJC_METACLASS_$_SearchUIShortcutsImage
+ _OBJC_METACLASS_$_SearchUIWeatherColor
+ _OBJC_METACLASS_$__TtC8SearchUI32SearchUIAppDistributionUtilities
+ _SSGetDisabledBundleSet
+ __DATA_SearchUIArchivedRowModel
+ __DATA_SearchUIContentConfigurator
+ __DATA_SearchUIRequestUserReportUtility
+ __DATA_SearchUIWeatherColor
+ __DATA__TtC8SearchUI32SearchUIAppDistributionUtilities
+ __IVARS_SearchUIArchivedRowModel
+ __METACLASS_DATA_SearchUIArchivedRowModel
+ __METACLASS_DATA_SearchUIContentConfigurator
+ __METACLASS_DATA_SearchUIRequestUserReportUtility
+ __METACLASS_DATA_SearchUIWeatherColor
+ __METACLASS_DATA__TtC8SearchUI32SearchUIAppDistributionUtilities
+ __OBJC_$_CATEGORY_BMDeviceWiFiAvailabilityStatus_$_SearchUIExtension
+ __OBJC_$_CATEGORY_SFRequestProductPageCommand_$_SearchUICommandClass
+ __OBJC_$_CLASS_METHODS_SearchUIContentConfigurator
+ __OBJC_$_CLASS_METHODS_SearchUIRequestUserReportHandler
+ __OBJC_$_CLASS_METHODS_SearchUIRequestUserReportUtility
+ __OBJC_$_CLASS_METHODS_SearchUIShortcutsImage
+ __OBJC_$_CLASS_METHODS__TtC8SearchUI32SearchUIAppDistributionUtilities
+ __OBJC_$_INSTANCE_METHODS_BMDeviceWiFiAvailabilityStatus(SearchUIExtension)
+ __OBJC_$_INSTANCE_METHODS_SFRequestProductPageCommand(SearchUICommandClass)
+ __OBJC_$_INSTANCE_METHODS_SearchUIArchivedRowModel
+ __OBJC_$_INSTANCE_METHODS_SearchUIContentConfigurator
+ __OBJC_$_INSTANCE_METHODS_SearchUIRequestProductPageCommandHandler
+ __OBJC_$_INSTANCE_METHODS_SearchUIRequestUserReportHandler
+ __OBJC_$_INSTANCE_METHODS_SearchUIRequestUserReportUtility
+ __OBJC_$_INSTANCE_METHODS_SearchUIShortcutsImage
+ __OBJC_$_INSTANCE_METHODS_SearchUIWeatherColor
+ __OBJC_$_INSTANCE_METHODS_SearchUIWeatherColorGenerator
+ __OBJC_$_INSTANCE_METHODS__TtC8SearchUI32SearchUIAppDistributionUtilities
+ __OBJC_$_INSTANCE_VARIABLES_SearchUIShortcutsImage
+ __OBJC_$_PROP_LIST_SearchUICommandButton.80
+ __OBJC_$_PROP_LIST_SearchUIShortcutsImage
+ __OBJC_CLASS_RO_$_SearchUIRequestProductPageCommandHandler
+ __OBJC_CLASS_RO_$_SearchUIShortcutsImage
+ __OBJC_METACLASS_RO_$_SearchUIRequestProductPageCommandHandler
+ __OBJC_METACLASS_RO_$_SearchUIShortcutsImage
+ __PROPERTIES_SearchUIArchivedRowModel
+ ___70-[SearchUISearchInAppHandler performCommand:triggerEvent:environment:]_block_invoke
+ ___75-[SearchUIShortcutsImage loadImageWithScale:isDarkStyle:completionHandler:]_block_invoke
+ ___75-[SearchUIShortcutsImage loadImageWithScale:isDarkStyle:completionHandler:]_block_invoke_2
+ ___84-[SearchUIRequestProductPageCommandHandler performCommand:triggerEvent:environment:]_block_invoke
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e44_v24?0"WFContextualActionIcon"8"NSError"16ls32l8s40l8
+ _objc_msgSend$distributorBundleIdentifier
+ _objc_msgSend$generateHexColorsWithSfColor:completionHandler:
+ _objc_msgSend$initWithLNPropertyIdentifier:displayStyle:
+ _objc_msgSend$isWiFiSwitchOn
+ _objc_msgSend$lnPropertyIdentifier
+ _objc_msgSend$loadLNPropertyImageWithCompletion:
+ _objc_msgSend$queryContext
+ _objc_msgSend$requestProductPageWithDistributorID:itemID:versionID:completionHandler:
+ _objc_msgSend$requestSearchPageWithDistributorID:searchString:completionHandler:
+ _objc_msgSend$searchInAppType
+ _objc_msgSend$setDisableBundles:
+ _objc_msgSend$versionIdentifier
+ _swift_deletedAsyncMethodErrorTu
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _symbolic So14SFWeatherColorC
+ _symbolic So8NSStringC
+ _symbolic _____ 8SearchUI0A14UIWeatherColorC
+ _symbolic _____ 8SearchUI0A23UIRFCardSectionRowModelC
+ _symbolic _____ 8SearchUI0A26UIAppDistributionUtilitiesC
+ _symbolic _____ 8SearchUI24RequestUserReportUtilityC
+ _symbolic _____ s6UInt64V
+ _symbolic _____XMo 8SearchUI0A26UIAppDistributionUtilitiesC
- -[BMDeviceWiFi(SearchUIExtension) getEnabledStatusWithCompletion:]
- -[SearchUIBonusSPIAppTopHitAsyncSectionLoader imageFromContexualActionIcon:]
- _OBJC_CLASS_$_BMDeviceWiFi
- _OBJC_CLASS_$__TtC8SearchUI24SearchUIArchivedRowModel
- _OBJC_CLASS_$__TtC8SearchUI27SearchUIContentConfigurator
- _OBJC_METACLASS_$__TtC8SearchUI24SearchUIArchivedRowModel
- _OBJC_METACLASS_$__TtC8SearchUI27SearchUIContentConfigurator
- __DATA__TtC8SearchUI24SearchUIArchivedRowModel
- __DATA__TtC8SearchUI27SearchUIContentConfigurator
- __IVARS__TtC8SearchUI24SearchUIArchivedRowModel
- __METACLASS_DATA__TtC8SearchUI24SearchUIArchivedRowModel
- __METACLASS_DATA__TtC8SearchUI27SearchUIContentConfigurator
- __OBJC_$_CATEGORY_BMDeviceWiFi_$_SearchUIExtension
- __OBJC_$_CLASS_METHODS_SearchUIRequestUserReportHandler(SearchUI)
- __OBJC_$_CLASS_METHODS__TtC8SearchUI27SearchUIContentConfigurator
- __OBJC_$_INSTANCE_METHODS_BMDeviceWiFi(SearchUIExtension)
- __OBJC_$_INSTANCE_METHODS_SearchUIRequestUserReportHandler(SearchUI)
- __OBJC_$_INSTANCE_METHODS_SearchUIWeatherColorGenerator(SearchUI)
- __OBJC_$_INSTANCE_METHODS__TtC8SearchUI24SearchUIArchivedRowModel
- __OBJC_$_INSTANCE_METHODS__TtC8SearchUI27SearchUIContentConfigurator
- __OBJC_$_PROP_LIST_SearchUICommandButton.79
- __OBJC_CLASS_PROTOCOLS_$_BMDeviceWiFi(SearchUIExtension)
- __PROPERTIES__TtC8SearchUI24SearchUIArchivedRowModel
- _objc_msgSend$generateHexColorsWithCompletionHandler:
- _swift_getObjCClassFromMetadata
- _symbolic So29SearchUIWeatherColorGeneratorC
CStrings:
+ "\x12\"\x13\x12\x13"
+ "@\"WFContextualActionIcon\""
+ "@\"_UIConstraintBasedLayoutHostingView\""
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "SearchUIRequestProductPageCommandHandler"
+ "SearchUIRequestUserReportUtility"
+ "SearchUIShortcutsImage"
+ "SearchUIShortcutsImage failed to load image with property identifier: %@, error: %@"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<PXMemoryAssetsActionFactory>\",?,R,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"WFContextualActionIcon\",&,N,V_icon"
+ "T@\"_UIConstraintBasedLayoutHostingView\",&,N,V_hostedSnippetUIView"
+ "TB,?,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_TtC8SearchUI32SearchUIAppDistributionUtilities"
+ "_hostedSnippetUIView"
+ "_icon"
+ "distributorBundleIdentifier"
+ "generateHexColorsWithSfColor:completionHandler:"
+ "hostedSnippetUIView"
+ "hostedSnippetUIViewForFor:rowModel:interactionDelegate:"
+ "initWithLNPropertyIdentifier:displayStyle:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isWiFiSwitchOn"
+ "lnPropertyIdentifier"
+ "loadLNPropertyImageWithCompletion:"
+ "queryContext"
+ "requestProductPageWithDistributorID:itemID:versionID:completionHandler:"
+ "requestSearchPageWithDistributorID:searchString:completionHandler:"
+ "searchInAppType"
+ "setDisableBundles:"
+ "setHostedSnippetUIView:"
+ "v24@?0@\"WFContextualActionIcon\"8@\"NSError\"16"
+ "v32@0:8@\"SFWeatherColor\"16@?<v@?@\"NSArray\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSString\"16Q24Q32@?<v@?@\"NSError\">40"
+ "versionIdentifier"
- "\x12\"\x12\x12\x13"
- "SearchUIRFCardSectionRowModel"
- "T@\"<PXMemoryAssetsActionFactory>\",R,N"
- "_TtC8SearchUI24SearchUIArchivedRowModel"
- "_TtC8SearchUI27SearchUIContentConfigurator"
- "generateHexColorsWithCompletionHandler:"
- "v24@0:8@?<v@?@\"NSArray\">16"

```
