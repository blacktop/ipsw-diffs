## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-662.120.27.0.0
-  __TEXT.__text: 0x26014
-  __TEXT.__auth_stubs: 0x13c0
+746.0.0.0.0
+  __TEXT.__text: 0x250d4
   __TEXT.__objc_methlist: 0x490
-  __TEXT.__const: 0x7c8
-  __TEXT.__gcc_except_tab: 0xf5c
-  __TEXT.__cstring: 0x1f62
-  __TEXT.__oslogstring: 0x40b0
-  __TEXT.__unwind_info: 0x638
-  __TEXT.__objc_classname: 0x140
-  __TEXT.__objc_methname: 0x9e0
-  __TEXT.__objc_methtype: 0x360
-  __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__const: 0x7b8
+  __TEXT.__gcc_except_tab: 0xc38
+  __TEXT.__cstring: 0x1f58
+  __TEXT.__oslogstring: 0x40f0
+  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_nlclslist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x9f0
+  __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xe18
   __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x9f8
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x30

   - /usr/lib/libcryptex_interface.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C51BD4D8-E10B-3F0A-8D01-98154180F917
-  Functions: 507
-  Symbols:   1792
-  CStrings:  857
+  UUID: 95EA898B-1D63-30A9-85C0-0C68FE823218
+  Functions: 505
+  Symbols:   1790
+  CStrings:  657
 
