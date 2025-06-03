## MobileSafari

> `/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari`

```diff

-7617.2.4.10.8
-  __TEXT.__text: 0x6994
-  __TEXT.__auth_stubs: 0x430
+7618.1.15.10.11
+  __TEXT.__text: 0x6ac4
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_stubs: 0x14a0
   __TEXT.__objc_methlist: 0x250
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x781
+  __TEXT.__cstring: 0xd52
   __TEXT.__oslogstring: 0x102b
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x1477
+  __TEXT.__objc_methname: 0x1485
   __TEXT.__objc_methtype: 0x18d
-  __TEXT.__unwind_info: 0x174
-  __DATA_CONST.__auth_got: 0x228
+  __TEXT.__unwind_info: 0x17c
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__cfstring: 0xf80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xd0
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA.__objc_const: 0x540
   __DATA.__objc_selrefs: 0x590
-  __DATA.__objc_classrefs: 0xd0
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FAF6BF9-8FAE-375F-BC66-DE58BF431A6F
-  Functions: 109
-  Symbols:   165
-  CStrings:  462
+  UUID: FE8F1165-5927-30FE-851D-A12ECAF93DAD
+  Functions: 110
+  Symbols:   218
+  CStrings:  560
 
Symbols:
+ _SafariStorageSettingsControllerDataSourceClassName
+ _SafariWebExtensionDataSourceType
+ _SafariWebsiteDataDataSourceType
+ _debugBarHidingBehaviorKey
+ _debugOverrideTabCapacityKey
+ _disableFluidProgressBarKey
+ _hasCompletedLiverpoolTCCFixDefaultsKey
+ _kAddressFieldSupportsJavascriptURLsDefaultsKey
+ _kAllowsInlineMediaPlaybackDefaultsKey
+ _kAlwaysDispatchScrollEventsDefaultsKey
+ _kCloudTabsEnabledDefaultsKey
+ _kDeletedStaticBookmarksDefaultsKey
+ _kDidCallAttentionToPasswordGenerationAssistanceKey
+ _kDisableWebsiteSpecificSearch
+ _kFontAutoSizeSettingDefaultsKey
+ _kLayoutIntervalDefaultsKey
+ _kLogMemoryJetsamDetailsDefaultsKey
+ _kMemoryWarningSleepIntervalDefaultsKey
+ _kNetworkDiskCacheConfigurationDefaultsKey
+ _kPageLoadAllSubresourcesLoadedTime
+ _kPageLoadDOMContentLoadedTime
+ _kPageLoadEndTime
+ _kPageLoadFirstMeaningfulPaintTime
+ _kPageLoadFirstVisuallyNonEmptyLayoutTime
+ _kPageLoadStartTime
+ _kPageMemoryAfterWarning
+ _kPageMemoryBeforeWarning
+ _kReaderMaxDistanceForLoadingNextPageDefaultsKey
+ _kSafariApplePayDisclosureDidChangeNotification
+ _kSafariAutoFillStateChangedNotification
+ _kSafariDataMigratorFileProtectionEnabledDefaultsKey
+ _kSafariDidClearHistoryAndWebsiteDataNotification
+ _kSafariDidClearHistoryNotification
+ _kSafariEducationModeEducationTabsLastSyncDate
+ _kSafariQuickWebsiteSearchProvidersDidChangeNotification
+ _kSafariSettingsChangedExtensionSettingsNotification
+ _kSafariUniversalSearchDebugAlwaysShowResults
+ _kSafariUniversalSearchUserGUIDDefaultsKey
+ _kSafariUniversalSearchUserGUIDExpirationDateDefaultsKey
+ _kSearchEngineLastSpamDateDefaultsKey
+ _kSearchEngineSpamIntervalDefaultsKey
+ _kShowTabBarDefaultsKey
+ _kSpeculativeLoadingDefaultsKey
+ _kUserAgentDefaultsKey
+ _kWebFoundationPreferencesDomain
+ _kWebGLEnabledDefaultsKey
+ _lastModifiedTimeOfCloudTabDeviceUsedForRestoration
+ _objc_retainBlock
+ _overridenFrequentlyVisitedSitesKey
+ _shouldShowSiriSuggestionsWelcomeViewKey
+ _showSidebarDefaultsKey
+ _startPageExpansionDictionaryKey
+ _uuidOfCloudTabDeviceUsedForRestoration
CStrings:
+ "@\"NSArray\"16@?0@\"NSArray\"8"
+ "AddressFieldSupportsJavascriptURLs"
+ "DebugAlwaysShowUniversalSearchResults"
+ "DebugBarCollapsingBehavior"
+ "DebugOverrideTabCapacity"
+ "DeletedStaticBookmarks"
+ "DidCallAttentionToPasswordGenerationAssistance"
+ "DisableFluidProgressBar"
+ "DisableWebsiteSpecificSearch"
+ "FontAutoSizeSetting"
+ "LayoutInterval"
+ "LiverpoolTCCFixDone"
+ "LogMemoryJetsamDetails"
+ "MemoryWarningSleepInterval"
+ "NetworkDiskCacheConfiguration"
+ "OverridenFrequentlyVisitedSites"
+ "PageLoadAllSubresourcesLoadedTime"
+ "PageLoadDOMContentLoadedTime"
+ "PageLoadEndTime"
+ "PageLoadFirstMeaningfulPaintTime"
+ "PageLoadFirstVisuallyNonEmptyLayoutTime"
+ "PageLoadStartTime"
+ "PageMemoryAfterWarning"
+ "PageMemoryBeforeWarning"
+ "ReaderMaxDistanceForLoadingNextPage"
+ "SafariEducationModeEducationTabsLastSyncDate"
+ "SafariStorageSettingsControllerDataSourceClassName"
+ "SafariWebExtensionDataSource"
+ "SafariWebsiteDataDataSource"
+ "SearchEngineLastSpamDate"
+ "SearchEngineSpamInterval"
+ "ShowSidebar"
+ "ShowTabBar"
+ "SpeculativeLoading"
+ "T@\"NSString\",?,R,C"
+ "UniversalSearchUserGUID"
+ "UniversalSearchUserGUIDExpirationDate"
+ "UserAgent"
+ "WebKitAlwaysDispatchScrollEvents"
+ "WebKitMediaPlaybackAllowsInline"
+ "WebKitWebGLEnabled"
+ "com.apple.WebFoundation"
+ "com.apple.mobilesafari.ApplePayDisclosureDidChange"
+ "com.apple.mobilesafari.AutoFillStateChanged"
+ "com.apple.mobilesafari.ClearHistory"
+ "com.apple.mobilesafari.ClearHistoryAndWebsiteData"
+ "com.apple.mobilesafari.QuickWebsiteSearchProvidersDidChange"
+ "com.apple.mobilesafari.SafariSettingsChangedExtensionSettings"
+ "shouldShowSiriSuggestionsWelcomeView"
+ "startPageExpansionDictionary"

```
