## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1402.200.35.0.0
-  __TEXT.__text: 0x1ba358
-  __TEXT.__auth_stubs: 0x2610
+1402.200.57.0.0
+  __TEXT.__text: 0x1bb524
+  __TEXT.__auth_stubs: 0x2600
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x13048
+  __TEXT.__objc_methlist: 0x13120
   __TEXT.__const: 0x17e0
-  __TEXT.__gcc_except_tab: 0x15de0
-  __TEXT.__cstring: 0x101f7
-  __TEXT.__oslogstring: 0x1de99
+  __TEXT.__gcc_except_tab: 0x15dec
+  __TEXT.__cstring: 0x10547
+  __TEXT.__oslogstring: 0x1de49
+  __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
-  __TEXT.__ustring: 0x18
   __TEXT.__constg_swiftt: 0x548
   __TEXT.__swift5_typeref: 0x9f3
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x6c
   __TEXT.__swift5_capture: 0x4ac
-  __TEXT.__unwind_info: 0x7c78
+  __TEXT.__unwind_info: 0x7cb8
   __TEXT.__eh_frame: 0x8c8
-  __TEXT.__objc_classname: 0x24bc
-  __TEXT.__objc_methname: 0x3c378
-  __TEXT.__objc_methtype: 0x6454
-  __TEXT.__objc_stubs: 0x23e80
-  __DATA_CONST.__got: 0x1e28
-  __DATA_CONST.__const: 0x4f88
+  __TEXT.__objc_classname: 0x24c5
+  __TEXT.__objc_methname: 0x3c738
+  __TEXT.__objc_methtype: 0x647c
+  __TEXT.__objc_stubs: 0x24160
+  __DATA_CONST.__got: 0x1e58
+  __DATA_CONST.__const: 0x4fc8
   __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc6c8
+  __DATA_CONST.__objc_selrefs: 0xc780
   __DATA_CONST.__objc_protorefs: 0x190
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x1328
+  __AUTH_CONST.__auth_got: 0x1320
   __AUTH_CONST.__auth_ptr: 0x320
-  __AUTH_CONST.__const: 0x4160
-  __AUTH_CONST.__cfstring: 0xb8c0
-  __AUTH_CONST.__objc_const: 0x20bd0
+  __AUTH_CONST.__const: 0x4180
+  __AUTH_CONST.__cfstring: 0xbc00
+  __AUTH_CONST.__objc_const: 0x20ca0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x28a0
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x10fc
-  __DATA.__data: 0x28c8
+  __DATA.__objc_ivar: 0x1108
+  __DATA.__data: 0x28d8
   __DATA.__bss: 0x2d68
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x2340

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8793
-  Symbols:   2300
-  CStrings:  14193
+  Functions: 8817
+  Symbols:   2308
+  CStrings:  14250
 
