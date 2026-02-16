## libmrc.dylib

> `/usr/lib/libmrc.dylib`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0x602c
+2881.100.53.0.0
+  __TEXT.__text: 0x5f90
   __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x14c
   __TEXT.__const: 0x40

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6DCA3440-8BDF-30F4-84A0-AAC2D5FBC229
+  UUID: B386DDBE-CE3C-3DFA-8606-7A5BC9BEFDB1
   Functions: 188
   Symbols:   635
   CStrings:  189
Functions:
~ _mdns_cfarray_enumerate : 144 -> 124
~ _mdns_cfset_enumerate : 308 -> 296
~ _DomainNameFromString : 288 -> 300
~ __mdns_domain_name_equal : 240 -> 232
~ __mdns_domain_name_create : 780 -> 720
~ _mdns_snprintf_add : 148 -> 144
~ __mrc_xpc_dns_proxy_params_print_description : 824 -> 804
~ ____mrc_session_send_stop_message_block_invoke : 524 -> 520
~ ____mrc_session_send_start_message_block_invoke : 736 -> 732
~ _mrc_dns_proxy_parameters_add_input_interface : 224 -> 220
~ _mrc_dns_proxy_parameters_enumerate_input_interfaces : 176 -> 160
~ __mrc_dns_service_registration_handle_notification : 320 -> 316
~ ____mrc_cached_local_records_inquiry_process_create_enhanced_record_info_copy_block_invoke : 848 -> 840
~ __mrc_cached_local_records_inquiry_handle_start : 112 -> 116
~ _mdns_xpc_dictionary_get_int32 : 88 -> 80

```
