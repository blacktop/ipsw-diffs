## UXKit

> `/System/Library/PrivateFrameworks/UXKit.framework/Versions/A/UXKit`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x72ca0
-  __TEXT.__objc_methlist: 0x9c74
-  __TEXT.__const: 0x2a0
+916.41.100.0.0
+  __TEXT.__text: 0x7387c
+  __TEXT.__objc_methlist: 0x9d54
+  __TEXT.__const: 0x2b0
   __TEXT.__gcc_except_tab: 0x56c
-  __TEXT.__cstring: 0x4bc2
+  __TEXT.__cstring: 0x4bb5
   __TEXT.__oslogstring: 0x4d0
-  __TEXT.__unwind_info: 0x2840
+  __TEXT.__unwind_info: 0x2878
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60e8
+  __DATA_CONST.__objc_selrefs: 0x6168
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x7c8
-  __AUTH_CONST.__const: 0x23a0
+  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__got: 0x7e8
+  __AUTH_CONST.__const: 0x2340
   __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0xe248
+  __AUTH_CONST.__objc_const: 0xe318
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1090
-  __DATA.__objc_ivar: 0xcac
+  __DATA.__objc_ivar: 0xcc0
   __DATA.__data: 0xfb0
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x78

   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3372
-  Symbols:   8037
-  CStrings:  542
+  Functions: 3388
+  Symbols:   8072
+  CStrings:  540
 
