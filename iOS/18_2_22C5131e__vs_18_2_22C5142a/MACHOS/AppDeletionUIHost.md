## AppDeletionUIHost

> `/Applications/AppDeletionUIHost.app/AppDeletionUIHost`

```diff

-631.60.50.0.0
-  __TEXT.__text: 0x3fd0
-  __TEXT.__auth_stubs: 0x3b0
+631.62.3.0.0
+  __TEXT.__text: 0x45cc
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_stubs: 0x15c0
-  __TEXT.__objc_methlist: 0x354
-  __TEXT.__const: 0xb4
-  __TEXT.__objc_methname: 0x2188
-  __TEXT.__cstring: 0xeab
-  __TEXT.__objc_classname: 0x122
-  __TEXT.__oslogstring: 0x598
-  __TEXT.__objc_methtype: 0xf02
-  __TEXT.__ustring: 0x27e
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0x160
+  __TEXT.__objc_methlist: 0x384
+  __TEXT.__const: 0xd0
+  __TEXT.__objc_methname: 0x27b6
+  __TEXT.__cstring: 0xf28
+  __TEXT.__objc_classname: 0x14a
+  __TEXT.__oslogstring: 0x71f
+  __TEXT.__objc_methtype: 0x13cf
+  __TEXT.__ustring: 0x28a
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__cfstring: 0x920
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x24d0
-  __DATA.__objc_selrefs: 0x5f8
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_const: 0x2a60
+  __DATA.__objc_selrefs: 0x600
+  __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x18
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 101
-  Symbols:   115
-  CStrings:  568
+  Functions: 110
+  Symbols:   112
+  CStrings:  652
 
Symbols:
+ _OBJC_CLASS_$_UITextView
+ _UIEdgeInsetsZero
+ __os_log_fault_impl
+ _exit
+ _objc_retain_x26
- _CGSizeZero
- _OBJC_CLASS_$_NSLayoutManager
- _OBJC_CLASS_$_NSTextContainer
- _OBJC_CLASS_$_NSTextStorage
- _OBJC_CLASS_$_UILabel
- _OBJC_CLASS_$_UITapGestureRecognizer
- _objc_retain_x24
- _objc_retain_x25
CStrings:
+ "\x13\x14"
+ "%@ %@"
+ "%s: Attempting to construct the deletion sheet for %@ with type %lu"
+ "%s: Did not receive the number of apps installed via %@!"
+ "%s: Exiting, assuming this is a test for validating crash behavior"
+ "%s: Failed to initialize AppDeletionPresentingViewController"
+ "%s: Presenting the deletion sheet for %@ with type %lu"
+ "%s: Scene class is not of kind SBSUIRemoteAlertScene; failing!"
+ "%s: Successfully configured the deletion sheet for %@ with type %lu"
+ "-[AppDeletionPresentingViewController presentSheetViewController:]"
+ "-[AppDeletionPresentingViewController textView:primaryActionForTextItem:defaultAction:]_block_invoke"
+ "-[AppDeletionUISceneDelegate _communicateAlertInvalidate]"
+ "-[AppDeletionUISceneDelegate sceneDidBecomeActive:]"
+ "@\"NSArray\"40@0:8@\"UITextView\"16{_NSRange=QQ}24"
+ "@\"UIAction\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIAction\"32"
+ "@\"UIMenu\"48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSArray\"40"
+ "@\"UITextItemMenuConfiguration\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIMenu\"32"
+ "@\"UITextView\""
+ "@\"UIView\"24@0:8@\"UIScrollView\"16"
+ "@40@0:8@16{_NSRange=QQ}24"
+ "@48@0:8@16{_NSRange=QQ}24@40"
+ "B24@0:8@\"UIScrollView\"16"
+ "B24@0:8@\"UITextView\"16"
+ "B48@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32"
+ "B48@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32"
+ "B48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSString\"40"
+ "B48@0:8@16@24{_NSRange=QQ}32"
+ "B48@0:8@16{_NSRange=QQ}24@40"
+ "B56@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32q48"
+ "B56@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32q48"
+ "B56@0:8@16@24{_NSRange=QQ}32q48"
+ "DELETION_SHEET_APP_MARKETPLACE_BODY"
+ "NumInstalledApps"
+ "T@\"NSNumber\",R,N,V_numAppsInstalled"
+ "T@\"UITextView\",&,N,V_textView"
+ "TestCrash"
+ "UIScrollViewDelegate"
+ "UITextViewDelegate"
+ "_addBlurredBackgroundToView:"
+ "_communicateAlertInvalidate"
+ "_dismissAlert:"
+ "_numAppsInstalled"
+ "_textView"
+ "addBulletedListItemWithTitle:description:symbolName:tintColor:"
+ "begin"
+ "contentType"
+ "font"
+ "numAppsInstalled"
+ "objectForKeyedSubscript:"
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
+ "scrollViewWillBeginDragging:"
+ "scrollViewWillBeginZooming:withView:"
+ "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
+ "setAlpha:"
+ "setContentSize:"
+ "setEditable:"
+ "setFont:"
+ "setShowsHorizontalScrollIndicator:"
+ "setShowsVerticalScrollIndicator:"
+ "setTextColor:"
+ "setTextContainerInset:"
+ "setTextView:"
+ "systemRedColor"
+ "textAlignment"
+ "textColor"
+ "textContainer"
+ "textView"
+ "textView:didBeginFormattingWithViewController:"
+ "textView:didEndFormattingWithViewController:"
+ "textView:editMenuForTextInRange:suggestedActions:"
+ "textView:menuConfigurationForTextItem:defaultMenu:"
+ "textView:primaryActionForTextItem:defaultAction:"
+ "textView:shouldChangeTextInRange:replacementText:"
+ "textView:shouldInteractWithTextAttachment:inRange:"
+ "textView:shouldInteractWithTextAttachment:inRange:interaction:"
+ "textView:shouldInteractWithURL:inRange:"
+ "textView:shouldInteractWithURL:inRange:interaction:"
+ "textView:textItemMenuWillDisplayForTextItem:animator:"
+ "textView:textItemMenuWillEndForTextItem:animator:"
+ "textView:willBeginFormattingWithViewController:"
+ "textView:willDismissEditMenuWithAnimator:"
+ "textView:willEndFormattingWithViewController:"
+ "textView:willPresentEditMenuWithAnimator:"
+ "textView:writingToolsIgnoredRangesInEnclosingRange:"
+ "textViewDidBeginEditing:"
+ "textViewDidChange:"
+ "textViewDidChangeSelection:"
+ "textViewDidEndEditing:"
+ "textViewShouldBeginEditing:"
+ "textViewShouldEndEditing:"
+ "textViewWritingToolsDidEnd:"
+ "textViewWritingToolsWillBegin:"
+ "v24@0:8@\"UIScrollView\"16"
+ "v24@0:8@\"UITextView\"16"
+ "v28@0:8@\"UIScrollView\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
+ "v32@0:8@\"UITextView\"16@\"<UIEditMenuInteractionAnimating>\"24"
+ "v32@0:8@\"UITextView\"16@\"UITextFormattingViewController\"24"
+ "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
+ "v40@0:8@\"UITextView\"16@\"UITextItem\"24@\"<UIContextMenuInteractionAnimating>\"32"
+ "v40@0:8@16@24d32"
+ "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
+ "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
+ "viewForZoomingInScrollView:"
- "\x14\x11"
- "%@\n\n%@"
- "%s: Failed to construct AppDeletionPresentingVC"
- "-[AppDeletionPresentingViewController _openURLOnTap:]_block_invoke"
- "-[AppDeletionUISceneDelegate communicateAlertInvalidate]"
- "DELETION_SHEET_ALTERNATE_APP_MARKETPLACE_SECOND"
- "DELETION_SHEET_APPSTORE_BODY_FIRST"
- "Learn more..."
- "_openURLOnTap:"
- "addGestureRecognizer:"
- "addLayoutManager:"
- "addTextContainer:"
- "attributedText"
- "characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:"
- "communicateAlertInvalidate"
- "contentView"
- "dismissAlert:"
- "initWithAttributedString:"
- "initWithSize:"
- "initWithTarget:action:"
- "length"
- "lineBreakMode"
- "locationInView:"
- "setLineBreakMode:"
- "setNumberOfLines:"
- "setNumberOfTapsRequired:"
- "setSize:"
- "setText:"
- "setUserInteractionEnabled:"
- "unsignedLongValue"

```
