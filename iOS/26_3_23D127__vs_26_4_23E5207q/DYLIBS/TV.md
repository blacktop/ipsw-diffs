## TV

> `/System/Library/AccessibilityBundles/TV.axbundle/TV`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x297c
-  __TEXT.__auth_stubs: 0x2e0
+3005.16.0.0.0
+  __TEXT.__text: 0x2b40
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x510
   __TEXT.__cstring: 0x870
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2d0
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0xb20
   __AUTH_CONST.__objc_const: 0x1050

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A6B4B42-6312-37E3-998F-4AAF26A0BC87
+  UUID: 4569B671-C596-31C3-BF73-767C9EA2181F
   Functions: 98
-  Symbols:   499
+  Symbols:   495
   CStrings:  322
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ ___44+[AXTVAppGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___44+[AXTVAppGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___44+[AXTVAppGlue accessibilityInitializeBundle]_block_invoke_4 : 352 -> 360
~ _accessibilityLocalizedString : 160 -> 168
~ +[VideosChaptersTableViewControllerAccessibility _accessibilityPerformValidations:] : 172 -> 184
~ -[VideosChaptersTableViewControllerAccessibility tableView:cellForRowAtIndexPath:] : 692 -> 716
~ ___82-[VideosChaptersTableViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke : 104 -> 108
~ -[VideosDetailHeaderViewAccessibility _axApplyPlayButtonLabel] : 128 -> 136
~ -[VideosDetailHeaderViewAccessibility playButton] : 104 -> 108
~ +[VideosDetailViewControllerAccessibility _accessibilityPerformValidations:] : 260 -> 272
~ -[VideosDetailViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 228 -> 244
~ -[VideosDetailViewControllerAccessibility _updateContentInsets] : 536 -> 560
~ +[VideosPlaybackViewControllerAccessibility _accessibilityPerformValidations:] : 336 -> 344
~ -[VideosPlaybackViewControllerAccessibility _axAnnounceControlsVisible:] : 144 -> 148
~ -[VideosPlaybackViewControllerAccessibility _overlayIdleTimerFired:] : 368 -> 380
~ +[VideosPosterCollectionViewCellAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[VideosPosterCollectionViewCellAccessibility _axIsDeletable] : 64 -> 68
~ -[VideosPosterCollectionViewCellAccessibility accessibilityLabel] : 572 -> 636
~ -[VideosPosterCollectionViewCellAccessibility accessibilityHint] : 68 -> 72
~ -[VideosPosterCollectionViewCellAccessibility accessibilityActivationPoint] : 136 -> 140
~ -[VideosRelatedStoreItemsCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:] : 336 -> 352
~ ___102-[VideosRelatedStoreItemsCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke : 180 -> 192
~ -[VideosRelatedStoreItemsCollectionViewControllerAccessibility _createCollectionView] : 104 -> 108
~ +[VideosRentalCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[VideosRentalCollectionViewCellAccessibility accessibilityLabel] : 272 -> 296
~ +[VideosTVEpisodesTableViewControllerAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[VideosTVEpisodesTableViewControllerAccessibility configureCell:atIndexPath:withEntity:invalidationContext:] : 528 -> 532
~ ___109-[VideosTVEpisodesTableViewControllerAccessibility configureCell:atIndexPath:withEntity:invalidationContext:]_block_invoke : 88 -> 92
~ -[VideosUICollectionViewAccessibility _accessibilityContentInset] : 416 -> 428
~ ___65-[VideosUICollectionViewAccessibility _accessibilityContentInset]_block_invoke : 148 -> 156
~ -[VideosUICollectionViewAccessibility _accessibilityOtherCollectionViewItems] : 412 -> 432
~ ___77-[VideosUICollectionViewAccessibility _accessibilityOtherCollectionViewItems]_block_invoke : 124 -> 128
~ +[VideosUITableViewAccessibility _accessibilityPerformValidations:] : 112 -> 120
~ -[VideosUITableViewAccessibility _accessibilitySupplementaryHeaderViews] : 272 -> 292
~ ___72-[VideosUITableViewAccessibility _accessibilitySupplementaryHeaderViews]_block_invoke : 80 -> 84
~ -[VideosUIViewAccessibility _accessibilityParentForFindingScrollParent] : 176 -> 188
~ +[_TVInfoCellViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[_TVInfoCellViewAccessibility accessibilityLabel] : 304 -> 328
~ -[VideosUITableViewCellAccessibility _accessibilityShouldBypassScrollToVisibleWithChild] : 64 -> 68
~ ___88-[VideosUITableViewCellAccessibility _accessibilityShouldBypassScrollToVisibleWithChild]_block_invoke : 80 -> 84

```
