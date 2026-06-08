## libCoreKE.dylib

> `/usr/lib/libCoreKE.dylib`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x18552f0
+  __TEXT.__text: 0x16992dc
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x80
-  __TEXT.__const: 0xdcc44
+  __TEXT.__const: 0xdd7ec
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x230b
+  __TEXT.__cstring: 0x25f2
   __TEXT.__objc_methname: 0x5b
-  __TEXT.__unwind_info: 0xb58
-  __TEXT.__eh_frame: 0x88
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1cc88
+  __TEXT.__unwind_info: 0xc08
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0x1cbf8
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x5338
+  __DATA.__data: 0x5350
   __DATA.__bss: 0x71
-  __DATA.__common: 0xbb0
+  __DATA.__common: 0xc40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78616FDA-9AE0-3B7A-9888-689C0427DDEB
-  Functions: 725
-  Symbols:   174
-  CStrings:  386
+  UUID: 008FCF7C-9AB6-303D-B4B1-DA370B9FF51E
+  Functions: 822
+  Symbols:   179
+  CStrings:  396
 
Symbols:
+ ___stderrp
+ _mmap
+ _munmap
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x23
+ _sched_yield
+ _sysconf
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x8
- _objc_storeStrong
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "Failed to get data protection class for given path %s with errno %s (%d)\n"
+ "_aks_remote_peer_drop"
+ "_aks_remote_peer_get_state"
+ "aks_pki_token_get_info"
+ "aks_pki_token_list"
+ "aks_pki_token_op_register"
+ "aks_pki_token_op_set_password"
+ "aks_pki_token_op_unlock"
+ "aks_pki_token_op_verify"
+ "aks_pki_token_register_internal"
+ "aks_pki_token_request_challenge"
+ "aks_pki_token_unregister"
+ "decode_pfk_bulk_data"
+ "decode_pfk_bulk_entry"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "AKSGetStashStats"
- "aks_remote_peer_drop"
- "aks_remote_peer_get_state"
- "aks_smartcard_register"
- "aks_smartcard_request_unlock"
- "aks_smartcard_unlock"
- "aks_smartcard_unregister"

```
