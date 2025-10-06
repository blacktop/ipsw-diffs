## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-342.4.1.0.0
-  __TEXT.__text: 0x2454c
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x17a4
+344.25.0.0.0
+  __TEXT.__text: 0x254b4
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x197c
   __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x3943
-  __TEXT.__oslogstring: 0x1986
+  __TEXT.__cstring: 0x3b0b
+  __TEXT.__oslogstring: 0x1987
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x6b0
-  __TEXT.__objc_classname: 0x324
-  __TEXT.__objc_methname: 0x3bcf
-  __TEXT.__objc_methtype: 0x8fe
-  __TEXT.__objc_stubs: 0x2480
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__unwind_info: 0x700
+  __TEXT.__objc_classname: 0x34d
+  __TEXT.__objc_methname: 0x402e
+  __TEXT.__objc_methtype: 0x996
+  __TEXT.__objc_stubs: 0x2580
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37c0
-  __DATA_CONST.__objc_selrefs: 0x1078
+  __DATA_CONST.__objc_const: 0x3b30
+  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x3b0
-  __AUTH_CONST.__objc_const: 0xd68
+  __AUTH_CONST.__objc_const: 0xe88
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x32c0
+  __AUTH_CONST.__cfstring: 0x34e0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0xb8
-  __DATA.__objc_ivar: 0x1e4
+  __AUTH_CONST.__auth_got: 0x650
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x3d0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB691E2D-B4FB-3AA6-9AB1-FFB450114FA2
-  Functions: 613
-  Symbols:   2254
-  CStrings:  2075
+  UUID: 76B36CC3-8FF1-375B-84B1-09A3AFD4729A
+  Functions: 660
+  Symbols:   2404
+  CStrings:  2162
 
