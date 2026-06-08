## libdns_services.dylib

> `/usr/lib/libdns_services.dylib`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0xdce4
-  __TEXT.__auth_stubs: 0x5f0
+3066.0.0.502.1
+  __TEXT.__text: 0xdec0
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0xea0
-  __TEXT.__cstring: 0x11d8
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0x15b
-  __TEXT.__objc_methtype: 0xb5
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x590
+  __TEXT.__oslogstring: 0xed1
+  __TEXT.__cstring: 0x1320
+  __TEXT.__unwind_info: 0x220
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x600
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_const: 0x508
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 018A492A-874F-3F60-A80D-6BAEC8A26DC4
-  Functions: 187
-  Symbols:   500
-  CStrings:  327
+  UUID: 319B6B68-CF75-37EB-AD00-519BFB464714
+  Functions: 198
+  Symbols:   519
+  CStrings:  293
 
Symbols:
+ ____dnssd_getaddrinfo_result_create_svcb_block_invoke_4
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.21
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.3.147
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.329
+ ___block_descriptor_tmp.4.151
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.5.154
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.6.157
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.86
+ ___block_descriptor_tmp.87
+ ___block_literal_global.19
+ ___block_literal_global.23
+ ___block_literal_global.62
+ ___block_literal_global.71
+ ___dnssd_getaddrinfo_result_enumerate_tls_supported_groups_block_invoke
+ ___dnssd_svcb_access_tls_supported_groups_block_invoke
+ _adv_hints_dump_callback
+ _adv_hints_erase_callback
+ _advertising_proxy_add_pref64_prefix
+ _advertising_proxy_disable_srp_compression
+ _advertising_proxy_dump_hints_database
+ _advertising_proxy_enable_srp_compression
+ _advertising_proxy_erase_hints_database
+ _advertising_proxy_remove_pref64_prefix
+ _advertising_proxy_set_query_jitter
+ _dnssd_getaddrinfo_result_enumerate_tls_supported_groups
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.20
- ___block_descriptor_tmp.24
- ___block_descriptor_tmp.3.135
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.314
- ___block_descriptor_tmp.4.139
- ___block_descriptor_tmp.47
- ___block_descriptor_tmp.49
- ___block_descriptor_tmp.5.142
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.63
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.76
- ___block_literal_global.18
- ___block_literal_global.22
- ___block_literal_global.59
- ___block_literal_global.68
- _advertising_proxy_add_nat64_prefix
- _advertising_proxy_remove_nat64_prefix
CStrings:
+ "B12@?0S8"
+ "add pref64 prefix"
+ "adv_erase_hints_callback: error response code %d"
+ "advertising_proxy_add_pref64_prefix"
+ "advertising_proxy_disable_srp_compression"
+ "advertising_proxy_dump_hints_database"
+ "advertising_proxy_enable_srp_compression"
+ "advertising_proxy_erase_hints_database"
+ "advertising_proxy_remove_pref64_prefix"
+ "advertising_proxy_set_query_jitter"
+ "disable srp compression"
+ "dump hints database"
+ "enable srp compression"
+ "erase hints database"
+ "jitter_seconds"
+ "remove pref64 prefix"
+ "set query jitter"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "OS_dnssd_cname_array"
- "OS_dnssd_getaddrinfo"
- "OS_dnssd_getaddrinfo_result"
- "OS_dnssd_object"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "add nat64 prefix"
- "advertising_proxy_add_nat64_prefix"
- "advertising_proxy_remove_nat64_prefix"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "descriptions"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "redactedDescription"
- "release"
- "remove nat64 prefix"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@0:8"
- "zone"

```
