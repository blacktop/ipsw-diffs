## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-  __TEXT.__text: 0xc9020
+  __TEXT.__text: 0xc9208
   __TEXT.__auth_stubs: 0x1d20
   __TEXT.__objc_stubs: 0xd400
   __TEXT.__objc_methlist: 0x29dc
   __TEXT.__const: 0x1040
-  __TEXT.__gcc_except_tab: 0xa1bc
+  __TEXT.__gcc_except_tab: 0xa1f4
   __TEXT.__cstring: 0x33ad
-  __TEXT.__oslogstring: 0x1786b
+  __TEXT.__oslogstring: 0x17c2b
   __TEXT.__objc_classname: 0x68f
-  __TEXT.__objc_methname: 0x129ab
-  __TEXT.__objc_methtype: 0x2c89
+  __TEXT.__objc_methname: 0x12a9b
+  __TEXT.__objc_methtype: 0x2ca9
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x74e
   __TEXT.__constg_swiftt: 0x480

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1738
   Symbols:   905
-  CStrings:  5161
+  CStrings:  5170
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ "   Group found, but failed validation. Dropping incoming group message payload %@. senderFailedValidation %{BOOL}d isPlaceholder %{BOOL}d"
+ "   Group found, but sender was not in the set of participants and was rejected. Dropping incoming group message payload %@."
+ "   No group found. A new group chat will get created with the new "
+ "   No group found. Dropping incoming group message payload %@."
+ "@72@0:8@16@24@32@40@48Q56^Q64"
+ "B68@0:8@16@24@32@40@48B56@60"
+ "Dropping group photo request -- sender is not a member in the chat."
+ "Group Message Payload is from a known sender %@. The payload will continue processing."
+ "Group Message Payload is incoming on an unknown chat. The message type, %@, is not acceptable for an unknown chat and will be dropped."
+ "Group Message Payload is incoming on chat %@, which is a known chat. The payload will continue processing."
+ "Group Message Payload is incoming, but a chat was not found. The message type, %@, is not acceptable for a non-existant chat and will be dropped."
+ "Group Message Payload is of type %@ that is acceptable for both known and unknown senders. The payload will continue processing."
+ "Incoming group message payload from: %@   payload: %@  isReflection: %{BOOL}d  to: %@, timestamp: %@"
+ "_findChatFromIdentifier:toIdentifier:displayName:participants:groupID:validationOptions:outFailedValidations:"
+ "_shouldAcceptGroupMessagePayloadWithFromIdentifier:toIdentifier:displayName:participants:groupID:isKnownSender:type:"
+ "bestCandidateGroupChatWithFromIdentifier:toIdentifier:displayName:participants:updatingToLatestiMessageGroupID:sortedIdentifiers:serviceName:validationOptions:outFailedValidations:"
- "   No group found"
- "B36@0:8@16B24@28"
- "Incoming group message payload from: %@   payload: %@  isReflection: %@  to: %@, timestamp: %@"
- "Received GenericGroupCommand from someone who is not in the group. fromIdentifier: %@ chatGuid: %@"
- "_shouldAcceptGroupMessagePayloadWithExistingChat:isKnownSender:type:"
- "_validateChat:containsFromIdentifier:isReflection:"
- "getNumberOfTimesRespondedToThread"

```
