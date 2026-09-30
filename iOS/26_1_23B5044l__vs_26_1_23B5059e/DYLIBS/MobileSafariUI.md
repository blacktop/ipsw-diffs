## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-622.2.5.10.3
-  __TEXT.__text: 0x24f6ac
-  __TEXT.__auth_stubs: 0x3610
-  __TEXT.__objc_methlist: 0x229f4
-  __TEXT.__const: 0x1548
-  __TEXT.__gcc_except_tab: 0x1c36c
-  __TEXT.__cstring: 0x109b4
-  __TEXT.__dlopen_cstrs: 0x774
+622.2.9.10.3
+  __TEXT.__text: 0x251248
+  __TEXT.__auth_stubs: 0x3520
+  __TEXT.__objc_methlist: 0x22b54
+  __TEXT.__const: 0x1738
+  __TEXT.__gcc_except_tab: 0x1c388
+  __TEXT.__cstring: 0x10cf2
+  __TEXT.__dlopen_cstrs: 0x7e0
   __TEXT.__oslogstring: 0x91c8
   __TEXT.__ustring: 0x10e8
-  __TEXT.__constg_swiftt: 0xb38
-  __TEXT.__swift5_typeref: 0x143c
+  __TEXT.__constg_swiftt: 0xbb8
+  __TEXT.__swift5_typeref: 0x1532
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x698
-  __TEXT.__swift5_fieldmd: 0x580
-  __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift5_capture: 0x17b8
+  __TEXT.__swift5_reflstr: 0x748
+  __TEXT.__swift5_fieldmd: 0x61c
+  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__swift5_proto: 0xb4
+  __TEXT.__swift5_types: 0x84
+  __TEXT.__swift5_capture: 0x181c
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xd930
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0xd9e0
   __TEXT.__eh_frame: 0xd38
-  __TEXT.__objc_classname: 0x3f4d
-  __TEXT.__objc_methname: 0x6b906
-  __TEXT.__objc_methtype: 0x15035
-  __TEXT.__objc_stubs: 0x466a0
-  __DATA_CONST.__got: 0x2cb0
-  __DATA_CONST.__const: 0x8b10
-  __DATA_CONST.__objc_classlist: 0x948
+  __TEXT.__objc_classname: 0x3f6a
+  __TEXT.__objc_methname: 0x6bdbb
+  __TEXT.__objc_methtype: 0x150f4
+  __TEXT.__objc_stubs: 0x46940
+  __DATA_CONST.__got: 0x2c90
+  __DATA_CONST.__const: 0x8b30
+  __DATA_CONST.__objc_classlist: 0x958
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0xac8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x169b8
+  __DATA_CONST.__objc_selrefs: 0x16ac0
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x6a0
-  __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x1b20
-  __AUTH_CONST.__const: 0x60b0
-  __AUTH_CONST.__cfstring: 0xc4e0
-  __AUTH_CONST.__objc_const: 0x30270
+  __DATA_CONST.__objc_superrefs: 0x6a8
+  __DATA_CONST.__objc_arraydata: 0x340
+  __AUTH_CONST.__auth_got: 0x1aa8
+  __AUTH_CONST.__const: 0x61e0
+  __AUTH_CONST.__cfstring: 0xc700
+  __AUTH_CONST.__objc_const: 0x305a8
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x2ee0
-  __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x20b4
-  __DATA.__data: 0x7fc0
-  __DATA.__bss: 0x1330
-  __DATA.__common: 0x50
-  __DATA_DIRTY.__objc_data: 0x3d80
-  __DATA_DIRTY.__data: 0x9e8
-  __DATA_DIRTY.__bss: 0x8d0
+  __AUTH.__objc_data: 0x2ff8
+  __AUTH.__data: 0x1b0
+  __DATA.__objc_ivar: 0x20c4
+  __DATA.__data: 0x7f80
+  __DATA.__bss: 0x15b0
+  __DATA.__common: 0x21
+  __DATA_DIRTY.__objc_data: 0x3da8
+  __DATA_DIRTY.__data: 0x9f0
+  __DATA_DIRTY.__bss: 0x8f0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88B89F79-F2B1-3448-86A0-F6916A00E813
-  Functions: 13484
-  Symbols:   44264
-  CStrings:  22022
+  UUID: 1592C532-DB59-314C-B9C5-6CCF2195FACD
+  Functions: 13566
+  Symbols:   44376
+  CStrings:  22121
 
