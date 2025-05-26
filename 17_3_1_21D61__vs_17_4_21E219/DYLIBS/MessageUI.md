## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0xfa4a4
-  __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_methlist: 0xd36c
-  __TEXT.__gcc_except_tab: 0x20280
-  __TEXT.__cstring: 0x89c6
+3774.500.171.2.2
+  __TEXT.__text: 0xf9f14
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0xd3ec
+  __TEXT.__gcc_except_tab: 0x20408
+  __TEXT.__cstring: 0x88a6
   __TEXT.__const: 0x744
   __TEXT.__oslogstring: 0x46ef
   __TEXT.__ustring: 0x4d2

   __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__objc_const_ax: 0x4c4
-  __TEXT.__unwind_info: 0x94ec
-  __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x20fc
-  __TEXT.__objc_methname: 0x31c18
-  __TEXT.__objc_methtype: 0xa9d8
-  __TEXT.__objc_stubs: 0x21a80
+  __TEXT.__unwind_info: 0x94a8
+  __TEXT.__eh_frame: 0x158
+  __TEXT.__objc_classname: 0x20fb
+  __TEXT.__objc_methname: 0x31f38
+  __TEXT.__objc_methtype: 0xaa43
+  __TEXT.__objc_stubs: 0x21be0
   __DATA_CONST.__got: 0x9f8
-  __DATA_CONST.__const: 0x41c8
+  __DATA_CONST.__const: 0x41f0
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ac90
-  __DATA_CONST.__objc_selrefs: 0xa270
+  __DATA_CONST.__objc_const: 0x1add0
+  __DATA_CONST.__objc_selrefs: 0xa2c8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0xf98
+  __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __AUTH_CONST.__cfstring: 0x8b80
+  __AUTH_CONST.__cfstring: 0x8bc0
   __AUTH_CONST.__objc_const: 0x55c0
-  __AUTH_CONST.__const: 0xe50
+  __AUTH_CONST.__const: 0xe90
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH_CONST.__auth_got: 0xdb0
   __AUTH.__objc_data: 0x2948
   __AUTH.__data: 0x160
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xf98
-  __DATA.__objc_superrefs: 0x498
-  __DATA.__objc_ivar: 0x1070
+  __DATA.__objc_ivar: 0x1074
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x3110
   __DATA.__bss: 0x3d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5435
-  Symbols:   22851
-  CStrings:  10692
+  Functions: 5444
+  Symbols:   22905
+  CStrings:  10725
 
