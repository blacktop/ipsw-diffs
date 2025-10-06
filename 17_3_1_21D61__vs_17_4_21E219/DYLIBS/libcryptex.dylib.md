## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-369.60.3.0.0
-  __TEXT.__text: 0x22d0c
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_methlist: 0x468
-  __TEXT.__const: 0x6cd
-  __TEXT.__gcc_except_tab: 0x5e4
-  __TEXT.__oslogstring: 0x36c2
-  __TEXT.__cstring: 0x179f
-  __TEXT.__unwind_info: 0x538
+369.100.36.0.0
+  __TEXT.__text: 0x25f6c
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_methlist: 0x490
+  __TEXT.__const: 0x6fd
+  __TEXT.__gcc_except_tab: 0xa28
+  __TEXT.__oslogstring: 0x36c3
+  __TEXT.__cstring: 0x1b2c
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_classname: 0x140
-  __TEXT.__objc_methname: 0x999
-  __TEXT.__objc_methtype: 0x327
-  __TEXT.__objc_stubs: 0x9e0
+  __TEXT.__objc_methname: 0x9e7
+  __TEXT.__objc_methtype: 0x360
+  __TEXT.__objc_stubs: 0xa40
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_nlclslist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x968
-  __DATA_CONST.__objc_selrefs: 0x2b0
+  __DATA_CONST.__objc_const: 0x998
+  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_classrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__objc_const: 0x480
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x980
+  __AUTH_CONST.__auth_got: 0x9b0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_classrefs: 0xc8
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x98
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib
   - /usr/lib/libcryptex_interface.dylib
-  - /usr/lib/libimg4.dylib
+  - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB5D6066-B3DD-3C84-B214-98950C9C696A
-  Functions: 549
-  Symbols:   1638
-  CStrings:  773
+  UUID: F87E7DED-09A5-38E9-9719-94AC8B1EAAFA
+  Functions: 567
+  Symbols:   1686
+  CStrings:  823
 
