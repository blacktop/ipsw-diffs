## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-640.120.2.0.0
-  __TEXT.__text: 0x1de14
-  __TEXT.__auth_stubs: 0x13c0
+674.0.0.0.0
+  __TEXT.__text: 0x1f460
+  __TEXT.__auth_stubs: 0x1410
   __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__cstring: 0x971c
+  __TEXT.__cstring: 0x9825
   __TEXT.__const: 0x506
   __TEXT.__oslogstring: 0x28
-  __TEXT.__gcc_except_tab: 0x640
+  __TEXT.__gcc_except_tab: 0x658
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__unwind_info: 0x938
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x1509
-  __TEXT.__objc_methtype: 0x9b0
+  __TEXT.__objc_methname: 0x15d5
+  __TEXT.__objc_methtype: 0xa31
   __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__const: 0x888
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x9f0
-  __AUTH_CONST.__const: 0x700
+  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x4fc0
   __AUTH_CONST.__objc_const: 0x718
   __AUTH.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D853B01B-2348-3C02-8146-29FA51C525E3
-  Functions: 667
-  Symbols:   2050
-  CStrings:  2069
+  UUID: 53EB5B09-0D0C-358E-9690-7A249140C175
+  Functions: 692
+  Symbols:   2051
+  CStrings:  2076
 
