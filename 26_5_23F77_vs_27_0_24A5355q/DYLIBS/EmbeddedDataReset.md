## EmbeddedDataReset

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset`

```diff

-56.4.1.0.0
-  __TEXT.__text: 0x25c8
-  __TEXT.__auth_stubs: 0x2b0
+58.0.0.0.0
+  __TEXT.__text: 0x2258
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x26f
-  __TEXT.__gcc_except_tab: 0x15c
+  __TEXT.__cstring: 0x277
+  __TEXT.__gcc_except_tab: 0x104
   __TEXT.__oslogstring: 0x48c
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0xadc
-  __TEXT.__objc_methtype: 0x286
-  __TEXT.__objc_stubs: 0x720
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x830
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x2a0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0D3725A3-8590-31CC-9E2C-61E8AC268773
+  UUID: 2CF0BE3F-B764-3A87-B160-5C69DF0BEBD5
   Functions: 67
-  Symbols:   361
-  CStrings:  250
+  Symbols:   366
+  CStrings:  61
 
Symbols:
+ ___41-[DDRResetService dataResetXPCConnection]_block_invoke.71
+ ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.74
+ ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.57
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x8
- ___41-[DDRResetService dataResetXPCConnection]_block_invoke.72
- ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.75
- ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.58
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ _DDRLogForCategory : 104 -> 96
~ +[DDRResetService sharedInstance] : 176 -> 160
~ ___33+[DDRResetService sharedInstance]_block_invoke : 176 -> 172
~ ___30-[DDRResetService addOberver:]_block_invoke : 528 -> 448
~ ___34-[DDRResetService removeObserver:]_block_invoke : 352 -> 288
~ -[DDRResetService observerNonLaunchingXPCConnection] : 704 -> 620
~ ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke : 140 -> 136
~ ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.58 -> ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.57 : 140 -> 136
~ -[DDRResetService dataResetXPCConnection] : 796 -> 704
~ ___41-[DDRResetService dataResetXPCConnection]_block_invoke : 140 -> 136
~ ___41-[DDRResetService dataResetXPCConnection]_block_invoke.72 -> ___41-[DDRResetService dataResetXPCConnection]_block_invoke.71 : 140 -> 136
~ -[DDRResetService notifyClientsOfResetFailedWithErrorCode:] : 256 -> 248
~ -[DDRResetService resetWithRequest:completion:] : 956 -> 880
~ ___47-[DDRResetService resetWithRequest:completion:]_block_invoke : 252 -> 204
~ ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.75 -> ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.74 : 172 -> 168
~ -[DDRResetService invalidate] : 136 -> 132
~ -[DDRResetService willBeginDataResetWithMode:] : 560 -> 548
~ -[DDRResetService didBeginDataResetWithMode:] : 560 -> 548
~ -[DDRResetService didCompleteDataResetMode:withError:completion:] : 808 -> 804
~ -[DDRResetService setDataResetXPCConnection:] : 64 -> 12
~ -[DDRResetService setObserverNonLaunchingXPCConnection:] : 64 -> 12
~ -[DDRResetService setObervers:] : 64 -> 12
~ -[DDRResetService setObserverQueue:] : 64 -> 12
~ -[DDRResetOptions initWithCoder:] : 312 -> 300
~ -[DDRResetOptions encodeWithCoder:] : 292 -> 280
~ -[DDRResetOptions setBootstrapToken:] : 64 -> 12
~ -[DDRResetOptions setRevertToSnapshotName:] : 64 -> 12
~ -[DDRResetRequest initWithMode:options:reason:] : 152 -> 160
~ -[DDRResetRequest initWithCoder:] : 172 -> 160
~ -[DDRResetRequest encodeWithCoder:] : 136 -> 128
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"DDRResetOptions\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DDRClientObserverProtocol"
- "DDRClientResetProtocol"
- "DDRResetOptions"
- "DDRResetRequest"
- "DDRResetService"
- "DDRServerObserverProtocol"
- "DDRServerProtocol"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"DDRResetOptions\",R,N,V_options"
- "T@\"NSArray\",C,N,V_exclusionPaths"
- "T@\"NSData\",&,N,V_bootstrapToken"
- "T@\"NSHashTable\",&,N,V_obervers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_observerQueue"
- "T@\"NSString\",&,N,V_revertToSnapshotName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_reason"
- "T@\"NSXPCConnection\",&,N,V_dataResetXPCConnection"
- "T@\"NSXPCConnection\",&,N,V_observerNonLaunchingXPCConnection"
- "TB,N,V_disallowProximitySetup"
- "TB,N,V_eraseDataPlan"
- "TB,N,V_hideProgress"
- "TB,N,V_invalidated"
- "TB,R"
- "TQ,R"
- "Ti,N,V_currentResetState"
- "Tq,N,V_mode"
- "Tq,R,N,V_mode"
- "T{os_unfair_lock_s=I},N,V_lock"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_bootstrapToken"
- "_currentResetState"
- "_dataResetXPCConnection"
- "_disallowProximitySetup"
- "_eraseDataPlan"
- "_exclusionPaths"
- "_hideProgress"
- "_invalidated"
- "_lock"
- "_mode"
- "_obervers"
- "_observerNonLaunchingXPCConnection"
- "_observerQueue"
- "_options"
- "_reason"
- "_revertToSnapshotName"
- "_xpcConnection"
- "addOberver:"
- "addObject:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "connect"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentResetState"
- "dataResetXPCConnection"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "didBeginDataResetWithMode:"
- "didCompleteDataResetMode:withError:completion:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithMode:options:reason:"
- "interfaceWithProtocol:"
- "invalidate"
- "invalidated"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lock"
- "notifyClientsOfResetFailedWithErrorCode:"
- "obervers"
- "observerNonLaunchingXPCConnection"
- "observerQueue"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "release"
- "remoteObjectProxy"
- "removeObject:"
- "removeObserver:"
- "resetDataWithRequest:completion:"
- "resetService:didBeginDataResetWithMode:"
- "resetService:didCompleteDataResetMode:withError:completion:"
- "resetService:willBeginDataResetWithMode:"
- "resetWithRequest:completion:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setBootstrapToken:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCurrentResetState:"
- "setDataResetXPCConnection:"
- "setDisallowProximitySetup:"
- "setEraseDataPlan:"
- "setExclusionPaths:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHideProgress:"
- "setInterruptionHandler:"
- "setInvalidated:"
- "setInvalidationHandler:"
- "setLock:"
- "setMode:"
- "setObervers:"
- "setObserverNonLaunchingXPCConnection:"
- "setObserverQueue:"
- "setRemoteObjectInterface:"
- "setRevertToSnapshotName:"
- "setWithObjects:"
- "sharedInstance"
- "superclass"
- "supportsSecureCoding"
- "sync"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@\"DDRResetRequest\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8q16@\"NSError\"24@?<v@?>32"
- "v40@0:8q16@24@?32"
- "weakObjectsHashTable"
- "willBeginDataResetWithMode:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
