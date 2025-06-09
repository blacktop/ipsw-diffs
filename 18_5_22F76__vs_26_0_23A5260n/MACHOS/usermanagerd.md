## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-417.100.1.0.0
-  __TEXT.__text: 0xa494c
-  __TEXT.__auth_stubs: 0x1830
-  __TEXT.__objc_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x18dc
-  __TEXT.__const: 0x1124
-  __TEXT.__gcc_except_tab: 0xdf4
-  __TEXT.__cstring: 0x67bc
+452.0.0.0.0
+  __TEXT.__text: 0xb15a4
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_methlist: 0x19e8
+  __TEXT.__const: 0x1384
+  __TEXT.__gcc_except_tab: 0x16c4
+  __TEXT.__cstring: 0x6dbb
   __TEXT.__objc_classname: 0x39a
-  __TEXT.__objc_methname: 0x346d
-  __TEXT.__objc_methtype: 0x12c2
-  __TEXT.__oslogstring: 0x107da
-  __TEXT.__unwind_info: 0x1390
-  __DATA_CONST.__auth_got: 0xc28
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x2660
-  __DATA_CONST.__cfstring: 0x1c00
+  __TEXT.__objc_methname: 0x37f1
+  __TEXT.__objc_methtype: 0x146e
+  __TEXT.__oslogstring: 0x118be
+  __TEXT.__unwind_info: 0x14b8
+  __DATA_CONST.__auth_got: 0xc70
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__cfstring: 0x1ca0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x45e8
-  __DATA.__objc_selrefs: 0xc70
-  __DATA.__objc_ivar: 0x1d8
+  __DATA.__objc_const: 0x4678
+  __DATA.__objc_selrefs: 0xcd8
+  __DATA.__objc_ivar: 0x1e0
   __DATA.__objc_data: 0xa00
-  __DATA.__data: 0x11e8
-  __DATA.__bss: 0x319
-  __DATA.__common: 0xb8
+  __DATA.__data: 0x12a0
+  __DATA.__bss: 0x371
+  __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: BA74A071-15B7-3ACB-99B5-39D43235848A
-  Functions: 2045
-  Symbols:   456
-  CStrings:  3401
+  UUID: D47321E1-6DCC-38CE-8F04-2E8E96979720
+  Functions: 2195
+  Symbols:   466
+  CStrings:  3558
 
