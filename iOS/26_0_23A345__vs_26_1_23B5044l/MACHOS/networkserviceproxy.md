## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-906.0.1.0.0
-  __TEXT.__text: 0xb771c
-  __TEXT.__auth_stubs: 0x18d0
-  __TEXT.__objc_stubs: 0xc280
-  __TEXT.__objc_methlist: 0x4dec
+919.0.0.0.0
+  __TEXT.__text: 0xb8044
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_stubs: 0xc300
+  __TEXT.__objc_methlist: 0x4df4
   __TEXT.__const: 0x321
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3f6c
-  __TEXT.__oslogstring: 0xfe65
-  __TEXT.__cstring: 0xcf5d
-  __TEXT.__objc_methname: 0xf3f8
+  __TEXT.__gcc_except_tab: 0x3f7c
+  __TEXT.__oslogstring: 0x10016
+  __TEXT.__cstring: 0xcf88
+  __TEXT.__objc_methname: 0xf45f
   __TEXT.__objc_classname: 0xc7b
-  __TEXT.__objc_methtype: 0x28db
+  __TEXT.__objc_methtype: 0x28ee
   __TEXT.__unwind_info: 0x1880
-  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__auth_got: 0xc88
   __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2040
-  __DATA_CONST.__cfstring: 0x8180
+  __DATA_CONST.__cfstring: 0x81c0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x648
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xad60
-  __DATA.__objc_selrefs: 0x3710
+  __DATA.__objc_const: 0xad68
+  __DATA.__objc_selrefs: 0x3738
   __DATA.__objc_ivar: 0x9bc
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xb48

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 432EF096-ECF0-3842-96C6-F9BCB4ADAC5E
-  Functions: 2078
-  Symbols:   632
-  CStrings:  6997
+  UUID: 4907EDAF-7091-37BE-B821-64CAFF601795
+  Functions: 2081
+  Symbols:   634
+  CStrings:  7020
 
Symbols:
+ _OBJC_CLASS_$_NWEndpoint
+ _nw_endpoint_create_address_from_string
+ _xpc_dictionary_set_uuid
- _ne_privacy_dns_netagent_id
CStrings:
+ "%s called with null (nonce.length == 32)"
+ "%s called with null (nonce.length == 4)"
+ "%s called with null authenticator"
+ "%s called with null nonce"
+ "-[NSPPrivateAccessTokenResponse initWithChallenge:nonce:tokenKey:authenticator:]"
+ "@\"NSUUID\"24@0:8q16"
+ "Failed to get known type (%u), cannot add auxiliary authentication data to cache"
+ "Failed to get known type (%u), cannot fetch auxiliary authentication data from cache"
+ "Got request to fetch an agent UUID for type %d"
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "NSPAgentType"
+ "NSPAgentUUID"
+ "Not running yet, ignoring proxy info update"
+ "Seed"
+ "endpointWithCEndpoint:"
+ "flowRemoteAddress:prefix:"
+ "getAgentUUIDForType:"
+ "ignore platform binary %d"
+ "ignorePlatformBinary"
+ "quota service count changed"
+ "quota services changed"
+ "setIgnorePlatformBinary:"
+ "trusted network discovered proxies changed"
+ "trusted network discovered proxies count changed"
+ "unknown agent type"
- "%s called with null blindSignature"
- "-[NSPPrivateAccessTokenResponse initWithChallenge:clientNonce:tokenKey:blindSignature:]"
- "Failed to get known type, cannot add auxiliary authentication data to cache"
- "Failed to get known type, cannot fetch auxiliary authentication data from cache"
- "initWithUUIDBytes:"

```
