## configd

> `/usr/libexec/configd`

```diff

-1385.0.0.0.0
-  __TEXT.__text: 0x66c24
-  __TEXT.__auth_stubs: 0x24b0
+1385.0.4.0.0
+  __TEXT.__text: 0x6708c
+  __TEXT.__auth_stubs: 0x24e0
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x2f3d
-  __TEXT.__oslogstring: 0x5430
-  __TEXT.__objc_methname: 0x1a5f
+  __TEXT.__cstring: 0x2f52
+  __TEXT.__oslogstring: 0x5455
+  __TEXT.__objc_methname: 0x1a6b
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methtype: 0x501
   __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__unwind_info: 0x9f0
-  __DATA_CONST.__auth_got: 0x1268
-  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__auth_got: 0x1280
+  __DATA_CONST.__got: 0x6c0
   __DATA_CONST.__auth_ptr: 0x108
   __DATA_CONST.__const: 0x19d0
-  __DATA_CONST.__cfstring: 0x2580
+  __DATA_CONST.__cfstring: 0x25a0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62CF6945-C921-3A64-B46E-4EC5E49D49F9
-  Functions: 929
-  Symbols:   818
-  CStrings:  1948
+  UUID: 53DC78D1-B39F-3047-95DC-8E1735ACA0C6
+  Functions: 930
+  Symbols:   820
+  CStrings:  1952
 
Symbols:
+ _CFDataGetBytes
+ _nw_proxy_config_get_agent_domain
+ _nw_proxy_config_get_system_privacy_proxy_agent_type
- _ne_privacy_proxy_netagent_id
CStrings:
+ "%@: ignoring invalid %@"
+ "%@: using %@"
+ "NetworkSignatureHash"
+ "removeNetworkAgentDomain:agentType:"
- "removeNetworkAgentUUID:"

```
