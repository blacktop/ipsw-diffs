## libmrc.dylib

> `/usr/lib/libmrc.dylib`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0x5f90
-  __TEXT.__auth_stubs: 0x570
+3066.0.0.502.1
+  __TEXT.__text: 0x6330
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x723
+  __TEXT.__cstring: 0x70f
+  __TEXT.__const: 0x60
   __TEXT.__oslogstring: 0x26a
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__objc_classname: 0x16b
-  __TEXT.__objc_methname: 0x15b
-  __TEXT.__objc_methtype: 0xb5
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x410
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH_CONST.__const: 0x5c8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__objc_const: 0xf58
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52717038-1871-3C9D-BE3E-ECB0FCCC8F94
-  Functions: 188
-  Symbols:   635
-  CStrings:  189
+  UUID: 51DA5B28-45FD-3F2A-A7B1-56F909145062
+  Functions: 194
+  Symbols:   644
+  CStrings:  131
 
Symbols:
+ ____mdns_siphash_get_per_process_key_block_invoke
+ ___block_descriptor_tmp.359
+ ___block_descriptor_tmp.6
+ ___block_descriptor_tmp.6.238
+ ___block_literal_global
+ ___block_literal_global.332
+ ___block_literal_global.8
+ __mdns_siphash_get_per_process_key.s_siphash_key
+ __mdns_siphash_get_per_process_key.s_siphash_key_once
+ __mdns_siphash_with_key_ex
+ _arc4random_buf
+ _mdns_address_copy_string
+ _mdns_base64_encode_u32_unpadded
+ _mdns_base64_encode_u32_unpadded.base64_charset
+ _mdns_privacy_obfuscate_domain_name_str
+ _mdns_privacy_obfuscate_ipv4_address
+ _mdns_privacy_obfuscate_ipv6_address
+ _mdns_siphash_u32
+ _mdns_string_builder_append_sockaddr
+ _snprintf
- __DNSMessagePrintObfuscatedIPAddress
- __GetCULibHandle.sHandle
- __GetCULibHandle.sOnce
- __GetCUSymAddr_SNPrintF.sAddr
- __GetCUSymAddr_SNPrintF.sOnce
- ____GetCULibHandle_block_invoke
- ____GetCUSymAddr_SNPrintF_block_invoke
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.262
- ___block_descriptor_tmp.371
- ___block_descriptor_tmp.8
- ___block_literal_global.10
- ___block_literal_global.220
- ___block_literal_global.264
- ___block_literal_global.344
- _dlopen
- _dlsym
CStrings:
+ " %s"
+ "%*s"
+ "%s %s"
+ "<dn:%s>"
+ "<ipv4:%s>"
+ "<ipv6:%s>"
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
- "#16@0:8"
- "%#.4a"
- "%.16a"
- "%.4H"
- "%~s"
- "/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils"
- "<IPv4:%s>"
- "<IPv6:%s>"
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
- "OS_mrc_cached_local_records_inquiry"
- "OS_mrc_discovery_proxy"
- "OS_mrc_discovery_proxy_parameters"
- "OS_mrc_dns_proxy"
- "OS_mrc_dns_proxy_parameters"
- "OS_mrc_dns_proxy_state_inquiry"
- "OS_mrc_dns_service_registration"
- "OS_mrc_mdns_address"
- "OS_mrc_mdns_domain_name"
- "OS_mrc_mdns_string_builder"
- "OS_mrc_object"
- "OS_mrc_record_cache_flush"
- "OS_mrc_session"
- "OS_mrc_shared_assist_cache"
- "Q16@0:8"
- "SNPrintF"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
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
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@0:8"
- "zone"
- "«REDACTED»"

```
