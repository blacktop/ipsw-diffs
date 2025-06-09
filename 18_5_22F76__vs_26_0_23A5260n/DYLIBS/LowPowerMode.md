## LowPowerMode

> `/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode`

```diff

-1754.120.2.0.0
-  __TEXT.__text: 0x4124
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x4a4
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__cstring: 0x1e8
-  __TEXT.__oslogstring: 0x4b2
-  __TEXT.__unwind_info: 0x1a0
-  __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x5a2
-  __TEXT.__objc_methtype: 0x193
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x1b0
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x28
+1846.0.7.0.0
+  __TEXT.__text: 0x5ee8
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_methlist: 0x94c
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0xd8
+  __TEXT.__cstring: 0x3c5
+  __TEXT.__oslogstring: 0x677
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x1ab
+  __TEXT.__objc_methname: 0xedc
+  __TEXT.__objc_methtype: 0x3ab
+  __TEXT.__objc_stubs: 0xa60
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x170
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x540
-  __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x1e0
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__objc_const: 0xc38
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0x420
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 699D7A42-9612-3378-9BC6-9148CC9B4F06
-  Functions: 136
-  Symbols:   535
-  CStrings:  177
+  UUID: 72A5CE08-A5DE-3370-AE1A-E86E9C6604ED
+  Functions: 209
+  Symbols:   838
+  CStrings:  371
 
Symbols:
+ +[PMPowerMitigationSession supportsSecureCoding]
+ +[PMPowerMitigations sharedInstance]
+ +[PMPowerMitigations sharedInstance].cold.1
+ +[_PMWeakProxy proxyWithTarget:]
+ -[PMPowerMitigationInfo .cxx_destruct]
+ -[PMPowerMitigationInfo clientIdentifier]
+ -[PMPowerMitigationInfo initWithMitigationLevel:]
+ -[PMPowerMitigationInfo initWithMitigationLevel:clientIdentifier:]
+ -[PMPowerMitigationInfo mitigationLevel]
+ -[PMPowerMitigationSession .cxx_destruct]
+ -[PMPowerMitigationSession description]
+ -[PMPowerMitigationSession encodeWithCoder:]
+ -[PMPowerMitigationSession engagementReason]
+ -[PMPowerMitigationSession initWithCoder:]
+ -[PMPowerMitigationSession initWithSource:reason:level:]
+ -[PMPowerMitigationSession initWithSource:reason:level:duration:]
+ -[PMPowerMitigationSession isTimedSession]
+ -[PMPowerMitigationSession sessionSource]
+ -[PMPowerMitigationSession systemWideMitigationLevel]
+ -[PMPowerMitigationSession timeDuration]
+ -[PMPowerMitigations .cxx_destruct]
+ -[PMPowerMitigations addObserver:forClientIdentifier:]
+ -[PMPowerMitigations configureConnectionInterruptionHandler]
+ -[PMPowerMitigations configureConnectionInvalidationHandler]
+ -[PMPowerMitigations configureConnectionReconnectionOnServiceRestart]
+ -[PMPowerMitigations configureConnectionReconnectionOnServiceRestart].cold.1
+ -[PMPowerMitigations connectionInterrupted]
+ -[PMPowerMitigations connection]
+ -[PMPowerMitigations copyCurrentMitigationInfoForClientIdentifier:]
+ -[PMPowerMitigations currentMitigationSession]
+ -[PMPowerMitigations didUpdateToMitigation:fromMitigation:]
+ -[PMPowerMitigations getCurrentMitigationInfoForClientIdentifier:]
+ -[PMPowerMitigations initConnectionToService]
+ -[PMPowerMitigations initConnectionToService].cold.1
+ -[PMPowerMitigations init]
+ -[PMPowerMitigations log]
+ -[PMPowerMitigations newMitigationInfoForClientIdentifier:]
+ -[PMPowerMitigations observersByClientId]
+ -[PMPowerMitigations queue]
+ -[PMPowerMitigations registerForMitigationUpdates]
+ -[PMPowerMitigations removeObserver:forClientIdentifier:]
+ -[PMPowerMitigations setConnection:]
+ -[PMPowerMitigations setConnectionInterrupted:]
+ -[PMPowerMitigations setCurrentMitigationSession:]
+ -[PMPowerMitigations setLog:]
+ -[PMPowerMitigations setObserversByClientId:]
+ -[PMPowerMitigations setQueue:]
+ -[_PMWeakProxy .cxx_destruct]
+ -[_PMWeakProxy class]
+ -[_PMWeakProxy conformsToProtocol:]
+ -[_PMWeakProxy debugDescription]
+ -[_PMWeakProxy description]
+ -[_PMWeakProxy forwardInvocation:]
+ -[_PMWeakProxy hash]
+ -[_PMWeakProxy initWithTarget:]
+ -[_PMWeakProxy isEqual:]
+ -[_PMWeakProxy isKindOfClass:]
+ -[_PMWeakProxy methodSignatureForSelector:]
+ -[_PMWeakProxy respondsToSelector:]
+ -[_PMWeakProxy target]
+ GCC_except_table4
+ GCC_except_table6
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSMethodSignature
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSProxy
+ _OBJC_CLASS_$_PMPowerMitigationInfo
+ _OBJC_CLASS_$_PMPowerMitigationSession
+ _OBJC_CLASS_$_PMPowerMitigations
+ _OBJC_CLASS_$__PMWeakProxy
+ _OBJC_IVAR_$_PMPowerMitigationInfo._clientIdentifier
+ _OBJC_IVAR_$_PMPowerMitigationInfo._mitigationLevel
+ _OBJC_IVAR_$_PMPowerMitigationSession._engagementReason
+ _OBJC_IVAR_$_PMPowerMitigationSession._sessionSource
+ _OBJC_IVAR_$_PMPowerMitigationSession._systemWideMitigationLevel
+ _OBJC_IVAR_$_PMPowerMitigationSession._timeDuration
+ _OBJC_IVAR_$_PMPowerMitigations._connection
+ _OBJC_IVAR_$_PMPowerMitigations._connectionInterrupted
+ _OBJC_IVAR_$_PMPowerMitigations._currentMitigationSession
+ _OBJC_IVAR_$_PMPowerMitigations._log
+ _OBJC_IVAR_$_PMPowerMitigations._observersByClientId
+ _OBJC_IVAR_$_PMPowerMitigations._queue
+ _OBJC_IVAR_$__PMWeakProxy._target
+ _OBJC_METACLASS_$_NSProxy
+ _OBJC_METACLASS_$_PMPowerMitigationInfo
+ _OBJC_METACLASS_$_PMPowerMitigationSession
+ _OBJC_METACLASS_$_PMPowerMitigations
+ _OBJC_METACLASS_$__PMWeakProxy
+ __OBJC_$_CLASS_METHODS_PMPowerMitigationSession
+ __OBJC_$_CLASS_METHODS_PMPowerMitigations
+ __OBJC_$_CLASS_METHODS__PMWeakProxy
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_PMPowerMitigationSession
+ __OBJC_$_INSTANCE_METHODS_PMPowerMitigationInfo
+ __OBJC_$_INSTANCE_METHODS_PMPowerMitigationSession
+ __OBJC_$_INSTANCE_METHODS_PMPowerMitigations
+ __OBJC_$_INSTANCE_METHODS__PMWeakProxy
+ __OBJC_$_INSTANCE_VARIABLES_PMPowerMitigationInfo
+ __OBJC_$_INSTANCE_VARIABLES_PMPowerMitigationSession
+ __OBJC_$_INSTANCE_VARIABLES_PMPowerMitigations
+ __OBJC_$_INSTANCE_VARIABLES__PMWeakProxy
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_PMPowerMitigationInfo
+ __OBJC_$_PROP_LIST_PMPowerMitigationSession
+ __OBJC_$_PROP_LIST_PMPowerMitigations
+ __OBJC_$_PROP_LIST__PMWeakProxy
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PMPowerMitigationsObservable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PMPowerMitigationsServiceCallbackProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PMPowerMitigationsServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PMPowerMitigationsObservable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PMPowerMitigationsServiceCallbackProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PMPowerMitigationsServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_PMPowerMitigationsObservable
+ __OBJC_CLASS_PROTOCOLS_$_PMPowerMitigationSession
+ __OBJC_CLASS_PROTOCOLS_$_PMPowerMitigations
+ __OBJC_CLASS_RO_$_PMPowerMitigationInfo
+ __OBJC_CLASS_RO_$_PMPowerMitigationSession
+ __OBJC_CLASS_RO_$_PMPowerMitigations
+ __OBJC_CLASS_RO_$__PMWeakProxy
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_PMPowerMitigationsObservable
+ __OBJC_LABEL_PROTOCOL_$_PMPowerMitigationsServiceCallbackProtocol
+ __OBJC_LABEL_PROTOCOL_$_PMPowerMitigationsServiceProtocol
+ __OBJC_METACLASS_RO_$_PMPowerMitigationInfo
+ __OBJC_METACLASS_RO_$_PMPowerMitigationSession
+ __OBJC_METACLASS_RO_$_PMPowerMitigations
+ __OBJC_METACLASS_RO_$__PMWeakProxy
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_PMPowerMitigationsObservable
+ __OBJC_PROTOCOL_$_PMPowerMitigationsServiceCallbackProtocol
+ __OBJC_PROTOCOL_$_PMPowerMitigationsServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_PMPowerMitigationsServiceCallbackProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_PMPowerMitigationsServiceProtocol
+ ___36+[PMPowerMitigations sharedInstance]_block_invoke
+ ___50-[PMPowerMitigations registerForMitigationUpdates]_block_invoke
+ ___50-[PMPowerMitigations registerForMitigationUpdates]_block_invoke.cold.1
+ ___54-[PMPowerMitigations addObserver:forClientIdentifier:]_block_invoke
+ ___57-[PMPowerMitigations removeObserver:forClientIdentifier:]_block_invoke
+ ___59-[PMPowerMitigations didUpdateToMitigation:fromMitigation:]_block_invoke
+ ___60-[PMPowerMitigations configureConnectionInterruptionHandler]_block_invoke
+ ___60-[PMPowerMitigations configureConnectionInvalidationHandler]_block_invoke
+ ___60-[PMPowerMitigations configureConnectionInvalidationHandler]_block_invoke.cold.1
+ ___67-[PMPowerMitigations copyCurrentMitigationInfoForClientIdentifier:]_block_invoke
+ ___69-[PMPowerMitigations configureConnectionReconnectionOnServiceRestart]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ __os_log_debug_impl
+ _configureConnectionReconnectionOnServiceRestart.syncToken
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_sync
+ _kPMLPMSourceIBLM
+ _kPMLPMSourceStandbyMode
+ _kPowerMitigationsManagerService
+ _kPowerMitigationsManagerServiceStartupNotify
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_getProperty
+ _objc_msgSend$activate
+ _objc_msgSend$addObject:
+ _objc_msgSend$configureConnectionInterruptionHandler
+ _objc_msgSend$configureConnectionInvalidationHandler
+ _objc_msgSend$configureConnectionReconnectionOnServiceRestart
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$connection
+ _objc_msgSend$connectionInterrupted
+ _objc_msgSend$copyCurrentMitigationInfoForClientIdentifier:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$currentMitigationSession
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$dictionary
+ _objc_msgSend$didChangeToMitigations:withSessionInfo:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$hash
+ _objc_msgSend$initConnectionToService
+ _objc_msgSend$initWithMitigationLevel:clientIdentifier:
+ _objc_msgSend$initWithSource:reason:level:duration:
+ _objc_msgSend$initWithTarget:
+ _objc_msgSend$invoke
+ _objc_msgSend$isEqual:
+ _objc_msgSend$log
+ _objc_msgSend$methodReturnType
+ _objc_msgSend$methodSignature
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$newMitigationInfoForClientIdentifier:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$observersByClientId
+ _objc_msgSend$registerForMitigationUpdates
+ _objc_msgSend$registerForPowerMitigations
+ _objc_msgSend$removeObject:
+ _objc_msgSend$selector
+ _objc_msgSend$sessionSource
+ _objc_msgSend$set
+ _objc_msgSend$setConnectionInterrupted:
+ _objc_msgSend$setCurrentMitigationSession:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setReturnValue:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$signatureWithObjCTypes:
+ _objc_msgSend$systemWideMitigationLevel
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retain_x22
+ _objc_retain_x8
+ _objc_setProperty_atomic
+ _objc_storeWeak
+ _sharedInstance.instance
CStrings:
+ "#16@0:8"
+ "%@ has restarted"
+ "<%@: %p, target: %@ (%@)>"
+ "<%@: %p, target: %@>"
+ "<PMPowerMitigationSession: Level %ld, sessionSource %@>"
+ "@"
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSString\"16@0:8"
+ "@\"PMPowerMitigationInfo\"24@0:8@\"NSString\"16"
+ "@\"PMPowerMitigationSession\""
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@24@0:8q16"
+ "@32@0:8:16@24"
+ "@32@0:8q16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16q24q32"
+ "@48@0:8@16q24q32d40"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "Connection to %@ interrupted"
+ "Connection to %@ invalidated"
+ "Failed to connect to %@"
+ "Failed to connect to service. Error: %@"
+ "Failed to register for reconnections with service with status:0x%x"
+ "IBLM"
+ "NSCoding"
+ "NSObject"
+ "NSSecureCoding"
+ "PMPowerMitigationInfo"
+ "PMPowerMitigationSession"
+ "PMPowerMitigations"
+ "PMPowerMitigationsObservable"
+ "PMPowerMitigationsServiceCallbackProtocol"
+ "PMPowerMitigationsServiceProtocol"
+ "Q16@0:8"
+ "Received updated PowerMitigationSession info with level: %ld triggered by source %@."
+ "Registering for mitigation updates with %@"
+ "StandbyMode"
+ "T#,R"
+ "T@\"NSMutableDictionary\",&,V_observersByClientId"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSObject<OS_os_log>\",&,V_log"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,C,N,V_clientIdentifier"
+ "T@\"NSString\",R,C,N,V_sessionSource"
+ "T@\"PMPowerMitigationSession\",&,V_currentMitigationSession"
+ "T@,R,W,N"
+ "TB,R"
+ "TB,V_connectionInterrupted"
+ "TQ,R"
+ "Td,R,N,V_timeDuration"
+ "Tq,R,N,V_engagementReason"
+ "Tq,R,N,V_mitigationLevel"
+ "Tq,R,N,V_systemWideMitigationLevel"
+ "Updating observers as mitigation levels have changed."
+ "Updating observers for clientId: %@"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_PMWeakProxy"
+ "_clientIdentifier"
+ "_connectionInterrupted"
+ "_currentMitigationSession"
+ "_engagementReason"
+ "_log"
+ "_mitigationLevel"
+ "_observersByClientId"
+ "_queue"
+ "_sessionSource"
+ "_systemWideMitigationLevel"
+ "_target"
+ "_timeDuration"
+ "activate"
+ "addObject:"
+ "addObserver:forClientIdentifier:"
+ "autorelease"
+ "class"
+ "clientIdentifier"
+ "com.apple.lowpowermode"
+ "com.apple.lowpowermode.pmpowermitigations.queue"
+ "com.apple.pmpowermitigations.update"
+ "com.apple.powerexperienced.powermitigationsmanager.restart"
+ "com.apple.powerexperienced.powermitigationsmanager.service"
+ "com.apple.powerexperienced.restart"
+ "configureConnectionInterruptionHandler"
+ "configureConnectionInvalidationHandler"
+ "configureConnectionReconnectionOnServiceRestart"
+ "conformsToProtocol:"
+ "connectionInterrupted"
+ "copyCurrentMitigationInfoForClientIdentifier:"
+ "countByEnumeratingWithState:objects:count:"
+ "currentMitigationSession"
+ "d"
+ "d16@0:8"
+ "debugDescription"
+ "decodeDoubleForKey:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "description"
+ "dictionary"
+ "didChangeToMitigations:withSessionInfo:"
+ "didUpdateToMitigation:fromMitigation:"
+ "encodeDouble:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "engagementReason"
+ "established connection to %@"
+ "forwardInvocation:"
+ "getCurrentMitigationInfoForClientIdentifier:"
+ "hash"
+ "initConnectionToService"
+ "initWithCoder:"
+ "initWithMitigationLevel:"
+ "initWithMitigationLevel:clientIdentifier:"
+ "initWithSource:reason:level:"
+ "initWithSource:reason:level:duration:"
+ "initWithTarget:"
+ "invoke"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isTimedSession"
+ "log"
+ "methodReturnType"
+ "methodSignature"
+ "methodSignatureForSelector:"
+ "mitigationLevel"
+ "newMitigationInfoForClientIdentifier:"
+ "nil"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "observersByClientId"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "proxyWithTarget:"
+ "q"
+ "queue"
+ "registerForMitigationUpdates"
+ "registerForPowerMitigations"
+ "release"
+ "removeObject:"
+ "removeObserver:forClientIdentifier:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "selector"
+ "self"
+ "sessionSource"
+ "set"
+ "setConnectionInterrupted:"
+ "setCurrentMitigationSession:"
+ "setLog:"
+ "setObject:forKeyedSubscript:"
+ "setObserversByClientId:"
+ "setQueue:"
+ "setReturnValue:"
+ "setTarget:"
+ "signatureWithObjCTypes:"
+ "superclass"
+ "supportsSecureCoding"
+ "systemWideMitigationLevel"
+ "target"
+ "timeDuration"
+ "v24@0:8@\"NSCoder\"16"
+ "v32@0:8@\"<PMPowerMitigationsObserver>\"16@\"NSString\"24"
+ "v32@0:8@\"PMPowerMitigationSession\"16@\"PMPowerMitigationSession\"24"
+ "v32@0:8@16@24"
+ "v@:"
+ "zone"

```
