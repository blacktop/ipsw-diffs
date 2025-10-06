## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x27ab0
+198.1.2.0.0
+  __TEXT.__text: 0x272f8
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x3404
-  __TEXT.__const: 0xe0
+  __TEXT.__objc_methlist: 0x3424
+  __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0xc04
-  __TEXT.__cstring: 0x184f
+  __TEXT.__cstring: 0x1809
   __TEXT.__oslogstring: 0x329
-  __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0xa20
-  __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methname: 0x9749
-  __TEXT.__objc_methtype: 0x1d79
-  __TEXT.__objc_stubs: 0x72c0
+  __TEXT.__ustring: 0x60
+  __TEXT.__unwind_info: 0xa30
+  __TEXT.__objc_classname: 0x5ab
+  __TEXT.__objc_methname: 0x97ad
+  __TEXT.__objc_methtype: 0x1d99
+  __TEXT.__objc_stubs: 0x7300
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0xe38
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2530
+  __DATA_CONST.__objc_selrefs: 0x2528
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2bc0
-  __AUTH_CONST.__objc_const: 0x4f78
+  __AUTH_CONST.__cfstring: 0x2b20
+  __AUTH_CONST.__objc_const: 0x4f18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x408
+  __DATA.__objc_ivar: 0x3fc
   __DATA.__data: 0x858
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/TipsUI.framework/TipsUI
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF436D4A-5C57-36DA-AAE3-603A565D35B3
-  Functions: 1083
-  Symbols:   4195
-  CStrings:  2681
+  UUID: 3A88079C-423D-3240-B2FC-C91F1008B76D
+  Functions: 1086
+  Symbols:   4200
+  CStrings:  2670
 
Symbols:
+ +[HLPHelpViewController URLWithTopicID:anchorID:]
+ -[HLPHelpLoadingView contentMessageViewController]
+ -[HLPHelpLoadingView removeContentMessage]
+ -[HLPHelpLoadingView setContentMessageViewController:]
+ -[HLPHelpLoadingView showMessageWithError:]
+ -[HLPHelpSearchResultTableViewController noResultFooterViewWithText:]
+ -[HLPHelpSearchResultTableViewController viewDidLayoutSubviews]
+ -[HLPHelpTableOfContentCell displayTopicsAccessoryView]
+ -[HLPHelpTableOfContentCell setDisplayTopicsAccessoryView:]
+ -[HLPHelpViewController resetLastScrolledPosition]
+ GCC_except_table57
+ GCC_except_table70
+ _OBJC_CLASS_$_ContentMessageViewController
+ _OBJC_CLASS_$_ContentMessageViewModel
+ _OBJC_CLASS_$_UIFontDescriptor
+ _OBJC_IVAR_$_HLPHelpLoadingView._contentMessageViewController
+ _OBJC_IVAR_$_HLPHelpTableOfContentCell._displayTopicsAccessoryView
+ ___43-[HLPHelpLoadingView showMessageWithError:]_block_invoke
+ _objc_msgSend$configurationWithFont:
+ _objc_msgSend$contentMessageViewController
+ _objc_msgSend$displayTopicsAccessoryView
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$initWithContentMessageViewModel:
+ _objc_msgSend$initWithError:defaultMessage:
+ _objc_msgSend$initWithType:additionalContext:defaultMessage:
+ _objc_msgSend$noResultFooterViewWithText:
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:
+ _objc_msgSend$removeContentMessage
+ _objc_msgSend$setContentMessageViewController:
+ _objc_msgSend$setDebugActionHandler:
+ _objc_msgSend$setDisplayTopicsAccessoryView:
+ _objc_msgSend$setFooterView:
+ _objc_msgSend$showHelpBookInfo
+ _objc_msgSend$showMessageWithError:
+ _objc_msgSend$tertiaryLabelColor
- -[HLPHelpLoadingView errorMessageLabel]
- -[HLPHelpLoadingView errorTitleLabel]
- -[HLPHelpLoadingView removeErrorView]
- -[HLPHelpLoadingView setErrorMessageLabel:]
- -[HLPHelpLoadingView setErrorTitleLabel:]
- -[HLPHelpLoadingView showDefaultErrorMessage]
- -[HLPHelpLoadingView showErrorWithTitle:message:]
- -[HLPHelpLoadingView showNoConnectionErrorMessage]
- GCC_except_table53
- GCC_except_table68
- _OBJC_IVAR_$_HLPHelpLoadingView._errorImageView
- _OBJC_IVAR_$_HLPHelpLoadingView._errorMessageLabel
- _OBJC_IVAR_$_HLPHelpLoadingView._errorTitleLabel
- _OBJC_IVAR_$_HLPHelpSearchResultTableViewController._footerLabel
- _OBJC_IVAR_$_HLPHelpTableOfContentCell._accessoryImageViewLeadingConstraint
- _UIFontTextStyleHeadline
- _UIFontTextStyleSubheadline
- _UIFontTextStyleTitle2
- _objc_msgSend$centerXAnchor
- _objc_msgSend$constraintEqualToAnchor:multiplier:
- _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
- _objc_msgSend$imageWithRenderingMode:
- _objc_msgSend$initWithImage:
- _objc_msgSend$isNetworkError:
- _objc_msgSend$labelColor
- _objc_msgSend$removeErrorView
- _objc_msgSend$setAdjustsFontForContentSizeCategory:
- _objc_msgSend$setContentMode:
- _objc_msgSend$setTintColor:
- _objc_msgSend$showDefaultErrorMessage
- _objc_msgSend$showErrorWithTitle:message:
- _objc_msgSend$showNoConnectionErrorMessage
- _objc_msgSend$size
CStrings:
+ "@\"ContentMessageViewController\""
+ "T@\"ContentMessageViewController\",&,N,V_contentMessageViewController"
+ "TB,N,V_displayTopicsAccessoryView"
+ "URLWithTopicID:anchorID:"
+ "_contentMessageViewController"
+ "_displayTopicsAccessoryView"
+ "configurationWithFont:"
+ "contentMessageViewController"
+ "displayTopicsAccessoryView"
+ "fontWithDescriptor:size:"
+ "initWithContentMessageViewModel:"
+ "initWithError:defaultMessage:"
+ "initWithType:additionalContext:defaultMessage:"
+ "noResultFooterViewWithText:"
+ "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
+ "removeContentMessage"
+ "resetLastScrolledPosition"
+ "setContentMessageViewController:"
+ "setDebugActionHandler:"
+ "setDisplayTopicsAccessoryView:"
+ "showMessageWithError:"
+ "tertiaryLabelColor"
- "HLPHelpBook"
- "HLPHelpTOCToggle"
- "No Internet connection."
- "No results found"
- "T@\"UILabel\",&,N,V_errorMessageLabel"
- "T@\"UILabel\",&,N,V_errorTitleLabel"
- "_accessoryImageViewLeadingConstraint"
- "_errorImageView"
- "_errorMessageLabel"
- "_errorTitleLabel"
- "_footerLabel"
- "centerXAnchor"
- "constraintEqualToAnchor:multiplier:"
- "errorMessageLabel"
- "errorTitleLabel"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageWithRenderingMode:"
- "initWithImage:"
- "labelColor"
- "removeErrorView"
- "setAdjustsFontForContentSizeCategory:"
- "setContentMode:"
- "setErrorMessageLabel:"
- "setErrorTitleLabel:"
- "setTintColor:"
- "showDefaultErrorMessage"
- "showErrorWithTitle:message:"
- "showNoConnectionErrorMessage"
- "size"

```
