## ZoomWindow

> `/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow`

```diff

-850.3.2.0.0
-  __TEXT.__text: 0x480f8
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0xbd60
-  __TEXT.__objc_methlist: 0x4ed8
-  __TEXT.__const: 0x458
-  __TEXT.__objc_methname: 0x11885
+872.0.0.0.0
+  __TEXT.__text: 0x498d4
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_stubs: 0xc080
+  __TEXT.__objc_methlist: 0x4f90
+  __TEXT.__const: 0x468
+  __TEXT.__objc_methname: 0x11b7a
   __TEXT.__objc_classname: 0x7e7
-  __TEXT.__objc_methtype: 0x383f
-  __TEXT.__cstring: 0x2017
+  __TEXT.__objc_methtype: 0x38af
+  __TEXT.__cstring: 0x2021
   __TEXT.__gcc_except_tab: 0x950
   __TEXT.__oslogstring: 0x352
-  __TEXT.__unwind_info: 0x1018
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x4e8
+  __TEXT.__unwind_info: 0x1040
+  __DATA_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__got: 0x510
   __DATA_CONST.__const: 0xaf0
-  __DATA_CONST.__cfstring: 0x1900
+  __DATA_CONST.__cfstring: 0x1920
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8

   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x7698
-  __DATA.__objc_selrefs: 0x38b0
-  __DATA.__objc_ivar: 0x728
+  __DATA.__objc_const: 0x7798
+  __DATA.__objc_selrefs: 0x3988
+  __DATA.__objc_ivar: 0x73c
   __DATA.__objc_data: 0xcd0
   __DATA.__data: 0xbd8
   __DATA.__bss: 0x100

   - /System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager
   - /System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
+  - /System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared
   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF3DA405-B2DB-3FF0-8A08-ADCF76DB118D
-  Functions: 1667
-  Symbols:   4655
-  CStrings:  3471
+  UUID: E7D2D443-3808-3290-AA7C-67B4808F3B29
+  Functions: 1684
+  Symbols:   4712
+  CStrings:  3512
 
Symbols:
+ -[ZWLensChromeView didMoveToWindow]
+ -[ZWLensChromeView updateCornerRadii]
+ -[ZWLensZoomView didMoveToWindow]
+ -[ZWLensZoomView updateCornerRadii]
+ -[ZWMenuChooserTableViewController contentInset]
+ -[ZWMenuChooserTableViewController setContentInset:]
+ -[ZWMenuItemSimpleButtonTableViewCell .cxx_destruct]
+ -[ZWMenuItemSimpleButtonTableViewCell cellLabel]
+ -[ZWMenuItemSimpleButtonTableViewCell checkmarkImageView]
+ -[ZWMenuItemSimpleButtonTableViewCell isChecked]
+ -[ZWMenuItemSimpleButtonTableViewCell setCellLabel:]
+ -[ZWMenuItemSimpleButtonTableViewCell setCheckmarkImageView:]
+ -[ZWMenuItemSimpleButtonTableViewCell setIsChecked:]
+ -[ZWMenuViewController contentInset]
+ -[ZWMenuViewController setContentInset:]
+ OBJC_IVAR_$_ZWMenuChooserTableViewController._contentInset
+ OBJC_IVAR_$_ZWMenuItemSimpleButtonTableViewCell._cellLabel
+ OBJC_IVAR_$_ZWMenuItemSimpleButtonTableViewCell._checkmarkImageView
+ OBJC_IVAR_$_ZWMenuItemSimpleButtonTableViewCell._isChecked
+ OBJC_IVAR_$_ZWMenuViewController._contentInset
+ _AXCornerRadiiForFrameInContainer
+ _AXCornerRadiusForBackgroundWithSize
+ _CACornerRadiiZero
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UILabel
+ _UIFontTextStyleBody
+ _ZWCornerRadiiForFrameInContainer
+ _ZWCornerRadiusForBackgroundWithSize
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke.283
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_2.284
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_3.285
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_4.286
+ __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.298
+ __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.299
+ __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke_2.300
+ __75-[ZWUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.334
+ __OBJC_$_INSTANCE_VARIABLES_ZWMenuItemSimpleButtonTableViewCell
+ __OBJC_$_PROP_LIST_ZWMenuItemSimpleButtonTableViewCell
+ __UISolariumEnabled
+ __block_literal_global.279
+ __block_literal_global.295
+ __block_literal_global.301
+ __block_literal_global.302
+ __block_literal_global.353
+ __block_literal_global.367
+ __block_literal_global.544
+ _objc_msgSend$ax_setWantsGlassAppearance:
+ _objc_msgSend$cellLabel
+ _objc_msgSend$checkmarkImageView
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$constraintEqualToAnchor:constant:
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$constraintGreaterThanOrEqualToConstant:
+ _objc_msgSend$contentInset
+ _objc_msgSend$heightAnchor
+ _objc_msgSend$preferredFontForTextStyle:
+ _objc_msgSend$secondarySystemFillColor
+ _objc_msgSend$setAdjustsFontForContentSizeCategory:
+ _objc_msgSend$setCellLabel:
+ _objc_msgSend$setCheckmarkImageView:
+ _objc_msgSend$setContentInset:
+ _objc_msgSend$setCornerRadii:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setIsChecked:
+ _objc_msgSend$setScrollIndicatorInsets:
+ _objc_msgSend$setSeparatorStyle:
+ _objc_msgSend$setUserInterfaceStyle:
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _objc_msgSend$traitOverrides
+ _objc_msgSend$updateCornerRadii
+ _objc_msgSend$widthAnchor
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke.280
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_2.281
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_3.282
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_4.283
- __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.295
- __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.296
- __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke_2.297
- __75-[ZWUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.331
- __block_literal_global.276
- __block_literal_global.292
- __block_literal_global.296
- __block_literal_global.298
- __block_literal_global.350
- __block_literal_global.364
- __block_literal_global.541
CStrings:
+ "@\"UILabel\""
+ "T@\"UIImageView\",&,N,V_checkmarkImageView"
+ "T@\"UILabel\",&,N,V_cellLabel"
+ "TB,N,V_isChecked"
+ "T{UIEdgeInsets=dddd},N,V_contentInset"
+ "_cellLabel"
+ "_checkmarkImageView"
+ "_contentInset"
+ "_isChecked"
+ "ax_setWantsGlassAppearance:"
+ "cellLabel"
+ "checkmark"
+ "checkmarkImageView"
+ "configurationWithPointSize:weight:"
+ "constraintEqualToAnchor:constant:"
+ "constraintEqualToConstant:"
+ "constraintGreaterThanOrEqualToConstant:"
+ "contentInset"
+ "didMoveToWindow"
+ "heightAnchor"
+ "isChecked"
+ "preferredFontForTextStyle:"
+ "secondarySystemFillColor"
+ "setAdjustsFontForContentSizeCategory:"
+ "setCellLabel:"
+ "setCheckmarkImageView:"
+ "setContentInset:"
+ "setCornerRadii:"
+ "setFont:"
+ "setIsChecked:"
+ "setScrollIndicatorInsets:"
+ "setSeparatorStyle:"
+ "setUserInterfaceStyle:"
+ "systemImageNamed:withConfiguration:"
+ "traitOverrides"
+ "updateCornerRadii"
+ "v48@0:8{UIEdgeInsets=dddd}16"
+ "widthAnchor"
+ "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
+ "{UIEdgeInsets=dddd}16@0:8"

```