Symbols:
+ +[NFAssertionInternal supportsSecureCoding]
+ +[NFCardSessionConfig configWithInitialUIText:]
+ +[NFCardSessionConfig supportsSecureCoding]
+ -[NFAssertionInternal .cxx_destruct]
+ -[NFAssertionInternal assertionTime]
+ -[NFAssertionInternal assertionType]
+ -[NFAssertionInternal description]
+ -[NFAssertionInternal encodeWithCoder:]
+ -[NFAssertionInternal hash]
+ -[NFAssertionInternal initWithCoder:]
+ -[NFAssertionInternal initWithDictionary:]
+ -[NFAssertionInternal isEqual:]
+ -[NFAssertionInternal pid]
+ -[NFAssertionInternal sessionID]
+ -[NFCardSessionConfig .cxx_destruct]
+ -[NFCardSessionConfig copyWithZone:]
+ -[NFCardSessionConfig encodeWithCoder:]
+ -[NFCardSessionConfig initWithCoder:]
+ -[NFCardSessionConfig initialUIText]
+ -[NFCardSessionConfig setInitialUIText:]
+ -[NFCommandAPDU isSecureMessaging]
+ -[NFSecureXPCEventPublisher _sendDictionary:dispatch:]
+ -[NFSecureXPCEventPublisher _sendEvent:dispatch:]
+ -[NFSecureXPCEventPublisher _sendSimpleEvent:dispatch:]
+ -[NFSecureXPCEventPublisher _sendSimpleEvent:objectNumber:dispatch:]
+ -[NFSecureXPCEventPublisher _sendSimpleEvent:objectString:dispatch:]
+ -[NFSecureXPCEventPublisher _syncSetupConnection]
+ -[NFSecureXPCEventPublisher asyncSendDictionary:]
+ -[NFSecureXPCEventPublisher asyncSendSimpleEvent:]
+ -[NFSecureXPCEventPublisher asyncSendSimpleEvent:objectNumber:]
+ -[NFSecureXPCEventPublisher asyncSendSimpleEvent:objectString:]
+ -[NFSecureXPCEventPublisher connectionLock]
+ -[NFSecureXPCEventPublisher eventSendQueue]
+ -[NFSecureXPCEventPublisher initWithMachPort:xpcConnectionQueue:eventSendQueue:]
+ -[NFSecureXPCEventPublisher invalidate]
+ -[NFSecureXPCEventPublisher setConnectionLock:]
+ -[NFSecureXPCEventPublisher setEventSendQueue:]
+ -[NFSecureXPCEventPublisher setXpcConnectionQueue:]
+ -[NFSecureXPCEventPublisher xpcConnectionQueue]
+ -[NFServiceWhitelistChecker _initCardSessionEntitlementsWithSecTask:]
+ -[NFServiceWhitelistChecker nfcCardSessionAIDPrefixList]
+ -[NFServiceWhitelistChecker nfcCardSessionAccess]
+ -[NSXPCConnection(NFUserInfo) NF_clearPresentmentIntentSuppressionHolder]
+ -[NSXPCConnection(NFUserInfo) NF_presentmentIntentSuppressionHolder]
+ -[NSXPCConnection(NFUserInfo) NF_setPresentmentIntentSuppressionHolder]
+ _NFIsDeviceAnIPadWithLPMSupport
+ _OBJC_CLASS_$_NFAssertionInternal
+ _OBJC_CLASS_$_NFCardSessionConfig
+ _OBJC_IVAR_$_NFAssertionInternal._assertionTime
+ _OBJC_IVAR_$_NFAssertionInternal._assertionType
+ _OBJC_IVAR_$_NFAssertionInternal._pid
+ _OBJC_IVAR_$_NFCardSessionConfig._initialUIText
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._connectionLock
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._eventSendQueue
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._xpcConnectionQueue
+ _OBJC_IVAR_$_NFServiceWhitelistChecker._nfcCardSessionAIDPrefixList
+ _OBJC_IVAR_$_NFServiceWhitelistChecker._nfcCardSessionAccess
+ _OBJC_METACLASS_$_NFAssertionInternal
+ _OBJC_METACLASS_$_NFCardSessionConfig
+ __OBJC_$_CLASS_METHODS_NFAssertionInternal
+ __OBJC_$_CLASS_METHODS_NFCardSessionConfig
+ __OBJC_$_CLASS_PROP_LIST_NFAssertionInternal
+ __OBJC_$_CLASS_PROP_LIST_NFCardSessionConfig
+ __OBJC_$_INSTANCE_METHODS_NFAssertionInternal
+ __OBJC_$_INSTANCE_METHODS_NFCardSessionConfig
+ __OBJC_$_INSTANCE_VARIABLES_NFAssertionInternal
+ __OBJC_$_INSTANCE_VARIABLES_NFCardSessionConfig
+ __OBJC_$_PROP_LIST_NFAssertionInternal
+ __OBJC_$_PROP_LIST_NFCardSessionConfig
+ __OBJC_CLASS_PROTOCOLS_$_NFAssertionInternal
+ __OBJC_CLASS_PROTOCOLS_$_NFCardSessionConfig
+ __OBJC_CLASS_RO_$_NFAssertionInternal
+ __OBJC_CLASS_RO_$_NFCardSessionConfig
+ __OBJC_METACLASS_RO_$_NFAssertionInternal
+ __OBJC_METACLASS_RO_$_NFCardSessionConfig
+ ___39-[NFSecureXPCEventPublisher invalidate]_block_invoke
+ ___49-[NFSecureXPCEventPublisher _sendEvent:dispatch:]_block_invoke
+ ___49-[NFSecureXPCEventPublisher _sendEvent:dispatch:]_block_invoke.14
+ ___49-[NFSecureXPCEventPublisher _sendEvent:dispatch:]_block_invoke_2
+ ___49-[NFSecureXPCEventPublisher _syncSetupConnection]_block_invoke
+ ___49-[NFSecureXPCEventPublisher _syncSetupConnection]_block_invoke.4
+ ___80-[NFSecureXPCEventPublisher initWithMachPort:xpcConnectionQueue:eventSendQueue:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___kCFBooleanTrue
+ __unnamed_array_storage.201
+ __unnamed_array_storage.202
+ _malloc_type_calloc
+ _objc_msgSend$_initCardSessionEntitlementsWithSecTask:
+ _objc_msgSend$_syncSetupConnection
+ _objc_msgSend$assertionTime
+ _objc_msgSend$assertionType
+ _objc_msgSend$eventSendQueue
+ _objc_msgSend$hash
+ _objc_msgSend$initWithMachPort:xpcConnectionQueue:eventSendQueue:
+ _objc_msgSend$initialUIText
+ _objc_msgSend$pid
+ _objc_msgSend$setInitialUIText:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_retain_x10
+ _objc_retain_x25
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[NFSecureXPCEventPublisher _setupConnection]
- -[NFSecureXPCEventPublisher queue]
- -[NFSecureXPCEventPublisher sendEvent:]
- -[NFSecureXPCEventPublisher setQueue:]
- _OBJC_IVAR_$_NFSecureXPCEventPublisher._queue
- ___39-[NFSecureXPCEventPublisher sendEvent:]_block_invoke
- ___45-[NFSecureXPCEventPublisher _setupConnection]_block_invoke
- __unnamed_array_storage.198
- __unnamed_array_storage.199
- _malloc_type_malloc
- _objc_msgSend$_setupConnection
- _objc_msgSend$queue
- _objc_msgSend$sendEvent:
CStrings:
+ "\x02\x11\x112"
+ "\x14"
+ "%c[%{public}s %{public}s]:%i Service unavailable: %{public}@"
+ "%c[%{public}s %{public}s]:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@"
+ "%s:%i Failed to alloc %ld"
+ "%{public}s:%i Failed to alloc %ld"
+ "@\"NSDate\""
+ "@40@0:8@16@24@32"
+ "Assertion Type = %@ for PID %d, taken at %@"
+ "Assertion-PowerUp-%d-%lf"
+ "CardSession: %@"
+ "CardSessionAIDPrefixList: %@"
+ "NFAssertionInternal"
+ "NFAssertionPID"
+ "NFAssertionTime"
+ "NFAssertionType"
+ "NFCardSessionConfig"
+ "NF_clearPresentmentIntentSuppressionHolder"
+ "NF_presentmentIntentSuppressionHolder"
+ "NF_setPresentmentIntentSuppressionHolder"
+ "No Reset"
+ "Power Up"
+ "Presentment intent suppression"
+ "PresentmentIntentSuppressionHolder"
+ "Prevent Background Tag Reading"
+ "Prevent Connection Handover"
+ "T@\"NSDate\",R,V_assertionTime"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_eventSendQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcConnectionQueue"
+ "T@\"NSOrderedSet\",R,N"
+ "T@\"NSString\",&,N,V_initialUIText"
+ "T@\"NSString\",?,R,C"
+ "TQ,R,V_assertionType"
+ "Ti,R,V_pid"
+ "T{os_unfair_lock_s=I},N,V_connectionLock"
+ "_assertionTime"
+ "_assertionType"
+ "_connectionLock"
+ "_eventSendQueue"
+ "_initCardSessionEntitlementsWithSecTask:"
+ "_initialUIText"
+ "_nfcCardSessionAIDPrefixList"
+ "_nfcCardSessionAccess"
+ "_pid"
+ "_sendDictionary:dispatch:"
+ "_sendEvent:dispatch:"
+ "_syncSetupConnection"
+ "_xpcConnectionQueue"
+ "assertionTime"
+ "assertionType"
+ "asyncSendDictionary:"
+ "asyncSendSimpleEvent:"
+ "asyncSendSimpleEvent:objectNumber:"
+ "asyncSendSimpleEvent:objectString:"
+ "com.apple.developer.nfc.hce"
+ "com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes"
+ "com.apple.nfcd.generalTransactionStatisticDim"
+ "configWithInitialUIText:"
+ "connectionLock"
+ "eventSendQueue"
+ "initWithMachPort:xpcConnectionQueue:eventSendQueue:"
+ "initialUIText"
+ "isSecureMessaging"
+ "nfcCardSessionAIDPrefixList"
+ "nfcCardSessionAccess"
+ "pid"
+ "sessionID"
+ "setConnectionLock:"
+ "setEventSendQueue:"
+ "setInitialUIText:"
+ "setXpcConnectionQueue:"
+ "timeIntervalSinceReferenceDate"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8^{__SecTask=}16"
+ "xpcConnectionQueue"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "\x02\x11B"
- "\x03"
- "%c[%{public}s %{public}s]:%i Notification is being dropped due to no valid connection"
- "%c[%{public}s %{public}s]:%i Service unavailable: %{public}@ - re-create it"
- "%s:%i Failed to malloc %ld"
- "%{public}s:%i Failed to malloc %ld"
- "_setupConnection"
- "sendEvent:"

```
