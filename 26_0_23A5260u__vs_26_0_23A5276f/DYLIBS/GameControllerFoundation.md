## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-13.0.28.0.0
-  __TEXT.__text: 0x6dfe8
+13.0.31.0.0
+  __TEXT.__text: 0x6e3cc
   __TEXT.__auth_stubs: 0x1420
   __TEXT.__objc_methlist: 0x68b4
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x3384
-  __TEXT.__cstring: 0x6d1d
+  __TEXT.__gcc_except_tab: 0x32e8
+  __TEXT.__cstring: 0x6f56
   __TEXT.__oslogstring: 0x30a9
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x20d0
+  __TEXT.__unwind_info: 0x20a0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x174f
-  __TEXT.__objc_methname: 0x8e35
+  __TEXT.__objc_methname: 0x8e34
   __TEXT.__objc_methtype: 0x296a
   __TEXT.__objc_stubs: 0x51e0
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1b88
+  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x160

   __DATA.__objc_ivar: 0x854
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AAC76E1D-8357-30AD-B402-8C2622E12472
-  Functions: 2837
-  Symbols:   9804
-  CStrings:  4288
+  UUID: CBA57AC5-B117-3328-B91F-A1F3086EF440
+  Functions: 2844
+  Symbols:   9821
+  CStrings:  4295
 
Symbols:
+ _GCPrepareIOCFPlugInVtbl.Lock
+ _GCPrepareIUnknownVtbl.Lock
+ _GCPrepareIUnknownVtbl.cold.1
+ _IOGCDeviceInterfacePrepareObjCVtbl.Lock
+ _IOGCFastPathClientInterfacePrepareObjCVtbl.Lock
+ _IOGCFastPathClientInterfacePrepareObjCVtbl.cold.2
+ _IOGCFastPathControlQueueInterfacePrepareObjCVtbl.Lock
+ _IOGCFastPathControlQueueInterfacePrepareObjCVtbl.cold.2
+ _IOGCFastPathInputQueueInterfacePrepareObjCVtbl.Lock
+ _IOGCFastPathReaderInterfacePrepareObjCVtbl.Lock
+ _IOGCFastPathReaderInterfacePrepareObjCVtbl.cold.2
+ _IOGCFastPathSampleContainerInterfacePrepareObjCVtbl.Lock
+ _IOGCFastPathSampleContainerInterfacePrepareObjCVtbl.cold.2
+ ___IOGCFastPathInputQueueInterfacePrepareObjCVtbl_block_invoke
+ ___IOGCFastPathInputQueueInterfacePrepareObjCVtbl_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e70_v24?0^{IOGCFastPathInputQueueInterface=^v^?^?^?SSI^?^?^?^?^?^?^?}8q16ls32l8
+ _objc_msgSend$bytes
+ _objc_msgSend$initWithBytes:length:
- _OBJC_CLASS_$_NSMutableData
- _objc_msgSend$initWithLength:
- _objc_msgSend$mutableBytes
CStrings:
+ "BUG IN CLIENT OF GCIUnknownObjC: vtbl offset out of supported range."
+ "BUG IN CLIENT OF IOGCFastPathClientInterface: vtbl offset out of supported range."
+ "BUG IN CLIENT OF IOGCFastPathControlQueueInterface: vtbl offset out of supported range."
+ "BUG IN CLIENT OF IOGCFastPathInputQueueInterface: vtbl offset out of supported range."
+ "BUG IN CLIENT OF IOGCFastPathReaderInterface: vtbl offset out of supported range."
+ "BUG IN CLIENT OF IOGCFastPathSampleContainerInterface: vtbl offset out of supported range."
+ "bytes"
+ "initWithBytes:length:"
+ "v24@?0^{IOGCFastPathInputQueueInterface=^v^?^?^?SSI^?^?^?^?^?^?^?}8q16"
- "initWithLength:"
- "mutableBytes"

```
