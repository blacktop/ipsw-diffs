## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-174.104.0.0.0
-  __TEXT.__text: 0x32b5d4
+175.0.0.0.0
+  __TEXT.__text: 0x32c61c
   __TEXT.__auth_stubs: 0x2cf0
-  __TEXT.__objc_methlist: 0x3bed4
-  __TEXT.__const: 0x6654
+  __TEXT.__objc_methlist: 0x3c014
+  __TEXT.__const: 0x6664
   __TEXT.__cstring: 0x1b42f
   __TEXT.__gcc_except_tab: 0x3e64
   __TEXT.__oslogstring: 0xdd80

   __TEXT.__swift5_assocty: 0x318
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x98
-  __TEXT.__swift5_capture: 0xfd8
+  __TEXT.__swift5_capture: 0xffc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe3b0
+  __TEXT.__unwind_info: 0xe3e0
   __TEXT.__eh_frame: 0x990
-  __TEXT.__objc_classname: 0x6ddb
-  __TEXT.__objc_methname: 0x9a221
+  __TEXT.__objc_classname: 0x6ddd
+  __TEXT.__objc_methname: 0x9a539
   __TEXT.__objc_methtype: 0x19352
-  __TEXT.__objc_stubs: 0x594e0
+  __TEXT.__objc_stubs: 0x59660
   __DATA_CONST.__got: 0x2260
   __DATA_CONST.__const: 0x96d0
   __DATA_CONST.__objc_classlist: 0x1270
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b940
+  __DATA_CONST.__objc_selrefs: 0x1b9b0
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe38
   __DATA_CONST.__objc_arraydata: 0x6d8
   __AUTH_CONST.__auth_got: 0x1688
-  __AUTH_CONST.__const: 0x62e8
+  __AUTH_CONST.__const: 0x6360
   __AUTH_CONST.__cfstring: 0x15ca0
-  __AUTH_CONST.__objc_const: 0x55258
+  __AUTH_CONST.__objc_const: 0x553f8
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x6178
   __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x3b18
+  __DATA.__objc_ivar: 0x3b34
   __DATA.__data: 0x8848
   __DATA.__bss: 0x21f8
   __DATA.__common: 0x58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5D9E18E7-AE25-3D9D-A6EC-7FD716A2EFE7
-  Functions: 22498
-  Symbols:   64133
-  CStrings:  30611
+  UUID: 3D078450-4DEF-3E69-8C04-9769FEE93D6E
+  Functions: 22529
+  Symbols:   64205
+  CStrings:  30635
 
