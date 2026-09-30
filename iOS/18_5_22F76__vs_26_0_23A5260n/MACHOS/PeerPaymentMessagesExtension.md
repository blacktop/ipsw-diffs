## PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

-1591.6.7.0.0
-  __TEXT.__text: 0xcb98
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0x7c8
-  __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x280
-  __TEXT.__cstring: 0x1075
-  __TEXT.__objc_methname: 0x2c77
-  __TEXT.__oslogstring: 0x167c
+1619.6.3.0.0
+  __TEXT.__text: 0xebd8
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x3120
+  __TEXT.__objc_methlist: 0x898
+  __TEXT.__const: 0xb8
+  __TEXT.__gcc_except_tab: 0x1cc
+  __TEXT.__cstring: 0x120a
+  __TEXT.__objc_methname: 0x31c2
+  __TEXT.__oslogstring: 0x1683
+  __TEXT.__ustring: 0x12e
   __TEXT.__objc_classname: 0x16e
-  __TEXT.__objc_methtype: 0x6fe
-  __TEXT.__unwind_info: 0x308
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x9f0
-  __DATA_CONST.__cfstring: 0xc40
+  __TEXT.__objc_methtype: 0x721
+  __TEXT.__unwind_info: 0x370
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__cfstring: 0xe00
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0xd08
-  __DATA.__objc_ivar: 0x48
+  __DATA.__objc_const: 0x760
+  __DATA.__objc_selrefs: 0xe78
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x360
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DCEA2710-69E0-3FD9-99B1-69016F4B1EE5
-  Functions: 181
-  Symbols:   248
-  CStrings:  825
+  UUID: DE85F0E3-DAF3-3DF1-A08E-D17DB6A0FDF6
+  Functions: 219
+  Symbols:   275
+  CStrings:  900
 
