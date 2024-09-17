## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1402.200.35.0.0
-  __TEXT.__text: 0xe1fa4
-  __TEXT.__auth_stubs: 0x1a40
+1402.200.57.0.0
+  __TEXT.__text: 0xea18c
+  __TEXT.__auth_stubs: 0x1ab0
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x428
-  __TEXT.__const: 0x3d70
+  __TEXT.__objc_methlist: 0x454
+  __TEXT.__const: 0x3e90
   __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x3f73
+  __TEXT.__objc_methname: 0x408f
   __TEXT.__objc_methtype: 0xd75
-  __TEXT.__cstring: 0x2f85
-  __TEXT.__constg_swiftt: 0x1ac8
-  __TEXT.__swift5_typeref: 0x1add
-  __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0xe13
+  __TEXT.__cstring: 0x3095
+  __TEXT.__constg_swiftt: 0x1b90
+  __TEXT.__swift5_typeref: 0x1bdf
+  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__swift5_reflstr: 0xeb2
   __TEXT.__swift5_assocty: 0x278
-  __TEXT.__oslogstring: 0x456a
-  __TEXT.__swift5_proto: 0x308
-  __TEXT.__swift5_types: 0x174
-  __TEXT.__swift5_capture: 0x868
-  __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__swift5_fieldmd: 0x1348
+  __TEXT.__oslogstring: 0x483a
+  __TEXT.__swift5_proto: 0x318
+  __TEXT.__swift5_types: 0x180
+  __TEXT.__swift5_capture: 0x900
+  __TEXT.__swift5_mpenum: 0xbc
+  __TEXT.__swift5_fieldmd: 0x13fc
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x3010
-  __TEXT.__eh_frame: 0x78e8
-  __DATA_CONST.__auth_got: 0xd28
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__auth_ptr: 0x518
-  __DATA_CONST.__const: 0x4868
-  __DATA_CONST.__objc_classlist: 0x80
+  __TEXT.__unwind_info: 0x3258
+  __TEXT.__eh_frame: 0x8018
+  __DATA_CONST.__auth_got: 0xd60
+  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__auth_ptr: 0x540
+  __DATA_CONST.__const: 0x4a98
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x1cf8
-  __DATA.__objc_selrefs: 0x1120
-  __DATA.__objc_data: 0x318
-  __DATA.__data: 0x34a0
-  __DATA.__bss: 0x4e00
-  __DATA.__common: 0xa8
+  __DATA.__objc_const: 0x2500
+  __DATA.__objc_selrefs: 0x1160
+  __DATA.__objc_data: 0x408
+  __DATA.__data: 0x3698
+  __DATA.__bss: 0x5000
+  __DATA.__common: 0xb8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3248
-  Symbols:   366
-  CStrings:  1280
+  Functions: 3398
+  Symbols:   376
+  CStrings:  1308
 
