## GPUToolsTransport

> `/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport`

```diff

-230.45.0.0.0
-  __TEXT.__text: 0x2a1d4
+240.6.0.0.0
+  __TEXT.__text: 0x2a410
   __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0x4ad4
+  __TEXT.__objc_methlist: 0x4af4
   __TEXT.__const: 0x208
   __TEXT.__cstring: 0x2027
   __TEXT.__oslogstring: 0x6b5
-  __TEXT.__unwind_info: 0xaf0
-  __TEXT.__objc_classname: 0x103d
-  __TEXT.__objc_methname: 0x7491
-  __TEXT.__objc_methtype: 0x17bb
-  __TEXT.__objc_stubs: 0x2920
+  __TEXT.__unwind_info: 0xb00
+  __TEXT.__objc_classname: 0x103e
+  __TEXT.__objc_methname: 0x7541
+  __TEXT.__objc_methtype: 0x17da
+  __TEXT.__objc_stubs: 0x2960
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xad0
+  __DATA_CONST.__const: 0xaf8
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9850
-  __DATA_CONST.__objc_selrefs: 0x1958
+  __DATA_CONST.__objc_const: 0x98d0
+  __DATA_CONST.__objc_selrefs: 0x1970
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__cfstring: 0x29e0
   __AUTH_CONST.__objc_intobj: 0x48

   __DATA.__objc_protorefs: 0x88
   __DATA.__objc_classrefs: 0x470
   __DATA.__objc_superrefs: 0x450
-  __DATA.__objc_ivar: 0x768
+  __DATA.__objc_ivar: 0x778
   __DATA.__data: 0xf7c
   __DATA.__common: 0x18
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1617
-  Symbols:   5776
-  CStrings:  2286
+  Functions: 1621
+  Symbols:   5791
+  CStrings:  2294
 
Symbols:
+ -[GTBulkDataService initWithDownloadHighWaterMark:]
+ -[GTBulkDataService takeDownloadDataForHandle:]
+ -[GTBulkDataService waitUntilDownloadCapacity]
+ _OBJC_IVAR_$_GTBulkDataService._downloadHighWaterMarkBytes
+ _OBJC_IVAR_$_GTBulkDataService._downloadStoreBytes
+ _OBJC_IVAR_$_GTBulkDataService._downloadTransmitOff
+ _OBJC_IVAR_$_GTBulkDataService._downloadTransmitState
+ ___47-[GTBulkDataService takeDownloadDataForHandle:]_block_invoke
+ ___ProxyReplayerBatchRequest_block_invoke_2
+ ___block_descriptor_56_8_32s40s48s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
+ _objc_msgSend$initWithDownloadHighWaterMark:
+ _objc_msgSend$takeDownloadDataForHandle:
- ___68-[GTBulkDataService downloadData:usingTransferOptions:chunkHandler:]_block_invoke.68
CStrings:
+ "\x01\x111\x15"
+ "@\"NSObject<OS_dispatch_group>\""
+ "_downloadHighWaterMarkBytes"
+ "_downloadStoreBytes"
+ "_downloadTransmitOff"
+ "_downloadTransmitState"
+ "initWithDownloadHighWaterMark:"
+ "takeDownloadDataForHandle:"
+ "waitUntilDownloadCapacity"
- "\x01\x11\x15"

```
