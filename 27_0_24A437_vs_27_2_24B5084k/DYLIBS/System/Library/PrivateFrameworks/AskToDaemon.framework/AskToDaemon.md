## AskToDaemon

> `/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon`

```diff

-96.0.0.0.0
-  __TEXT.__text: 0x83b7c
+97.125.4.0.0
+  __TEXT.__text: 0x86bcc
   __TEXT.__objc_methlist: 0x600
-  __TEXT.__const: 0x3248
-  __TEXT.__swift5_typeref: 0x19e4
-  __TEXT.__swift5_fieldmd: 0xe78
-  __TEXT.__constg_swiftt: 0x11d4
-  __TEXT.__swift5_reflstr: 0x1014
+  __TEXT.__const: 0x33dc
+  __TEXT.__swift5_typeref: 0x1b29
+  __TEXT.__swift5_fieldmd: 0xf1c
+  __TEXT.__constg_swiftt: 0x1284
+  __TEXT.__oslogstring: 0x54f2
   __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_reflstr: 0x10cd
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__cstring: 0x1fc7
-  __TEXT.__swift5_protos: 0x8c
-  __TEXT.__swift5_proto: 0x1b4
-  __TEXT.__swift5_types: 0x114
-  __TEXT.__oslogstring: 0x52e2
-  __TEXT.__swift_as_entry: 0x198
-  __TEXT.__swift_as_cont: 0x414
-  __TEXT.__swift5_capture: 0x75c
+  __TEXT.__swift5_protos: 0x94
+  __TEXT.__swift5_proto: 0x1bc
+  __TEXT.__swift5_types: 0x120
+  __TEXT.__cstring: 0x2099
+  __TEXT.__swift_as_entry: 0x1a8
+  __TEXT.__swift_as_cont: 0x464
+  __TEXT.__swift5_capture: 0x82c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift_as_ret: 0x1f0
-  __TEXT.__unwind_info: 0x1a60
-  __TEXT.__eh_frame: 0x44d8
+  __TEXT.__swift_as_ret: 0x210
+  __TEXT.__unwind_info: 0x1bc0
+  __TEXT.__eh_frame: 0x48dc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x740
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2ad8
-  __AUTH_CONST.__objc_const: 0x1598
-  __AUTH_CONST.__auth_got: 0x12a0
+  __AUTH_CONST.__const: 0x2cf0
+  __AUTH_CONST.__objc_const: 0x15d8
+  __AUTH_CONST.__auth_got: 0x12a8
   __AUTH.__objc_data: 0x278
-  __AUTH.__data: 0xcf8
-  __DATA.__data: 0xf78
+  __AUTH.__data: 0xd98
+  __DATA.__data: 0xfb8
   __DATA.__common: 0x290
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1546
-  Symbols:   1085
-  CStrings:  529
+  Functions: 1616
+  Symbols:   1104
+  CStrings:  540
 
Symbols:
+ ___swift_closure_destructor.130Tm
+ ___swift_closure_destructor.26Tm
+ ___swift_closure_destructor.34Tm
+ ___swift_closure_destructor.42Tm
+ ___swift_closure_destructor.60Tm
+ _flat unique So8NSObject_p
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _symbolic $s11AskToDaemon0aB22BalloonMessageScanningP
+ _symbolic $s11AskToDaemon37LegacyScreenTimeMessagesLookupCapableP
+ _symbolic SS11messageGUID______7payload_____6sourcet 9AskToCore9ATPayloadC 0aB6Daemon23ScreenTimeAnswerHandlerV13MessageSourceO
+ _symbolic SS11messageGUID______7payloadt 9AskToCore9ATPayloadC
+ _symbolic ScCySaySS11messageGUID______10payloadURL_____0C0tG______pG 10Foundation3URLV 9AskToCore9ATPayloadC s5ErrorP
+ _symbolic _____ 11AskToDaemon08IMSPIAskB21BalloonMessageScannerV
+ _symbolic _____ 11AskToDaemon23ScreenTimeAnswerHandlerV13MessageSourceO
+ _symbolic _____ 11AskToDaemon30LegacyScreenTimeMessagesLookupV
+ _symbolic _____ s8DurationV
+ _symbolic _____10payloadURL_t 10Foundation3URLV
+ _symbolic _____SbIeggd_ 9AskToCore9ATPayloadC
+ _symbolic ______p 11AskToDaemon0aB22BalloonMessageScanningP
+ _symbolic ______p 11AskToDaemon37LegacyScreenTimeMessagesLookupCapableP
+ _symbolic ______p So8NSObjectP
+ _symbolic _____ySS11messageGUID______7payload_____6sourcetG s23_ContiguousArrayStorageC 9AskToCore9ATPayloadC 0dE6Daemon23ScreenTimeAnswerHandlerV13MessageSourceO
+ _symbolic _____ySS11messageGUID______7payloadtG s23_ContiguousArrayStorageC 9AskToCore9ATPayloadC
+ _type_layout_string 11AskToDaemon14MessagesLookupV
- ___swift_closure_destructor.16Tm
- ___swift_closure_destructor.38Tm
- ___swift_closure_destructor.56Tm
- ___swift_closure_destructor.65Tm
- _symbolic ScCySaySS11messageGUID______10payloadURL_____0C0tG_____G 10Foundation3URLV 9AskToCore9ATPayloadC s5NeverO
- _symbolic So7NSErrorCSgIeyBy_
- _symbolic ______pSgIegg_ s5ErrorP
CStrings:
+ "%s called with question identifier: %s"
+ "AskTo balloon lookup failed for request ID %s. error: %@"
+ "Every matched message for request ID %s failed to parse"
+ "Failed to get the new Messages payload from the extension. error: %@"
+ "Found %ld matches for request ID %s in the AskTo balloon"
+ "Found %ld matches for request ID %s in the legacy ScreenTime balloon"
+ "Found matching AskTo balloon message with GUID %s"
+ "No legacy ScreenTime balloon match for request ID %s; returning the AskTo balloon match. error: %@"
+ "Notifying clients that message compose finished"
+ "Skipping message GUID %s for request ID %s; failed to parse payload. error: %@"
+ "The data for the messages payload obtained from the extension was nil."
+ "Timed out waiting for messagesComposeDidFinish on client with id %s: %@"
+ "findAllMessages(matchingLegacyRequestID:)"
+ "findAllMessages(matchingQuestionIdentifier:)"
+ "findMessagesInAskToBalloon(matching:)"
+ "init(requestID:responderDSID:answer:messagesLookup:legacyMessagesLookup:)"
+ "parsePayload(from:)"
- "Failed to get the new Messages payload from the People extension. error: %@"
- "Found matching question with ID %s in message GUID %s"
- "Inspecting AskTo message with GUID %s for question ID %s"
- "The data for the messages paylaod obtained from the People extension was nil."
- "findAllMessagesInMessagesDatabase(matching:)"
- "init(requestID:responderDSID:answer:)"
```