Symbols:
+ ___block_literal_global.155
+ ___cryptex_remote_service_copy_installed2_block_invoke.151
+ __cryptex_bundle_init.cold.4
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- GCC_except_table75
- ___block_literal_global.156
- ___cryptex_remote_service_copy_installed2_block_invoke.152
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "%{public}s: added %{public}s to ccx_im4m_array"
+ "%{public}s: duplicated cryptex found at [%lu]:\nidentity: %{public}s\nvariant = %{public}s %{darwin.errno}d"
+ "%{public}s: failed to map buffer for file: %{public}s %{darwin.errno}d"
+ "%{public}s: no Signatures found for:\nidentity: %{public}s\nvariant = %{public}s"
+ "746"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Thu May 21 08:14:53 PDT 2026; root:libcryptex-746~413/libcryptex/RELEASE_ARM64E"
+ "Darwin Cryptex Interface Version 2.0.0: Thu May 21 08:14:53 PDT 2026; root:libcryptex-746~413/libcryptex/RELEASE_ARM64E"
+ "Failed to open %{public}s"
+ "XPC error (code %d) in response to session message: %{public}s"
- "%{public}s: added %s to ccx_im4m_array"
- "%{public}s: duplicated cryptex found at [%lu]:\nidentity: %s\nvariant = %s %{darwin.errno}d"
- "%{public}s: failed to map buffer for file: %s %{darwin.errno}d"
- "%{public}s: no Signatures found for:\nidentity: %s\nvariant = %s"
- "*"
- "*16@0:8"
- ".cxx_destruct"
- "662.120.27"
- "@\"CollationCore\""
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSObject<OS_session>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"OS_remote_device\""
- "@\"OS_remote_service\""
- "@\"OS_xpc_remote_connection\""
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Sat Apr 18 17:49:16 PDT 2026; root:libcryptex-662.120.27~92/libcryptex/RELEASE_ARM64E"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8r^{_img4_chip_instance=S^{_img4_chip}QIIIIQBBBBBBBIB{_img4_dgst=SQ[48C]}IIII}16"
- "@24@0:8r^{_img4_nonce=S[48C]I}16"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@40@0:8@16@24Q32"
- "@40@0:8Q16@24@?32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8r*16"
- "Collation"
- "CryptexEventSubscriber"
- "CryptexRemoteDeviceIdentifier"
- "CryptexRemoteObject"
- "CryptexRemoteObjectArray"
- "CryptexRemoteService"
- "CryptexRemoteServiceNonce"
- "CryptexRemoteServiceNonceAttr"
- "Darwin Cryptex Interface Version 2.0.0: Sat Apr 18 17:49:16 PDT 2026; root:libcryptex-662.120.27~92/libcryptex/RELEASE_ARM64E"
- "Failed to open %s"
- "I"
- "I16@0:8"
- "OS_cryptex"
- "OS_cryptex_attr"
- "OS_cryptex_bundle"
- "OS_cryptex_signing_service"
- "OS_cryptex_su_preboot_bundle"
- "OS_session"
- "Q16@0:8"
- "SimpleSession"
- "T*,R,N,V_identifier"
- "T*,R,N,V_version"
- "T@\"CollationCore\",&,N,V_ccore"
- "T@\"NSArray\",R,N,V_array"
- "T@\"NSMutableDictionary\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dq"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_client_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_internal_queue"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "T@\"NSObject<OS_os_log>\",R,N,V_log"
- "T@\"NSObject<OS_session>\",&,V_session"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_client_con"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_endpoint"
- "T@\"NSString\",&,N,V_coll_description"
- "T@\"NSString\",R,N,V_xpcEventName"
- "T@\"OS_remote_device\",R,N,V_device"
- "T@?,C,N,V_callback"
- "TB,N,V_active"
- "TI,N,V_ndom_handle"
- "TQ,N,V_image_type"
- "TQ,N,V_persistence"
- "TQ,R,N,V_flags"
- "T^{_img4_chip_instance=S^{_img4_chip}QIIIIQBBBBBBBIB{_img4_dgst=SQ[48C]}IIII},R,N,V_inst"
- "T^{_img4_nonce=S[48C]I},R,N,V_nonce"
- "UTF8String"
- "XPC error (code %d) in response to session message: %s"
- "^{__CFDictionary=}16@0:8"
- "^{__CFError=}16@0:8"
- "^{__CFError=}32@0:8@16^@24"
- "^{_img4_chip_instance=S^{_img4_chip}QIIIIQBBBBBBBIB{_img4_dgst=SQ[48C]}IIII}"
- "^{_img4_chip_instance=S^{_img4_chip}QIIIIQBBBBBBBIB{_img4_dgst=SQ[48C]}IIII}16@0:8"
- "^{_img4_nonce=S[48C]I}"
- "^{_img4_nonce=S[48C]I}16@0:8"
- "_active"
- "_array"
- "_callback"
- "_ccore"
- "_client_con"
- "_client_queue"
- "_coll_description"
- "_device"
- "_dq"
- "_endpoint"
- "_flags"
- "_handleXPCEvent:"
- "_identifier"
- "_image_type"
- "_inst"
- "_internal_queue"
- "_log"
- "_ndom_handle"
- "_nonce"
- "_persistence"
- "_queue"
- "_session"
- "_version"
- "_xpcEventName"
- "active"
- "addObject:"
- "allKeysForObject:"
- "array"
- "attachToStream:withRegistration:"
- "callback"
- "cancel"
- "ccore"
- "client_con"
- "client_queue"
- "coll_description"
- "connection"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "detachFromStream:"
- "device"
- "dictionaryWithObjects:forKeys:count:"
- "dq"
- "endpoint"
- "enumerateElements:"
- "enumerateObjectsUsingBlock:"
- "firstObject"
- "flags"
- "getID"
- "getNonceDomainIndex"
- "getValidPaths:forBundleID:"
- "getValidPaths:forLabels:"
- "handleXPCEvent:"
- "identifier"
- "image_type"
- "init"
- "initForUser:"
- "initService"
- "initWithArray:"
- "initWithChipInstance:"
- "initWithData:encoding:"
- "initWithDesc:"
- "initWithDevice:queue:flags:"
- "initWithFlags:"
- "initWithFlags:name:"
- "initWithNonce:"
- "initWithSessionCore:"
- "initWithXPC:queue:"
- "initializeEventStream"
- "inst"
- "internal_queue"
- "log"
- "mountPointOfBundleID:"
- "ndom_handle"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "packToXPC"
- "persistence"
- "propertyListWithData:options:format:error:"
- "queue"
- "registerForEvents:onQueue:withCompletion:"
- "remote_conn"
- "removeObjectForKey:"
- "scopeToString:"
- "sendRequestSync:response:"
- "service"
- "setActive:"
- "setCallback:"
- "setCcore:"
- "setClient_con:"
- "setColl_description:"
- "setDq:"
- "setEndpoint:"
- "setImage_type:"
- "setLog:"
- "setNdom_handle:"
- "setObject:forKeyedSubscript:"
- "setPersistence:"
- "setQueue:"
- "setSession:"
- "streamQueue"
- "stringWithUTF8String:"
- "subscribers"
- "supportsFeature:"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "version"
- "xpcEventName"

```
