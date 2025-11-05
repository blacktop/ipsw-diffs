## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x17d28
-  __TEXT.__auth_stubs: 0xd30
+493.101.1.0.0
+  __TEXT.__text: 0x18a64
+  __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x1bc4
-  __TEXT.__oslogstring: 0x2b04
-  __TEXT.__gcc_except_tab: 0x424
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x1e0c
+  __TEXT.__oslogstring: 0x2c40
+  __TEXT.__gcc_except_tab: 0x49c
   __TEXT.__dlopen_cstrs: 0x69
-  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__unwind_info: 0x540
   __TEXT.__objc_classname: 0xcd
   __TEXT.__objc_methname: 0xb69
   __TEXT.__objc_methtype: 0x19b
   __TEXT.__objc_stubs: 0xc00
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xa30
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x368
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x408
-  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__const: 0x428
+  __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x280
-  __DATA.__bss: 0x2a0
+  __DATA.__bss: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcurl.4.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0014DE88-D2C1-33A3-823B-9DCF48EB154C
-  Functions: 437
-  Symbols:   1052
-  CStrings:  787
+  UUID: F1FF2093-D701-397A-9A56-B69A4B1C97A8
+  Functions: 450
+  Symbols:   1076
+  CStrings:  799
 
Symbols:
+ -[CryptexTSS info_content]
+ -[CryptexTSS setInfo_content:]
+ GCC_except_table0
+ GCC_except_table68
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table83
+ OBJC_IVAR_$_CryptexTSS._info_content
+ _CFCreateAssertImpl.cold.1
+ __Block_copy
+ __Block_release
+ __CFCreateAssertImpl
+ ___block_descriptor_44_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16l
+ ___cryptex_magister_authenticate_f_block_invoke
+ ___cryptex_metadata_log_block_invoke
+ ___cryptex_metadata_write_to_file_xattrs_block_invoke
+ ___log_util_block_invoke
+ __cryptex_asset_init_path
+ __cryptex_metadata_keys
+ __digest_file
+ _cryptex_asset_close
+ _cryptex_asset_init_path.cold.1
+ _cryptex_asset_is_open
+ _cryptex_asset_open
+ _cryptex_core_close
+ _cryptex_core_get_num_assets
+ _cryptex_core_metadata_matches
+ _cryptex_core_metadata_matches_xattrs
+ _cryptex_core_open
+ _cryptex_core_select_chip
+ _cryptex_core_write_metadata_to_xattrs
+ _cryptex_magister_authenticate_f
+ _cryptex_metadata_log
+ _cryptex_metadata_read_from_cryptex
+ _cryptex_metadata_read_from_file_xattrs
+ _cryptex_metadata_write_to_file_xattrs
+ _cryptex_system_cryptex_lookup.cold.1
+ _cryptex_tss_set_info_from_file
+ _digest_file.cold.1
+ _digest_file.cold.2
+ _digest_file.cold.3
+ _digest_file.cold.4
+ _digest_file.cold.5
+ _image4_trust_destroy
+ _kAMAuthInstallApParameterSiKA
+ _objc_msgSend$info_content
+ _objc_msgSend$setInfo_content:
+ _open
+ _read_file.cold.2
+ _read_file.cold.3
+ _read_file.cold.4
+ _read_file.cold.5
+ _read_file.cold.6
+ _write_file.cold.1
+ _write_file.cold.2
+ _write_file.cold.3
+ _xpc_equal
+ cryptex_asset_copy.cold.2
+ cryptex_metadata_log.cold.1
+ cryptex_metadata_log.logHandle
+ cryptex_metadata_log.onceToken
+ cryptex_tss_create.cold.1
+ cryptex_tss_set_info_from_file.cold.1
+ log_util.log
+ log_util.onceToken
- -[CryptexTSS c411_content]
- -[CryptexTSS setC411_content:]
- GCC_except_table69
- GCC_except_table75
- GCC_except_table76
- GCC_except_table77
- OBJC_IVAR_$_CryptexTSS._c411_content
- _CFDictionaryCreateMutableForCFTypes.cold.1
- _CFDictionarySetString.cold.1
- _CFDictionarySetUInt32.cold.1
- _CFDictionarySetUInt64.cold.1
- _CFURLCreateFromFileDescriptor.cold.1
- _CFURLCreateFromFileDescriptor.cold.2
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_9
- ___copy_helper_block_8_32r
- ___cryptex_signature_write_metadata_to_file_block_invoke
- ___destroy_helper_block_8_32r
- ___sig_metadata_log_block_invoke
- __cryptex_magister_select_chip
- __cs_metadata_keys
- _cftag.cold.1
- _cftag.cold.2
- _cryptex_asset_generic_stamp.cold.2
- _cryptex_scrivener_init.cold.1
- _cryptex_scrivener_init.cold.2
- _cryptex_scrivener_init_tss_common.cold.2
- _cryptex_scrivener_init_tss_common.cold.3
- _cryptex_scrivener_init_tss_common.cold.4
- _cryptex_scrivener_sign_continue.cold.3
- _cryptex_tss_set_c411_from_file
- _objc_msgSend$c411_content
- _objc_msgSend$setC411_content:
- _signature_metadata_read_from_cryptex
- _signature_metadata_read_from_file
- cryptex_asset_create_generic_digest.cold.1
- cryptex_asset_create_generic_digest.cold.2
- cryptex_asset_create_generic_digest.cold.3
- cryptex_tss_set_c411_from_file.cold.1
- sig_metadata_log.logHandle
- sig_metadata_log.onceToken
CStrings:
+ "%{public}s: Closed all assets from cryptex"
+ "%{public}s: Failed to open asset '%{public}s': %{darwin.errno}d"
+ "%{public}s: Opened all assets from cryptex"
+ "%{public}s: failed to get cryptex metadata %{darwin.errno}d"
+ "%{public}s: failed to read cryptex metadata from %s %{darwin.errno}d"
+ "%{public}s: failed to write cryptex metadata to %s %{darwin.errno}d"
+ "%{public}s: realpath %{darwin.errno}d"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_core"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/core/cryptex_core.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/core/magister.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/core/scrivener.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/core/signature.c"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libcryptex/core/tss.m"
+ "493.101.1"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Mon Mar 10 20:53:44 PDT 2025; root:libcryptex-493.101.1~2/libcryptex_core/RELEASE_ARM64E"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "Darwin Cryptex Core Interface Version 2.0.0: Mon Mar 10 20:53:44 PDT 2025; root:libcryptex-493.101.1~2/libcryptex_core/RELEASE_ARM64E"
+ "Failed to apply xattr '%s'.: %{darwin.errno}d"
+ "Invalid metadata.: %{darwin.errno}d"
+ "T@\"NSData\",&,N,V_info_content"
+ "Unexpected value for cryptex_metadata key '%s': %{darwin.errno}d"
+ "_info_content"
+ "assertion failure: \"buffer != ((void *)0)\" -> %llu"
+ "com.apple.security.cryptex.tatsu"
+ "cryptex_core_metadata_matches"
+ "cryptex_core_metadata_matches_xattrs"
+ "cryptex_core_write_metadata_to_xattrs"
+ "failed to map file into memory: %{darwin.errno}d"
+ "failed to stat file: %{darwin.errno}d"
+ "info_content"
+ "metadata"
+ "realpath_np failed: %{darwin.errno}d"
+ "setInfo_content:"
+ "tss request failed: [%d] %{public}s"
+ "v40@?0^{_cryptex_magister={_cryptex_base={_os_object_header=^vii}Q^{dispatch_queue_s}^{dispatch_queue_s}^?i}{_object_proto=**^{os_log_s}}Q^{_cryptex_core}^{_cryptex_signature}^{_cryptex_host}^{_img4_chip}{_img4_nonce=S[48C]I}}8r^{_cryptex_asset_type=Q^?^?qI**}16^{_buff=(?=**^v^v)(?=Qq)^vQ^v^?^?}24^{__CFError=}32"
- "%{public}s: Failed to apply xattr '%s'.: %{darwin.errno}d"
- "%{public}s: Signature has invalid metadata.: %{darwin.errno}d"
- "%{public}s: Unexpected value for metadata key '%s': %{darwin.errno}d"
- "%{public}s: failed to map asset into memory: %s: %{darwin.errno}d"
- "%{public}s: failed to stat object: %s: %{darwin.errno}d"
- "%{public}s: tss request failed: [%d] %{public}s %{darwin.errno}d"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_core"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/core/magister.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/core/scrivener.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/core/signature.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex/core/tss.m"
- "475.80.3"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Thu Dec 19 22:10:31 PST 2024; root:libcryptex-475.80.3~207/libcryptex_core/RELEASE_ARM64E"
- "B24@?0r*8^v16"
- "Darwin Cryptex Core Interface Version 2.0.0: Thu Dec 19 22:10:31 PST 2024; root:libcryptex-475.80.3~207/libcryptex_core/RELEASE_ARM64E"
- "T@\"NSData\",&,N,V_c411_content"
- "_c411_content"
- "assertion failure: \"buffer != ((void *)0)\" -> %lld"
- "c411_content"
- "http://gs.apple.com"
- "setC411_content:"
- "signature_metadata"

```
