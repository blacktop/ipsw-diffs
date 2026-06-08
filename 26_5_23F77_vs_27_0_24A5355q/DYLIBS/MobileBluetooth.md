## MobileBluetooth

> `/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth`

```diff

-195.7.1.2.0
-  __TEXT.__text: 0x2e9b8
-  __TEXT.__auth_stubs: 0x490
+2700.37.0.0.0
+  __TEXT.__text: 0x2e40c
   __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x67da
-  __TEXT.__cstring: 0x3279
-  __TEXT.__unwind_info: 0x820
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x2158
-  __AUTH_CONST.__auth_got: 0x248
+  __TEXT.__oslogstring: 0x69d9
+  __TEXT.__cstring: 0x33de
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x21f8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__common: 0x2a00
   __DATA_DIRTY.__data: 0x1e8
   __DATA_DIRTY.__common: 0x3730

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: FF11FB2D-BF3F-3701-AEF4-6A9666CACAEB
-  Functions: 992
-  Symbols:   3945
-  CStrings:  922
+  UUID: 54F6B7C7-74FB-396B-8E03-AB9AC12003BE
+  Functions: 1009
+  Symbols:   4007
+  CStrings:  951
 
Symbols:
+ _BTDeviceHasTag
+ _BTDeviceHasTag.cold.1
+ _BTDeviceHasTag.cold.2
+ _BTDeviceHasTag.cold.3
+ _BTDeviceHasTag.cold.4
+ _BTDeviceHasTag.cold.5
+ _BTDeviceHasTag.cold.6
+ _BTDeviceTag
+ _BTDeviceTag.cold.1
+ _BTDeviceTag.cold.2
+ _BTDeviceTag.cold.3
+ _BTDeviceTag.cold.4
+ _BTDeviceTag.cold.5
+ _BTDeviceTag.cold.6
+ _BTDeviceUntag
+ _BTDeviceUntag.cold.1
+ _BTDeviceUntag.cold.2
+ _BTDeviceUntag.cold.3
+ _BTDeviceUntag.cold.4
+ _BTDeviceUntag.cold.5
+ _BTDeviceUntag.cold.6
+ _BTLocalDeviceGetConnectedLEDevices
+ _BTLocalDeviceGetConnectedLEDevices.cold.1
+ _BTLocalDeviceGetConnectedLEDevices.cold.2
+ _BTLocalDeviceGetConnectedLEDevices.cold.3
+ _BTLocalDeviceGetConnectedLEDevices.cold.4
+ ___BTDeviceHasTag_block_invoke
+ ___BTDeviceHasTag_block_invoke.cold.1
+ ___BTDeviceHasTag_block_invoke.cold.2
+ ___BTDeviceTag_block_invoke
+ ___BTDeviceTag_block_invoke.cold.1
+ ___BTDeviceTag_block_invoke.cold.2
+ ___BTDeviceUntag_block_invoke
+ ___BTDeviceUntag_block_invoke.cold.1
+ ___BTDeviceUntag_block_invoke.cold.2
+ ___BTLocalDeviceGetConnectedLEDevices_block_invoke
+ ___BTLocalDeviceGetConnectedLEDevices_block_invoke.cold.1
+ ___BTLocalDeviceGetConnectedLEDevices_block_invoke.cold.2
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.145
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.178
+ ___block_descriptor_tmp.190
+ _sendMessageWithReplySync.cold.5
+ _sendMessageWithReplySync.cold.6
+ _uuid_parse
+ _xpc_retain
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.133
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.146
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.177
CStrings:
+ "BTDeviceHasTag over XPC"
+ "BTDeviceTag over XPC"
+ "BTDeviceUntag over XPC"
+ "BTLocalDeviceGetConnectedLEDevices over XPC"
+ "Found %zu LE devices (of %zu total)"
+ "Invalid argument"
+ "Invalid tag string argument"
+ "LE Device"
+ "MBFXPC releaseMBXpcConnection finalizer running for session:%s on queue:%s"
+ "kCBMsgArgBdAddress"
+ "kCBMsgArgBtBand"
+ "kCBMsgArgConnectionInterval"
+ "kCBMsgArgConnectionRole"
+ "kCBMsgArgIsStreaming"
+ "kCBMsgArgLEDeviceArray"
+ "kCBMsgArgNumberOfFlushes"
+ "kCBMsgArgOptimizedState"
+ "kCBMsgArgRole"
+ "kCBMsgArgTag"
+ "kCBMsgArgUUIDString"
+ "kCBMsgIdDeviceHasTagMsg"
+ "kCBMsgIdDeviceHasTagMsg reply result:%llx, _hasTag %d"
+ "kCBMsgIdDeviceTagMsg"
+ "kCBMsgIdDeviceTagMsg reply result:%llx"
+ "kCBMsgIdDeviceUntagMsg"
+ "kCBMsgIdDeviceUntagMsg reply result:%llx"
+ "kCBMsgIdLocalDeviceGetConnectedLEDevicesMsg"
+ "sendMessageWithReplySync: xpcConnection is NULL for sessionName:%s msgId:%s — connection already torn down"
+ "unknown"

```