Symbols:
+ -[UXCollectionView _isTouchDoubleTapAtLocation:indexPath:]
+ -[UXCollectionView _mouseDoubleClickRecognized:]
+ -[UXCollectionView _resetTouchDoubleTapState]
+ -[UXCollectionView _updateTouchDoubleTapStateForClickAtLocation:]
+ -[UXNavigationBar globalLeadingBarButtonItem]
+ -[UXNavigationBar setGlobalLeadingBarButtonItem:]
+ -[UXNavigationItem hidesGlobalLeadingBarButtonItem]
+ -[UXNavigationItem setHidesGlobalLeadingBarButtonItem:]
+ -[UXSourceController _restoreWantsSourceListHidden:]
+ -[UXSourceController _setWantsSourceListHidden:animated:completion:]
+ -[UXSourceController _splitViewDidResizeSubviews:]
+ -[UXSourceController _splitViewWillResizeSubviews:]
+ -[UXSourceController _updateDetailMinimumWidth]
+ -[UXSourceController didChangeWantsSourceListHidden]
+ -[UXSourceController minimumWidthForInlineSourceList]
+ -[UXSourceController setMinimumWidthForInlineSourceList:]
+ -[UXWindowToolbarController _layoutOnceWithATrailingItemRemovedFromToolbar:]
+ -[UXWindowToolbarController globalLeadingBarButtonItem]
+ -[UXWindowToolbarController setGlobalLeadingBarButtonItem:]
+ -[_UXNavigationItemContainerView _leftBarButtonItems]
+ -[_UXNavigationItemContainerView _rightBarButtonItems]
+ GCC_except_table1255
+ GCC_except_table1541
+ GCC_except_table1543
+ GCC_except_table1551
+ GCC_except_table1557
+ GCC_except_table1560
+ GCC_except_table1577
+ GCC_except_table1761
+ GCC_except_table1812
+ GCC_except_table2051
+ GCC_except_table2445
+ GCC_except_table2471
+ GCC_except_table2494
+ GCC_except_table2496
+ GCC_except_table2627
+ GCC_except_table2645
+ GCC_except_table2649
+ GCC_except_table2755
+ GCC_except_table3006
+ GCC_except_table3027
+ GCC_except_table3029
+ GCC_except_table3031
+ GCC_except_table3032
+ GCC_except_table3033
+ GCC_except_table3034
+ OBJC_IVAR_$_UXCollectionView._lastTouchClickIndexPath
+ OBJC_IVAR_$_UXCollectionView._lastTouchClickLocationInWindow
+ OBJC_IVAR_$_UXCollectionView._lastTouchClickTime
+ OBJC_IVAR_$_UXCollectionView._mouseDoubleClickRecognizer
+ OBJC_IVAR_$_UXNavigationBar._globalLeadingBarButtonItem
+ OBJC_IVAR_$_UXNavigationItem._hidesGlobalLeadingBarButtonItem
+ OBJC_IVAR_$_UXSourceController._isUserResizingSourceListDivider
+ OBJC_IVAR_$_UXSourceController._minimumWidthForInlineSourceList
+ OBJC_IVAR_$_UXWindowToolbarController._globalLeadingBarButtonItem
+ OBJC_IVAR_$__UXCollectionViewGestureDelegate._mouseDoubleClickRecognizer
+ _NSSplitViewDidResizeSubviewsNotification
+ _NSSplitViewDividerIndexKey
+ _NSSplitViewUserResizeKey
+ _NSSplitViewWillResizeSubviewsNotification
+ _objc_msgSend$_isTouchDoubleTapAtLocation:indexPath:
+ _objc_msgSend$_layoutOnceWithATrailingItemRemovedFromToolbar:
+ _objc_msgSend$_leftBarButtonItems
+ _objc_msgSend$_resetTouchDoubleTapState
+ _objc_msgSend$_rightBarButtonItems
+ _objc_msgSend$_updateDetailMinimumWidth
+ _objc_msgSend$_updateTouchDoubleTapStateForClickAtLocation:
+ _objc_msgSend$didChangeWantsSourceListHidden
+ _objc_msgSend$globalLeadingBarButtonItem
+ _objc_msgSend$hidesGlobalLeadingBarButtonItem
+ _objc_msgSend$itemIdentifiers
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$setGlobalLeadingBarButtonItem:
+ _objc_msgSend$wantsInspectorCollapsed
- -[UXCollectionView _doubleClickRecognized:]
- -[UXNavigationItem setSwitchLibraryButtonItem:]
- -[UXNavigationItem switchLibraryButtonItem]
- GCC_except_table1251
- GCC_except_table1534
- GCC_except_table1536
- GCC_except_table1544
- GCC_except_table1550
- GCC_except_table1553
- GCC_except_table1570
- GCC_except_table1754
- GCC_except_table1805
- GCC_except_table2044
- GCC_except_table2437
- GCC_except_table2463
- GCC_except_table2486
- GCC_except_table2488
- GCC_except_table2612
- GCC_except_table2619
- GCC_except_table2630
- GCC_except_table2740
- GCC_except_table2991
- GCC_except_table3012
- GCC_except_table3014
- GCC_except_table3016
- GCC_except_table3017
- GCC_except_table3018
- GCC_except_table3019
- OBJC_IVAR_$_UXCollectionView._doubleClickRecognizer
- OBJC_IVAR_$_UXNavigationItem._switchLibraryButtonItem
- OBJC_IVAR_$_UXSourceController._isTogglingSidebar
- OBJC_IVAR_$__UXCollectionViewGestureDelegate._doubleClickRecognizer
- OBJC_IVAR_$__UXCollectionViewGestureDelegate._touchClickRecognizer
- ___42-[UXWindowToolbarController updateToolbar]_block_invoke
- ___42-[UXWindowToolbarController updateToolbar]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e5_B8?0l
- ___block_descriptor_49_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
- _objc_msgSend$doubleClickInterval
- _objc_msgSend$switchLibraryButtonItem
CStrings:
+ "UXCollectionView.mouseDoubleClickRecognizer"
+ "hidesGlobalLeadingBarButtonItem"
+ "\xf0\xf0\xf0\xf0\xf0\xf0C"
- "UXCollectionView.doubleClickRecognizer"
- "switchLibraryButtonItem"
- "v32@?0@\"NSString\"8Q16^B24"
- "\xf0\xf0\xf0\xf0\xf0\xf3"
- "\xf1"
```