Symbols:
+ _OBJC_CLASS_$_NSMutableString
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccder_sizeof_implicit_raw_octet_string
+ _ccgcm_context_size
+ _ccgcm_finalize
+ _ccgcm_init
+ _ccgcm_set_iv
+ _ccgcm_update
+ _voucher_get_current_persona
CStrings:
+ "%@%08X"
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n"
+ "2457711A-523C-4604-B75A-F48A571D5036"
+ ">"
+ "ACMContextCopyData"
+ "ACMContextCreateWithFlags"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "AKSIdentity for user:%d already loaded, identity exists"
+ "AKSIdentity for user:%d not loaded, loading to verify existance"
+ "AKSLoadIdentity Succeeded, it exists, unloading now..."
+ "AKSLoadIdentity after check failed with Error:%d"
+ "AKSLoadIdentity after check failed with Error:%ld"
+ "AKSLoadIdentity cannot be loaded, failure to validate token, error:%ld"
+ "AKSLoadIdentity failed with Error:%ld  is kAKSReturnDecodeError, so BST does not exist, ENOENT error returned"
+ "AKSLoadIdentity failed with Error:%ld, might not exist.."
+ "AKSLoadIdentity failed with unexpected Error:%ld , EIO error returned"
+ "AKSUnLoadIdentity after load failed with Error:%ld"
+ "Adopting persona %{public}@ (%d) for PID %d"
+ "B40@0:8I16@\"NSData\"20B28^@32"
+ "B40@0:8I16@20B28^@32"
+ "B48@0:8@\"NSUUID\"16I24@\"NSData\"28B36^@40"
+ "B48@0:8@16I24@28B36^@40"
+ "B56@0:8@\"NSUUID\"16@\"NSData\"24@\"NSData\"32I40B44^@48"
+ "B56@0:8@\"NSUUID\"16@\"NSData\"24I32@\"NSData\"36B44^@48"
+ "B56@0:8@16@24@32I40B44^@48"
+ "B56@0:8@16@24I32@36B44^@48"
+ "Bootstrap AKSIdentity not loaded, loading to verify existance"
+ "Created MKB persona key for user %u, persona: %{public}@, homeDir: %{public}@"
+ "Created persona %{public}@ (%u) for user %{public}@ (%u)"
+ "Created universal persona for user %{public}@ (%u)"
+ "Creating bootstrap token with tokendata length:%d"
+ "Data Separated PERSONA with ID: %u IS DISABLED, skipping persona load"
+ "Deleted persona %{public}@ (%u) from user %{public}@ (%u)"
+ "Deleted universal persona %{public}@"
+ "FAILED TO MOUNT APFSUser Volume with error:?%d, unloading kernel persona"
+ "FEEDEEEE-DDDD-CCCC-BBBB-0000"
+ "FEEDEEEE-DDDD-CCCC-BBBB-330000000000"
+ "FEEDEEEE-DDDD-CCCC-BBBB-3333"
+ "FEEDEEEE-DDDD-CCCC-BBBB-550000000000"
+ "FEEDEEEE-DDDD-CCCC-BBBB-5555"
+ "Failed to adopt persona %{public}@ for pid %d: failed to get unique pid"
+ "Failed to adopt persona %{public}@: persona is disabled"
+ "Failed to change bootstrap token secret with error %{public}@"
+ "Failed to create bootstrap token with error %{public}@"
+ "Failed to delete bootstrap token with error %{public}@"
+ "Failed to load bootstrap user with error %@"
+ "Failed to load bootstrap user with error %{public}@"
+ "Failed to retrieve device Passcode"
+ "Failed to retrieve oldTokenData"
+ "Failed to set up voucher for persona %{public}@: no personas found for user %{public}@"
+ "Failed to set up voucher for persona %{public}@: persona not found on user %{public}@"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "Loaded the Bootstrap User, changing tokenData"
+ "Loading the Bootstrap User to change tokenData"
+ "NO"
+ "NULL newToken"
+ "NULL oldToken"
+ "Out of Memory!!! could not allocate dict, exiting...."
+ "Persona disabled due to %@"
+ "Persona volume UUID: %{public}@"
+ "Posted Darwin Notification kUMUserPersonaDisabledNotificationToken"
+ "Received fetchAllUsersPersonaListforPid (sync, pid: %d)"
+ "Received fetchPersonaListforPid (async, pid: %d)"
+ "Received fetchPersonaListforPid (sync, pid: %d)"
+ "Remote Service replacePersonaMachPortVoucher requested by %{public}@ (%d)"
+ "Removed MKB persona key for user %u, persona: %{public}@, volumeUUID: %{public}@"
+ "Removing underneath mount point path:%@"
+ "Returning after failing to create persona session"
+ "Setup Last User volume again"
+ "Succesful change of tokenData for bootstrap token"
+ "Succesful creation of bootstrap token, loading the bootstrap user"
+ "Succesful deletion of bootstrap token"
+ "Successful deletion of the mount path"
+ "Successful load of Bootstrap user, transferring the primary to bootstrap user"
+ "Successful load of Bootstrap user, unload Bootstrap user..."
+ "Successfully unloaded Kernel persona after volume mount failure"
+ "Token Validated as Unlock with it is successful, attempting locking the identity"
+ "UNLOADING kernel persona after volume mount failure failed with error %@"
+ "Unable to find PersonaString for type:%d"
+ "Unable to unlock the idenitity with Error:%ld"
+ "Unloaded the bootstrap User, deleting bootstrap user"
+ "Unloading of the Identity of BOOTSTRAP User SUCCESS"
+ "Unloading the BOOTSTRAP User FAILED with error:%ld"
+ "UserPersonaDisablementReason"
+ "YES"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "_changeSecretrForIdentityErrorOverride"
+ "_disablementReason"
+ "acm_transport"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "changeBootstrapToken with SECRET newToken"
+ "changeBootstrapToken with SECRET oldToken"
+ "changeBootstrapToken: End"
+ "changeBootstrapToken: Start"
+ "changeBootstrapTokenWithOldSecret:oldSize:withNewSecret:newSize:withReply:"
+ "changeBootstrapTokenWithOldSecret:withNewSecret:withReply:"
+ "changeSecretrForIdentityWithUUID:oldPasscode:newPasscode:existingSession:isACMCredential:error:"
+ "checkBootstrapToken: End"
+ "checkBootstrapToken: Start"
+ "checkBootstrapTokenExistsWithReply:"
+ "checkCCError"
+ "com.apple.mobile.usermanagerd.userpersona_disabled"
+ "com.apple.usermanagerd.bootstrap.fullaccess"
+ "createBootstrapToken with NULL device Passcode"
+ "createBootstrapToken with NULL token"
+ "createBootstrapToken with SECRET token"
+ "createBootstrapToken: End"
+ "createBootstrapToken: Start"
+ "createBootstrapTokenWithSecret:secretSize:withDeviceSecretHandle:deviceSecretSize:withReply:"
+ "createBootstrapTokenWithSecret:withDevicePasscode:withReply:"
+ "createIdentityWithUUID:passcode:existingSession:existingSessionPasscode:isACMCredential:error:"
+ "createPersona:withSecret:secretSize:forPid:completionHandler:"
+ "createPersona:withSecret:secretSize:passcodeDataType:forPid:completionHandler:"
+ "crypto_decryptText"
+ "crypto_decryptText_version1"
+ "crypto_decryptText_version2"
+ "crypto_deriveKeyAndDecryptData"
+ "crypto_deriveKeyAndEncryptData"
+ "crypto_encryptText"
+ "crypto_encryptText_version1"
+ "crypto_encryptText_version2"
+ "crypto_generateKey"
+ "crypto_generateKeyFromSharedInfo"
+ "crypto_generateKeyFromSharedInfo_version1"
+ "crypto_generateKeyFromSharedInfo_version2"
+ "crypto_generateRandomSaltLazily"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "deleteBootstrapToken with NULL token"
+ "deleteBootstrapToken with SECRET token"
+ "deleteBootstrapToken with no device Passcode"
+ "deleteBootstrapToken: END"
+ "deleteBootstrapToken: Start"
+ "deleteBootstrapTokenWithSecret:secretSize:withDeviceSecretHandle:deviceSecretSize:withReply:"
+ "deleteBootstrapTokenWithSecret:withDevicePasscode:withReply:"
+ "directSwitchToUser:withSecret:secretSize:context:preferences:pid:completionHandler:"
+ "failed to find last booted user with error:%d, setup again"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "fetchAllUsersPersonaListforPid (async, pid: %d) failed to fetch all user persona array: %{darwin.errno}d"
+ "fetchAllUsersPersonaListforPid (async, pid: %d): entitlement OK"
+ "fetchAllUsersPersonaListforPid (async, pid: %d): entitlement failure"
+ "fetchAllUsersPersonaListforPid (async, pid: %d): no completion handler"
+ "fetchAllUsersPersonaListforPid (sync, pid: %d) failed to fetch all user persona array: %{darwin.errno}d"
+ "fetchAllUsersPersonaListforPid (sync, pid: %d): entitlement OK"
+ "fetchAllUsersPersonaListforPid (sync, pid: %d): entitlement failure"
+ "fetchAllUsersPersonaListforPid (sync, pid: %d): no completion handler"
+ "fetchPersonaListforPid (async, pid: %d): entitlement failure"
+ "fetchPersonaListforPid (async, pid: %d): no completion handler"
+ "fetchPersonaListforPid (async, pid: %d, asid :%d): failed to fetch persona array for session %{public}@: %{darwin.errno}d"
+ "fetchPersonaListforPid (async, pid: %d, asid: %d): entitlement OK"
+ "fetchPersonaListforPid (sync, pid: %d): entitlement OK"
+ "fetchPersonaListforPid (sync, pid: %d): entitlement failure"
+ "fetchPersonaListforPid (sync, pid: %d): no completion handler"
+ "fetchPersonaListforPid (sync, pid: %d, asid: %d): entitlement OK"
+ "generateRandom"
+ "getRequirementDataSizeForVersion"
+ "has device passcode"
+ "loading the bootstrap user"
+ "loginIdentity:intoSession:passcode:isACMCredential:error:"
+ "mach_voucher_persona_for_originator successful; replacement port is: %d"
+ "mach_voucher_persona_for_originator(%d, %d, %lld)"
+ "mach_voucher_persona_for_originator(%d, %d, %lld) failed: %{mach.errno}d"
+ "platform_rng"
+ "replacePersonaMachPortVoucher from pid %d, voucher persona %u, requested persona %{public}@, generationSet: %{bool}d"
+ "replacePersonaMachPortVoucher with no entitlement from pid:%d"
+ "replacePersonaMachPortVoucher: failed to create transport for target port"
+ "replacePersonaMachPortVoucher: have SourcePort:%d"
+ "replacePersonaMachPortVoucher: kernel replacement voucher port:%d"
+ "replacePersonaMachPortVoucher: mach_port_deallocate(%d) failed with error: %{mach.errno}d"
+ "replacePersonaMachPortVoucher: no Account ID from pid:%d"
+ "replacePersonaMachPortVoucher: no Source Voucher Port from pid:%d"
+ "replacePersonaMachPortVoucher: no replacement voucher port received from kernel"
+ "replacePersonaMachPortVoucher: setupVoucherwithPersonaID failed: %{darwin.errno}d"
+ "requirement"
+ "resetBytesInRange:"
+ "switchToUser:withSecret:secretSize:context:pid:completionHandler:"
+ "switchToUser:withSecret:secretSize:context:preferences:pid:completionHandler:"
+ "unlockIdentityInSession:passcode:isACMCredential:error:"
+ "uppercaseString"
+ "userlayout"
+ "usermanagerd failed assertion: targetVoucherPortPtr != NULL"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSFileHandle\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v52@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v56@0:8@\"NSFileHandle\"16Q24@\"NSFileHandle\"32Q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16Q24@32Q40@?48"
+ "v60@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32@\"NSData\"40i48@?<v@?@\"NSError\">52"
+ "v60@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32Q40i48@?<v@?@\"NSDictionary\"@\"NSError\">52"
+ "v60@0:8@16@24Q32@40i48@?52"
+ "v60@0:8@16@24Q32Q40i48@?52"
+ "v68@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32@\"NSData\"40@\"NSDictionary\"48i56@?<v@?@\"NSError\">60"
+ "v68@0:8@16@24Q32@40@48i56@?60"
+ "validateBootstrapToken with NULL token"
+ "validateBootstrapToken with SECRET token"
+ "validateBootstrapToken: End"
+ "validateBootstrapToken: Start"
+ "validateBootstrapTokenWithSecret:secretSize:withReply:"
+ "validateBootstrapTokenWithSecret:withReply:"
- "%s%s:%s%s%s%s%u:%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sdump %s (len = %zd)%s%s\n"
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
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s overflow%s\n"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] created.\n"
- "="
- "ACMContextCreate"
- "B36@0:8I16@\"NSData\"20^@28"
- "B36@0:8I16@20^@28"
- "B52@0:8@\"NSUUID\"16@\"NSData\"24I32@\"NSData\"36^@44"
- "B52@0:8@16@24I32@36^@44"
- "Calling mach_voucher_persona_for_originator with personaID:%d sourcePort:%d with uniqpid:%lld"
- "Cannot find Persona Dict for accountID:%@"
- "Clearing path underneath mount point:%@"
- "Created persona %u for user %@"
- "Created universal persona for user %@"
- "Deleted persona %@ (%u)"
- "Deleted universal persona"
- "Failed to get unique pid for pid %d: %{public}@"
- "In RDServer: No all users persona array pid:%d, error:%d"
- "In RDServer: No persona array pid:%d, asid:%d error:%d"
- "In RDServer: fetchAllUsersPersonaListforPid entitlement OK:%d"
- "In RDServer: fetchAllUsersPersonaListforPid entitlement failure:%d"
- "In RDServer: fetchPersonaListforPid entitlement OK:%d with asid:%d"
- "In RDServer: fetchPersonaListforPid entitlement failure:%d"
- "In RDServer: fetchPersonaListforPid from pid:%d"
- "In UMSyncServer: No persona array OK:%d"
- "In UMSyncServer: fetchAllUsersPersonaListforPid entitlement OK:%d"
- "In UMSyncServer: fetchAllUsersPersonaListforPid entitlement failure:%d"
- "In UMSyncServer: fetchAllUsersPersonaListforPid from pid:%d"
- "In UMSyncServer: fetchPersonaListforPid entitlement failure:%d"
- "In UMSyncServer: fetchPersonaListforPid from pid:%d"
- "MKBUserSessionCreatePersonaKeyForUser(%u, %{public}@, %{public}@)"
- "MKBUserSessionRemovePersonaKeyForUser(%u, %{public}@, %{public}@)"
- "PersonaId:%d requested from PID:%d with personaString:%@"
- "Remote Service replacePersonaMachPortVoucher requested by %@"
- "Replacement port is %d"
- "Successful deletion of mount path"
- "UserManagement early boot taskfailed to find last booted user with error"
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"
- "createIdentityWithUUID:passcode:existingSession:existingSessionPasscode:error:"
- "createPersona:passcodeData:forPid:completionHandler:"
- "createPersona:passcodeData:passcodeDataType:forPid:completionHandler:"
- "deleted"
- "der_key_validate"
- "destroyed"
- "directSwitchToUser:passcodeData:context:preferences:pid:completionHandler:"
- "failed to create transport for target port"
- "failed to find last booted user with error:%d"
- "failed to open connection to %s\n"
- "have SourcePort:%d"
- "kernel replacement voucher port:%d"
- "loginIdentity:intoSession:passcode:error:"
- "mach_port_deallocate failed with error:%d"
- "mach_voucher_persona_for_originator failed with %d"
- "mach_voucher_persona_for_originator successful and returnPort:%d"
- "no replacement voucher port received from kernel"
- "replacePersonaVoucher with no Account ID from pid:%d"
- "replacePersonaVoucher with no Source Voucher Port from pid:%d"
- "replacePersonaVoucher with no entitlement from pid:%d"
- "setupVoucherwithPersonaID failed with %d"
- "switchToUser:passcodeData:context:pid:completionHandler:"
- "switchToUser:passcodeData:context:preferences:pid:completionHandler:"
- "unlockIdentityInSession:passcode:error:"
- "v44@0:8@\"NSDictionary\"16@\"NSData\"24i32@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v52@0:8@\"NSDictionary\"16@\"NSData\"24@\"NSData\"32i40@?<v@?@\"NSError\">44"
- "v52@0:8@\"NSDictionary\"16@\"NSData\"24Q32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16@24@32i40@?44"
- "v60@0:8@\"NSDictionary\"16@\"NSData\"24@\"NSData\"32@\"NSDictionary\"40i48@?<v@?@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"

```
