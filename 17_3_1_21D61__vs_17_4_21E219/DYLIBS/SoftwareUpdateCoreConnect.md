## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

```diff

-1856.80.3.0.1
-  __TEXT.__text: 0xa90c
+1856.100.79.0.3
+  __TEXT.__text: 0xae98
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x69c
+  __TEXT.__objc_methlist: 0x6b4
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__cstring: 0xaab
-  __TEXT.__oslogstring: 0x2278
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__cstring: 0xaf7
+  __TEXT.__oslogstring: 0x236f
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0x197
-  __TEXT.__objc_methname: 0x1896
-  __TEXT.__objc_methtype: 0x4de
-  __TEXT.__objc_stubs: 0x10a0
+  __TEXT.__objc_methname: 0x1986
+  __TEXT.__objc_methtype: 0x50d
+  __TEXT.__objc_stubs: 0x1140
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10d8
-  __DATA_CONST.__objc_selrefs: 0x530
-  __AUTH_CONST.__cfstring: 0x880
+  __DATA_CONST.__objc_const: 0x1108
+  __DATA_CONST.__objc_selrefs: 0x560
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__auth_got: 0x210
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xe0
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_ivar: 0xac
   __DATA.__data: 0x360
   __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__objc_const: 0x3f0

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F08ED65C-348C-3AA1-A57A-51E7B365586F
-  Functions: 224
-  Symbols:   881
-  CStrings:  578
+  UUID: 155473B9-C590-3A23-9E8F-B7D7FDEAAFB8
+  Functions: 232
+  Symbols:   903
+  CStrings:  594
 
Symbols:
+ -[SUCoreConnectMessage clientConnectionAuditToken]
+ -[SUCoreConnectMessage setClientConnectionAuditToken:]
+ -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.5
+ -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.6
+ -[SUCoreConnectServer listener:shouldAcceptNewConnection:].cold.1
+ -[SUCoreConnectServer listener:shouldAcceptNewConnection:].cold.2
+ _OBJC_IVAR_$_SUCoreConnectMessage._clientConnectionAuditToken
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.115
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.116
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.117
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.117.cold.1
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.15
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.88
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.89
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.86
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.86.cold.1
+ ___62-[SUCoreConnectClient _internalConnectToServerWithCompletion:]_block_invoke.91
+ ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke.128
+ ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.114
+ ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.109.cold.1
+ ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.109.cold.2
+ ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.110
+ ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.115
+ ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.118
+ ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.121
+ _objc_msgSend$auditToken
+ _objc_msgSend$checkedDescription
+ _objc_msgSend$isConnection:authorizedForMessage:
+ _objc_msgSend$isConnectionAuthorized:
+ _objc_msgSend$setClientConnectionAuditToken:
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.107
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.108
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.109
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.109.cold.1
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.11
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.82
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.86
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.83
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.83.cold.1
- ___62-[SUCoreConnectClient _internalConnectToServerWithCompletion:]_block_invoke.89
- ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke.127
- ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.106
- ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.108
- ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.108.cold.1
- ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.108.cold.2
- ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.113
- ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.116
- ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.120
CStrings:
+ "T@\"NSString\",?,R,C"
+ "T{?=[8I]},N,V_clientConnectionAuditToken"
+ "[ListenerNewConnection](%{public}@) Rejecting connection - client is not entitled correctly per server delegate"
+ "[SendServerMessage](%@) client is not entitled for specific message request"
+ "[SendServerMessage](%{public}@) Calling completion block with error:%{public}@"
+ "[SendServerMessage](%{public}@) connectProtocolFromClientSendServerMessage using isConnection:authorizedForMessage: via server delegate"
+ "_clientConnectionAuditToken"
+ "auditToken"
+ "checkedDescription"
+ "clientConnectionAuditToken"
+ "isConnection:authorizedForMessage:"
+ "isConnectionAuthorized:"
+ "setClientConnectionAuditToken:"
+ "v48@0:8{?=[8I]}16"
+ "{?=\"val\"[8I]}"
+ "{?=[8I]}16@0:8"
- "[SendServerMessage](%{public}@) Calling completion block with error: %{public}@"

```
