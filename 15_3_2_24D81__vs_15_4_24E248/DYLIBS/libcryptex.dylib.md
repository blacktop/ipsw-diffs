## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x28ce8
-  __TEXT.__auth_stubs: 0x12c0
+493.101.1.0.0
+  __TEXT.__text: 0x28b94
+  __TEXT.__auth_stubs: 0x12b0
   __TEXT.__objc_methlist: 0x490
-  __TEXT.__const: 0x7d5
+  __TEXT.__const: 0x7d8
   __TEXT.__gcc_except_tab: 0xf84
-  __TEXT.__oslogstring: 0x4381
-  __TEXT.__cstring: 0x1e3f
-  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__oslogstring: 0x45d5
+  __TEXT.__cstring: 0x1e46
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x9da
   __TEXT.__objc_methtype: 0x360
   __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_nlclslist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x970
-  __AUTH_CONST.__const: 0x2f0
+  __AUTH_CONST.__auth_got: 0x968
+  __AUTH_CONST.__const: 0x370
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xe18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x98
-  __DATA.__bss: 0x78
+  __DATA.__data: 0x80
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/Versions/A/RemoteXPC
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib
   - /usr/lib/libcryptex_interface.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9B1A771-2D48-314E-965B-F07EE2E4B7A5
-  Functions: 489
-  Symbols:   1269
-  CStrings:  860
+  UUID: 69FDFA94-F9B0-3EA1-9061-172A77FE202A
+  Functions: 493
+  Symbols:   1299
+  CStrings:  872
 
