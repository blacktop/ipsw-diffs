## ProactiveExperimentsInternals

> `/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals`

```diff

-1303.10.0.0.0
-  __TEXT.__text: 0x1fe0
-  __TEXT.__auth_stubs: 0x3d0
+1311.4.1.0.0
+  __TEXT.__text: 0x2084
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x234
-  __TEXT.__const: 0x88
+  __TEXT.__const: 0x90
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__cstring: 0x1af
   __TEXT.__oslogstring: 0x394
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xe8
   __TEXT.__objc_classname: 0x93
   __TEXT.__objc_methname: 0xb5d
   __TEXT.__objc_methtype: 0x379

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x468

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA8C8727-BF47-319E-A1C1-5A3934C5F8D1
+  UUID: 5CD47B55-E59F-333F-8248-72281504E12A
   Functions: 32
-  Symbols:   275
+  Symbols:   272
   CStrings:  170
 
Symbols:
+ _objc_autorelease
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x8
Functions:
~ -[PREResponsesServerRequestHandler setBundleIdResolver:] : 12 -> 64
~ -[PREResponsesServerRequestHandler registerResponse:position:isCanned:isUsingQuickResponses:locale:modelConfigPath:vocabPath:] : 256 -> 240
~ -[PREResponsesServerRequestHandler preResponseItemArrayFromQuickResponses:] : 964 -> 1016
~ -[PREResponsesServerRequestHandler predictForMessage:conversationTurns:language:plistPath:espressoBinPath:vocabPath:heads:completion:] : 824 -> 836
~ ___getSGMultiHeadInferenceClass_block_invoke : 492 -> 508
~ ___134-[PREResponsesServerRequestHandler predictForMessage:conversationTurns:language:plistPath:espressoBinPath:vocabPath:heads:completion:]_block_invoke : 148 -> 156
~ -[PREResponsesServerRequestHandler preResponseItemsForMessage:maximumResponses:conversationTurns:context:time:language:recipientHandles:modelFilePath:modelConfigPath:espressoBinFilePath:vocabFilePath:registerDisplayed:includeCustomResponses:includeResponsesToRobots:completion:] : 632 -> 608
~ -[PREResponsesServerRequestHandler setRemoteObjectProxy:] : 12 -> 64
~ -[PREResponsesServerDelegate listener:shouldAcceptNewConnection:] : 828 -> 824
~ _procNameForPid : 208 -> 204
~ +[PREXPCServerHelper hasTrueBooleanEntitlement:connection:] : 96 -> 100
~ +[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:] : 1056 -> 1028
~ ___175+[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:]_block_invoke : 260 -> 264
~ ___175+[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:]_block_invoke.11 : 260 -> 264
~ _pre_sv_xpc_handle : 84 -> 100
~ _pre_sv_responses_handle : 84 -> 100
~ +[PREXPCServer _registerResponsesListener] : 192 -> 196

```
