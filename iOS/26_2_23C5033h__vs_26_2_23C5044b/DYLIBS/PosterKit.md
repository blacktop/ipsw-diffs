## PosterKit

> `/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit`

```diff

-304.2.5.100.0
-  __TEXT.__text: 0x1351cc
+304.2.6.100.0
+  __TEXT.__text: 0x13552c
   __TEXT.__auth_stubs: 0x20c0
-  __TEXT.__objc_methlist: 0x182e4
+  __TEXT.__objc_methlist: 0x1831c
   __TEXT.__const: 0x22f4
-  __TEXT.__cstring: 0x9bc8
+  __TEXT.__cstring: 0x9c08
   __TEXT.__oslogstring: 0x5f09
   __TEXT.__gcc_except_tab: 0x28a0
   __TEXT.__ustring: 0x1c

   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x118
-  __TEXT.__unwind_info: 0x4ee0
+  __TEXT.__unwind_info: 0x4ef0
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x3bcc
-  __TEXT.__objc_methname: 0x3dba6
+  __TEXT.__objc_methname: 0x3dc37
   __TEXT.__objc_methtype: 0xbb9f
-  __TEXT.__objc_stubs: 0x20f40
+  __TEXT.__objc_stubs: 0x20fe0
   __DATA_CONST.__got: 0x18b8
   __DATA_CONST.__const: 0x34f0
   __DATA_CONST.__objc_classlist: 0xa08
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb670
+  __DATA_CONST.__objc_selrefs: 0xb698
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x830
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x1070
   __AUTH_CONST.__const: 0x1db0
   __AUTH_CONST.__cfstring: 0x9720
-  __AUTH_CONST.__objc_const: 0x4e620
+  __AUTH_CONST.__objc_const: 0x4e640
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x36d8
   __AUTH.__data: 0x408
-  __DATA.__objc_ivar: 0x18b4
+  __DATA.__objc_ivar: 0x18b8
   __DATA.__data: 0x47f0
   __DATA.__bss: 0x1360
   __DATA.__common: 0x29

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8CB17D36-C2D2-317C-AC36-467044E41E41
-  Functions: 8475
-  Symbols:   28252
-  CStrings:  13140
+  UUID: C2ED37F6-5DF4-37EB-B1DB-A593D731FB3C
+  Functions: 8483
+  Symbols:   28274
+  CStrings:  13148
 
Symbols:
+ -[PRRenderer _cleanupSessionAssertions]
+ -[PRRenderingServiceServer _addConnection:]
+ -[PRRenderingServiceServer _queue_addConnection:]
+ -[PRRenderingServiceServer _queue_removeConnection:]
+ -[PRRenderingServiceServer _removeConnection:]
+ -[PRRenderingServiceServer connectionsCopy]
+ _OBJC_IVAR_$_PRRenderingServiceServer._connectionQueue_connections
+ _OBJC_IVAR_$_PRRenderingServiceServer._connectionsQueue
+ _OBJC_IVAR_$_PRRenderingServiceServer._targetQueue
+ ___39-[PRRenderer _cleanupSessionAssertions]_block_invoke
+ ___43-[PRRenderingServiceServer _addConnection:]_block_invoke
+ ___43-[PRRenderingServiceServer connectionsCopy]_block_invoke
+ ___46-[PRRenderingServiceServer _removeConnection:]_block_invoke
+ ___70-[PRRenderingServiceServer listener:didReceiveConnection:withContext:]_block_invoke.81
+ _objc_msgSend$_addConnection:
+ _objc_msgSend$_queue_addConnection:
+ _objc_msgSend$_queue_removeConnection:
+ _objc_msgSend$_removeConnection:
+ _objc_msgSend$connectionsCopy
- _OBJC_IVAR_$_PRRenderingServiceServer._connectionQueue
- _OBJC_IVAR_$_PRRenderingServiceServer._connections
- ___31-[PRRenderer initWithDelegate:]_block_invoke_5
- ___31-[PRRenderer initWithDelegate:]_block_invoke_6
- ___70-[PRRenderingServiceServer listener:didReceiveConnection:withContext:]_block_invoke.80
CStrings:
+ "_addConnection:"
+ "_connectionQueue_connections"
+ "_connectionsQueue"
+ "_queue_addConnection:"
+ "_queue_removeConnection:"
+ "_removeConnection:"
+ "_targetQueue"
+ "com.apple.PosterKit.PRRenderingServiceServer.connectionsQueue"
+ "com.apple.PosterKit.PRRenderingServiceServer.targetQueue"
+ "connectionsCopy"
- "_connections"
- "com.apple.PosterKit.PRRenderingServiceServer.connectionQueue"

```
