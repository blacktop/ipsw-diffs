## iMessageApps

> `/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps`

```diff

-1448.100.1.2.101
-  __TEXT.__text: 0x4e10
+1450.200.35.2.5
+  __TEXT.__text: 0x4900
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0xddc
+  __TEXT.__objc_methlist: 0xd4c
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x228
-  __TEXT.__oslogstring: 0x1e1
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x198
-  __TEXT.__objc_methname: 0x31cd
-  __TEXT.__objc_methtype: 0x1307
-  __TEXT.__objc_stubs: 0x1ac0
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x230
+  __TEXT.__oslogstring: 0x29c
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_classname: 0x174
+  __TEXT.__objc_methname: 0x2d30
+  __TEXT.__objc_methtype: 0x11a3
+  __TEXT.__objc_stubs: 0x1800
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb30
+  __DATA_CONST.__objc_selrefs: 0xa40
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0xff8
+  __AUTH_CONST.__objc_const: 0xf68
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x300
+  __DATA.__objc_ivar: 0x98
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CEDA602F-CE44-3831-AD12-19DE85B56F36
-  Functions: 190
-  Symbols:   852
-  CStrings:  627
+  UUID: 4EEB853F-4C86-3FDF-9B4C-CDDDA4046E5E
+  Functions: 189
+  Symbols:   820
+  CStrings:  591
 
Symbols:
+ -[IMAAppPresenter presentAppWithBundleIdentifier:completion:].cold.1
+ -[IMAAppPresenter requestPresentationStyleExpanded:].cold.1
+ -[IMAAppPresenter(Stickers) currentStickerViewController].cold.1
+ ___block_literal_global.289
+ ___block_literal_global.291
- -[IMAAppPresenter _presentAppWithBundleIdentifier:completion:]
- _OBJC_CLASS_$_CKExpandedAppViewController
- _OBJC_IVAR_$_IMAAppPresenter._expandedAppViewController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CKExpandedAppViewControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CKExpandedAppViewControllerDelegate
- __OBJC_$_PROTOCOL_REFS_CKExpandedAppViewControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_CKExpandedAppViewControllerDelegate
- __OBJC_PROTOCOL_$_CKExpandedAppViewControllerDelegate
- ___60-[IMAAppPresenter hideAppViewControllerAnimated:completion:]_block_invoke_2
- ___62-[IMAAppPresenter _presentAppWithBundleIdentifier:completion:]_block_invoke
- ___62-[IMAAppPresenter _presentAppWithBundleIdentifier:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_literal_global.299
- ___block_literal_global.301
- _objc_msgSend$_presentAppWithBundleIdentifier:completion:
- _objc_msgSend$addNewGrabberView
- _objc_msgSend$addSwitcher
- _objc_msgSend$contentViewController
- _objc_msgSend$dismissCurrentExpandedBrowserAnimated:completion:
- _objc_msgSend$dismissExpandedAppViewController:animated:completion:
- _objc_msgSend$initWithConversation:plugin:
- _objc_msgSend$layer
- _objc_msgSend$presentExpandedAppViewController:animated:completion:
- _objc_msgSend$releaseOwnershipOfBrowserForConsumer:
- _objc_msgSend$requestOwnershipOfBrowserForConsumer:
- _objc_msgSend$setAddsVerticalPaddingForStatusBar:
- _objc_msgSend$setContentViewController:
- _objc_msgSend$setCornerRadius:
- _objc_msgSend$setExpanded:withReason:
- _objc_msgSend$setFadesOutDuringStickerDrag:
- _objc_msgSend$setPresentingViewController:
- _objc_msgSend$setUsesDimmingView:
- _objc_msgSend$showBrowserInSwitcherForPlugin:datasource:reloadData:
- _objc_msgSend$transitionToCollapsed
- _objc_msgSend$transitionToFullscreen
- _objc_msgSend$updateBrowserSessionForPlugin:datasource:
CStrings:
+ "Attempted to change expanded presentation style with app cards disabled. Bailing."
+ "Legacy expanded app presentation no longer supported"
+ "currentStickerViewController: alwaysPresentAppsExpanded is no longer supported. Returning nil."
+ "presentAppWithBundleIdentifier: tried to present an app when the app cards feature flag is disabled! Bailing."
- "@\"CKExpandedAppViewController\""
- "B24@0:8@\"<CKExpandedAppViewControllerProtocol>\"16"
- "CKExpandedAppViewControllerDelegate"
- "IMADockViewController delegate does not respond to -dismissExpandedAppViewController:animated:completion: even though -alwaysPresentAppsExpanded is YES."
- "_expandedAppViewController"
- "_presentAppWithBundleIdentifier:completion:"
- "addNewGrabberView"
- "contentViewController"
- "d24@0:8@\"<CKExpandedAppViewControllerProtocol>\"16"
- "dismissCurrentExpandedBrowserAnimated:completion:"
- "dismissExpandedAppViewController:animated:completion:"
- "expandedAppViewController:hasUpdatedLastTouchDate:"
- "expandedAppViewController:wantsToSwitchToPlugin:datasource:"
- "expandedAppViewControllerCollapsedContentHeight:"
- "expandedAppViewControllerCollapsedHeaderHeight:"
- "expandedAppViewControllerDidTransitionFromOrientation:toOrientation:"
- "expandedAppViewControllerShouldDismissOnDragSuccess:"
- "expandedAppViewControllerSwitcherDidSelectAppManager:"
- "expandedAppViewControllerSwitcherDidSelectAppStore:"
- "expandedAppViewControllerWantsToCollapse:"
- "initWithConversation:plugin:"
- "layer"
- "presentExpandedAppViewController:animated:completion:"
- "releaseOwnershipOfBrowserForConsumer:"
- "requestOwnershipOfBrowserForConsumer:"
- "setAddsVerticalPaddingForStatusBar:"
- "setContentViewController:"
- "setCornerRadius:"
- "setExpanded:withReason:"
- "setFadesOutDuringStickerDrag:"
- "setPresentingViewController:"
- "setUsesDimmingView:"
- "showBrowserInSwitcherForPlugin:datasource:reloadData:"
- "transitionToCollapsed"
- "transitionToFullscreen"
- "updateBrowserSessionForPlugin:datasource:"
- "v24@0:8@\"<CKExpandedAppViewControllerProtocol>\"16"
- "v32@0:8@\"<CKExpandedAppViewControllerProtocol>\"16@\"NSDate\"24"
- "v32@0:8q16q24"
- "v40@0:8@\"<CKExpandedAppViewControllerProtocol>\"16@\"IMBalloonPlugin\"24@\"IMBalloonPluginDataSource\"32"

```