Symbols:
+ -[SBFloatingDockViewController contentVisibility]
+ -[SBFloatingDockViewController setContentVisibility:]
+ -[SBHClockApplicationIconImageView effectiveDate]
+ -[SBHClockApplicationIconImageView effectiveOverrideDateOffset]
+ -[SBHClockApplicationIconImageView effectiveOverrideDate]
+ -[SBHClockApplicationIconImageView effectivelyHidesSecondsHand]
+ -[SBHClockApplicationIconImageView hidesSecondsHand]
+ -[SBHClockApplicationIconImageView overrideDateOffset]
+ -[SBHClockApplicationIconImageView overrideDate]
+ -[SBHClockApplicationIconImageView setHidesSecondsHand:]
+ -[SBHClockApplicationIconImageView setOverrideDate:]
+ -[SBHClockApplicationIconImageView setOverrideDateOffset:]
+ -[SBHIconManager iconDragManager:duplicateIconBehaviorInDragSession:]
+ -[SBIcon shouldDim]
+ -[SBIconDragContext createdFileStackIcons]
+ -[SBIconDragContext duplicateIconBehavior]
+ -[SBIconDragContext setCreatedFileStackIcons:]
+ -[SBIconDragContext setDuplicateIconBehavior:]
+ -[SBIconDragManager createFileStackIconsIfNecessary:forDragDropSession:]
+ -[SBIconDragManager createFileStackIconsIfNecessary:forDragDropSession:].cold.1
+ -[SBIconDragManager duplicateIconBehavior]
+ -[SBIconDragManager duplicateIconsIfNecessary:forDragDropSession:]
+ -[SBIconDragManager handleDuplicateIconsBeforePerformingIconDropWithDraggedIcons:dropSession:]
+ -[SBIconDragManager hideableIconsForDraggedIcons:iconLocation:dragIdentifier:]
+ -[SBIconDragManager modifyIconsInDragIfNecessaryForDragDropSession:]
+ -[SBIconDragManager setDuplicateIconBehavior:]
+ -[SBIconImageView addObserver:]
+ -[SBIconImageView removeObserver:]
+ -[SBIconView accessoryView]
+ -[SBLeafIcon shouldDim]
+ GCC_except_table137
+ GCC_except_table190
+ GCC_except_table262
+ GCC_except_table291
+ GCC_except_table322
+ _OBJC_IVAR_$_SBFloatingDockViewController._contentVisibility
+ _OBJC_IVAR_$_SBHClockApplicationIconImageView._hidesSecondsHand
+ _OBJC_IVAR_$_SBHClockApplicationIconImageView._overrideDate
+ _OBJC_IVAR_$_SBHClockApplicationIconImageView._overrideDateOffset
+ _OBJC_IVAR_$_SBIconDragContext._createdFileStackIcons
+ _OBJC_IVAR_$_SBIconDragContext._duplicateIconBehavior
+ _OBJC_IVAR_$_SBIconDragManager._duplicateIconBehavior
+ _OBJC_IVAR_$_SBIconImageView._observers
+ ___53-[SBFloatingDockViewController setContentVisibility:]_block_invoke
+ ___78-[SBIconDragManager hideableIconsForDraggedIcons:iconLocation:dragIdentifier:]_block_invoke
+ ___block_descriptor_40_e24_v16?0"SBIconListView"8l
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSString"8"SBIcon"16^B24ls32l8
+ ___block_literal_global.252
+ ___block_literal_global.2743
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.325
+ ___block_literal_global.377
+ ___block_literal_global.385
+ ___block_literal_global.405
+ _block_copy_helper.814
+ _block_copy_helper.825
+ _block_descriptor.816
+ _block_descriptor.827
+ _block_destroy_helper.815
+ _block_destroy_helper.826
+ _objc_msgSend$createFileStackIconsIfNecessary:forDragDropSession:
+ _objc_msgSend$createdFileStackIcons
+ _objc_msgSend$directlyContainedListLeadingToIcon:
+ _objc_msgSend$duplicateIconBehavior
+ _objc_msgSend$duplicateIconsIfNecessary:forDragDropSession:
+ _objc_msgSend$effectiveOverrideDate
+ _objc_msgSend$effectiveOverrideDateOffset
+ _objc_msgSend$effectivelyHidesSecondsHand
+ _objc_msgSend$handleDuplicateIconsBeforePerformingIconDropWithDraggedIcons:dropSession:
+ _objc_msgSend$hideableIconsForDraggedIcons:iconLocation:dragIdentifier:
+ _objc_msgSend$iconDragManager:duplicateIconBehaviorInDragSession:
+ _objc_msgSend$iconImageView:didEndAsynchronousImageLoadForIcon:
+ _objc_msgSend$iconImageView:willBeginAsynchronousImageLoadForIcon:
+ _objc_msgSend$iconShouldBeDimmed:
+ _objc_msgSend$modifyIconsInDragIfNecessaryForDragDropSession:
+ _objc_msgSend$setCreatedFileStackIcons:
+ _objc_msgSend$setDuplicateIconBehavior:
+ _objc_msgSend$shouldDim
- -[SBHClockApplicationIconImageView hidesSecondHand]
- -[SBHIconManager iconDragManager:shouldDuplicateIconsInDragSession:]
- -[SBIconDragContext duplicatesSourceIcons]
- -[SBIconDragContext setDuplicatesSourceIcons:]
- -[SBIconDragManager duplicateIconsIfNecessary:forDropSession:]
- -[SBIconDragManager duplicateIconsIfNecessary:forDropSession:].cold.1
- GCC_except_table136
- GCC_except_table189
- GCC_except_table224
- GCC_except_table261
- GCC_except_table296
- GCC_except_table314
- GCC_except_table55
- GCC_except_table89
- _OBJC_IVAR_$_SBIconDragContext._duplicatesSourceIcons
- ___57-[SBFloatyFolderView iconFadeAnimator:wantsToApplyAlpha:]_block_invoke_2
- ___79-[SBIconDragManager _removeDraggedIconsFromLayout:iconLocation:dragIdentifier:]_block_invoke
- ___block_descriptor_33_e46_v24?0"SBFloatyFolderBackgroundClipView"8^B16l
- ___block_descriptor_48_e8_32s40s_e33_v32?0"NSString"8"SBIcon"16^B24ls32l8s40l8
- ___block_literal_global.250
- ___block_literal_global.2740
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.323
- ___block_literal_global.375
- ___block_literal_global.383
- ___block_literal_global.401
- _block_copy_helper.815
- _block_descriptor.817
- _block_destroy_helper.816
- _objc_msgSend$duplicateIconsIfNecessary:forDropSession:
- _objc_msgSend$duplicatesSourceIcons
- _objc_msgSend$hidesSecondHand
- _objc_msgSend$iconDragManager:shouldDuplicateIconsInDragSession:
- _objc_msgSend$setDuplicatesSourceIcons:
- _objc_msgSend$setUsesGlass:
CStrings:
+ "T@\"NSArray\",C,N,V_createdFileStackIcons"
+ "T@\"NSDate\",C,N,V_overrideDate"
+ "T@\"NSDate\",R,N"
+ "T@\"UIView<SBIconAccessoryView>\",R,N,V_accessoryView"
+ "TB,N,V_hidesSecondsHand"
+ "Td,N,V_overrideDateOffset"
+ "Tq,N,V_duplicateIconBehavior"
+ "_createdFileStackIcons"
+ "_duplicateIconBehavior"
+ "_hidesSecondsHand"
+ "_overrideDate"
+ "_overrideDateOffset"
+ "accessoryView"
+ "createFileStackIconsIfNecessary:forDragDropSession:"
+ "createdFileStackIcons"
+ "directlyContainedListLeadingToIcon:"
+ "duplicateIconBehavior"
+ "duplicateIconsIfNecessary:forDragDropSession:"
+ "effectiveOverrideDate"
+ "effectiveOverrideDateOffset"
+ "effectivelyHidesSecondsHand"
+ "handleDuplicateIconsBeforePerformingIconDropWithDraggedIcons:dropSession:"
+ "hideableIconsForDraggedIcons:iconLocation:dragIdentifier:"
+ "iconDragManager:duplicateIconBehaviorInDragSession:"
+ "iconImageView:didEndAsynchronousImageLoadForIcon:"
+ "iconImageView:willBeginAsynchronousImageLoadForIcon:"
+ "iconShouldBeDimmed:"
+ "modifyIconsInDragIfNecessaryForDragDropSession:"
+ "q32@0:8@\"SBIconDragManager\"16@\"<UIDragDropSession>\"24"
+ "setCreatedFileStackIcons:"
+ "setDuplicateIconBehavior:"
+ "shouldDim"
+ "\xe1"
+ "\xf0\xf0\xa1"
+ "\xf2\x81"
- "B32@0:8@\"SBIconDragManager\"16@\"<UIDragDropSession>\"24"
- "TB,N,V_duplicatesSourceIcons"
- "_duplicatesSourceIcons"
- "duplicateIconsIfNecessary:forDropSession:"
- "duplicatesSourceIcons"
- "hidesSecondHand"
- "iconDragManager:shouldDuplicateIconsInDragSession:"
- "setDuplicatesSourceIcons:"
- "\xd1"
- "\xe2\x81"
- "\xf0\xf0\x91"

```
