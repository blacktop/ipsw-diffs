## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0xbc98
+2422.0.15.0.2
+  __TEXT.__text: 0xb0a8
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x9c8
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x3f8
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x36c
   __TEXT.__cstring: 0xb6b
-  __TEXT.__oslogstring: 0x260d
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__oslogstring: 0x1e56
+  __TEXT.__unwind_info: 0x328
   __TEXT.__objc_classname: 0x1ac
   __TEXT.__objc_methname: 0x1b8b
   __TEXT.__objc_methtype: 0x5b3
   __TEXT.__objc_stubs: 0x12a0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DAF9429F-9F6A-37D5-A453-CE2F1F10449F
-  Functions: 254
-  Symbols:   999
-  CStrings:  635
+  UUID: B263D711-EC42-3F4E-9FF7-D0FE0507AC0F
+  Functions: 259
+  Symbols:   1006
+  CStrings:  612
 
Symbols:
+ -[SUCoreConnectServer _removeConnection:].cold.1
+ -[SUCoreConnectServer isConnectionEntitled:].cold.3
+ -[SUCoreConnectServer isConnectionEntitled:].cold.4
+ -[SUCoreConnectServer isConnectionEntitled:].cold.5
+ _OUTLINED_FUNCTION_9
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.115
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.117
+ ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.117.cold.1
+ ___55-[SUCoreConnectServer setupListenerAndResumeConnection]_block_invoke.90
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.87
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.85
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.88
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_3
+ ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_3.cold.1
+ ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.114
- -[SUCoreConnectServer _clientIDForConnection:].cold.1
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.117
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.118
- ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.118.cold.1
- ___55-[SUCoreConnectServer setupListenerAndResumeConnection]_block_invoke.91
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.85
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.88
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.89
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.86
- ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.86.cold.1
- ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.115
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
CStrings:
+ "[SendServerMessage](%{public}@) connectProtocolFromClientSendServerMessage calling completion block with error:%{public}@"
+ "[SendServerMessage](%{public}@) connectProtocolFromClientSendServerMessage calling completion block, response:%{public}@ error:%{public}@"
- "[ClientIDForConnection] Located clientID: %{public}@, for connection: %{public}@"
- "[ClientIDForConnection] No clientID located for connection: %{public}@"
- "[ConnectToServer](%{public}@) Already connected to server, not reconnecting for client that usesPersistentXPCConnections for connection %{public}@"
- "[ConnectToServer](%{public}@) Attempting to connect to server"
- "[ConnectToServer](%{public}@) Successfully connected to server with connection %{public}@"
- "[ConnectionForClientID] From %lu clientIDs, %lu connections located for clientID: %{public}@, connections: %{public}@"
- "[GetAllObserverConnections] Returning %lu observable connections"
- "[ListenerNewConnection](%{public}@) Attempting to connect with new connection"
- "[ListenerNewConnection](%{public}@) Completion successfully received for request of clientID: %{public}@"
- "[ListenerNewConnection](%{public}@) Resumed connection, requesting clientID"
- "[RemoveConnection] From %lu clientIDs currently connected, attempting to remove connection: %{public}@"
- "[RemoveConnection] Informing server of connection disconnect for clientID: %{public}@"
- "[RemoveConnection] No remaining connections for clientID: %{public}@"
- "[RemoveConnection] Removing connection for clientID: %{public}@, connection: %{public}@"
- "[RemoveConnection] Removing observable connection: %{public}@"
- "[RemoveConnection] Set remaining %lu connections for clientID: %{public}@, connections: %{public}@"
- "[RequestClientID](%{public}@) Replying to server for clientID request: %{public}@"
- "[RequestClientID](%{public}@) Replying to server for clientID request: %{public}@, no reply block provided"
- "[SendClientMessage](%{public}@) Calling client delegate method handleMessage"
- "[SendServerMessage](%{public}@) connectProtocolFromClientSendServerMessage using isConnection:authorizedForMessage: via server delegate"
- "[SetConnection] Adding new observable connection: %{public}@"
- "[SetConnection] Attempting to set new clientID: %{public}@, for connection: %{public}@"
- "[SetConnection] Same connection already exists for clientID: %{public}@"
- "[SetConnection] Setting new connection (to existing set) for clientID: %{public}@, newConnection: %{public}@"
- "[SetConnection] Setting new connection (to new set) for clientID: %{public}@, newConnection: %{public}@"

```