Symbols:
+ -[BrowserController fastAddBookmarkForTabDocument:]
+ -[BrowserControllerDefaultUIDelegate _browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:]
+ -[BrowserControllerDefaultUIDelegate browserController:animateSafariIconLinkFromPoint:inView:withCompletionHandler:]
+ -[BrowserRootViewController _updateTopScrollEdgeEffectStyle]
+ -[BrowserRootViewController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[CatalogViewController setTopScrollEdgeEffectColor:]
+ -[CatalogViewController setTopScrollEdgeEffectStyle:]
+ -[CatalogViewController topScrollEdgeEffectColor]
+ -[CatalogViewController topScrollEdgeEffectStyle]
+ -[CompletionGroupListing _bottomParsecResultGroup]
+ -[CompletionGroupListing _parsecResultsGroupFromResults:withIdentifier:]
+ -[ScrollColorBlockTestProcessor _createTestPageIfNeeded]
+ -[ScrollColorBlockTestProcessor endedScrollColorBlockTest]
+ -[ScrollColorBlockTestProcessor initWithTestName:browserController:]
+ -[ScrollColorBlockTestProcessor performActionForPage:]
+ -[ScrollColorBlockTestProcessor setEndedScrollColorBlockTest:]
+ -[ScrollColorBlockTestProcessor setStartedScrollColorBlockTest:]
+ -[ScrollColorBlockTestProcessor startPageAction:]
+ -[ScrollColorBlockTestProcessor startedScrollColorBlockTest]
+ -[ScrollTestProcessor endedScrollTest]
+ -[ScrollTestProcessor isNatural]
+ -[ScrollTestProcessor setEndedScrollTest:]
+ -[ScrollTestProcessor setIsNatural:]
+ GCC_except_table1008
+ GCC_except_table1011
+ GCC_except_table1017
+ GCC_except_table1022
+ GCC_except_table1028
+ GCC_except_table1035
+ GCC_except_table1039
+ GCC_except_table1045
+ GCC_except_table1046
+ GCC_except_table1050
+ GCC_except_table1056
+ GCC_except_table1057
+ GCC_except_table1064
+ GCC_except_table1067
+ GCC_except_table1068
+ GCC_except_table1074
+ GCC_except_table1080
+ GCC_except_table1096
+ GCC_except_table1103
+ GCC_except_table1109
+ GCC_except_table1113
+ GCC_except_table1117
+ GCC_except_table1126
+ GCC_except_table1134
+ GCC_except_table1140
+ GCC_except_table1146
+ GCC_except_table1147
+ GCC_except_table1162
+ GCC_except_table1163
+ GCC_except_table1167
+ GCC_except_table1168
+ GCC_except_table1174
+ GCC_except_table1184
+ GCC_except_table1185
+ GCC_except_table1188
+ GCC_except_table1192
+ GCC_except_table1196
+ GCC_except_table1204
+ GCC_except_table1205
+ GCC_except_table1208
+ GCC_except_table1213
+ GCC_except_table1216
+ GCC_except_table1224
+ GCC_except_table1229
+ GCC_except_table1241
+ GCC_except_table1244
+ GCC_except_table1247
+ GCC_except_table1250
+ GCC_except_table1253
+ GCC_except_table1260
+ GCC_except_table1267
+ GCC_except_table1272
+ GCC_except_table1273
+ GCC_except_table1345
+ GCC_except_table1351
+ GCC_except_table944
+ GCC_except_table963
+ GCC_except_table971
+ GCC_except_table972
+ GCC_except_table984
+ GCC_except_table989
+ _CompletionGroupIdentifierBottomPegasusResults
+ _CompletionGroupIdentifierTopPegasusResults
+ _OBJC_CLASS_$_ScrollColorBlockTestProcessor
+ _OBJC_CLASS_$_UIScrollEdgeEffectStyle
+ _OBJC_CLASS_$__TtC14MobileSafariUI18AddedBookmarkToast
+ _OBJC_IVAR_$_CatalogViewController._topScrollEdgeEffectColor
+ _OBJC_IVAR_$_CatalogViewController._topScrollEdgeEffectStyle
+ _OBJC_IVAR_$_ScrollColorBlockTestProcessor._endedScrollColorBlockTest
+ _OBJC_IVAR_$_ScrollColorBlockTestProcessor._startedScrollColorBlockTest
+ _OBJC_IVAR_$_ScrollTestProcessor._endedScrollTest
+ _OBJC_IVAR_$_ScrollTestProcessor._isNatural
+ _OBJC_METACLASS_$_ScrollColorBlockTestProcessor
+ _OBJC_METACLASS_$__TtC14MobileSafariUI18AddedBookmarkToast
+ _SFBrowserViewDidLoadNotification
+ _SFDidGetTextInputModeDirectionality
+ _SFLastSelectedBookmarksFolderTimeKey
+ __DATA__TtC14MobileSafariUI18AddedBookmarkToast
+ __INSTANCE_METHODS__TtC14MobileSafariUI18AddedBookmarkToast
+ __IVARS_FolderSuggestionManager
+ __IVARS__TtC14MobileSafariUI18AddedBookmarkToast
+ __METACLASS_DATA__TtC14MobileSafariUI18AddedBookmarkToast
+ __OBJC_$_INSTANCE_METHODS_ScrollColorBlockTestProcessor
+ __OBJC_$_INSTANCE_VARIABLES_ScrollColorBlockTestProcessor
+ __OBJC_$_PROP_LIST_ScrollColorBlockTestProcessor
+ __OBJC_CLASS_RO_$_ScrollColorBlockTestProcessor
+ __OBJC_METACLASS_RO_$_ScrollColorBlockTestProcessor
+ __PROPERTIES__TtC14MobileSafariUI18AddedBookmarkToast
+ ___114-[BrowserRootViewController capsuleNavigationBarViewController:selectedItemWillChangeToState:options:coordinator:]_block_invoke.274
+ ___115-[BrowserControllerDefaultUIDelegate _browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:]_block_invoke
+ ___115-[BrowserControllerDefaultUIDelegate _browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:]_block_invoke_2
+ ___115-[BrowserControllerDefaultUIDelegate _browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:]_block_invoke_3
+ ___115-[BrowserControllerDefaultUIDelegate _browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:]_block_invoke_4
+ ___115-[BrowserControllerDefaultUIDelegate _browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:]_block_invoke_5
+ ___44-[ScrollTestProcessor performActionForPage:]_block_invoke
+ ___46-[BrowserRootViewController _layOutTopBanners]_block_invoke.177
+ ___51-[BrowserController fastAddBookmarkForTabDocument:]_block_invoke
+ ___54-[ScrollColorBlockTestProcessor performActionForPage:]_block_invoke
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1162
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1163
+ ___56-[ScrollColorBlockTestProcessor _createTestPageIfNeeded]_block_invoke
+ ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1126
+ ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1126.cold.1
+ ___72-[BrowserController _sendPDFRepresentationForScreenshotWithTabDocument:]_block_invoke.1187
+ ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.131
+ ___Block_byref_object_copy_.323
+ ___Block_byref_object_dispose_.324
+ ___block_descriptor_104_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_96_e8_32s40s48bs_e49_v32?0q8"<_SFBarRegistrationToken>"16"UIView"24ls32l8s40l8s48l8
+ ___block_literal_global.1092
+ ___block_literal_global.1097
+ ___block_literal_global.1122
+ ___block_literal_global.1134
+ ___block_literal_global.1142
+ ___block_literal_global.1150
+ ___block_literal_global.1154
+ ___block_literal_global.1160
+ ___block_literal_global.1174
+ ___block_literal_global.2944
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___getRPTDirectionalSwipeTestParametersClass_block_invoke
+ ___getRPTDirectionalSwipeTestParametersClass_block_invoke.cold.1
+ _associated conformance 14MobileSafariUI28BookmarksViewContentProviderC14LoadingOptionsVs10SetAlgebraAASQ
+ _associated conformance 14MobileSafariUI28BookmarksViewContentProviderC14LoadingOptionsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 14MobileSafariUI28BookmarksViewContentProviderC14LoadingOptionsVs9OptionSetAASY
+ _associated conformance 14MobileSafariUI28BookmarksViewContentProviderC14LoadingOptionsVs9OptionSetAAs0K7Algebra
+ _block_copy_helper.24
+ _block_copy_helper.27
+ _block_copy_helper.33
+ _block_copy_helper.39
+ _block_copy_helper.40
+ _block_copy_helper.48
+ _block_copy_helper.54
+ _block_copy_helper.60
+ _block_descriptor.26
+ _block_descriptor.29
+ _block_descriptor.35
+ _block_descriptor.41
+ _block_descriptor.42
+ _block_descriptor.50
+ _block_descriptor.56
+ _block_descriptor.62
+ _block_destroy_helper.25
+ _block_destroy_helper.28
+ _block_destroy_helper.34
+ _block_destroy_helper.40
+ _block_destroy_helper.41
+ _block_destroy_helper.49
+ _block_destroy_helper.55
+ _block_destroy_helper.61
+ _getRPTDirectionalSwipeTestParametersClass.softClass
+ _objc_msgSend$_browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:
+ _objc_msgSend$_createTestPageIfNeeded
+ _objc_msgSend$_performNaturalScrollTest:completionHandler:
+ _objc_msgSend$_updateTopScrollEdgeEffectStyle
+ _objc_msgSend$automaticStyle
+ _objc_msgSend$browserController:animateSafariIconLinkFromPoint:inView:withCompletionHandler:
+ _objc_msgSend$disableTemporarily
+ _objc_msgSend$endedScrollColorBlockTest
+ _objc_msgSend$endedScrollTest
+ _objc_msgSend$fastAddBookmarkForTabDocument:
+ _objc_msgSend$glassButtonConfiguration
+ _objc_msgSend$hardStyle
+ _objc_msgSend$initWithTestName:testType:scrollView:completionHandler:
+ _objc_msgSend$isNatural
+ _objc_msgSend$migrateToReadingListItem
+ _objc_msgSend$setCornerStyle:
+ _objc_msgSend$setEndedScrollColorBlockTest:
+ _objc_msgSend$setEndedScrollTest:
+ _objc_msgSend$setIsNatural:
+ _objc_msgSend$setStartedScrollColorBlockTest:
+ _objc_msgSend$setTopScrollEdgeEffectColor:
+ _objc_msgSend$setTopScrollEdgeEffectStyle:
+ _objc_msgSend$shouldDisableBackgroundColorInBar:traitCollection:
+ _objc_msgSend$shouldShowInternalUI
+ _objc_msgSend$softStyle
+ _objc_msgSend$startedScrollColorBlockTest
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$topEdgeEffect
+ _objc_msgSend$writeToURL:atomically:encoding:error:
+ _swift_retain_n
+ _symbolic $s14MobileSafariUI33AddedBookmarkToastInteractionViewC8DelegateP
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic So11UIImageViewC
+ _symbolic So15_SFSiteIconViewC
+ _symbolic So32AddedBookmarkToastViewControllerCSgXw
+ _symbolic So7UILabelC
+ _symbolic _____ 14MobileSafariUI18AddedBookmarkToastC
+ _symbolic _____ 14MobileSafariUI28BookmarksViewContentProviderC14LoadingOptionsV
+ _symbolic _____Sg 14MobileSafariUI33AddedBookmarkToastInteractionViewC
+ _symbolic ______pSgXw 14MobileSafariUI33AddedBookmarkToastInteractionViewC8DelegateP
+ _type_layout_string 14MobileSafariUI28BookmarksViewContentProviderC14LoadingOptionsV
- -[BrowserRootViewController _shouldDisableBackgroundColorInTabBar:]
- -[BrowserRootViewController _updateTopScrollPocketStyle]
- -[CatalogViewController setTopScrollPocketColor:]
- -[CatalogViewController setTopScrollPocketStyle:]
- -[CatalogViewController topScrollPocketColor]
- -[CatalogViewController topScrollPocketStyle]
- -[CompletionGroupListing _parsecResultsGroupFromResults:]
- GCC_except_table1010
- GCC_except_table1013
- GCC_except_table1019
- GCC_except_table1024
- GCC_except_table1030
- GCC_except_table1037
- GCC_except_table1043
- GCC_except_table1047
- GCC_except_table1048
- GCC_except_table1052
- GCC_except_table1060
- GCC_except_table1061
- GCC_except_table1066
- GCC_except_table1070
- GCC_except_table1073
- GCC_except_table1076
- GCC_except_table1082
- GCC_except_table1100
- GCC_except_table1107
- GCC_except_table1111
- GCC_except_table1115
- GCC_except_table1119
- GCC_except_table1130
- GCC_except_table1138
- GCC_except_table1142
- GCC_except_table1149
- GCC_except_table1152
- GCC_except_table1164
- GCC_except_table1165
- GCC_except_table1170
- GCC_except_table1173
- GCC_except_table1176
- GCC_except_table1186
- GCC_except_table1189
- GCC_except_table1190
- GCC_except_table1194
- GCC_except_table1198
- GCC_except_table1206
- GCC_except_table1207
- GCC_except_table1214
- GCC_except_table1217
- GCC_except_table1218
- GCC_except_table1226
- GCC_except_table1231
- GCC_except_table1243
- GCC_except_table1248
- GCC_except_table1251
- GCC_except_table1255
- GCC_except_table1256
- GCC_except_table1262
- GCC_except_table1269
- GCC_except_table1343
- GCC_except_table1349
- GCC_except_table940
- GCC_except_table946
- GCC_except_table968
- GCC_except_table973
- GCC_except_table974
- GCC_except_table986
- GCC_except_table993
- _CompletionGroupIdentifierPegasusResults
- _OBJC_IVAR_$_CatalogViewController._topScrollPocketColor
- _OBJC_IVAR_$_CatalogViewController._topScrollPocketStyle
- _OUTLINED_FUNCTION_100
- _OUTLINED_FUNCTION_99
- ___114-[BrowserRootViewController capsuleNavigationBarViewController:selectedItemWillChangeToState:options:coordinator:]_block_invoke.272
- ___46-[BrowserRootViewController _layOutTopBanners]_block_invoke.175
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1159
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1160
- ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1124
- ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1124.cold.1
- ___72-[BrowserController _sendPDFRepresentationForScreenshotWithTabDocument:]_block_invoke.1185
- ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.130
- ___99-[BrowserControllerDefaultUIDelegate browserController:animateLinkImage:fromRect:inView:toBarItem:]_block_invoke
- ___99-[BrowserControllerDefaultUIDelegate browserController:animateLinkImage:fromRect:inView:toBarItem:]_block_invoke_2
- ___99-[BrowserControllerDefaultUIDelegate browserController:animateLinkImage:fromRect:inView:toBarItem:]_block_invoke_3
- ___99-[BrowserControllerDefaultUIDelegate browserController:animateLinkImage:fromRect:inView:toBarItem:]_block_invoke_4
- ___Block_byref_object_copy_.319
- ___Block_byref_object_dispose_.320
- ___block_descriptor_88_e8_32s40s_e49_v32?0q8"<_SFBarRegistrationToken>"16"UIView"24ls32l8s40l8
- ___block_descriptor_96_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_literal_global.1090
- ___block_literal_global.1095
- ___block_literal_global.1120
- ___block_literal_global.1132
- ___block_literal_global.1140
- ___block_literal_global.1148
- ___block_literal_global.1152
- ___block_literal_global.1158
- ___block_literal_global.1172
- ___block_literal_global.2941
- ___block_literal_global.374
- _block_copy_helper.14
- _block_copy_helper.18
- _block_copy_helper.28
- _block_copy_helper.4
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.16
- _block_descriptor.20
- _block_descriptor.30
- _block_descriptor.6
- _block_destroy_helper.15
- _block_destroy_helper.19
- _block_destroy_helper.29
- _block_destroy_helper.5
- _block_destroy_helper.9
- _objc_msgSend$_glassButtonConfiguration
- _objc_msgSend$_setPocketStyle:forEdge:
- _objc_msgSend$_shouldDisableBackgroundColorInTabBar:
- _objc_msgSend$_updateTopScrollPocketStyle
- _objc_msgSend$disable
- _objc_msgSend$setTopScrollPocketColor:
- _objc_msgSend$setTopScrollPocketStyle:
- _objc_msgSend$sf_isDarkColorForAdaptiveGlass
- _symbolic Sny_____G 10Foundation16AttributedStringV5IndexV
- _symbolic Sny_____GSg 10Foundation16AttributedStringV5IndexV
- _symbolic _____ 10Foundation16AttributedStringV
- _symbolic _____Sg 10Foundation16AttributedStringV
- _symbolic _____Sg 10Foundation6LocaleV
CStrings:
+ "#000"
+ "#222"
+ "#444"
+ "#666"
+ "#aaa"
+ "#ccc"
+ "#ddd"
+ "#fff"
+ "<!doctype html><html><head><meta charset='utf-8'><title>ScrollColorBlockTest</title><style>.box{width:100%;aspect-ratio:2/1;}</style></head><body>"
+ "</body></html>"
+ "<div class='box' style='background-color:%@;'></div>"
+ "@\"UIScrollEdgeEffectStyle\""
+ "BottomPegasusResults"
+ "Dark"
+ "Light"
+ "MobileSafariUI.AddedBookmarkToast"
+ "MobileSafariUI/AddedBookmarkToast.swift"
+ "Natural"
+ "RPTDirectionalSwipeTestParameters"
+ "ScrollColorBlockTest"
+ "ScrollColorBlockTestProcessor"
+ "T@\"NSTimer\",N,&,VdismissTimer"
+ "T@\"UIColor\",&,N,V_topScrollEdgeEffectColor"
+ "T@\"UIScrollEdgeEffectStyle\",&,N,V_topScrollEdgeEffectStyle"
+ "TB,N,V_endedScrollColorBlockTest"
+ "TB,N,V_endedScrollTest"
+ "TB,N,V_isNatural"
+ "TB,N,V_startedScrollColorBlockTest"
+ "Td,N,R,VlastSelectedFolderValidityPeriod"
+ "TopPegasusResults"
+ "T{CGSize=dd},N,R"
+ "_TtC14MobileSafariUI18AddedBookmarkToast"
+ "_browserController:animateLinkImage:fromRect:inView:toBarItem:withCompletion:"
+ "_createTestPageIfNeeded"
+ "_endedScrollColorBlockTest"
+ "_endedScrollTest"
+ "_isNatural"
+ "_performNaturalScrollTest:completionHandler:"
+ "_startedScrollColorBlockTest"
+ "_topScrollEdgeEffectColor"
+ "_topScrollEdgeEffectStyle"
+ "_updateTopScrollEdgeEffectStyle"
+ "addedToLabel"
+ "automaticStyle"
+ "browserController:animateSafariIconLinkFromPoint:inView:withCompletionHandler:"
+ "cancelDismissTimer"
+ "chevronImageView"
+ "didTapToast"
+ "disableTemporarily"
+ "dismissTimer"
+ "endedScrollColorBlockTest"
+ "endedScrollTest"
+ "fastAddBookmarkForTabDocument:"
+ "folderIconView"
+ "folderNameLabel"
+ "folderType"
+ "glassButtonConfiguration"
+ "hardStyle"
+ "html"
+ "initWithTestName:testType:scrollView:completionHandler:"
+ "isNatural"
+ "lastSelectedFolderValidityPeriod"
+ "loadingOptions"
+ "migrateToBookmarkItem"
+ "migrateToReadingListItem"
+ "secondarySystemFillColor"
+ "setAdjustsImageSizeForAccessibilityContentSizeCategory:"
+ "setBookmark:withBackgroundColor:"
+ "setCornerStyle:"
+ "setCustomImageInset:"
+ "setDismissTimer:"
+ "setEndedScrollColorBlockTest:"
+ "setEndedScrollTest:"
+ "setImage:withBackgroundColor:"
+ "setImageContentMode:"
+ "setIsNatural:"
+ "setStartedScrollColorBlockTest:"
+ "setTopScrollEdgeEffectColor:"
+ "setTopScrollEdgeEffectStyle:"
+ "shouldDisableBackgroundColorInBar:traitCollection:"
+ "shouldShowInternalUI"
+ "softStyle"
+ "startDismissTimer"
+ "startedScrollColorBlockTest"
+ "stringByAppendingPathExtension:"
+ "toast"
+ "topEdgeEffect"
+ "topScrollEdgeEffectColor"
+ "topScrollEdgeEffectStyle"
+ "v56@0:8@\"BrowserController\"16{CGPoint=dd}24@\"UIView\"40@?<v@?>48"
+ "v56@0:8@16{CGPoint=dd}24@40@?48"
+ "v88@0:8@16^{CGImage=}24{CGRect={CGPoint=dd}{CGSize=dd}}32@64q72@?80"
+ "viewDidMoveToWindow:shouldAppearOrDisappear:"
+ "writeToURL:atomically:encoding:error:"
- "AddedBookmarkToastViewController"
- "PegasusResults"
- "T@\"UIColor\",&,N,V_topScrollPocketColor"
- "Tq,N,V_topScrollPocketStyle"
- "_glassButtonConfiguration"
- "_setPocketStyle:forEdge:"
- "_shouldDisableBackgroundColorInTabBar:"
- "_topScrollPocketColor"
- "_topScrollPocketStyle"
- "_updateTopScrollPocketStyle"
- "configurationWithFont:"
- "disable"
- "imageWithTintColor:"
- "setTopScrollPocketColor:"
- "setTopScrollPocketStyle:"
- "sf_isDarkColorForAdaptiveGlass"
- "toastButton"
- "toastButtonPressed"
- "topScrollPocketColor"
- "topScrollPocketStyle"

```
