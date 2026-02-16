## MobileSafariSettings

> `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings`

```diff

-7623.2.7.10.4
-  __TEXT.__text: 0x547bc
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_stubs: 0xc840
-  __TEXT.__objc_methlist: 0x43dc
-  __TEXT.__objc_methname: 0x1132c
-  __TEXT.__objc_classname: 0x1070
-  __TEXT.__objc_methtype: 0x2690
+7624.1.11.10.3
+  __TEXT.__text: 0x59f54
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_stubs: 0xcdc0
+  __TEXT.__objc_methlist: 0x44ec
+  __TEXT.__objc_methname: 0x119ee
+  __TEXT.__objc_classname: 0x1164
+  __TEXT.__objc_methtype: 0x26de
   __TEXT.__const: 0x304
-  __TEXT.__cstring: 0x5524
+  __TEXT.__cstring: 0x55b6
   __TEXT.__ustring: 0x7dc
-  __TEXT.__gcc_except_tab: 0x1f0c
-  __TEXT.__oslogstring: 0x99b
+  __TEXT.__gcc_except_tab: 0x1f34
+  __TEXT.__oslogstring: 0xa2b
   __TEXT.__constg_swiftt: 0x128
-  __TEXT.__swift5_typeref: 0x22c
-  __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_reflstr: 0x91
+  __TEXT.__swift5_typeref: 0x256
+  __TEXT.__swift5_fieldmd: 0x80
+  __TEXT.__swift5_reflstr: 0xa1
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__unwind_info: 0x15b8
+  __TEXT.__unwind_info: 0x16b0
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__auth_got: 0x820
-  __DATA_CONST.__got: 0xe18
-  __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x2230
+  __DATA_CONST.__auth_got: 0x810
+  __DATA_CONST.__got: 0xe50
+  __DATA_CONST.__auth_ptr: 0xc8
+  __DATA_CONST.__const: 0x2428
   __DATA_CONST.__cfstring: 0x4ce0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_const: 0x7548
-  __DATA.__objc_selrefs: 0x4100
-  __DATA.__objc_ivar: 0x4c0
-  __DATA.__objc_data: 0x1c00
+  __DATA.__objc_const: 0x7678
+  __DATA.__objc_selrefs: 0x4230
+  __DATA.__objc_ivar: 0x4d0
+  __DATA.__objc_data: 0x1c50
   __DATA.__data: 0x1098
-  __DATA.__bss: 0x210
+  __DATA.__bss: 0x220
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
+  - /System/Library/Frameworks/BrowserKit.framework/BrowserKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
-  - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3C22E02C-0128-32DB-8527-2C3F9AACC36F
-  Functions: 1531
-  Symbols:   5342
-  CStrings:  4206
+  UUID: D295D89B-7401-3443-8F1C-38EDE06BE8C9
+  Functions: 1593
+  Symbols:   5492
+  CStrings:  4261
 
Symbols:
+ -[SafariAutoFillSettingsController _headerGroupCellFooterText]
+ -[SafariDownloadsSettingsController _locationContainingItem:]
+ -[SafariDownloadsSettingsController _setDefaultDownloadsLocationItemURL:]
+ -[SafariDownloadsSettingsController _updateSelectedFolderWithItem:]
+ -[SafariSettingsBrowsingDataExportController _exportReadingListToFileWithURL:completionHandler:]
+ -[SafariSettingsBrowsingDataExportController _extensionsToBeExported]
+ -[SafariSettingsBrowsingDataExportController _numberOfReadingListItemsToBeExported]
+ -[SafariSettingsBrowsingDataExportController exportBookmarksWithBlock:]
+ -[SafariSettingsBrowsingDataExportController exportExtensionsWithBlock:]
+ -[SafariSettingsBrowsingDataExportController exportHistoryWithBlock:]
+ -[SafariSettingsBrowsingDataExportController exportReadingListWithBlock:]
+ -[SafariSettingsBrowsingDataImportController _computeNumberOfReadingListItemsToBeImportedFromURL:completionHandler:]
+ -[SafariSettingsBrowsingDataImportController _importReadingListFromURL:completionHandler:]
+ -[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]
+ -[SafariSettingsController _showImportSheetWithCompletionHandler:]
+ -[SafariSettingsController isExportButtonDisabled:]
+ -[SafariSettingsController isImportButtonDisabled:]
+ -[SafariSettingsController setSpecifier:]
+ -[SafariSettingsController toggleExportButtonEnabledState]
+ -[SafariSettingsController toggleImportButtonEnabledState]
+ -[SafariSettingsExportRequest .cxx_destruct]
+ -[SafariSettingsExportRequest setToken:]
+ -[SafariSettingsExportRequest token]
+ -[SafariSettingsListController createSpecifiers]
+ -[SafariSettingsListController specifiers]
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table241
+ GCC_except_table61
+ GCC_except_table98
+ OBJC_IVAR_$_SafariSettingsController._browserDataExchangeExportManager
+ OBJC_IVAR_$_SafariSettingsController._exportButtonDisabled
+ OBJC_IVAR_$_SafariSettingsController._exportRequest
+ OBJC_IVAR_$_SafariSettingsController._importButtonDisabled
+ OBJC_IVAR_$_SafariSettingsExportRequest._token
+ _OBJC_CLASS_$_BEBrowserDataBookmark
+ _OBJC_CLASS_$_BEBrowserDataExportManager
+ _OBJC_CLASS_$_BEBrowserDataExtension
+ _OBJC_CLASS_$_BEBrowserDataHistoryVisit
+ _OBJC_CLASS_$_BEBrowserDataImportManager
+ _OBJC_CLASS_$_BEBrowserDataReadingListItem
+ _OBJC_CLASS_$_BEExportMetadata
+ _OBJC_CLASS_$_BEImportMetadata
+ _OBJC_CLASS_$_SafariSettingsExportRequest
+ _OBJC_METACLASS_$_SafariSettingsExportRequest
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _SafariSettingsExportRequestSpecifierPropertyKey
+ _WBSExtensionsExportDeveloperNameKey
+ _WBSExtensionsExportDisplayNameKey
+ _WBSExtensionsExportMarketplaceLookupKey
+ _WBSExtensionsExportStoreIdentifierKey
+ __47-[SafariDownloadsSettingsController specifiers]_block_invoke.72
+ __47-[SafariSettingsController _exportButtonTapped]_block_invoke.650
+ __47-[SafariSettingsController _exportButtonTapped]_block_invoke_5.cold.1
+ __47-[SafariSettingsController _importButtonTapped]_block_invoke.605
+ __47-[SafariSettingsController _importButtonTapped]_block_invoke.cold.1
+ __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.357
+ __58-[SafariDownloadsSettingsController _updateSelectedFolder]_block_invoke.76
+ __73-[SafariDownloadsSettingsController _setDefaultDownloadsLocationItemURL:]_block_invoke.91
+ __73-[SafariDownloadsSettingsController _setDefaultDownloadsLocationItemURL:]_block_invoke.cold.1
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke.654
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke.657
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke.660
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke.663
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.655
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.655.cold.1
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.658
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.658.cold.1
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.661
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.661.cold.1
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.664
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.664.cold.1
+ __94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2.cold.1
+ __OBJC_$_INSTANCE_METHODS_SafariSettingsExportRequest
+ __OBJC_$_INSTANCE_VARIABLES_SafariSettingsExportRequest
+ __OBJC_$_PROP_LIST_SafariSettingsExportRequest
+ __OBJC_CLASS_RO_$_SafariSettingsExportRequest
+ __OBJC_METACLASS_RO_$_SafariSettingsExportRequest
+ ___47-[SafariSettingsController _exportButtonTapped]_block_invoke
+ ___47-[SafariSettingsController _exportButtonTapped]_block_invoke_2
+ ___47-[SafariSettingsController _exportButtonTapped]_block_invoke_3
+ ___47-[SafariSettingsController _exportButtonTapped]_block_invoke_4
+ ___47-[SafariSettingsController _exportButtonTapped]_block_invoke_5
+ ___58-[SafariSettingsController toggleExportButtonEnabledState]_block_invoke
+ ___58-[SafariSettingsController toggleImportButtonEnabledState]_block_invoke
+ ___66-[SafariSettingsController _showImportSheetWithCompletionHandler:]_block_invoke
+ ___69-[SafariSettingsBrowsingDataExportController exportHistoryWithBlock:]_block_invoke
+ ___69-[SafariSettingsBrowsingDataExportController exportHistoryWithBlock:]_block_invoke_2
+ ___71-[SafariSettingsBrowsingDataExportController exportBookmarksWithBlock:]_block_invoke
+ ___71-[SafariSettingsBrowsingDataExportController exportBookmarksWithBlock:]_block_invoke_2
+ ___72-[SafariSettingsBrowsingDataExportController exportExtensionsWithBlock:]_block_invoke
+ ___73-[SafariDownloadsSettingsController _setDefaultDownloadsLocationItemURL:]_block_invoke
+ ___73-[SafariSettingsBrowsingDataExportController exportReadingListWithBlock:]_block_invoke
+ ___73-[SafariSettingsBrowsingDataExportController exportReadingListWithBlock:]_block_invoke_2
+ ___76-[SafariSettingsBrowsingDataExportController _numberOfBookmarksToBeExported]_block_invoke
+ ___83-[SafariSettingsBrowsingDataExportController _numberOfReadingListItemsToBeExported]_block_invoke
+ ___94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke
+ ___94-[SafariSettingsController _exportBrowsingDataWithExportOptions:browsingDataExportController:]_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e42_v32?0"NSString"8"NSString"16"NSDate"24ls32l8
+ ___block_descriptor_40_e8_32bs_e45_v24?0"DOCDownloadSettingsItem"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e60_v44?0B8"NSString"12"NSString"20"NSString"28"NSString"36ls32l8
+ ___block_descriptor_40_e8_32bs_e75_v80?0"NSString"8d16"NSString"24B32B36"NSString"40d48"NSString"56d64Q72ls32l8
+ ___block_descriptor_40_e8_32s_e45_v24?0"DOCDownloadSettingsItem"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e37_v24?0"BEImportOptions"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e34_v20?0"BEBrowserDataBookmark"8B16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e35_v20?0"BEBrowserDataExtension"8B16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e37_v24?0"BEExportOptions"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e38_v20?0"BEBrowserDataHistoryVisit"8B16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e41_v20?0"BEBrowserDataReadingListItem"8B16lw40l8s32l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e11_v24?0Q8Q16lr40l8r48l8r56l8r64l8s32l8
+ ___block_descriptor_81_e8_32s40r48r56r64r72w_e5_v8?0lw72l8r40l8r48l8r56l8r64l8s32l8
+ ___block_descriptor_88_e8_32s40s48r56r64r72r80w_e5_v8?0lw80l8s32l8r48l8r56l8r64l8r72l8s40l8
+ ___swift_memcpy16_8
+ __block_literal_global.139
+ __block_literal_global.174
+ __block_literal_global.328
+ __block_literal_global.443
+ __block_literal_global.445
+ __block_literal_global.632
+ __block_literal_global.666
+ __block_literal_global.768
+ __block_literal_global.772
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_MobileSafariSettings
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_MobileSafariSettings
+ _bookmarkQueue
+ _dispatch_group_wait
+ _objc_msgSend$_computeNumberOfBookmarksToBeImportedFromURL:completionHandler:
+ _objc_msgSend$_exportBrowsingDataWithExportOptions:browsingDataExportController:
+ _objc_msgSend$_extensionsToBeExported
+ _objc_msgSend$_headerGroupCellFooterText
+ _objc_msgSend$_importBookmarksFromURL:completionHandler:
+ _objc_msgSend$_locationContainingItem:
+ _objc_msgSend$_setDefaultDownloadsLocationItemURL:
+ _objc_msgSend$_showImportSheetWithCompletionHandler:
+ _objc_msgSend$_updateSelectedFolderWithItem:
+ _objc_msgSend$bundle
+ _objc_msgSend$createSpecifiers
+ _objc_msgSend$dataTypes
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$deviceIdentifier
+ _objc_msgSend$exportBookmarksWithBlock:
+ _objc_msgSend$exportBookmarksWithBlock:completionHandler:
+ _objc_msgSend$exportBrowserData:completionHandler:
+ _objc_msgSend$exportExtensionsWithBlock:
+ _objc_msgSend$exportFinishedWithCompletionHandler:
+ _objc_msgSend$exportHistoryWithBlock:
+ _objc_msgSend$exportHistoryWithBlock:completionHandler:
+ _objc_msgSend$exportReadingListToFileWithURL:completionHandler:
+ _objc_msgSend$exportReadingListWithBlock:
+ _objc_msgSend$exportReadingListWithBlock:completionHandler:
+ _objc_msgSend$exportToFiles
+ _objc_msgSend$fetchDefaultDownloadsLocationSettingsItem:
+ _objc_msgSend$fetchSuitableLocationsForDownloads:
+ _objc_msgSend$importBookmarksFromURL:completionHandler:
+ _objc_msgSend$importFromFiles
+ _objc_msgSend$inAppWebBrowsingSettingsFeatureDescriptionCell
+ _objc_msgSend$init
+ _objc_msgSend$initAsFolder:title:identifier:url:parentIdentifier:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$initWithDisplayName:developerName:identifier:storeIdentifier:
+ _objc_msgSend$initWithScene:
+ _objc_msgSend$initWithSupportForExportToFiles:bookmarksCount:readingListCount:historyCount:extensionsCount:
+ _objc_msgSend$initWithSupportForImportFromFiles:
+ _objc_msgSend$initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:score:
+ _objc_msgSend$initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:
+ _objc_msgSend$initWithTitle:url:dateOfLastVisit:
+ _objc_msgSend$initWithURL:dateOfLastVisit:title:loadedSuccessfully:httpGet:redirectSourceURL:redirectSourceDateOfVisit:redirectDestinationURL:redirectDestinationDateOfVisit:visitCount:
+ _objc_msgSend$initWithWindowScene:
+ _objc_msgSend$isKindOfClass:
+ _objc_msgSend$isLocalStorageDomain
+ _objc_msgSend$isSolariumCompactTabBarEnabled
+ _objc_msgSend$isiCloudDriveDomain
+ _objc_msgSend$localizedSubtitle
+ _objc_msgSend$locationSharesDomainWith:
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$providerFullDisplayName
+ _objc_msgSend$providerIcon
+ _objc_msgSend$readingListFolder
+ _objc_msgSend$requestExportForMetadata:token:completionHandler:
+ _objc_msgSend$requestImportForMetadata:completionHandler:
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$setDefaultDownloadsLocationURL:completionHandler:
+ _objc_msgSend$setDefaultDownloadsToLocation:completionHandler:
+ _objc_msgSend$setSpecifierIdentifierToScrollAndHighlight:
+ _objc_msgSend$setSpecifierIdentifierToScrollAndSelect:
+ _objc_msgSend$setToken:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$toggleExportButtonEnabledState
+ _objc_msgSend$toggleImportButtonEnabledState
+ _objc_msgSend$token
+ _objc_msgSend$windowScene
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _symbolic So27SafariSettingsExportRequestC
+ _symbolic _____Sg 10Foundation4UUIDV
+ bookmarkQueue.cold.1
+ get_witness_table 8Settings05TupleA17ExperienceContentVyAA0acD0PAAE02onaC7OpenURL7performQrAA0acF9URLActionV6ResultVAI5InputVYacn_tFQOyAA0A4PaneVy19PreferencesExtended0M14ControllerViewVG_Qo__A2sOy7SwiftUI0P0PAAE07bridgedA33FeatureDescriptionNavigationTitleyQrqd__SyRd__lFQOyAR_SSQo_GQPGAaDHPyHC.27
- -[SafariDownloadsSettingsController _itemManager]
- -[SafariDownloadsSettingsController _setDefaultDownloadsLocationItem:]
- GCC_except_table128
- GCC_except_table208
- GCC_except_table47
- OBJC_IVAR_$_SafariDownloadsSettingsController._itemManager
- _DOCDocumentSourceIdentifierLocal
- _DOCLocalizedDisplayName
- _OBJC_CLASS_$_DOCDocumentSource
- _OBJC_CLASS_$_FPItemID
- _OBJC_CLASS_$_FPItemManager
- _OBJC_CLASS_$_FPProviderDomain
- __47-[SafariDownloadsSettingsController specifiers]_block_invoke.75
- __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.350
- __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.cold.2
- __58-[SafariDownloadsSettingsController _updateSelectedFolder]_block_invoke.79
- __70-[SafariDownloadsSettingsController _setDefaultDownloadsLocationItem:]_block_invoke.cold.1
- __75-[SafariDownloadsSettingsController documentPicker:didPickDocumentsAtURLs:]_block_invoke.cold.1
- ___54-[SafariDownloadsSettingsController _showFolderPicker]_block_invoke
- ___54-[SafariDownloadsSettingsController _showFolderPicker]_block_invoke_2
- ___70-[SafariDownloadsSettingsController _setDefaultDownloadsLocationItem:]_block_invoke
- ___75-[SafariDownloadsSettingsController documentPicker:didPickDocumentsAtURLs:]_block_invoke
- ___77-[SafariSettingsBrowsingDataExportController _numberOfExtensionsToBeExported]_block_invoke
- ___block_descriptor_32_e32_"NSString"16?0"NSDictionary"8l
- ___block_descriptor_40_e8_32bs_e28_v24?0"FPItem"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e18_v24?0q8"NSURL"16ls32l8
- ___block_descriptor_40_e8_32s_e28_v24?0"FPItem"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e28_v24?0"FPItem"8"NSError"16ls32l8s40l8
- __block_literal_global.137
- __block_literal_global.168
- __block_literal_global.320
- __block_literal_global.436
- __block_literal_global.438
- __block_literal_global.622
- __block_literal_global.744
- __block_literal_global.748
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_itemManager
- _objc_msgSend$_setDefaultDownloadsLocationItem:
- _objc_msgSend$fetchDefaultDownloadsLocationItem:
- _objc_msgSend$fetchItemForURL:completionHandler:
- _objc_msgSend$fetchProvidersSuitableForDownloads:
- _objc_msgSend$fetchURLForItem:completionHandler:
- _objc_msgSend$folderType
- _objc_msgSend$iconForFileProvider:size:
- _objc_msgSend$importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:
- _objc_msgSend$initWithTitle:address:parentID:subtype:collectionType:score:
- _objc_msgSend$initWithTitle:symbolImageName:favoritesFolderServerID:
- _objc_msgSend$isReadingListFolder
- _objc_msgSend$isiCloudDriveProvider
- _objc_msgSend$itemID
- _objc_msgSend$providerDomainForItem:error:
- _objc_msgSend$providerDomainID
- _objc_msgSend$providerID
- _objc_msgSend$rootItemIDWithProviderDomainID:
- _objc_msgSend$setDefaultDownloadsItemForProviderDomain:completionHandler:
- _objc_msgSend$setDefaultDownloadsLocationItem:completionHandler:
- _objc_msgSend$suggestedImportedBookmarksFolderName
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- get_witness_table 8Settings05TupleA17ExperienceContentVyAA0acD0PAAE02onaC7OpenURL7performQrAA0acF9URLActionV6ResultVAI5InputVYacn_tFQOyAA0A4PaneVy19PreferencesExtended0M14ControllerViewVG_Qo__A2sOy7SwiftUI0P0PAAE07bridgedA33FeatureDescriptionNavigationTitleyQrqd__SyRd__lFQOyAR_SSQo_GQPGAaDHPyHC.26
CStrings:
+ "/Library/Caches/com.apple.xbs/8B46371E-4790-4DAF-A963-85DBC666A642/TemporaryDirectory.CVogdh/Sources/Safari/iOS/MobileSafari/SafariStorageSettingsController.m"
+ "@\"BEBrowserDataExportManager\""
+ "@\"DOCDownloadSettingsItem\""
+ "@\"NSUUID\""
+ "@\"SafariSettingsExportRequest\""
+ "Failed to export bookmark: %{public}@"
+ "Failed to export extensions: %{public}@"
+ "Failed to export history: %{public}@"
+ "Failed to export reading list item: %{public}@"
+ "Failed to initiate browser data exchange: %{public}@"
+ "SafariSettingsExportRequest"
+ "SafariSettingsExportRequestSpecifierPropertyKey"
+ "SearchEngineSettingsController"
+ "T@\"NSUUID\",&,N,V_token"
+ "Unable to finish the browser data export: %{public}@"
+ "WebBrowsingSettingsController"
+ "_browserDataExchangeExportManager"
+ "_computeNumberOfReadingListItemsToBeImportedFromURL:completionHandler:"
+ "_exportBrowsingDataWithExportOptions:browsingDataExportController:"
+ "_exportButtonDisabled"
+ "_exportReadingListToFileWithURL:completionHandler:"
+ "_exportRequest"
+ "_extensionsToBeExported"
+ "_headerGroupCellFooterText"
+ "_importButtonDisabled"
+ "_importReadingListFromURL:completionHandler:"
+ "_locationContainingItem:"
+ "_numberOfReadingListItemsToBeExported"
+ "_setDefaultDownloadsLocationItemURL:"
+ "_showImportSheetWithCompletionHandler:"
+ "_token"
+ "_updateSelectedFolderWithItem:"
+ "com.apple.Safari.SafariSettingsBrowsingDataExportController.bookmarkQueue"
+ "createSpecifiers"
+ "dataTypes"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deviceIdentifier"
+ "exportBookmarksWithBlock:"
+ "exportBookmarksWithBlock:completionHandler:"
+ "exportBrowserData:completionHandler:"
+ "exportExtensionsWithBlock:"
+ "exportFinishedWithCompletionHandler:"
+ "exportHistoryWithBlock:"
+ "exportHistoryWithBlock:completionHandler:"
+ "exportReadingListToFileWithURL:completionHandler:"
+ "exportReadingListWithBlock:"
+ "exportReadingListWithBlock:completionHandler:"
+ "exportToFiles"
+ "fetchDefaultDownloadsLocationSettingsItem:"
+ "fetchSuitableLocationsForDownloads:"
+ "importBookmarksFromURL:completionHandler:"
+ "importFromFiles"
+ "initAsFolder:title:identifier:url:parentIdentifier:"
+ "initWithDisplayName:developerName:identifier:storeIdentifier:"
+ "initWithScene:"
+ "initWithSupportForExportToFiles:bookmarksCount:readingListCount:historyCount:extensionsCount:"
+ "initWithSupportForImportFromFiles:"
+ "initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:score:"
+ "initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:"
+ "initWithTitle:url:dateOfLastVisit:"
+ "initWithURL:dateOfLastVisit:title:loadedSuccessfully:httpGet:redirectSourceURL:redirectSourceDateOfVisit:redirectDestinationURL:redirectDestinationDateOfVisit:visitCount:"
+ "initWithWindowScene:"
+ "isExportButtonDisabled:"
+ "isImportButtonDisabled:"
+ "isLocalStorageDomain"
+ "isSolariumCompactTabBarEnabled"
+ "isiCloudDriveDomain"
+ "localizedSubtitle"
+ "locationSharesDomainWith:"
+ "providerFullDisplayName"
+ "providerIcon"
+ "readingListFolder"
+ "requestExportForMetadata:token:completionHandler:"
+ "requestImportForMetadata:completionHandler:"
+ "setDefaultDownloadsLocationURL:completionHandler:"
+ "setDefaultDownloadsToLocation:completionHandler:"
+ "setToken:"
+ "toggleExportButtonEnabledState"
+ "toggleImportButtonEnabledState"
+ "token"
+ "v20@?0@\"BEBrowserDataBookmark\"8B16"
+ "v20@?0@\"BEBrowserDataExtension\"8B16"
+ "v20@?0@\"BEBrowserDataHistoryVisit\"8B16"
+ "v20@?0@\"BEBrowserDataReadingListItem\"8B16"
+ "v24@?0@\"BEExportOptions\"8@\"NSError\"16"
+ "v24@?0@\"BEImportOptions\"8@\"NSError\"16"
+ "v24@?0@\"DOCDownloadSettingsItem\"8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSDate\"24"
+ "v44@?0B8@\"NSString\"12@\"NSString\"20@\"NSString\"28@\"NSString\"36"
+ "v80@?0@\"NSString\"8d16@\"NSString\"24B32B36@\"NSString\"40d48@\"NSString\"56d64Q72"
+ "windowScene"
- "/Library/Caches/com.apple.xbs/Sources/Safari/iOS/MobileSafari/SafariStorageSettingsController.m"
- "@\"FPItem\""
- "@\"FPItemManager\""
- "@\"NSString\"16@?0@\"NSDictionary\"8"
- "Could not fetch FPItem for URL %{private}@: %{public}@"
- "Failed to determine provider domain for downloads folder: %{public}@"
- "_itemManager"
- "_setDefaultDownloadsLocationItem:"
- "com.apple.CloudDocs.iCloudDriveFileProvider"
- "com.apple.FileProvider.LocalStorage"
- "fetchDefaultDownloadsLocationItem:"
- "fetchItemForURL:completionHandler:"
- "fetchProvidersSuitableForDownloads:"
- "fetchURLForItem:completionHandler:"
- "folderType"
- "iconForFileProvider:size:"
- "importBookmarksFromURL:inFolderWithSuggestedName:completionHandler:"
- "initWithTitle:address:parentID:subtype:collectionType:score:"
- "initWithTitle:symbolImageName:favoritesFolderServerID:"
- "isReadingListFolder"
- "isiCloudDriveProvider"
- "itemID"
- "providerDomainForItem:error:"
- "providerDomainID"
- "providerID"
- "rootItemIDWithProviderDomainID:"
- "setDefaultDownloadsItemForProviderDomain:completionHandler:"
- "setDefaultDownloadsLocationItem:completionHandler:"
- "suggestedImportedBookmarksFolderName"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"FPItem\"8@\"NSError\"16"

```
