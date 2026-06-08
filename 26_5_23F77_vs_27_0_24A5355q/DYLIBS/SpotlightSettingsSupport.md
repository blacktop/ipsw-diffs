## SpotlightSettingsSupport

> `/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport`

```diff

-181.4.6.0.0
-  __TEXT.__text: 0x4b38
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x2c4
+228.102.0.0.0
+  __TEXT.__text: 0x4984
+  __TEXT.__objc_methlist: 0x2cc
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__cstring: 0x77f
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__cstring: 0x7a7
   __TEXT.__dlopen_cstrs: 0x142
   __TEXT.__oslogstring: 0x5a
   __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methname: 0xd50
-  __TEXT.__objc_methtype: 0xa9
-  __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__objc_const: 0x578
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
   __DATA.__bss: 0x78

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91278362-F825-3E66-B1AA-CC916CF8796C
-  Functions: 80
-  Symbols:   503
-  CStrings:  309
+  UUID: E0C2E90F-2B75-348E-9535-1085C3C6B729
+  Functions: 81
+  Symbols:   506
+  CStrings:  152
 
Symbols:
+ +[SpotlightSettingsUtilities linwoodEnabled]
+ _AFIsLinwoodEnabledAndAvailable
+ ___block_literal_global.242
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$linwoodEnabled
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
- ___block_literal_global.197
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
Functions:
~ +[SpotlightAppClipSettingsController bundle] : 112 -> 104
~ -[SpotlightAppClipSettingsController viewDidLoad] : 160 -> 152
~ -[SpotlightAppClipSettingsController specifiers] : 1652 -> 1564
~ -[SpotlightAppClipSettingsController setShowInSearchEnabled:specifier:] : 384 -> 392
~ -[SpotlightAppClipSettingsController showInSearchEnabled:] : 84 -> 88
~ +[SpotlightCell bundle] : 120 -> 108
~ -[SpotlightDetailController specifiers] : 724 -> 716
~ -[SpotlightDetailController _isApplicationHiddenCheck:] : 104 -> 96
~ -[SpotlightDetailController _isApplicationLockedCheck:] : 104 -> 96
~ -[SpotlightDetailController _addWhileSearchingSpecifiersToSpecifiers:] : 912 -> 864
~ -[SpotlightDetailController whileSearchingShowAppEnabled:] : 132 -> 128
~ -[SpotlightDetailController _authenticateForBundleIdentifier:completion:] : 420 -> 376
~ ___73-[SpotlightDetailController _authenticateForBundleIdentifier:completion:]_block_invoke : 248 -> 204
~ -[SpotlightDetailController setWhileSearchingShowAppEnabled:specifier:] : 500 -> 512
~ ___71-[SpotlightDetailController setWhileSearchingShowAppEnabled:specifier:]_block_invoke : 308 -> 312
~ ___71-[SpotlightDetailController setWhileSearchingShowAppEnabled:specifier:]_block_invoke_3 : 32 -> 36
~ -[SpotlightDetailController _saveWhileSearchingShowAppEnabled:] : 288 -> 284
~ -[SpotlightDetailController whileSearchingShowContentEnabled:] : 132 -> 128
~ -[SpotlightDetailController setWhileSearchingShowContentEnabled:specifier:] : 500 -> 512
~ ___75-[SpotlightDetailController setWhileSearchingShowContentEnabled:specifier:]_block_invoke_3 : 32 -> 36
~ -[SpotlightDetailController _saveWhileSearchingShowContentEnabled:] : 288 -> 284
~ -[SpotlightDetailController _bundleId] : 92 -> 84
~ -[SpotlightDetailController _appName] : 92 -> 84
~ +[SpotlightSettingsController bundle] : 120 -> 108
~ -[SpotlightSettingsController viewDidLoad] : 160 -> 152
~ -[SpotlightSettingsController viewDidAppear:] : 296 -> 280
~ -[SpotlightSettingsController specifiers] : 188 -> 184
~ -[SpotlightSettingsController configureSearchAndLoookupSpecifiersFor:] : 1024 -> 1156
~ -[SpotlightSettingsController configureSafariSearchEngine:] : 1252 -> 1192
~ -[SpotlightSettingsController configureAnonymouslyRecordingQueries:] : 792 -> 736
~ -[SpotlightSettingsController configureApplicationListSpecifiersFor:] : 1952 -> 1900
~ ___69-[SpotlightSettingsController configureApplicationListSpecifiersFor:]_block_invoke : 120 -> 112
~ -[SpotlightSettingsController showAboutSearchSuggestionsSheet:] : 108 -> 104
~ -[SpotlightSettingsController isShowInLookUpEnabled] : 96 -> 84
~ -[SpotlightSettingsController setShowInLookUpEnabled:] : 228 -> 224
~ -[SpotlightSettingsController isShowInSpotlightEnabled] : 112 -> 116
~ -[SpotlightSettingsController setShowInSpotlightEnabled:] : 132 -> 136
~ -[SpotlightSettingsController refreshSafariSearchEnginePreference:] : 100 -> 96
~ -[SpotlightSettingsController isAnonymouslyRecordSearchQueriesEnabled] : 96 -> 92
~ -[SpotlightSettingsController setAnonymouslyRecordSearchQueriesEnabled:] : 116 -> 112
~ +[SpotlightSettingsUtilities isAppWithBundleIDPresent:] : 172 -> 168
~ +[SpotlightSettingsUtilities logSearchPreferencesModificationState] : 232 -> 188
~ +[SpotlightSettingsUtilities updateSearchPreferencesModificationForKeys:] : 604 -> 580
+ +[SpotlightSettingsUtilities linwoodEnabled]
CStrings:
+ "SEARCH_AND_LOOKUP_FOOTER_LINWOOD"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSMutableSet\""
- "@\"NSSet\""
- "@\"PSSpecifier\""
- "@16@0:8"
- "@24@0:8@16"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "SpotlightAppClipSettingsController"
- "SpotlightCell"
- "SpotlightDetailController"
- "SpotlightPseudoHeaderHyperlinkView"
- "SpotlightSettingsController"
- "SpotlightSettingsUtilities"
- "URLWithString:"
- "_addWhileSearchingSpecifiersToSpecifiers:"
- "_allAppsSpecifiers"
- "_appName"
- "_authenticateForBundleIdentifier:completion:"
- "_bundleId"
- "_disabledLockScreenBundles"
- "_disabledSpotlightApps"
- "_disabledSpotlightBundles"
- "_disabledSpotlightDomains"
- "_disabledSpotlightShortcuts"
- "_disabledSuggestApps"
- "_installedBundleIDs"
- "_isApplicationHidden"
- "_isApplicationHiddenCheck:"
- "_isApplicationLocked"
- "_isApplicationLockedCheck:"
- "_saveWhileSearchingShowAppEnabled:"
- "_saveWhileSearchingShowContentEnabled:"
- "_whileSearchingGroup"
- "_whileSearchingShowAppSpecifier"
- "_whileSearchingShowContentSpecifier"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "allObjects"
- "applicationProxyForIdentifier:"
- "applicationState"
- "applicationWithBundleIdentifier:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "authenticateForSubject:relayingAuditToken:completion:"
- "boolValue"
- "bundle"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleURL"
- "bundleWithIdentifier:"
- "canReload"
- "cellStyle"
- "configureAnonymouslyRecordingQueries:"
- "configureApplicationListSpecifiersFor:"
- "configureSafariSearchEngine:"
- "configureSearchAndLoookupSpecifiersFor:"
- "containsObject:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentLocale"
- "d24@0:8d16"
- "defaultCenter"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "displayName"
- "enginesAvailableForUnifiedFieldSearching"
- "firstObject"
- "flow"
- "getSearchQueriesDataSharingStatus"
- "groupSpecifierWithName:"
- "hiddenApplications"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithKey:table:locale:bundleURL:"
- "insertContiguousSpecifiers:afterSpecifier:animated:"
- "intValue"
- "isAnonymouslyRecordSearchQueriesEnabled"
- "isAppWithBundleIDPresent:"
- "isEqual:"
- "isInstalled"
- "isPlaceholder"
- "isShowInLookUpEnabled"
- "isShowInSpotlightEnabled"
- "isShowZKWRecentsEnabled:"
- "learnFromAppClipsEnabled:"
- "linkWithBundleIdentifier:"
- "loadSpecifiersFromPlistName:target:"
- "loadSystemLanguageProperties"
- "localizedButtonTitle"
- "localizedCaseInsensitiveCompare:"
- "localizedStringForKey:value:table:"
- "lockedApplications"
- "logSearchPreferencesModificationState"
- "minusSet:"
- "mutableCopy"
- "name"
- "now"
- "numberWithBool:"
- "numberWithInt:"
- "pe_emitNavigationEventForApplicationSettingsWithApplicationBundleIdentifier:title:localizedNavigationComponents:deepLink:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferredHeightForWidth:"
- "present"
- "presenterForPrivacySplashWithIdentifier:"
- "propertyForKey:"
- "q16@0:8"
- "rangeOfString:"
- "refreshSafariSearchEnginePreference:"
- "reloadSpecifier:animated:"
- "reloadSpecifiers"
- "removeContiguousSpecifiers:animated:"
- "removeObject:"
- "saveSpotlightSettings"
- "setAnonymouslyRecordSearchQueriesEnabled:"
- "setDetailControllerClass:"
- "setIdentifier:"
- "setLearnFromAppClipsEnabled:specifier:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPresentingViewController:"
- "setProperty:forKey:"
- "setSearchQueriesDataSharingStatus:completion:"
- "setShowInLookUpEnabled:"
- "setShowInSearchEnabled:specifier:"
- "setShowInSpotlightEnabled:"
- "setShowZKWRecentsEnabled:forSpecifier:"
- "setSuggestAppClipsEnabled:specifier:"
- "setTitle:"
- "setValues:titles:shortTitles:"
- "setWhileSearchingShowAppEnabled:specifier:"
- "setWhileSearchingShowContentEnabled:specifier:"
- "setWithArray:"
- "sharedGuard"
- "sharedInstance"
- "sharedPreferences"
- "shortName"
- "showInSearchEnabled:"
- "sortedArrayUsingComparator:"
- "specifier"
- "specifierForID:"
- "specifiers"
- "stringWithFormat:"
- "suggestAppClipsEnabled:"
- "updateSearchPreferencesModificationForKeys:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "valueWithNonretainedObject:"
- "viewDidAppear:"
- "viewDidLoad"
- "whileSearchingShowAppEnabled:"
- "whileSearchingShowContentEnabled:"

```
