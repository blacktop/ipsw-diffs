## libdns_services.dylib

> `/usr/lib/libdns_services.dylib`

```diff

-2600.120.12.0.0
-  __TEXT.__text: 0xc720
-  __TEXT.__auth_stubs: 0x5e0
+2862.0.0.0.1
+  __TEXT.__text: 0xd3e4
+  __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0xc3a
-  __TEXT.__cstring: 0xf03
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__oslogstring: 0xe44
+  __TEXT.__cstring: 0x10e7
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x6c
   __TEXT.__objc_methname: 0x15b
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__const: 0x590
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_const: 0x508
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__objc_superrefs: 0x8
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0A88A0A-88BE-3875-B169-577FE18F38A1
-  Functions: 170
-  Symbols:   471
-  CStrings:  289
+  UUID: 04386295-D74A-32EF-819B-ECBE644E4E36
+  Functions: 182
+  Symbols:   493
+  CStrings:  322
 
Symbols:
+ ____dnssd_getaddrinfo_result_create_svcb_block_invoke_3
+ ___block_descriptor_tmp.10
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.16
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.3.135
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.311
+ ___block_descriptor_tmp.4.139
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.5.142
+ ___block_descriptor_tmp.55
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.76
+ ___block_literal_global.18
+ ___block_literal_global.22
+ ___block_literal_global.59
+ ___block_literal_global.68
+ ___dnssd_getaddrinfo_result_enumerate_sla_values_block_invoke
+ ___dnssd_svcb_access_sla_values_block_invoke
+ _adv_host_allocate_
+ _adv_host_service_get_callback
+ _advertising_proxy_block_interface
+ _advertising_proxy_block_unblock_interface
+ _advertising_proxy_continue_apple_service
+ _advertising_proxy_get_host_service
+ _advertising_proxy_stop_apple_service
+ _advertising_proxy_unblock_interface
+ _dnssd_getaddrinfo_result_enumerate_sla_values
+ _xpc_array_set_int64
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.281
- ___block_descriptor_tmp.3.125
- ___block_descriptor_tmp.30
- ___block_descriptor_tmp.4.129
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.50
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.59
- ___block_descriptor_tmp.60
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.96
- ___block_literal_global.17
- ___block_literal_global.21
- ___block_literal_global.56
- ___block_literal_global.65
CStrings:
+ "%{public}s: \"strict_calloc called with count 0\""
+ "%{public}s: \"strict_calloc count * size would overflow\""
+ "%{public}s: \"strict_calloc(%zu, %zu) failed\""
+ "%{public}s: strdup() failed"
+ "%{public}s: strict allocator failed"
+ "%{public}s: strict_calloc called with count 0"
+ "%{public}s: strict_calloc count * size would overflow"
+ "%{public}s: strict_calloc(%zu, %zu) failed"
+ "%{public}s: strict_malloc called with size 0"
+ "B12@?0C8"
+ "address"
+ "adv_host_service_get_callback"
+ "adv_host_service_get_callback: No registered services."
+ "adv_host_service_get_callback: Non-error response host value is not an array"
+ "adv_host_service_get_callback: Non-error response instances value is not an array"
+ "adv_host_service_get_callback: error response code %d"
+ "adv_host_service_get_callback: lookup error %d in response"
+ "adv_host_service_get_callback: non-error response doesn't contain a host key"
+ "adv_host_service_get_callback: non-error response doesn't contain an instances key"
+ "adv_host_service_get_callback: regname or hostname not provided"
+ "adv_host_service_get_callback: services array[%zu] is not a dictionary"
+ "adv_host_service_get_callback: too many addresses: %zu"
+ "advertising_proxy_block_interface"
+ "advertising_proxy_continue_apple_service"
+ "advertising_proxy_get_host_service"
+ "advertising_proxy_set_variable"
+ "advertising_proxy_stop_apple_service"
+ "advertising_proxy_unblock_interface"
+ "block interface"
+ "continue apple service"
+ "error_code"
+ "get host service info"
+ "host_name"
+ "instance_name"
+ "interface"
+ "lease_time"
+ "num_addresses"
+ "num_instances"
+ "service_type"
+ "status_bitmap"
+ "stop apple service"
+ "strict_strdup"
+ "unblock interface"
- "%{public}s: \"no memory for %zu subscribers\""
- "%{public}s: \"no memory for domain %{private}s . %{public}s\""
- "%{public}s: \"no memory for name %{private}s . %{public}s\""
- "%{public}s: \"no memory for service state %{public}s\""
- "%{public}s: \"no memory for service type %{private}s . %{public}s\""
- "%{public}s: \"no memory for service_type %{public}s\""
- "%{public}s: \"no memory for state %{private}s . %{public}s\""
- "adv_ctl_list_callback: no memory for host object"
- "adv_service_list_callback: no memory for address object."
- "adv_service_list_callback: no memory for instance object."

```