Symbols:
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_PKPaymentTransactionRequest
+ _OBJC_CLASS_$_PKPeerPaymentDeviceScoreAttributes
+ _OBJC_CLASS_$_PKPeerPaymentInformalRequestToken
+ _OBJC_CLASS_$_PKPeerPaymentMessagesRecipientPickerViewController
+ _OBJC_CLASS_$_PKPeerPaymentRecipient
+ _PKAnalyticsReportPeerPaymentDataDetectorMenuPageTag
+ _PKAnalyticsReportPeerPaymentDataDetectorSendButtonTag
+ _PKAnalyticsReportPeerPaymentErrorAmbiguousSenderPageTag
+ _PKAnalyticsReportPeerPaymentErrorNoEligibleParticipantsPageTag
+ _PKAnalyticsReportPeerPaymentErrorRecipientUnavailablePageTag
+ _PKAnalyticsReportPeerPaymentMessagesAppExtensionPageTag
+ _PKAnalyticsReportPeerPaymentMessagesContextConversationTypeGroup
+ _PKAnalyticsReportPeerPaymentMessagesContextConversationTypeIndividual
+ _PKAnalyticsReportPeerPaymentMessagesContextConversationTypeKey
+ _PKAnalyticsReportPeerPaymentMessagesContextGroupSizeKey
+ _PKAnalyticsReportPeerPaymentMessagesContextIneligibleCountKey
+ _PKAnalyticsReportPeerPaymentMessagesContextRequestTypeClosed
+ _PKAnalyticsReportPeerPaymentMessagesContextRequestTypeInformal
+ _PKAnalyticsReportPeerPaymentMessagesContextRequestTypeKey
+ _PKAnalyticsReportPeerPaymentMessagesContextRequestTypeOpen
+ _PKAnalyticsReportPeerPaymentMessagesContextStyleCompact
+ _PKAnalyticsReportPeerPaymentMessagesContextStyleExpanded
+ _PKAnalyticsReportPeerPaymentMessagesContextStyleKey
+ _PKIDSSanitizedAddress
+ _PKOSVariantSubsystem
+ _PKPeerPaymentGroupDisclosureWarningSeen
+ _PKPeerPaymentSetGroupDisclosureWarningSeen
+ __UISolariumFeatureFlagEnabled
+ __os_log_debug_impl
+ __os_log_error_impl
+ _objc_release_x2
+ _os_variant_has_internal_ui
- _OBJC_CLASS_$_PKPeerPaymentRequestToken
- _PKAnalyticsReportPeerPaymentAmountSelectionPageTag
- _PKAnalyticsReportPeerPaymentErrorInvalidRecipientPageTag
- _PKAnalyticsReportPeerPaymentP2PContextMessagesCompact
- _PKPeerPaymentDeviceScoreEndpointIdentifierQuote
- _PKPeerPaymentDeviceScoreEndpointIdentifierRequestToken
CStrings:
+ "1"
+ "=ب\xdeW"
+ "@\"NSDictionary\""
+ "A"
+ "B16@?0@\"NSString\"8"
+ "B24@0:8Q16"
+ "Current content state when reporting analytics: %@"
+ "I Understand"
+ "Not calling Perform on peer payment quote for message %@"
+ "PEER_PAYMENT_ERROR_INVALID_RECIPIENT_MESSAGE"
+ "PEER_PAYMENT_ERROR_INVALID_RECIPIENT_TITLE"
+ "PEER_PAYMENT_MESSAGES_GROUP_RECIPIENTS_INVALID"
+ "PKArrayContaining:forKey:"
+ "PKPeerPaymentGroupInvalidRecipientsKey"
+ "PKPeerPaymentGroupValidRecipientsKey"
+ "PKPeerPaymentMessagesActionChooseRecipient"
+ "PKPeerPaymentMessagesActionContinue"
+ "PKPeerPaymentMessagesActionEnterAmount"
+ "PKPeerPaymentMessagesActionRequestWithoutAmount"
+ "PKPeerPaymentMessagesAppViewController: %p; Asked to handle a Payment Message of incorrect type: %@"
+ "PKPeerPaymentMessagesAppViewController: %p; Did become active with conversation: %@, recipientAddresses:%@"
+ "PKPeerPaymentMessagesAppViewController: %p; Did cancel sending message: %@"
+ "PKPeerPaymentMessagesAppViewController: %p; Did start sending message: %@"
+ "PKPeerPaymentMessagesAppViewController: %p; Handle Payment Request Message: %@"
+ "PKPeerPaymentMessagesAppViewController: %p; Handle action: %{public}@, handled: %{public}@"
+ "PKPeerPaymentMessagesAppViewController: %p; Will become active with conversation: %@, recipientAddresses:%@"
+ "Peer Payment Messages Extension: Updating content state in response to a change in group message support."
+ "SenderHandle"
+ "_analyticsMessagesContext"
+ "_conversationAddress"
+ "_handleRecipientError:"
+ "_handleRespondToPaymentRequestActionWithMessage:completion:"
+ "_identifiedRecipientForRecipientAddress:"
+ "_identifiedRecipients"
+ "_identifyGroupRecipientsWithCompletion:"
+ "_identifyRecipient"
+ "_pendingInformalPaymentRequestRecipientAddress"
+ "_prepareIdentifiedRecipient:forAmountEntryViewController:"
+ "_prewarmDeviceScoreForGroupsWithRecipients:"
+ "_recipientAddressFoundInContacts:"
+ "_recipientErrorTitle"
+ "_reportAnalyticsForStateWithEventType:"
+ "_reportAnalyticsStagedBubbleButtonTap:"
+ "_resetIdentifiedRecipientForAmountEntryViewController:"
+ "_shouldEmbedViewControllerInNavigationControllerForState:"
+ "_unregisterAppViewController:"
+ "addObject:"
+ "allowsPaymentRequests"
+ "bucketValueForGroupSize:"
+ "bucketValueForIneligibleCount:"
+ "clearColor"
+ "context"
+ "conversationAddress"
+ "conversationSize"
+ "identifyRecipientWithConversationAddress:senderAddress:completion:"
+ "identifyRecipientsWithConversationAddresses:senderAddress:completion:"
+ "idsQualifiedNormalizedAddress"
+ "ineligibleCount"
+ "initWithValidRecipients:invalidRecipients:amount:peerPaymentController:contentDelegate:"
+ "invalidateMessageTintColor"
+ "isFromMe"
+ "messageTintColor"
+ "messagesContext"
+ "navigationController"
+ "normalizedAddress"
+ "peerPaymentRequestToken"
+ "pk_firstObjectPassingTest:"
+ "pk_isGreaterThan:"
+ "preferredUserInterfaceStyle"
+ "prewarmDeviceScoreForAttributes:"
+ "q16@0:8"
+ "referenceBackgroundColorForState:"
+ "reportAnalyticsInternally"
+ "reportAppleCashEvent:withMessagesContext:"
+ "selectIdentifiedRecipient:"
+ "setCenterAction:"
+ "setContext:"
+ "setEndpoint:"
+ "setLeadingAction:"
+ "setLimit:"
+ "setMessagesContext:"
+ "setPeerPaymentRequestToken:"
+ "setQuoteRequestDestination:"
+ "setRecipient:"
+ "setRecipientAddresses:"
+ "setTrailingAction:"
+ "setViewControllers:"
+ "supportsGroupMessage"
+ "token"
+ "transactionsForRequest:completion:"
+ "updateSupportsGroupMessage"
+ "v20@?0B8@\"NSError\"12"
+ "zero"
- "Memo updated for recurring payment %@"
- "Not performing a peer payment quote for message %@"
- "Peer Payment Messages Extension: Asked to handle a Payment Message of incorrect type: %@"
- "Peer Payment Messages Extension: Did become active with conversation: %@, recipientAddresses:%@"
- "Peer Payment Messages Extension: Did cancel sending message: %@"
- "Peer Payment Messages Extension: Did start sending message: %@"
- "Peer Payment Messages Extension: Handle Payment Request Message: %@"
- "Peer Payment Messages Extension: Handle action: %{public}@, handled: %{public}@"
- "Peer Payment Messages Extension: Will become active with conversation: %@, recipientAddresses:%@"
- "Presenting peer payment setup flow via url."
- "Presenting peer payment setup flow via view service."
- "Recurring payment created with identifier : %@"
- "Updated recurring payments after message insertion"
- "_amountEntryViewController"
- "_recipientAddress"
- "_recipientNameErrorTitle"
- "_reportAnalyticsButtonTap:"
- "_reportAnalyticsForState"
- "allowsFormalPaymentRequests"
- "identifyRecipientWithAddress:senderAddress:completion:"
- "informalRequestToken"
- "phoneOrEmail"
- "prewarmDeviceScoreForEndpoint:recipientAddress:quoteDestinationType:"
- "recipientFoundInContacts"
- "setShowSendAndRequest:"
- "setShowSetupRecurringSend:"
- "setViewControllers:animated:"
- "subject:sendEvent:"
- "v16@?0@\"PKPeerPaymentRecurringPayment\"8"
- "viewControllers"

```
