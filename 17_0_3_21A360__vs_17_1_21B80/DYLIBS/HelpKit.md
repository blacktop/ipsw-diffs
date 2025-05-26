## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

-170.0.0.0.0
-  __TEXT.__text: 0x25e74
+174.0.0.0.0
+  __TEXT.__text: 0x26c8c
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x2aa4
+  __TEXT.__objc_methlist: 0x2b1c
   __TEXT.__const: 0xd8
   __TEXT.__gcc_except_tab: 0x928
-  __TEXT.__cstring: 0x17b2
+  __TEXT.__cstring: 0x1810
   __TEXT.__oslogstring: 0x318
   __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x9cc
-  __TEXT.__objc_classname: 0x5b6
-  __TEXT.__objc_methname: 0x8eb8
-  __TEXT.__objc_methtype: 0x1a81
-  __TEXT.__objc_stubs: 0x6d80
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xdf0
+  __TEXT.__unwind_info: 0x9c4
+  __TEXT.__objc_classname: 0x5f0
+  __TEXT.__objc_methname: 0x92c8
+  __TEXT.__objc_methtype: 0x1c23
+  __TEXT.__objc_stubs: 0x6fc0
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4900
-  __DATA_CONST.__objc_selrefs: 0x2118
-  __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__cfstring: 0x2880
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__objc_const: 0x1158
-  __AUTH_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_const: 0x4bc0
+  __DATA_CONST.__objc_selrefs: 0x21b0
+  __DATA_CONST.__objc_arraydata: 0x80
+  __AUTH_CONST.__cfstring: 0x2940
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__objc_const: 0x1118
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0x378
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_classrefs: 0x340
+  __DATA.__objc_classrefs: 0x358
   __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x3f4
-  __DATA.__data: 0x7f8
-  __DATA.__bss: 0x1a0
+  __DATA.__objc_ivar: 0x400
+  __DATA.__data: 0x8b8
+  __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1035
-  Symbols:   4064
-  CStrings:  2234
+  Functions: 1049
+  Symbols:   4126
+  CStrings:  2294
 
