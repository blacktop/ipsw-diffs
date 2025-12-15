## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-2205.62.1.0.0
-  __TEXT.__text: 0x32cac
-  __TEXT.__auth_stubs: 0x1970
+2205.80.6.0.0
+  __TEXT.__text: 0x32cd0
+  __TEXT.__auth_stubs: 0x1be0
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__const: 0x25c
   __TEXT.__cstring: 0x29f9
   __TEXT.__oslogstring: 0x7fa3
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__unwind_info: 0x738
   __TEXT.__objc_classname: 0x53
   __TEXT.__objc_methname: 0x8d6
   __TEXT.__objc_methtype: 0x20e

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH_CONST.__auth_got: 0xdf8
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x548

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DAE4DAC-5F78-394F-A32C-02CAAD649358
+  UUID: 76CB9570-9135-355D-9539-846F6A755F4C
   Functions: 607
-  Symbols:   1768
+  Symbols:   1807
   CStrings:  1188
 
Symbols:
+ _nw_protocol_connect
+ _nw_protocol_connect_is_valid
+ _nw_protocol_connected
+ _nw_protocol_connected_is_valid
+ _nw_protocol_disconnect
+ _nw_protocol_disconnect_is_valid
+ _nw_protocol_disconnected
+ _nw_protocol_disconnected_is_valid
+ _nw_protocol_error
+ _nw_protocol_error_is_valid
+ _nw_protocol_finalize_output_frames
+ _nw_protocol_finalize_output_frames_is_valid
+ _nw_protocol_get_flow_id
+ _nw_protocol_get_input_frames
+ _nw_protocol_get_input_frames_is_valid
+ _nw_protocol_get_input_handler
+ _nw_protocol_get_local_endpoint
+ _nw_protocol_get_output_frames
+ _nw_protocol_get_output_frames_is_valid
+ _nw_protocol_get_output_handler
+ _nw_protocol_get_parameters
+ _nw_protocol_get_path
+ _nw_protocol_get_remote_endpoint
+ _nw_protocol_input_available
+ _nw_protocol_input_available_is_valid
+ _nw_protocol_input_finished
+ _nw_protocol_input_finished_is_valid
+ _nw_protocol_output_available
+ _nw_protocol_output_available_is_valid
+ _nw_protocol_output_finished
+ _nw_protocol_output_finished_is_valid
+ _nw_protocol_remove_input_handler
+ _nw_protocol_remove_input_handler_is_valid
+ _nw_protocol_reset
+ _nw_protocol_reset_is_valid
+ _nw_protocol_set_flow_id_from_protocol
+ _nw_protocol_set_input_handler
+ _nw_protocol_set_output_handler
+ _nw_protocol_upcast
Functions:
~ ___ne_filter_request_xpc_connection_block_invoke.28 : 560 -> 468
~ _nw_filter_protocol_reset : 1468 -> 1440
~ _ne_filter_process_verdict : 3768 -> 3776
~ _ne_filter_protocol_drop_flow : 848 -> 872
~ _ne_filter_protocol_connect : 1736 -> 1740
~ _ne_filter_send_approved_frames : 3032 -> 3040
~ _ne_filter_handle_output_finished : 1292 -> 1296
~ _ne_filter_handle_input_finished : 1516 -> 1524
~ _ne_filter_protocol_input_available : 420 -> 424
~ _ne_filter_cleanup : 816 -> 836
~ _ne_filter_protocol_connected : 472 -> 456
~ _ne_filter_read_from_network : 1224 -> 1236
~ _ne_filter_protocol_output_available : 420 -> 424
~ _ne_filter_protocol_finalize_output_frames : 1856 -> 1860
~ _ne_filter_protocol_get_output_frames : 932 -> 980
~ _ne_filter_protocol_get_input_frames : 4124 -> 4140
~ _ne_filter_protocol_remove_input_handler : 376 -> 408
~ _ne_filter_protocol_add_input_handler : 1700 -> 1676

```
