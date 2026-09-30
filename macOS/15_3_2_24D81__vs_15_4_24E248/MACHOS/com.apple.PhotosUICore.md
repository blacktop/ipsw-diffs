## com.apple.PhotosUICore

> `/System/Library/Accessibility/BundlesBase/com.apple.PhotosUICore.axbundle/Versions/A/com.apple.PhotosUICore`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0x6a60
+287.6.4.0.0
+  __TEXT.__text: 0x6aac
   __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x12c0
-  __TEXT.__objc_methlist: 0x924
+  __TEXT.__objc_methlist: 0xd98
   __TEXT.__objc_classname: 0x825
   __TEXT.__cstring: 0x1289
-  __TEXT.__objc_methname: 0x1910
+  __TEXT.__objc_methname: 0x192e
   __TEXT.__objc_methtype: 0x606
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__gcc_except_tab: 0x148
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x2c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA.__objc_const: 0x2828
-  __DATA.__objc_selrefs: 0x590
+  __DATA.__objc_const: 0x2038
+  __DATA.__objc_selrefs: 0x7f8
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x28

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5AA15926-6CDF-30FC-A75E-71DE30C04AAC
-  Functions: 195
-  Symbols:   762
-  CStrings:  780
+  UUID: 707A9419-44A8-3838-BED4-33F589B163D1
+  Functions: 196
+  Symbols:   763
+  CStrings:  782
 
Symbols:
+ +[PXGReusableAXInfoAccessibility _accessibilityImageDescriptionQueue].cold.1
Functions:
~ -[HomeSectionTungstenLayoutAccessibility _accessibilityPhotosGroupRole] : 272 -> 276
~ -[HomeSectionTungstenLayoutAccessibility _accessibilityPhotosCustomActions] : 400 -> 396
~ ___75-[HomeSectionTungstenLayoutAccessibility _accessibilityPhotosCustomActions]_block_invoke : 244 -> 248
~ -[HomeSectionTungstenLayoutAccessibility _accessibilitySectionHeaderTungstenLayout] : 412 -> 416
~ -[HomeElementTungstenLayoutAccessibility _accessibilityPhotosGroupRole] : 264 -> 272
~ ___57-[PXGItemsLayoutAccessibility _updateFocusedItemIfNeeded]_block_invoke : 108 -> 112
~ -[PXCuratedLibrarySectionHeaderLayoutAccessibility _accessibilityRoleForSpriteIndex:] : 224 -> 228
~ -[HomeAlbumCellTungstenLayoutAccessibility axGroup:didRequestToPerformAction:userInfo:] : 508 -> 512
~ -[HomeAlbumCellTungstenLayoutAccessibility _accessibilityFrameForSpriteIndex:] : 216 -> 220
~ -[PXPhotosLayoutAccessibility axGroup:didChange:userInfo:] : 376 -> 380
~ -[PXNSScrollViewAccessibility accessibilityContents] : 252 -> 256
~ -[PXFeedSectionContentLayoutAccessibility axGroup:didRequestToPerformAction:userInfo:] : 968 -> 956
~ -[PXFeedSectionContentLayoutAccessibility _accessibilitySectionObjectForSpriteIndex:] : 516 -> 520
~ -[PXFeedSectionContentLayoutAccessibility _handlePresentMenuActionForIndex:atLocation:inView:] : 712 -> 720
~ -[_PXScrollDocumentViewAccessibility accessibilityFocusedUIElement] : 724 -> 736
~ +[PXGReusableAXInfoAccessibility _accessibilityImageDescriptionQueue] : 84 -> 68
~ -[PXGReusableAXInfoAccessibility _accessibilityContainingLayout] : 192 -> 196
~ ___71-[PXGReusableAXInfoAccessibility accessibilityEmbeddedImageDescription]_block_invoke : 504 -> 512
~ -[PXPhotosViewUXInteractionResponderAccessibility accessibilityFocusedUIElement] : 544 -> 548
~ -[HomePersonCellTungstenLayoutAccessibility axGroup:didRequestToPerformAction:userInfo:] : 508 -> 512
~ -[PXFeedContentLayoutAccessibility axLocalizedLabel] : 480 -> 484
~ ___64-[PXFeedContentLayoutAccessibility _updateFeedSelectionSnapshot]_block_invoke : 396 -> 408
~ -[HomeCellTungstenLayoutAccessibility axGroup:didRequestToPerformAction:userInfo:] : 508 -> 512
~ -[PXGLayoutAccessibility axContentInfoAtSpriteIndex:] : 704 -> 684
+ +[PXGReusableAXInfoAccessibility _accessibilityImageDescriptionQueue].cold.1
CStrings:
+ "focalLength"
+ "focalLengthIn35mm"

```
