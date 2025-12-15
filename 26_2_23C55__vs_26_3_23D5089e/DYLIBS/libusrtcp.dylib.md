## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5569.60.39.0.3
-  __TEXT.__text: 0x5ca8c
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__const: 0x244
+5569.80.33.502.1
+  __TEXT.__text: 0x5ccc8
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__const: 0x24c
   __TEXT.__oslogstring: 0xe713
-  __TEXT.__cstring: 0x1a37
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__cstring: 0x1a3b
+  __TEXT.__unwind_info: 0x460
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x3e8
-  __AUTH_CONST.__auth_got: 0x810
+  __DATA_CONST.__const: 0x410
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH_CONST.__const: 0x1a8
   __AUTH.__data: 0x220
   __DATA.__data: 0x10

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECA1BE40-90E7-310E-8770-51A8EB97703C
-  Functions: 327
-  Symbols:   1009
+  UUID: 1845983F-6019-3ED5-8295-EDC33E4E83EC
+  Functions: 328
+  Symbols:   1013
   CStrings:  1118
 
Symbols:
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.9
+ ___tcp_set_rto_deadline_block_invoke
+ _nw_get_future_time_from
- ___block_descriptor_tmp.10
Functions:
~ _tcp_output : 32864 -> 32780
~ _tcp_ip_output_send : 3092 -> 3396
~ _nw_protocol_tcp_get_frames : 8720 -> 8732
~ _nw_frame_tcp_finalize : 2404 -> 2408
~ _nw_protocol_tcp_get_malloc_frame : 3568 -> 3576
~ ___nw_frame_tcp_finalize_block_invoke : 792 -> 796
~ _nw_tcp_release_frame_array : 2092 -> 2148
+ ___tcp_set_rto_deadline_block_invoke
CStrings:
+ "B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}[16C]QQ^{nw_protocol_metadata}iiCCb2b1b1b1b1b1b1[5C]}ISSCCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b3[1C]}8"
- "B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}[16C]QQ^{nw_protocol_metadata}iiCCb2b1b1b1b1b1b1[5C]}ISSCCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b5[1C]}8"

```
