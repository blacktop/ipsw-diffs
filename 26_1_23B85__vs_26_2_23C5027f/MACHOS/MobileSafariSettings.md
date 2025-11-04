## MobileSafariSettings

> `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings`

```diff

-7622.2.11.10.8
-  __TEXT.__text: 0x52d04
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0xc580
-  __TEXT.__objc_methlist: 0x4354
-  __TEXT.__objc_methname: 0x110af
+7623.1.12.10.4
+  __TEXT.__text: 0x547b8
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_stubs: 0xc860
+  __TEXT.__objc_methlist: 0x43dc
+  __TEXT.__objc_methname: 0x1135f
   __TEXT.__objc_classname: 0x1070
-  __TEXT.__objc_methtype: 0x26b2
-  __TEXT.__const: 0x2d4
-  __TEXT.__cstring: 0x54f4
+  __TEXT.__objc_methtype: 0x2690
+  __TEXT.__const: 0x304
+  __TEXT.__cstring: 0x5564
   __TEXT.__ustring: 0x7dc
   __TEXT.__gcc_except_tab: 0x1f14
-  __TEXT.__oslogstring: 0x953
+  __TEXT.__oslogstring: 0x99b
   __TEXT.__constg_swiftt: 0x128
-  __TEXT.__swift5_typeref: 0x1ee
+  __TEXT.__swift5_typeref: 0x22c
   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_reflstr: 0x91
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_capture: 0x50
+  __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__unwind_info: 0x1560
+  __TEXT.__unwind_info: 0x15b8
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__auth_got: 0x768
-  __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__auth_ptr: 0xa8
-  __DATA_CONST.__const: 0x21f0
-  __DATA_CONST.__cfstring: 0x4ca0
+  __DATA_CONST.__auth_got: 0x820
+  __DATA_CONST.__got: 0xe10
+  __DATA_CONST.__auth_ptr: 0xc0
+  __DATA_CONST.__const: 0x2220
+  __DATA_CONST.__cfstring: 0x4d00
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_const: 0x7508
-  __DATA.__objc_selrefs: 0x4040
-  __DATA.__objc_ivar: 0x4b8
+  __DATA.__objc_const: 0x7548
+  __DATA.__objc_selrefs: 0x4108
+  __DATA.__objc_ivar: 0x4c0
   __DATA.__objc_data: 0x1c00
-  __DATA.__data: 0x1058
-  __DATA.__bss: 0x2a0
+  __DATA.__data: 0x1098
+  __DATA.__bss: 0x210
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 85FF0F79-518E-3648-9D82-078210F0735B
-  Functions: 1522
-  Symbols:   5310
-  CStrings:  4179
+  UUID: 960A8D8C-0E38-358F-AEB7-C5B3A66B9664
+  Functions: 1531
+  Symbols:   5337
+  CStrings:  4209
 
Symbols:
+ -[SafariAutoFillSettingsController _highlightSpecifier:]
+ -[SafariExtensionsSettingsController _didReceiveDeepLink:]
+ -[SafariExtensionsSettingsController _drillIntoExtensionWithIdentifier:]
+ -[SafariExtensionsSettingsController _extension:wasAddedToProfileWithIdentifier:]
+ -[SafariExtensionsSettingsController _extensionWasAdded:]
+ -[SafariExtensionsSettingsController _extensionWithComposedIdentifier:wasDiscoveredByProfileWithIdentifier:]
+ -[SafariExtensionsSettingsController _selectOrHighlightExtensionsIfNecessary:]
+ -[SafariExtensionsSettingsController _specifierForExtensionWrapper:]
+ -[SafariExtensionsSettingsController _wasExtensionDiscoveredByAllProfiles:]
+ -[SafariExtensionsSettingsController viewDidAppear:]
+ -[SafariSettingsController clearHistoryViewController:clearDataWithRequest:]
+ -[SafariSettingsListController viewWillAppear:]
+ GCC_except_table208
+ OBJC_IVAR_$_SafariExtensionsSettingsController._newExtensionIdentifierToDiscoveredProfiles
+ OBJC_IVAR_$_SafariExtensionsSettingsController._viewIsForeground
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_UIContentUnavailableConfiguration
+ _OBJC_CLASS_$_UIContentUnavailableView
+ _OBJC_CLASS_$_WBSUserDefinedContentBlockerSQLiteStore
+ _SafariAutofillSettingsDidReceiveDeepLinkNotification
+ _SafariAutofillSettingsHighlightSpecifierKey
+ _SafariExtensionsSettingsDidReceiveDeepLinkNotification
+ _SafariSettingsHighlightExtensionIdentifiersKey
+ _WBSExtensionWasAddedNotification
+ _WBSOSLogAutoFill
+ _WBSOSLogDownloads
+ _WBSOSLogExport
+ _WBSOSLogExtensions
+ _WBSOSLogImport
+ _WBSOSLogKeychain
+ _WBSOSLogSafariProfiles
+ _WBSOSLogWebExtensions
+ _WBSOSLogWebsiteData
+ _WBSSafariExtensionStateProfileIdentifier
+ __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.353
+ __76-[SafariSettingsController clearHistoryViewController:clearDataWithRequest:]_block_invoke.cold.1
+ __Block_copy
+ __Block_release
+ ___57-[SafariExtensionsSettingsController _extensionWasAdded:]_block_invoke
+ ___76-[SafariSettingsController clearHistoryViewController:clearDataWithRequest:]_block_invoke
+ ___78-[SafariExtensionsSettingsController _selectOrHighlightExtensionsIfNecessary:]_block_invoke
+ ___81-[SafariExtensionsSettingsController _extension:wasAddedToProfileWithIdentifier:]_block_invoke
+ ___81-[SafariExtensionsSettingsController _extension:wasAddedToProfileWithIdentifier:]_block_invoke_2
+ ___81-[SafariExtensionsSettingsController _extension:wasAddedToProfileWithIdentifier:]_block_invoke_3
+ ___81-[SafariExtensionsSettingsController _extension:wasAddedToProfileWithIdentifier:]_block_invoke_4
+ ___81-[SafariExtensionsSettingsController _extension:wasAddedToProfileWithIdentifier:]_block_invoke_5
+ ___block_descriptor_32_e8_v12?0B8l
+ ___block_descriptor_40_e8_32s_e28_v16?0"SFExtensionWrapper"8ls32l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s80l8s48l8s56l8s64l8s72l8
+ __block_literal_global.237
+ __block_literal_global.323
+ __block_literal_global.439
+ __block_literal_global.441
+ __block_literal_global.747
+ __block_literal_global.751
+ __swiftEmptyDictionarySingleton
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _objc_msgSend$_drillIntoExtensionWithIdentifier:
+ _objc_msgSend$_extension:wasAddedToProfileWithIdentifier:
+ _objc_msgSend$_extensionWithComposedIdentifier:wasDiscoveredByProfileWithIdentifier:
+ _objc_msgSend$_selectOrHighlightExtensionsIfNecessary:
+ _objc_msgSend$_specifierForExtensionWrapper:
+ _objc_msgSend$_wasExtensionDiscoveredByAllProfiles:
+ _objc_msgSend$afterDate
+ _objc_msgSend$allWebExtensionControllers
+ _objc_msgSend$beforeDate
+ _objc_msgSend$clearAllProfiles
+ _objc_msgSend$clearDistractionControlSettings
+ _objc_msgSend$closeAllTabs
+ _objc_msgSend$filledButtonConfiguration
+ _objc_msgSend$highlightSpecifierWithID:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$profileIdentifier
+ _objc_msgSend$resetDatabaseWithCompletionHandler:
+ _objc_msgSend$safari_arrayContainingObjectsOfClass:forKey:
+ _objc_msgSend$safari_isWebExtension
+ _objc_msgSend$scrollToRowAtIndexPath:atScrollPosition:animated:
+ _objc_msgSend$searchConfiguration
+ _objc_msgSend$setBaseBackgroundColor:
+ _objc_msgSend$setBaseForegroundColor:
+ _objc_msgSend$setCornerStyle:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$tableView:didSelectRowAtIndexPath:
+ _objc_msgSend$whiteColor
+ _objc_retain_x28
+ _swift_initStackObject
+ _swift_setDeallocating
+ _symbolic SaySSG
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC s11AnyHashableV
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ block_copy_helper.23
+ block_descriptor.25
+ block_destroy_helper.24
+ get_witness_table 8Settings05TupleA17ExperienceContentVyAA0acD0PAAE02onaC7OpenURL7performQrAA0acF9URLActionV6ResultVAI5InputVYacn_tFQOyAA0A4PaneVy19PreferencesExtended0M14ControllerViewVG_Qo__A2sOy7SwiftUI0P0PAAE07bridgedA33FeatureDescriptionNavigationTitleyQrqd__SyRd__lFQOyAR_SSQo_GQPGAaDHPyHC.26
- -[SafariSettingsController clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:]
- GCC_except_table207
- WBS_LOG_CHANNEL_PREFIXAutoFill.cold.1
- WBS_LOG_CHANNEL_PREFIXAutoFill.log
- WBS_LOG_CHANNEL_PREFIXAutoFill.onceToken
- WBS_LOG_CHANNEL_PREFIXDownloads.cold.1
- WBS_LOG_CHANNEL_PREFIXDownloads.log
- WBS_LOG_CHANNEL_PREFIXDownloads.onceToken
- WBS_LOG_CHANNEL_PREFIXExport.cold.1
- WBS_LOG_CHANNEL_PREFIXExport.log
- WBS_LOG_CHANNEL_PREFIXExport.onceToken
- WBS_LOG_CHANNEL_PREFIXExtensions.cold.1
- WBS_LOG_CHANNEL_PREFIXExtensions.log
- WBS_LOG_CHANNEL_PREFIXExtensions.onceToken
- WBS_LOG_CHANNEL_PREFIXImport.cold.1
- WBS_LOG_CHANNEL_PREFIXImport.log
- WBS_LOG_CHANNEL_PREFIXImport.onceToken
- WBS_LOG_CHANNEL_PREFIXKeychain.cold.1
- WBS_LOG_CHANNEL_PREFIXKeychain.log
- WBS_LOG_CHANNEL_PREFIXKeychain.onceToken
- WBS_LOG_CHANNEL_PREFIXSafariProfiles.cold.1
- WBS_LOG_CHANNEL_PREFIXSafariProfiles.log
- WBS_LOG_CHANNEL_PREFIXSafariProfiles.onceToken
- WBS_LOG_CHANNEL_PREFIXWebExtensions.cold.1
- WBS_LOG_CHANNEL_PREFIXWebExtensions.log
- WBS_LOG_CHANNEL_PREFIXWebExtensions.onceToken
- WBS_LOG_CHANNEL_PREFIXWebsiteData.cold.1
- WBS_LOG_CHANNEL_PREFIXWebsiteData.log
- WBS_LOG_CHANNEL_PREFIXWebsiteData.onceToken
- _OBJC_CLASS_$__UIContentUnavailableView
- _WBS_LOG_CHANNEL_PREFIXAutoFill
- _WBS_LOG_CHANNEL_PREFIXDownloads
- _WBS_LOG_CHANNEL_PREFIXExport
- _WBS_LOG_CHANNEL_PREFIXExtensions
- _WBS_LOG_CHANNEL_PREFIXImport
- _WBS_LOG_CHANNEL_PREFIXKeychain
- _WBS_LOG_CHANNEL_PREFIXSafariProfiles
- _WBS_LOG_CHANNEL_PREFIXWebExtensions
- _WBS_LOG_CHANNEL_PREFIXWebsiteData
- __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.354
- ___WBS_LOG_CHANNEL_PREFIXAutoFill_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXDownloads_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXExport_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXExtensions_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXImport_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXKeychain_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSafariProfiles_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebExtensions_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebsiteData_block_invoke
- __block_literal_global.10
- __block_literal_global.22
- __block_literal_global.238
- __block_literal_global.31
- __block_literal_global.324
- __block_literal_global.34
- __block_literal_global.37
- __block_literal_global.4
- __block_literal_global.40
- __block_literal_global.440
- __block_literal_global.442
- __block_literal_global.7
- __block_literal_global.748
- _objc_msgSend$initWithFrame:title:style:
- _objc_msgSend$isLockedPrivateBrowsingEnabled
- _objc_msgSend$isSafariProfilesEnabled
- _objc_msgSend$now
- _os_log_create
- get_witness_table 8Settings05TupleA17ExperienceContentVyAA0acD0PAAE02onaC7OpenURL7performQrAA0acF9URLActionV6ResultVAI5InputVYacn_tFQOyAA0A4PaneVy19PreferencesExtended0M14ControllerViewVG_Qo__A2sOy7SwiftUI0P0PAAE07bridgedA33FeatureDescriptionNavigationTitleyQrqd__SyRd__lFQOyAR_SSQo_GQPGAaDHPyHC.17
CStrings:
+ "@\"UIContentUnavailableView\""
+ "Failed to clear UserDefinedContentBlocker data for Distraction Control."
+ "HighlightExtensionIdentifiers"
+ "SafariAutofillSettingsDidReceiveDeepLinkNotification"
+ "SafariAutofillSettingsHighlightSpecifier"
+ "SafariExtensionsSettingsDidReceiveDeepLinkNotification"
+ "_didReceiveDeepLink:"
+ "_drillIntoExtensionWithIdentifier:"
+ "_extension:wasAddedToProfileWithIdentifier:"
+ "_extensionWasAdded:"
+ "_extensionWithComposedIdentifier:wasDiscoveredByProfileWithIdentifier:"
+ "_highlightSpecifier:"
+ "_newExtensionIdentifierToDiscoveredProfiles"
+ "_selectOrHighlightExtensionsIfNecessary:"
+ "_specifierForExtensionWrapper:"
+ "_viewIsForeground"
+ "_wasExtensionDiscoveredByAllProfiles:"
+ "afterDate"
+ "allWebExtensionControllers"
+ "beforeDate"
+ "clearAllProfiles"
+ "clearDistractionControlSettings"
+ "clearHistoryViewController:clearDataWithRequest:"
+ "closeAllTabs"
+ "filledButtonConfiguration"
+ "initWithConfiguration:"
+ "line.3.horizontal.decrease"
+ "profileIdentifier"
+ "resetDatabaseWithCompletionHandler:"
+ "safari_arrayContainingObjectsOfClass:forKey:"
+ "safari_isWebExtension"
+ "scrollToRowAtIndexPath:atScrollPosition:animated:"
+ "searchConfiguration"
+ "setBaseBackgroundColor:"
+ "setBaseForegroundColor:"
+ "setCornerStyle:"
+ "standardUserDefaults"
+ "v16@?0@\"SFExtensionWrapper\"8"
+ "v32@0:8@\"SFClearHistoryViewController\"16@\"SFBrowsingDataDeletionRequest\"24"
+ "viewDidAppear:"
+ "whiteColor"
- "@\"_UIContentUnavailableView\""
- "Keychain"
- "SafariProfiles"
- "WebExtensions"
- "WebsiteData"
- "clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:"
- "initWithFrame:title:style:"
- "isLockedPrivateBrowsingEnabled"
- "isSafariProfilesEnabled"
- "line.3.horizontal.decrease.circle"
- "line.3.horizontal.decrease.circle.fill"
- "now"
- "v56@0:8@\"SFClearHistoryViewController\"16@\"NSDate\"24@\"NSDate\"32@\"NSString\"40B48B52"
- "v56@0:8@16@24@32@40B48B52"

```
