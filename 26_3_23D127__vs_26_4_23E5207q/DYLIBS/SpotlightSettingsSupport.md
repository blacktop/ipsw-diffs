## SpotlightSettingsSupport

> `/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport`

```diff

-181.3.1.0.0
-  __TEXT.__text: 0x4864
-  __TEXT.__auth_stubs: 0x3a0
+181.4.5.0.0
+  __TEXT.__text: 0x4b38
+  __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__gcc_except_tab: 0x104
   __TEXT.__cstring: 0x77f
   __TEXT.__dlopen_cstrs: 0x142
   __TEXT.__oslogstring: 0x5a
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x190
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methname: 0xd50
   __TEXT.__objc_methtype: 0xa9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_const: 0x578

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DC43202-C8AC-329F-83EC-459476EFF35D
-  Functions: 78
-  Symbols:   500
+  UUID: FEC9154C-85F5-37BA-AFC1-EE68D0114C0D
+  Functions: 80
+  Symbols:   503
   CStrings:  309
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
Functions:
~ +[SpotlightAppClipSettingsController bundle] : 104 -> 112
~ -[SpotlightAppClipSettingsController viewDidLoad] : 152 -> 160
~ -[SpotlightAppClipSettingsController specifiers] : 1552 -> 1652
~ -[SpotlightAppClipSettingsController setShowInSearchEnabled:specifier:] : 380 -> 384
~ +[SpotlightCell bundle] : 108 -> 120
~ -[SpotlightDetailController specifiers] : 696 -> 724
~ -[SpotlightDetailController _isApplicationHiddenCheck:] : 96 -> 104
~ -[SpotlightDetailController _isApplicationLockedCheck:] : 96 -> 104
~ -[SpotlightDetailController _addWhileSearchingSpecifiersToSpecifiers:] : 848 -> 912
~ -[SpotlightDetailController whileSearchingShowAppEnabled:] : 124 -> 132
~ -[SpotlightDetailController _authenticateForBundleIdentifier:completion:] : 416 -> 420
~ -[SpotlightDetailController setWhileSearchingShowAppEnabled:specifier:] : 512 -> 500
~ ___71-[SpotlightDetailController setWhileSearchingShowAppEnabled:specifier:]_block_invoke : 300 -> 308
~ -[SpotlightDetailController _saveWhileSearchingShowAppEnabled:] : 280 -> 288
~ -[SpotlightDetailController whileSearchingShowContentEnabled:] : 124 -> 132
~ -[SpotlightDetailController setWhileSearchingShowContentEnabled:specifier:] : 512 -> 500
~ -[SpotlightDetailController _saveWhileSearchingShowContentEnabled:] : 280 -> 288
~ -[SpotlightDetailController _bundleId] : 84 -> 92
~ -[SpotlightDetailController _appName] : 84 -> 92
~ +[SpotlightSettingsController bundle] : 108 -> 120
~ -[SpotlightSettingsController viewDidLoad] : 152 -> 160
~ -[SpotlightSettingsController viewDidAppear:] : 280 -> 296
~ -[SpotlightSettingsController specifiers] : 180 -> 188
~ -[SpotlightSettingsController configureSearchAndLoookupSpecifiersFor:] : 952 -> 1024
~ -[SpotlightSettingsController configureSafariSearchEngine:] : 1184 -> 1252
~ -[SpotlightSettingsController configureAnonymouslyRecordingQueries:] : 736 -> 792
~ -[SpotlightSettingsController configureApplicationListSpecifiersFor:] : 1872 -> 1952
~ ___69-[SpotlightSettingsController configureApplicationListSpecifiersFor:]_block_invoke : 112 -> 120
~ -[SpotlightSettingsController showAboutSearchSuggestionsSheet:] : 104 -> 108
~ -[SpotlightSettingsController saveSpotlightSettings] : 240 -> 244
~ -[SpotlightSettingsController isShowInLookUpEnabled] : 84 -> 96
~ -[SpotlightSettingsController setShowInLookUpEnabled:] : 224 -> 228
~ -[SpotlightSettingsController refreshSafariSearchEnginePreference:] : 96 -> 100
~ -[SpotlightSettingsController isAnonymouslyRecordSearchQueriesEnabled] : 92 -> 96
~ -[SpotlightSettingsController setAnonymouslyRecordSearchQueriesEnabled:] : 112 -> 116
+ _OUTLINED_FUNCTION_0
~ +[SpotlightSettingsUtilities isAppWithBundleIDPresent:] : 168 -> 172
~ +[SpotlightSettingsUtilities updateSearchPreferencesModificationForKeys:] : 576 -> 604
+ -[SpotlightSettingsController configureApplicationListSpecifiersFor:].cold.3

```
