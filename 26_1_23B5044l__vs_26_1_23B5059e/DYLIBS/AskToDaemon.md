## AskToDaemon

> `/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon`

```diff

-67.125.1.1.0
-  __TEXT.__text: 0x60118
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_methlist: 0x558
-  __TEXT.__const: 0x2698
-  __TEXT.__cstring: 0x2bca
-  __TEXT.__swift5_typeref: 0x147d
-  __TEXT.__swift5_capture: 0x4a0
-  __TEXT.__constg_swiftt: 0xf40
-  __TEXT.__swift5_fieldmd: 0xc50
+67.125.4.0.0
+  __TEXT.__text: 0x65f60
+  __TEXT.__auth_stubs: 0x1f50
+  __TEXT.__objc_methlist: 0x588
+  __TEXT.__const: 0x2758
+  __TEXT.__cstring: 0x2dfa
+  __TEXT.__swift5_typeref: 0x15d3
+  __TEXT.__swift5_capture: 0x524
+  __TEXT.__constg_swiftt: 0xf60
+  __TEXT.__swift5_fieldmd: 0xc84
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xdf7
+  __TEXT.__swift5_reflstr: 0xe57
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_proto: 0x188
+  __TEXT.__swift5_proto: 0x18c
   __TEXT.__swift5_types: 0xec
-  __TEXT.__swift_as_entry: 0x108
-  __TEXT.__swift_as_ret: 0x158
-  __TEXT.__oslogstring: 0x4782
-  __TEXT.__swift5_protos: 0x64
+  __TEXT.__swift_as_entry: 0x124
+  __TEXT.__swift_as_ret: 0x180
+  __TEXT.__oslogstring: 0x4d02
+  __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x11f8
-  __TEXT.__eh_frame: 0x2eb8
+  __TEXT.__unwind_info: 0x1340
+  __TEXT.__eh_frame: 0x345c
   __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x1759
+  __TEXT.__objc_methname: 0x17b4
   __TEXT.__objc_methtype: 0x936
-  __DATA_CONST.__got: 0x680
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x6c8
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0xf90
-  __AUTH_CONST.__const: 0x1ff8
-  __AUTH_CONST.__objc_const: 0x14f0
+  __AUTH_CONST.__auth_got: 0xfa8
+  __AUTH_CONST.__const: 0x2110
+  __AUTH_CONST.__objc_const: 0x1520
   __AUTH.__objc_data: 0x278
-  __AUTH.__data: 0xd90
-  __DATA.__data: 0xe30
-  __DATA.__bss: 0x2500
+  __AUTH.__data: 0xda0
+  __DATA.__data: 0xec8
+  __DATA.__bss: 0x2580
   __DATA.__common: 0x218
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D1DF354-4A87-389F-9D1F-D977344917BE
-  Functions: 1291
-  Symbols:   1061
-  CStrings:  866
+  UUID: E872A4A9-D9E9-351A-84B9-6F4BFB942F9D
+  Functions: 1357
+  Symbols:   1080
+  CStrings:  900
 
Symbols:
+ __PROTOCOLS__TtC11AskToDaemon6Server.3
+ _associated conformance 11AskToDaemon0C5ErrorO10Foundation09LocalizedD0AAs0D0
+ _block_copy_helper.108
+ _block_copy_helper.162
+ _block_copy_helper.75
+ _block_descriptor.110
+ _block_descriptor.164
+ _block_descriptor.77
+ _block_destroy_helper.109
+ _block_destroy_helper.163
+ _block_destroy_helper.76
+ _objectdestroy.34Tm
+ _objectdestroy.83Tm
+ _swift_bridgeObjectRelease_n
+ _symbolic $s11AskToDaemon22MessagesLookupProtocolP
+ _symbolic SS11messageGUID______10payloadURL_____0C0t 10Foundation3URLV 9AskToCore9ATPayloadC
+ _symbolic SS___________t 10Foundation3URLV 9AskToCore9ATPayloadC
+ _symbolic SaySS11messageGUID______10payloadURL_____0C0tG 10Foundation3URLV 9AskToCore9ATPayloadC
+ _symbolic SaySS___________tG 10Foundation3URLV 9AskToCore9ATPayloadC
+ _symbolic SaySS___________tGz_Xx 10Foundation3URLV 9AskToCore9ATPayloadC
+ _symbolic ScCySaySS11messageGUID______10payloadURL_____0C0tG_____G 10Foundation3URLV 9AskToCore9ATPayloadC s5NeverO
+ _symbolic ______pSg 11AskToDaemon22MessagesLookupProtocolP
+ _symbolic _____ySS11messageGUID______10payloadURL_____0C0tG s23_ContiguousArrayStorageC 10Foundation3URLV 9AskToCore9ATPayloadC
+ _symbolic _____ySS___________tG s23_ContiguousArrayStorageC 10Foundation3URLV 9AskToCore9ATPayloadC
- __PROTOCOLS__TtC11AskToDaemon6Server.2
- _block_copy_helper.121
- _block_copy_helper.68
- _block_descriptor.123
- _block_descriptor.70
- _block_destroy_helper.122
- _block_destroy_helper.69
CStrings:
+ "%s Client is missing required entitlement \"com.apple.asktod.updateMessageBubble\""
+ "%s called with question ID: %s"
+ "%s called with question ID: %s, responderHandle: %s, answerChoice: %s"
+ "%s returning isPending: %{bool}d for question ID: %s"
+ "%s successfully updated %ld message bubbles for question ID: %s"
+ "AskTo messages extension bundle identifier was nil"
+ "Client is missing required entitlement"
+ "Could not parse ATPayload for message with GUID %s"
+ "Failed to get the new Messages payload from the AskTo extension. error: %@"
+ "Failed to inflate recipient group for IDS sync: %@. Skipping IDS sync."
+ "Found matching question with ID %s in message GUID %s"
+ "Got nil messageGUID or payloadURL from IMSPI"
+ "Inspecting AskTo message with GUID %s for question ID %s"
+ "Messages balloon bundle identifier not available"
+ "No conversation participants found. Skipping IDS sync."
+ "No valid IDS destinations found from conversation participants. Skipping IDS sync."
+ "Question %s %s"
+ "Question %s not found in Messages database"
+ "Question not found in Messages database"
+ "Sent IDS message for cross-device bubble update sync to %ld destinations"
+ "Skipping IDS sync for ScreenTime request"
+ "The data for the messages payload obtained from the AskTo extension was nil."
+ "Updating message bubble with GUID %s with response: %@"
+ "_findAllMessagesForQuestion(_:)"
+ "_isQuestionPendingInMessages(_:)"
+ "_updateMessageBubble(_:responderHandle:answerChoice:)"
+ "dictionaryRepresentation was nil for payload or could not parse recipient group. Skipping IDS sync"
+ "has no response - still pending"
+ "has response - not pending"
+ "isQuestionPendingInMessages:reply:"
+ "messagesLookup"
+ "updateMessageBubble:responderHandle:answerChoice:reply:"
+ "v32@0:8@\"_TtC5AskTo10ATQuestion\"16@?<v@?B@\"NSError\">24"
+ "v48@0:8@\"_TtC5AskTo10ATQuestion\"16@\"NSString\"24@\"_TtC5AskTo14ATAnswerChoice\"32@?<v@?@\"NSError\">40"

```
