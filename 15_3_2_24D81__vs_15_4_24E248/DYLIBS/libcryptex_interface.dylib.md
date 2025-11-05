## libcryptex_interface.dylib

> `/usr/lib/libcryptex_interface.dylib`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x7a00
-  __TEXT.__auth_stubs: 0x730
+493.101.1.0.0
+  __TEXT.__text: 0x7cc0
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0xb80
-  __TEXT.__oslogstring: 0x900
-  __TEXT.__gcc_except_tab: 0x35c
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__const: 0x160
+  __TEXT.__cstring: 0xc79
+  __TEXT.__oslogstring: 0x91c
+  __TEXT.__gcc_except_tab: 0x374
+  __TEXT.__unwind_info: 0x278
   __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methname: 0x21f
   __TEXT.__objc_methtype: 0x9a
   __TEXT.__objc_stubs: 0x1e0
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__const: 0x2d0
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x1f0
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2E3F069-5EA2-3317-9327-4A348CC63B1B
-  Functions: 172
-  Symbols:   420
-  CStrings:  212
+  UUID: BBCE5CE7-4AA0-37A3-A878-A84A26BBC586
+  Functions: 181
+  Symbols:   437
+  CStrings:  221
 
Symbols:
+ +[UpgradeInterfaceLock getSharedInstance].cold.1
+ _CFCreateAssertImpl.cold.1
+ _CFRetain
+ __CFCreateAssertImpl
+ __CFErrorCopyTopLevelErrorWithDomain
+ __CFErrorIterUnderlying
+ ____CFErrorCopyTopLevelErrorWithDomain_block_invoke
+ ___copy_helper_block_8_32r
+ ___destroy_helper_block_8_32r
+ _codex_interface_create_uninstall_request
+ _mnt_intf_log.cold.1
+ _rsi_log.cold.1
+ _xpc_dictionary_key_with_type_exists.cold.1
+ _xpc_dictionary_key_with_type_exists.cold.2
+ _xpc_dictionary_to_cferr.cold.1
+ _xpc_dictionary_to_cferr.cold.2
+ _xpc_dictionary_to_cferr.cold.3
+ _xpc_dictionary_to_cferr.cold.4
+ _xpc_dictionary_to_cferr.cold.5
+ _xpc_dictionary_to_cferr.cold.6
+ collation_xpc_get_queue.cold.1
+ cryptex_trampoline_upgrade_interface_wait.cold.1
+ cryptex_upgrade_abort_osl.cold.1
+ cryptex_upgrade_interface_abort.cold.1
+ cryptex_upgrade_trampoline_osl.cold.1
- _CFDictionaryCreateMutableForCFTypes.cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __CFDictionaryCreateMutableForCFTypes
- _cryptex_subsystem_cryptex
- _cryptex_uninstall_pack
- _cryptex_uninstall_reply_pack
- _cryptex_uninstall_reply_unpack
- _cryptex_uninstall_unpack
CStrings:
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_interface"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/codex_xpc_interface.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/mount_interface.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/remote_service_interface.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/upgrade_abort_interface.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/upgrade_lock_interface.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/util/rpc.c"
+ "493.101.1"
+ "@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Mon Mar 10 20:53:27 PDT 2025; root:libcryptex-493.101.1~2/libcryptex_interface/RELEASE_ARM64E"
+ "B16@?0^{__CFError=}8"
+ "CODEX"
+ "CODEX_SUB_REQ"
+ "Cryptex IPC Interface Version 2.0.0: Mon Mar 10 20:53:27 PDT 2025; root:libcryptex-493.101.1~2/libcryptex_interface/RELEASE_ARM64E"
+ "Invalid cryptex identifier."
+ "UNINSTALL"
+ "UNINSTALL:CXID"
+ "UNINSTALL:CXVER"
+ "UNINSTALL:FORCE_UNMOUNT"
+ "codex_interface_create_uninstall_request"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_interface"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/mount_interface.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/remote_service_interface.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/upgrade_abort_interface.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/interface/upgrade_lock_interface.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/util/rpc.c"
- "475.80.3"
- "@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Thu Dec 19 22:10:14 PST 2024; root:libcryptex-475.80.3~207/libcryptex_interface/RELEASE_ARM64E"
- "Cryptex IPC Interface Version 2.0.0: Thu Dec 19 22:10:14 PST 2024; root:libcryptex-475.80.3~207/libcryptex_interface/RELEASE_ARM64E"
- "com.apple.security.libcryptex.interface.cryptex"

```
