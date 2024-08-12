## Network

> `/System/Library/Frameworks/Network.framework/Network`

```diff

-4277.0.153.0.7
-  __TEXT.__text: 0xc50f28
+4277.2.5.0.0
+  __TEXT.__text: 0xc51784
   __TEXT.__auth_stubs: 0x5c20
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0xb90
   __TEXT.__init_offsets: 0x5a8
   __TEXT.__objc_methlist: 0x788c
   __TEXT.__const: 0xcf250
-  __TEXT.__cstring: 0x5c795
+  __TEXT.__cstring: 0x5c7af
   __TEXT.__swift5_typeref: 0x36c0
   __TEXT.__swift5_capture: 0x19d0
   __TEXT.__swift5_reflstr: 0x2408

   __TEXT.__swift5_proto: 0x6ec
   __TEXT.__swift5_types: 0x440
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__oslogstring: 0x11e8c0
-  __TEXT.__gcc_except_tab: 0x8a8cc
-  __TEXT.__unwind_info: 0x180e8
+  __TEXT.__oslogstring: 0x11ea81
+  __TEXT.__gcc_except_tab: 0x8a93c
+  __TEXT.__unwind_info: 0x18108
   __TEXT.__eh_frame: 0x620c
   __TEXT.__objc_classname: 0x2307
   __TEXT.__objc_methname: 0x13d70
-  __TEXT.__objc_methtype: 0x8ff0
+  __TEXT.__objc_methtype: 0x9004
   __TEXT.__objc_stubs: 0x9a60
   __DATA_CONST.__got: 0xda0
-  __DATA_CONST.__const: 0x12620
+  __DATA_CONST.__const: 0x12640
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x4d0

   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x6b8
   __AUTH_CONST.__auth_got: 0x2ec8
-  __AUTH_CONST.__auth_ptr: 0x1028
-  __AUTH_CONST.__const: 0xc798
+  __AUTH_CONST.__auth_ptr: 0xf80
+  __AUTH_CONST.__const: 0xc7b8
   __AUTH_CONST.__cfstring: 0x80a0
   __AUTH_CONST.__objc_const: 0x26a58
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21149
-  Symbols:   15211
-  CStrings:  32602
+  Functions: 21154
+  Symbols:   15216
+  CStrings:  32608
 
CStrings:
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] Already servicing writes, ignoring..."
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING)"
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING), backtrace limit exceeded"
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING), dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING), no backtrace"
+ "-[NWURLLoaderHTTP readResponse]"
+ "4277.2.5"
+ "{nw_flow_protocol=\"protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"listen_protocol\"{nw_listen_protocol=\"callbacks\"^{nw_listen_protocol_callbacks}\"protocol_handler\"^{nw_protocol}\"protocol_handler_context\"^v\"handle\"^v}\"replay_protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"handler\"@\"NWConcrete_nw_endpoint_handler\"\"retained_flow\"@\"NWConcrete_nw_endpoint_flow\"\"parameters\"@\"NSObject<OS_nw_parameters>\"\"context\"@\"NSObject<OS_nw_context>\"\"write_requests\"@\"NSObject<OS_nw_write_request>\"\"initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"cloned_initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"read_requests\"@\"NSObject<OS_nw_read_request>\"\"last_output_context\"@\"NSObject<OS_nw_content_context>\"\"metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"input_metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"output_context\"@\"NSObject<OS_nw_content_context>\"\"input_contexts\"@\"NSObject<OS_nw_dictionary>\"\"single_input_context\"@\"NSObject<OS_nw_content_context>\"\"pending_input_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"candidate_output_handlers\"^{nw_hash_table}\"fast_open_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"final_read_list\"@\"NSObject<OS_nw_array>\"\"last_error\"@\"NSObject<OS_nw_error>\"\"fast_open_frame_finalized_count\"I\"initialized\"b1\"last_output_context_pending\"b1\"servicing_reads\"b1\"servicing_writes\"b1\"input_finished\"b1\"waiting_for_initial_read\"b1\"deferred_final_read\"b1\"delivered_final_read\"b1\"flow_unregistered\"b1\"flow_disconnected\"b1\"waiting_for_connected\"b1\"in_fast_open\"b1\"unused\"b4\"__pad\"[2C]}"
- "4277.0.153.0.7"
- "{nw_flow_protocol=\"protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"listen_protocol\"{nw_listen_protocol=\"callbacks\"^{nw_listen_protocol_callbacks}\"protocol_handler\"^{nw_protocol}\"protocol_handler_context\"^v\"handle\"^v}\"replay_protocol\"{nw_protocol=\"flow_id\"[16C]\"identifier\"^{nw_protocol_identifier}\"callbacks\"^{nw_protocol_callbacks}\"output_handler\"^{nw_protocol}\"handle\"^v\"default_input_handler\"^{nw_protocol}\"output_handler_context\"^v}\"handler\"@\"NWConcrete_nw_endpoint_handler\"\"retained_flow\"@\"NWConcrete_nw_endpoint_flow\"\"parameters\"@\"NSObject<OS_nw_parameters>\"\"context\"@\"NSObject<OS_nw_context>\"\"write_requests\"@\"NSObject<OS_nw_write_request>\"\"initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"cloned_initial_write_requests\"@\"NSObject<OS_nw_write_request>\"\"read_requests\"@\"NSObject<OS_nw_read_request>\"\"last_output_context\"@\"NSObject<OS_nw_content_context>\"\"metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"input_metadata\"@\"NSObject<OS_nw_protocol_metadata>\"\"output_context\"@\"NSObject<OS_nw_content_context>\"\"input_contexts\"@\"NSObject<OS_nw_dictionary>\"\"single_input_context\"@\"NSObject<OS_nw_content_context>\"\"pending_input_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"candidate_output_handlers\"^{nw_hash_table}\"fast_open_frames\"{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}\"final_read_list\"@\"NSObject<OS_nw_array>\"\"last_error\"@\"NSObject<OS_nw_error>\"\"fast_open_frame_finalized_count\"I\"initialized\"b1\"last_output_context_pending\"b1\"servicing_reads\"b1\"input_finished\"b1\"waiting_for_initial_read\"b1\"deferred_final_read\"b1\"delivered_final_read\"b1\"flow_unregistered\"b1\"flow_disconnected\"b1\"waiting_for_connected\"b1\"in_fast_open\"b1\"unused\"b5\"__pad\"[2C]}"

```
