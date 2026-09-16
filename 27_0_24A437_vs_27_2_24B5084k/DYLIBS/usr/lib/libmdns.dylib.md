## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-3111.0.5.0.1
-  __TEXT.__text: 0x30bf4
+3111.40.40.0.0
+  __TEXT.__text: 0x32384
   __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__cstring: 0x21c9
-  __TEXT.__const: 0x1d0
+  __TEXT.__cstring: 0x22c3
+  __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__oslogstring: 0x38e8
-  __TEXT.__unwind_info: 0xc98
+  __TEXT.__oslogstring: 0x39ca
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2ab8
+  __DATA_CONST.__const: 0x2b48
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x2f0
-  __AUTH_CONST.__const: 0x1380
+  __AUTH_CONST.__const: 0x1480
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x3580
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xf18
+  __AUTH_CONST.__auth_got: 0xf28
   __AUTH.__objc_data: 0xfa0
   __DATA.__data: 0x14b4
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 853
-  Symbols:   2177
-  CStrings:  892
+  Functions: 877
+  Symbols:   2211
+  CStrings:  906
 
Symbols:
+ GCC_except_table229
+ GCC_except_table423
+ GCC_except_table427
+ GCC_except_table700
+ _CFDictionaryApplyFunction
+ _CFDictionaryRemoveAllValues
+ ____mdns_clock_log_block_invoke
+ ____mdns_domain_name_log_block_invoke
+ ____mdns_domain_name_offset_map_copy_description_block_invoke
+ ___mdns_message_builder_write_message_block_invoke
+ __mdns_clock_log.s_log
+ __mdns_clock_log.s_once
+ __mdns_domain_name_log.s_log
+ __mdns_domain_name_log.s_once
+ __mdns_domain_name_offset_map_applier_function
+ __mdns_domain_name_offset_map_copy_description
+ __mdns_domain_name_offset_map_finalize
+ __mdns_domain_name_offset_map_kind
+ __mdns_message_builder_copy_description
+ __mdns_message_builder_finalize
+ __mdns_message_builder_kind
+ __mdns_message_builder_write_record
+ __mdns_pf_create_thread_conn_tracking_rule_dictionary
+ __mdns_resource_record_copy_description
+ __mdns_resource_record_copy_description_bytes
+ __mdns_resource_record_finalize
+ __mdns_resource_record_kind
+ _mdns_clock_uptime_ns
+ _mdns_domain_name_append_to_copier
+ _mdns_domain_name_offset_map_create.key_callbacks
+ _mdns_message_builder_append_answer_record
+ _mdns_message_builder_create
+ _mdns_message_builder_set_aa_bit
+ _mdns_message_builder_set_qr_bit
+ _mdns_message_builder_write_message
+ _mdns_resource_record_create
+ _mdns_resource_record_get_rdata_bytes_ptr
+ _mdns_resource_record_get_rdata_length
- GCC_except_table227
- GCC_except_table415
- GCC_except_table419
- GCC_except_table682
CStrings:
+ "%s\n\t%s: %u"
+ "<NO RDATA>"
+ "B16@?0r^{mdns_resource_record_s=}8"
+ "B20@?0r^{mdns_domain_name_s={mdns_obj_s=^vii^{mdns_kind_s}}*Q*i{os_unfair_lock_s=I}IBB[2c]}8S16"
+ "Failed to create domain name object: %{mdns:err}ld"
+ "Failed to insert domain name offset map pair: %{mdns:err}ld"
+ "PFUserAddRule() for TCP connection tracking failed"
+ "PFUserAddRule() for UDP connection tracking failed"
+ "clock"
+ "clock_gettime_nsec_np(CLOCK_UPTIME_RAW) error: %{mdns:err}d"
+ "domain_name"
+ "mdns_domain_name_offset_map"
+ "mdns_message_builder"
+ "mdns_resource_record"
+ "«NAME»"
- "PFUserAddRule() for connection tracking failed"
```
