## icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

-1936.4.3.0.0
-  __TEXT.__text: 0x595c
-  __TEXT.__auth_stubs: 0x4b0
+2013.0.0.0.0
+  __TEXT.__text: 0x5014
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x23c
+  __TEXT.__objc_methlist: 0x22c
   __TEXT.__cstring: 0x1f15
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__objc_methname: 0xa80
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__objc_methname: 0xa70
   __TEXT.__oslogstring: 0x34
-  __TEXT.__objc_classname: 0x45
+  __TEXT.__objc_classname: 0x43
   __TEXT.__objc_methtype: 0x1c7
-  __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__auth_got: 0x268
+  __TEXT.__unwind_info: 0x168
+  __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__cfstring: 0x1de0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_arraydata: 0x2880
   __DATA_CONST.__objc_dictobj: 0x21c0
   __DATA.__objc_const: 0x278
-  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 62A2D5BF-083E-32EE-B9F5-8ADE545EFE56
-  Functions: 72
-  Symbols:   120
-  CStrings:  620
+  UUID: E380B476-55A7-3C19-868E-8C4723C758F1
+  Functions: 70
+  Symbols:   305
+  CStrings:  619
 
Symbols:
+ +[ICDeviceAccessManager sharedAccessManager]
+ +[ICDeviceAccessManager sharedAccessManager].cold.1
+ -[ICDeviceAccessManager addBundleIdentifier:]
+ -[ICDeviceAccessManager addBundleIdentifier:].cold.1
+ -[ICDeviceAccessManager allBundleIdentifiers]
+ -[ICDeviceAccessManager bundleIdentifier:stateForAccessType:]
+ -[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]
+ -[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]
+ -[ICDeviceAccessManager bundleIdentifiersWithAccessType:]
+ -[ICDeviceAccessManager captureUserIntentForBundleIdentifier:withNotification:]
+ -[ICDeviceAccessManager connection:stateForAccessType:]
+ -[ICDeviceAccessManager dealloc]
+ -[ICDeviceAccessManager dealloc].cold.1
+ -[ICDeviceAccessManager deviceAccessQueue]
+ -[ICDeviceAccessManager displayAlertForApplication:withNotification:completionBlock:]
+ -[ICDeviceAccessManager externalMediaAccessDB]
+ -[ICDeviceAccessManager init]
+ -[ICDeviceAccessManager openDB:]
+ -[ICDeviceAccessManager revokeBundleIdentifier:]
+ -[ICDeviceAccessManager revokeBundleIdentifier:].cold.1
+ -[ICDeviceAccessManager setDeviceAccessQueue:]
+ -[ICDeviceAccessManager setExternalMediaAccessDB:]
+ -[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]
+ -[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]
+ -[ICDeviceAccessManager validateBundleIdentifierInstalled:]
+ -[ICRemotePrefManager addRemoteManagerConnection:]
+ -[ICRemotePrefManager addSelectorToInterface:selectorString:origin:]
+ -[ICRemotePrefManager addSelectorToInterface:selectorString:origin:].cold.1
+ -[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]
+ -[ICRemotePrefManager checkTetheringAccess:shouldPrompt:]
+ -[ICRemotePrefManager dealloc]
+ -[ICRemotePrefManager init]
+ -[ICRemotePrefManager listener:shouldAcceptNewConnection:]
+ -[ICRemotePrefManager osTransactions]
+ -[ICRemotePrefManager remoteManagerConnections]
+ -[ICRemotePrefManager removeRemoteManagerConnectionWithProcessIdentifier:]
+ -[ICRemotePrefManager requestContentsAuthorizationStatusShouldPrompt:withReply:]
+ -[ICRemotePrefManager requestControlAuthorizationStatusShouldPrompt:withReply:]
+ -[ICRemotePrefManager requestGoodNewsStatusWithReply:]
+ -[ICRemotePrefManager resetContentsAuthorizationStatusWithReply:]
+ -[ICRemotePrefManager resetControlAuthorizationStatusWithReply:]
+ -[ICRemotePrefManager setOsTransactions:]
+ -[ICRemotePrefManager setRemoteManagerConnections:]
+ GCC_except_table11
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table3
+ GCC_except_table30
+ ICLocalizedString.bundle
+ ICLocalizedString.cold.1
+ ICLocalizedString.once
+ OBJC_IVAR_$_ICDeviceAccessManager._deviceAccessQueue
+ OBJC_IVAR_$_ICDeviceAccessManager._externalMediaAccessDB
+ OBJC_IVAR_$_ICRemotePrefManager._osTransactions
+ OBJC_IVAR_$_ICRemotePrefManager._remoteManagerConnections
+ OBJC_IVAR_$_ICRemotePrefManager._remoteManagerConnectionsLock
+ _ICAccessTypeControlInformed
+ _ICAccessTypeRead
+ _ICAcessQuery
+ _ICAcessStatusQuery
+ _ICLocalizedString
+ _ICLoggingDomain
+ _ICRemotePrefManagerEvaluatePrivateEntitlement
+ _OBJC_CLASS_$_ICDeviceAccessManager
+ _OBJC_CLASS_$_ICRemotePrefManager
+ _OBJC_METACLASS_$_ICDeviceAccessManager
+ _OBJC_METACLASS_$_ICRemotePrefManager
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __29-[ICDeviceAccessManager init]_block_invoke.cold.1
+ __29-[ICDeviceAccessManager init]_block_invoke.cold.2
+ __45-[ICDeviceAccessManager allBundleIdentifiers]_block_invoke.cold.1
+ __48-[ICDeviceAccessManager revokeBundleIdentifier:]_block_invoke.cold.1
+ __57-[ICDeviceAccessManager bundleIdentifiersWithAccessType:]_block_invoke.cold.1
+ __59-[ICDeviceAccessManager validateBundleIdentifierInstalled:]_block_invoke.cold.1
+ __69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke.cold.1
+ __ICOSLogCreate.cold.1
+ __ICOSLogCreate.onceToken
+ __OBJC_$_CLASS_METHODS_ICDeviceAccessManager
+ __OBJC_$_INSTANCE_METHODS_ICDeviceAccessManager
+ __OBJC_$_INSTANCE_METHODS_ICRemotePrefManager
+ __OBJC_$_INSTANCE_VARIABLES_ICDeviceAccessManager
+ __OBJC_$_INSTANCE_VARIABLES_ICRemotePrefManager
+ __OBJC_$_PROP_LIST_ICDeviceAccessManager
+ __OBJC_$_PROP_LIST_ICRemotePrefManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICXPCAuthManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICXPCAuthManagerProtocol
+ __OBJC_CLASS_RO_$_ICDeviceAccessManager
+ __OBJC_CLASS_RO_$_ICRemotePrefManager
+ __OBJC_LABEL_PROTOCOL_$_ICXPCAuthManagerProtocol
+ __OBJC_METACLASS_RO_$_ICDeviceAccessManager
+ __OBJC_METACLASS_RO_$_ICRemotePrefManager
+ __OBJC_PROTOCOL_$_ICXPCAuthManagerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ICXPCAuthManagerProtocol
+ ___29-[ICDeviceAccessManager init]_block_invoke
+ ___44+[ICDeviceAccessManager sharedAccessManager]_block_invoke
+ ___45-[ICDeviceAccessManager addBundleIdentifier:]_block_invoke
+ ___45-[ICDeviceAccessManager allBundleIdentifiers]_block_invoke
+ ___48-[ICDeviceAccessManager revokeBundleIdentifier:]_block_invoke
+ ___50-[ICRemotePrefManager addRemoteManagerConnection:]_block_invoke
+ ___57-[ICDeviceAccessManager bundleIdentifiersWithAccessType:]_block_invoke
+ ___59-[ICDeviceAccessManager validateBundleIdentifierInstalled:]_block_invoke
+ ___68-[ICRemotePrefManager addSelectorToInterface:selectorString:origin:]_block_invoke
+ ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke
+ ___79-[ICDeviceAccessManager captureUserIntentForBundleIdentifier:withNotification:]_block_invoke
+ ___79-[ICRemotePrefManager requestControlAuthorizationStatusShouldPrompt:withReply:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___ICLocalizedString_block_invoke
+ ___ICOSLogCreate
+ _____ICOSLogCreate_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32o_e37_v24?0"BSProcessHandle"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32o40r_e11_v20?0B8Q12lr40l8s32l8
+ ___block_descriptor_48_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32o40o48o56o_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global
+ __block_literal_global.11
+ __block_literal_global.40
+ __gICOSLog
+ _main
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addBundleIdentifier:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addRemoteManagerConnection:
+ _objc_msgSend$addSelectorToInterface:selectorString:origin:
+ _objc_msgSend$allBundleIdentifiers
+ _objc_msgSend$allKeys
+ _objc_msgSend$array
+ _objc_msgSend$auditToken
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleIdentifier:stateForAccessType:
+ _objc_msgSend$bundleIdentifiersWithAccessType:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$captureUserIntentForBundleIdentifier:withNotification:
+ _objc_msgSend$checkFilesAndFoldersAccess:shouldPrompt:
+ _objc_msgSend$checkTetheringAccess:shouldPrompt:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$date
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$deviceAccessQueue
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$displayAlertForApplication:withNotification:completionBlock:
+ _objc_msgSend$externalMediaAccessDB
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$length
+ _objc_msgSend$localizedName
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$openApplication:withOptions:completion:
+ _objc_msgSend$openDB:
+ _objc_msgSend$osTransactions
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeRemoteManagerConnectionWithProcessIdentifier:
+ _objc_msgSend$resume
+ _objc_msgSend$revokeBundleIdentifier:
+ _objc_msgSend$run
+ _objc_msgSend$serviceListener
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$sharedAccessManager
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updateBundleIdentifier:accessType:withState:
+ _objc_msgSend$validateBundleIdentifierInstalled:
+ _objc_msgSend$valueForEntitlement:
+ addSelectorToInterface:selectorString:origin:.incomingClasses
+ addSelectorToInterface:selectorString:origin:.onceToken
+ sharedAccessManager.mgr
+ sharedAccessManager.onceToken
- _objc_autoreleaseReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_getProperty
- _objc_release
- _objc_release_x1
- _objc_release_x19
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retain
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x28
- _objc_retain_x4
- _objc_retain_x8
- _objc_setProperty_atomic
- _objc_storeStrong
- radr://5614542
CStrings:
+ "T@\"NSObject<OS_dispatch_queue>\",V_deviceAccessQueue"
- ".cxx_destruct"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_deviceAccessQueue"

```