Symbols:
+ -[CryptexRemoteService supportsFeature:]
+ -[CryptexRemoteServiceNonceAttr ndom_handle]
+ -[CryptexRemoteServiceNonceAttr ndom_handle].cold.1
+ -[CryptexRemoteServiceNonceAttr setNdom_handle:]
+ GCC_except_table1
+ GCC_except_table15
+ GCC_except_table40
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ _OBJC_IVAR_$_CryptexRemoteServiceNonceAttr._ndom_handle
+ ___block_descriptor_tmp.20
+ ___block_literal_global.156
+ ___cryptex_remote_service_copy_device_identifier2_block_invoke
+ ___cryptex_remote_service_copy_installed2_block_invoke
+ ___cryptex_remote_service_copy_installed2_block_invoke.152
+ ___cryptex_remote_service_copy_nonce2_block_invoke
+ ___cryptex_remote_service_install2_block_invoke
+ ___cryptex_remote_service_roll_nonce2_block_invoke
+ ___cryptex_remote_service_uninstall2_block_invoke
+ __xpc_reply_get_cferr
+ _cryptex_core_get_nonce_domain_handle
+ _cryptex_remote_service_copy_device_identifier2
+ _cryptex_remote_service_copy_device_identifier2.cold.1
+ _cryptex_remote_service_copy_device_identifier2.cold.2
+ _cryptex_remote_service_copy_installed2
+ _cryptex_remote_service_copy_installed2.cold.1
+ _cryptex_remote_service_copy_installed2.cold.2
+ _cryptex_remote_service_copy_nonce2
+ _cryptex_remote_service_copy_nonce2.cold.1
+ _cryptex_remote_service_copy_nonce2.cold.2
+ _cryptex_remote_service_copy_nonce2.cold.3
+ _cryptex_remote_service_install2
+ _cryptex_remote_service_install2.cold.1
+ _cryptex_remote_service_install2.cold.2
+ _cryptex_remote_service_install2.cold.3
+ _cryptex_remote_service_install2.cold.4
+ _cryptex_remote_service_nonce_attr_set_cryptex
+ _cryptex_remote_service_nonce_attr_set_cryptex.cold.1
+ _cryptex_remote_service_nonce_attr_set_cryptex.cold.2
+ _cryptex_remote_service_nonce_attr_set_cryptex.cold.3
+ _cryptex_remote_service_roll_nonce2
+ _cryptex_remote_service_roll_nonce2.cold.1
+ _cryptex_remote_service_roll_nonce2.cold.2
+ _cryptex_remote_service_supports_feature
+ _cryptex_remote_service_uninstall2
+ _cryptex_remote_service_uninstall2.cold.1
+ _cryptex_remote_service_uninstall2.cold.2
+ _img4_chip_instance_from_xpc
+ _objc_msgSend$ndom_handle
+ _objc_msgSend$setNdom_handle:
+ _objc_msgSend$supportsFeature:
+ _objc_retain_x23
+ _objc_retain_x27
+ _remote_service_create_nonce_handle_request
+ _remote_service_create_nonce_index_request
+ _remote_service_create_personalization_identifiers_request
+ _remote_service_create_roll_nonce_handle_request
+ _remote_service_create_roll_nonce_index_request
+ _remote_service_supports_feature
- -[CryptexRemoteService initService].cold.2
- GCC_except_table43
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table53
- ___block_literal_global.141
- ___cryptex_remote_service_copy_installed_block_invoke
- ___cryptex_remote_service_copy_installed_block_invoke.137
- ___cryptex_remote_service_copy_nonce_block_invoke
- ___cryptex_remote_service_install_block_invoke
- ___cryptex_remote_service_roll_nonce_block_invoke
- ___cryptex_remote_service_uninstall_block_invoke
- _cryptex_remote_service_copy_device_identifier.cold.1
- _cryptex_remote_service_copy_device_identifier.cold.2
- _cryptex_remote_service_copy_installed.cold.1
- _cryptex_remote_service_copy_installed.cold.2
- _cryptex_remote_service_copy_nonce.cold.1
- _cryptex_remote_service_copy_nonce.cold.2
- _cryptex_remote_service_copy_nonce.cold.3
- _cryptex_remote_service_install.cold.1
- _cryptex_remote_service_install.cold.2
- _cryptex_remote_service_install.cold.3
- _cryptex_remote_service_install.cold.4
- _cryptex_remote_service_roll_nonce.cold.1
- _cryptex_remote_service_roll_nonce.cold.2
- _cryptex_remote_service_uninstall.cold.1
- _cryptex_remote_service_uninstall.cold.2
- _objc_retain_x26
- _remote_service_create_nonce_request
- _remote_service_create_roll_nonce_request
CStrings:
+ "-[CryptexRemoteService initService]"
+ "-[CryptexRemoteService sendRequestSync:response:]"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex/hlutil/img4_xpc.m"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex/src/remote_service.m"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex/util/xpc.c"
+ "369.100.36"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Wed Feb 21 20:36:21 PST 2024; root:libcryptex-369.100.36~293/libcryptex/RELEASE_ARM64E"
+ "B24@0:8r*16"
+ "Darwin Cryptex Interface Version 2.0.0: Wed Feb 21 20:36:21 PST 2024; root:libcryptex-369.100.36~293/libcryptex/RELEASE_ARM64E"
+ "Failed to read identifiers from remote device properties."
+ "I"
+ "I16@0:8"
+ "Invalid chip instance XPC object."
+ "Invalid value (%llu) for key: %s"
+ "Missing key: %s"
+ "POSIX error from cryptexd. %{darwin.errno}d"
+ "ReadIdentifiers"
+ "RemoteXPC error: %s"
+ "TI,N,V_ndom_handle"
+ "^{__CFError=}16@0:8"
+ "^{__CFError=}32@0:8@16^@24"
+ "_cryptex_remote_service_copy_device_identifier_from_rsd"
+ "_ndom_handle"
+ "_xpc_reply_get_cferr"
+ "cannot fetch remote device properties"
+ "cferr"
+ "cryptex doesn't contain im4m"
+ "cryptex doesn't contain image asset"
+ "cryptex doesn't contain trust cache"
+ "cryptex remote service not found on remote device %{darwin.errno}d"
+ "cryptex_remote_service_copy_device_identifier2"
+ "cryptex_remote_service_copy_installed2"
+ "cryptex_remote_service_copy_nonce2"
+ "cryptex_remote_service_install2"
+ "failed to create chip instance from remote device %{darwin.errno}d"
+ "failed to create remote service install request: %@"
+ "failed to decode AppleImage4 chip instance.: %@"
+ "failed to init service: %@"
+ "img4_chip_bord"
+ "img4_chip_cepo"
+ "img4_chip_chip"
+ "img4_chip_clas"
+ "img4_chip_cpro"
+ "img4_chip_csec"
+ "img4_chip_ecid"
+ "img4_chip_epro"
+ "img4_chip_esdm"
+ "img4_chip_esec"
+ "img4_chip_euou"
+ "img4_chip_fchp"
+ "img4_chip_fpgt"
+ "img4_chip_instance_from_xpc"
+ "img4_chip_iuou"
+ "img4_chip_omit"
+ "img4_chip_rsch"
+ "img4_chip_sdom"
+ "img4_chip_styp"
+ "img4_chip_type"
+ "malformed response: cannot fetch error"
+ "malformed response: cannot fetch response"
+ "ndom_handle"
+ "personalization identifier request failed: %@"
+ "received a nonce with different version: %d"
+ "remote device %s disconnected"
+ "remote device has disconnected %{darwin.errno}d"
+ "remote service copy nonce request failed: %@"
+ "remote service install request failed: %@"
+ "remote service install response doesn't have key %s"
+ "remote service roll nonce request failed: %@"
+ "remote service uninstall request failed: %@"
+ "routine error"
+ "setNdom_handle:"
+ "supportsFeature:"
+ "unexpected failure: Failed to read NonceDomain handle."
+ "unknown error %{darwin.errno}d"
+ "v20@0:8I16"
- "369.60.3"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Wed Dec 20 22:36:16 PST 2023; root:libcryptex-369.60.3~536/libcryptex/RELEASE_ARM64E"
- "Darwin Cryptex Interface Version 2.0.0: Wed Dec 20 22:36:16 PST 2023; root:libcryptex-369.60.3~536/libcryptex/RELEASE_ARM64E"
- "cannot fetch remote device properties: %{darwin.errno}d"
- "cryptex doesn't contain im4m: %{darwin.errno}d"
- "cryptex doesn't contain image asset: %{darwin.errno}d"
- "cryptex doesn't contain trust cache: %{darwin.errno}d"
- "cryptex remote service not found on remote device"
- "failed to create chip instance from remote device: %{darwin.errno}d"
- "failed to create remote service install request: %{darwin.errno}d"
- "failed to init service: %{darwin.errno}d"
- "i16@0:8"
- "i32@0:8@16^@24"
- "malformed response: cannot fetch error: %{darwin.errno}d"
- "malformed response: cannot fetch response: %{darwin.errno}d"
- "received a nonce with different version: %d: %{darwin.errno}d"
- "received error sending message to remote device: %{darwin.errno}d"
- "remote device %s disconnected: %{darwin.errno}d"
- "remote device has disconnected"
- "remote service copy nonce request failed: %{darwin.errno}d"
- "remote service install request failed: %{darwin.errno}d"
- "remote service install response doesn't have key %s: %{darwin.errno}d"
- "remote service roll nonce request failed: %{darwin.errno}d"
- "remote service uninstall request failed: %{darwin.errno}d"
- "routine error: %{darwin.errno}d"
- "unknown error: %{darwin.errno}d"

```
