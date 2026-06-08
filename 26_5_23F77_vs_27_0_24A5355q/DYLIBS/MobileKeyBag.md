## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-674.100.13.0.0
-  __TEXT.__text: 0x163cc
-  __TEXT.__auth_stubs: 0x10b0
+695.0.0.0.0
+  __TEXT.__text: 0x165a0
   __TEXT.__objc_methlist: 0x544
-  __TEXT.__cstring: 0x5efc
-  __TEXT.__const: 0x468
-  __TEXT.__oslogstring: 0x28
+  __TEXT.__cstring: 0x5f24
+  __TEXT.__const: 0x478
+  __TEXT.__oslogstring: 0xec
   __TEXT.__gcc_except_tab: 0x5a4
   __TEXT.__unwind_info: 0x7a0
-  __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methname: 0x11e5
-  __TEXT.__objc_methtype: 0x9b8
-  __TEXT.__objc_stubs: 0xca0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0x1c0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x3de0
   __AUTH_CONST.__objc_const: 0x2e8
+  __AUTH_CONST.__auth_got: 0x8a0
   __DATA.__data: 0x2e0
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 017E5106-D303-35A7-B3CE-6F1DC7CAF419
-  Functions: 540
-  Symbols:   1575
-  CStrings:  1479
+  UUID: 1A655FB0-D1A3-3839-A935-84C2CE0F0DB3
+  Functions: 543
+  Symbols:   1589
+  CStrings:  1270
 
