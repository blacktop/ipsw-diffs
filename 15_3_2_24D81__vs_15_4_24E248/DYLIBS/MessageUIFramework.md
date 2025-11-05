## MessageUIFramework

> `/System/iOSSupport/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/Versions/A/MessageUIFramework`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x6990
+2963.10.10.0.0
+  __TEXT.__text: 0x6a0c
   __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0xcb4
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x165b
   __TEXT.__oslogstring: 0x3d
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__unwind_info: 0x2f0
   __TEXT.__objc_classname: 0xb71
   __TEXT.__objc_methname: 0x1110
   __TEXT.__objc_methtype: 0x16e

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3DC613F-48FA-3F02-A345-4429B878313B
-  Functions: 252
-  Symbols:   886
+  UUID: 73D218FC-253A-3BEE-AC80-C267D73760BE
+  Functions: 255
+  Symbols:   889
   CStrings:  783
 
Symbols:
+ -[MFComposeImageSizeViewAccessibility setSizeDescription:forScale:].cold.1
+ -[_MFAtomFieldEditorAccessibility _accessibilityCanBeFirstResponder].cold.1
+ __46+[AXMessageUIFrameworkGlue _webKitInitialized]_block_invoke.cold.1
Functions:
~ ___46+[AXMessageUIFrameworkGlue _webKitInitialized]_block_invoke : 40 -> 44
~ -[WKContentViewAccessibility__MessageUI__WebKit _accessibilityLoadAccessibilityInformation] : 268 -> 264
~ -[MFComposeActionCardTitleViewAccessibility _accessibilityLoadAccessibilityInformation] : 740 -> 744
~ -[MFComposeImageSizeViewAccessibility setSizeDescription:forScale:] : 580 -> 564
~ -[MFComposeSubjectViewAccessibility setNotifyOptionSelected:] : 144 -> 148
~ -[MFComposeTextColorButtonAccessibility accessibilityValue] : 180 -> 184
~ -[MFMailComposeViewAccessibility dragSource:draggableItemsAtPoint:] : 232 -> 236
~ -[MFMailComposeViewAccessibility dropTarget:dragDidMoveToPoint:] : 1008 -> 1016
~ -[MFModernAddressAtomAccessibility accessibilityLabel] : 468 -> 472
~ -[MFModernLabelledAtomListAccessibility _accessibilitySpeakThisString] : 228 -> 232
~ -[MFModernLabelledAtomListAccessibility accessibilityElements] : 232 -> 236
~ -[MFPhotoPickerControllerAccessibility _accessibilityLoadAccessibilityInformation] : 252 -> 256
~ -[MFPhotoPickerControllerAccessibility collectionView:cellForItemAtIndexPath:] : 332 -> 336
~ -[MFPhotoPickerControllerAccessibility viewDidLoad] : 196 -> 200
~ -[UITextViewAccessibility__MessageUI__UIKit accessibilityFrame] : 308 -> 312
~ -[_MFAtomFieldEditorAccessibility _axAtomTextViewAncestor] : 144 -> 148
~ -[_MFAtomFieldEditorAccessibility accessibilityTraits] : 120 -> 128
~ -[_MFAtomFieldEditorAccessibility accessibilityPlaceholderValue] : 192 -> 196
~ -[_MFAtomFieldEditorAccessibility _accessibilityCanBeFirstResponder] : 220 -> 208
~ -[_MFAtomTextViewAccessibility accessibilityValue] : 544 -> 548

```
