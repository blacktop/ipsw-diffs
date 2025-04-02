## NetworkInfo

> `/System/Library/PrivateFrameworks/NetworkInfo.framework/Versions/A/NetworkInfo`

```diff

-147.100.6.0.0
-  __TEXT.__text: 0x808f0
-  __TEXT.__auth_stubs: 0x17c0
+147.120.5.0.0
+  __TEXT.__text: 0x80a6c
+  __TEXT.__auth_stubs: 0x17e0
   __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0x1b4a
-  __TEXT.__cstring: 0x2318
+  __TEXT.__cstring: 0x2328
   __TEXT.__oslogstring: 0x1f34
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0x90a

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x9c
   __TEXT.__swift5_assocty: 0x110
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__unwind_info: 0xef8
   __TEXT.__eh_frame: 0x1a68
   __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methname: 0x152e
+  __TEXT.__objc_methname: 0x153a
   __TEXT.__objc_methtype: 0x86f
-  __TEXT.__objc_stubs: 0xac0
+  __TEXT.__objc_stubs: 0xae0
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x548
+  __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH_CONST.__auth_ptr: 0x3e8
-  __AUTH_CONST.__const: 0x5800
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x1518
+  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH_CONST.__auth_ptr: 0x3e0
+  __AUTH_CONST.__const: 0x5830
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__objc_const: 0x1538
   __AUTH.__objc_data: 0xdd0
   __AUTH.__data: 0x520
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0xa60
   __DATA.__bss: 0x2e30
   __DATA.__common: 0xc0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2159
-  Symbols:   1096
-  CStrings:  803
+  Functions: 2161
+  Symbols:   1103
+  CStrings:  805
 
Symbols:
+ -[ICMPPingProbe running]
+ -[ICMPPingProbe setRunning:]
+ -[PacketCaptureur connectToXPCService]
+ -[PacketCaptureur connectToXPCService].cold.1
+ -[PacketCaptureur connectToXPCService].cold.2
+ OBJC_IVAR_$_ICMPPingProbe._completionHandlerCalled
+ OBJC_IVAR_$_ICMPPingProbe._running
+ ___38-[PacketCaptureur connectToXPCService]_block_invoke
+ ___43-[PacketCaptureur stopTask:withCompletion:]_block_invoke_2
+ ___56-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke_2
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ __block_literal_global.247
+ _dispatch_assert_queue$V2
+ _dispatch_sync
+ _objc_msgSend$connectToXPCService
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$running
- -[PacketCaptureur connectToNetDiagnosticsd]
- -[PacketCaptureur connectToNetDiagnosticsd].cold.1
- -[PacketCaptureur connectToNetDiagnosticsd].cold.2
- -[TestProbe isRunning]
- -[TestProbe setRunning:]
- OBJC_IVAR_$_TestProbe._running
- ___43-[PacketCaptureur connectToNetDiagnosticsd]_block_invoke
- __block_literal_global.236
- _objc_msgSend$connectToNetDiagnosticsd
- _objc_msgSend$isRunning
CStrings:
+ "-[PacketCaptureur connectToXPCService]"
+ "-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke_2"
+ "-[PacketCaptureur stopTask:withCompletion:]_block_invoke_2"
+ "TB,V_running"
+ "_completionHandlerCalled"
+ "connectToXPCService"
+ "numberWithInt:"
+ "timeout_seconds"
- "-[PacketCaptureur connectToNetDiagnosticsd]"
- "-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke"
- "-[PacketCaptureur stopTask:withCompletion:]_block_invoke"
- "TB,N,GisRunning,V_running"
- "connectToNetDiagnosticsd"
- "isRunning"

```
