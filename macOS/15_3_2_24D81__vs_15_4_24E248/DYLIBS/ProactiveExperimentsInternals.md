## ProactiveExperimentsInternals

> `/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/Versions/A/ProactiveExperimentsInternals`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x233c
+1276.10.4.0.0
+  __TEXT.__text: 0x232c
   __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0xe8
-  __TEXT.__const: 0x90
+  __TEXT.__objc_methlist: 0x234
+  __TEXT.__const: 0x98
+  __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__gcc_except_tab: 0x94
   __TEXT.__cstring: 0x20e
   __TEXT.__oslogstring: 0x394
-  __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x93
   __TEXT.__objc_methname: 0xb5d

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_protorefs: 0x8
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x190
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x6c8
+  __AUTH_CONST.__objc_const: 0x468
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F298BB4F-9CBC-3F57-B0EC-12D448983A1A
+  UUID: 0A91C757-B4BF-39C2-900A-A90B7802A286
   Functions: 39
   Symbols:   229
   CStrings:  171
Symbols:
+ __175+[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:]_block_invoke.11
+ __65-[PREResponsesServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.38
+ __65-[PREResponsesServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.42
+ __block_literal_global.45
+ __block_literal_global.98
- __175+[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:]_block_invoke.5
- __65-[PREResponsesServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.32
- __65-[PREResponsesServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.36
- __block_literal_global.39
- __block_literal_global.92
Functions:
~ -[PREResponsesServerRequestHandler predictForMessage:conversationTurns:language:plistPath:espressoBinPath:vocabPath:heads:completion:] : 904 -> 900
~ +[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:] : 1148 -> 1136

```
