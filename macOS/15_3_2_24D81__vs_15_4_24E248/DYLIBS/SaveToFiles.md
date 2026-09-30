## SaveToFiles

> `/System/iOSSupport/System/Library/AccessibilityBundles/SaveToFiles.axbundle/Contents/MacOS/SaveToFiles`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x46f0
+2963.10.10.0.0
+  __TEXT.__text: 0x474c
   __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0x744
   __TEXT.__cstring: 0xd5f
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__gcc_except_tab: 0x124
   __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0x5c1
   __TEXT.__objc_methname: 0xc2a

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 784F71DC-BE60-3E0E-AC8E-35AAF15E7725
-  Functions: 148
-  Symbols:   562
+  UUID: 086DEAC5-A076-30DF-A7D4-65CF265F4DF6
+  Functions: 149
+  Symbols:   563
   CStrings:  480
 
Symbols:
+ +[AXDocumentManagerUICoreSaveToFilesGlue accessibilityInitializeBundle].cold.1
Functions:
~ -[DOCSearchControllerAccessibility searchBarTextDidEndEditing:] : 284 -> 288
~ -[DOCSidebarItemCellAccessibility accessibilityCustomActions] : 384 -> 380
~ ___61-[DOCSidebarItemCellAccessibility accessibilityCustomActions]_block_invoke : 412 -> 416
~ -[DOCSidebarItemCellAccessibility accessibilityTraits] : 148 -> 152
~ -[DOCFilenameViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 284
~ ___84-[DOCFilenameViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 216 -> 220
~ +[AXDocumentManagerUICoreSaveToFilesGlue accessibilityInitializeBundle] : 40 -> 44
~ -[DOCItemCollectionCellAccessibility accessibilityIdentifier] : 384 -> 388
~ -[DOCItemCollectionCellAccessibility _axAttrTitle] : 176 -> 180
~ -[DOCItemCollectionCellAccessibility _axCustomActionsFromUIMenu:] : 876 -> 880
~ -[DOCItemCollectionCellAccessibility _accessibilityItemCollectionViewController] : 164 -> 168
~ -[DOCItemCollectionCellAccessibility accessibilityScrollToVisible] : 224 -> 228
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
