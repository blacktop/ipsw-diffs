## securityd_system

> `/usr/libexec/securityd_system`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x40be0
-  __TEXT.__auth_stubs: 0x19d0
+61439.101.1.0.0
+  __TEXT.__text: 0x3c944
+  __TEXT.__auth_stubs: 0x1a20
   __TEXT.__objc_stubs: 0x1600
-  __TEXT.__objc_methlist: 0xbb4
-  __TEXT.__const: 0x62c
-  __TEXT.__cstring: 0x7e7f
+  __TEXT.__objc_methlist: 0xdc0
+  __TEXT.__const: 0x26c
+  __TEXT.__cstring: 0x7a26
   __TEXT.__objc_classname: 0x2be
   __TEXT.__objc_methtype: 0xbb9
   __TEXT.__objc_methname: 0x1cbc
   __TEXT.__oslogstring: 0x367d
   __TEXT.__gcc_except_tab: 0x388
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0xc48
-  __DATA_CONST.__auth_got: 0xcf8
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0xa888
-  __DATA_CONST.__cfstring: 0x7560
+  __TEXT.__unwind_info: 0xb98
+  __DATA_CONST.__auth_got: 0xd20
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0xaf40
+  __DATA_CONST.__cfstring: 0x75a0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1c40
-  __DATA.__objc_selrefs: 0x768
+  __DATA.__objc_const: 0x1890
+  __DATA.__objc_selrefs: 0x7f0
   __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x808
+  __DATA.__data: 0x6c8
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x10
-  __DATA.__bss: 0x6d8
-  __DATA.__common: 0x20
+  __DATA.__bss: 0x6c0
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E330563D-81D3-35AF-9A12-A7C740879260
-  Functions: 1048
-  Symbols:   569
-  CStrings:  2859
+  UUID: A912D940-D033-3B83-B706-FA664C148476
+  Functions: 1027
+  Symbols:   573
+  CStrings:  2828
 
Symbols:
+ _aks_assert_drop
+ _aks_assert_hold
+ _aks_dealloc
+ _aks_generation
+ _aks_get_bag_uuid
+ _aks_get_lock_state
+ _aks_kc_backup_get_uuid
+ _aks_kc_backup_open_keybag
+ _aks_kc_backup_unwrap_key
+ _aks_kc_backup_wrap_key
+ _aks_operation_optional_params
+ _aks_params_create
+ _aks_params_free
+ _aks_params_get_der
+ _aks_params_set_data
+ _aks_ref_key_create
+ _aks_ref_key_create_with_blob
+ _aks_ref_key_decrypt
+ _aks_ref_key_delete
+ _aks_ref_key_encrypt
+ _aks_ref_key_free
+ _aks_ref_key_get_blob
+ _aks_ref_key_get_external_data
+ _aks_ref_key_unwrap
+ _aks_ref_key_wrap
+ _aks_unwrap_key
+ _aks_wrap_key
- _IOConnectCallMethod
- _IORegistryEntryFromPath
- _IOServiceClose
- ___stdoutp
- _bzero
- _ccaes_cbc_decrypt_mode
- _cccbc_clear_iv
- _cccbc_init
- _cccbc_update
- _cccurve25519_make_pub
- _ccder_blob_decode_len
- _ccder_blob_decode_range
- _ccder_blob_decode_sequence_tl
- _ccder_blob_decode_tag
- _ccder_blob_decode_tl
- _ccder_blob_encode_body
- _ccder_blob_encode_tl
- _ccn_read_uint
- _ccpbkdf2_hmac
- _fprintf
- _qsort
- _syslog$DARWIN_EXTSN
- _uuid_compare
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "_SecItemAdd returned bad data type"
+ "fetchNewestChangesFirst"
+ "initialSyncFinished"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Unwrapped DER backup bag%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "AppleKeyStore"
- "IOService:/IOResources/AppleKeyStore"
- "REQUIRE_func"
- "_aks_operation"
- "_get_prederived_configuration"
- "_merge_dict_cb"
- "aks"
- "aks-client-queue"
- "aks_assert_drop"
- "aks_assert_hold"
- "aks_generation"
- "aks_get_bag_uuid"
- "aks_get_lock_state"
- "aks_kc_backup_get_uuid"
- "aks_kc_backup_open_keybag"
- "aks_kc_backup_unwrap_key"
- "aks_kc_backup_wrap_key"
- "aks_load_bag"
- "aks_unload_bag"
- "aks_unlock_bag"
- "aks_unwrap_key"
- "aks_wrap_key"
- "der_key_validate"
- "failed to open connection to %s\n"
- "ks_decrypt_data: invalid version %d"

```
