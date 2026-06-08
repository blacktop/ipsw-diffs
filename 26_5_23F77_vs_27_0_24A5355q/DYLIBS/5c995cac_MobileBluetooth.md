## MobileBluetooth

> `/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth`

```diff

-195.7.1.2.0
-  __TEXT.__text: 0x2e9b8 sha256:b59b1d1900ad61d53c833cdb9584ef465733faf5cb70f16ff3811805b2c98f7e
-  __TEXT.__auth_stubs: 0x490 sha256:490f7298c8d9eff196e5b19eae699153ec82303a38ae79ee8aaee3f97c8c198b
-  __TEXT.__const: 0xc8 sha256:cc1882f2d51076e82938e3837349a59a0d461cece14a1bbd58763fd4876a0614
-  __TEXT.__oslogstring: 0x67da sha256:0e67726d1213ce6679291c50bb86521d4a1d083ae6fdbf4fa2794628c209270a
-  __TEXT.__cstring: 0x3279 sha256:67682dc34d9f0c4d98fa61b65368d28a6bf377b29201b7216d83b0f0a8ccbc2e
-  __TEXT.__unwind_info: 0x820 sha256:922aacd1a69c988e602893768bb785d51cdfd7c69fc6c21898936b0b30b6568f
-  __DATA_CONST.__got: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
-  __DATA_CONST.__const: 0x2158 sha256:5d48a97f336000f6e06978e26da825b18b9fb154b8b691044f72c79d45dd580e
-  __AUTH_CONST.__auth_got: 0x248 sha256:62ec1707572ac5078d31a687a5d23de0c6d2a58d3462efb7039957548a7986cc
-  __AUTH_CONST.__cfstring: 0x40 sha256:9be335c7313a464679b85e3774daca1dfa99c6425cd119d6781dcff4fd9803b3
+2700.37.0.0.0
+  __TEXT.__text: 0x2e40c sha256:feb09686ffcb072317e7a4ecf8e59a79bc43968b6a3c0a1045f88c13fcaaa8f6
+  __TEXT.__const: 0xc8 sha256:e8cb26d981dedf84956c91b50f93844667100f045a254a5d0f264a04092ea1fc
+  __TEXT.__oslogstring: 0x69d9 sha256:83339a6f0a82123515dda1ecb65cc512bb208a598fa3ff511930605442b6f158
+  __TEXT.__cstring: 0x33de sha256:2b2b04e5524fdcd3e57377e11ccfc442c6e7757e2e7e6317491b78f8779031d1
+  __TEXT.__unwind_info: 0x840 sha256:e35fa67d8f3f0fab8fc6afd05d9234f0e508ee67055118e9386d99f2a1429baf
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x21f8 sha256:afdaf11f090a4838392c135181adcb266e056f2bb1bda423fcad075d3d521f8c
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x40 sha256:ea5e2a938fdca3a7ef56ed01f682cc20d81c63021be8242d58263f115891c697
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__common: 0x2a00 sha256:ee0d534dd385f4c26c52ee121654897b783c0754c6512886e53578dce4b24735
-  __DATA_DIRTY.__data: 0x1e8 sha256:7f2d7d58797051267b40f5aa7f2ab7d74d7eb14d4278e163b655db918b4893a5
+  __DATA_DIRTY.__data: 0x1e8 sha256:c7fef3c5e6d17494597b7a93a241db4d04a7142c777a854f2d9e7fb4ab8f7b47
   __DATA_DIRTY.__common: 0x3730 sha256:c2f3fd7c5460d6496be2b97fa4e960d60b5a2148124508003546625c7c345bc3
   __DATA_DIRTY.__bss: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
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
