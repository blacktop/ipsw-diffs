## IntentsUICardKitProviderSupport

> `/System/Library/PrivateFrameworks/IntentsUICardKitProviderSupport.framework/IntentsUICardKitProviderSupport`

```diff

-3500.5.1.0.0
-  __TEXT.__text: 0x3d84
-  __TEXT.__auth_stubs: 0x370
+3520.8.1.0.0
+  __TEXT.__text: 0x3fc4
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_methlist: 0x904
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__gcc_except_tab: 0x80
   __TEXT.__cstring: 0x14b
   __TEXT.__oslogstring: 0x46b
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0x34f
   __TEXT.__objc_methname: 0x17c4
   __TEXT.__objc_methtype: 0x8f8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x2598

   - /System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9E18E50-2367-32D9-96BE-498E98BA27A9
+  UUID: 2DE11EA3-0099-31C9-B8FD-7E380187C240
   Functions: 112
-  Symbols:   697
+  Symbols:   691
   CStrings:  363
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ +[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:] : 288 -> 264
~ ___126+[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:]_block_invoke : 276 -> 272
~ ___126+[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:]_block_invoke_2 : 300 -> 308
~ ___126+[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:]_block_invoke_4 : 116 -> 112
~ -[INUICKPSynchronousRemoteViewController setRemoteViewController:] : 236 -> 260
~ -[INUICKPSynchronousRemoteViewController cachedRepresentedParameters] : 100 -> 112
~ -[INUICKPSynchronousRemoteViewController _interaction] : 100 -> 112
~ -[INUICKPSynchronousRemoteViewController _minimumSizesBySystemVersion] : 272 -> 288
~ -[INUICKPSynchronousRemoteViewController maximumSizesBySystemVersionForRemoteViewController:] : 308 -> 328
~ -[INUICKPSynchronousRemoteViewController interfaceSectionsForRemoteViewController:] : 76 -> 84
~ -[INUICKPSynchronousRemoteViewController preferredContentSize] : 120 -> 128
~ +[INUICKPInterfaceSectionConverter generateInterfaceSectionsFromCard:] : 488 -> 500
~ +[INUICKPInterfaceSectionConverter _interactionMatchingCardSection:inCard:] : 80 -> 88
~ +[INUICKPInterfaceSectionConverter _intrinsicInteractiveBehaviorForCardSection:] : 496 -> 516
~ -[INUICKPSynchronousRemoteView sizeThatFits:] : 80 -> 84
~ -[INUICKPSynchronousRemoteView layoutSubviews] : 292 -> 296
~ -[INUICKPCardSectionViewProvider providerIdentifier] : 16 -> 64
~ -[INUICKPCardSectionViewProvider vetoDisplayOfCardSection:] : 208 -> 212
~ ___59-[INUICKPCardSectionViewProvider vetoDisplayOfCardSection:]_block_invoke : 180 -> 192
~ +[INUICKPCardSectionViewProvider requestInstanceFromDefaultAllocatorWithCard:delegate:reply:] : 188 -> 180
~ +[INUICKPCardSectionViewProvider requestInstanceWithCard:delegate:allocator:reply:] : 728 -> 720
~ ___83+[INUICKPCardSectionViewProvider requestInstanceWithCard:delegate:allocator:reply:]_block_invoke : 148 -> 152
~ -[INUICKPCardSectionViewProvider boundingWidthForViewControllerAllocator:] : 128 -> 136
~ +[INUICKPCardSectionViewProvider _viewConfigurationsFromAllocator:] : 616 -> 640
~ -[INUICKPCardSectionViewProvider setAllocator:] : 12 -> 64
~ -[INUICKPExtensionCardSectionViewController desiresInteractivity:] : 96 -> 100
~ -[INUICKPExtensionCardSectionViewController remoteViewController:requestsHandlingOfIntent:] : 108 -> 112
~ -[INUICKPExtensionCardSectionViewController remoteViewControllerWillBeginEditing:] : 108 -> 112
~ -[INUICKPExtensionCardSectionViewController cardEventDidOccur:withIdentifier:userInfo:] : 680 -> 700
~ -[INUICKPEntryPoint providerIdentifier] : 16 -> 64
~ -[INParameter(CardKit) isSubParameterOf:] : 548 -> 584
~ -[INUICKPCardInterfaceSection isEqual:] : 264 -> 276
~ -[INUICKPCardInterfaceSection isWildCardSection] : 104 -> 112
~ -[INUICKPCardInterfaceSection setCardSection:] : 20 -> 80
~ -[INUICKPSynchronousRemoteViewControllerAllocator performAllocationsFromInteraction:initialInterfaceSections:completion:] : 276 -> 264
~ -[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:] : 1168 -> 1128
~ ___121-[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:]_block_invoke_2 : 384 -> 396
~ ___121-[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:]_block_invoke_3 : 564 -> 580
~ -[INUICKPSynchronousRemoteViewControllerAllocator _unhandledParametersForInterfaceSection:] : 520 -> 528
~ -[INUICKPSynchronousRemoteViewControllerAllocator boundingWidthForSynchronousRemoteViewController:] : 72 -> 76
~ -[INUICKPSynchronousRemoteViewControllerAllocator setInteraction:] : 12 -> 64
~ __INUICKPInteractionMatchingCardSectionInCard : 80 -> 88
~ __INUICKPIntrinsicInteractiveBehaviorForCardSection : 496 -> 516
~ _INUICKPInterfaceSectionsFromCard : 564 -> 576
~ +[NSObject(IntentsUICardKitProvider) inuickp_interactiveBehaviorPrecedenceOrder] : 68 -> 84
~ -[NSObject(IntentsUICardKitProvider) inuickp_intrinsicInteractiveBehavior] : 512 -> 528
~ -[INUICKPSynchronousRemoteViewController remoteViewControllerServiceDidTerminate:].cold.1 : 208 -> 216

```
