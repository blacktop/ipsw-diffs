## libInFieldCollection.dylib

> `/usr/lib/libInFieldCollection.dylib`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x5efe8
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__cstring: 0x218b
-  __TEXT.__const: 0xcf64
-  __TEXT.__unwind_info: 0x560
-  __TEXT.__objc_methname: 0x67
-  __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x15a8
+  __TEXT.__text: 0x75acc
+  __TEXT.__cstring: 0x27f3
+  __TEXT.__const: 0x7034
+  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x15d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x34e8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x3490
   __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__auth_got: 0x3c0
   __AUTH.__data: 0x8
-  __DATA.__data: 0x1348
-  __DATA.__bss: 0x2f9
+  __DATA.__data: 0x1438
+  __DATA.__bss: 0x311
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43982F63-0AF9-3F3E-B9E5-9A4A27E45B73
-  Functions: 703
-  Symbols:   156
-  CStrings:  394
+  UUID: 6C485790-67D9-32CB-89A8-B2D8DFE67966
+  Functions: 752
+  Symbols:   157
+  CStrings:  417
 
Symbols:
+ ___stderrp
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ "/.exclave"
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
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "decode_pfk_bulk_data"
+ "decode_pfk_bulk_entry"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "AKSGetStashStats"
- "UTF8String"
- "aks_fv_new_sibling_vek"
- "aks_remote_peer_drop"
- "aks_remote_peer_get_state"
- "aks_smartcard_register"
- "aks_smartcard_request_unlock"
- "aks_smartcard_unlock"
- "aks_smartcard_unregister"
- "aks_stash_escrow"
- "embeddedSecureElement"
- "failed to open connection to %s\n"
- "getHwSupport"
- "queryHardwareSupport:"
- "serialNumber"
- "sharedHardwareManager"

```
