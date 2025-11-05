## SilexWeb

> `/System/iOSSupport/System/Library/PrivateFrameworks/SilexWeb.framework/Versions/A/SilexWeb`

```diff

-5626.0.0.0.0
-  __TEXT.__text: 0x1590c
+5676.0.3.0.0
+  __TEXT.__text: 0x15814
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x240c
+  __TEXT.__objc_methlist: 0x2e34
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x195b
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x7a0
+  __TEXT.__unwind_info: 0x7a8
   __TEXT.__objc_classname: 0x7b8
-  __TEXT.__objc_methname: 0x6057
-  __TEXT.__objc_methtype: 0x1988
+  __TEXT.__objc_methname: 0x60ea
+  __TEXT.__objc_methtype: 0x1a18
   __TEXT.__objc_stubs: 0x3fe0
   __DATA_CONST.__got: 0x420
   __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1270
+  __DATA_CONST.__objc_selrefs: 0x13f0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x200
   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x7c0
   __AUTH_CONST.__cfstring: 0x1600
-  __AUTH_CONST.__objc_const: 0x95d8
+  __AUTH_CONST.__objc_const: 0x8480
   __AUTH.__objc_data: 0x1360
   __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x14a8

   - /System/iOSSupport/System/Library/PrivateFrameworks/UIAccessibility.framework/Versions/A/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C99C9DBB-299C-30E7-BE3E-19E3B3CA6317
-  Functions: 801
-  Symbols:   2799
-  CStrings:  1715
+  UUID: 7376C25D-9C4D-3CDB-AFD2-1569B0CA89A3
+  Functions: 802
+  Symbols:   2800
+  CStrings:  1719
 
Symbols:
+ SWSetupLogging.cold.1
Functions:
~ -[SWPresentationManager initWithWebContentScriptsManager:messageHandlerManager:documentStateProvider:logger:] : 488 -> 484
~ -[SWPresentationManager height] : 44 -> 48
~ -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:] : 896 -> 892
~ -[SWContainerViewController viewDidLoad] : 440 -> 436
~ -[SWContainerViewController viewWillTransitionToSize:withTransitionCoordinator:] : 284 -> 280
~ -[SWErrorManager initWithMessageHandlerManager:timeoutManager:logger:] : 356 -> 352
~ -[SWURLSchemeHandlerManager webView:startURLSchemeTask:] : 892 -> 888
~ -[SWContainerConfiguration copyWithZone:] : 416 -> 420
~ -[SWKeyboardConfiguration description] : 372 -> 352
~ _SWSetupLogging : 40 -> 44
~ -[SWViewController initWithWebView:setupManager:scriptsManager:messageHandlerManager:navigationManager:errorReporter:documentStateReporter:timeoutManager:terminationManager:contentRuleManager:reachabilityProvider:logger:sessionManager:datastoreSynchronizationManager:localDatastoreManager:URLSchemeHandlerManager:] : 1152 -> 1136
~ -[SWViewController loadURL:cachePolicy:] : 280 -> 276
~ ___40-[SWViewController loadURL:cachePolicy:]_block_invoke : 460 -> 452
~ -[SWViewController loadHTMLString:baseURL:] : 308 -> 304
~ ___43-[SWViewController loadHTMLString:baseURL:]_block_invoke : 472 -> 464
~ -[SWScriptsManager initWithWebView:documentStateProvider:logger:] : 596 -> 584
~ -[SWInteractionProvider initWithMessageHandlerManager:documentStateProvider:interactionFactory:logger:] : 516 -> 512
~ -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:] : 948 -> 952
~ -[SWConfiguration copyWithZone:] : 536 -> 532
~ -[SWConfiguration isEqualToConfiguration:] : 1468 -> 1340
~ -[SWConfiguration description] : 840 -> 828
~ -[SWDatastoreSynchronizationManager synchronizeDatastore:from:previousDatastore:originatingSession:completion:] : 496 -> 456
CStrings:
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
+ "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"

```
