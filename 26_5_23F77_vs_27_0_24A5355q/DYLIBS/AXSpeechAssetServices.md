## AXSpeechAssetServices

> `/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0xee4
-  __TEXT.__auth_stubs: 0x1e0
+3229.1.6.0.0
+  __TEXT.__text: 0xd10
   __TEXT.__objc_methlist: 0x29c
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x158
+  __TEXT.__cstring: 0x15c
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x71
-  __TEXT.__objc_methname: 0x6b4
-  __TEXT.__objc_methtype: 0x282
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x3e8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CEF9DE3A-774F-3AAA-9991-5F592AE78395
-  Functions: 22
+  UUID: B61B67BF-17FC-3F26-A2CF-BCAE21A93690
+  Functions: 21
   Symbols:   163
-  CStrings:  149
+  CStrings:  35
 
Symbols:
+ ___block_literal_global.436
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- -[AXSpeechPronunciationHelper _assetUpdaterClient].cold.1
- ___block_literal_global.416
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x27
Functions:
~ -[AXSpeechPronunciationOptions initWithCoder:] : 216 -> 208
~ -[AXSpeechPronunciationOptions encodeWithCoder:] : 164 -> 156
~ -[AXSpeechPronunciationOptions description] : 152 -> 140
~ -[AXSpeechPronunciationOptions setOrthography:] : 64 -> 12
~ -[AXSpeechPronunciationOptions setLanguage:] : 64 -> 12
~ -[AXSpeechPronunciationHelper dealloc] : 96 -> 92
~ -[AXSpeechPronunciationHelper supportsPronunciationSessions] : 84 -> 80
~ -[AXSpeechPronunciationHelper userInterfaceClient:processMessageFromServer:withIdentifier:error:] : 544 -> 464
~ -[AXSpeechPronunciationHelper audioLevel] : 156 -> 144
~ -[AXSpeechPronunciationHelper startPronunciationSession:resultCallback:] : 1104 -> 1032
~ -[AXSpeechPronunciationHelper stopPronunciationSession] : 432 -> 360
~ -[AXSpeechPronunciationHelper cancelPronunciationSession] : 436 -> 364
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "@?"
- "AXSpeechPronunciationHelper"
- "AXSpeechPronunciationOptions"
- "AXUIClientDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",&,N,V_language"
- "T@\"NSString\",&,N,V_orthography"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_assetUpdaterClient"
- "_inSession"
- "_language"
- "_orthography"
- "_resultCallback"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "autorelease"
- "cancelPronunciationSession"
- "class"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "copy"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictationIsEnabled"
- "dictionaryWithObjects:forKeys:count:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "f16@0:8"
- "floatValue"
- "hash"
- "identifier"
- "ignoreLogging"
- "init"
- "initWithCoder:"
- "initWithIdentifier:serviceBundleName:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "mainAccessQueue"
- "objectForKeyedSubscript:"
- "orthography"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendSynchronousMessage:withIdentifier:error:"
- "setDelegate:"
- "setLanguage:"
- "setOrthography:"
- "sharedInstance"
- "sharedPreferences"
- "startPronunciationSession:resultCallback:"
- "stopPronunciationSession"
- "stringWithFormat:"
- "superclass"
- "supportsPronunciationSessions"
- "supportsSecureCoding"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "zone"

```
