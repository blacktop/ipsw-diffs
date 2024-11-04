## Network

> `/System/Library/Frameworks/Network.framework/Network`

```diff

-4277.60.230.502.1
-  __TEXT.__text: 0xc6fd00
+4277.60.249.0.0
+  __TEXT.__text: 0xc735cc
   __TEXT.__auth_stubs: 0x60a0
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0xbb4
   __TEXT.__init_offsets: 0x5a8
   __TEXT.__objc_methlist: 0x78e4
-  __TEXT.__const: 0xd03f8
-  __TEXT.__cstring: 0x5d210
-  __TEXT.__swift5_typeref: 0x3a2e
-  __TEXT.__swift5_capture: 0x1934
+  __TEXT.__const: 0xd0450
+  __TEXT.__cstring: 0x5d5dc
+  __TEXT.__swift5_typeref: 0x3a48
+  __TEXT.__swift5_capture: 0x194c
   __TEXT.__swift5_reflstr: 0x2878
   __TEXT.__swift5_assocty: 0x928
   __TEXT.__constg_swiftt: 0x43ec

   __TEXT.__swift5_proto: 0x7e0
   __TEXT.__swift5_types: 0x484
   __TEXT.__swift5_protos: 0x5c
-  __TEXT.__oslogstring: 0x11f91d
-  __TEXT.__gcc_except_tab: 0x8b440
-  __TEXT.__unwind_info: 0x185d8
-  __TEXT.__eh_frame: 0x630c
-  __TEXT.__objc_classname: 0x2308
-  __TEXT.__objc_methname: 0x1405c
+  __TEXT.__oslogstring: 0x11fca2
+  __TEXT.__gcc_except_tab: 0x8b850
+  __TEXT.__unwind_info: 0x186b8
+  __TEXT.__eh_frame: 0x63a4
+  __TEXT.__objc_classname: 0x2309
+  __TEXT.__objc_methname: 0x140a1
   __TEXT.__objc_methtype: 0x9076
   __TEXT.__objc_stubs: 0x9b80
   __DATA_CONST.__got: 0xdf8
-  __DATA_CONST.__const: 0x127c0
+  __DATA_CONST.__const: 0x12848
   __DATA_CONST.__objc_classlist: 0x978
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x4d0

   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x6b8
   __AUTH_CONST.__auth_got: 0x3108
-  __AUTH_CONST.__auth_ptr: 0x10f8
-  __AUTH_CONST.__const: 0xcb10
+  __AUTH_CONST.__auth_ptr: 0x1000
+  __AUTH_CONST.__const: 0xcb38
   __AUTH_CONST.__cfstring: 0x8020
-  __AUTH_CONST.__objc_const: 0x26eb0
+  __AUTH_CONST.__objc_const: 0x26f10
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x38e0
-  __AUTH.__data: 0x4ec0
-  __DATA.__objc_ivar: 0x2630
-  __DATA.__data: 0x6708
+  __AUTH.__objc_data: 0x3930
+  __AUTH.__data: 0x4ef0
+  __DATA.__objc_ivar: 0x2638
+  __DATA.__data: 0x66c8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x126a0
+  __DATA.__bss: 0x12741
   __DATA.__common: 0x2848
-  __DATA_DIRTY.__objc_data: 0x1090
-  __DATA_DIRTY.__data: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__data: 0x498
   __DATA_DIRTY.__bss: 0xc80
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21556
-  Symbols:   15319
-  CStrings:  32785
+  Functions: 21585
+  Symbols:   15339
+  CStrings:  32826
 
Symbols:
+ _nw_activity_has_global_parent
+ _nw_protocol_options_is_masque_listener
+ _nw_protocol_stack_copy_description
CStrings:
+ "\x162\""
+ "\x17\xf131\x11"
+ " (listener)"
+ "%!{(MISSING)public}s %!{(MISSING)public}s%!s(MISSING)<i%!u(MISSING):c%!u(MISSING):s%!u(MISSING)> extra bytes after a complete response, not allowing reuse"
+ "%!{(MISSING)public}s Cannot join existing protocol %!{(MISSING)public}s, endpoints do not match (%!{(MISSING)public}s != %!{(MISSING)public}s), (original %!{(MISSING)public}s, existing original %!{(MISSING)public}s)"
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] no connected handler, not checking for effective proxy config"
+ "%!{(MISSING)public}s [C%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s %!{(MISSING)public}s %!{(MISSING)public}s (%!{(MISSING)public}@)] no effective proxy config"
+ "%!{(MISSING)public}s called with null listener_uuid"
+ "%!{(MISSING)public}s called with null listener_uuid, backtrace limit exceeded"
+ "%!{(MISSING)public}s called with null listener_uuid, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s called with null listener_uuid, no backtrace"
+ "%!{(MISSING)public}s local port: %!u(MISSING)"
+ "%!{(MISSING)public}s%!s(MISSING)Found lower demux protocol %!p(MISSING), registering options"
+ "%!{(MISSING)public}s%!s(MISSING)added association uuid %!s(MISSING)%!s(MISSING)"
+ "%!{(MISSING)public}s%!s(MISSING)marking connected"
+ "%!{(MISSING)public}s%!s(MISSING)waiting for ACK capsules, not marking ready yet"
+ "4277.60.249"
+ "Global parent activity is immutable and cannot be set to a different activity"
+ "Set activity %!{(MISSING)public}@ as the global parent"
+ "Task <%!{(MISSING)public,uuid_t}.16P>.<%!u(MISSING)> cancelling automatically since the server did not reply to our close frame"
+ "Unset the global parent activity"
+ "Unsetting the global parent activity %!{(MISSING)public}@"
+ "app_intents_services:create_async_iterator"
+ "app_intents_services:fetch_next_async_iterator_results"
+ "app_intents_services:release_async_sequence"
+ "app_intents_services:restart_observing_events"
+ "application [%!u(MISSING)]: %!s(MISSING)\n"
+ "create_async_iterator"
+ "fetch_next_async_iterator_results"
+ "internet [%!u(MISSING)]: %!s(MISSING)\n"
+ "isListenerReady"
+ "listenerReadyContinuations"
+ "mcp_local_port"
+ "mlp_listener_association"
+ "ms_listener_associations_dictionary"
+ "nw_activity_inherit_from_global_parent_if_necessary"
+ "nw_demux_compare_options"
+ "nw_endpoint_resolver_receive_report_block_invoke"
+ "nw_http_encoding_check_http1_content_length"
+ "nw_masque_connection_pair_handle_listener_association_header"
+ "nw_masque_listener_pair_handle_listener_association_header"
+ "nw_masque_server_get_listener_association_port"
+ "nw_masque_server_set_listener_association_port"
+ "nw_parameters_get_listener_uuid"
+ "nw_parameters_set_listener_uuid"
+ "nw_protocol_options_is_masque_listener"
+ "persistent application [%!u(MISSING)]: %!s(MISSING)\n"
+ "publishAndWaitForReady(_:)"
+ "release_async_sequence"
+ "restart_observing_events"
+ "secondary transport [%!u(MISSING)]: %!s(MISSING)\n"
+ "transport [%!u(MISSING)]: %!s(MISSING)\n"
- "\x162!"
- "\x17\xf132"
- "%!{(MISSING)public}s Cannot join existing protocol %!{(MISSING)public}s, endpoints do not match (%!{(MISSING)public}s != %!{(MISSING)public}s)"
- "%!{(MISSING)public}s Connect was not called by endpoint_flow <%!p(MISSING):%!s(MISSING)>"
- "4277.60.230.502.1"
- "Global parent activity is immutable and cannot be set to a different activity."
- "Set activity %!{(MISSING)public}@ as the global parent."
- "Unset the global parent activity."
- "Unsetting the global parent activity %!{(MISSING)public}@."
- "cloned"
- "supportsProtobuf"

```
