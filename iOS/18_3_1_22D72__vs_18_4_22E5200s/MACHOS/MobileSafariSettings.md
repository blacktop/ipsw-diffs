## MobileSafariSettings

> `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings`

```diff

-7620.2.4.10.7
-  __TEXT.__text: 0x4ed6c
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0xbec0
-  __TEXT.__objc_methlist: 0x3578
-  __TEXT.__objc_methname: 0x10587
-  __TEXT.__objc_classname: 0x1032
-  __TEXT.__objc_methtype: 0x23f9
-  __TEXT.__const: 0x354
-  __TEXT.__cstring: 0x50d4
+7621.1.10.20.6
+  __TEXT.__text: 0x4f108
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_stubs: 0xc0e0
+  __TEXT.__objc_methlist: 0x40a4
+  __TEXT.__objc_methname: 0x1084f
+  __TEXT.__objc_classname: 0x104d
+  __TEXT.__objc_methtype: 0x248c
+  __TEXT.__const: 0x374
+  __TEXT.__cstring: 0x5114
   __TEXT.__ustring: 0x70a
-  __TEXT.__gcc_except_tab: 0x1da4
+  __TEXT.__gcc_except_tab: 0x1e34
   __TEXT.__oslogstring: 0x953
   __TEXT.__constg_swiftt: 0x10c
   __TEXT.__swift5_typeref: 0x16e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x1470
+  __TEXT.__unwind_info: 0x14a8
   __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__auth_got: 0x710
+  __DATA_CONST.__auth_got: 0x700
   __DATA_CONST.__got: 0xd08
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA_CONST.__const: 0x1ea8
-  __DATA_CONST.__cfstring: 0x48e0
+  __DATA_CONST.__const: 0x1f18
+  __DATA_CONST.__cfstring: 0x4900
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x218

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_const: 0x85b0
-  __DATA.__objc_selrefs: 0x39d0
+  __DATA.__objc_const: 0x7228
+  __DATA.__objc_selrefs: 0x3e58
   __DATA.__objc_ivar: 0x498
   __DATA.__objc_data: 0x1ca8
-  __DATA.__data: 0xe80
-  __DATA.__bss: 0x4b0
+  __DATA.__data: 0xee0
+  __DATA.__bss: 0x4a0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
+  - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SafariServices.framework/SafariServices

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1460
-  Symbols:   5085
-  CStrings:  3438
+  Functions: 1481
+  Symbols:   5204
+  CStrings:  3467
 
Symbols:
+ +[AvailableAppTableCell lockupViewGroup].cold.1
+ +[SafariSettingsController _createTabGroupManagerForClearingHistory]
+ +[SafariSettingsController _tabCollection].cold.1
+ +[SafariSettingsController privacyProxyAvailabilityManager].cold.1
+ +[SafariSettingsFeatureManager sharedFeatureManager].cold.1
+ +[SafariSettingsTaskHandler sharedHandler].cold.1
+ -[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitedSitesIfNecessary:]
+ -[FrequentlyVisitedSitesController openNewRadarProblemURLForFrequentlyVisitedSite:]
+ -[SafariDownloadsSettingsController specifiers].cold.1
+ -[SafariSettingsBrowsingDataImportController _recomputeFrequentlyVisitedSites].cold.1
+ -[SafariSettingsController queryControllerDidUpdate:resultDifference:]
+ GCC_except_table13
+ GCC_except_table194
+ OBJC_IVAR_$_FrequentlyVisitedSitesController._lastSeenFrequentlyVisitedSites
+ OBJC_IVAR_$_SafariSettingsController._contentBlockerQueryController
+ SafariLibraryPath.cold.1
+ SafariNonContaineredLibraryPath.cold.1
+ WBSLocalizableStringFlagPluralRules
+ WBS_LOG_CHANNEL_PREFIXAutoFill.cold.1
+ WBS_LOG_CHANNEL_PREFIXDownloads.cold.1
+ WBS_LOG_CHANNEL_PREFIXExport.cold.1
+ WBS_LOG_CHANNEL_PREFIXExtensions.cold.1
+ WBS_LOG_CHANNEL_PREFIXImport.cold.1
+ WBS_LOG_CHANNEL_PREFIXKeychain.cold.1
+ WBS_LOG_CHANNEL_PREFIXSafariProfiles.cold.1
+ WBS_LOG_CHANNEL_PREFIXWebExtensions.cold.1
+ WBS_LOG_CHANNEL_PREFIXWebsiteData.cold.1
+ _OBJC_CLASS_$__EXQuery
+ _OBJC_CLASS_$__EXQueryController
+ _SFShowTabBarDefaultsKey
+ __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.308
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__EXQueryControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__EXQueryControllerDelegate
+ __OBJC_$_PROTOCOL_REFS__EXQueryControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$__EXQueryControllerDelegate
+ __OBJC_PROTOCOL_$__EXQueryControllerDelegate
+ __SFDeviceAlertStyle
+ ___132-[SafariSettingsBrowsingDataImportController _generateLockupViewsForAvailableAppsWithWebBookmarksSettingsGateway:completionHandler:]_block_invoke_4
+ ___43-[FrequentlyVisitedSitesController dealloc]_block_invoke
+ ___70-[SafariSettingsController queryControllerDidUpdate:resultDifference:]_block_invoke
+ ___70-[SafariSettingsController queryControllerDidUpdate:resultDifference:]_block_invoke_2
+ ___83-[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitedSitesIfNecessary:]_block_invoke
+ ___83-[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitedSitesIfNecessary:]_block_invoke_2
+ ___83-[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitedSitesIfNecessary:]_block_invoke_3
+ ___83-[FrequentlyVisitedSitesController openNewRadarProblemURLForFrequentlyVisitedSite:]_block_invoke
+ ___block_descriptor_32_e23_B16?0"ASCLockupView"8l
+ ___block_descriptor_32_e30_16?0"_EXExtensionIdentity"8l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls40l8s32l8
+ ___block_descriptor_56_ea8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ __block_literal_global.122
+ __block_literal_global.16
+ __block_literal_global.20
+ __block_literal_global.299
+ __block_literal_global.677
+ _objc_msgSend$_createTabGroupManagerForClearingHistory
+ _objc_msgSend$_updateCachedFrequentlyVisitedSitesIfNecessary:
+ _objc_msgSend$activeProfileIdentifier
+ _objc_msgSend$clearActiveProfileReferencesOnWindowsWithProfileIdentifier:
+ _objc_msgSend$clearRecentlyClosedTabsForProfileWithIdentifier:
+ _objc_msgSend$clearSavedTabsForProfileWithIdentifier:closingDatabase:
+ _objc_msgSend$descriptionOfAllFrequentlyVisitedSitesForProblematicSiteURLString:completionHandler:
+ _objc_msgSend$extensionIdentities
+ _objc_msgSend$extensionWithIdentity:error:
+ _objc_msgSend$flags
+ _objc_msgSend$initWithExtensionPointIdentifier:
+ _objc_msgSend$initWithQueries:delegate:
+ _objc_msgSend$isAvailableInCurrentLocale
+ _objc_msgSend$linkPresentationMetadataProvider
+ _objc_msgSend$localTabGroup
+ _objc_msgSend$newRadarProblemURLWithInformationForProblematicFrequentlyVisitedSite:informationForOtherFrequentlyVisitedSites:inProfile:
+ _objc_msgSend$offer
+ _objc_msgSend$readRecentlyClosedTabsState
+ _objc_msgSend$registerWindowState:
+ _objc_msgSend$releaseResponseForURLString:
+ _objc_msgSend$resume
+ _objc_msgSend$saveWindowState:
+ _objc_msgSend$setActiveProfileIdentifier:
+ _objc_msgSend$setActiveTabGroupUUID:
+ _objc_msgSend$setExcludeLockedApps:
+ _objc_msgSend$viewIfLoaded
+ _objc_msgSend$window
+ _objc_msgSend$windowStates
+ _type_layout_string So21NSAttributedStringKeya
+ isiPad.cold.1
- -[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitesSitesIfNecessary]
- GCC_except_table15
- GCC_except_table186
- OBJC_IVAR_$_FrequentlyVisitedSitesController._frequentlyVisitedBookmarksToMetadataTokens
- OBJC_IVAR_$_SafariSettingsController._contentBlockerMatchingContext
- SafariNonContaineredSettingsDirectoryPath.onceToken
- SafariNonContaineredSettingsDirectoryPath.path
- _NSExtensionPointName
- _PKPlugInKitErrorDomain
- _SafariNonContaineredSettingsDirectoryPath
- __55-[SafariSettingsController _updateDownloadsFolderTitle]_block_invoke.307
- ___43-[SafariSettingsController viewWillAppear:]_block_invoke_5
- ___69+[SafariWebsiteDataDataSource deleteAllDataForProfileWithIdentifier:]_block_invoke_3
- ___69+[SafariWebsiteDataDataSource deleteAllDataForProfileWithIdentifier:]_block_invoke_4
- ___82-[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitesSitesIfNecessary]_block_invoke
- ___82-[FrequentlyVisitedSitesController _updateCachedFrequentlyVisitesSitesIfNecessary]_block_invoke_2
- ___SafariNonContaineredSettingsDirectoryPath_block_invoke
- ___block_descriptor_48_ea8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
- __block_literal_global.119
- __block_literal_global.15
- __block_literal_global.298
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_MobileSafariSettings
- __swift_FORCE_LOAD_$_swiftWebKit
- __swift_FORCE_LOAD_$_swiftWebKit_$_MobileSafariSettings
- _kShowTabBarDefaultsKey
- _objc_msgSend$_updateCachedFrequentlyVisitesSitesIfNecessary
- _objc_msgSend$beginMatchingExtensionsWithAttributes:completion:
- _objc_msgSend$cancelRequestsWithTokens:
- _objc_msgSend$clearSavedStatesForProfileWithIdentifier:closingDatabase:
- _objc_msgSend$deleteAllLocalSavedState
- _objc_msgSend$endMatchingExtensions:
- _objc_msgSend$isBrowsingAssistantEnabled
- _objc_msgSend$objectEnumerator
- _objc_msgSend$safari_matchesErrorDomain:andCode:
- _objc_msgSend$strongToStrongObjectsMapTable
- _objc_msgSend$visibleViewController
- _swift_bridgeObjectRelease_n
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "@\"_EXQueryController\""
+ "@16@?0@\"_EXExtensionIdentity\"8"
+ "B16@?0@\"ASCLockupView\"8"
+ "ImportSuccessDetails"
+ "Manage your privacy and Autofill for when you’re browsing the web in apps, clear website data, and more."
+ "_EXQueryControllerDelegate"
+ "_contentBlockerQueryController"
+ "_createTabGroupManagerForClearingHistory"
+ "_lastSeenFrequentlyVisitedSites"
+ "_updateCachedFrequentlyVisitedSitesIfNecessary:"
+ "activeProfileIdentifier"
+ "clearActiveProfileReferencesOnWindowsWithProfileIdentifier:"
+ "clearRecentlyClosedTabsForProfileWithIdentifier:"
+ "clearSavedTabsForProfileWithIdentifier:closingDatabase:"
+ "descriptionOfAllFrequentlyVisitedSitesForProblematicSiteURLString:completionHandler:"
+ "extensionIdentities"
+ "extensionWithIdentity:error:"
+ "flags"
+ "initWithExtensionPointIdentifier:"
+ "initWithQueries:delegate:"
+ "isAvailableInCurrentLocale"
+ "linkPresentationMetadataProvider"
+ "localTabGroup"
+ "newRadarProblemURLWithInformationForProblematicFrequentlyVisitedSite:informationForOtherFrequentlyVisitedSites:inProfile:"
+ "offer"
+ "openNewRadarProblemURLForFrequentlyVisitedSite:"
+ "queryControllerDidUpdate:difference:"
+ "queryControllerDidUpdate:enabledCount:disabledCount:unelectedCount:"
+ "queryControllerDidUpdate:resultDifference:"
+ "readRecentlyClosedTabsState"
+ "registerWindowState:"
+ "releaseResponseForURLString:"
+ "resume"
+ "saveWindowState:"
+ "setActiveProfileIdentifier:"
+ "setActiveTabGroupUUID:"
+ "setExcludeLockedApps:"
+ "v32@0:8@\"_EXQueryController\"16@\"NSOrderedCollectionDifference\"24"
+ "v48@0:8@\"_EXQueryController\"16Q24Q32Q40"
+ "v48@0:8@16Q24Q32Q40"
+ "viewIfLoaded"
+ "window"
+ "windowStates"
- "Manage your privacy and Autofill for when you're browsing the web in apps, clear web history, and more."
- "_contentBlockerMatchingContext"
- "_frequentlyVisitedBookmarksToMetadataTokens"
- "_updateCachedFrequentlyVisitesSitesIfNecessary"
- "beginMatchingExtensionsWithAttributes:completion:"
- "cancelRequestsWithTokens:"
- "clearSavedStatesForProfileWithIdentifier:closingDatabase:"
- "deleteAllLocalSavedState"
- "endMatchingExtensions:"
- "isBrowsingAssistantEnabled"
- "objectEnumerator"
- "safari_matchesErrorDomain:andCode:"
- "strongToStrongObjectsMapTable"
- "visibleViewController"

```
