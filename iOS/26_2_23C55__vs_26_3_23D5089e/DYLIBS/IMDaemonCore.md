## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1450.300.41.2.7
-  __TEXT.__text: 0x31d178
+1450.400.3.2.1
+  __TEXT.__text: 0x31f9c0
   __TEXT.__auth_stubs: 0x55b0
-  __TEXT.__objc_methlist: 0x1924c
+  __TEXT.__objc_methlist: 0x192d4
   __TEXT.__const: 0x68f8
-  __TEXT.__cstring: 0x14b81
-  __TEXT.__gcc_except_tab: 0x2567c
-  __TEXT.__oslogstring: 0x4d317
+  __TEXT.__cstring: 0x14c11
+  __TEXT.__gcc_except_tab: 0x25978
+  __TEXT.__oslogstring: 0x4d4b7
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
   __TEXT.__constg_swiftt: 0x2314
   __TEXT.__swift5_typeref: 0x2c4a
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x12bf
+  __TEXT.__swift5_reflstr: 0x12cf
   __TEXT.__swift5_fieldmd: 0x1580
   __TEXT.__swift5_assocty: 0x688
   __TEXT.__swift5_capture: 0x1240

   __TEXT.__swift_as_ret: 0x370
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xca78
+  __TEXT.__unwind_info: 0xcb10
   __TEXT.__eh_frame: 0x66ec
-  __TEXT.__objc_classname: 0x3560
-  __TEXT.__objc_methname: 0x4d2cf
-  __TEXT.__objc_methtype: 0xa137
-  __TEXT.__objc_stubs: 0x2fd00
-  __DATA_CONST.__got: 0x3198
-  __DATA_CONST.__const: 0x6300
+  __TEXT.__objc_classname: 0x3592
+  __TEXT.__objc_methname: 0x4d759
+  __TEXT.__objc_methtype: 0xa15c
+  __TEXT.__objc_stubs: 0x300e0
+  __DATA_CONST.__got: 0x31c8
+  __DATA_CONST.__const: 0x63f0
   __DATA_CONST.__objc_classlist: 0x958
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x748
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa68
+  __DATA_CONST.__objc_selrefs: 0xfb58
   __DATA_CONST.__objc_protorefs: 0x268
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x158
   __AUTH_CONST.__auth_got: 0x2ae8
   __AUTH_CONST.__const: 0x80e8
-  __AUTH_CONST.__cfstring: 0xdde0
-  __AUTH_CONST.__objc_const: 0x200b8
+  __AUTH_CONST.__cfstring: 0xde60
+  __AUTH_CONST.__objc_const: 0x200d0
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x31a8
   __AUTH.__data: 0x568
   __DATA.__objc_ivar: 0x1174
-  __DATA.__data: 0x59e8
-  __DATA.__bss: 0x5360
+  __DATA.__data: 0x59d8
+  __DATA.__bss: 0x5370
   __DATA.__common: 0x138
   __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0x2450
-  __DATA_DIRTY.__bss: 0x1720
+  __DATA_DIRTY.__data: 0x2400
+  __DATA_DIRTY.__bss: 0x1710
   __DATA_DIRTY.__common: 0x1b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0DF74031-7CA8-3177-96E7-CC6D5BAB707B
-  Functions: 12709
-  Symbols:   2954
-  CStrings:  21237
+  UUID: 0488095D-98CD-3E89-AB28-A84C6E5CB5B0
+  Functions: 12732
+  Symbols:   2960
+  CStrings:  21284
 
Symbols:
+ _IMServiceCapabilityLowQualityImageMode
+ _IMServiceCapabilityRCSChatBot
+ _OBJC_CLASS_$_IMUnifiedMessageMetric
+ _OBJC_CLASS_$_STConversation
+ _OBJC_CLASS_$_UNTextInputNotificationResponse
+ _UTTypeData
CStrings:
+ "Call to handle UNNotificationResponse with actionIdentifier=%@"
+ "IMDNotificationResponseUtilitiesAdditions"
+ "Metrics"
+ "Server Bag has no value for report-junk-mmcs-upload-timeout, using the default 10 seconds"
+ "User quick replied to notification - didRespondWithText:%@ didMarkAsRead :%@ while screentime not allowed for chatIdentifier:%@. returning early."
+ "Using server bag value for report-junk-mmcs-upload-timeout of %ld seconds"
+ "_applyChat:toMetric:"
+ "_applyTransferGUIDs:toMetric:isOutgoing:"
+ "_createJunkMessageDictionaryForItem:senderURI:chat:conversationID:receiverURI:notifyInternalSecurity:reportReason:completionBlock:"
+ "_finishReportMessageDictionariesWithiMessageSpamDictionaries:textMessageSpamDictionaries:trustKitSpamDictionaries:smsServiceReportAllowed:maxMessagesPerReport:chat:totalMessageCount:totalMessages:"
+ "_metricMessageDelivered:chat:serviceSession:"
+ "_processDeliveryReceiptForMessage:date:isFromOffGridCapableDevice:chat:serviceSession:"
+ "_reportReceivedMetricForSMSWithMessage:context:"
+ "_sendMessageResponse:toMessage:inChat:withCompletionHandler:"
+ "_uploadToMMCSForItem:transfer:completionBlock:"
+ "allowableByContactsHandles:"
+ "allowedByScreenTime"
+ "bestGuessTransportType"
+ "bestGuessUnifiedMetricTransportType"
+ "com.apple.iChat"
+ "com.apple.messages.MarkAsReadAction"
+ "com.apple.messages.ReplyAction"
+ "couldn't find chat for %@ to reply"
+ "handleMessagesNotificationResponse:userNotificationCenter:completionHandler:"
+ "initSynchronouslyWithBundleIdentifier:"
+ "initWithIncomingMessage:transportType:serviceType:recipients:receivingHandle:"
+ "initWithOutgoingMessage:transportType:serviceType:recipients:sendingHandle:"
+ "legacyMetricSubmissionsDisabled"
+ "lowQualityStatus"
+ "messageLatency"
+ "messageSize"
+ "report-junk-mmcs-upload-timeout"
+ "serviceTypeForServiceName:"
+ "setChatType:"
+ "setIsChatBot:"
+ "setIsHybridGroup:"
+ "setIsHybridMessage:"
+ "setLowQualityStatus:"
+ "setMessageSize:"
+ "setTotalFileTransferSize:"
+ "setTransferTypes:"
+ "submit"
+ "totalFileTransferSize"
+ "unifiedMetricForIncomingMessage:inChat:transportType:"
+ "unifiedMetricForOutgoingMessage:inChat:transportType:"
+ "userText"
+ "v20@?0B8@\"NSDictionary\"12"
+ "v76@0:8@16@24@32@40@48B56Q60@?68"
+ "v76@0:8@16@24@32B40Q44@52^Q60Q68"
- "@68@0:8@16@24@32@40@48B56Q60"
- "_createJunkMessageDictionaryForItem:senderURI:chat:conversationID:receiverURI:notifyInternalSecurity:reportReason:"
- "_metricMessageGUIDDelivered:sendDate:deliveryDate:"
- "_processDeliveryReceiptForMessage:date:isFromOffGridCapableDevice:chat:"
- "chat:groupIDUpdated:"
- "chat:originalGroupIDUpdated:"

```
