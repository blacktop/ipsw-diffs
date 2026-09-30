## NewsUI

> `/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x359e4
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x65fc
-  __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x2048
-  __TEXT.__gcc_except_tab: 0x814
+5718.1.0.0.0
+  __TEXT.__text: 0x33968
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x6314
+  __TEXT.__const: 0x258
+  __TEXT.__cstring: 0x1fcd
+  __TEXT.__gcc_except_tab: 0x800
   __TEXT.__oslogstring: 0xa55
   __TEXT.__ustring: 0x17a
-  __TEXT.__unwind_info: 0x1160
-  __TEXT.__objc_classname: 0x13d9
-  __TEXT.__objc_methname: 0xfe97
-  __TEXT.__objc_methtype: 0x386f
-  __TEXT.__objc_stubs: 0x9b00
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__const: 0x19a8
-  __DATA_CONST.__objc_classlist: 0x3b8
+  __TEXT.__unwind_info: 0x1090
+  __TEXT.__objc_classname: 0x1364
+  __TEXT.__objc_methname: 0xf434
+  __TEXT.__objc_methtype: 0x362a
+  __TEXT.__objc_stubs: 0x93e0
+  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__const: 0x1918
+  __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x368
+  __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3840
+  __DATA_CONST.__objc_selrefs: 0x3648
   __DATA_CONST.__objc_protorefs: 0x1c8
-  __DATA_CONST.__objc_superrefs: 0x2f8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0xda0
-  __AUTH_CONST.__cfstring: 0x12c0
-  __AUTH_CONST.__objc_const: 0xe438
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__const: 0xd40
+  __AUTH_CONST.__cfstring: 0x1260
+  __AUTH_CONST.__objc_const: 0xdfb0
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x138
-  __AUTH.__objc_data: 0xe10
-  __DATA.__objc_ivar: 0x5f0
-  __DATA.__data: 0x28e0
-  __DATA.__bss: 0x80
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x5c4
+  __DATA.__data: 0x2820
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 901DEF56-4859-3321-94E2-795EF3BADF94
-  Functions: 1677
-  Symbols:   7178
-  CStrings:  3691
+  UUID: DEE74C65-A0E7-38C9-861A-A05DA557A8F6
+  Functions: 1629
+  Symbols:   6964
+  CStrings:  3585
 
Symbols:
+ -[NUArticleContext initWithShouldAutoPlayVideo:scrollPosition:]
+ -[NUArticleViewController articleDidApplyDocumentStyle:]
+ -[NUArticleViewController prepareArticleLoadingWithContext:]
+ -[UIViewController(NUScrollView) findSafeAreaInsetsProviderForScrollView:]
+ GCC_except_table17
+ GCC_except_table71
+ __OBJC_$_PROTOCOL_REFS_NUSafeAreaInsetsProviding
+ __OBJC_LABEL_PROTOCOL_$_NUSafeAreaInsetsProviding
+ __OBJC_PROTOCOL_$_NUSafeAreaInsetsProviding
+ __OBJC_PROTOCOL_REFERENCE_$_NUSafeAreaInsetsProviding
+ ___61-[NUArticleViewController finalizeArticleLoadingWithContext:]_block_invoke.361
+ ___block_literal_global.1004
+ ___block_literal_global.1007
+ ___block_literal_global.1010
+ ___block_literal_global.1013
+ ___block_literal_global.1015
+ ___block_literal_global.1018
+ ___block_literal_global.186
+ ___block_literal_global.206
+ ___block_literal_global.216
+ ___block_literal_global.224
+ ___block_literal_global.239
+ ___block_literal_global.251
+ ___block_literal_global.269
+ ___block_literal_global.288
+ ___block_literal_global.316
+ ___block_literal_global.330
+ ___block_literal_global.341
+ ___block_literal_global.347
+ ___block_literal_global.357
+ ___block_literal_global.365
+ ___block_literal_global.384
+ ___block_literal_global.406
+ ___block_literal_global.409
+ ___block_literal_global.428
+ ___block_literal_global.432
+ ___block_literal_global.459
+ ___block_literal_global.517
+ ___block_literal_global.527
+ ___block_literal_global.536
+ ___block_literal_global.543
+ ___block_literal_global.907
+ ___block_literal_global.915
+ ___block_literal_global.940
+ ___block_literal_global.947
+ ___block_literal_global.956
+ ___block_literal_global.959
+ ___block_literal_global.962
+ ___block_literal_global.968
+ ___block_literal_global.971
+ ___block_literal_global.983
+ ___block_literal_global.990
+ ___block_literal_global.996
+ _objc_msgSend$articleDidApplyDocumentStyle:
+ _objc_msgSend$findSafeAreaInsetsProviderForScrollView:
+ _objc_msgSend$isDefaultCallingAppScheme:
+ _objc_msgSend$loadedArticle:didApplyDocumentStyle:
+ _objc_msgSend$nu_adjustInsetsForScrollView:
+ _objc_msgSend$prepareArticleLoadingWithContext:
+ _objc_msgSend$willLoadArticle:withContext:
- +[NUArticleNextButton nextArrowImage]
- +[NUArticleNextButton titleLabelFont]
- +[NUArticleNextButton titleLabelFont].cold.1
- -[NUArticleBarButtonItemManager .cxx_destruct]
- -[NUArticleBarButtonItemManager adjustedFrameForDoneBarButtonItemForTraitCollection:]
- -[NUArticleBarButtonItemManager adjustedFrameForNextArticleButtonForTraitCollection:]
- -[NUArticleBarButtonItemManager adjustedFrameForShareBarButtonItemForTraitCollection:]
- -[NUArticleBarButtonItemManager applyPageStyleToNextBarButtonItem:]
- -[NUArticleBarButtonItemManager createDoneBarButtonItem]
- -[NUArticleBarButtonItemManager createFlexibleSpacerBarButtonItem]
- -[NUArticleBarButtonItemManager createShareBarButtonItem]
- -[NUArticleBarButtonItemManager delegate]
- -[NUArticleBarButtonItemManager doDone:]
- -[NUArticleBarButtonItemManager doNext:]
- -[NUArticleBarButtonItemManager doShare:]
- -[NUArticleBarButtonItemManager doneBarButtonItem]
- -[NUArticleBarButtonItemManager initWithViewController:]
- -[NUArticleBarButtonItemManager nextBarButtonItem]
- -[NUArticleBarButtonItemManager nextButton]
- -[NUArticleBarButtonItemManager positionBarButtonItemsForTraitCollection:]
- -[NUArticleBarButtonItemManager setDelegate:]
- -[NUArticleBarButtonItemManager setDoneBarButtonItem:]
- -[NUArticleBarButtonItemManager setShareBarButtonItem:]
- -[NUArticleBarButtonItemManager shareBarButtonItem]
- -[NUArticleBarButtonItemManager sizeBarButtonItemsForTraitCollection:]
- -[NUArticleBarButtonItemManager viewController]
- -[NUArticleContainerViewController articleBarButtonItemManager:performDoneActionForBarButtonItem:]
- -[NUArticleContainerViewController articleBarButtonItemManager:performNextActionForBarButtonItem:]
- -[NUArticleContainerViewController articleBarButtonItemManager:performShareActionForBarButtonItem:]
- -[NUArticleContainerViewController articleBarButtonItemManagerDidLayoutBarButtonItems:]
- -[NUArticleContainerViewController barButtonItemManager]
- -[NUArticleContainerViewController traitCollectionDidChange:]
- -[NUArticleContext initWithShouldAutoPlayVideo:scrollPosition:shouldDisableTransparentNavigationBar:]
- -[NUArticleContext shouldDisableTransparentNavigationBar]
- -[NUArticleNextButton .cxx_destruct]
- -[NUArticleNextButton initWithFrame:]
- -[NUArticleNextButton layoutSubviews]
- -[NUArticleNextButton nextArrowImageView]
- -[NUArticleNextButton nextTitleLabel]
- -[NUArticleNextButton setHighlighted:]
- -[NUArticleNextButton setNextLabelTitle:animated:]
- -[NUArticleViewController setShouldDisableTransparentNavigationBar:]
- -[NUArticleViewController shouldDisableTransparentNavigationBar]
- -[NUArticleViewController useTransparentNavigationBar]
- -[UIViewController(NUScrollView) nu_adjustInsetsForScrollView:transparentNavigationBar:withEdgeInsets:]
- -[UIViewController(NUScrollView) nu_adjustInsetsForScrollView:withEdgeInsets:]
- GCC_except_table23
- GCC_except_table70
- _CGRectGetMinX
- _OBJC_CLASS_$_NUArticleBarButtonItemManager
- _OBJC_CLASS_$_NUArticleNextButton
- _OBJC_CLASS_$_UIActivityViewController
- _OBJC_CLASS_$_UIButton
- _OBJC_CLASS_$_UINavigationButton
- _OBJC_IVAR_$_NUArticleBarButtonItemManager._delegate
- _OBJC_IVAR_$_NUArticleBarButtonItemManager._doneBarButtonItem
- _OBJC_IVAR_$_NUArticleBarButtonItemManager._nextBarButtonItem
- _OBJC_IVAR_$_NUArticleBarButtonItemManager._nextButton
- _OBJC_IVAR_$_NUArticleBarButtonItemManager._shareBarButtonItem
- _OBJC_IVAR_$_NUArticleBarButtonItemManager._viewController
- _OBJC_IVAR_$_NUArticleContainerViewController._barButtonItemManager
- _OBJC_IVAR_$_NUArticleContext._shouldDisableTransparentNavigationBar
- _OBJC_IVAR_$_NUArticleNextButton._nextArrowImageView
- _OBJC_IVAR_$_NUArticleNextButton._nextTitleLabel
- _OBJC_IVAR_$_NUArticleViewController._shouldDisableTransparentNavigationBar
- _OBJC_METACLASS_$_NUArticleBarButtonItemManager
- _OBJC_METACLASS_$_NUArticleNextButton
- _OBJC_METACLASS_$_UIButton
- _UIActivityTypeAssignToContact
- _UIActivityTypePostToFlickr
- _UIActivityTypePostToVimeo
- _UIActivityTypePrint
- _UIActivityTypeSaveToCameraRoll
- _UIEdgeInsetsZero
- __OBJC_$_CLASS_METHODS_NUArticleNextButton
- __OBJC_$_INSTANCE_METHODS_NUArticleBarButtonItemManager
- __OBJC_$_INSTANCE_METHODS_NUArticleNextButton
- __OBJC_$_INSTANCE_VARIABLES_NUArticleBarButtonItemManager
- __OBJC_$_INSTANCE_VARIABLES_NUArticleNextButton
- __OBJC_$_PROP_LIST_FCUserEventHistoryStorageType
- __OBJC_$_PROP_LIST_NUArticleBarButtonItemManager
- __OBJC_$_PROP_LIST_NUArticleNextButton
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCClearableReadingHistory
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCUserEventHistoryStorageType
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NUArticleBarButtonItemManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_FCClearableReadingHistory
- __OBJC_$_PROTOCOL_METHOD_TYPES_FCUserEventHistoryStorageType
- __OBJC_$_PROTOCOL_METHOD_TYPES_NUArticleBarButtonItemManagerDelegate
- __OBJC_$_PROTOCOL_REFS_FCClearableReadingHistory
- __OBJC_$_PROTOCOL_REFS_FCUserEventHistoryStorageType
- __OBJC_$_PROTOCOL_REFS_NUArticleBarButtonItemManagerDelegate
- __OBJC_CLASS_RO_$_NUArticleBarButtonItemManager
- __OBJC_CLASS_RO_$_NUArticleNextButton
- __OBJC_LABEL_PROTOCOL_$_FCClearableReadingHistory
- __OBJC_LABEL_PROTOCOL_$_FCUserEventHistoryStorageType
- __OBJC_LABEL_PROTOCOL_$_NUArticleBarButtonItemManagerDelegate
- __OBJC_METACLASS_RO_$_NUArticleBarButtonItemManager
- __OBJC_METACLASS_RO_$_NUArticleNextButton
- __OBJC_PROTOCOL_$_FCClearableReadingHistory
- __OBJC_PROTOCOL_$_FCUserEventHistoryStorageType
- __OBJC_PROTOCOL_$_NUArticleBarButtonItemManagerDelegate
- __OBJC_PROTOCOL_REFERENCE_$_FCUserEventHistoryStorageType
- ___33-[NUCoreAssembly loadInRegistry:]_block_invoke_26
- ___33-[NUCoreAssembly loadInRegistry:]_block_invoke_27
- ___37+[NUArticleNextButton nextArrowImage]_block_invoke
- ___37+[NUArticleNextButton titleLabelFont]_block_invoke
- ___59-[NUArticleContainerViewController styleNavigationForPage:]_block_invoke_4
- ___61-[NUArticleViewController finalizeArticleLoadingWithContext:]_block_invoke.356
- ___99-[NUArticleContainerViewController articleBarButtonItemManager:performShareActionForBarButtonItem:]_block_invoke
- ___block_descriptor_32_e55_"<FCUserEventHistoryStorageType>"16?0"<TFResolver>"8l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32w_e21_v16?0"NUPageStyle"8lw32l8
- ___block_descriptor_48_e8_32s40s_e30_v16?0"<NUActivityProvider>"8ls32l8s40l8
- ___block_literal_global.1000
- ___block_literal_global.1003
- ___block_literal_global.1006
- ___block_literal_global.1009
- ___block_literal_global.1011
- ___block_literal_global.1014
- ___block_literal_global.182
- ___block_literal_global.202
- ___block_literal_global.212
- ___block_literal_global.220
- ___block_literal_global.235
- ___block_literal_global.247
- ___block_literal_global.265
- ___block_literal_global.284
- ___block_literal_global.304
- ___block_literal_global.307
- ___block_literal_global.326
- ___block_literal_global.337
- ___block_literal_global.349
- ___block_literal_global.361
- ___block_literal_global.383
- ___block_literal_global.423
- ___block_literal_global.427
- ___block_literal_global.443
- ___block_literal_global.446
- ___block_literal_global.455
- ___block_literal_global.464
- ___block_literal_global.468
- ___block_literal_global.563
- ___block_literal_global.572
- ___block_literal_global.579
- ___block_literal_global.589
- ___block_literal_global.903
- ___block_literal_global.911
- ___block_literal_global.936
- ___block_literal_global.943
- ___block_literal_global.952
- ___block_literal_global.955
- ___block_literal_global.958
- ___block_literal_global.964
- ___block_literal_global.967
- ___block_literal_global.979
- ___block_literal_global.986
- ___block_literal_global.992
- _nextArrowImage.image
- _nextArrowImage.onceToken
- _objc_msgSend$activities
- _objc_msgSend$activityItemSources
- _objc_msgSend$activityProvider:
- _objc_msgSend$addTarget:action:forControlEvents:
- _objc_msgSend$adjustedFrameForDoneBarButtonItemForTraitCollection:
- _objc_msgSend$adjustedFrameForNextArticleButtonForTraitCollection:
- _objc_msgSend$adjustedFrameForShareBarButtonItemForTraitCollection:
- _objc_msgSend$applyPageStyleToNextBarButtonItem:
- _objc_msgSend$articleBarButtonItemManager:performDoneActionForBarButtonItem:
- _objc_msgSend$articleBarButtonItemManager:performNextActionForBarButtonItem:
- _objc_msgSend$articleBarButtonItemManager:performShareActionForBarButtonItem:
- _objc_msgSend$articleBarButtonItemManagerDidLayoutBarButtonItems:
- _objc_msgSend$articleContainerViewControllerDidFinishPresenting:
- _objc_msgSend$barButtonItemManager
- _objc_msgSend$contentInset
- _objc_msgSend$createDoneBarButtonItem
- _objc_msgSend$createFlexibleSpacerBarButtonItem
- _objc_msgSend$createShareBarButtonItem
- _objc_msgSend$doneBarButtonItem
- _objc_msgSend$frameUsingCenterAndBounds
- _objc_msgSend$hasTelephonyScheme
- _objc_msgSend$initWithActivityItems:applicationActivities:
- _objc_msgSend$initWithBarButtonSystemItem:target:action:
- _objc_msgSend$initWithCustomView:
- _objc_msgSend$initWithTitle:style:target:action:
- _objc_msgSend$initWithViewController:
- _objc_msgSend$isHidden
- _objc_msgSend$items
- _objc_msgSend$layoutFrame
- _objc_msgSend$nextArrowImage
- _objc_msgSend$nextArrowImageView
- _objc_msgSend$nextBarButtonItem
- _objc_msgSend$nextButton
- _objc_msgSend$nextButtonTitle
- _objc_msgSend$nextTitleLabel
- _objc_msgSend$nu_adjustInsetsForScrollView:transparentNavigationBar:withEdgeInsets:
- _objc_msgSend$nu_adjustInsetsForScrollView:withEdgeInsets:
- _objc_msgSend$nu_view
- _objc_msgSend$popoverPresentationController
- _objc_msgSend$positionBarButtonItemsForTraitCollection:
- _objc_msgSend$recipeUserEventHistory
- _objc_msgSend$registerProtocol:name:factory:
- _objc_msgSend$routeToNewsAppForYouFeed
- _objc_msgSend$router
- _objc_msgSend$safeAreaLayoutGuide
- _objc_msgSend$setBarButtonItem:
- _objc_msgSend$setDoneBarButtonItem:
- _objc_msgSend$setExcludedActivityTypes:
- _objc_msgSend$setLeftBarButtonItems:
- _objc_msgSend$setNextLabelTitle:animated:
- _objc_msgSend$setRightBarButtonItems:
- _objc_msgSend$setShareBarButtonItem:
- _objc_msgSend$setShouldDisableTransparentNavigationBar:
- _objc_msgSend$setToolbarItems:
- _objc_msgSend$shareBarButtonItem
- _objc_msgSend$shouldDisableTransparentNavigationBar
- _objc_msgSend$sizeBarButtonItemsForTraitCollection:
- _objc_msgSend$storage
- _objc_msgSend$tabBar
- _objc_msgSend$tabBarController
- _objc_msgSend$titleLabelFont
- _objc_msgSend$uppercaseString
- _objc_msgSend$useTransparentNavigationBar
- _objc_msgSend$userEventHistory
- _titleLabelFont.font
- _titleLabelFont.onceToken
CStrings:
+ "%"
+ "@\"<FCRecipeItemFactoryType>\"16@0:8"
+ "@28@0:8B16@20"
+ "NUSafeAreaInsetsProviding"
+ "T@\"<FCRecipeItemFactoryType>\",R,N"
+ "articleDidApplyDocumentStyle:"
+ "dismissingIdentifier"
+ "findSafeAreaInsetsProviderForScrollView:"
+ "initWithShouldAutoPlayVideo:scrollPosition:"
+ "isDefaultCallingAppScheme:"
+ "loadedArticle:didApplyDocumentStyle:"
+ "prepareArticleLoadingWithContext:"
+ "recipeItemFactory"
+ "willLoadArticle:withContext:"
- "@\"<FCUserEventHistoryStorageType>\"16@?0@\"<TFResolver>\"8"
- "@\"<NUArticleBarButtonItemManagerDelegate>\""
- "@\"FCUserEventHistoryMetadata\"16@0:8"
- "@\"NUArticleBarButtonItemManager\""
- "@\"NUArticleNextButton\""
- "@\"UIBarButtonItem\""
- "@32@0:8B16@20B28"
- "Done"
- "FCClearableReadingHistory"
- "FCUserEventHistoryStorageType"
- "NUArticleBarButtonItemManager"
- "NUArticleBarButtonItemManagerDelegate"
- "NUArticleNextButton"
- "T@\"<NUArticleBarButtonItemManagerDelegate>\",W,N,V_delegate"
- "T@\"FCUserEventHistoryMetadata\",R,N"
- "T@\"NUArticleBarButtonItemManager\",R,N,V_barButtonItemManager"
- "T@\"NUArticleNextButton\",R,N,V_nextButton"
- "T@\"UIBarButtonItem\",&,N,V_doneBarButtonItem"
- "T@\"UIBarButtonItem\",&,N,V_shareBarButtonItem"
- "T@\"UIBarButtonItem\",R,N,V_nextBarButtonItem"
- "T@\"UIImageView\",R,N,V_nextArrowImageView"
- "T@\"UILabel\",R,N,V_nextTitleLabel"
- "T@\"UIViewController\",R,W,N,V_viewController"
- "TB,N,V_shouldDisableTransparentNavigationBar"
- "TB,R,N,V_shouldDisableTransparentNavigationBar"
- "_barButtonItemManager"
- "_doneBarButtonItem"
- "_nextArrowImageView"
- "_nextBarButtonItem"
- "_nextButton"
- "_nextTitleLabel"
- "_shareBarButtonItem"
- "_shouldDisableTransparentNavigationBar"
- "addTarget:action:forControlEvents:"
- "adjustedFrameForDoneBarButtonItemForTraitCollection:"
- "adjustedFrameForNextArticleButtonForTraitCollection:"
- "adjustedFrameForShareBarButtonItemForTraitCollection:"
- "applyPageStyleToNextBarButtonItem:"
- "articleBarButtonItemManager:performDoneActionForBarButtonItem:"
- "articleBarButtonItemManager:performNextActionForBarButtonItem:"
- "articleBarButtonItemManager:performShareActionForBarButtonItem:"
- "articleBarButtonItemManagerDidLayoutBarButtonItems:"
- "articleContainerViewControllerDidFinishPresenting:"
- "barButtonItemManager"
- "baseDirectoryURL"
- "clearAllSessions"
- "clearHistory"
- "contentInset"
- "createDoneBarButtonItem"
- "createFlexibleSpacerBarButtonItem"
- "createShareBarButtonItem"
- "doDone:"
- "doNext:"
- "doShare:"
- "doneBarButtonItem"
- "earliestSessionDate"
- "frameUsingCenterAndBounds"
- "hasTelephonyScheme"
- "icon-article-next-arrow"
- "initWithActivityItems:applicationActivities:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithCustomView:"
- "initWithShouldAutoPlayVideo:scrollPosition:shouldDisableTransparentNavigationBar:"
- "initWithTitle:style:target:action:"
- "initWithViewController:"
- "isEmpty"
- "isHidden"
- "items"
- "layoutFrame"
- "nextArrowImage"
- "nextArrowImageView"
- "nextBarButtonItem"
- "nextButton"
- "nextTitleLabel"
- "nu_adjustInsetsForScrollView:transparentNavigationBar:withEdgeInsets:"
- "nu_adjustInsetsForScrollView:withEdgeInsets:"
- "popoverPresentationController"
- "positionBarButtonItemsForTraitCollection:"
- "prunedSessionIDs"
- "prunedSessionSize"
- "recipe"
- "registerProtocol:name:factory:"
- "safeAreaLayoutGuide"
- "sessionIDs"
- "sessions"
- "setBarButtonItem:"
- "setDoneBarButtonItem:"
- "setExcludedActivityTypes:"
- "setHighlighted:"
- "setLeftBarButtonItems:"
- "setMetadataWithAggregateStoreGenerationTime:aggregateTotalCount:meanCountOfEvents:standardDeviationOfEvents:totalEventsCount:headlineEventCount:headlinesWithValidTitleEmbeddingsEventCount:headlinesWithInvalidTitleEmbeddingsEventCount:headlinesWithValidBodyEmbeddingsEventCount:headlinesWithInvalidBodyEmbeddingsEventCount:eventCounts:aggregateStoreData:"
- "setNextLabelTitle:animated:"
- "setRightBarButtonItems:"
- "setShareBarButtonItem:"
- "setShouldDisableTransparentNavigationBar:"
- "setToolbarItems:"
- "shareBarButtonItem"
- "shouldDisableTransparentNavigationBar"
- "sizeBarButtonItemsForTraitCollection:"
- "storage"
- "storeSessionID:sessionData:"
- "tabBar"
- "tabBarController"
- "titleLabelFont"
- "uppercaseString"
- "useTransparentNavigationBar"
- "v112@0:8q16q24d32d40q48q56q64q72q80q88@\"FCUserEventHistoryEventCounts\"96@\"FCUserEventHistoryAggregateStoreData\"104"
- "v112@0:8q16q24d32d40q48q56q64q72q80q88@96@104"
- "v16@?0@\"<NUActivityProvider>\"8"
- "v24@0:8@\"NUArticleBarButtonItemManager\"16"
- "v24@0:8@?<@\"NSData\"@?@\"FCUserEventHistorySession\">16"
- "v32@0:8@\"NSString\"16@\"NSData\"24"
- "v32@0:8@\"NUArticleBarButtonItemManager\"16@\"UIBarButtonItem\"24"
- "v56@0:8@16{UIEdgeInsets=dddd}24"
- "v60@0:8@16B24{UIEdgeInsets=dddd}28"
- "writeJSON:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"

```
