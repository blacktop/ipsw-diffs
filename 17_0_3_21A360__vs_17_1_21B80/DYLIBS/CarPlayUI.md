## CarPlayUI

> `/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI`

```diff

-271.5.2.0.0
-  __TEXT.__text: 0x2088c
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x29f8
-  __TEXT.__const: 0x534
+271.7.4.1.0
+  __TEXT.__text: 0x22434
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x2c88
+  __TEXT.__const: 0x544
   __TEXT.__cstring: 0x8d8
   __TEXT.__ustring: 0x12
   __TEXT.__oslogstring: 0x2cf

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x7a4
-  __TEXT.__objc_classname: 0x614
-  __TEXT.__objc_methname: 0x8ea1
-  __TEXT.__objc_methtype: 0x1087
-  __TEXT.__objc_stubs: 0x6900
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__unwind_info: 0x800
+  __TEXT.__objc_classname: 0x686
+  __TEXT.__objc_methname: 0x9499
+  __TEXT.__objc_methtype: 0x1106
+  __TEXT.__objc_stubs: 0x6cc0
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x488
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5bd0
-  __DATA_CONST.__objc_selrefs: 0x2110
+  __DATA_CONST.__objc_const: 0x5fe0
+  __DATA_CONST.__objc_selrefs: 0x2210
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__objc_const: 0x12d0
+  __AUTH_CONST.__objc_const: 0x13f0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__const: 0x378
   __AUTH_CONST.__cfstring: 0xbc0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH.__objc_data: 0x10f8
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH.__objc_data: 0x1238
   __AUTH.__data: 0xe8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x340
-  __DATA.__objc_superrefs: 0x110
-  __DATA.__objc_ivar: 0x400
+  __DATA.__objc_classrefs: 0x358
+  __DATA.__objc_superrefs: 0x128
+  __DATA.__objc_ivar: 0x434
   __DATA.__data: 0x578
   __DATA.__bss: 0x440
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A4C4A482-3EBE-3E43-A16A-25EB2DA1B84D
-  Functions: 973
-  Symbols:   3976
-  CStrings:  2014
+  UUID: 6B354514-764B-3E7A-85FE-A6D1CD944FEC
+  Functions: 1024
+  Symbols:   4151
+  CStrings:  2076
 
Symbols:
+ +[CPUIImageRowCellConfiguration configurationWithText:artworkCatalogs:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:]
+ +[CPUIImageRowCellConfiguration configurationWithText:images:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:]
+ -[CPUIAssistantCell sizeThatFits:]
+ -[CPUIImageRowCell _artworkContentWidth]
+ -[CPUIImageRowCell _maxArtworkCountFittingSize]
+ -[CPUIImageRowCell _removeArtworkTitleItem:]
+ -[CPUIImageRowCell _showsImageTitles]
+ -[CPUIImageRowCell imageTitles]
+ -[CPUIImageRowCell setImageTitles:]
+ -[CPUIImageRowCell setStackViewHeightConstraint:]
+ -[CPUIImageRowCell sizeThatFits:]
+ -[CPUIImageRowCell stackViewHeightConstraint]
+ -[CPUIImageRowCellConfiguration imageTitles]
+ -[CPUIImageRowCellConfiguration setImageTitles:]
+ -[CPUIMessageCell sizeThatFits:]
+ -[CPUIModernButton setShowButtonBackgroundShape:]
+ -[CPUIModernButton showButtonBackgroundShape]
+ -[CPUINowPlayingViewController _attributionButtonTapped:]
+ -[CPUINowPlayingViewController _sceneDidEnterBackground:]
+ -[CPUISongAttributionView .cxx_destruct]
+ -[CPUISongAttributionView artworkImageView]
+ -[CPUISongAttributionView artwork]
+ -[CPUISongAttributionView button]
+ -[CPUISongAttributionView initWithFrame:]
+ -[CPUISongAttributionView layoutSubviews]
+ -[CPUISongAttributionView name]
+ -[CPUISongAttributionView setArtwork:]
+ -[CPUISongAttributionView setArtworkImageView:]
+ -[CPUISongAttributionView setName:]
+ -[CPUISongDetailsView attributionArtwork]
+ -[CPUISongDetailsView attributionButton]
+ -[CPUISongDetailsView attributionName]
+ -[CPUISongDetailsView attributionView]
+ -[CPUISongDetailsView setAttributionArtwork:]
+ -[CPUISongDetailsView setAttributionName:]
+ -[CPUISongDetailsView setAttributionView:]
+ -[CPUITableCell sizeThatFits:]
+ -[_CPUIImageRowCellImageTitleItem .cxx_destruct]
+ -[_CPUIImageRowCellImageTitleItem button]
+ -[_CPUIImageRowCellImageTitleItem configureWithArtwork:title:imageSize:fallbackImage:]
+ -[_CPUIImageRowCellImageTitleItem initWithFrame:]
+ -[_CPUIImageRowCellImageTitleItem intrinsicContentSize]
+ -[_CPUIImageRowCellImageTitleItem label]
+ -[_CPUIImageRowCellImageTitleItem preferredSize]
+ -[_CPUIImageRowCellImageTitleItem setButton:]
+ -[_CPUIImageRowCellImageTitleItem setLabel:]
+ -[_CPUIImageRowCellImageTitleItem setPreferredSize:]
+ -[_CPUIImageRowHighlightButton focusLayerCornerRadius]
+ -[_CPUIOutsetHighlightButton .cxx_destruct]
+ -[_CPUIOutsetHighlightButton didMoveToWindow]
+ -[_CPUIOutsetHighlightButton didUpdateFocusInContext:withAnimationCoordinator:]
+ -[_CPUIOutsetHighlightButton focusRingView]
+ -[_CPUIOutsetHighlightButton setFocusRingView:]
+ _CPUIImageRowMinImageDimension
+ _OBJC_CLASS_$_CPUISongAttributionView
+ _OBJC_CLASS_$__CPUIImageRowCellImageTitleItem
+ _OBJC_CLASS_$__CPUIImageRowHighlightButton
+ _OBJC_CLASS_$__CPUIOutsetHighlightButton
+ _OBJC_IVAR_$_CPUIImageRowCell._imageTitles
+ _OBJC_IVAR_$_CPUIImageRowCell._stackViewHeightConstraint
+ _OBJC_IVAR_$_CPUIImageRowCellConfiguration._imageTitles
+ _OBJC_IVAR_$_CPUIModernButton._showButtonBackgroundShape
+ _OBJC_IVAR_$_CPUISongAttributionView._artwork
+ _OBJC_IVAR_$_CPUISongAttributionView._artworkImageView
+ _OBJC_IVAR_$_CPUISongAttributionView._button
+ _OBJC_IVAR_$_CPUISongAttributionView._name
+ _OBJC_IVAR_$_CPUISongDetailsView._attributionView
+ _OBJC_IVAR_$__CPUIImageRowCellImageTitleItem._button
+ _OBJC_IVAR_$__CPUIImageRowCellImageTitleItem._label
+ _OBJC_IVAR_$__CPUIImageRowCellImageTitleItem._preferredSize
+ _OBJC_IVAR_$__CPUIOutsetHighlightButton._focusRingView
+ _OBJC_METACLASS_$_CPUISongAttributionView
+ _OBJC_METACLASS_$__CPUIImageRowCellImageTitleItem
+ _OBJC_METACLASS_$__CPUIImageRowHighlightButton
+ _OBJC_METACLASS_$__CPUIOutsetHighlightButton
+ _UIFontWeightMedium
+ _UISceneDidEnterBackgroundNotification
+ __OBJC_$_INSTANCE_METHODS_CPUISongAttributionView
+ __OBJC_$_INSTANCE_METHODS__CPUIImageRowCellImageTitleItem
+ __OBJC_$_INSTANCE_METHODS__CPUIImageRowHighlightButton
+ __OBJC_$_INSTANCE_METHODS__CPUIOutsetHighlightButton
+ __OBJC_$_INSTANCE_VARIABLES_CPUISongAttributionView
+ __OBJC_$_INSTANCE_VARIABLES__CPUIImageRowCellImageTitleItem
+ __OBJC_$_INSTANCE_VARIABLES__CPUIOutsetHighlightButton
+ __OBJC_$_PROP_LIST_CPUISongAttributionView
+ __OBJC_$_PROP_LIST__CPUIImageRowCellImageTitleItem
+ __OBJC_$_PROP_LIST__CPUIOutsetHighlightButton
+ __OBJC_CLASS_RO_$_CPUISongAttributionView
+ __OBJC_CLASS_RO_$__CPUIImageRowCellImageTitleItem
+ __OBJC_CLASS_RO_$__CPUIImageRowHighlightButton
+ __OBJC_CLASS_RO_$__CPUIOutsetHighlightButton
+ __OBJC_METACLASS_RO_$_CPUISongAttributionView
+ __OBJC_METACLASS_RO_$__CPUIImageRowCellImageTitleItem
+ __OBJC_METACLASS_RO_$__CPUIImageRowHighlightButton
+ __OBJC_METACLASS_RO_$__CPUIOutsetHighlightButton
+ ___67-[CPUINowPlayingViewController _updateArtworkIfNeeded:placeholder:]_block_invoke.148
+ ___86-[_CPUIImageRowCellImageTitleItem configureWithArtwork:title:imageSize:fallbackImage:]_block_invoke
+ ___block_descriptor_48_e8_32s_e33_v32?0"MPArtworkCatalog"8Q16^B24ls32l8
+ __unnamed_array_storage.133
+ __unnamed_array_storage.53
+ __unnamed_array_storage.59
+ __unnamed_array_storage.64
+ _objc_msgSend$_artworkContentWidth
+ _objc_msgSend$_maxArtworkCountFittingSize
+ _objc_msgSend$_removeArtworkTitleItem:
+ _objc_msgSend$_showsImageTitles
+ _objc_msgSend$attributionArtworkForNowPlayingViewController:
+ _objc_msgSend$attributionButton
+ _objc_msgSend$attributionName
+ _objc_msgSend$attributionTitleForNowPlayingViewController:
+ _objc_msgSend$attributionView
+ _objc_msgSend$configurationWithText:artworkCatalogs:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:
+ _objc_msgSend$configurationWithText:images:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:
+ _objc_msgSend$configureWithArtwork:title:imageSize:fallbackImage:
+ _objc_msgSend$customSpacingAfterView:
+ _objc_msgSend$imageTitles
+ _objc_msgSend$label
+ _objc_msgSend$leftBarButtonItem
+ _objc_msgSend$minimumHeight
+ _objc_msgSend$nowPlayingViewControllerAttributionButtonTapped:
+ _objc_msgSend$nowPlayingViewControllerShouldHideBackButton:
+ _objc_msgSend$preferredSize
+ _objc_msgSend$relinquishWithAnimationSettings:
+ _objc_msgSend$rowHeight
+ _objc_msgSend$setAttributionArtwork:
+ _objc_msgSend$setAttributionName:
+ _objc_msgSend$setButton:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$setImageTitles:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setPreferredSize:
+ _objc_msgSend$setRingWidth:
+ _objc_msgSend$setShowButtonBackgroundShape:
+ _objc_msgSend$setStackViewHeightConstraint:
+ _objc_msgSend$showButtonBackgroundShape
+ _objc_msgSend$stackViewHeightConstraint
+ _objc_retain_x26
- -[CPUIImageRowCell _removeArtworkButton:]
- -[CPUIImageRowCell artworkViewCountThatFits:]
- ___48-[CPUIImageRowCell _layoutArtworkImagesIfNeeded]_block_invoke_2
- ___67-[CPUINowPlayingViewController _updateArtworkIfNeeded:placeholder:]_block_invoke.145
- ___block_descriptor_40_e8_32s_e33_v32?0"MPArtworkCatalog"8Q16^B24ls32l8
- __unnamed_array_storage.127
- __unnamed_array_storage.51
- __unnamed_array_storage.57
- __unnamed_array_storage.62
- _objc_msgSend$_removeArtworkButton:
- _objc_msgSend$artworkViewCountThatFits:
- _objc_msgSend$reliquishWithAnimationSettings:
- _objc_msgSend$setImageEdgeInsets:
CStrings:
+ "\x16"
+ "\x19"
+ "."
+ "@\"CPUISongAttributionView\""
+ "@\"_CPUIImageRowHighlightButton\""
+ "@\"_CPUIOutsetHighlightButton\""
+ "@64@0:8@16@24@32@?40@?48B56B60"
+ "CPUISongAttributionView"
+ "T@\"CPUIFocusRingView\",&,N,V_focusRingView"
+ "T@\"CPUIModernButton\",R,N"
+ "T@\"CPUIModernButton\",R,N,V_button"
+ "T@\"CPUISongAttributionView\",&,N,V_attributionView"
+ "T@\"NSArray\",C,N,V_imageTitles"
+ "T@\"NSLayoutConstraint\",&,N,V_stackViewHeightConstraint"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"UIImage\",&,N"
+ "T@\"UILabel\",&,N,V_label"
+ "T@\"_CPUIImageRowHighlightButton\",&,N,V_focusIndicator"
+ "T@\"_CPUIOutsetHighlightButton\",&,N,V_button"
+ "TB,N,V_showButtonBackgroundShape"
+ "T{CGSize=dd},N,V_preferredSize"
+ "_CPUIImageRowCellImageTitleItem"
+ "_CPUIImageRowHighlightButton"
+ "_CPUIOutsetHighlightButton"
+ "_artworkContentWidth"
+ "_attributionButtonTapped:"
+ "_attributionView"
+ "_focusRingView"
+ "_imageTitles"
+ "_label"
+ "_maxArtworkCountFittingSize"
+ "_name"
+ "_preferredSize"
+ "_removeArtworkTitleItem:"
+ "_sceneDidEnterBackground:"
+ "_showButtonBackgroundShape"
+ "_showsImageTitles"
+ "_stackViewHeightConstraint"
+ "attributionArtwork"
+ "attributionArtworkForNowPlayingViewController:"
+ "attributionButton"
+ "attributionName"
+ "attributionTitleForNowPlayingViewController:"
+ "attributionView"
+ "configurationWithText:artworkCatalogs:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:"
+ "configurationWithText:images:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:"
+ "configureWithArtwork:title:imageSize:fallbackImage:"
+ "customSpacingAfterView:"
+ "focusRingView"
+ "imageTitles"
+ "label"
+ "leftBarButtonItem"
+ "nowPlayingViewControllerAttributionButtonTapped:"
+ "nowPlayingViewControllerShouldHideBackButton:"
+ "preferredSize"
+ "relinquishWithAnimationSettings:"
+ "setAttributionArtwork:"
+ "setAttributionName:"
+ "setAttributionView:"
+ "setCustomSpacing:afterView:"
+ "setFocusRingView:"
+ "setImageTitles:"
+ "setLabel:"
+ "setPreferredSize:"
+ "setShowButtonBackgroundShape:"
+ "setStackViewHeightConstraint:"
+ "showButtonBackgroundShape"
+ "stackViewHeightConstraint"
+ "v48@0:8@16@24d32@40"
+ "{CGSize=dd}32@0:8{CGSize=dd}16"
- "\x18"
- ","
- "@\"CPUIHighlightButton\""
- "T@\"CPUIHighlightButton\",&,N,V_focusIndicator"
- "_removeArtworkButton:"
- "artworkViewCountThatFits:"
- "q32@0:8{CGSize=dd}16"
- "reliquishWithAnimationSettings:"
- "setImageEdgeInsets:"

```
