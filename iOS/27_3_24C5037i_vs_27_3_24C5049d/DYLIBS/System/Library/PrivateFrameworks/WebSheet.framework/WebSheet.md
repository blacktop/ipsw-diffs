## WebSheet

> `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet`

```diff

-339.0.0.0.0
-  __TEXT.__text: 0x8280
-  __TEXT.__objc_methlist: 0xce0
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x165b
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x350
+340.0.0.0.0
+  __TEXT.__text: 0xabac
+  __TEXT.__objc_methlist: 0xdd8
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x16a2
+  __TEXT.__gcc_except_tab: 0x64
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__const: 0x398
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe78
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xb60
-  __AUTH_CONST.__objc_const: 0x15a0
+  __AUTH_CONST.__cfstring: 0xb80
+  __AUTH_CONST.__objc_const: 0x1920
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xec
+  __DATA.__objc_ivar: 0x158
   __DATA.__data: 0x3c0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/WebUI.framework/WebUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   557
-  CStrings:  157
+  Functions: 229
+  Symbols:   628
+  CStrings:  159
 
Symbols:
+ -[WSWebSheetView _alignSystemDomainLineWithTitle]
+ -[WSWebSheetView _applySystemHeaderRowLayoutCollapsed:showsTitleRow:]
+ -[WSWebSheetView _configureSystemHeaderIfNeeded]
+ -[WSWebSheetView _systemCollapsedRowHeight]
+ -[WSWebSheetView _systemNavigationBarAddress]
+ -[WSWebSheetView _systemThreeLineTitleViewHeight]
+ -[WSWebSheetView _systemTitleRowHeight]
+ -[WSWebSheetView _systemTitleViewIsWithinBar]
+ -[WSWebSheetView _updateSystemBarMinimizedStateWithDomainAboveBar:verticalBarInUse:reservedRoomChanged:]
+ -[WSWebSheetView _updateSystemDomainLine:]
+ -[WSWebSheetView _updateSystemHeaderBackdropWidth]
+ -[WSWebSheetView _updateSystemHeaderTextsShowingAddress:]
+ -[WSWebSheetView _updateSystemNavigationBarTitle]
+ -[WSWebSheetView _usesSystemNavigationBar]
+ -[WSWebSheetView setSizeTransitionInProgress:]
+ -[WSWebSheetViewController noteHingeStatus:]
+ -[WSWebSheetViewController preferredVerticalBarBehavior]
+ -[WSWebSheetViewController setUsesSystemNavigationBar:]
+ -[WSWebSheetViewController usesSystemNavigationBar]
+ -[WSWebSheetViewController viewDidLoad]
+ GCC_except_table147
+ GCC_except_table4
+ _CGRectGetHeight
+ _CGRectGetMidY
+ _CGRectGetMinY
+ _CGRectIsEmpty
+ _NSForegroundColorAttributeName
+ _NSStringFromCGSize
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_UIHingeInteraction
+ _OBJC_CLASS_$_UINavigationBarAppearance
+ _OBJC_CLASS_$_UIStackView
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_CLASS_$_UITraitVerticalSizeClass
+ _OBJC_IVAR_$_WSWebSheetView._sizeTransitionsInProgress
+ _OBJC_IVAR_$_WSWebSheetView._systemAddressLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemAddressView
+ _OBJC_IVAR_$_WSWebSheetView._systemBarMinimized
+ _OBJC_IVAR_$_WSWebSheetView._systemCollapsedAddressLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemCollapsedLabelCenterY
+ _OBJC_IVAR_$_WSWebSheetView._systemCompactTitleLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemDomainLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemDomainLine
+ _OBJC_IVAR_$_WSWebSheetView._systemDomainLineBottom
+ _OBJC_IVAR_$_WSWebSheetView._systemDomainSecurityLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemExpandedBarEdges
+ _OBJC_IVAR_$_WSWebSheetView._systemHeaderBoundsSize
+ _OBJC_IVAR_$_WSWebSheetView._systemInBarTitleLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemMinimizedBarEdge
+ _OBJC_IVAR_$_WSWebSheetView._systemNetworkSSIDLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemNetworkTitleLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemNetworkTitleView
+ _OBJC_IVAR_$_WSWebSheetView._systemSSIDLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemSecurityLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemTitleLabel
+ _OBJC_IVAR_$_WSWebSheetView._systemTitleRechecks
+ _OBJC_IVAR_$_WSWebSheetView._systemTitleRow
+ _OBJC_IVAR_$_WSWebSheetView._systemTitleRowLeading
+ _OBJC_IVAR_$_WSWebSheetView._systemTitleRowTrailing
+ _OBJC_IVAR_$_WSWebSheetViewController._hingeStatus
+ _OBJC_IVAR_$_WSWebSheetViewController._usesSystemNavigationBar
+ _UIFontWeightSemibold
+ __OBJC_$_INSTANCE_VARIABLES_WSWebSheetViewController
+ __OBJC_$_PROP_LIST_WSWebSheetViewController
+ ___104-[WSWebSheetView _updateSystemBarMinimizedStateWithDomainAboveBar:verticalBarInUse:reservedRoomChanged:]_block_invoke
+ ___39-[WSWebSheetViewController viewDidLoad]_block_invoke
+ ___79-[WSWebSheetViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e57_v24?0"UIHingeInteraction"8"UIHingeInteractionUpdate"16lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ _objc_copyWeak
+ _objc_initWeak
- GCC_except_table131
CStrings:
+ "%@ %d %d"
+ "v24@?0@\"UIHingeInteraction\"8@\"UIHingeInteractionUpdate\"16"
+ "\xf0\xf0\xf0\xf0a"
- "\xf0\xf0\xa1"
```
