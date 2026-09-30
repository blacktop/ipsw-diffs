## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

```diff

-97.0.0.0.0
-  __TEXT.__text: 0x63894
-  __TEXT.__objc_methlist: 0x7184
-  __TEXT.__const: 0x310
-  __TEXT.__gcc_except_tab: 0x1ba8
-  __TEXT.__cstring: 0x2a97
+97.2.0.0.0
+  __TEXT.__text: 0x62a48
+  __TEXT.__objc_methlist: 0x70a4
+  __TEXT.__const: 0x300
+  __TEXT.__gcc_except_tab: 0x1bf4
+  __TEXT.__cstring: 0x2a95
   __TEXT.__ustring: 0x182
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0x1b88
+  __TEXT.__unwind_info: 0x1b80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf60
-  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4988
+  __DATA_CONST.__objc_selrefs: 0x4948
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__got: 0x910
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0xa750
+  __AUTH_CONST.__objc_const: 0xa560
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1630
-  __DATA.__objc_ivar: 0x7d0
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x7b4
   __DATA.__data: 0xcd8
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2303
-  Symbols:   6213
+  Functions: 2285
+  Symbols:   6168
   CStrings:  560
 
Symbols:
+ -[UIPrintInteractionController updatePageCountWithRanges:]
+ -[UIPrintPanelViewController compactPreviewController]
+ -[UIPrintPanelViewController setCompactPreviewController:]
+ -[UIPrintPanelViewController setSidebarPreviewController:]
+ -[UIPrintPanelViewController sidebarPreviewController]
+ -[UIPrintPreviewViewController initWithPrintPanelViewController:usingSideBar:withContainerView:]
+ -[UIPrintPreviewViewController layoutGlassButtonInset]
+ -[UIPrintPreviewViewController layoutGlassButtonLeadingConstraint]
+ -[UIPrintPreviewViewController layoutGlassButtonVerticalConstraint]
+ -[UIPrintPreviewViewController setLayoutGlassButtonLeadingConstraint:]
+ -[UIPrintPreviewViewController setLayoutGlassButtonVerticalConstraint:]
+ -[UIPrintPreviewViewController setUsingGlassLayoutButton:]
+ -[UIPrintPreviewViewController setUsingSideBar:]
+ -[UIPrintPreviewViewController usingGlassLayoutButton]
+ -[UIPrintPreviewViewController usingSideBar]
+ -[UIPrintPreviewViewController viewDidLayoutSubviews]
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table123
+ GCC_except_table132
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table157
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table68
+ GCC_except_table74
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table94
+ _OBJC_IVAR_$_UIPrintPanelViewController._compactPreviewController
+ _OBJC_IVAR_$_UIPrintPanelViewController._sidebarPreviewController
+ _OBJC_IVAR_$_UIPrintPreviewViewController._layoutGlassButtonLeadingConstraint
+ _OBJC_IVAR_$_UIPrintPreviewViewController._layoutGlassButtonVerticalConstraint
+ _OBJC_IVAR_$_UIPrintPreviewViewController._usingGlassLayoutButton
+ _OBJC_IVAR_$_UIPrintPreviewViewController._usingSideBar
+ ___block_descriptor_64_e8_32s40s48s56w_e8_v16?0q8lw56l8s32l8s40l8s48l8
+ _objc_msgSend$_setCollapsingEnabled:
+ _objc_msgSend$compactPreviewController
+ _objc_msgSend$constant
+ _objc_msgSend$hideColumn:
+ _objc_msgSend$initWithPrintPanelViewController:usingSideBar:withContainerView:
+ _objc_msgSend$layoutGlassButtonInset
+ _objc_msgSend$setCompactPreviewController:
+ _objc_msgSend$setSidebarPreviewController:
+ _objc_msgSend$setUsingGlassLayoutButton:
+ _objc_msgSend$setUsingSideBar:
+ _objc_msgSend$showColumn:
+ _objc_msgSend$sidebarPreviewController
+ _objc_msgSend$updatePageCountWithRanges:
+ _objc_msgSend$usingGlassLayoutButton
+ _objc_msgSend$usingSideBar
- -[UIPrintInteractionController _currentPrintInfo]
- -[UIPrintInteractionController pageRanges]
- -[UIPrintInteractionController setPageRanges:]
- -[UIPrintPanelViewController compactPreviewViewController]
- -[UIPrintPanelViewController horizScrollPrintPanelConstraints]
- -[UIPrintPanelViewController previewVertSeparatorView]
- -[UIPrintPanelViewController setCompactPreviewViewController:]
- -[UIPrintPanelViewController setHorizScrollPrintPanelConstraints:]
- -[UIPrintPanelViewController setPreviewVertSeparatorView:]
- -[UIPrintPanelViewController setSidebarPreviewViewController:]
- -[UIPrintPanelViewController setVertScrollPrintPanelConstraints:]
- -[UIPrintPanelViewController sidebarPreviewViewController]
- -[UIPrintPanelViewController splitViewController:willHideColumn:]
- -[UIPrintPanelViewController splitViewController:willShowColumn:]
- -[UIPrintPanelViewController vertScrollPrintPanelConstraints]
- -[UIPrintPanelViewController viewWillAppear:]
- -[UIPrintPreviewContainerView .cxx_destruct]
- -[UIPrintPreviewContainerView layoutGlassButtonLeadingConstraint]
- -[UIPrintPreviewContainerView layoutGlassButtonVerticalConstraint]
- -[UIPrintPreviewContainerView layoutGlassButton]
- -[UIPrintPreviewContainerView layoutSubviews]
- -[UIPrintPreviewContainerView setLayoutGlassButton:]
- -[UIPrintPreviewContainerView setLayoutGlassButtonLeadingConstraint:]
- -[UIPrintPreviewContainerView setLayoutGlassButtonVerticalConstraint:]
- -[UIPrintPreviewContainerView setUsingCompactPreview:]
- -[UIPrintPreviewContainerView usingCompactPreview]
- -[UIPrintPreviewViewController initWithPrintPanelViewController:useCompactPreview:withContainerView:]
- -[UIPrintPreviewViewController layoutBarButton]
- -[UIPrintPreviewViewController positionForBar:]
- -[UIPrintPreviewViewController setLayoutBarButton:]
- -[UIPrintPreviewViewController setSolariumEnabled:]
- -[UIPrintPreviewViewController setUsingCompactPreview:]
- -[UIPrintPreviewViewController solariumEnabled]
- -[UIPrintPreviewViewController usingCompactPreview]
- GCC_except_table112
- GCC_except_table118
- GCC_except_table12
- GCC_except_table125
- GCC_except_table134
- GCC_except_table147
- GCC_except_table150
- GCC_except_table159
- GCC_except_table274
- GCC_except_table275
- GCC_except_table279
- GCC_except_table30
- GCC_except_table46
- GCC_except_table47
- GCC_except_table48
- GCC_except_table49
- GCC_except_table58
- GCC_except_table61
- GCC_except_table79
- GCC_except_table87
- GCC_except_table88
- GCC_except_table92
- GCC_except_table96
- GCC_except_table99
- _OBJC_CLASS_$_UIPrintPreviewContainerView
- _OBJC_IVAR_$_UIPrintInteractionController._pageRanges
- _OBJC_IVAR_$_UIPrintPanelViewController._compactPreviewViewController
- _OBJC_IVAR_$_UIPrintPanelViewController._horizScrollPrintPanelConstraints
- _OBJC_IVAR_$_UIPrintPanelViewController._previewVertSeparatorView
- _OBJC_IVAR_$_UIPrintPanelViewController._sidebarPreviewViewController
- _OBJC_IVAR_$_UIPrintPanelViewController._vertScrollPrintPanelConstraints
- _OBJC_IVAR_$_UIPrintPreviewContainerView._layoutGlassButton
- _OBJC_IVAR_$_UIPrintPreviewContainerView._layoutGlassButtonLeadingConstraint
- _OBJC_IVAR_$_UIPrintPreviewContainerView._layoutGlassButtonVerticalConstraint
- _OBJC_IVAR_$_UIPrintPreviewContainerView._usingCompactPreview
- _OBJC_IVAR_$_UIPrintPreviewViewController._layoutBarButton
- _OBJC_IVAR_$_UIPrintPreviewViewController._solariumEnabled
- _OBJC_IVAR_$_UIPrintPreviewViewController._usingCompactPreview
- _OBJC_METACLASS_$_UIPrintPreviewContainerView
- __OBJC_$_INSTANCE_METHODS_UIPrintPreviewContainerView
- __OBJC_$_INSTANCE_VARIABLES_UIPrintPreviewContainerView
- __OBJC_$_PROP_LIST_UIPrintPreviewContainerView
- __OBJC_CLASS_RO_$_UIPrintPreviewContainerView
- __OBJC_METACLASS_RO_$_UIPrintPreviewContainerView
- ___block_descriptor_64_e8_32s40s48s56s_e8_v16?0q8ls32l8s40l8s48l8s56l8
- _objc_msgSend$_currentPrintInfo
- _objc_msgSend$_sceneUserResizability
- _objc_msgSend$compactPreviewViewController
- _objc_msgSend$horizScrollPrintPanelConstraints
- _objc_msgSend$initWithImage:menu:
- _objc_msgSend$initWithPrintPanelViewController:useCompactPreview:withContainerView:
- _objc_msgSend$layoutBarButton
- _objc_msgSend$layoutMargins
- _objc_msgSend$navigationBar
- _objc_msgSend$previewScrollDirection
- _objc_msgSend$previewVertSeparatorView
- _objc_msgSend$printOptionsLeadingConstraint
- _objc_msgSend$printOptionsWidthConstraint
- _objc_msgSend$setCompactPreviewViewController:
- _objc_msgSend$setHorizScrollPrintPanelConstraints:
- _objc_msgSend$setLayoutBarButton:
- _objc_msgSend$setPreviewVertSeparatorView:
- _objc_msgSend$setSidebarPreviewViewController:
- _objc_msgSend$setSolariumEnabled:
- _objc_msgSend$setUsingCompactPreview:
- _objc_msgSend$setUsingSplitView:
- _objc_msgSend$setVertScrollPrintPanelConstraints:
- _objc_msgSend$sidebarPreviewViewController
- _objc_msgSend$solariumEnabled
- _objc_msgSend$topItem
- _objc_msgSend$usingCompactPreview
- _objc_msgSend$usingSplitView
- _objc_msgSend$vertScrollPrintPanelConstraints
CStrings:
+ "q\xf0\xe1"
+ "\xf0\xf0\""
- "a"
- "\x81\xf0\xe1"
```
