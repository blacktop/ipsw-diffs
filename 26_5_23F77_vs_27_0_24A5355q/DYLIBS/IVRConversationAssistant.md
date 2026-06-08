## IVRConversationAssistant

> `/System/Library/PrivateFrameworks/IVRConversationAssistant.framework/IVRConversationAssistant`

```diff

 2.0.0.0.0
-  __TEXT.__text: 0x1520
-  __TEXT.__auth_stubs: 0x200
+  __TEXT.__text: 0x128c
   __TEXT.__objc_methlist: 0x120
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__cstring: 0xe4
+  __TEXT.__cstring: 0xe8
+  __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__oslogstring: 0x21c
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0x378
-  __TEXT.__objc_methtype: 0x108
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x238
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF49B45E-FAFF-31F4-996B-7EF049BA1E42
+  UUID: 3F7E0F74-5B5A-3C40-84B8-AFC69B3A6CB7
   Functions: 35
-  Symbols:   184
-  CStrings:  89
+  Symbols:   186
+  CStrings:  26
 
Symbols:
+ ___block_literal_global.58
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x20
- ___block_literal_global.59
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[IVROptionStreamData setOptionStreamData:] : 64 -> 12
~ -[IVROptionStream dealloc] : 120 -> 112
~ -[IVROptionStream initializeConnection] : 648 -> 608
~ _IVRCADefaultLog : 84 -> 68
~ ___39-[IVROptionStream initializeConnection]_block_invoke : 96 -> 92
~ ___39-[IVROptionStream initializeConnection]_block_invoke.15 : 72 -> 68
~ -[IVROptionStream startOptionStream] : 460 -> 400
~ ___36-[IVROptionStream startOptionStream]_block_invoke : 192 -> 144
~ -[IVROptionStream getOptionStream:error:] : 1036 -> 1012
~ ___41-[IVROptionStream getOptionStream:error:]_block_invoke.26 : 164 -> 136
~ ___41-[IVROptionStream getOptionStream:error:]_block_invoke_2 : 208 -> 204
~ -[IVROptionStream stopOptionStream] : 460 -> 400
~ ___35-[IVROptionStream stopOptionStream]_block_invoke : 192 -> 144
~ -[IVROptionStream userSelectedDTMFOption:] : 404 -> 340
~ ___42-[IVROptionStream userSelectedDTMFOption:]_block_invoke : 192 -> 144
~ -[IVROptionStream setClientQueue:] : 64 -> 12
~ -[IVROptionStream setServiceConnection:] : 64 -> 12
~ ___41-[IVROptionStream getOptionStream:error:]_block_invoke.cold.1 : 156 -> 108
CStrings:
- ".cxx_destruct"
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@?16^@24"
- "IVRCAXPCClientProtocol"
- "IVRCAXPCServiceProtocol"
- "IVROptionStream"
- "IVROptionStreamData"
- "T@\"NSDictionary\",&,N,V_optionStreamData"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_clientQueue"
- "T@\"NSXPCConnection\",&,N,V_serviceConnection"
- "Tq,N,V_type"
- "_clientQueue"
- "_optionStreamData"
- "_serviceConnection"
- "_type"
- "clientQueue"
- "dealloc"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "getOptionStream:error:"
- "getOptionStreamWithReply:"
- "init"
- "initWithServiceName:"
- "initializeConnection"
- "interfaceWithProtocol:"
- "invalidate"
- "optionStreamData"
- "q"
- "q16@0:8"
- "remoteObjectProxy"
- "resume"
- "serviceConnection"
- "setClientQueue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setOptionStreamData:"
- "setRemoteObjectInterface:"
- "setServiceConnection:"
- "setType:"
- "startOptionStream"
- "startOptionStreamWithReply:"
- "stopOptionStream"
- "stopOptionStreamWithReply:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "type"
- "userSelectedDTMFOption:"
- "userSelectedDTMFOption:withReply:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSString\"@\"NSError\">16"
- "v24@0:8q16"
- "v32@0:8@\"NSNumber\"16@?<v@?B>24"
- "v32@0:8@16@?24"

```
