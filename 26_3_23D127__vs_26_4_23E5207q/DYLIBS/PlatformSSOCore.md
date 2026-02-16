## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.80.8.0.0
-  __TEXT.__text: 0x8f058
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0x5f90
-  __TEXT.__const: 0x17e4
-  __TEXT.__cstring: 0xa558
-  __TEXT.__oslogstring: 0x19e7
-  __TEXT.__gcc_except_tab: 0x7f8
+483.100.68.0.0
+  __TEXT.__text: 0x931b8
+  __TEXT.__auth_stubs: 0x1ab0
+  __TEXT.__objc_methlist: 0x5fd0
+  __TEXT.__const: 0x1854
+  __TEXT.__cstring: 0xa40b
+  __TEXT.__oslogstring: 0x19d7
+  __TEXT.__gcc_except_tab: 0x7ec
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__swift5_typeref: 0x15e
+  __TEXT.__swift5_typeref: 0x16a
   __TEXT.__constg_swiftt: 0x374
   __TEXT.__swift5_reflstr: 0x146
   __TEXT.__swift5_fieldmd: 0x128

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x38
-  __TEXT.__unwind_info: 0x2020
-  __TEXT.__eh_frame: 0x5b8
-  __TEXT.__objc_classname: 0xd3d
-  __TEXT.__objc_methname: 0xcad3
-  __TEXT.__objc_methtype: 0x28de
-  __TEXT.__objc_stubs: 0x7060
-  __DATA_CONST.__got: 0x918
+  __TEXT.__unwind_info: 0x2108
+  __TEXT.__eh_frame: 0x598
+  __TEXT.__objc_classname: 0xf93
+  __TEXT.__objc_methname: 0xcd37
+  __TEXT.__objc_methtype: 0x2a03
+  __TEXT.__objc_stubs: 0x7160
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0x2448
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b20
+  __DATA_CONST.__objc_selrefs: 0x2b48
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xd88
+  __AUTH_CONST.__auth_got: 0xd68
   __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x7480
-  __AUTH_CONST.__objc_const: 0x14270
+  __AUTH_CONST.__objc_const: 0x142a0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3460
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x61c
-  __DATA.__data: 0x1050
+  __DATA.__objc_ivar: 0x620
+  __DATA.__data: 0x1068
   __DATA.__bss: 0xd31
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 030F4783-1653-377F-945B-FBA5C06958B7
-  Functions: 3620
-  Symbols:   11992
-  CStrings:  5092
+  UUID: 7794051C-C683-3E9D-9933-84DE32B648EC
+  Functions: 3670
+  Symbols:   12198
+  CStrings:  5101
 
Symbols:
+ +[POCoreConfigurationUtil _platformSSOOldTriggerFile]
+ +[POCoreConfigurationUtil platformSSODevModeTriggerFilePath]
+ +[POCoreConfigurationUtil platformSSOTriggerFilePath]
+ -[PODaemonCoreProcess setUseOldPrebootPath:]
+ -[PODaemonCoreProcess useOldPrebootPath]
+ _OBJC_IVAR_$_PODaemonCoreProcess._useOldPrebootPath
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ ___block_descriptor_tmp.181
+ ___block_literal_global.183
+ ___block_literal_global.245
+ ___block_literal_global.51
+ ___der_key_keybag_type
+ __swift_dead_method_stub
+ _akstest_new_ekwk.cold.1
+ _akstest_new_key.cold.1
+ _akstest_unwrap_ek.cold.1
+ _akstest_unwrap_key.cold.1
+ _der_key_keybag_type
+ _objc_msgSend$_platformSSOOldTriggerFile
+ _objc_msgSend$cipherText
+ _objc_msgSend$createEncryptionKeyForAlgorithm:
+ _objc_msgSend$encapsulatedKey
+ _objc_msgSend$platformSSODevModeTriggerFilePath
+ _objc_msgSend$platformSSOTriggerFilePath
+ _objc_msgSend$setCipherText:
+ _objc_msgSend$setEncapsulatedKey:
+ _symbolic _____Sg_ABt 9CryptoKit12SymmetricKeyV
- +[POCoreConfigurationUtil updateTriggerFile].cold.2
- ___block_descriptor_tmp.170
- ___block_literal_global.172
- ___block_literal_global.240
- ___block_literal_global.48
- _copy_raw_secret
- _fv_init_cred_from_secret
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "TB,V_useOldPrebootPath"
+ "_platformSSOOldTriggerFile"
+ "_useOldPrebootPath"
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "platformSSODevModeTriggerFilePath"
+ "platformSSOTriggerFilePath"
+ "setUseOldPrebootPath:"
+ "useOldPrebootPath"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "trigger file removed"

```
