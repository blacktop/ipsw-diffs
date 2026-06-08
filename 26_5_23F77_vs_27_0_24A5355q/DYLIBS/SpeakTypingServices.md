## SpeakTypingServices

> `/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0xf9c
-  __TEXT.__auth_stubs: 0x180
+3229.1.6.0.0
+  __TEXT.__text: 0xebc
   __TEXT.__objc_methlist: 0x29c
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xc8
+  __TEXT.__cstring: 0xca
   __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x7c2
-  __TEXT.__objc_methtype: 0x25f
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x260
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5D7BF19-A708-3606-AB0E-0C84EECD8CC9
-  Functions: 27
-  Symbols:   146
-  CStrings:  128
+  UUID: 1DEE0295-2C1A-3279-9C48-9AD410EB2C07
+  Functions: 26
+  Symbols:   148
+  CStrings:  22
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x24
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- +[SpeakTypingServices sharedInstance].cold.1
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[SpeakTypingServices dealloc] : 96 -> 92
~ -[SpeakTypingServices speakTypingClient] : 72 -> 68
~ -[SpeakTypingServices clearLastSpokenString] : 128 -> 120
~ -[SpeakTypingServices setVoiceIdentifier:forLanguage:] : 232 -> 228
~ -[SpeakTypingServices lastUsedVoiceIdentifier] : 136 -> 124
~ -[SpeakTypingServices lastSpokenString] : 136 -> 124
~ -[SpeakTypingServices verifyTestingConnection] : 132 -> 120
~ -[SpeakTypingServices setWordFeedbackEnabled:] : 256 -> 240
~ -[SpeakTypingServices setPhoneticFeedbackEnabled:] : 256 -> 240
~ -[SpeakTypingServices setLetterFeedbackEnabled:] : 256 -> 240
~ -[SpeakTypingServices notifySpeakServicesToStopSpeaking] : 76 -> 72
~ -[SpeakTypingServices notifySpeakServicesToStopSpeakingAutocorrections] : 76 -> 72
~ -[SpeakTypingServices notifySpeakServicesToInitializeServerConnection] : 40 -> 48
~ -[SpeakTypingServices notifySpeakServicesForAttributedSpeechOutput:] : 252 -> 240
~ -[SpeakTypingServices notifySpeakServicesForSpeechOutput:volume:speakingRate:] : 336 -> 324
~ -[SpeakTypingServices notifySpeakServicesForSpeakAutoCorrections:forCurrentInputMode:] : 264 -> 268
~ -[SpeakTypingServices notifySpeakServicesToFeedbackQuickTypePrediction:forCurrentInputMode:] : 268 -> 264
~ -[SpeakTypingServices _clientIdentifier] : 164 -> 152
~ -[SpeakTypingServices initializeServerConnection] : 176 -> 172
~ ___81-[SpeakTypingServices connectionWithServiceWasInterruptedForUserInterfaceClient:]_block_invoke : 184 -> 176
~ -[SpeakTypingServices setSpeakTypingClient:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXUIClient\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "AXUIClientDelegate"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B40@0:8@16d24d32"
- "NSObject"
- "Q16@0:8"
- "SpeakTypingServices"
- "T#,R"
- "T@\"AXUIClient\",&,N,V_speakTypingClient"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_clientIdentifier"
- "_speakTypingClient"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "autorelease"
- "boolValue"
- "class"
- "clearLastSpokenString"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "hash"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "initializeServerConnection"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastSpokenString"
- "lastUsedVoiceIdentifier"
- "length"
- "notifySpeakServicesForAttributedSpeechOutput:"
- "notifySpeakServicesForSpeakAutoCorrections:forCurrentInputMode:"
- "notifySpeakServicesForSpeechOutput:volume:speakingRate:"
- "notifySpeakServicesToFeedbackQuickTypePrediction:forCurrentInputMode:"
- "notifySpeakServicesToInitializeServerConnection"
- "notifySpeakServicesToStopSpeaking"
- "notifySpeakServicesToStopSpeakingAutocorrections"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "processInfo"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendSynchronousMessage:withIdentifier:error:"
- "setDelegate:"
- "setLetterFeedbackEnabled:"
- "setPhoneticFeedbackEnabled:"
- "setSpeakTypingClient:"
- "setVoiceIdentifier:forLanguage:"
- "setWordFeedbackEnabled:"
- "sharedInstance"
- "speakCorrectionsEnabled"
- "speakTypingClient"
- "stringWithFormat:"
- "superclass"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@16"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "verifyTestingConnection"
- "zone"

```
