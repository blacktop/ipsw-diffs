## IASUtilities

> `/System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities`

```diff

-657.0.0.0.0
-  __TEXT.__text: 0x183a0
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x1aa8
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x2d78
-  __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__unwind_info: 0x638
+658.0.0.0.0
+  __TEXT.__text: 0x1589c
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x1758
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x29df
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__unwind_info: 0x550
   __TEXT.__eh_frame: 0x168
-  __TEXT.__objc_classname: 0x427
-  __TEXT.__objc_methname: 0x51b7
-  __TEXT.__objc_methtype: 0x12a6
-  __TEXT.__objc_stubs: 0x4600
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__objc_classname: 0x37d
+  __TEXT.__objc_methname: 0x492e
+  __TEXT.__objc_methtype: 0x10cc
+  __TEXT.__objc_stubs: 0x3f60
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1808
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0x15d0
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x2180
-  __AUTH_CONST.__objc_const: 0x3aa0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x1fc0
+  __AUTH_CONST.__objc_const: 0x3530
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x480
-  __DATA.__bss: 0xe0
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x198
+  __DATA.__data: 0x300
+  __DATA.__bss: 0xb8
   __DATA.__common: 0x1
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa

   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 542
-  Symbols:   1957
-  CStrings:  1708
+  Functions: 457
+  Symbols:   1720
+  CStrings:  1563
 
Symbols:
- +[IASBootTimeInstallManager initialize]
- +[IASBootTimeInstallManager managerForVolume:error:]
- +[IASBootTimeInstallableItem supportsSecureCoding]
- -[IASBootTimeInstallClient .cxx_destruct]
- -[IASBootTimeInstallClient bootTimeInstallProgress:estimatedTimeRemaining:status:]
- -[IASBootTimeInstallClient connection]
- -[IASBootTimeInstallClient description]
- -[IASBootTimeInstallClient initWithConnection:]
- -[IASBootTimeInstallClient name]
- -[IASBootTimeInstallClient path]
- -[IASBootTimeInstallClient pid]
- -[IASBootTimeInstallClient setConnection:]
- -[IASBootTimeInstallClient setName:]
- -[IASBootTimeInstallClient setPath:]
- -[IASBootTimeInstallClient setPid:]
- -[IASBootTimeInstallClient setUid:]
- -[IASBootTimeInstallClient uid]
- -[IASBootTimeInstallManager .cxx_destruct]
- -[IASBootTimeInstallManager bootTimeInstallProgress:estimatedTimeRemaining:status:]
- -[IASBootTimeInstallManager clearQueuedPackagesReturningError:]
- -[IASBootTimeInstallManager connection]
- -[IASBootTimeInstallManager estimatedInstallationTimeForPackages:error:]
- -[IASBootTimeInstallManager initWithVolume:error:]
- -[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]
- -[IASBootTimeInstallManager isRestartRequiredByPackages:error:]
- -[IASBootTimeInstallManager performRestartReturningError:]
- -[IASBootTimeInstallManager progressHandlers]
- -[IASBootTimeInstallManager progressObserversQueue]
- -[IASBootTimeInstallManager queuePackageForInstallation:error:]
- -[IASBootTimeInstallManager queuedPackagesReturningError:]
- -[IASBootTimeInstallManager queuedPackages]
- -[IASBootTimeInstallManager setConnection:]
- -[IASBootTimeInstallManager setProgressHandlers:]
- -[IASBootTimeInstallManager setProgressObserversQueue:]
- -[IASBootTimeInstallManager setVolumeURL:]
- -[IASBootTimeInstallManager volumeURL]
- -[IASBootTimeInstallableItem .cxx_destruct]
- -[IASBootTimeInstallableItem clientIdentifier]
- -[IASBootTimeInstallableItem encodeWithCoder:]
- -[IASBootTimeInstallableItem evaluatorMetaInfo]
- -[IASBootTimeInstallableItem hash]
- -[IASBootTimeInstallableItem initWithCoder:]
- -[IASBootTimeInstallableItem initWithProductAtURL:error:]
- -[IASBootTimeInstallableItem init]
- -[IASBootTimeInstallableItem interfaceType]
- -[IASBootTimeInstallableItem isEqual:]
- -[IASBootTimeInstallableItem isEqualToInstallableItem:]
- -[IASBootTimeInstallableItem productURL]
- -[IASBootTimeInstallableItem setClientIdentifier:]
- -[IASBootTimeInstallableItem setEvaluatorMetaInfo:]
- -[IASBootTimeInstallableItem setInterfaceType:]
- -[IASBootTimeInstallableItem setProductURL:]
- GCC_except_table16
- GCC_except_table21
- GCC_except_table24
- GCC_except_table39
- GCC_except_table42
- IASLogObject.cold.1
- IASLogObject.logObj
- IASLogObject.onceToken
- OBJC_IVAR_$_IASBootTimeInstallClient._connection
- OBJC_IVAR_$_IASBootTimeInstallClient._name
- OBJC_IVAR_$_IASBootTimeInstallClient._path
- OBJC_IVAR_$_IASBootTimeInstallClient._pid
- OBJC_IVAR_$_IASBootTimeInstallClient._uid
- OBJC_IVAR_$_IASBootTimeInstallManager._connection
- OBJC_IVAR_$_IASBootTimeInstallManager._progressHandlers
- OBJC_IVAR_$_IASBootTimeInstallManager._progressObserversQueue
- OBJC_IVAR_$_IASBootTimeInstallManager._volumeURL
- OBJC_IVAR_$_IASBootTimeInstallableItem._clientIdentifier
- OBJC_IVAR_$_IASBootTimeInstallableItem._evaluatorMetaInfo
- OBJC_IVAR_$_IASBootTimeInstallableItem._interfaceType
- OBJC_IVAR_$_IASBootTimeInstallableItem._productURL
- _IASBootTimeInstallManagerAlternateStatusKey
- _IASBootTimeInstallManagerErrorDomain
- _IASBootTimeInstallManagerPrimaryStatusKey
- _IASBootTimeInstallableItemErrorDomain
- _IASLogObject
- _NSURLErrorDomain
- _OBJC_CLASS_$_IASBootTimeInstallClient
- _OBJC_CLASS_$_IASBootTimeInstallManager
- _OBJC_CLASS_$_IASBootTimeInstallableItem
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_METACLASS_$_IASBootTimeInstallClient
- _OBJC_METACLASS_$_IASBootTimeInstallManager
- _OBJC_METACLASS_$_IASBootTimeInstallableItem
- __58-[IASBootTimeInstallManager queuedPackagesReturningError:]_block_invoke.53
- __72-[IASBootTimeInstallManager estimatedInstallationTimeForPackages:error:]_block_invoke.57
- __82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke.64
- __82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke.65
- __82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke.66
- __Block_object_dispose
- __OBJC_$_CLASS_METHODS_IASBootTimeInstallManager
- __OBJC_$_CLASS_METHODS_IASBootTimeInstallableItem
- __OBJC_$_CLASS_PROP_LIST_IASBootTimeInstallableItem
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
- __OBJC_$_INSTANCE_METHODS_IASBootTimeInstallClient
- __OBJC_$_INSTANCE_METHODS_IASBootTimeInstallManager
- __OBJC_$_INSTANCE_METHODS_IASBootTimeInstallableItem
- __OBJC_$_INSTANCE_VARIABLES_IASBootTimeInstallClient
- __OBJC_$_INSTANCE_VARIABLES_IASBootTimeInstallManager
- __OBJC_$_INSTANCE_VARIABLES_IASBootTimeInstallableItem
- __OBJC_$_PROP_LIST_IASBootTimeInstallClient
- __OBJC_$_PROP_LIST_IASBootTimeInstallManager
- __OBJC_$_PROP_LIST_IASBootTimeInstallableItem
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_IASBootTimeInstallClientProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_IASBootTimeInstallDaemonProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_IASBootTimeInstallClientProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_IASBootTimeInstallDaemonProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding
- __OBJC_CLASS_PROTOCOLS_$_IASBootTimeInstallClient
- __OBJC_CLASS_PROTOCOLS_$_IASBootTimeInstallManager
- __OBJC_CLASS_PROTOCOLS_$_IASBootTimeInstallableItem
- __OBJC_CLASS_RO_$_IASBootTimeInstallClient
- __OBJC_CLASS_RO_$_IASBootTimeInstallManager
- __OBJC_CLASS_RO_$_IASBootTimeInstallableItem
- __OBJC_LABEL_PROTOCOL_$_IASBootTimeInstallClientProtocol
- __OBJC_LABEL_PROTOCOL_$_IASBootTimeInstallDaemonProtocol
- __OBJC_LABEL_PROTOCOL_$_NSCoding
- __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
- __OBJC_METACLASS_RO_$_IASBootTimeInstallClient
- __OBJC_METACLASS_RO_$_IASBootTimeInstallManager
- __OBJC_METACLASS_RO_$_IASBootTimeInstallableItem
- __OBJC_PROTOCOL_$_IASBootTimeInstallClientProtocol
- __OBJC_PROTOCOL_$_IASBootTimeInstallDaemonProtocol
- __OBJC_PROTOCOL_$_NSCoding
- __OBJC_PROTOCOL_$_NSSecureCoding
- __OBJC_PROTOCOL_REFERENCE_$_IASBootTimeInstallClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_IASBootTimeInstallDaemonProtocol
- ___50-[IASBootTimeInstallManager initWithVolume:error:]_block_invoke
- ___50-[IASBootTimeInstallManager initWithVolume:error:]_block_invoke_2
- ___52+[IASBootTimeInstallManager managerForVolume:error:]_block_invoke
- ___58-[IASBootTimeInstallManager performRestartReturningError:]_block_invoke
- ___58-[IASBootTimeInstallManager queuedPackagesReturningError:]_block_invoke
- ___63-[IASBootTimeInstallManager clearQueuedPackagesReturningError:]_block_invoke
- ___63-[IASBootTimeInstallManager clearQueuedPackagesReturningError:]_block_invoke_2
- ___63-[IASBootTimeInstallManager isRestartRequiredByPackages:error:]_block_invoke
- ___63-[IASBootTimeInstallManager isRestartRequiredByPackages:error:]_block_invoke_2
- ___63-[IASBootTimeInstallManager queuePackageForInstallation:error:]_block_invoke
- ___63-[IASBootTimeInstallManager queuePackageForInstallation:error:]_block_invoke_2
- ___72-[IASBootTimeInstallManager estimatedInstallationTimeForPackages:error:]_block_invoke
- ___82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke
- ___82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke_2
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___IASLogObject_block_invoke
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_e8_32r40r_e20_v24?0d8"NSError"16l
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e5_v8?0l
- ___block_descriptor_64_e8_32s40r48r_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48bs56bs_e20_v20?0B8"NSError"12l
- ___copy_helper_block_e8_32b
- ___copy_helper_block_e8_32r
- ___copy_helper_block_e8_32r40r
- ___copy_helper_block_e8_32s40b
- ___copy_helper_block_e8_32s40r48r
- ___copy_helper_block_e8_32s40s48b56b
- ___destroy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r40r
- ___destroy_helper_block_e8_32s40r48r
- __block_literal_global.49
- __installManagersQueue
- __volumeMountpointURLsToBootTimeInstallManagers
- _dispatch_sync
- _objc_msgSend$URLByResolvingSymlinksInPath
- _objc_msgSend$URLByStandardizingPath
- _objc_msgSend$absoluteURL
- _objc_msgSend$allowsKeyedCoding
- _objc_msgSend$bootTimeInstallProgress:estimatedTimeRemaining:status:
- _objc_msgSend$clearQueuedPackagesOnVolume:reply:
- _objc_msgSend$clientIdentifier
- _objc_msgSend$connection
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$effectiveUserIdentifier
- _objc_msgSend$encodeObject:forKey:
- _objc_msgSend$estimatedInstallationTimeForPackages:onVolume:reply:
- _objc_msgSend$evaluatorMetaInfo
- _objc_msgSend$exportedInterface
- _objc_msgSend$hash
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$initWithProductAtURL:error:
- _objc_msgSend$initWithVolume:error:
- _objc_msgSend$installQueuedPackages:onVolume:completionHandler:
- _objc_msgSend$interfaceType
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$isEqualToInstallableItem:
- _objc_msgSend$isFileURL
- _objc_msgSend$isRestartRequiredByPackages:onVolume:reply:
- _objc_msgSend$performRestart
- _objc_msgSend$pid
- _objc_msgSend$processIdentifier
- _objc_msgSend$processInfo
- _objc_msgSend$processName
- _objc_msgSend$productURL
- _objc_msgSend$progressHandlers
- _objc_msgSend$progressObserversQueue
- _objc_msgSend$queuePackageForInstallation:onVolume:reply:
- _objc_msgSend$queuedPackagesOnVolume:reply:
- _objc_msgSend$queuedPackagesReturningError:
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$remoteObjectProxy
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$resume
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setClientIdentifier:
- _objc_msgSend$setEvaluatorMetaInfo:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setInterfaceType:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setInvalidationHandler:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$setWithObject:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_msgSend$uid
- _objc_msgSend$volumeURL
- _objc_retainBlock
- _os_log_create
- _proc_name
- _proc_pidpath
CStrings:
- "\x04"
- "%@ (pid = %d, uid = %d, path = %@, connection remote object interface = %@, exported interface = %@, remote object proxy = %@)"
- "-init is not a permitted initializer for %@"
- "@\"NSXPCConnection\""
- "@24@0:8@\"NSCoder\"16"
- "@32@0:8@16^@24"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "BootTimeInstall: Service connection interrupted."
- "BootTimeInstall: Service connection invalidated."
- "I16@0:8"
- "IASBTII.clientIdentifier"
- "IASBTII.evaluatorMetaInfo"
- "IASBTII.interfaceType"
- "IASBTII.productURL"
- "IASBootTimeInstallClient"
- "IASBootTimeInstallClientProtocol"
- "IASBootTimeInstallDaemonProtocol"
- "IASBootTimeInstallManager"
- "IASBootTimeInstallManagerAlternateStatus"
- "IASBootTimeInstallManagerErrorDomain"
- "IASBootTimeInstallManagerPrimaryStatus"
- "IASBootTimeInstallableItem"
- "IASBootTimeInstallableItem does not support non-keyed archiving."
- "IASBootTimeInstallableItemErrorDomain"
- "IASBootTimeInstallableItemException"
- "IASNotImplementedException"
- "NSCoding"
- "NSSecureCoding"
- "T@\"NSArray\",R,C"
- "T@\"NSDictionary\",C,V_evaluatorMetaInfo"
- "T@\"NSMutableArray\",&,V_progressHandlers"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_progressObserversQueue"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",&,V_path"
- "T@\"NSString\",C,V_clientIdentifier"
- "T@\"NSString\",C,V_interfaceType"
- "T@\"NSURL\",&,V_volumeURL"
- "T@\"NSURL\",C,V_productURL"
- "T@\"NSXPCConnection\",&,V_connection"
- "TB,R"
- "TI,V_uid"
- "Ti,V_pid"
- "URLByResolvingSymlinksInPath"
- "URLByStandardizingPath"
- "_clientIdentifier"
- "_connection"
- "_evaluatorMetaInfo"
- "_interfaceType"
- "_path"
- "_pid"
- "_productURL"
- "_progressHandlers"
- "_progressObserversQueue"
- "_uid"
- "_volumeURL"
- "absoluteURL"
- "allowsKeyedCoding"
- "bootTimeInstallProgress:estimatedTimeRemaining:status:"
- "clearQueuedPackagesOnVolume:reply:"
- "clearQueuedPackagesReturningError:"
- "clientIdentifier"
- "com.apple.IASUtilities.IASBootTimeInstallManager.installManagersQueue"
- "com.apple.IASUtilities.IASBootTimeInstallManager.progressObserversQueue"
- "com.apple.bootinstalld"
- "com.apple.mac.install"
- "connection"
- "d32@0:8@16^@24"
- "decodeObjectOfClass:forKey:"
- "effectiveUserIdentifier"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "estimatedInstallationTimeForPackages:error:"
- "estimatedInstallationTimeForPackages:onVolume:reply:"
- "evaluatorMetaInfo"
- "exportedInterface"
- "initWithConnection:"
- "initWithMachServiceName:options:"
- "initWithProductAtURL:error:"
- "initWithVolume:error:"
- "installQueuedPackages:onVolume:completionHandler:"
- "installQueuedPackages:withProgress:completionHandler:"
- "interfaceType"
- "interfaceWithProtocol:"
- "isEqualToInstallableItem:"
- "isFileURL"
- "isRestartRequiredByPackages:error:"
- "isRestartRequiredByPackages:onVolume:reply:"
- "managerForVolume:error:"
- "performRestart"
- "performRestartReturningError:"
- "pid"
- "processIdentifier"
- "processInfo"
- "processName"
- "productURL"
- "progressHandlers"
- "progressObserversQueue"
- "queuePackageForInstallation:error:"
- "queuePackageForInstallation:onVolume:reply:"
- "queuedPackages"
- "queuedPackagesOnVolume:reply:"
- "queuedPackagesReturningError:"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientIdentifier:"
- "setConnection:"
- "setEvaluatorMetaInfo:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterfaceType:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setPath:"
- "setPid:"
- "setProductURL:"
- "setProgressHandlers:"
- "setProgressObserversQueue:"
- "setRemoteObjectInterface:"
- "setUid:"
- "setVolumeURL:"
- "setWithObject:"
- "setWithObjects:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "uid"
- "v16@?0@\"NSError\"8"
- "v20@0:8I16"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@\"NSCoder\"16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0d8@\"NSError\"16"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
- "v32@0:8f16f20@\"NSDictionary\"24"
- "v32@0:8f16f20@24"
- "v40@0:8@\"IASBootTimeInstallableItem\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?d@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "volumeURL"

```