Symbols:
+ +[HLPCommonDefines isVisionOS]
+ -[HLPHelpLoadingView initWithFrame:]
+ -[HLPHelpTableOfContentCell accessoryButton]
+ -[HLPHelpTableOfContentCell delegate]
+ -[HLPHelpTableOfContentCell setAccessoryButton:]
+ -[HLPHelpTableOfContentCell setDelegate:]
+ -[HLPHelpTableOfContentCell updateFont]
+ -[HLPHelpTableOfContentViewController tableOfContentCellRowToggled:]
+ -[HLPHelpTopicViewController isSingleTopic]
+ -[HLPHelpTopicViewController scrollViewDidScroll:]
+ -[HLPHelpTopicViewController setSingleTopic:]
+ -[HLPHelpTopicViewController updateNavigationBar]
+ -[HLPHelpViewController fullBookViewSeparator]
+ -[HLPHelpViewController platform]
+ -[HLPHelpViewController setFullBookViewSeparator:]
+ -[HLPHelpViewController setTopicViewController:]
+ -[HLPHelpViewController topicViewController]
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table7
+ _OBJC_CLASS_$_UIAction
+ _OBJC_CLASS_$_UIButtonConfiguration
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_IVAR_$_HLPHelpTableOfContentCell._accessoryButton
+ _OBJC_IVAR_$_HLPHelpTableOfContentCell._accessoryButtonLeadingConstraint
+ _OBJC_IVAR_$_HLPHelpTableOfContentCell._accessoryButtonTrailingConstraint
+ _OBJC_IVAR_$_HLPHelpTableOfContentCell._delegate
+ _OBJC_IVAR_$_HLPHelpTableOfContentViewController._initialized
+ _OBJC_IVAR_$_HLPHelpTopicViewController._singleTopic
+ _UIFontTextStyleTitle3
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HLPHelpTableOfContentCellDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HLPHelpTableOfContentCellDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate
+ __OBJC_$_PROTOCOL_REFS_HLPHelpTableOfContentCellDelegate
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_HLPHelpTableOfContentCellDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIScrollViewDelegate
+ __OBJC_PROTOCOL_$_HLPHelpTableOfContentCellDelegate
+ __OBJC_PROTOCOL_$_UIScrollViewDelegate
+ ___30+[HLPCommonDefines isVisionOS]_block_invoke
+ ___59-[HLPHelpTableOfContentCell initWithStyle:reuseIdentifier:]_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64s72s80s88s96s104w_e42_v28?0B8"NSError"12"NSHTTPURLResponse"20lw104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"UIAction"8ls32l8
+ ___block_literal_global.3
+ ___block_literal_global.51
+ __unnamed_array_storage.289
+ _isVisionOS._isVisionOS
+ _isVisionOS.onceToken
+ _objc_msgSend$accessoryButton
+ _objc_msgSend$actionWithHandler:
+ _objc_msgSend$borderlessButtonConfiguration
+ _objc_msgSend$buttonWithConfiguration:primaryAction:
+ _objc_msgSend$configurationWithScale:
+ _objc_msgSend$fullBookViewSeparator
+ _objc_msgSend$helpItem
+ _objc_msgSend$imageWithRenderingMode:
+ _objc_msgSend$imageWithTintColor:renderingMode:
+ _objc_msgSend$initWithRootViewController:
+ _objc_msgSend$isVisionOS
+ _objc_msgSend$labelColor
+ _objc_msgSend$platform
+ _objc_msgSend$setOpaque:
+ _objc_msgSend$setSingleTopic:
+ _objc_msgSend$setTintColor:
+ _objc_msgSend$superview
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _objc_msgSend$tableOfContentCellRowToggled:
+ _objc_msgSend$tableOfContentViewController
+ _objc_msgSend$tableView:didSelectRowAtIndexPath:
+ _objc_msgSend$topicViewController
+ _objc_msgSend$updateFont
+ _objc_msgSend$updateNavigationBar
- -[HLPHelpItem decodedName]
- -[HLPHelpLoadingView init]
- -[HLPHelpTableOfContentCell arrowImageView]
- -[HLPHelpTableOfContentCell setArrowImageView:]
- -[NSString(HLPAdditions) htmlDecodedString]
- GCC_except_table26
- GCC_except_table38
- GCC_except_table49
- GCC_except_table51
- _NSCharacterEncodingDocumentAttribute
- _NSDocumentTypeDocumentAttribute
- _NSHTMLTextDocumentType
- _OBJC_CLASS_$_NSAttributedString
- _OBJC_IVAR_$_HLPHelpItem._decodedName
- _OBJC_IVAR_$_HLPHelpTableOfContentCell._arrowImageView
- _OBJC_IVAR_$_HLPHelpTableOfContentCell._arrowImageViewLeadingConstraint
- __OBJC_$_CATEGORY_NSString_$_HLPAdditions
- __OBJC_$_INSTANCE_METHODS_NSString(HLPAdditions)
- ___block_descriptor_106_e8_32s40s48s56s64s72s80s88s96w_e42_v28?0B8"NSError"12"NSHTTPURLResponse"20lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.50
- __unnamed_array_storage.283
- _objc_msgSend$arrowImageView
- _objc_msgSend$decodedName
- _objc_msgSend$htmlDecodedString
- _objc_msgSend$initWithData:options:documentAttributes:error:
- _objc_msgSend$setAdjustsImageSizeForAccessibilityContentSizeCategory:
- _objc_msgSend$string
CStrings:
+ "\x01"
+ "\x06$"
+ "\x14/\x03"
+ "\x16)"
+ "3"
+ "@\"<HLPHelpTableOfContentCellDelegate>\""
+ "@\"UIView\"24@0:8@\"UIScrollView\"16"
+ "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "B24@0:8@\"UIScrollView\"16"
+ "HLPHelpTableOfContentCellDelegate"
+ "T@\"<HLPHelpTableOfContentCellDelegate>\",W,N,V_delegate"
+ "T@\"HLPHelpTopicViewController\",&,N,V_topicViewController"
+ "T@\"UIButton\",&,N,V_accessoryButton"
+ "T@\"UIView\",&,N,V_fullBookViewSeparator"
+ "TB,N,GisSingleTopic,V_singleTopic"
+ "UIScrollViewDelegate"
+ "_accessoryButton"
+ "_accessoryButtonLeadingConstraint"
+ "_accessoryButtonTrailingConstraint"
+ "_initialized"
+ "_singleTopic"
+ "a"
+ "accessoryButton"
+ "actionWithHandler:"
+ "apple-vision-pro"
+ "assistive-access"
+ "borderlessButtonConfiguration"
+ "buttonWithConfiguration:primaryAction:"
+ "chevron.right"
+ "configurationWithScale:"
+ "fullBookViewSeparator"
+ "imageWithRenderingMode:"
+ "imageWithTintColor:renderingMode:"
+ "initWithRootViewController:"
+ "isSingleTopic"
+ "isVisionOS"
+ "labelColor"
+ "scrollViewDidChangeAdjustedContentInset:"
+ "scrollViewDidEndDecelerating:"
+ "scrollViewDidEndDragging:willDecelerate:"
+ "scrollViewDidEndScrollingAnimation:"
+ "scrollViewDidEndZooming:withView:atScale:"
+ "scrollViewDidScroll:"
+ "scrollViewDidScrollToTop:"
+ "scrollViewDidZoom:"
+ "scrollViewShouldScrollToTop:"
+ "scrollViewWillBeginDecelerating:"
+ "scrollViewWillBeginZooming:withView:"
+ "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
+ "setAccessoryButton:"
+ "setFullBookViewSeparator:"
+ "setOpaque:"
+ "setSingleTopic:"
+ "setTintColor:"
+ "setTopicViewController:"
+ "single-topic"
+ "singleTopic"
+ "superview"
+ "systemImageNamed:withConfiguration:"
+ "tableOfContentCellRowToggled:"
+ "topicViewController"
+ "updateFont"
+ "updateNavigationBar"
+ "v16@?0@\"UIAction\"8"
+ "v24@0:8@\"HLPHelpTableOfContentCell\"16"
+ "v24@0:8@\"UIScrollView\"16"
+ "v28@0:8@\"UIScrollView\"16B24"
+ "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
+ "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
+ "v40@0:8@16@24d32"
+ "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
+ "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
+ "viewForZoomingInScrollView:"
+ "vision"
+ "visionos"
- "\x013"
- "\x04\x15"
- "\x06)"
- "\x16/\x01"
- "T@\"UIImageView\",&,N,V_arrowImageView"
- "_arrowImageView"
- "_arrowImageViewLeadingConstraint"
- "_decodedName"
- "arrowImageView"
- "decodedName"
- "htmlDecodedString"
- "initWithData:options:documentAttributes:error:"
- "setAdjustsImageSizeForAccessibilityContentSizeCategory:"
- "setArrowImageView:"
- "string"

```
