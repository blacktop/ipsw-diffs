## PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

-1642.6.5.0.0
-  __TEXT.__text: 0xfec8
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0x3240
-  __TEXT.__objc_methlist: 0x8b0
+1677.4.0.0.0
+  __TEXT.__text: 0x11370
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_stubs: 0x38c0
+  __TEXT.__objc_methlist: 0x9a8
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x12d3
-  __TEXT.__objc_methname: 0x32db
-  __TEXT.__oslogstring: 0x170d
-  __TEXT.__objc_classname: 0x16e
-  __TEXT.__objc_methtype: 0x73e
-  __TEXT.__unwind_info: 0x3b8
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0xb50
-  __DATA_CONST.__cfstring: 0xdc0
+  __TEXT.__gcc_except_tab: 0x298
+  __TEXT.__cstring: 0x14eb
+  __TEXT.__objc_methname: 0x3921
+  __TEXT.__oslogstring: 0x186d
+  __TEXT.__objc_classname: 0x16a
+  __TEXT.__objc_methtype: 0x814
+  __TEXT.__unwind_info: 0x410
+  __DATA_CONST.__const: 0xc48
+  __DATA_CONST.__cfstring: 0xf20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x770
-  __DATA.__objc_selrefs: 0xec8
-  __DATA.__objc_ivar: 0x50
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__got: 0x508
+  __DATA.__objc_const: 0x818
+  __DATA.__objc_selrefs: 0x1080
+  __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x360
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41AA08E9-6AB2-3505-B9BA-FE9344E35C7F
-  Functions: 233
-  Symbols:   270
-  CStrings:  911
+  UUID: 24F2878C-FE78-35B4-9429-BCEB3C2AF284
+  Functions: 258
+  Symbols:   289
+  CStrings:  1006
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_PKPeerPaymentMessagesActionConfiguration
+ _OBJC_CLASS_$_PKPeerPaymentQuoteConfiguration
+ _OBJC_CLASS_$_PKPeerPaymentReceiptFlowController
+ _OBJC_CLASS_$_PKPeerPaymentReceiptImageManager
+ _OBJC_CLASS_$_PKReceiptCaptureConfiguration
+ _OBJC_CLASS_$_PKReceiptCaptureViewController
+ _PKAnalyticsReportPeerPaymentBillSplitContextSplitTypeEqualSplit
+ _PKAnalyticsReportPeerPaymentBillSplitContextSplitTypeItemize
+ _PKAnalyticsReportPeerPaymentGroupMessagePageTag
+ _PKAnalyticsReportPeerPaymentPayButtonTag
+ _PKDisplayableErrorPreferredActionKey
+ _PKPeerPaymentExistingiMessageChatForRecipientAddresses
+ _PKURLActionRoutePeerPaymentPendingRequest
+ __Z35PKLocalizedPeerPaymentReceiptStringP8NSString
+ __os_feature_enabled_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x9
- _OBJC_CLASS_$_PKPeerPaymentRecipient
- _OBJC_CLASS_$_UIApplication
- _PKEqualObjects
- _PKUserNotificationActionRouteAddPaymentCard
- _objc_release_x10
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"NSArray\"16@0:8"
+ "@\"PKPeerPaymentReceiptImageManager\""
+ "@\"PKReceiptCaptureViewController\""
+ "Action"
+ "Attempting to send receipt request without image"
+ "BillSplitVI"
+ "ContactHandle"
+ "PEER_PAYMENT_RECEIPT_BUBBLE_UNAVAILABLE_ALERT_BUTTON_TITLE"
+ "PEER_PAYMENT_RECEIPT_BUBBLE_UNAVAILABLE_ALERT_MESSAGE"
+ "PEER_PAYMENT_RECEIPT_BUBBLE_UNAVAILABLE_ALERT_TITLE"
+ "PKPeerPaymentMessagesActionRequestWithReceipt"
+ "PKPeerPaymentMessagesActionRespondToReceiptRequest"
+ "PKPeerPaymentMessagesActionShowPendingRequestDetails"
+ "PKPeerPaymentMessagesActionShowReceiptRequestDetails"
+ "PKPeerPaymentMessagesAppViewController: %p; Handle text input payload with payloadID: %@, payload: %@"
+ "PKPeerPaymentMessagesAppViewController: %p; Unable to find recipient for request message with sender address %@, recipients: %@"
+ "PKStringForKey:"
+ "Peer Payment Messages Extension: Insert receipt request with amount: %@ requestToken: %@"
+ "Peer Payment Messages Extension: Launching pending request details with url: %@"
+ "Peer Payment Messages Extension: cannot fetch thumbnail data for a nil message identifier"
+ "Peer payment add debit card flow presented with success %{public}@."
+ "Received text input payload for unsupported action: %@"
+ "T@\"NSArray\",R,N"
+ "Text input payload does not contain a valid format. Payload: %@"
+ "Wallet"
+ "_confirmPaymentMessageInsertionWithQuote:configuration:completion:"
+ "_insertMessage:completion:"
+ "_insertPaymentMessageWithQuote:configuration:completion:"
+ "_insertReceiptRequestMessageWithConfiguration:requestToken:completion:"
+ "_openWalletURL:forMessage:"
+ "_presentAlertWithDisplayableError:recoveryActionHandler:"
+ "_presentInlineAddDebitCardFlowWithCompletion:"
+ "_receiptCaptureViewController"
+ "_receiptCaptureViewControllerNeedsUpdate"
+ "_receiptImageManager"
+ "_showPendingRequestDetailsForMessage:completion:"
+ "_showReceiptRequestDetailsForMessage:completion:"
+ "_stagePaymentWithConfiguration:completion:"
+ "_stageReceiptRequestWithConfiguration:completion:"
+ "action"
+ "addObjectsFromArray:"
+ "amountStepperView"
+ "billSplitContextWithSplitType:receiptLength:"
+ "com.apple.messages.surf.billsplit"
+ "currentWindowScene"
+ "displayNameForCounterpartHandle:"
+ "displayNameForCounterpartHandle:foundInContacts:"
+ "effectiveGeometry"
+ "fetchImageWithMessageIdentifier:fileTransferDetails:variant:completion:"
+ "flowType"
+ "formalRequestTokenForAmount:source:flowType:completion:"
+ "handleActionWithConfiguration:sender:completion:"
+ "initWithAmount:peerPaymentController:contentDelegate:"
+ "initWithConfiguration:contentDelegate:"
+ "initWithContext:peerPaymentMessage:"
+ "invalidRecipients"
+ "localAccountAddresses"
+ "localAccountAddresses: %@"
+ "mainView"
+ "merchantName"
+ "participantCount"
+ "pk_isPositiveNumber"
+ "presentAddDebitCardFlowWithOrientation:completion:"
+ "presentReceiptFlowFromViewController:configuration:contentDelegate:"
+ "presentedViewController"
+ "quoteWithAmount:configuration:completion:"
+ "receiptButtonTapped"
+ "receiptCaptureDidDismiss"
+ "receiptData"
+ "receiptImage"
+ "receiptRequestType"
+ "receiptThumbnailDataForMessage:completion:"
+ "receiptThumbnailDetails"
+ "recipients"
+ "reportSplitBillPaySplitBillButtonTapWithP2PContext:messagesContext:billSplitContext:"
+ "request"
+ "send"
+ "setAction:"
+ "setCameraViewMode:"
+ "setEntryPoint:"
+ "setFlowType:"
+ "setMerchantName:"
+ "setParticipantCount:"
+ "setPeerPaymentController:"
+ "setPreserveCurrentBalance:"
+ "setPresetReceiptMode:"
+ "setReceiptData:"
+ "setReceiptImageDetails:"
+ "setReceiptRequestType:"
+ "setReceiptThumbnailDetails:"
+ "setRecurringPaymentIdentifier:"
+ "setSource:"
+ "setUsedKeypad:"
+ "split_bill"
+ "storeImage:messageIdentifier:completion:"
+ "updateCoordinatorWithPeerPaymentController:"
+ "uploadImagesWithMessageIdentifier:completion:"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8@\"PKPeerPaymentMessage\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@?0@\"PKPeerPaymentMessageFileTransferDetails\"8@\"PKPeerPaymentMessageFileTransferDetails\"16@\"NSError\"24"
+ "v40@0:8@\"PKPeerPaymentMessagesActionConfiguration\"16@24@?<v@?B>32"
+ "validRecipients"
+ "viewIfLoaded"
+ "wallet://%@/%@/%@"
+ "window"
- "Error inserting message %@ with error: %@"
- "PKArrayContaining:forKey:"
- "PKPeerPaymentGroupInvalidRecipientsKey"
- "PKPeerPaymentGroupValidRecipientsKey"
- "PKPeerPaymentMessagesAppViewController: %p; Unable to find recipient for request message with sender address %@, identifiedRecipients: %@"
- "Text input payload currency amount dictionary does not contain appropriate values: %@"
- "Text input payload currency array contains non-dictionary type: %@"
- "Text input payload does not contain a currency array. Payload: %@"
- "_confirmPaymentMessageInsertionWithQuote:completion:"
- "_insertPaymentMessageWithQuote:completion:"
- "_stagePaymentWithAmount:completion:"
- "displayNameForRecipientAddress:"
- "displayNameForRecipientAddress:foundInContacts:"
- "initWithString:"
- "initWithValidRecipients:invalidRecipients:amount:peerPaymentController:contentDelegate:"
- "openURL:configuration:completionHandler:"
- "quoteWithAmount:source:requestToken:alternateFundingSource:preserveCurrentBalance:recurringPaymentIdentifier:frequency:startDate:threshold:completion:"
- "quoteWithAmount:source:requestToken:completion:"
- "sharedApplication"
- "wallet://%@"
- "windows"

```
