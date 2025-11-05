## BridgeOSSoftwareUpdate

> `/System/Library/PrivateFrameworks/BridgeOSSoftwareUpdate.framework/Versions/A/BridgeOSSoftwareUpdate`

```diff

 52.0.0.0.0
-  __TEXT.__text: 0x48d4
+  __TEXT.__text: 0x4c88
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x288
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x18b1
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_classname: 0x91
   __TEXT.__objc_methname: 0xb02
   __TEXT.__objc_methtype: 0x12c

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D1A7409-A38C-3D3E-8700-1FF6279083AF
-  Functions: 85
-  Symbols:   282
+  UUID: DF98B5C3-97AD-37CE-BE70-563BA582F5AC
+  Functions: 110
+  Symbols:   309
   CStrings:  391
 
Symbols:
+ -[BridgeOSSoftwareUpdateController sendProxyMessageAsync:mergeDict:options:errorHandler:].cold.1
+ -[BridgeOSSoftwareUpdateController sendProxyMessageAsync:mergeDict:options:errorHandler:].cold.2
+ -[BridgeOSSoftwareUpdateController transferUpdateBrain:options:].cold.1
+ -[BridgeOSSoftwareUpdateController transferUpdateBrain:options:].cold.2
+ -[BridgeOSSoftwareUpdateController transferUpdateBundle:options:].cold.1
+ -[BridgeOSSoftwareUpdateController transferUpdateBundle:options:].cold.2
+ -[NSMutableDictionary(BridgeOSSoftwareUpdateStateAdditions) addPathForFileTransfer:].cold.1
+ -[NSMutableDictionary(BridgeOSSoftwareUpdateStateAdditions) addPathForFileTransfer:].cold.2
+ BOSU_Log_Init.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __89-[BridgeOSSoftwareUpdateController sendProxyMessageAsync:mergeDict:options:errorHandler:]_block_invoke.cold.1
+ __89-[BridgeOSSoftwareUpdateController sendProxyMessageAsync:mergeDict:options:errorHandler:]_block_invoke.cold.2
+ __89-[BridgeOSSoftwareUpdateController sendProxyMessageAsync:mergeDict:options:errorHandler:]_block_invoke.cold.3
+ merge_into_xpc_dict.cold.1
+ merge_into_xpc_dict.cold.2
+ merge_into_xpc_dict.cold.3
+ xpc_dictionary_set_error.cold.1
+ xpc_dictionary_set_error.cold.2
+ xpc_dictionary_set_object.cold.1
+ xpc_dictionary_set_object.cold.2
+ xpc_dictionary_set_object.cold.3
+ xpc_dictionary_set_object.cold.4
+ xpc_dictionary_set_object.cold.5
CStrings:
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/BridgeOSSoftwareUpdateController/Framework/BridgeOSSoftwareUpdateController.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/BridgeOSSoftwareUpdateController/Shared/BridgeOSSoftwareUpdateIPCUtilities.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/BridgeOSSoftwareUpdateController/Shared/BridgeOSSoftwareUpdateUtilities.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/BridgeOSSoftwareUpdateController/Framework/BridgeOSSoftwareUpdateController.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/BridgeOSSoftwareUpdateController/Shared/BridgeOSSoftwareUpdateIPCUtilities.m"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/BridgeOSSoftwareUpdateController/Shared/BridgeOSSoftwareUpdateUtilities.m"

```
