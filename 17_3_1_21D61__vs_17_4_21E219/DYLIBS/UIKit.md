## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

```diff

-2909.1.4.18.0
-  __TEXT.__text: 0x16ece0
+2909.23.0.0.0
+  __TEXT.__text: 0x16f968
   __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_methlist: 0xdf08
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x171e0
+  __TEXT.__objc_methlist: 0xdf30
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x17319
   __TEXT.__oslogstring: 0x2075
   __TEXT.__gcc_except_tab: 0x1e84
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x78
   __TEXT.__unwind_info: 0x2a74
   __TEXT.__objc_classname: 0x86cc
-  __TEXT.__objc_methname: 0x15056
-  __TEXT.__objc_methtype: 0x2187
+  __TEXT.__objc_methname: 0x1511c
+  __TEXT.__objc_methtype: 0x21ed
   __TEXT.__objc_stubs: 0xf9c0
   __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0x1cf8

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x11498
-  __DATA_CONST.__objc_selrefs: 0x53a0
+  __DATA_CONST.__objc_const: 0x114b8
+  __DATA_CONST.__objc_selrefs: 0x53b8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x7e8
+  __DATA_CONST.__objc_superrefs: 0x9c8
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__objc_const: 0xe5e0
-  __AUTH_CONST.__cfstring: 0x1bde0
+  __AUTH_CONST.__cfstring: 0x1bfc0
   __AUTH_CONST.__const: 0x1380
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0xa38
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x7e8
-  __DATA.__objc_superrefs: 0x9c8
+  __AUTH.__objc_data: 0x8c0
   __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x620
   __DATA.__bss: 0x266
-  __DATA_DIRTY.__objc_data: 0xf5a0
+  __DATA_DIRTY.__objc_data: 0xf6e0
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5481
-  Symbols:   18714
-  CStrings:  7978
+  Functions: 5487
+  Symbols:   18726
+  CStrings:  8001
 
Symbols:
+ -[UIIndexBarAccessoryViewAccessibility _didSelectEntry:atIndex:location:]
+ -[UIKeyboardImplAccessibility touchUpdateLastUsedInputModeAction]
+ -[UIScrollViewAccessibility _axPageAlignedContentOffsetForPoint:forValidation:]
+ -[UITableViewCellEditControlAccessibility _multiSelectNotSelectedImage]
+ -[UITableViewCellEditControlAccessibility _multiSelectSelectedImage]
+ GCC_except_table40
+ GCC_except_table65
+ GCC_except_table71
+ GCC_except_table76
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.740
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.741
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.742
+ ___54-[UITextViewAccessibility _accessibilityActivateLink:]_block_invoke_3
+ ___56-[_UIEditMenuListViewAccessibility _reloadMenuAnimated:]_block_invoke
+ ___60-[UITextViewAccessibility _accessibilityUserTestingChildren]_block_invoke.520
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.264
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.277
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.503
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.504
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.373
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.374
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.361
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.362
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.645
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.646
+ ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.460
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.523
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.524
+ ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.585
+ ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.291
+ ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.303
+ ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.509
+ ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.519
+ ___93-[_UIRemoteViewControllerAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.330
+ ___block_literal_global.1858
+ ___block_literal_global.1864
+ ___block_literal_global.2421
+ ___block_literal_global.243
+ ___block_literal_global.249
+ ___block_literal_global.252
+ ___block_literal_global.257
+ ___block_literal_global.291
+ ___block_literal_global.295
+ ___block_literal_global.300
+ ___block_literal_global.301
+ ___block_literal_global.3011
+ ___block_literal_global.3013
+ ___block_literal_global.3018
+ ___block_literal_global.3030
+ ___block_literal_global.3056
+ ___block_literal_global.3064
+ ___block_literal_global.313
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.368
+ ___block_literal_global.372
+ ___block_literal_global.376
+ ___block_literal_global.378
+ ___block_literal_global.383
+ ___block_literal_global.391
+ ___block_literal_global.394
+ ___block_literal_global.405
+ ___block_literal_global.413
+ ___block_literal_global.443
+ ___block_literal_global.466
+ ___block_literal_global.468
+ ___block_literal_global.479
+ ___block_literal_global.497
+ ___block_literal_global.499
+ ___block_literal_global.506
+ ___block_literal_global.526
+ ___block_literal_global.536
+ ___block_literal_global.540
+ ___block_literal_global.548
+ ___block_literal_global.558
+ ___block_literal_global.570
+ ___block_literal_global.574
+ ___block_literal_global.583
+ ___block_literal_global.587
+ ___block_literal_global.590
+ ___block_literal_global.593
+ ___block_literal_global.595
+ ___block_literal_global.609
+ ___block_literal_global.612
+ ___block_literal_global.613
+ ___block_literal_global.618
+ ___block_literal_global.635
+ ___block_literal_global.638
+ ___block_literal_global.644
+ ___block_literal_global.648
+ ___block_literal_global.676
+ ___block_literal_global.679
+ ___block_literal_global.682
+ ___block_literal_global.699
+ ___block_literal_global.728
+ ___block_literal_global.790
+ ___block_literal_global.796
+ ___block_literal_global.848
+ ___block_literal_global.850
+ ___block_literal_global.885
+ ___block_literal_global.891
+ ___block_literal_global.894
+ ___block_literal_global.908
+ ___block_literal_global.909
+ ___block_literal_global.911
+ ___block_literal_global.926
+ ___block_literal_global.931
+ ___block_literal_global.953
+ ___block_literal_global.962
+ ___block_literal_global.996
+ __unnamed_array_storage.274
+ __unnamed_array_storage.338
+ __unnamed_array_storage.408
+ __unnamed_array_storage.418
+ __unnamed_array_storage.419
+ __unnamed_array_storage.969
+ __unnamed_array_storage.976
+ __unnamed_array_storage.977
+ __unnamed_array_storage.991
+ __unnamed_array_storage.992
+ _objc_msgSend$_didSelectEntry:atIndex:location:
+ _objc_msgSend$_setAccessibilityShouldUseViewHierarchyForFindingScrollParent:
- -[UIIndexBarAccessoryViewAccessibility _didSelectEntry:atIndex:]
- -[UIScrollViewAccessibility _axPageAlignedContentOffsetForPoint:]
- GCC_except_table39
- GCC_except_table64
- GCC_except_table70
- GCC_except_table75
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.715
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.716
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.717
- ___60-[UITextViewAccessibility _accessibilityUserTestingChildren]_block_invoke.489
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.240
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.253
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.479
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.480
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.349
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.350
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.337
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.338
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.621
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.622
- ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.436
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.499
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.500
- ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.557
- ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.267
- ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.279
- ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.485
- ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.495
- ___93-[_UIRemoteViewControllerAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.306
- ___block_literal_global.1834
- ___block_literal_global.1840
- ___block_literal_global.219
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.228
- ___block_literal_global.229
- ___block_literal_global.233
- ___block_literal_global.2397
- ___block_literal_global.267
- ___block_literal_global.276
- ___block_literal_global.289
- ___block_literal_global.2987
- ___block_literal_global.2989
- ___block_literal_global.2994
- ___block_literal_global.3006
- ___block_literal_global.3008
- ___block_literal_global.3040
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.328
- ___block_literal_global.333
- ___block_literal_global.335
- ___block_literal_global.336
- ___block_literal_global.340
- ___block_literal_global.344
- ___block_literal_global.348
- ___block_literal_global.354
- ___block_literal_global.367
- ___block_literal_global.370
- ___block_literal_global.389
- ___block_literal_global.418
- ___block_literal_global.419
- ___block_literal_global.420
- ___block_literal_global.451
- ___block_literal_global.455
- ___block_literal_global.473
- ___block_literal_global.478
- ___block_literal_global.482
- ___block_literal_global.492
- ___block_literal_global.498
- ___block_literal_global.512
- ___block_literal_global.524
- ___block_literal_global.534
- ___block_literal_global.550
- ___block_literal_global.559
- ___block_literal_global.563
- ___block_literal_global.566
- ___block_literal_global.569
- ___block_literal_global.571
- ___block_literal_global.584
- ___block_literal_global.585
- ___block_literal_global.589
- ___block_literal_global.594
- ___block_literal_global.607
- ___block_literal_global.611
- ___block_literal_global.614
- ___block_literal_global.620
- ___block_literal_global.624
- ___block_literal_global.652
- ___block_literal_global.655
- ___block_literal_global.658
- ___block_literal_global.674
- ___block_literal_global.703
- ___block_literal_global.766
- ___block_literal_global.772
- ___block_literal_global.823
- ___block_literal_global.825
- ___block_literal_global.860
- ___block_literal_global.866
- ___block_literal_global.869
- ___block_literal_global.881
- ___block_literal_global.883
- ___block_literal_global.884
- ___block_literal_global.886
- ___block_literal_global.901
- ___block_literal_global.928
- ___block_literal_global.937
- ___block_literal_global.971
- __unnamed_array_storage.250
- __unnamed_array_storage.314
- __unnamed_array_storage.384
- __unnamed_array_storage.394
- __unnamed_array_storage.395
- __unnamed_array_storage.944
- __unnamed_array_storage.951
- __unnamed_array_storage.952
- __unnamed_array_storage.966
- __unnamed_array_storage.967
- _objc_msgSend$_didSelectEntry:atIndex:
- _objc_msgSend$setDisablesUpdateLastUsedInputModeTimer:
CStrings:
+ "B48@0:8@16q24{CGPoint=dd}32"
+ "T@\"NSArray\",?,R,C,N,G_linearFocusMovementSequences"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"UIFocusEffect\",?,R,C,N"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIView\",?,R,N"
+ "T@\"UIView\",?,R,W,N"
+ "T@,?,R,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R,N"
+ "TB,?,R,N,G_isEligibleForFocusInteraction"
+ "TB,?,R,N,G_isEligibleForFocusOcclusion"
+ "Tq,?,N"
+ "Tq,?,R,N"
+ "Tq,?,R,N,G_preferredFocusMovementStyle"
+ "_UITextInteractableLinkItem"
+ "_didSelectEntry:atIndex:location:"
+ "_ignoresTouches"
+ "_multiSelectNotSelectedImage"
+ "_multiSelectSelectedImage"
+ "_setAccessibilityShouldUseViewHierarchyForFindingScrollParent:"
+ "caretTransformForPosition:"
+ "circle"
+ "link"
+ "menuView"
+ "nextResultButton"
+ "previousResultButton"
+ "search.next.button"
+ "search.previous.button"
+ "selected"
+ "text.option.type.cancel.label"
+ "text.option.type.revert.label"
+ "touchUpdateLastUsedInputModeAction"
+ "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
+ "{CGAffineTransform=dddddd}24@0:8@16"
- "B32@0:8@16q24"
- "T@\"NSArray\",R,C,N,G_linearFocusMovementSequences"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R,C,N"
- "T@\"UIFocusEffect\",R,C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@\"UIView\",R,N"
- "T@\"UIView\",R,W,N"
- "T@,R,N"
- "TB,N"
- "TB,N,GisSecureTextEntry"
- "TB,R,N,G_isEligibleForFocusInteraction"
- "TB,R,N,G_isEligibleForFocusOcclusion"
- "Tq,N"
- "Tq,R,N"
- "Tq,R,N,G_preferredFocusMovementStyle"
- "_didSelectEntry:atIndex:"
- "setDisablesUpdateLastUsedInputModeTimer:"

```
