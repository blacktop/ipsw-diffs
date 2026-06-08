## PairedUnlock

> `/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock`

```diff

-184.4.1.0.0
-  __TEXT.__text: 0x2d6c
-  __TEXT.__auth_stubs: 0x280
+184.4.2.0.0
+  __TEXT.__text: 0x2c0c
   __TEXT.__objc_methlist: 0x624
-  __TEXT.__cstring: 0x39b
+  __TEXT.__cstring: 0x3a4
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__gcc_except_tab: 0x148
   __TEXT.__oslogstring: 0x36
-  __TEXT.__unwind_info: 0x1d0
-  __TEXT.__objc_classname: 0xa1
-  __TEXT.__objc_methname: 0xe09
-  __TEXT.__objc_methtype: 0x306
-  __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x290
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x8f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x1e8
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96BC6008-8F78-37B8-8BF5-CA5BE63B1A97
+  UUID: B175FC10-F250-319D-B921-77A29DCFEDF4
   Functions: 105
-  Symbols:   480
-  CStrings:  294
+  Symbols:   487
+  CStrings:  75
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[PUError errorWithCode:description:] : 228 -> 220
~ -[PURemoteDeviceState isEqual:] : 700 -> 712
~ -[PURemoteDeviceState hash] : 224 -> 220
~ -[PURemoteDeviceState description] : 272 -> 264
~ -[PURemoteDeviceState initWithCoder:] : 228 -> 224
~ -[PURemoteDeviceState encodeWithCoder:] : 196 -> 188
~ -[PURemoteDeviceState setPasscodePolicy:] : 64 -> 12
~ -[PURemotePasscodePolicy description] : 176 -> 168
~ -[PURemotePasscodePolicy encodeWithCoder:] : 116 -> 108
~ _pu_log : 84 -> 68
~ -[PUConnection queueNameWithSuffix:] : 152 -> 144
~ +[PUConnection serverInterface] : 84 -> 68
~ ___31+[PUConnection serverInterface]_block_invoke : 216 -> 212
~ +[PUConnection clientInterface] : 84 -> 68
~ ___31+[PUConnection clientInterface]_block_invoke : 244 -> 240
~ -[PUConnection serverConnection] : 152 -> 132
~ ___32-[PUConnection serverConnection]_block_invoke : 544 -> 532
~ -[PUConnection setServerConnection:] : 160 -> 152
~ ___36-[PUConnection setServerConnection:]_block_invoke : 60 -> 12
~ -[PUConnection pairForUnlockWithPasscode:] : 120 -> 112
~ -[PUConnection unpairForUnlock] : 96 -> 88
~ -[PUConnection enableOnlyRemoteUnlockWithPasscode:] : 120 -> 112
~ -[PUConnection disableOnlyRemoteUnlock] : 96 -> 88
~ -[PUConnection requestRemoteDeviceRemoteAction:type:] : 120 -> 112
~ -[PUConnection requestRemoteDeviceUnlockNotification] : 96 -> 88
~ -[PUConnection requestRemoteDeviceRemoveLockout:] : 200 -> 204
~ ___49-[PUConnection requestRemoteDeviceRemoveLockout:]_block_invoke : 188 -> 180
~ -[PUConnection requestDeviceSetWristDetectionDisabled:completion:] : 376 -> 328
~ ___66-[PUConnection requestDeviceSetWristDetectionDisabled:completion:]_block_invoke : 156 -> 148
~ ___37-[PUConnection getRemoteDeviceState:]_block_invoke : 196 -> 192
~ -[PUConnection queryRemoteDeviceState:] : 120 -> 112
~ -[PUConnection delegateIfRespondsToSelector:] : 88 -> 84
~ -[PUConnection didPairForUnlock:error:] : 216 -> 220
~ ___39-[PUConnection didPairForUnlock:error:]_block_invoke : 152 -> 148
~ -[PUConnection didUnpairForUnlock:error:] : 216 -> 220
~ ___41-[PUConnection didUnpairForUnlock:error:]_block_invoke : 152 -> 148
~ -[PUConnection didEnableOnlyRemoteUnlock:error:] : 216 -> 220
~ ___48-[PUConnection didEnableOnlyRemoteUnlock:error:]_block_invoke : 152 -> 148
~ -[PUConnection didDisableOnlyRemoteUnlock:error:] : 216 -> 220
~ ___49-[PUConnection didDisableOnlyRemoteUnlock:error:]_block_invoke : 152 -> 148
~ -[PUConnection remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:] : 244 -> 256
~ ___76-[PUConnection remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:]_block_invoke : 156 -> 152
~ ___37-[PUConnection remoteDeviceDidUnlock]_block_invoke : 148 -> 144
~ -[PUConnection didGetRemoteDeviceState:error:] : 236 -> 248
~ ___46-[PUConnection didGetRemoteDeviceState:error:]_block_invoke : 156 -> 152
~ -[PUConnection remoteDeviceDidRemoveLockout:error:] : 208 -> 212
~ ___51-[PUConnection remoteDeviceDidRemoveLockout:error:]_block_invoke : 208 -> 200
~ -[PUConnectionUnlockClient initWithConnection:] : 124 -> 120
~ -[PUConnectionUnlockClient remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:] : 124 -> 128
~ -[PUConnectionUnlockClient didGetRemoteDeviceState:error:] : 116 -> 120
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PUConnectionDelegate>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"PUConnection\""
- "@\"PUConnectionUnlockClient\""
- "@\"PURemotePasscodePolicy\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "PUConnection"
- "PUConnectionUnlockClient"
- "PUError"
- "PURemoteDeviceState"
- "PURemotePasscodePolicy"
- "PUUnlockClient"
- "PUUnlockServer"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<PUConnectionDelegate>\",W,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"PUConnection\",W,N,V_connection"
- "T@\"PURemotePasscodePolicy\",&,N,V_passcodePolicy"
- "T@?,C,N,V_remoteDeviceRemoveLockoutHandler"
- "TB,N,GhasPasscodeSet,V_passcodeSet"
- "TB,N,GisModificationAllowed,V_modificationAllowed"
- "TB,N,GisPasscodeLocked,V_passcodeLocked"
- "TB,N,GisUnlockOnly,V_unlockOnly"
- "TB,N,GisWristDetectEnabled,V_wristDetectEnabled"
- "TB,R"
- "TI,N,V_version"
- "TQ,N,V_passcodeMinimumLength"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_delegate"
- "_delegateQueue"
- "_modificationAllowed"
- "_passcodeLocked"
- "_passcodeMinimumLength"
- "_passcodePolicy"
- "_passcodeSet"
- "_remoteDeviceRemoveLockoutHandler"
- "_serverConnection"
- "_serverConnectionQueue"
- "_unlockClient"
- "_unlockOnly"
- "_version"
- "_wristDetectEnabled"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendInt:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:withName:"
- "autorelease"
- "build"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "checkIn"
- "class"
- "clientInterface"
- "conformsToProtocol:"
- "copy"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "delegateIfRespondsToSelector:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didCompleteRemoteAction:error:"
- "didDisableOnlyRemoteUnlock:error:"
- "didEnableOnlyRemoteUnlock:error:"
- "didGetRemoteDeviceState:error:"
- "didPairForUnlock:error:"
- "didUnpairForUnlock:error:"
- "disableOnlyRemoteUnlock"
- "enableOnlyRemoteUnlockWithPasscode:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithCode:description:"
- "errorWithDomain:code:userInfo:"
- "getRemoteDeviceState:"
- "hasPasscodeSet"
- "hash"
- "init"
- "initWithCoder:"
- "initWithConnection:"
- "initWithDelegate:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isWristDetectEnabled"
- "modificationAllowed"
- "numberWithBool:"
- "pairForUnlockWithPasscode:"
- "passcodeLocked"
- "passcodePolicy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "queryRemoteDeviceState:"
- "queueNameWithSuffix:"
- "r*24@0:8@16"
- "release"
- "remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:"
- "remoteDeviceDidRemoveLockout:error:"
- "remoteDeviceDidUnlock"
- "remoteDeviceRemoveLockoutHandler"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "requestDeviceSetWristDetectionDisabled:completion:"
- "requestRemoteDeviceRemoteAction:type:"
- "requestRemoteDeviceRemoveLockout"
- "requestRemoteDeviceRemoveLockout:"
- "requestRemoteDeviceUnlockNotification"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverConnection"
- "serverInterface"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setModificationAllowed:"
- "setPasscodeLocked:"
- "setPasscodeMinimumLength:"
- "setPasscodePolicy:"
- "setPasscodeSet:"
- "setRemoteDeviceRemoveLockoutHandler:"
- "setRemoteObjectInterface:"
- "setServerConnection:"
- "setUnlockOnly:"
- "setVersion:"
- "setWithObjects:"
- "setWristDetectEnabled:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "syncPasscodeState"
- "unlockConnection:didDisableOnlyRemoteUnlock:error:"
- "unlockConnection:didEnableOnlyRemoteUnlock:error:"
- "unlockConnection:didPairForUnlock:error:"
- "unlockConnection:didUnpairForUnlock:error:"
- "unlockConnection:remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:"
- "unlockConnection:remoteDeviceDidNotifyState:"
- "unlockConnectionRemoteDeviceDidUnlock:"
- "unlockOnly"
- "unpairForUnlock"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"PURemoteDeviceState\"@\"NSError\">16"
- "v24@0:8Q16"
- "v28@0:8B16@\"NSError\"20"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"PURemoteDeviceState\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8q16q24"
- "v36@0:8B16@\"PURemoteDeviceState\"20@\"NSError\"28"
- "v36@0:8B16@20@28"
- "zone"

```
