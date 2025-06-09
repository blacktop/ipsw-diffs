## configd

> `/usr/libexec/configd`

```diff

-1351.120.3.0.0
-  __TEXT.__text: 0x656f8
-  __TEXT.__auth_stubs: 0x2400
-  __TEXT.__objc_stubs: 0x1460
-  __TEXT.__objc_methlist: 0xa4c
-  __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x2f37
-  __TEXT.__oslogstring: 0x530b
-  __TEXT.__objc_methname: 0x19d5
+1385.0.0.0.0
+  __TEXT.__text: 0x66c24
+  __TEXT.__auth_stubs: 0x24b0
+  __TEXT.__objc_stubs: 0x14e0
+  __TEXT.__objc_methlist: 0xa64
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x2f3d
+  __TEXT.__oslogstring: 0x5430
+  __TEXT.__objc_methname: 0x1a5f
   __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methtype: 0x4ef
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__unwind_info: 0x9d0
-  __DATA_CONST.__auth_got: 0x1210
-  __DATA_CONST.__got: 0x6a0
+  __TEXT.__objc_methtype: 0x501
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__unwind_info: 0x9f0
+  __DATA_CONST.__auth_got: 0x1268
+  __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x108
-  __DATA_CONST.__const: 0x19a8
+  __DATA_CONST.__const: 0x19d0
   __DATA_CONST.__cfstring: 0x2580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA.__objc_const: 0xc48
-  __DATA.__objc_selrefs: 0x718
+  __DATA.__objc_selrefs: 0x738
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x104

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/liblockdown.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E743267-30F1-33B5-A53C-86BE93392E9A
-  Functions: 924
-  Symbols:   802
-  CStrings:  1935
+  UUID: 62CF6945-C921-3A64-B46E-4EC5E49D49F9
+  Functions: 929
+  Symbols:   818
+  CStrings:  1948
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _kSCPropNetDNSEncryptedServerAddresses
+ _kSCPropNetDNSEncryptedServerAuthenticationDomainName
+ _kSCPropNetDNSEncryptedServerServiceParameters
+ _kSCPropNetDNSEncryptedServerServicePriority
+ _kSCPropNetDNSEncryptedServers
+ _nw_resolver_config_add_name_server
+ _nw_resolver_config_add_search_domain
+ _nw_resolver_config_copy_plist_data_ref
+ _nw_resolver_config_create
+ _nw_resolver_config_set_class
+ _nw_resolver_config_set_port
+ _nw_resolver_config_set_protocol
+ _nw_resolver_config_set_provider_name
+ _nw_resolver_config_set_provider_path
+ _objc_retainBlock
+ _objc_retain_x4
- _CFAllocatorAllocate
CStrings:
+ "%.*s"
+ "B24@?0r^v8Q16"
+ "B40@0:8r*16Q24@32"
+ "Custom port found in DNR SvcParameters"
+ "DNR ALPN value unsupported"
+ "DNR SvcParameter option length value greater than actual SvcParameter bytes. Skipping."
+ "DNR is configuring DoH resolver"
+ "DNR is configuring DoT resolver"
+ "Encrypted-%@"
+ "Invalid encrypted dns resolver"
+ "Unrecognized DNR SvcParameter key. Skipping."
+ "componentsSeparatedByString:"
+ "dataForEncryptedResolver:"
+ "extractDNRSvcParameterValues:buffer_size:resolverConfig:"
+ "objectAtIndexedSubscript:"
- "NameServers"
- "SearchDomains"

```