Symbols:
+ _swift_dynamicCastObjCClass
+ _IMBalloonBundleIdentifierChatBot
+ __swiftEmptySetSingleton
+ _IMChatBotBusinessName
+ _OBJC_CLASS_$_CTLazuliChatBotOrgNameEntry
+ _dispatch_group_enter
+ _OBJC_CLASS_$__TtC3RCS28RCSOutgoingMessageController
+ _dispatch_group_leave
+ _dispatch_group_create
+ _OBJC_METACLASS_$__TtC3RCS28RCSOutgoingMessageController
CStrings:
+ "Failed to re-create group, failing message %!s(MISSING) due to error %!@(MISSING)"
+ "Dropping disposition notification for %!s(MISSING) as it is from an unexpected sender %!s(MISSING) - would allow from %!s(MISSING)"
+ "RCSTreatDeliveredAsInterworked"
+ "Can't report spam %!s(MISSING) with empty chatIdentifier"
+ "Can't report spam %!s(MISSING) with empty destination URI"
+ "Failed to send %!s(MISSING) via CT: %!@(MISSING)"
+ "Assigning GUID %!s(MISSING) to RCS message %!s(MISSING) as the network ID was a valid, unique UUID"
+ "notifyDidSendMessageID:account:shouldNotify:wasDowngraded:wasInterworked:"
+ "orgName"
+ "didReportSpam:forDestination:withResult:"
+ "RCS service downgraded"
+ "RCSForceRecreationRequired"
+ "orgDetails"
+ "CTLazuliSpamReportInformation is not defined. Can't report lazuli spam"
+ "Not sending group message, we are not a member anymore"
+ "Assigning a random GUID %!s(MISSING) to RCS message %!s(MISSING) due to non-UUID network ID"
+ "RCSTreatInterworkedAsDelivered"
+ "Assigning a random GUID %!s(MISSING) to RCS message %!s(MISSING) due to database collision"
+ "extractRawMessageID"
+ "RCS.RCSOutgoingMessageController"
+ "conversationWasDowngraded"
+ "pcc"
+ "%!s(MISSING) unreachable because destination is offline and this is not a group"
+ "didFinishGroupUpdate:forGroupChat:"
+ "com.apple.Messages.RCSMessageProcessingQueue"
+ "Re-send after group creation failed, failing message %!s(MISSING) due to error %!@(MISSING)"
+ "No CTXPCContext found to report spam %!s(MISSING) error %!s(MISSING)"
+ "Populate business name %!s(MISSING) for chat: %!s(MISSING)"
+ "availibility"
+ "copyCarrierBundleValueForSubscriptionContext:keyHierarchy:defaultValue:valueIfError:"
+ "didReportSpam(_:for:with:)"
+ "sendLazuliSpamReport:isBot:spamType:"
+ "networkSupportsInterworkingForContext:"
+ "%!s(MISSING) reachable because is bot and supports chat"
+ "%!{(MISSING)public}s simID: %!s(MISSING) forDestination: %!@(MISSING) operationResult: %!@(MISSING)"
+ "Group recreation requested, recreating group"
+ "Can't resolve a chat to report spam %!s(MISSING)"
+ "Failed to parse person centric ID into RCSHandle, likely not a chatbot: %!s(MISSING)"
+ "waitingQueue"
+ "MismatchedMessageIDCasing"
+ "%!s(MISSING) reachable because supports text and transfer"
+ "botInfo"
+ "outgoingMessageController"
+ "messageSent:onService:compatibilityService:wasInterworked:"
+ "_TtC3RCS28RCSOutgoingMessageController"
+ "%!s(MISSING) unreachable beacuse doesn't support chat"
+ "setBalloonBundleID:"
+ "v36@0:8@16B24Q28"
+ "RCSForceEvictedFromGroup"
+ "We were evicted from the group, failing message send and updating chat join state"
- "RCSDeliveryImpliesSendSuccess"
- "accountID"
- "Mirroring failed message send to group operation controller due to defaults"
- "RCSForceSendSuccess"
- "chatCapabilities"
- "RCS chat capabilities (%!@(MISSING)) has a valid revoke timer :%!@(MISSING). Network doesn't support interworking"
- "Dropping disposition notification as it is from an unexpected sender"
- "RCS chat capabilities (%!@(MISSING)) has no valid revoke timer. Network supports interworking"
- "v32@0:8@16Q24"
- "Can't resolve a chat to report chatbot spam %!s(MISSING)"
- "Failed to hand %!s(MISSING) off to CT: %!@(MISSING)"
- "Dropping disposition notification due to unknown message UUID"
- "No CTXPCContext found to report chatbot spam %!s(MISSING) error %!s(MISSING)"
- "revokeTimer"
- "setAccountID:"
- "notifyDidSendMessageID:account:shouldNotify:"
- "sendChatbotSpamReport:spamType:"
- "Can't report chatbot spam %!s(MISSING) with empty chatIdentifier"
- "storeMessage:forceReplace:modifyError:modifyFlags:flagMask:"
- "Inferring send success due to disposition notification"
- "RCSMirrorFailedMessageSendsToOperationController"
- "Can't report chatbot spam %!s(MISSING) with empty chatbot URI"
- "setService:"

```
