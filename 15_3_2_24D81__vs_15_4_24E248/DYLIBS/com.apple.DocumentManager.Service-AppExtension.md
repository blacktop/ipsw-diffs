## com.apple.DocumentManager.Service-AppExtension

> `/System/iOSSupport/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/Contents/MacOS/com.apple.DocumentManager.Service-AppExtension`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x4754
+2963.10.10.0.0
+  __TEXT.__text: 0x47b0
   __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0x704
   __TEXT.__cstring: 0xebb
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__gcc_except_tab: 0x124
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0x571
   __TEXT.__objc_methname: 0xc2d
   __TEXT.__objc_methtype: 0x70

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B5BF8C0-7453-36D7-B7BF-B2B03C09819E
-  Functions: 144
-  Symbols:   546
+  UUID: 8B170E8C-ACBB-38CE-9363-4AEBD7D4568A
+  Functions: 145
+  Symbols:   547
   CStrings:  480
 
Symbols:
+ +[AXDocumentManagerServiceGlue accessibilityInitializeBundle].cold.1
Functions:
~ +[AXDocumentManagerServiceGlue accessibilityInitializeBundle] : 40 -> 44
~ -[DOCSidebarItemCellAccessibility accessibilityCustomActions] : 384 -> 380
~ ___61-[DOCSidebarItemCellAccessibility accessibilityCustomActions]_block_invoke : 412 -> 416
~ -[DOCSidebarItemCellAccessibility accessibilityTraits] : 148 -> 152
~ -[DOCFilenameViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 284
~ ___84-[DOCFilenameViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 216 -> 220
~ -[DOCItemCollectionCellAccessibility accessibilityIdentifier] : 384 -> 388
~ -[DOCItemCollectionCellAccessibility _axAttrTitle] : 176 -> 180
~ -[DOCItemCollectionCellAccessibility _axCustomActionsFromUIMenu:] : 876 -> 880
~ -[DOCItemCollectionCellAccessibility _accessibilityItemCollectionViewController] : 164 -> 168
~ -[DOCItemCollectionCellAccessibility accessibilityScrollToVisible] : 224 -> 228
~ -[DOCPickerFilenameViewAccessibility _accessibilityLoadAccessibilityInformation] : 180 -> 184
~ -[DOCItemCollectionGridCellAccessibility _accessibilitySubviewIsVisible:] : 180 -> 184
~ -[DOCItemCollectionGridCellAccessibility _axAttrTitle] : 224 -> 228
~ -[DOCItemCollectionGridCellAccessibility accessibilityLabel] : 1012 -> 1016
~ -[DOCItemCollectionGridCellAccessibility accessibilityActivationPoint] : 264 -> 268
~ -[DOCItemCollectionGridCellAccessibility accessibilityDropPointDescriptors] : 444 -> 448
~ -[DOCItemCollectionGridCellAccessibility _accessibilityIsFolder] : 136 -> 140
~ -[DOCItemCollectionListCellAccessibility _axAttrTitle] : 176 -> 180
~ -[DOCItemCollectionListCellAccessibility accessibilityLabel] : 1260 -> 1264
~ -[DOCItemCollectionListCellAccessibility _accessibilityIsFolder] : 136 -> 140
~ -[UIDocumentBrowserActionBarButtonAccessibility accessibilityLabel] : 244 -> 248

```