Symbols:
+ -[MFCaptionLabel _attributedStringForImage:]
+ -[MFCaptionLabel _concatenateStringForRecipientList:recipientCount:prefixGenerationBlock:listSuffix:]
+ -[MFCaptionLabel _formattedReplyToString]
+ -[MFCaptionLabel _maxWidthForRecipientList]
+ -[MFCaptionLabel _questionMarkAttributedString]
+ -[MFCaptionLabel _questionMarkImage]
+ -[MFCaptionLabel _whitespaceTextAttachment]
+ -[MFCaptionLabel hasDifferentReplyToAddress]
+ -[MFCaptionLabel lengthValidationBlock]
+ -[MFCaptionLabel replyToSenders]
+ -[MFCaptionLabel setHasDifferentReplyToAddress:]
+ -[MFCaptionLabel setReplyToSenders:]
+ -[MFSecureMIMEPersonHeaderView initWithFrame:warningLabelTextColor:]
+ GCC_except_table698
+ GCC_except_table699
+ _MFImageGlyphQuestionMark
+ _OBJC_IVAR_$_MFCaptionLabel._hasDifferentReplyToAddress
+ _OBJC_IVAR_$_MFCaptionLabel._replyToSenders
+ ___33-[MFMailComposeController close:]_block_invoke.639
+ ___36-[MFCaptionLabel _questionMarkImage]_block_invoke
+ ___38-[MFMailComposeController performSend]_block_invoke.672
+ ___38-[MFMailComposeController performSend]_block_invoke.673
+ ___38-[MFMailComposeController performSend]_block_invoke.674
+ ___38-[MFMailComposeController performSend]_block_invoke.675
+ ___39-[MFCaptionLabel lengthValidationBlock]_block_invoke
+ ___39-[MFMailComposeController sendMessage:]_block_invoke.870
+ ___40-[MFMailComposeController insertDrawing]_block_invoke.309
+ ___41-[MFCaptionLabel _formattedReplyToString]_block_invoke
+ ___41-[MFCaptionLabel _formattedReplyToString]_block_invoke_2
+ ___45-[MFMailComposeController _finishedComposing]_block_invoke.881
+ ___45-[MFMailComposeController _finishedComposing]_block_invoke.884
+ ___47-[MFMailComposeController autosaveWithHandler:]_block_invoke.615
+ ___50-[MFMailComposeController _loadCompositionContext]_block_invoke.227
+ ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.480
+ ___64-[MFMailComposeController _prepareHMEAddressesWithContinuation:]_block_invoke.681
+ ___64-[MFMailComposeController _prepareHMEAddressesWithContinuation:]_block_invoke.688
+ ___66-[MFMailComposeController _setUpDeliveryObject:completionHandler:]_block_invoke.651
+ ___66-[MFMailComposeController _setUpDeliveryObject:completionHandler:]_block_invoke.657
+ ___66-[MFMailComposeController _setUpDeliveryObject:completionHandler:]_block_invoke.660
+ ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.757
+ ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.757.cold.1
+ ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.759
+ ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.759.cold.1
+ ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.767
+ ___74-[MFMailComposeController documentCameraViewController:didFinishWithScan:]_block_invoke.325
+ ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke.737
+ ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke.747
+ ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke.753
+ ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke_2.756
+ ___block_descriptor_32_e18_"NSString"16?0Q8l
+ ___block_descriptor_40_ea8_32s_e31_B24?0"NSString"8"NSString"16ls32l8
+ ___block_literal_global.1002
+ ___block_literal_global.1028
+ ___block_literal_global.194
+ ___block_literal_global.2264
+ ___block_literal_global.2273
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.287
+ ___block_literal_global.296
+ ___block_literal_global.339
+ ___block_literal_global.348
+ ___block_literal_global.360
+ ___block_literal_global.366
+ ___block_literal_global.45
+ ___block_literal_global.52
+ ___block_literal_global.559
+ ___block_literal_global.561
+ ___block_literal_global.575
+ ___block_literal_global.61
+ ___block_literal_global.621
+ ___block_literal_global.626
+ ___block_literal_global.742
+ ___block_literal_global.750
+ ___block_literal_global.755
+ _objc_msgSend$_attributedStringForImage:
+ _objc_msgSend$_concatenateStringForRecipientList:recipientCount:prefixGenerationBlock:listSuffix:
+ _objc_msgSend$_formattedReplyToString
+ _objc_msgSend$_maxWidthForRecipientList
+ _objc_msgSend$_questionMarkAttributedString
+ _objc_msgSend$_questionMarkImage
+ _objc_msgSend$_whitespaceTextAttachment
+ _objc_msgSend$hasDifferentReplyToAddress
+ _objc_msgSend$initWithFrame:warningLabelTextColor:
+ _objc_msgSend$lengthValidationBlock
+ _objc_msgSend$replyToSenders
- -[MFMailComposeController drawingInsertCount]
- -[MFMailComposeController setDrawingInsertCount:]
- GCC_except_table700
- GCC_except_table701
- _OBJC_IVAR_$_MFMailComposeController._drawingInsertCount
- ___33-[MFMailComposeController close:]_block_invoke.635
- ___38-[MFMailComposeController performSend]_block_invoke.662
- ___38-[MFMailComposeController performSend]_block_invoke.663
- ___38-[MFMailComposeController performSend]_block_invoke.664
- ___38-[MFMailComposeController performSend]_block_invoke.665
- ___39-[MFMailComposeController sendMessage:]_block_invoke.866
- ___40-[MFMailComposeController insertDrawing]_block_invoke.308
- ___44-[MFCaptionLabel _formattedAttributedString]_block_invoke_3
- ___45-[MFMailComposeController _finishedComposing]_block_invoke.877
- ___45-[MFMailComposeController _finishedComposing]_block_invoke.880
- ___47-[MFMailComposeController autosaveWithHandler:]_block_invoke.611
- ___50-[MFMailComposeController _loadCompositionContext]_block_invoke.226
- ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.478
- ___64-[MFMailComposeController _prepareHMEAddressesWithContinuation:]_block_invoke.673
- ___64-[MFMailComposeController _prepareHMEAddressesWithContinuation:]_block_invoke.684
- ___66-[MFMailComposeController _setUpDeliveryObject:completionHandler:]_block_invoke.647
- ___66-[MFMailComposeController _setUpDeliveryObject:completionHandler:]_block_invoke.653
- ___66-[MFMailComposeController _setUpDeliveryObject:completionHandler:]_block_invoke.656
- ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.753
- ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.753.cold.1
- ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.755
- ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.755.cold.1
- ___70-[MFMailComposeController _checkForShareParticipantsWithContinuation:]_block_invoke.763
- ___74-[MFMailComposeController documentCameraViewController:didFinishWithScan:]_block_invoke.324
- ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke.733
- ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke.743
- ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke.749
- ___91-[MFMailComposeController _checkForOmittedRecipientsOrAttachmentsIfNeededWithContinuation:]_block_invoke_2.748
- ___block_descriptor_48_ea8_32s_e31_B24?0"NSString"8"NSString"16ls32l8
- ___block_literal_global.1022
- ___block_literal_global.193
- ___block_literal_global.2267
- ___block_literal_global.2276
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.286
- ___block_literal_global.295
- ___block_literal_global.338
- ___block_literal_global.347
- ___block_literal_global.359
- ___block_literal_global.365
- ___block_literal_global.41
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.571
- ___block_literal_global.617
- ___block_literal_global.622
- ___block_literal_global.738
- ___block_literal_global.746
- ___block_literal_global.751
- ___block_literal_global.998
- _swift_bridgeObjectRetain
CStrings:
+ "\x02\x18/\x0e1&\x14\x15Q'\x16\x12\x13\x13\x11"
+ "&"
+ "@\"NSString\"24@0:8@\"WKWebView\"16"
+ "@48@0:8@16Q24@?32@40"
+ "Reply To:"
+ "T@\"<UITextInputSuggestionDelegate>\",?,R,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSArray\",C,N,V_replyToSenders"
+ "T@\"NSIndexSet\",?,C,N"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"RTIInputSystemSourceSession\",?,R,N"
+ "T@\"UIColor\",?,&,N"
+ "T@\"UIImage\",?,&,N"
+ "T@\"UIInputContextHistory\",?,&,N"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UITextRange\",?,R,N"
+ "T@\"UIView\",?,R,N"
+ "T@\"_UISupplementalLexicon\",?,&,N"
+ "T@,?,N"
+ "T@,?,R,N"
+ "TB,?,D,N"
+ "TB,?,D,N,GisSecureTextEntry"
+ "TB,?,N"
+ "TB,?,N,GisDevicePasscodeEntry"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R,N"
+ "TB,N,V_hasDifferentReplyToAddress"
+ "TQ,?,N"
+ "T^{__CFCharacterSet=},?,N"
+ "Td,?,N"
+ "Ti,?,N"
+ "Tq,?,D,N"
+ "Tq,?,N"
+ "Tq,?,R,N"
+ "T{UIEdgeInsets=dddd},?,N"
+ "T{_NSRange=QQ},?,N"
+ "_attributedStringForImage:"
+ "_concatenateStringForRecipientList:recipientCount:prefixGenerationBlock:listSuffix:"
+ "_formattedReplyToString"
+ "_hasDifferentReplyToAddress"
+ "_hostSceneBundleIdentifierForWebView:"
+ "_hostSceneIdentifierForWebView:"
+ "_maxWidthForRecipientList"
+ "_questionMarkAttributedString"
+ "_questionMarkImage"
+ "_replyToSenders"
+ "_webView:startXRSessionWithFeatures:completionHandler:"
+ "_whitespaceTextAttachment"
+ "captionLabel.questionMark"
+ "caretTransformForPosition:"
+ "hasDifferentReplyToAddress"
+ "initWithFrame:warningLabelTextColor:"
+ "lengthValidationBlock"
+ "matchHighlightColor"
+ "replyToSenders"
+ "setHasDifferentReplyToAddress:"
+ "setMatchHighlightColor:"
+ "setReplyToSenders:"
+ "setTypingAdaptationDisabled:"
+ "typingAdaptationDisabled"
+ "v40@0:8@\"WKWebView\"16Q24@?<v@?@@\"UIViewController\">32"
+ "\xf0\xf0\xf0\xf0a!\x12\xe1\xa1"
- "\x02\x18/\x0e1&\x14\x15Q#\x14\x16\x12\x13\x13\x11"
- "%"
- "Division by zero in remainder operation"
- "Division results in an overflow in remainder operation"
- "StaticString should have Unicode scalar representation"
- "StaticString should have pointer representation"
- "Swift/IntegerTypes.swift"
- "T@\"<UITextInputSuggestionDelegate>\",R,N"
- "T@\"NSIndexSet\",C,N"
- "T@\"RTIInputSystemSourceSession\",R,N"
- "T@\"UIImage\",&,N"
- "T@\"UIInputContextHistory\",&,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@\"UIView\",R,N"
- "T@\"_UISupplementalLexicon\",&,N"
- "T@,N"
- "TB,D,N,GisSecureTextEntry"
- "TB,N,GisDevicePasscodeEntry"
- "TB,N,GisSecureTextEntry"
- "T^{__CFCharacterSet=},N"
- "Tq,D,N"
- "Tq,N,V_drawingInsertCount"
- "T{UIEdgeInsets=dddd},N"
- "T{_NSRange=QQ},N"
- "UnsafeBufferPointer has a nil start and nonzero count"
- "_drawingInsertCount"
- "_webView:requestWebAuthenticationNoGestureForOrigin:completionHandler:"
- "drawingInsertCount"
- "setDrawingInsertCount:"
- "\xf0\xf0\xf0\xf0a!\x12\xf1\xa1"

```
