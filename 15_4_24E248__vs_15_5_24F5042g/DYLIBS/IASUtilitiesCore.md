## IASUtilitiesCore

> `/System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore`

```diff

-657.0.0.0.0
-  __TEXT.__text: 0x371bc
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x17bc
-  __TEXT.__const: 0x1519
-  __TEXT.__cstring: 0x4d1d
-  __TEXT.__gcc_except_tab: 0x4e8
+658.0.0.0.0
+  __TEXT.__text: 0x39cf8
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_methlist: 0x1b54
+  __TEXT.__const: 0x1509
+  __TEXT.__cstring: 0x50c4
+  __TEXT.__gcc_except_tab: 0x564
   __TEXT.__oslogstring: 0xc0c
-  __TEXT.__unwind_info: 0xb28
-  __TEXT.__objc_classname: 0x204
-  __TEXT.__objc_methname: 0x3488
-  __TEXT.__objc_methtype: 0xba5
-  __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x1630
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__unwind_info: 0xc18
+  __TEXT.__objc_classname: 0x2c2
+  __TEXT.__objc_methname: 0x3dbf
+  __TEXT.__objc_methtype: 0xd7c
+  __TEXT.__objc_stubs: 0x32c0
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x1650
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x898
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x310
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x2568
+  __AUTH_CONST.__const: 0x530
+  __AUTH_CONST.__cfstring: 0x1680
+  __AUTH_CONST.__objc_const: 0x2b48
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x1f0
-  __DATA.__data: 0x95a
-  __DATA.__bss: 0xa5
+  __AUTH.__objc_data: 0x780
+  __DATA.__objc_ivar: 0x22c
+  __DATA.__data: 0xada
+  __DATA.__bss: 0xb5
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1421
-  Symbols:   2971
-  CStrings:  1553
+  Functions: 1508
+  Symbols:   3203
+  CStrings:  1707
 
Symbols:
+ +[IASBootTimeInstallManager initialize]
+ +[IASBootTimeInstallManager managerForVolume:error:]
+ +[IASBootTimeInstallableItem supportsSecureCoding]
+ -[IASBootTimeInstallClient .cxx_destruct]
+ -[IASBootTimeInstallClient bootTimeInstallProgress:estimatedTimeRemaining:status:]
+ -[IASBootTimeInstallClient connection]
+ -[IASBootTimeInstallClient description]
+ -[IASBootTimeInstallClient initWithConnection:]
+ -[IASBootTimeInstallClient name]
+ -[IASBootTimeInstallClient path]
+ -[IASBootTimeInstallClient pid]
+ -[IASBootTimeInstallClient setConnection:]
+ -[IASBootTimeInstallClient setName:]
+ -[IASBootTimeInstallClient setPath:]
+ -[IASBootTimeInstallClient setPid:]
+ -[IASBootTimeInstallClient setUid:]
+ -[IASBootTimeInstallClient uid]
+ -[IASBootTimeInstallManager .cxx_destruct]
+ -[IASBootTimeInstallManager bootTimeInstallProgress:estimatedTimeRemaining:status:]
+ -[IASBootTimeInstallManager clearQueuedPackagesReturningError:]
+ -[IASBootTimeInstallManager connection]
+ -[IASBootTimeInstallManager estimatedInstallationTimeForPackages:error:]
+ -[IASBootTimeInstallManager initWithVolume:error:]
+ -[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]
+ -[IASBootTimeInstallManager isRestartRequiredByPackages:error:]
+ -[IASBootTimeInstallManager performRestartReturningError:]
+ -[IASBootTimeInstallManager progressHandlers]
+ -[IASBootTimeInstallManager progressObserversQueue]
+ -[IASBootTimeInstallManager queuePackageForInstallation:error:]
+ -[IASBootTimeInstallManager queuedPackagesReturningError:]
+ -[IASBootTimeInstallManager queuedPackages]
+ -[IASBootTimeInstallManager setConnection:]
+ -[IASBootTimeInstallManager setProgressHandlers:]
+ -[IASBootTimeInstallManager setProgressObserversQueue:]
+ -[IASBootTimeInstallManager setVolumeURL:]
+ -[IASBootTimeInstallManager volumeURL]
+ -[IASBootTimeInstallableItem .cxx_destruct]
+ -[IASBootTimeInstallableItem cleanupPackageOnDequeue]
+ -[IASBootTimeInstallableItem clientIdentifier]
+ -[IASBootTimeInstallableItem encodeWithCoder:]
+ -[IASBootTimeInstallableItem evaluatorMetaInfo]
+ -[IASBootTimeInstallableItem hash]
+ -[IASBootTimeInstallableItem initWithCoder:]
+ -[IASBootTimeInstallableItem initWithProductAtURL:error:]
+ -[IASBootTimeInstallableItem init]
+ -[IASBootTimeInstallableItem interfaceType]
+ -[IASBootTimeInstallableItem isEqual:]
+ -[IASBootTimeInstallableItem isEqualToInstallableItem:]
+ -[IASBootTimeInstallableItem isJumpStartItem]
+ -[IASBootTimeInstallableItem productURL]
+ -[IASBootTimeInstallableItem setCleanupPackageOnDequeue:]
+ -[IASBootTimeInstallableItem setClientIdentifier:]
+ -[IASBootTimeInstallableItem setEvaluatorMetaInfo:]
+ -[IASBootTimeInstallableItem setInterfaceType:]
+ -[IASBootTimeInstallableItem setJumpStartItem:]
+ -[IASBootTimeInstallableItem setProductURL:]
+ -[IASBootTimeInstallableItem(TemplateMigration) isTemplateMigrationItem]
+ -[IASBootTimeInstallableItem(TemplateMigration) setTemplateMigrationItem:]
+ GCC_except_table11
+ GCC_except_table16
+ GCC_except_table24
+ GCC_except_table39
+ GCC_except_table42
+ OBJC_IVAR_$_IASBootTimeInstallClient._connection
+ OBJC_IVAR_$_IASBootTimeInstallClient._name
+ OBJC_IVAR_$_IASBootTimeInstallClient._path
+ OBJC_IVAR_$_IASBootTimeInstallClient._pid
+ OBJC_IVAR_$_IASBootTimeInstallClient._uid
+ OBJC_IVAR_$_IASBootTimeInstallManager._connection
+ OBJC_IVAR_$_IASBootTimeInstallManager._progressHandlers
+ OBJC_IVAR_$_IASBootTimeInstallManager._progressObserversQueue
+ OBJC_IVAR_$_IASBootTimeInstallManager._volumeURL
+ OBJC_IVAR_$_IASBootTimeInstallableItem._cleanupPackageOnDequeue
+ OBJC_IVAR_$_IASBootTimeInstallableItem._clientIdentifier
+ OBJC_IVAR_$_IASBootTimeInstallableItem._evaluatorMetaInfo
+ OBJC_IVAR_$_IASBootTimeInstallableItem._interfaceType
+ OBJC_IVAR_$_IASBootTimeInstallableItem._jumpStartItem
+ OBJC_IVAR_$_IASBootTimeInstallableItem._productURL
+ _IASBootTimeInstallManagerAlternateStatusKey
+ _IASBootTimeInstallManagerErrorDomain
+ _IASBootTimeInstallManagerPrimaryStatusKey
+ _IASBootTimeInstallableItemErrorDomain
+ _NSURLErrorDomain
+ _NSURLErrorKey
+ _OBJC_CLASS_$_IASBootTimeInstallClient
+ _OBJC_CLASS_$_IASBootTimeInstallManager
+ _OBJC_CLASS_$_IASBootTimeInstallableItem
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_IASBootTimeInstallClient
+ _OBJC_METACLASS_$_IASBootTimeInstallManager
+ _OBJC_METACLASS_$_IASBootTimeInstallableItem
+ __58-[IASBootTimeInstallManager queuedPackagesReturningError:]_block_invoke.53
+ __72-[IASBootTimeInstallManager estimatedInstallationTimeForPackages:error:]_block_invoke.57
+ __82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke.64
+ __82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke.65
+ __82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke.66
+ __OBJC_$_CLASS_METHODS_IASBootTimeInstallManager
+ __OBJC_$_CLASS_METHODS_IASBootTimeInstallableItem
+ __OBJC_$_CLASS_PROP_LIST_IASBootTimeInstallableItem
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_IASBootTimeInstallClient
+ __OBJC_$_INSTANCE_METHODS_IASBootTimeInstallManager
+ __OBJC_$_INSTANCE_METHODS_IASBootTimeInstallableItem(TemplateMigration)
+ __OBJC_$_INSTANCE_VARIABLES_IASBootTimeInstallClient
+ __OBJC_$_INSTANCE_VARIABLES_IASBootTimeInstallManager
+ __OBJC_$_INSTANCE_VARIABLES_IASBootTimeInstallableItem
+ __OBJC_$_PROP_LIST_IASBootTimeInstallClient
+ __OBJC_$_PROP_LIST_IASBootTimeInstallManager
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IASBootTimeInstallClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IASBootTimeInstallDaemonProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IASBootTimeInstallClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IASBootTimeInstallDaemonProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_IASBootTimeInstallClient
+ __OBJC_CLASS_PROTOCOLS_$_IASBootTimeInstallManager
+ __OBJC_CLASS_PROTOCOLS_$_IASBootTimeInstallableItem
+ __OBJC_CLASS_RO_$_IASBootTimeInstallClient
+ __OBJC_CLASS_RO_$_IASBootTimeInstallManager
+ __OBJC_CLASS_RO_$_IASBootTimeInstallableItem
+ __OBJC_LABEL_PROTOCOL_$_IASBootTimeInstallClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_IASBootTimeInstallDaemonProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_IASBootTimeInstallClient
+ __OBJC_METACLASS_RO_$_IASBootTimeInstallManager
+ __OBJC_METACLASS_RO_$_IASBootTimeInstallableItem
+ __OBJC_PROTOCOL_$_IASBootTimeInstallClientProtocol
+ __OBJC_PROTOCOL_$_IASBootTimeInstallDaemonProtocol
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_IASBootTimeInstallClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_IASBootTimeInstallDaemonProtocol
+ ___50-[IASBootTimeInstallManager initWithVolume:error:]_block_invoke
+ ___50-[IASBootTimeInstallManager initWithVolume:error:]_block_invoke_2
+ ___52+[IASBootTimeInstallManager managerForVolume:error:]_block_invoke
+ ___58-[IASBootTimeInstallManager performRestartReturningError:]_block_invoke
+ ___58-[IASBootTimeInstallManager queuedPackagesReturningError:]_block_invoke
+ ___63-[IASBootTimeInstallManager clearQueuedPackagesReturningError:]_block_invoke
+ ___63-[IASBootTimeInstallManager clearQueuedPackagesReturningError:]_block_invoke_2
+ ___63-[IASBootTimeInstallManager isRestartRequiredByPackages:error:]_block_invoke
+ ___63-[IASBootTimeInstallManager isRestartRequiredByPackages:error:]_block_invoke_2
+ ___63-[IASBootTimeInstallManager queuePackageForInstallation:error:]_block_invoke
+ ___63-[IASBootTimeInstallManager queuePackageForInstallation:error:]_block_invoke_2
+ ___72-[IASBootTimeInstallManager estimatedInstallationTimeForPackages:error:]_block_invoke
+ ___82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke
+ ___82-[IASBootTimeInstallManager installQueuedPackages:withProgress:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32r40r_e20_v24?0d8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs56bs_e20_v20?0B8"NSError"12l
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32s40b
+ ___copy_helper_block_e8_32s40r48r
+ ___copy_helper_block_e8_32s40s48b56b
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40s48s56s
+ __block_literal_global.49
+ __installManagersQueue
+ __volumeMountpointURLsToBootTimeInstallManagers
+ _objc_msgSend$URLByResolvingSymlinksInPath
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$absoluteURL
+ _objc_msgSend$allowsKeyedCoding
+ _objc_msgSend$bootTimeInstallProgress:estimatedTimeRemaining:status:
+ _objc_msgSend$cleanupPackageOnDequeue
+ _objc_msgSend$clearQueuedPackagesOnVolume:reply:
+ _objc_msgSend$clientIdentifier
+ _objc_msgSend$connection
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$description
+ _objc_msgSend$effectiveUserIdentifier
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$estimatedInstallationTimeForPackages:onVolume:reply:
+ _objc_msgSend$evaluatorMetaInfo
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$hash
+ _objc_msgSend$initWithProductAtURL:error:
+ _objc_msgSend$initWithVolume:error:
+ _objc_msgSend$installQueuedPackages:onVolume:completionHandler:
+ _objc_msgSend$interfaceType
+ _objc_msgSend$isEqualToInstallableItem:
+ _objc_msgSend$isJumpStartItem
+ _objc_msgSend$isRestartRequiredByPackages:onVolume:reply:
+ _objc_msgSend$name
+ _objc_msgSend$performRestart
+ _objc_msgSend$pid
+ _objc_msgSend$productURL
+ _objc_msgSend$progressHandlers
+ _objc_msgSend$progressObserversQueue
+ _objc_msgSend$queuePackageForInstallation:onVolume:reply:
+ _objc_msgSend$queuedPackagesOnVolume:reply:
+ _objc_msgSend$queuedPackagesReturningError:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$removeObject:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setCleanupPackageOnDequeue:
+ _objc_msgSend$setClientIdentifier:
+ _objc_msgSend$setEvaluatorMetaInfo:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInterfaceType:
+ _objc_msgSend$setJumpStartItem:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$uid
+ _objc_msgSend$volumeURL
+ _objc_retainBlock
+ _objc_setProperty_atomic_copy
+ _proc_name
+ _proc_pidpath
- _IASChunklistDefaultChunkSize
CStrings:
+ "\x13"
+ "\x14"
+ "%@ (pid = %d, uid = %d, path = %@, connection remote object interface = %@, exported interface = %@, remote object proxy = %@)"
+ "-init is not a permitted initializer for %@"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "@\"NSDictionary\""
+ "@\"NSXPCConnection\""
+ "@24@0:8@\"NSCoder\"16"
+ "@32@0:8@16^@24"
+ "B24@0:8^@16"
+ "BootTimeInstall: Service connection interrupted."
+ "BootTimeInstall: Service connection invalidated."
+ "IASBTII.cleanupPackageOnDequeue"
+ "IASBTII.clientIdentifier"
+ "IASBTII.evaluatorMetaInfo"
+ "IASBTII.interfaceType"
+ "IASBTII.jumpStartItem"
+ "IASBTII.productURL"
+ "IASBootTimeInstallClient"
+ "IASBootTimeInstallClientProtocol"
+ "IASBootTimeInstallDaemonProtocol"
+ "IASBootTimeInstallManager"
+ "IASBootTimeInstallManagerAlternateStatus"
+ "IASBootTimeInstallManagerErrorDomain"
+ "IASBootTimeInstallManagerPrimaryStatus"
+ "IASBootTimeInstallableItem"
+ "IASBootTimeInstallableItem does not support non-keyed archiving."
+ "IASBootTimeInstallableItemErrorDomain"
+ "IASBootTimeInstallableItemException"
+ "IASNotImplementedException"
+ "NSCoding"
+ "NSSecureCoding"
+ "T@\"NSArray\",R,C"
+ "T@\"NSDictionary\",C,V_evaluatorMetaInfo"
+ "T@\"NSMutableArray\",&,V_progressHandlers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_progressObserversQueue"
+ "T@\"NSString\",&,V_name"
+ "T@\"NSString\",&,V_path"
+ "T@\"NSString\",C,V_clientIdentifier"
+ "T@\"NSString\",C,V_interfaceType"
+ "T@\"NSURL\",&,V_volumeURL"
+ "T@\"NSURL\",C,V_productURL"
+ "T@\"NSXPCConnection\",&,V_connection"
+ "TB,GisJumpStartItem,V_jumpStartItem"
+ "TB,GisTemplateMigrationItem"
+ "TB,V_cleanupPackageOnDequeue"
+ "TI,V_uid"
+ "TemplateMigration"
+ "Ti,V_pid"
+ "URLByResolvingSymlinksInPath"
+ "URLByStandardizingPath"
+ "_cleanupPackageOnDequeue"
+ "_clientIdentifier"
+ "_connection"
+ "_evaluatorMetaInfo"
+ "_interfaceType"
+ "_jumpStartItem"
+ "_name"
+ "_path"
+ "_pid"
+ "_productURL"
+ "_progressHandlers"
+ "_progressObserversQueue"
+ "_uid"
+ "_volumeURL"
+ "absoluteURL"
+ "allowsKeyedCoding"
+ "bootTimeInstallProgress:estimatedTimeRemaining:status:"
+ "cleanupPackageOnDequeue"
+ "clearQueuedPackagesOnVolume:reply:"
+ "clearQueuedPackagesReturningError:"
+ "clientIdentifier"
+ "com.apple.IASUtilities.IASBootTimeInstallManager.installManagersQueue"
+ "com.apple.IASUtilities.IASBootTimeInstallManager.progressObserversQueue"
+ "com.apple.bootinstalld"
+ "connection"
+ "containsValueForKey:"
+ "d32@0:8@16^@24"
+ "decodeBoolForKey:"
+ "decodeObjectOfClass:forKey:"
+ "effectiveUserIdentifier"
+ "encodeBool:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "estimatedInstallationTimeForPackages:error:"
+ "estimatedInstallationTimeForPackages:onVolume:reply:"
+ "evaluatorMetaInfo"
+ "exportedInterface"
+ "initWithCoder:"
+ "initWithConnection:"
+ "initWithProductAtURL:error:"
+ "initWithVolume:error:"
+ "installQueuedPackages:onVolume:completionHandler:"
+ "installQueuedPackages:withProgress:completionHandler:"
+ "interfaceType"
+ "isEqualToInstallableItem:"
+ "isJumpStartItem"
+ "isRestartRequiredByPackages:error:"
+ "isRestartRequiredByPackages:onVolume:reply:"
+ "isTemplateMigrationItem"
+ "jumpStartItem"
+ "managerForVolume:error:"
+ "name"
+ "performRestart"
+ "performRestartReturningError:"
+ "pid"
+ "productURL"
+ "progressHandlers"
+ "progressObserversQueue"
+ "queuePackageForInstallation:error:"
+ "queuePackageForInstallation:onVolume:reply:"
+ "queuedPackages"
+ "queuedPackagesOnVolume:reply:"
+ "queuedPackagesReturningError:"
+ "remoteObjectInterface"
+ "remoteObjectProxy"
+ "removeObject:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setCleanupPackageOnDequeue:"
+ "setClientIdentifier:"
+ "setConnection:"
+ "setEvaluatorMetaInfo:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterfaceType:"
+ "setJumpStartItem:"
+ "setPath:"
+ "setPid:"
+ "setProductURL:"
+ "setProgressHandlers:"
+ "setProgressObserversQueue:"
+ "setTemplateMigrationItem:"
+ "setUid:"
+ "setVolumeURL:"
+ "setWithObject:"
+ "setWithObjects:"
+ "supportsSecureCoding"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "templateMigrationItem"
+ "uid"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0d8@\"NSError\"16"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v32@0:8f16f20@\"NSDictionary\"24"
+ "v32@0:8f16f20@24"
+ "v40@0:8@\"IASBootTimeInstallableItem\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?d@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@16@?24@?32"
+ "volumeURL"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"

```
