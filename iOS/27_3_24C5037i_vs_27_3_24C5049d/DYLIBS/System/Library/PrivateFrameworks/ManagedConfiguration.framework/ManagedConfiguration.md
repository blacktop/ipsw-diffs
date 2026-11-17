## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2483.60.6.0.0
-  __TEXT.__text: 0xf2c8c
-  __TEXT.__objc_methlist: 0xb374
+2483.60.9.0.0
+  __TEXT.__text: 0xf329c
+  __TEXT.__objc_methlist: 0xb404
   __TEXT.__const: 0x1594
-  __TEXT.__cstring: 0x18832
-  __TEXT.__oslogstring: 0x9892
-  __TEXT.__gcc_except_tab: 0x1080
+  __TEXT.__cstring: 0x1889b
+  __TEXT.__oslogstring: 0x992f
+  __TEXT.__gcc_except_tab: 0x1094
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x4628
+  __TEXT.__unwind_info: 0x4650
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x4e18
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e58
+  __DATA_CONST.__objc_selrefs: 0x5e80
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0xac0
-  __AUTH_CONST.__const: 0x2130
-  __AUTH_CONST.__cfstring: 0x197e0
-  __AUTH_CONST.__objc_const: 0xd850
+  __DATA_CONST.__got: 0xac8
+  __AUTH_CONST.__const: 0x2190
+  __AUTH_CONST.__cfstring: 0x19840
+  __AUTH_CONST.__objc_const: 0xdec0
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0xbf8
   __AUTH.__objc_data: 0x2350
   __DATA.__objc_ivar: 0x99c
-  __DATA.__data: 0xcd0
+  __DATA.__data: 0xd30
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x228

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5829
-  Symbols:   9749
-  CStrings:  4641
+  Functions: 5840
+  Symbols:   9768
+  CStrings:  4646
 
Symbols:
+ +[MCAccountUtilities isDDMManagedAccount:]
+ +[MCAccountUtilities saveAccount:toAccountStore:timeout:error:]
+ -[MCProfileConnection(Private) releaseProfileReferencesToAccountWithIdentifier:]
+ -[MCProfileConnection(Profiles) installedPayloadsWithUUID:ofKindOfClass:filterFlags:]
+ GCC_except_table107
+ GCC_except_table29
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table73
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table94
+ GCC_except_table97
+ _MCBKDeviceClass
+ _MCBKDeviceClass.onceToken
+ _MCBKDeviceClass.theClass
+ _MCBKDeviceManagerClass
+ _MCBKDeviceManagerClass.onceToken
+ _MCBKDeviceManagerClass.theClass
+ _MCBKUserProtectedConfigurationClass
+ _MCBKUserProtectedConfigurationClass.onceToken
+ _MCBKUserProtectedConfigurationClass.theClass
+ _MCBiometricKitFrameworkClassNamed
+ __OBJC_$_PROP_LIST_MCAccountPayloadProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MCAccountPayloadProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCAccountPayloadProtocol
+ __OBJC_LABEL_PROTOCOL_$_MCAccountPayloadProtocol
+ __OBJC_PROTOCOL_$_MCAccountPayloadProtocol
+ ___63+[MCAccountUtilities saveAccount:toAccountStore:timeout:error:]_block_invoke
+ ___80-[MCProfileConnection(Private) releaseProfileReferencesToAccountWithIdentifier:]_block_invoke
+ ___MCBKDeviceClass_block_invoke
+ ___MCBKDeviceManagerClass_block_invoke
+ ___MCBKUserProtectedConfigurationClass_block_invoke
+ ___MCBiometricKitFrameworkClassNamed_block_invoke
+ ___block_descriptor_48_e8_32s40r_e21_v20?0B8"NSBundle"12lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e20_v20?0B8"NSError"12ls32l8r48l8r56l8s40l8
- GCC_except_table46
- GCC_except_table49
- GCC_except_table72
- GCC_except_table77
- GCC_except_table80
- GCC_except_table82
- GCC_except_table85
- GCC_except_table93
- _MCBiometricKitClass
- _MCBiometricKitClass.onceToken
- _MCBiometricKitClass.theClass
- ___71+[MCAccountUtilities checkAccountConsistencyAndReleaseOrphanedAccounts]_block_invoke
- ___MCBiometricKitClass_block_invoke
- ___MCBiometricKitClass_block_invoke_2
- ___MCRemoteManagementTransferProfileAccount_block_invoke
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e20_v20?0B8"NSError"12lr48l8r56l8s32l8s40l8
CStrings:
+ "Account %{public}@ belongs to profile %{public}@, which was not installed by MDM; refusing transfer"
+ "BKDevice"
+ "BKDeviceManager"
+ "BKUserProtectedConfiguration"
+ "ERROR_ACCOUNT_TAKEOVER_PROFILE_NOT_INSTALLED_BY_MDM_P_ID"
+ "Release profile references to account error. Error: %{public}@"
+ "RemoteManagement"
+ "Removing profile information from DDM-managed account %{public}@"
- "BiometricKit"
- "Save profile-managed account transfer %{public}@ completed: %{public}@"
- "timed out"
```
