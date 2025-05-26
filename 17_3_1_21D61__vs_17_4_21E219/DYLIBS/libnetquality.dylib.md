## libnetquality.dylib

> `/usr/lib/libnetquality.dylib`

```diff

-113.60.5.0.0
-  __TEXT.__text: 0x15698
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x11d0
+113.100.4.0.0
+  __TEXT.__text: 0x15838
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x11f0
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__gcc_except_tab: 0x380
   __TEXT.__cstring: 0x208b
-  __TEXT.__oslogstring: 0x146d
-  __TEXT.__unwind_info: 0x47c
+  __TEXT.__oslogstring: 0x1481
+  __TEXT.__unwind_info: 0x48c
   __TEXT.__objc_classname: 0x2f2
-  __TEXT.__objc_methname: 0x3747
+  __TEXT.__objc_methname: 0x37a1
   __TEXT.__objc_methtype: 0xc28
-  __TEXT.__objc_stubs: 0x2e20
+  __TEXT.__objc_stubs: 0x2e80
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__const: 0x578
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2d90
-  __DATA_CONST.__objc_selrefs: 0xcd8
+  __DATA_CONST.__objc_selrefs: 0xcf0
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x798

   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x558
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x98
   __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0x300
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 509
-  Symbols:   2088
-  CStrings:  1259
+  Functions: 512
+  Symbols:   2099
+  CStrings:  1263
 
Symbols:
+ -[NetworkQualityHTTPServer HTTP2ParametersForServer]
+ -[NetworkQualityHTTPServer HTTP3ParametersForServer]
+ -[NetworkQualityHTTPServer setCommmonParameters:]
+ GCC_except_table19
+ ___34-[NetworkQualityHTTPServer start:]_block_invoke.15
+ ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.28
+ ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.59
+ ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke_2.29
+ ___52-[NetworkQualityHTTPServer HTTP2ParametersForServer]_block_invoke
+ ___52-[NetworkQualityHTTPServer HTTP2ParametersForServer]_block_invoke_2
+ ___52-[NetworkQualityHTTPServer HTTP3ParametersForServer]_block_invoke
+ ___52-[NetworkQualityHTTPServer HTTP3ParametersForServer]_block_invoke_2
+ ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.233
+ ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.234
+ __unnamed_array_storage.185
+ __unnamed_array_storage.201
+ _nw_http2_set_idle_timeout
+ _nw_http3_set_idle_timeout
+ _nw_parameters_set_data_mode
+ _nw_parameters_set_prohibit_joining_protocols
+ _objc_msgSend$HTTP2ParametersForServer
+ _objc_msgSend$HTTP3ParametersForServer
+ _objc_msgSend$setCommmonParameters:
+ _sec_protocol_options_set_peer_authentication_required
- ___34-[NetworkQualityHTTPServer start:]_block_invoke.12
- ___34-[NetworkQualityHTTPServer start:]_block_invoke.16
- ___34-[NetworkQualityHTTPServer start:]_block_invoke_2.17
- ___34-[NetworkQualityHTTPServer start:]_block_invoke_3.20
- ___34-[NetworkQualityHTTPServer start:]_block_invoke_4
- ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.31
- ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke.62
- ___40-[NetworkQualityHTTPServer receiveLoop:]_block_invoke_2.32
- ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.232
- ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.233
- ___block_descriptor_40_e8_32s_e42_v16?0"NSObject<OS_nw_protocol_options>"8ls32l8
- __unnamed_array_storage.184
- __unnamed_array_storage.199
- _nw_protocol_options_copy_definition
- _nw_protocol_stack_iterate_application_protocols
CStrings:
+ "%s:%u - [Staging] Configuration URL: %@"
+ "%s:%u - [Staging] Got configuration: %@"
+ "HTTP2ParametersForServer"
+ "HTTP3ParametersForServer"
+ "T@\"NSString\",?,R,C"
+ "setCommmonParameters:"
- "%s:%u - Configuration URL: %@"
- "%s:%u - Got configuration: %@"

```
