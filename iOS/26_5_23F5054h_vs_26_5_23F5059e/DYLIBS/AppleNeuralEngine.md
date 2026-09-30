## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-380.502.0.0.0
-  __TEXT.__text: 0x45be8
+380.601.0.0.0
+  __TEXT.__text: 0x46104
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x263c
+  __TEXT.__objc_methlist: 0x264c
   __TEXT.__const: 0x280
-  __TEXT.__oslogstring: 0x81e6
-  __TEXT.__cstring: 0x2e21
-  __TEXT.__gcc_except_tab: 0x51a8
-  __TEXT.__unwind_info: 0x1208
+  __TEXT.__oslogstring: 0x8375
+  __TEXT.__cstring: 0x2e26
+  __TEXT.__gcc_except_tab: 0x527c
+  __TEXT.__unwind_info: 0x1230
   __TEXT.__objc_classname: 0x2ef
-  __TEXT.__objc_methname: 0x5fce
-  __TEXT.__objc_methtype: 0x24ac
-  __TEXT.__objc_stubs: 0x4440
+  __TEXT.__objc_methname: 0x5fef
+  __TEXT.__objc_methtype: 0x24c8
+  __TEXT.__objc_stubs: 0x4460
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1668
+  __DATA_CONST.__objc_selrefs: 0x1670
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x118
   __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x490
-  __AUTH_CONST.__cfstring: 0x3a60
+  __AUTH_CONST.__cfstring: 0x3a80
   __AUTH_CONST.__objc_const: 0x3658
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: F3E0C997-4F0B-3F22-9E29-2F3C194F6E43
-  Functions: 1426
-  Symbols:   4706
-  CStrings:  2704
+  UUID: D029ADFA-3196-39A1-B3D9-E51B46E57179
+  Functions: 1446
+  Symbols:   4752
+  CStrings:  2715
 
Symbols:
+ +[_ANEVirtualClient copyData:toExistingIOSurfaceRef:]
+ +[_ANEVirtualClient copyData:toExistingIOSurfaceRef:].cold.1
+ +[_ANEVirtualClient copyData:toExistingIOSurfaceRef:].cold.2
+ +[_ANEVirtualClient copyData:toExistingIOSurfaceRef:].cold.3
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table71
+ GCC_except_table89
+ ___39-[_ANEDaemonConnection echo:withReply:]_block_invoke.cold.1
+ ___42+[_ANEDeviceInfo aneSubTypeProductVariant]_block_invoke.143
+ ___49-[_ANEDaemonConnection endRealTimeTaskWithReply:]_block_invoke.cold.1
+ ___51-[_ANEDaemonConnection beginRealTimeTaskWithReply:]_block_invoke.cold.1
+ ___53-[_ANEDaemonConnection purgeCompiledModel:withReply:]_block_invoke.cold.1
+ ___54-[_ANEDaemonConnection reportTelemetryToPPS:playload:]_block_invoke.cold.1
+ ___57-[_ANEDaemonConnection compiledModelExistsFor:withReply:]_block_invoke.cold.1
+ ___58-[_ANEDaemonConnection unloadModel:options:qos:withReply:]_block_invoke.cold.1
+ ___65-[_ANEDaemonConnection purgeCompiledModelMatchingHash:withReply:]_block_invoke.cold.1
+ ___66-[_ANEDaemonConnection compiledModelExistsMatchingHash:withReply:]_block_invoke.cold.1
+ ___73-[_ANEDaemonConnection loadModel:sandboxExtension:options:qos:withReply:]_block_invoke.cold.1
+ ___76-[_ANEDaemonConnection compileModel:sandboxExtension:options:qos:withReply:]_block_invoke.cold.1
+ ___83-[_ANEDaemonConnection loadModelNewInstance:options:modelInstParams:qos:withReply:]_block_invoke.cold.1
+ ___83-[_ANEDaemonConnection prepareChainingWithModel:options:chainingReq:qos:withReply:]_block_invoke.cold.1
+ ___block_literal_global.145
+ ___block_literal_global.150
+ _objc_msgSend$copyData:toExistingIOSurfaceRef:
- GCC_except_table106
- GCC_except_table111
- GCC_except_table122
- GCC_except_table72
- GCC_except_table88
- ___42+[_ANEDeviceInfo aneSubTypeProductVariant]_block_invoke.140
- ___block_literal_global.139
- ___block_literal_global.147
CStrings:
+ "%@: Copied %zu bytes to existing IOSurface ioSID=%u"
+ "%@: Created reusable IOSurface with ioSID=%u (size=%u) for chunked transfer"
+ "%@: ERROR data length is 0"
+ "%@: ERROR data length=%zu exceeds IOSurface size=%llu"
+ "%@: ERROR failed to copy segment=%d data to existing IOSurface for fileSize=%llu chunkSize=%u chunkDataLength=%llu at path=%@"
+ "%@: ERROR failed to create IOSurface for chunked transfer with chunkSize=%u at path=%@"
+ "%@: ERROR failed to get segment=%d for fileSize=%llu chunkSize=%u data.length=%llu at path=%@"
+ "%@: ERROR passed in data is nil"
+ "%@: ERROR passed in ioSurfaceRef is NULL"
+ "B32@0:8@16^{__IOSurface=}24"
+ "copyData:toExistingIOSurfaceRef:"
+ "h17s"
- "%@: ERROR failed to get segment=%d for fileSize=%llu chunkSize=%u at path=%@"
- "%@: ERROR failed to write segment=%d to IOSurface for fileSize=%llu chunkSize=%u chunkDataLength=%llu at path=%@"

```
