## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.600.31.0.0
-  __TEXT.__text: 0x91e34
-  __TEXT.__auth_stubs: 0x1330
+1402.600.41.2.6
+  __TEXT.__text: 0x92328
+  __TEXT.__auth_stubs: 0x1340
   __TEXT.__objc_stubs: 0xb280
   __TEXT.__objc_methlist: 0x26ec
-  __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa948
-  __TEXT.__cstring: 0x2d7d
-  __TEXT.__oslogstring: 0x13ed8
+  __TEXT.__const: 0x38e
+  __TEXT.__gcc_except_tab: 0xa9cc
+  __TEXT.__cstring: 0x2ddd
+  __TEXT.__oslogstring: 0x13fe8
   __TEXT.__objc_classname: 0x4e2
-  __TEXT.__objc_methname: 0x1041e
-  __TEXT.__objc_methtype: 0x2779
+  __TEXT.__objc_methname: 0x1042c
+  __TEXT.__objc_methtype: 0x277d
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_typeref: 0x261

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__unwind_info: 0x1da0
   __TEXT.__eh_frame: 0x2c0
-  __DATA_CONST.__auth_got: 0x9a8
+  __DATA_CONST.__auth_got: 0x9b0
   __DATA_CONST.__got: 0xdb8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x2ac8
-  __DATA_CONST.__cfstring: 0x32e0
+  __DATA_CONST.__cfstring: 0x3320
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1179
-  Symbols:   779
-  CStrings:  4161
+  Symbols:   780
+  CStrings:  4166
 
Symbols:
+ _objc_retain_x9
CStrings:
+ "=> Received group photo update from: %@, payload: %@"
+ "About to request group photo for chatGuid %@ from %@ to %@"
+ "Couldn't send new features to these destinations: %@, [%lu] times we're in fallback"
+ "Group photo message parsed: isExplicitlyRequestedResponse: %d, isExplicitResponseThatWeDidNotRequest: %d, isExplicitRefresh: %d, isLegacyRequestedResponse: %d, isExplicitlyNewPhoto: %d, isAssumedLegacyNewPhoto: %d"
+ "MessageDeliveryControllerTooManyFallbacks"
+ "Removing %@ from inflight photo requests list."
+ "Repeatedly trying to send fallback message"
+ "We received a local message from a device that is not our own."
+ "_sendMessage:context:deliveryContext:fromID:fromAccount:toID:chatIdentifier:toSessionToken:toGroup:toParticipants:originallyToParticipants:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:canInlineAttachments:type:msgPayloadUploadDictionary:originalPayload:replyToMessageGUID:fallbackCount:willSendBlock:completionBlock:"
+ "v188@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120B128q132@140@148@156Q164@?172@?180"
- "Couldn't send new features to these destinations: %@"
- "Group photo message parsed: isExplicitlyRequestedResponse: %d, isLegacyRequestedResponse: %d, isExplicitlyNewPhoto: %d, isAssumedLegacyNewPhoto: %d"
- "Requesting group photo for chatGuid %@ from %@ to %@"
- "_sendMessage:context:deliveryContext:fromID:fromAccount:toID:chatIdentifier:toSessionToken:toGroup:toParticipants:originallyToParticipants:requiredRegProperties:interestingRegProperties:requiresLackOfRegProperties:canInlineAttachments:type:msgPayloadUploadDictionary:originalPayload:replyToMessageGUID:willSendBlock:completionBlock:"
- "v180@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120B128q132@140@148@156@?164@?172"

```