Symbols:
+ +[CryptexEventSubscriber initializeEventStream].cold.1
+ +[CryptexEventSubscriber streamQueue].cold.1
+ +[CryptexEventSubscriber subscribers].cold.1
+ GCC_except_table41
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table72
+ GCC_except_table79
+ _CFCreateAssertImpl.cold.1
+ _OUTLINED_FUNCTION_12
+ __CFCreateAssertImpl
+ __CFErrorCopyTopLevelErrorWithDomain
+ __CFErrorIterUnderlying
+ ____CFErrorCopyTopLevelErrorWithDomain_block_invoke
+ ____CFErrorHasDomainAndCode_block_invoke
+ ___log_util_block_invoke
+ ___xpc_plist_merge_block_invoke.cold.1
+ __block_descriptor_tmp.49
+ __cryptex_bundle_find_cryptexes
+ _codex_interface_create_uninstall_request
+ _cryptex_attr_set_uninstall_flags
+ _cryptex_bundle_find_cryptexes.cold.1
+ _cryptex_bundle_find_cryptexes.cold.2
+ _cryptex_core_close
+ _cryptex_core_get_num_assets
+ _cryptex_core_open
+ _cryptex_core_set_nonce_persistence
+ _cryptex_metadata_read_from_file_xattrs
+ _cryptex_remote_service_nonce_attr_set_ndom_handle
+ _cryptex_tss_set_info_from_file
+ _img4_chip_instance_from_remote_device_properties.cold.1
+ _img4_chip_instance_from_remote_device_properties.cold.10
+ _img4_chip_instance_from_remote_device_properties.cold.2
+ _img4_chip_instance_from_remote_device_properties.cold.3
+ _img4_chip_instance_from_remote_device_properties.cold.4
+ _img4_chip_instance_from_remote_device_properties.cold.5
+ _img4_chip_instance_from_remote_device_properties.cold.6
+ _img4_chip_instance_from_remote_device_properties.cold.7
+ _img4_chip_instance_from_remote_device_properties.cold.8
+ _img4_chip_instance_from_remote_device_properties.cold.9
+ _mount_log.cold.1
+ _read_file.cold.2
+ _read_file.cold.3
+ _read_file.cold.4
+ _read_file.cold.5
+ _read_file.cold.6
+ _remote_service_log.cold.1
+ _simple_session_log.cold.1
+ _write_file.cold.1
+ _write_file.cold.2
+ _write_file.cold.3
+ _xpc_dictionary_key_with_type_exists.cold.1
+ _xpc_dictionary_key_with_type_exists.cold.2
+ _xpc_dictionary_to_cferr.cold.1
+ _xpc_dictionary_to_cferr.cold.2
+ _xpc_dictionary_to_cferr.cold.3
+ _xpc_dictionary_to_cferr.cold.4
+ _xpc_dictionary_to_cferr.cold.5
+ _xpc_dictionary_to_cferr.cold.6
+ cryptex_remote_service_nonce_attr_set_ndom_handle.cold.1
+ log_util.log
+ log_util.onceToken
- GCC_except_table40
- GCC_except_table54
- GCC_except_table56
- GCC_except_table58
- GCC_except_table60
- GCC_except_table62
- GCC_except_table66
- GCC_except_table77
- _CFDictionaryCreateMutableForCFTypes.cold.1
- _DEREncoderAddData
- _DEREncoderAddDataFromEncoderNoCopy
- _DEREncoderAddDataNoCopy
- _DEREncoderCreate
- _DEREncoderCreateEncodedBuffer
- _DEREncoderDestroy
- _OUTLINED_FUNCTION_11
- __CFDictionaryCreateMutableForCFTypes
- __DEREncoderAddDataFromEncoderByEncoding
- __DEREncoderAddEncodedData
- __EncodedDataCreate
- __EncodedDataRelease
- __cryptex_actor_init_invoke_cstr
- __cryptex_uninstall_by_name
- _calloc
- _cryptex_bundle_init.cold.2
- _cryptex_bundle_init.cold.3
- _cryptex_subsystem_cryptex
- _cryptex_tss_set_c411_from_file
- _cryptex_uninstall_pack
- _cryptex_uninstall_reply_unpack
- _kImg4TagStr_IM4P
- _malloc
- _memcmp
- _memmove
- _signature_metadata_read_from_file
- cryptex_array_pack_from_path.cold.3
CStrings:
+ "%{public}s: Build identity %lu (%{public}s) is not a cryptex. Skipping."
+ "%{public}s: Failed to open all cryptex assets"
+ "%{public}s: Performing nonce domain workaround, 0x8 mapped to 0x3"
+ "%{public}s: reading preboot manifest: %s"
+ "%{public}s: setting uninstall flags: %#llx"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/hlutil/img4_xpc.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/bundle.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/cryptex.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/cryptex_mount.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/event.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/remote_service.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/signing_service.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/src/simple_session.m"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/util/xpc.c"
+ "493.101.1"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Mon Mar 10 20:53:58 PDT 2025; root:libcryptex-493.101.1~2/libcryptex/RELEASE_ARM64E"
+ "B16@?0^{__CFError=}8"
+ "Darwin Cryptex Interface Version 2.0.0: Mon Mar 10 20:53:58 PDT 2025; root:libcryptex-493.101.1~2/libcryptex/RELEASE_ARM64E"
+ "Error in response to uninstall request: %{public}@"
+ "Error unpacking uninstall response: %{darwin.errno}d"
+ "Failed to create uninstall request"
+ "Failed to get response to uninstall request."
+ "RemoteXPC error: %{public}s"
+ "UNINSTALL:ERROR_DICT"
+ "Unexpected response to uninstall request: %s"
+ "XPC error in response to uninstall request: %s"
+ "assertion failure: \"dict != ((void *)0)\" -> %llu"
+ "assertion failure: \"matches.count <= 1\" -> %llu"
+ "assertion failure: \"self->service\" -> %llu"
+ "canceling RXPC connection '%{public}@'"
+ "cryptex_uninstall"
+ "establish RXPC connection '%{public}@'"
+ "failed to copy cryptex from bundle [no error]"
+ "failed to copy cryptex from bundle: %@"
+ "got reply: %{public}s"
+ "remote device %{public}s disconnected"
+ "remote service install response doesn't have key '%{public}s'"
+ "sending request: %{public}s"
- "%{public}s: uninstall rpc: %{darwin.errno}d"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/hlutil/img4_xpc.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/bundle.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/cryptex.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/cryptex_mount.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/event.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/remote_service.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/signing_service.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/src/simple_session.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/util/xpc.c"
- "475.80.3"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Thu Dec 19 22:10:48 PST 2024; root:libcryptex-475.80.3~207/libcryptex/RELEASE_ARM64E"
- "Cryptex1,ChipId"
- "Darwin Cryptex Interface Version 2.0.0: Thu Dec 19 22:10:48 PST 2024; root:libcryptex-475.80.3~207/libcryptex/RELEASE_ARM64E"
- "RemoteXPC error: %s"
- "assertion failure: \"dict != ((void *)0)\" -> %lld"
- "assertion failure: \"matches.count <= 1\" -> %lld"
- "assertion failure: \"self->service\" -> %lld"
- "canceling RXPC connection %{public}@"
- "establish RXPC connection %{public}@"
- "failed to copy cryptex from bundle"
- "got reply: %s"
- "remote device %s disconnected"
- "remote service install response doesn't have key %s"
- "sending request: %s"
- "unexpected failure: not implemented"

```
