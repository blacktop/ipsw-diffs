## AccessoryBLEPairing

> `/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x7a5c
-  __TEXT.__auth_stubs: 0x3b0
+1176.0.26.502.1
+  __TEXT.__text: 0x6cd0
   __TEXT.__objc_methlist: 0x534
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__oslogstring: 0x17c2
-  __TEXT.__cstring: 0x709
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methname: 0xe13
-  __TEXT.__objc_methtype: 0x3e3
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x268
+  __TEXT.__cstring: 0x713
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x368
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0x40
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x770
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x48
   __DATA.__data: 0x120
+  __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x20
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45DC3940-5DB4-34B6-BEF8-CAD8F1CD3F22
-  Functions: 112
-  Symbols:   602
-  CStrings:  379
+  UUID: A6F25EB5-0CBE-3375-9B5B-C1D7B63C3574
+  Functions: 115
+  Symbols:   635
+  CStrings:  172
 
Symbols:
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingAttached:blePairingUUID:accInfoDict:supportedPairTypes:].cold.4
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingDataUpdate:blePairingUUID:pairType:pairData:].cold.4
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingDetachAll].cold.3
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingDetached:blePairingUUID:].cold.4
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingFinished:blePairingUUID:].cold.5
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingFinished:blePairingUUID:].cold.6
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingInfoUpdate:blePairingUUID:pairType:pairInfoList:].cold.4
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingNoAccessories].cold.2
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingStateUpdate:blePairingUUID:validMask:btRadioOn:pairingState:pairingModeOn:].cold.4
+ -[ACCBLEPairingProviderInternal registerDelegate:provider:forUUID:].cold.4
+ -[ACCBLEPairingProviderInternal registerDelegate:provider:forUUID:].cold.5
+ __MergedGlobals.4
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.152
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.152.cold.1
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.153.cold.2
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.157
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.157.cold.1
+ ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.69
+ ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.69.cold.1
+ ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.69.cold.2
+ ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.69.cold.3
+ ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.69.cold.4
+ ___block_descriptor_tmp.3
+ ___block_literal_global.156
+ ___block_literal_global.240
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.154
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.154.cold.1
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.154.cold.2
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.158
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.158.cold.1
- ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.70
- ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.70.cold.1
- ___51-[ACCBLEPairingProviderInternal initSharedInstance]_block_invoke.70.cold.2
- ___block_literal_global.157
- _objc_release
- _objc_retain
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACCBLEPairingProviderProtocol>\""
- "@\"<ACCBLEPairingXPCServerProtocol>\""
- "@\"ACCBLEPairingProvider\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSLock\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32@40"
- "ACCBLEPairingAccessory"
- "ACCBLEPairingDelegateReference"
- "ACCBLEPairingProvider"
- "ACCBLEPairingProviderInternal"
- "ACCBLEPairingXPCClientProtocol"
- "ACCBLEPairingXPCServerProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SharedInstance"
- "T#,R"
- "T@\"<ACCBLEPairingProviderProtocol>\",W,N,V_delegate"
- "T@\"<ACCBLEPairingXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"ACCBLEPairingProvider\",W,N,V_provider"
- "T@\"NSData\",&,N,V_blePairingUUID"
- "T@\"NSData\",&,N,V_supportedPairTypes"
- "T@\"NSDictionary\",&,N,V_accInfo"
- "T@\"NSLock\",&,N,V_delegateListLock"
- "T@\"NSMutableDictionary\",&,N,V_accessories"
- "T@\"NSMutableDictionary\",&,N,V_delegateList"
- "T@\"NSString\",&,N,V_accessoryUID"
- "T@\"NSString\",&,N,V_delegateUUID"
- "T@\"NSString\",&,N,V_providerUID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "TB,N,V_blePairingFinished"
- "TB,N,V_desiredBLEPairingState"
- "TQ,R"
- "Ti,N"
- "Ti,N,V_accDetectToken"
- "Ti,N,V_lastScorpiusDetectType"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accDetectToken"
- "_accInfo"
- "_accessories"
- "_accessoryUID"
- "_blePairingFinished"
- "_blePairingUUID"
- "_delegate"
- "_delegateList"
- "_delegateListLock"
- "_delegateUUID"
- "_desiredBLEPairingState"
- "_lastScorpiusDetectType"
- "_provider"
- "_providerUID"
- "_remoteObject"
- "_serverConnection"
- "_supportedPairTypes"
- "accDetectToken"
- "accInfo"
- "accessories"
- "accessoryBLEPairingAttached:blePairingUUID:accInfoDict:supportedPairTypes:"
- "accessoryBLEPairingDataUpdate:blePairingUUID:pairType:pairData:"
- "accessoryBLEPairingDetachAll"
- "accessoryBLEPairingDetached:blePairingUUID:"
- "accessoryBLEPairingFinished:blePairingUUID:"
- "accessoryBLEPairingInfoUpdate:blePairingUUID:pairType:pairInfoList:"
- "accessoryBLEPairingStateUpdate:blePairingUUID:validMask:btRadioOn:pairingState:pairingModeOn:"
- "accessoryUID"
- "allValues"
- "autorelease"
- "blePairing:accessoryAttached:blePairingUUID:accInfoDict:supportedPairTypes:"
- "blePairing:accessoryDetached:blePairingUUID:"
- "blePairing:accessoryDetect:"
- "blePairing:pairingFinished:blePairingUUID:"
- "blePairingDataUpdate:pairType:pairData:accessory:blePairingUUID:"
- "blePairingFinished"
- "blePairingInfoUpdate:pairType:pairInfoList:accessory:blePairingUUID:"
- "blePairingNoAccessories:"
- "blePairingStateUpdate:validMask:btRadioOn:pairingState:pairingModeOn:accessory:blePairingUUID:"
- "blePairingUUID"
- "class"
- "conformsToProtocol:"
- "connectToServer"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "delegate"
- "delegateList"
- "delegateListLock"
- "delegateUUID"
- "description"
- "desiredBLEPairingState"
- "devicePairingData:blePairingUUID:pairType:pairData:"
- "deviceStateUpdate:blePairingUUID:bRadioOn:pairState:bPairModeOn:"
- "deviceUpdatePairingInfo:blePairingUUID:pairType:pairInfo:"
- "getAccDetectType:"
- "hash"
- "i"
- "i16@0:8"
- "i20@0:8i16"
- "init"
- "initConnection:"
- "initSharedInstance"
- "initWithAccessoryUID:blePairingUUID:andAccInfo:supportedPairTypes:"
- "initWithDelegate:"
- "initWithDelegate:provider:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastScorpiusDetectType"
- "lock"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "provider"
- "providerUID"
- "registerDelegate:provider:forUUID:"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverConnection"
- "setAccDetectToken:"
- "setAccInfo:"
- "setAccessories:"
- "setAccessoryUID:"
- "setBlePairingFinished:"
- "setBlePairingUUID:"
- "setDelegate:"
- "setDelegateList:"
- "setDelegateListLock:"
- "setDelegateUUID:"
- "setDesiredBLEPairingState:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastScorpiusDetectType:"
- "setObject:forKey:"
- "setProvider:"
- "setProviderUID:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setServerConnection:"
- "setSupportedPairTypes:"
- "startBLEUpdates:blePairingUUID:pairType:bRadioUpdatesOn:bPairInfoUpdatesOn:"
- "stopBLEUpdates:blePairingUUID:"
- "superclass"
- "supportedPairTypes"
- "unlock"
- "unregisterDelegateForUUID:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v32@0:8@\"NSString\"16@\"NSData\"24"
- "v32@0:8@16@24"
- "v40@0:8@16@24@32"
- "v44@0:8@\"NSString\"16@\"NSData\"24B32i36B40"
- "v44@0:8@\"NSString\"16@\"NSData\"24C32@\"NSArray\"36"
- "v44@0:8@\"NSString\"16@\"NSData\"24C32@\"NSData\"36"
- "v44@0:8@\"NSString\"16@\"NSData\"24C32B36B40"
- "v44@0:8@16@24B32i36B40"
- "v44@0:8@16@24C32@36"
- "v44@0:8@16@24C32B36B40"
- "v44@0:8@16@24i32@36"
- "v44@0:8@16@24i32B36B40"
- "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSDictionary\"32@\"NSData\"40"
- "v48@0:8@\"NSString\"16@\"NSData\"24I32B36i40B44"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24I32B36i40B44"
- "zone"

```
