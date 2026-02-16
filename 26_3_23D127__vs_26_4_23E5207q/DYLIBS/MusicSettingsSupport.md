## MusicSettingsSupport

> `/System/Library/PrivateFrameworks/MusicSettingsSupport.framework/MusicSettingsSupport`

```diff

-4025.400.5.0.0
-  __TEXT.__text: 0x36dc
-  __TEXT.__auth_stubs: 0x320
+4025.510.40.1.0
+  __TEXT.__text: 0x38f8
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x324
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0xf0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_const: 0x5d0
   __AUTH.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AE7D51D-CF33-3FF4-B115-FA7196D35B76
+  UUID: B3F5063D-C7DF-3A77-A18B-8EE41080C3DD
   Functions: 57
-  Symbols:   375
+  Symbols:   373
   CStrings:  250
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[MusicSettingsListItemsViewController itemsFromParent] : 500 -> 536
~ -[MusicSettingsListItemsViewController listItemSelected:] : 440 -> 448
~ ___57-[MusicSettingsListItemsViewController listItemSelected:]_block_invoke : 144 -> 148
~ -[MusicSettingsListItemsViewController tableView:cellForRowAtIndexPath:] : 324 -> 348
~ -[MusicSettingsListItemsViewController loadSpecifiersFromPlistName:target:bundle:] : 184 -> 188
~ -[MusicSettingsListViewController _sectionedCollectionRepresentation] : 276 -> 288
~ -[MusicSettingsListViewController _configureCell:forIndexPath:] : 160 -> 164
~ -[MusicSettingsListViewController updateVisibleSpecifiers] : 736 -> 732
~ ___58-[MusicSettingsListViewController updateVisibleSpecifiers]_block_invoke : 296 -> 324
~ ___58-[MusicSettingsListViewController updateVisibleSpecifiers]_block_invoke_2 : 240 -> 256
~ ___58-[MusicSettingsListViewController updateVisibleSpecifiers]_block_invoke_3 : 296 -> 304
~ ___58-[MusicSettingsListViewController updateVisibleSpecifiers]_block_invoke_4 : 464 -> 488
~ -[MusicSettingsListViewController tableView:willDisplayCell:forRowAtIndexPath:] : 180 -> 172
~ -[MusicSettingsListViewController specifiers] : 148 -> 160
~ -[MusicSettingsListViewController loadSpecifiersFromPlistName:target:bundle:] : 184 -> 188
~ -[MusicSettingsDynamicFooterHyperlinkAction initWithTarget:selectorString:] : 148 -> 144
~ __MSS_resolvedSpecifiers : 1852 -> 1936
~ __MSS_hasMusicRequiredCapabilities_specifier : 708 -> 716
~ __MSS_setValue_forSpecifier_key : 1716 -> 1824
~ ____MSS_resolvedSpecifiers_block_invoke : 648 -> 660
~ __MSS__hasMusicRequiredCapabilities_specifier : 672 -> 676
~ ____MSS__hasMusicRequiredCapabilities_specifier_block_invoke : 148 -> 152
~ __MSS_valueForRequirementKey_specifier : 360 -> 380
~ -[PSSpecifier(MusicSettingsAdditions) _music_specifierButtonAction:] : 196 -> 208
~ _MusicSettingsPerformSelector2 : 324 -> 328
~ -[PSSpecifier(MusicSettingsAdditions) _music_specifierSetter:] : 216 -> 232
~ -[PSSpecifier(MusicSettingsAdditions) _music_specifierGetter] : 184 -> 200
~ -[PSSpecifier(MusicSettingsAdditions) music_getValue] : 140 -> 144
~ -[PSSpecifier(MusicSettingsAdditions) music_areDisplayValuesEqual:] : 628 -> 688
~ -[PSSpecifier(MusicSettingsAdditions) music_copy] : 592 -> 612

```
