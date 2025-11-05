## TestFlightCore

> `/System/Library/PrivateFrameworks/TestFlightCore.framework/Versions/A/TestFlightCore`

```diff

 4.4.14.0.0
-  __TEXT.__text: 0x1a648
+  __TEXT.__text: 0x1a5e8
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x1730
+  __TEXT.__objc_methlist: 0x1dcc
   __TEXT.__const: 0x138
   __TEXT.__cstring: 0x217e
   __TEXT.__oslogstring: 0x1955
   __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_classname: 0x62e
   __TEXT.__objc_methname: 0x6d39
   __TEXT.__objc_methtype: 0x1ccb

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1828
+  __DATA_CONST.__objc_selrefs: 0x1ab8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x6d0
   __AUTH_CONST.__cfstring: 0x1b40
-  __AUTH_CONST.__objc_const: 0x5ce0
+  __AUTH_CONST.__objc_const: 0x5090
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 107C744A-B209-3EE8-A38C-471AD8D813BB
-  Functions: 549
-  Symbols:   2040
+  UUID: 822A3B3C-92E7-3CDE-AA13-0D8DE028F9AD
+  Functions: 555
+  Symbols:   2047
   CStrings:  1901
 
Symbols:
+ +[TFBundle frameworkBundle].cold.1
+ +[TFLogConfiguration defaultConfiguration].cold.1
+ -[NSMutableAttributedString(TFCoreAdditions) tf_addLanguageAwareness:].cold.1
+ -[NSMutableAttributedString(TFCoreAdditions) tf_addLanguageAwareness:].cold.2
+ -[NSMutableAttributedString(TFCoreAdditions) tf_addLanguageAwareness:].cold.3
+ -[TFFeedbackSession _currentContextStringDescription].cold.1
+ TFLocalizedString.cold.1
Functions:
~ -[TFFeedbackEntryGroup initWithIdentifier:entries:title:election:headerText:headerTextLinkMap:footerText:footerTextLinkMap:] : 552 -> 540
~ -[TFFeedbackFormImageAlertPresenter presentBatchedErrorsIfAny] : 876 -> 856
~ -[TFFeedbackFormScreenshotItem loadView] : 1964 -> 1944
~ -[TFFeedbackFormScreenshotItem setImage:] : 172 -> 168
~ -[TFFeedbackFormScreenshotItem setFileName:] : 188 -> 184
~ -[TFBetaApplicationProxy deviceWillInstallVersion:build:withLocalizedDisplayNames:localizedTestNotes:primaryLocaleKey:developerName:expirationDate:iconUrlTemplate:testerEmail:] : 1200 -> 1192
~ -[TFBetaApplicationProxy overwriteMetadataForInstalledVersion:build:withLocalizedDisplayNames:localizedTestNotes:primaryLocaleKey:developerName:expirationDate:iconUrlTemplate:testerEmail:] : 1516 -> 1508
~ -[TFBetaApplicationProxy _asdAppPlatform] : 32 -> 28
~ -[TFFeedbackFormPresenter _indexPathsOfVisibleEntriesWithIdentifiers:] : 300 -> 296
~ -[TFFeedbackFormViewController initWithPresenter:] : 780 -> 776
~ ___50-[TFFeedbackFormViewController initWithPresenter:]_block_invoke : 280 -> 276
~ +[TFBundle frameworkBundle] : 84 -> 68
~ -[NSMutableAttributedString(TFCoreAdditions) tf_addLanguageAwareness:] : 2488 -> 2484
- sub_250eeca5c
~ -[TFFeedbackFormScreenshotCollectionView setHighlightedColorEnabled:] : 284 -> 224
~ -[TFBetaAppLaunchScreenWindowController initWithPresenter:] : 264 -> 260
~ -[TFBetaAppLaunchScreenWindowController actionButtonWindow:] : 236 -> 240
~ +[TFLogConfiguration defaultConfiguration] : 84 -> 68
~ +[TFLocale preferredLocaleKeyFromAvailableKeys:primaryLocaleKey:] : 704 -> 708
~ -[TFFeedbackDataContainer(Testing) objectForIdentifier:] : 160 -> 152
~ -[TFFeedbackSession _beginFeedbackSubmisionForViewController:] : 980 -> 976
~ ___62-[TFFeedbackSession _beginFeedbackSubmisionForViewController:]_block_invoke : 216 -> 208
~ -[TFFeedbackSession _currentContextStringDescription] : 112 -> 96
~ _TFLocalizedString : 148 -> 132

```
