## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

```diff

-3285.8.3.0.0
-  __TEXT.__text: 0x52ab8c
+3285.9.1.0.0
+  __TEXT.__text: 0x52ac30
   __TEXT.__auth_stubs: 0x38e0
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0xe54

   __TEXT.__oslogstring: 0x4e93
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__dlopen_cstrs: 0x9b
-  __TEXT.__unwind_info: 0x5980
+  __TEXT.__unwind_info: 0x5988
   __TEXT.__eh_frame: 0x7694
   __TEXT.__objc_classname: 0x37a
   __TEXT.__objc_methname: 0x24db
   __TEXT.__objc_methtype: 0x967
   __TEXT.__objc_stubs: 0x1900
-  __DATA_CONST.__got: 0xdb8
+  __DATA_CONST.__got: 0xdc0
   __DATA_CONST.__const: 0x3ba8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x20

   __AUTH.__data: 0x70
   __DATA.__objc_ivar: 0x21c
   __DATA.__data: 0x3d4
-  __DATA.__bss: 0x590
+  __DATA.__bss: 0x598
   __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x2b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA7B156A-D707-31D7-981A-D16584664488
-  Functions: 8424
-  Symbols:   20352
+  UUID: 78A6F9FC-29A8-388C-9363-4FCE085D21A4
+  Functions: 8427
+  Symbols:   20359
   CStrings:  3845
 
Symbols:
+ _VTDecompressionSessionRemoteBridge_PreferHighPriorityQueueForAllDecompression
+ _VTDecompressionSessionRemotePreferHighPriorityQueueForAllDecompression
+ _VTDecompressionSessionRemoteXPC_PreferHighPriorityQueueForAllDecompression
+ _gXPCRemoteClientUseHighPriorityQueue
+ _kFigXPCRemoteClientOption_QueuePriority
Functions:
+ _VTDecompressionSessionRemotePreferHighPriorityQueueForAllDecompression
+ _VTDecompressionSessionRemoteXPC_PreferHighPriorityQueueForAllDecompression
~ ___dsrxpc_oneTimeInitialization_block_invoke : 324 -> 356
+ _VTDecompressionSessionRemoteBridge_FlushPixelBufferPool
~ _vtMetalTransferSessionRebuild : 12616 -> 12620
CStrings:
+ "description=CoreMedia_VideoToolbox-3285.9.1"
- "description=CoreMedia_VideoToolbox-3285.8.3"

```