Symbols:
+ _IMChatInterworkingStateChangedNotification
+ _kCTStewieOffer
+ _IMNumberOfAttemptsToShowOTGBannerKey
+ _IMMinimumTimeBeforeShowingOTGBannerKey
+ _IMTimesShownOTGBannerKey
+ _IMIgnoreTimerLimit
+ _IMReasonDidBeginTyping
+ _IMServiceCapabilityKeptReceipts
+ _IMSPIRetrieveLocalizedServiceStringByServiceName
+ _IMServiceCapabilityNetworkFallback
+ _kCTStewieOfferReason
+ _IMServiceCapabilityGroupServer
- _IMServiceDefaultsHandlesWithNetworkFallback
- _IMChorosMonitorStartedNotification
- _IMMessageSummaryInfoOriginalServiceName
- _IMSharedHelperRetrieveSimDetailsFromTelephony
CStrings:
+ "_lastPendingSatelliteSendMessage"
+ "_uncachedInterworkingState"
+ "_sentMessagesSinceInterworking"
+ "originalServiceName"
+ "_isSentMessage:"
+ "reportLazuliSpam:isBot:"
+ "TEXT_MESSAGE_RCS"
+ "ignoreTimerLimit"
+ "5G_MESSAGING"
+ "__kIMChatInterworkingStateChangedNotification"
+ "Not showing satellite connection banner. Only showing banner on after %!l(MISSING)d attempts. Number of attempts: %!l(MISSING)d"
+ "MADRID"
+ "IMChorosMonitor+Request"
+ "Found RCS account, reporting spam, isBot: %!d(MISSING)"
+ "wasInterworked"
+ "_interworkingState"
+ "interworking"
+ "Request"
+ "RCSGroupURI"
+ "\x02G\x12\x16\x112=!!\x122\x13\")"
+ "how-often-to-show-OTG-banner"
+ "_lastInterworkedMessage"
+ "relayMessageGUIDSent:onService:interworked:"
+ "DidBeginTyping"
+ "limit-to-start-showing-OTG-banner"
+ "Chat %!@(MISSING) is ending holds on updates for reason: %!{(MISSING)public}@"
+ "_recalculateIsInterworking"
+ "setInterworkingService:"
+ "Not showing satellite connection banner. Only showing banner on every %!l(MISSING)d attempt. number of times attempted: %!l(MISSING)d"
+ "service_id"
+ "messagesAppDomain"
+ "v44@0:8@16B24Q28@36"
+ "setInterworkingState:"
+ "setAssociatedMessageEffect:"
+ "v44@0:8@\"IMMessageItem\"16B24Q28@\"NSString\"36"
+ "AppOpen"
+ "--> Chat %!@(MISSING) has %!{(MISSING)public}ld remaining holds: %!@(MISSING)"
+ "when-to-first-show-OTG-banner"
+ "TB,R,N,GisSatelliteMessagingCompatible"
+ "@36@0:8Q16@24B32"
+ "_canLeaveChatIgnoringParticipantCount:"
+ "_itemsAreRelayItemsFromMeWithServiceSwitch:otherItem:"
+ "loadUnreadMessagesWithLimit:fallbackToMessagesUpToGUID:loadImmediately:"
+ "Not showing satellite connection banner. Limit has been reached. Limit: %!l(MISSING)d, number of times shown: %!l(MISSING)d"
+ "TEXT_MESSAGE"
+ "lastPendingSatelliteSendMessage"
+ "Text Message"
+ "PLACEHOLDER_TEXT_VIEW_SATELLITE_MESSAGE_SMS"
+ "endAllHoldsOnUpdatesForReason:updateTriggeredIfNotHeldShouldBeDeferred:"
+ "endAllHoldsOnChatItemsUpdatesForReason:"
+ "isOlderThanItem:"
+ "TB,R,N,GisInterworking"
+ "Tq,N,V_interworkingState"
+ "isInterworking"
+ "No RCS Account found while reporting spam. Chat Items -> %!@(MISSING)"
+ "when-to-stop-showing-OTG-banner"
+ "satelliteMessagingCompatible"
+ "presentSatelliteConnectionBannerIfNecessaryWithChat:withReason:ignoreTimerLimit:"
+ "sendLazuliSpamReport:isBot:spamType:account:"
+ "PLACEHOLDER_TEXT_VIEW_SATELLITE_MESSAGE"
+ "interworkingState"
+ "supportsNetworkFallback"
+ "No chat item of type IMMessageItem found while reporting spam. Chat Items -> %!@(MISSING)"
+ "_interworkingService"
+ "TEXT_MESSAGE_SMS"
+ "Presenting satellite connection banner"
+ "Request Satellite error: %!@(MISSING)"
+ "T@\"NSString\",&,N,V_interworkingService"
+ "TQ,R,N,V_index"
+ "interworkingService"
+ "isSatelliteMessagingCompatible"
+ "Not showing satellite connection banner as it's been less than %!l(MISSING)d minutes since we are without connection"
- "service-id"
- "_handlesSupportingNetworkFallback"
- "handleSupportsNetworkFallback:"
- "No chat item of type IMMessageItem found while reporting chatbot spam. Chat Items -> %!@(MISSING)"
- "\x02G\x12\x16B=!\x11\x122\x13\")"
- "No RCS Account found while reporting chatbot spam. Chat Items -> %!@(MISSING)"
- "suppressAccountRetargetingForNamedGroupConversation"
- "IMChorosMonitorStartedNotification"
- "--> Chat %!{(MISSING)public}@ has %!{(MISSING)public}ld remaining holds: %!@(MISSING)"
- "v40@0:8@\"IMMessageItem\"16Q24@\"NSString\"32"
- "reportChatbotSpam:"
- "This was iMessage group, don't downgrade: %!@(MISSING)"
- "(-refreshServiceForSending) bailing, don't downgrade named iMessage group chat: %!@(MISSING)"
- "Found RCS account, reporting chatbot spam"
- "sendChatbotSpamReport:spamType:account:"

```
