## AssistantSettingsSupport

> `/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport`

```diff

-3302.13.3.1.1
-  __TEXT.__text: 0x22948
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x1a64
-  __TEXT.__const: 0x30
+3304.61.1.0.0
+  __TEXT.__text: 0x23d44
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x1be4
+  __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x598
-  __TEXT.__cstring: 0x3e46
-  __TEXT.__oslogstring: 0xd00
+  __TEXT.__cstring: 0x3ffd
+  __TEXT.__oslogstring: 0xa8a
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x420
-  __TEXT.__unwind_info: 0x900
-  __TEXT.__objc_classname: 0x58a
-  __TEXT.__objc_methname: 0x6cb4
-  __TEXT.__objc_methtype: 0xaa3
-  __TEXT.__objc_stubs: 0x5300
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0xa48
-  __DATA_CONST.__objc_classlist: 0x118
+  __TEXT.__unwind_info: 0x944
+  __TEXT.__objc_classname: 0x5ef
+  __TEXT.__objc_methname: 0x7106
+  __TEXT.__objc_methtype: 0xa72
+  __TEXT.__objc_stubs: 0x5640
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0xa20
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28f8
-  __DATA_CONST.__objc_selrefs: 0x1a28
-  __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0xcf0
-  __AUTH_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_const: 0x2a60
+  __DATA_CONST.__objc_selrefs: 0x1af8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__objc_const: 0xe58
+  __AUTH_CONST.__cfstring: 0x32e0
+  __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x390
-  __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x430
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x240
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C77585A1-C5CC-364E-97A4-EC70CFBC0750
-  Functions: 739
-  Symbols:   3085
-  CStrings:  2200
+  UUID: F9024D6E-2DA4-39CF-9AD1-ECFB3059A66C
+  Functions: 765
+  Symbols:   3191
+  CStrings:  2265
 
Symbols:
+ +[AssistantDetailListController bundle]
+ +[AssistantMultilingualDetailController bundle]
+ -[AssistantController _askSiriUseOutOfSpaceFooterTextWithGroupSpecifier:withSpaceRequired:]
+ -[AssistantController _updateSiriFooterGroup:withStatus:]
+ -[AssistantController _updateSiriFooterGroup:withStatus:].cold.1
+ -[AssistantController detailTextForLanguageSpecifierFromTitles:]
+ -[AssistantController multilingualResponseLanguageVariants]
+ -[AssistantDetailListController .cxx_destruct]
+ -[AssistantDetailListController checkmarkImage]
+ -[AssistantDetailListController init]
+ -[AssistantDetailListController setChecked:forSpecifier:]
+ -[AssistantDetailListController setCheckmarkImage:]
+ -[AssistantDetailListController setTransparentImage:]
+ -[AssistantDetailListController transparentImage]
+ -[AssistantLanguageController _itemsFromParent]
+ -[AssistantLanguageController listItemSelected:]
+ -[AssistantLanguageController multilingualResponseLanguageVariants]
+ -[AssistantLanguageController reloadSpecifier:]
+ -[AssistantLanguageController setMultilingualResponseLanguageVariants:]
+ -[AssistantLanguageController setParentController:]
+ -[AssistantLanguageController specifiers]
+ -[AssistantLanguageController tableView:didSelectRowAtIndexPath:]
+ -[AssistantLanguageController updateDetailedTextLabelForSpecifier:]
+ -[AssistantLanguageController updateSelectionToCurrentAssistantLanguageAndScrollToVisible:]
+ -[AssistantLanguageController viewWillAppear:]
+ -[AssistantMultilingualDetailController .cxx_destruct]
+ -[AssistantMultilingualDetailController _addLinkAttributesToHeaderSpecifier]
+ -[AssistantMultilingualDetailController _languageSpecificLocalizedStringForKey:]
+ -[AssistantMultilingualDetailController _learnMoreTapped]
+ -[AssistantMultilingualDetailController _refreshFooterForSpecifier:]
+ -[AssistantMultilingualDetailController _syncSelectionToPrefs]
+ -[AssistantMultilingualDetailController listItemSelected:]
+ -[AssistantMultilingualDetailController specifiers]
+ -[AssistantMultilingualDetailController tableView:didSelectRowAtIndexPath:]
+ -[AssistantMultilingualDetailController viewDidDisappear:]
+ -[AssistantMultilingualDetailController viewWillAppear:]
+ -[AssistantSubtitleTableViewCell canReload]
+ -[AssistantSubtitleTableViewCell refreshCellContentsWithSpecifier:]
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table150
+ GCC_except_table161
+ GCC_except_table170
+ GCC_except_table3
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table79
+ GCC_except_table9
+ OBJC_IVAR_$_AssistantDetailListController._groupSpecifier
+ OBJC_IVAR_$_AssistantDetailListController._previousSelectedSpecifier
+ OBJC_IVAR_$_AssistantDetailListController._supportsMultilingualResponses
+ OBJC_IVAR_$_PSViewController._specifier
+ _OBJC_CLASS_$_AFFeatureFlags
+ _OBJC_CLASS_$_AssistantDetailListController
+ _OBJC_CLASS_$_AssistantMultilingualDetailController
+ _OBJC_CLASS_$_AssistantSubtitleTableViewCell
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_UIFontDescriptor
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_IVAR_$_AssistantDetailListController._checkmarkImage
+ _OBJC_IVAR_$_AssistantDetailListController._transparentImage
+ _OBJC_IVAR_$_AssistantLanguageController._multilingualResponseLanguageVariants
+ _OBJC_IVAR_$_AssistantMultilingualDetailController._headerSpecifier
+ _OBJC_IVAR_$_AssistantMultilingualDetailController._preferEnglishOnlySpecifier
+ _OBJC_IVAR_$_AssistantMultilingualDetailController._preferMultilingualSpecifier
+ _OBJC_IVAR_$_AssistantMultilingualDetailController._setterValue
+ _OBJC_METACLASS_$_AssistantDetailListController
+ _OBJC_METACLASS_$_AssistantMultilingualDetailController
+ _OBJC_METACLASS_$_AssistantSubtitleTableViewCell
+ _PSIsRadioGroupKey
+ _PSTableCellSubtitleTextKey
+ __OBJC_$_CLASS_METHODS_AssistantDetailListController
+ __OBJC_$_CLASS_METHODS_AssistantMultilingualDetailController
+ __OBJC_$_INSTANCE_METHODS_AssistantDetailListController
+ __OBJC_$_INSTANCE_METHODS_AssistantMultilingualDetailController
+ __OBJC_$_INSTANCE_METHODS_AssistantSubtitleTableViewCell
+ __OBJC_$_INSTANCE_VARIABLES_AssistantDetailListController
+ __OBJC_$_INSTANCE_VARIABLES_AssistantMultilingualDetailController
+ __OBJC_$_PROP_LIST_AssistantDetailListController
+ __OBJC_$_PROP_LIST_AssistantLanguageController
+ __OBJC_CLASS_RO_$_AssistantDetailListController
+ __OBJC_CLASS_RO_$_AssistantMultilingualDetailController
+ __OBJC_CLASS_RO_$_AssistantSubtitleTableViewCell
+ __OBJC_METACLASS_RO_$_AssistantDetailListController
+ __OBJC_METACLASS_RO_$_AssistantMultilingualDetailController
+ __OBJC_METACLASS_RO_$_AssistantSubtitleTableViewCell
+ ___34+[AssistantVoiceController bundle]_block_invoke
+ ___57-[AssistantMultilingualDetailController _learnMoreTapped]_block_invoke
+ ___91-[AssistantController _createVoiceSelectionCompletionForSpecifier:recognitionLanguageCode:]_block_invoke.546
+ ___block_literal_global.151
+ ___block_literal_global.249
+ ___block_literal_global.252
+ ___block_literal_global.500
+ ___block_literal_global.517
+ _bundle.onceToken
+ _bundle.sAssistantMultilingualBundle
+ _objc_msgSend$_addLinkAttributesToHeaderSpecifier
+ _objc_msgSend$_askSiriUseOutOfSpaceFooterTextWithGroupSpecifier:withSpaceRequired:
+ _objc_msgSend$_itemsFromParent
+ _objc_msgSend$_languageSpecificLocalizedStringForKey:
+ _objc_msgSend$_syncSelectionToPrefs
+ _objc_msgSend$_updateSiriFooterGroup:withStatus:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$cellType
+ _objc_msgSend$checkmarkImage
+ _objc_msgSend$clearColor
+ _objc_msgSend$configurationByApplyingConfiguration:
+ _objc_msgSend$configurationWithFont:scale:
+ _objc_msgSend$configurationWithHierarchicalColor:
+ _objc_msgSend$currentAssetStatus
+ _objc_msgSend$defaultFontDescriptorWithTextStyle:
+ _objc_msgSend$detailTextForLanguageSpecifierFromTitles:
+ _objc_msgSend$fontDescriptorWithSymbolicTraits:
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$grayColor
+ _objc_msgSend$imageView
+ _objc_msgSend$isMultilingualResponseVariantSelectorEnabled
+ _objc_msgSend$listItemSelected:
+ _objc_msgSend$multilingualResponseEnabledForLanguage:
+ _objc_msgSend$multilingualResponseLanguageVariants
+ _objc_msgSend$openSensitiveURL:withOptions:
+ _objc_msgSend$performSetterWithValue:
+ _objc_msgSend$scrollToRowAtIndexPath:atScrollPosition:animated:
+ _objc_msgSend$setAutoRetryEnabled:
+ _objc_msgSend$setCellType:
+ _objc_msgSend$setChecked:forSpecifier:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setMultilingualResponseEnabled:forLanguage:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$setValues:titles:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _objc_msgSend$transparentImage
+ _objc_msgSend$updateDetailedTextLabelForSpecifier:
+ _objc_msgSend$updateSelectionToCurrentAssistantLanguageAndScrollToVisible:
+ _objc_msgSend$values
+ _objc_opt_respondsToSelector
- +[AssistantCell defaultCellHeight]
- -[AssistantController _askSiriUseOutOfSpaceFooterTextWithGroupSpecifier:withSpaceRequiredText:]
- -[AssistantController _downloadSiriAssets]
- -[AssistantController _updateSiriFooterGroup:forceReload:]
- -[AssistantController _updateSiriFooterGroup:forceReload:].cold.1
- -[AssistantController _updateSiriFooterGroup:forceReload:].cold.2
- -[AssistantController assistantEnabledDidChange:]
- -[AssistantController assistantLanguageDidChange:]
- -[AssistantController downloadSiriAssets]
- -[AssistantController networkPathChangeSatisfied:isExpensive:]
- -[AssistantController retryDownloadSiriAssetsWithDelay:]
- GCC_except_table129
- GCC_except_table137
- GCC_except_table141
- GCC_except_table146
- GCC_except_table159
- GCC_except_table177
- GCC_except_table44
- GCC_except_table5
- GCC_except_table50
- GCC_except_table78
- _AFDeviceSupportsSiriUOD
- _AFShouldRunAsrOnServerForUOD
- _CFAbsoluteTimeGetCurrent
- _CPFSSizeStrings
- _OBJC_CLASS_$_CLLocationManager
- _OBJC_CLASS_$_UAFAssetStatus
- _OBJC_IVAR_$_AssistantController._assetRetryLimit
- _OBJC_IVAR_$_AssistantController._assetState
- _OBJC_IVAR_$_AssistantController._lastDownloadTimestamp
- _OBJC_IVAR_$_AssistantController._utilityQueue
- _OBJC_METACLASS_$_PSListItemsController
- _UITableViewAutomaticDimension
- ___41-[AssistantController downloadSiriAssets]_block_invoke
- ___56-[AssistantController retryDownloadSiriAssetsWithDelay:]_block_invoke
- ___56-[AssistantController retryDownloadSiriAssetsWithDelay:]_block_invoke.681
- ___91-[AssistantController _createVoiceSelectionCompletionForSpecifier:recognitionLanguageCode:]_block_invoke.548
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.245
- ___block_literal_global.248
- ___block_literal_global.502
- ___block_literal_global.519
- _dispatch_after
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_create
- _objc_msgSend$_askSiriUseOutOfSpaceFooterTextWithGroupSpecifier:withSpaceRequiredText:
- _objc_msgSend$_downloadSiriAssets
- _objc_msgSend$_updateSiriFooterGroup:forceReload:
- _objc_msgSend$assetStatus
- _objc_msgSend$authorizationStatusForBundle:
- _objc_msgSend$getAssistantLanguageIfAvailableSync
- _objc_msgSend$mockAssetStatus
- _objc_msgSend$refreshUAFAssetStatusAsync
- _objc_msgSend$retryDownloadSiriAssetsWithDelay:
- _objc_msgSend$setAuthorizationStatusByType:forBundle:
- _objc_msgSend$setColor:
- _objc_msgSend$siriLanguage
- _objc_msgSend$stringFromUAFAssetState:
- _objc_msgSend$understandingOnDeviceAssetsAvailable
CStrings:
+ "\x0f\x1e\x11"
+ "\x14"
+ "%@_%@"
+ "-[AssistantController _updateSiriFooterGroup:withStatus:]"
+ "@\"UIImage\""
+ "AssistantDetailListController"
+ "AssistantMultilingualDetail"
+ "AssistantMultilingualDetailController"
+ "AssistantSubtitleTableViewCell"
+ "LIST_ITEMS_GROUP_SPECIFIER"
+ "MULTILINGUAL_DETAIL_ENGLISH_ONLY_%@"
+ "MULTILINGUAL_DETAIL_FOOTER_ENGLISH_ONLY"
+ "MULTILINGUAL_DETAIL_FOOTER_MIXED"
+ "MULTILINGUAL_DETAIL_GROUP_ID"
+ "MULTILINGUAL_DETAIL_HEADER"
+ "MULTILINGUAL_DETAIL_HEADER_GROUP_ID"
+ "MULTILINGUAL_DETAIL_HEADER_LINK_TEXT"
+ "MULTILINGUAL_DETAIL_HEADER_LINK_URL"
+ "MULTILINGUAL_DETAIL_MIXED_%@"
+ "MULTILINGUAL_DETAIL_OPTION_ENGLISH_ONLY"
+ "MULTILINGUAL_DETAIL_OPTION_ENGLISH_ONLY_ID"
+ "MULTILINGUAL_DETAIL_OPTION_MIXED"
+ "MULTILINGUAL_DETAIL_OPTION_MIXED_ID"
+ "MULTILINGUAL_DETAIL_TOP_LEVEL_MIXED_%@"
+ "T@\"NSArray\",&,N,V_multilingualResponseLanguageVariants"
+ "T@\"NSArray\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIImage\",&,N,V_checkmarkImage"
+ "T@\"UIImage\",&,N,V_transparentImage"
+ "_addLinkAttributesToHeaderSpecifier"
+ "_askSiriUseOutOfSpaceFooterTextWithGroupSpecifier:withSpaceRequired:"
+ "_checkmarkImage"
+ "_headerSpecifier"
+ "_itemsFromParent"
+ "_languageSpecificLocalizedStringForKey:"
+ "_learnMoreTapped"
+ "_multilingualResponseLanguageVariants"
+ "_preferEnglishOnlySpecifier"
+ "_preferMultilingualSpecifier"
+ "_previousSelectedSpecifier"
+ "_setterValue"
+ "_supportsMultilingualResponses"
+ "_syncSelectionToPrefs"
+ "_transparentImage"
+ "_updateSiriFooterGroup:withStatus:"
+ "arrayWithCapacity:"
+ "cellType"
+ "checkmark"
+ "checkmarkImage"
+ "clearColor"
+ "configurationByApplyingConfiguration:"
+ "configurationWithFont:scale:"
+ "configurationWithHierarchicalColor:"
+ "currentAssetStatus"
+ "defaultFontDescriptorWithTextStyle:"
+ "detailTextForLanguageSpecifierFromTitles:"
+ "en-IN"
+ "fontDescriptorWithSymbolicTraits:"
+ "fontWithDescriptor:size:"
+ "grayColor"
+ "imageView"
+ "isMultilingualResponseVariantSelectorEnabled"
+ "listItemSelected:"
+ "multilingualResponseEnabledForLanguage:"
+ "multilingualResponseLanguageVariants"
+ "openSensitiveURL:withOptions:"
+ "performSetterWithValue:"
+ "scrollToRowAtIndexPath:atScrollPosition:animated:"
+ "setAutoRetryEnabled:"
+ "setCellType:"
+ "setChecked:forSpecifier:"
+ "setCheckmarkImage:"
+ "setImage:"
+ "setMultilingualResponseEnabled:forLanguage:"
+ "setMultilingualResponseLanguageVariants:"
+ "setTextColor:"
+ "setTransparentImage:"
+ "setValues:titles:"
+ "setWithObjects:"
+ "systemImageNamed:withConfiguration:"
+ "transparentImage"
+ "updateDetailedTextLabelForSpecifier:"
+ "updateSelectionToCurrentAssistantLanguageAndScrollToVisible:"
+ "values"
- "\x0f\x1e2"
- "%s #settings Asset state remains %@"
- "%s #settings Changing asset state to %@ with value %d"
- "%s #settings Enqueue retry after a %f seconds..."
- "%s #settings Forcing display state to %@ (enabled:%d, hybridUOD:%d, fullUOD:%d)"
- "%s #settings Forcing display state to %@ due to UOD available"
- "%s #settings Retry number %d Skipping too many failed asset download retries"
- "%s #settings Retry number %d for failed asset download"
- "%s #settings Retrying download now..."
- "%s #settings Skip retry due nil language"
- "%s #settings Skipping download due to too many retries (curr:%f prev:%f interval:%f)"
- "%s #settings Using mock asset state %@ with value %d"
- "-[AssistantController _downloadSiriAssets]"
- "-[AssistantController _updateSiriFooterGroup:forceReload:]"
- "-[AssistantController retryDownloadSiriAssetsWithDelay:]_block_invoke"
- "@\"NSObject<OS_dispatch_queue>\""
- "I"
- "_askSiriUseOutOfSpaceFooterTextWithGroupSpecifier:withSpaceRequiredText:"
- "_assetRetryLimit"
- "_assetState"
- "_downloadSiriAssets"
- "_lastDownloadTimestamp"
- "_updateSiriFooterGroup:forceReload:"
- "_utilityQueue"
- "assetStatus"
- "authorizationStatusForBundle:"
- "com.apple.Preferences.UtilityQueue"
- "d"
- "defaultCellHeight"
- "getAssistantLanguageIfAvailableSync"
- "mockAssetStatus"
- "refreshUAFAssetStatusAsync"
- "retryDownloadSiriAssetsWithDelay:"
- "setAuthorizationStatusByType:forBundle:"
- "setColor:"
- "siriLanguage"
- "stringFromUAFAssetState:"
- "understandingOnDeviceAssetsAvailable"
- "v24@0:8d16"
- "v32@0:8@16Q24"

```
