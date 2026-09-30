## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.100.235.0.0
-  __TEXT.__text: 0x8d9f4
+1837.100.250.0.0
+  __TEXT.__text: 0x8da24
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_methlist: 0x6aac
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x128ce
+  __TEXT.__cstring: 0x128fb
   __TEXT.__oslogstring: 0xaf04
   __TEXT.__gcc_except_tab: 0x1350
   __TEXT.__unwind_info: 0x1ef8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E64D1B0-488B-3CFB-8BE2-2230C4027BA5
+  UUID: BE5449E1-5612-37AD-9DA8-822828ED54BB
   Functions: 2967
   Symbols:   9032
-  CStrings:  7612
+  CStrings:  7615
 
Symbols:
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1221
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1222
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1215
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1216
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1220
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1218
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1219
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1213
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1214
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1217
Functions:
~ ___73-[MAXpcManager sendSync:gettingResponseCode:codeForXpcError:loggingName:]_block_invoke : 624 -> 648
~ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke_2 : 888 -> 912
CStrings:
+ "requestType"
+ "requestTypeAsync"
+ "requestTypeSync"

```
