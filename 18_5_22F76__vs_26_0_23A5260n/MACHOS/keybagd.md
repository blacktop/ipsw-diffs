## keybagd

> `/usr/libexec/keybagd`

```diff

-640.120.2.0.0
-  __TEXT.__text: 0x1f4f4
-  __TEXT.__auth_stubs: 0x1430
+674.0.0.0.0
+  __TEXT.__text: 0x21768
+  __TEXT.__auth_stubs: 0x14a0
   __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x814
-  __TEXT.__cstring: 0x936c
-  __TEXT.__const: 0x171
+  __TEXT.__cstring: 0x97f2
+  __TEXT.__const: 0x198
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__objc_methname: 0x176d
+  __TEXT.__objc_methname: 0x17d3
   __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methtype: 0x925
+  __TEXT.__objc_methtype: 0x967
   __TEXT.__dlopen_cstrs: 0x16a
-  __TEXT.__oslogstring: 0x16a
-  __TEXT.__unwind_info: 0x740
-  __DATA_CONST.__auth_got: 0xa28
-  __DATA_CONST.__got: 0x1c8
+  __TEXT.__oslogstring: 0x281
+  __TEXT.__unwind_info: 0x788
+  __DATA_CONST.__auth_got: 0xa60
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xfa8
-  __DATA_CONST.__cfstring: 0x4d60
+  __DATA_CONST.__const: 0xff0
+  __DATA_CONST.__cfstring: 0x4e60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x638
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x1f8
+  __DATA.__data: 0x1fa
   __DATA.__common: 0x30
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A45F84D1-9597-3A01-B636-1CF565128092
-  Functions: 606
-  Symbols:   391
-  CStrings:  2051
+  UUID: 0BE8AEC1-D2ED-3504-AA4B-B124BFB43985
+  Functions: 651
+  Symbols:   399
+  CStrings:  2105
 
Symbols:
+ _IOConnectCallScalarMethod
+ _IOConnectCallStructMethod
+ _aks_backup_enable_volume_with_acm
+ _aks_change_secret_epilogue_with_opts
+ _aks_keybag_persona_create_with_flags
+ _aks_recover_with_escrow_bag_with_acm
+ _aks_se_get_passcode_derivation
+ _aks_se_get_reset_token_for_memento_secret_with_opts
+ _aks_se_recover_with_opts
+ _aks_set_system_with_opts
+ _aks_unlock_device_with_opts
+ _aks_verify_password_with_opts
+ _kIOMasterPortDefault
+ _objc_release_x26
+ _objc_retain_x26
+ _printf
- _CFDataDeleteBytes
- _aks_change_secret
- _aks_change_secret_epilogue
- _aks_change_secret_se
- _aks_se_get_reset_token_for_memento_secret
- _aks_verify_password_memento
- _objc_release_x25
- _objc_retain_x25
CStrings:
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: called.\n"
+ "%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n"
+ "%s: %s: cmd(%u) on CS[%u] -> ok.\n"
+ "%s: %s: log level set to %d.\n"
+ "%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n"
+ "%s: %s: returning, err = %ld.\n"
+ "%s: %s: returning.\n"
+ "(memento:%d, verify_only:%d, acm:%d) -> %d"
+ "-[KBXPCService SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:]"
+ "-[KBXPCService SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:]"
+ "-[KBXPCService SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:]"
+ "-[KBXPCService changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:]"
+ "-[KBXPCService changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:]"
+ "-[KBXPCService changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:]_block_invoke"
+ "-[KBXPCService createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:]"
+ "-[KBXPCService createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:]_block_invoke"
+ "-[KBXPCService enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:]"
+ "-[KBXPCService registerBackupBag:withSecret:secretSize:secretIsACM:reply:]"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "<data>"
+ "ACM"
+ "ACMContextCopyData"
+ "ACMContextCreateWithFlags"
+ "ACMContextDelete"
+ "ACMContextGetExternalForm"
+ "ACMHandleWithPayload"
+ "ACMLib"
+ "AKS STASH VERIFY success (handle:%d, result:%d)"
+ "AppleCredentialManager"
+ "Can't register OTA Backup bag with AppleKeyStore(acm:%d): %x."
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMContextCreate"
+ "LibCall_ACMContextDelete"
+ "LibCall_BuildCommand"
+ "NO"
+ "Seshat preflight = %llx (%llx) (acm: %d)"
+ "SeshatCreateDerivedPasscodeOpts"
+ "SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:"
+ "SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:"
+ "SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:"
+ "YES"
+ "acm_mem_alloc_info"
+ "acm_mem_free_info"
+ "aks_change_secret_opts() failed"
+ "cant verify passcode acm:%d memento:%d"
+ "cant verify passcode(acm:%d,memento:%d) 0x%x"
+ "changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:"
+ "changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:"
+ "createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:"
+ "enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:"
+ "failed to copy context data type %d = %d"
+ "failed to create context"
+ "failed to derive SE passcode %d"
+ "failed to get se derivation"
+ "handle: %d, se-support: %d, primary-user: %d, subject-to-seshat: %d, preflight: %d, se_bound: %d, se_unenroll:%d, dis-imm-enr: %d"
+ "ioKitTransport"
+ "keybag maps to invalid seshat slot %u"
+ "keybagd_SeshatEnroll_block_invoke_2"
+ "oldSecret=%s newSecret=%s %s (params:%d)"
+ "oldpass=%s newpass=%s %s (acm:%d)"
+ "performCommand"
+ "registerBackupBag:withSecret:secretSize:secretIsACM:reply:"
+ "secretCopy -> %d bytes"
+ "seshat slot couter %u reached end of life"
+ "seshat_validate_sanity_block_invoke"
+ "slot %d needs no recovery"
+ "slot is out of bounds %u >= %zd"
+ "stash driven unbind from Seshat (acm: %d)(0x%x -> 0x%x)"
+ "subject_for_seshat"
+ "unable to fetch state for handle %d"
+ "unlock(%d) -> %d"
+ "unlock(handle:%d, acm:%d)"
+ "updateLogLevelFromKext"
+ "v24@?0r^v8Q16"
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
- "-[KBXPCService SeshatEnrollWithSecret:secretSize:withReply:]"
- "-[KBXPCService SeshatRecoverWithSecret:secretSize:withReply:]"
- "-[KBXPCService SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:]"
- "-[KBXPCService changeClassKeysGenerationWithSecret:secretSize:generationOption:reply:]"
- "-[KBXPCService changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:reply:]"
- "-[KBXPCService changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:reply:]_block_invoke"
- "-[KBXPCService createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:withReply:]"
- "-[KBXPCService createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:withReply:]_block_invoke"
- "-[KBXPCService enableBackupForVolume:withSecret:secretSize:reply:]"
- "-[KBXPCService registerBackupBag:withSecret:secretSize:reply:]"
- "AKS STASH VERIFY success (handle:%d)"
- "AnalyticsEvent: change_count: %llu"
- "Can't register OTA Backup bag with AppleKeyStore: %x."
- "Posting analytics stats"
- "SeshatEnrollWithSecret:secretSize:withReply:"
- "SeshatRecoverWithSecret:secretSize:withReply:"
- "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:"
- "aks_change_secret_se() failed"
- "aks_unlock_device() -> %d"
- "analytics_send_passphrase_change"
- "cant verify old memento passcode 0x%x"
- "cant verify old passcode 0x%x"
- "cant verify passcode for memento"
- "changeClassKeysGenerationWithSecret:secretSize:generationOption:reply:"
- "changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:reply:"
- "change_count"
- "com.apple.mobile.keybagd.phrasechange"
- "createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:withReply:"
- "enableBackupForVolume:withSecret:secretSize:reply:"
- "handle: %d, se-support: %d, primary-user: %d, no-passcode: %d, preflight: %d, se_bound: %d, se_unenroll:%d, dis-imm-enr: %d"
- "keybagd_SeshatEnroll_block_invoke"
- "oldpass=%s newpass=%s %s"
- "oldpass=%s newpass=%s %s (params:%d)"
- "registerBackupBag:withSecret:secretSize:reply:"
- "stash driven unbind from Seshat (0x%x -> 0x%x)"
- "unlock(memento:%d, verify_only: %d) -> %d"
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
