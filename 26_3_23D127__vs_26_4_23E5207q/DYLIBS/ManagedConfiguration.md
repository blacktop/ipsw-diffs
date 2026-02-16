## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2432.80.10.0.0
-  __TEXT.__text: 0xf931c
-  __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0xb1fc
-  __TEXT.__const: 0x13c4
-  __TEXT.__cstring: 0x17cc9
-  __TEXT.__oslogstring: 0x903f
-  __TEXT.__gcc_except_tab: 0x10d4
+2438.100.15.502.1
+  __TEXT.__text: 0x101384
+  __TEXT.__auth_stubs: 0x1700
+  __TEXT.__objc_methlist: 0xb24c
+  __TEXT.__const: 0x143c
+  __TEXT.__cstring: 0x18396
+  __TEXT.__oslogstring: 0x9137
+  __TEXT.__gcc_except_tab: 0xfb4
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x3158
-  __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0x1e312
+  __TEXT.__unwind_info: 0x3628
+  __TEXT.__objc_classname: 0xcb4
+  __TEXT.__objc_methname: 0x1e40f
   __TEXT.__objc_methtype: 0x236f
-  __TEXT.__objc_stubs: 0xdc80
-  __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0x4d40
+  __TEXT.__objc_stubs: 0xdd00
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0x4d18
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d20
+  __DATA_CONST.__objc_selrefs: 0x5d60
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__auth_got: 0xb90
   __AUTH_CONST.__const: 0x2090
-  __AUTH_CONST.__cfstring: 0x19280
-  __AUTH_CONST.__objc_const: 0xd738
+  __AUTH_CONST.__cfstring: 0x192e0
+  __AUTH_CONST.__objc_const: 0xd768
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x2328
-  __DATA.__objc_ivar: 0x98c
-  __DATA.__data: 0xc30
+  __AUTH.__objc_data: 0x2300
+  __DATA.__objc_ivar: 0x990
+  __DATA.__data: 0xc38
   __DATA.__bss: 0xc69
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x2f8
+  __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5AA151A-7CC8-3D70-BB83-D042CDE6A64F
-  Functions: 5653
-  Symbols:   17411
-  CStrings:  12235
+  UUID: B9B4F8EA-8081-3E2F-A030-91A8A97ED708
+  Functions: 5748
+  Symbols:   17637
+  CStrings:  12277
 
Symbols:
+ -[MCProfileConnection(Misc) isEmojiKeyboardAllowed]
+ -[MCProfileConnection(Misc) isMDMEnrollmentAllowed]
+ -[MCSingleAppModeConfiguration allowEmojiKeyboard]
+ -[MCSingleAppModeConfiguration setAllowEmojiKeyboard:]
+ -[NSData(ManagedConfigurationAtomic) mc_atomicWriteToPath:error:]
+ -[NSData(ManagedConfigurationAtomic) mc_atomicWriteToURL:error:]
+ -[NSDictionary(ManagedConfiguration) mc_atomicWriteToPath:error:]
+ -[NSDictionary(ManagedConfiguration) mc_atomicWriteToURL:error:]
+ GCC_except_table286
+ _ACMContextCredentialGetPropertyEx
+ _LibCall_ACMSecContextCopyCredentialsArrayEx
+ _LibCall_ACMSecCredentialsArrayDelete
+ _LibSer_ContextCredentialGetPropertyEx_Deserialize
+ _LibSer_ContextCredentialGetPropertyEx_GetSize
+ _LibSer_ContextCredentialGetPropertyEx_Serialize
+ _MCFeatureEmojiKeyboardAllowed
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowEmojiKeyboard
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
+ __OBJC_$_CATEGORY_NSData_$_ManagedConfigurationAtomic
+ __OBJC_$_CLASS_METHODS_NSData(ManagedConfigurationAtomic|ManagedConfiguration)
+ __OBJC_$_INSTANCE_METHODS_NSData(ManagedConfigurationAtomic|ManagedConfiguration)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(MCUtilities|ManagedConfiguration)
+ ___block_descriptor_tmp.181
+ ___block_literal_global.183
+ ___der_key_keybag_type
+ _akstest_new_ekwk.cold.1
+ _akstest_new_key.cold.1
+ _akstest_unwrap_ek.cold.1
+ _akstest_unwrap_key.cold.1
+ _der_key_keybag_type
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$allowEmojiKeyboard
+ _objc_msgSend$isAuthenticatedTemporarySessionEnabled
+ _objc_msgSend$mc_atomicWriteToPath:error:
+ _objc_msgSend$mc_atomicWriteToURL:error:
+ _objc_msgSend$writeToURL:options:error:
- -[NSDictionary(MCUtilities) MCWriteToBinaryFile:atomically:]
- GCC_except_table284
- __OBJC_$_CATEGORY_CLASS_METHODS_NSData_$_ManagedConfiguration
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_ManagedConfiguration
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_MCUtilities
- __OBJC_$_CATEGORY_NSData_$_ManagedConfiguration
- ___block_descriptor_tmp.170
- ___block_literal_global.172
- _copy_raw_secret
- _fv_init_cred_from_secret
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithDictionary:path:
- _objc_msgSend$write
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x9
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
+ ".temp-%@-%@"
+ "/Library/Caches/com.apple.xbs/03406D6F-D828-4122-BD56-0E36D2E1008B/TemporaryDirectory.fj0oNB/Sources/ManagedConfiguration/Connection/MCProfileConnection_Private.m"
+ "/Library/Caches/com.apple.xbs/03406D6F-D828-4122-BD56-0E36D2E1008B/TemporaryDirectory.fj0oNB/Sources/ManagedConfiguration/Connection/MCProfileConnection_Profiles.m"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "ACMContextCredentialGetPropertyEx"
+ "Failed to convert to plist: %{public}@"
+ "Failed to remove temporary file: %{public}@"
+ "Failed to replace original file: %{public}@"
+ "Failed to write temporary file since a directory is present: %{public}@"
+ "Failed to write temporary file: %{public}@"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "MCFileToolsErrorDomain"
+ "ManagedConfigurationAtomic"
+ "TB,N,V_allowEmojiKeyboard"
+ "URLByDeletingLastPathComponent"
+ "Wrong permissions, %lo instead of %lo, on file at path %{public}@."
+ "Wrote file atomically in-place: %{public}@"
+ "_allowEmojiKeyboard"
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "allowEmojiKeyboard"
+ "isAuthenticatedTemporarySessionEnabled"
+ "isEmojiKeyboardAllowed"
+ "isMDMEnrollmentAllowed"
+ "mc_atomicWriteToPath:error:"
+ "mc_atomicWriteToURL:error:"
+ "setAllowEmojiKeyboard:"
+ "writeToURL:options:error:"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "/Library/Caches/com.apple.xbs/Sources/ManagedConfiguration/Connection/MCProfileConnection_Private.m"
- "/Library/Caches/com.apple.xbs/Sources/ManagedConfiguration/Connection/MCProfileConnection_Profiles.m"
- "ACMContextCredentialGetProperty"
- "Could not serialize data for %{public}@: %{public}@"
- "Could not write data to path %{public}@: %{public}@"
- "MCWriteToBinaryFile:atomically:"

```