Symbols:
+ -[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:]
+ -[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]
+ -[MKBKeyStoreDevice SeshatRecover:secretIsACM:]
+ -[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]
+ -[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:]
+ -[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:]
+ -[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]
+ -[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]
+ GCC_except_table81
+ _MKBBackupEnableForVolumeWithACM
+ _MKBDeviceSetGracePeriodWithACM
+ _MKBKeyBagChangeSecretWithACM
+ _MKBKeyBagChangeSystemGenerationWithACM
+ _MKBKeyBagChangeSystemSecretWithACM
+ _MKBKeyBagChangeSystemSecretWithEscrowWithACM
+ _MKBKeyBagCreateEscrowWithACM
+ _MKBKeyBagCreateOTABackupWithACM
+ _MKBKeyBagCreateSystemUnwrappedWithACM
+ _MKBKeyBagCreateSystemWithACM
+ _MKBKeyBagPerformRecoveryWithACM
+ _MKBKeyBagRegisterOTABackupWithACM
+ _MKBKeyBagUnlockWithACM
+ _MKBSetDeviceConfigurationsWithACM
+ _MKBUnlockDeviceWithACM
+ _MKBUserSessionCreatePersonaKeyForUserWithACM
+ _MKBVerifyACMPasswordWithContext
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _SeshatCreateDerivedPasscodeOpts
+ _SeshatCreateDerivedPasscodeOpts.cold.1
+ __MKBBackupEnableForVolume
+ __MKBDeviceSetGracePeriod
+ __MKBKeyBagChangeSystemSecretOpts
+ __MKBKeyBagCreateOTABackup
+ __MKBKeyBagPerformRecovery
+ __MKBKeyBagRegisterOTABackup
+ __MKBVerifyPasswordWithContext
+ ___102-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:]_block_invoke
+ ___102-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:]_block_invoke_2
+ ___109-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:]_block_invoke
+ ___109-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:]_block_invoke_2
+ ___46-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke
+ ___46-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke_2
+ ___47-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]_block_invoke
+ ___47-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]_block_invoke_2
+ ___62-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke
+ ___62-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke_2
+ ___74-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke
+ ___74-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke_2
+ ___90-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]_block_invoke
+ ___90-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]_block_invoke_2
+ ___90-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:]_block_invoke
+ ___90-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_literal_global.141
+ ___block_literal_global.205
+ ___block_literal_global.252
+ _aks_change_secret_epilogue_with_opts
+ _aks_create_bag_with_acm
+ _aks_create_escrow_bag_with_acm
+ _aks_recover_with_escrow_bag_with_acm
+ _aks_se_get_passcode_derivation
+ _aks_se_get_reset_token_for_memento_secret_with_opts
+ _aks_se_recover_with_opts
+ _aks_set_configuration_with_acm
+ _aks_set_system_with_opts
+ _aks_unlock_bag_with_acm
+ _aks_unlock_device_with_opts
+ _aks_verify_password_with_opts
+ _objc_msgSend$ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:
+ _objc_msgSend$SeshatEnroll:secretIsACM:
+ _objc_msgSend$SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:
+ _objc_msgSend$SeshatRecover:secretIsACM:
+ _objc_msgSend$SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:
+ _objc_msgSend$SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:
+ _objc_msgSend$SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:
+ _objc_msgSend$addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:
+ _objc_msgSend$changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:
+ _objc_msgSend$changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:
+ _objc_msgSend$changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:
+ _objc_msgSend$createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:
+ _objc_msgSend$enableBackupForVolume:withSecret:secretIsACM:bagData:
+ _objc_msgSend$enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:
+ _objc_msgSend$registerBackupBag:withSecret:secretSize:secretIsACM:reply:
+ _objc_msgSend$registerOTABackup:withSecret:secretIsACM:
- -[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:]
- -[MKBKeyStoreDevice SeshatEnroll:]
- -[MKBKeyStoreDevice SeshatRecover:]
- -[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]
- -[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:withPersonaUUIDString:forPath:]
- -[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:]
- -[MKBKeyStoreDevice enableBackupForVolume:withSecret:bagData:]
- -[MKBKeyStoreDevice registerOTABackup:withSecret:]
- _MKBVerifyPasswordWithContext.cold.1
- _SeshatCreateDerivedPasscode
- ___101-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:]_block_invoke
- ___101-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:]_block_invoke_2
- ___34-[MKBKeyStoreDevice SeshatEnroll:]_block_invoke
- ___34-[MKBKeyStoreDevice SeshatEnroll:]_block_invoke_2
- ___35-[MKBKeyStoreDevice SeshatRecover:]_block_invoke
- ___35-[MKBKeyStoreDevice SeshatRecover:]_block_invoke_2
- ___50-[MKBKeyStoreDevice registerOTABackup:withSecret:]_block_invoke
- ___50-[MKBKeyStoreDevice registerOTABackup:withSecret:]_block_invoke_2
- ___62-[MKBKeyStoreDevice enableBackupForVolume:withSecret:bagData:]_block_invoke
- ___62-[MKBKeyStoreDevice enableBackupForVolume:withSecret:bagData:]_block_invoke_2
- ___68-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]_block_invoke
- ___68-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]_block_invoke_2
- ___78-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:]_block_invoke
- ___78-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:]_block_invoke_2
- ___90-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:withPersonaUUIDString:forPath:]_block_invoke
- ___90-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:withPersonaUUIDString:forPath:]_block_invoke_2
- ___block_literal_global.153
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.201
- ___block_literal_global.212
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.240
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.255
- ___block_literal_global.257
- ___block_literal_global.259
- ___block_literal_global.261
- ___block_literal_global.264
- ___block_literal_global.266
- ___block_literal_global.271
- ___block_literal_global.276
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.301
- _aks_change_secret_epilogue
- _aks_se_get_reset_token_for_memento_secret
- _aks_se_recover
- _aks_set_system_with_passcode
- _aks_unlock_device
- _aks_verify_password
- _aks_verify_password_memento
- _objc_msgSend$ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:
- _objc_msgSend$SeshatEnroll:
- _objc_msgSend$SeshatEnrollWithSecret:secretSize:withReply:
- _objc_msgSend$SeshatRecover:
- _objc_msgSend$SeshatRecoverWithSecret:secretSize:withReply:
- _objc_msgSend$SeshatUnlock:withMemento:verifyOnly:withACMRef:
- _objc_msgSend$SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:
- _objc_msgSend$addPersonaKeyForUserSession:withSecret:withPersonaUUIDString:forPath:
- _objc_msgSend$changeClassKeysGenerationWithSecret:secretSize:generationOption:reply:
- _objc_msgSend$changeClassKeysGenerationWithSecret:withGenerationOption:
- _objc_msgSend$changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:reply:
- _objc_msgSend$createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:withReply:
- _objc_msgSend$enableBackupForVolume:withSecret:bagData:
- _objc_msgSend$enableBackupForVolume:withSecret:secretSize:reply:
- _objc_msgSend$registerBackupBag:withSecret:secretSize:reply:
- _objc_msgSend$registerOTABackup:withSecret:
CStrings:
+ "-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:]_block_invoke"
+ "-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke"
+ "-[MKBKeyStoreDevice SeshatEnroll:secretIsACM:]_block_invoke_2"
+ "-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]"
+ "-[MKBKeyStoreDevice SeshatRecover:secretIsACM:]_block_invoke"
+ "-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]"
+ "-[MKBKeyStoreDevice SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:]_block_invoke"
+ "-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:]_block_invoke"
+ "-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:]_block_invoke"
+ "-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke"
+ "-[MKBKeyStoreDevice enableBackupForVolume:withSecret:secretIsACM:bagData:]_block_invoke_2"
+ "-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke"
+ "-[MKBKeyStoreDevice registerOTABackup:withSecret:secretIsACM:]_block_invoke_2"
+ "ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:"
+ "KBSeshatGetSeSecret"
+ "MKBDeviceSetGracePeriod(acm:%d): To (%lld)AKS return Value is %d\n"
+ "SeshatCreateDerivedPasscodeOpts"
+ "SeshatEnroll:secretIsACM:"
+ "SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:"
+ "SeshatRecover:secretIsACM:"
+ "SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:"
+ "SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:"
+ "SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:"
+ "_MKBDeviceSetGracePeriod"
+ "_MKBKeyBagChangeSystemSecretOpts"
+ "_MKBVerifyPasswordWithContext"
+ "addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:"
+ "cant verify passcode(acm:%d,memento:%d) 0x%x"
+ "changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:"
+ "changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:"
+ "changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:"
+ "createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:"
+ "enableBackupForVolume:withSecret:secretIsACM:bagData:"
+ "enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:"
+ "failed to get se derivation"
+ "handle: %d, se-support: %d, primary-user: %d, subject-to-seshat: %d, preflight: %d, se_bound: %d, se_unenroll:%d, dis-imm-enr: %d"
+ "i28@0:8@16B24"
+ "i32@0:8@16i24B28"
+ "i36@0:8@16@24B32"
+ "i44@0:8@16@24B32^@36"
+ "i48@0:8@16B24B28B32@36i44"
+ "i48@0:8I16@20B28@32@40"
+ "i56@0:8@16@24@32@40i48B52"
+ "registerBackupBag:withSecret:secretSize:secretIsACM:reply:"
+ "registerOTABackup:withSecret:secretIsACM:"
+ "subject_for_seshat"
+ "v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?i@\"NSError\">36"
+ "v44@0:8@16Q24B32@?36"
+ "v48@0:8@\"NSFileHandle\"16Q24B32i36@?<v@?@\"NSError\">40"
+ "v48@0:8@16Q24B32i36@?40"
+ "v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSData\"@\"NSError\">44"
+ "v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16@24Q32B40@?44"
+ "v64@0:8@\"NSFileHandle\"16Q24B32B36B40@\"NSData\"44i52@?<v@?i@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24I32@\"NSFileHandle\"36Q44B52@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24I32@36Q44B52@?56"
+ "v64@0:8@16Q24B32B36B40@44i52@?56"
+ "v80@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@\"NSFileHandle\"40Q48@\"NSData\"56B64B68@?<v@?@\"NSError\">72"
+ "v80@0:8@16@24Q32@40Q48@56B64B68@?72"
- "-[MKBKeyStoreDevice ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:]_block_invoke"
- "-[MKBKeyStoreDevice SeshatEnroll:]_block_invoke"
- "-[MKBKeyStoreDevice SeshatEnroll:]_block_invoke_2"
- "-[MKBKeyStoreDevice SeshatRecover:]"
- "-[MKBKeyStoreDevice SeshatRecover:]_block_invoke"
- "-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]"
- "-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]_block_invoke"
- "-[MKBKeyStoreDevice addPersonaKeyForUserSession:withSecret:withPersonaUUIDString:forPath:]_block_invoke"
- "-[MKBKeyStoreDevice changeClassKeysGenerationWithSecret:withGenerationOption:]_block_invoke"
- "-[MKBKeyStoreDevice enableBackupForVolume:withSecret:bagData:]_block_invoke"
- "-[MKBKeyStoreDevice enableBackupForVolume:withSecret:bagData:]_block_invoke_2"
- "-[MKBKeyStoreDevice registerOTABackup:withSecret:]_block_invoke"
- "-[MKBKeyStoreDevice registerOTABackup:withSecret:]_block_invoke_2"
- "ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:"
- "MKBDeviceSetGracePeriod"
- "MKBDeviceSetGracePeriod: To (%lld)AKS return Value is %d\n"
- "MKBKeyBagChangeSystemSecretOpts"
- "MKBVerifyPasswordWithContext"
- "SeshatEnroll:"
- "SeshatEnrollWithSecret:secretSize:withReply:"
- "SeshatRecover:"
- "SeshatRecoverWithSecret:secretSize:withReply:"
- "SeshatUnlock:withMemento:verifyOnly:withACMRef:"
- "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:"
- "addPersonaKeyForUserSession:withSecret:withPersonaUUIDString:forPath:"
- "cant verify old memento passcode 0x%x"
- "cant verify old passcode 0x%x"
- "changeClassKeysGenerationWithSecret:secretSize:generationOption:reply:"
- "changeClassKeysGenerationWithSecret:withGenerationOption:"
- "changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:reply:"
- "createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:withReply:"
- "enableBackupForVolume:withSecret:bagData:"
- "enableBackupForVolume:withSecret:secretSize:reply:"
- "handle: %d, se-support: %d, primary-user: %d, no-passcode: %d, preflight: %d, se_bound: %d, se_unenroll:%d, dis-imm-enr: %d"
- "i40@0:8@16@24^@32"
- "i40@0:8@16B24B28@32"
- "i44@0:8I16@20@28@36"
- "i52@0:8@16@24@32@40i48"
- "registerBackupBag:withSecret:secretSize:reply:"
- "registerOTABackup:withSecret:"
- "v40@0:8@\"NSFileHandle\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSFileHandle\"16Q24@?<v@?i@\"NSError\">32"
- "v44@0:8@\"NSFileHandle\"16Q24i32@?<v@?@\"NSError\">36"
- "v44@0:8@16Q24i32@?36"
- "v48@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v56@0:8@\"NSFileHandle\"16Q24B32B36@\"NSData\"40@?<v@?i@\"NSError\">48"
- "v56@0:8@16Q24B32B36@40@?48"
- "v60@0:8@\"NSString\"16@\"NSString\"24I32@\"NSFileHandle\"36Q44@?<v@?@\"NSError\">52"
- "v60@0:8@16@24I32@36Q44@?52"
- "v76@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@\"NSFileHandle\"40Q48@\"NSData\"56B64@?<v@?@\"NSError\">68"
- "v76@0:8@16@24Q32@40Q48@56B64@?68"

```