Symbols:
+ _MKBKeyBagKeyStashCreateWithACM
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ __MergedGlobals
+ ____mkb_signpost_log_block_invoke
+ ___block_literal_global.204
+ ___block_literal_global.209
+ ___block_literal_global.272
+ __os_signpost_emit_with_name_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_storeStrong
+ _os_log_create
+ _os_signpost_enabled
+ _os_signpost_id_generate
- ___block_literal_global.205
- ___block_literal_global.210
- _objc_release_x9
- _objc_retainAutoreleasedReturnValue
- _twoSigFigsWithRoundUp
CStrings:
+ "AKS_unlock_verify"
+ "PointsOfInterest"
+ "SE_enroll"
+ "SE_unlock"
+ "com.apple.MobileKeyBag"
+ "completed"
+ "handle=%{public}d"
+ "handle=%{public}d secretIsACM=%{public}d use_memento=%{public}d verify_only=%{public}d"
+ "result=%{public}d"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16Q24^@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8i16B20^i24"
- "ChangeSystemSecretWithEscrow:FromOldPasscode:ToNew:withOpaqueDats:withKeepState:withACM:"
- "Event:"
- "KBXPCProtocol"
- "MKBKeyStoreDevice"
- "NSObject"
- "Q16@0:8"
- "SeshatDebug:"
- "SeshatDebugWithDebugMask:withReply:"
- "SeshatEnroll:secretIsACM:"
- "SeshatEnrollWithSecret:secretSize:secretIsACM:withReply:"
- "SeshatRecover:secretIsACM:"
- "SeshatRecoverWithSecret:secretSize:secretIsACM:withReply:"
- "SeshatUnlock:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:"
- "SeshatUnlockWithSecret:secretSize:secretIsACM:withMemento:verifyOnly:withACMRef:forHandle:withReply:"
- "SetSystemSecretBlob:"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_CreateMKBServerConnection"
- "_xpcConnection"
- "addPersonaKeyForUserSession:withSecret:secretIsACM:withPersonaUUIDString:forPath:"
- "autorelease"
- "backupUUIDForVolume:bagUUID:"
- "backupUUIDForVolume:reply:"
- "bytes"
- "changeClassKeysGenerationWithSecret:secretSize:secretIsACM:generationOption:reply:"
- "changeClassKeysGenerationWithSecret:withGenerationOption:secretIsACM:"
- "changeSystemSecretFromOldPasscode:ToNew:withOpaqueData:withParams:"
- "changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:"
- "changeSystemSecretfromOldSecret:oldSize:toNewSecret:newSize:opaqueData:withParams:reply:"
- "class"
- "code"
- "conformsToProtocol:"
- "copySytemSecretBlob"
- "createKeybagForUserSession:withSessionUID:WithSecret:secretSize:withGracePeriod:withOpaqeStuff:withReply:"
- "createKeybagForUserSession:withSessionUID:WithSecret:withGracePeriod:withOpaqeStuff:"
- "createPersonaKeyForUserSession:forPath:withUID:WithSecret:secretSize:secretIsACM:withReply:"
- "createSyncBagForUserSession:withSessionUID:"
- "createSyncBagForUserSession:withSessionUID:withReply:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "debugDescription"
- "deleteKeybagForUserSession:"
- "deleteKeybagForUserSession:withReply:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disableBackupForVolume:"
- "disableBackupForVolume:reply:"
- "enableBackupForVolume:withSecret:secretIsACM:bagData:"
- "enableBackupForVolume:withSecret:secretSize:secretIsACM:reply:"
- "errorWithDomain:code:userInfo:"
- "forgottenPasscodeEvent"
- "forgottenPasscodeEventWithReply:"
- "getBackupBlobreply:"
- "getBackupkeyForVolume:andCryptoID:withError:"
- "getBackupkeyForVolume:andCryptoID:withReply:"
- "getBytes:length:"
- "getDeviceLockState:needsExtended:withReply:"
- "getDeviceLockStateForUser:extendedState:withLockStateInfo:"
- "getFileHandleForData:"
- "getLockSateInfoforUser:WithReply:"
- "getLockStateForUser:"
- "getPasscodeBlobWithReply:"
- "hash"
- "i16@0:8"
- "i20@0:8I16"
- "i20@0:8i16"
- "i24@0:8@16"
- "i24@0:8I16I20"
- "i24@0:8^i16"
- "i28@0:8@16B24"
- "i28@0:8@16i24"
- "i32@0:8@16@24"
- "i32@0:8@16^@24"
- "i32@0:8@16i24B28"
- "i32@0:8^i16I24I28"
- "i36@0:8@16@24B32"
- "i36@0:8@16i24I28I32"
- "i36@0:8I16@20@28"
- "i44@0:8@16@24@32I40"
- "i44@0:8@16@24B32^@36"
- "i48@0:8@16B24B28B32@36i44"
- "i48@0:8@16i24@28B36i40B44"
- "i48@0:8@16i24@28i36@40"
- "i48@0:8I16@20B28@32@40"
- "i56@0:8@16@24@32@40i48B52"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKeyRollingInProgresswithreply:"
- "isKeyRollingWithKeyStatus:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "loadKeybagForUserSession:withSessionID:withSecret:secretSize:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:withReply:"
- "loadKeybagForUserSession:withSessionID:withSecret:shouldSetGracePeriod:withGracePeriod:isInEarlyStar:"
- "loadSyncBagForUserSession:withSessionUID:"
- "loadSyncBagForUserSession:withSessionUID:withReply:"
- "migrateFS"
- "migrationWithReply:"
- "null"
- "numberWithUnsignedLongLong:"
- "passcodeUnlockFailed"
- "passcodeUnlockFailedWithReply:"
- "passcodeUnlockStart"
- "passcodeUnlockStartWithReply:"
- "passcodeUnlockSuccess"
- "passcodeUnlockSuccessWithReply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "registerBackupBag:withSecret:secretSize:secretIsACM:reply:"
- "registerOTABackup:withSecret:secretIsACM:"
- "release"
- "removePersonaKeyForUserSession:withPersonaUUIDString:withVolumeUUIDString:"
- "removePersonaKeyForUserSession:withUID:withVolumeUUIDString:withReply:"
- "removeSyncBagForUserSession:withSessionUID:"
- "removeSyncBagForUserSession:withSessionUID:withReply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setRemoteObjectInterface:"
- "setSpacedRepetitionMode:"
- "setSpacedRepetitionMode:reply:"
- "setSystemSecretBlob:reply:"
- "setVolumeToPersona:withPersonaString:"
- "setVolumeToPersona:withPersonaString:withReply:"
- "sharedService"
- "startBackupSessionForVolume:"
- "startBackupSessionForVolume:withReply:"
- "stashCommit:WithFlags:"
- "stashCommitwithUID:WithFlags:WithReply:"
- "stashCreateWithSecret:withMode:withUID:WithFlags:"
- "stashCreatewithSecret:secrestSize:withMode:withUID:WithFlags:reply:"
- "stashDestroy"
- "stashDestroywithReply:"
- "stashVerifywithUID:WithFlags:WithReply:"
- "stashVerifywithValidity:WithUID:WithFlags:"
- "stopBackupSessionForVolume:"
- "stopBackupSessionForVolume:withReply:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unloadKeybagForUserSession:"
- "unloadKeybagForUserSession:withReply:"
- "unloadSyncBagForUserSession:withSessionUID:"
- "unloadSyncBagForUserSession:withSessionUID:withReply:"
- "v20@0:8i16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?i@\"NSError\">16"
- "v28@0:8I16@?20"
- "v28@0:8I16@?<v@?@\"NSError\">20"
- "v28@0:8i16@?20"
- "v28@0:8i16@?<v@?@\"NSDictionary\"@\"NSError\">20"
- "v28@0:8i16@?<v@?@\"NSError\">20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8I16I20@?24"
- "v32@0:8I16I20@?<v@?@\"NSError\">24"
- "v32@0:8I16I20@?<v@?i@\"NSError\">24"
- "v32@0:8i16B20@?24"
- "v32@0:8i16B20@?<v@?i@\"NSError\">24"
- "v36@0:8@\"NSDictionary\"16i24@?<v@?@\"NSError\">28"
- "v36@0:8@16i24@?28"
- "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?i@\"NSError\">36"
- "v44@0:8@\"NSString\"16I24@\"NSString\"28@?<v@?@\"NSError\">36"
- "v44@0:8@16I24@28@?36"
- "v44@0:8@16Q24B32@?36"
- "v48@0:8@\"NSFileHandle\"16Q24B32i36@?<v@?@\"NSError\">40"
- "v48@0:8@16Q24B32i36@?40"
- "v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSData\"@\"NSError\">44"
- "v52@0:8@\"NSData\"16@\"NSFileHandle\"24Q32B40@?<v@?@\"NSError\">44"
- "v52@0:8@\"NSFileHandle\"16Q24i32I36I40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24Q32B40@?44"
- "v52@0:8@16Q24i32I36I40@?44"
- "v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36B44i48B52@?<v@?@\"NSError\">56"
- "v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36i44@\"NSData\"48@?<v@?@\"NSError\">56"
- "v64@0:8@\"NSFileHandle\"16Q24B32B36B40@\"NSData\"44i52@?<v@?i@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24I32@\"NSFileHandle\"36Q44B52@?<v@?@\"NSError\">56"
- "v64@0:8@16@24I32@36Q44B52@?56"
- "v64@0:8@16Q24B32B36B40@44i52@?56"
- "v64@0:8@16i24@28Q36B44i48B52@?56"
- "v64@0:8@16i24@28Q36i44@48@?56"
- "v68@0:8@\"NSFileHandle\"16Q24@\"NSFileHandle\"32Q40@\"NSData\"48I56@?<v@?@\"NSError\">60"
- "v68@0:8@16Q24@32Q40@48I56@?60"
- "v80@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@\"NSFileHandle\"40Q48@\"NSData\"56B64B68@?<v@?@\"NSError\">72"
- "v80@0:8@16@24Q32@40Q48@56B64B68@?72"
- "verifySyncBagForUserSession:withSessionUID:"
- "verifySyncBagForUserSession:withSessionUID:withReply:"
- "zone"

```
