## UserProfilesCore

> `/System/Library/PrivateFrameworks/UserProfilesCore.framework/UserProfilesCore`

```diff

-194.50.3.0.0
-  __TEXT.__text: 0x695c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x71c
-  __TEXT.__const: 0x286
-  __TEXT.__cstring: 0x367
-  __TEXT.__oslogstring: 0x700
-  __TEXT.__gcc_except_tab: 0x90
+299.0.0.0.0
+  __TEXT.__text: 0x9d5c
+  __TEXT.__objc_methlist: 0xcfc
+  __TEXT.__const: 0x2b6
+  __TEXT.__cstring: 0x7d7
+  __TEXT.__oslogstring: 0x8a0
+  __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__swift5_typeref: 0x150
   __TEXT.__swift5_fieldmd: 0xc4
   __TEXT.__constg_swiftt: 0x1b4

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__unwind_info: 0x400
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x14bd
-  __TEXT.__objc_methtype: 0x3ad
-  __TEXT.__objc_stubs: 0xf40
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_catlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x278
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0xde8
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x2ce0
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x368
-  __DATA.__bss: 0x120
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__data: 0x550
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6BFBBB85-52D1-30F6-9426-2FBBD86C649A
-  Functions: 243
-  Symbols:   865
-  CStrings:  407
+  UUID: 4FDBFF8D-1E66-3045-BB5E-71555353D182
+  Functions: 367
+  Symbols:   1408
+  CStrings:  191
 
Symbols:
+ +[UPChangedValue _descriptionObjectForObject:]
+ +[UPObserverHandle isValidHandleSubclass:invalidReason:]
+ +[UPObserverSet _defaultHandleClass]
+ +[UPServiceSpecification configureConnection:]
+ +[UPServiceSpecification connectionEndpoint]
+ +[UPServiceSpecification identifier]
+ +[UPServiceSpecification interface]
+ +[UPServiceSpecification queueAttributes]
+ +[UPServiceSpecification serviceQuality]
+ +[UPSystemMachServiceSpecification connectionEndpoint]
+ +[UPSystemMachServiceSpecification systemMachName]
+ +[UPXPCServiceSpecification connectionEndpoint]
+ +[UPXPCServiceSpecification serviceName]
+ -[NSManagedObject(UserProfilesCore) up_changedValues]
+ -[NSManagedObject(UserProfilesCore) up_dictionaryForKey:]
+ -[NSMapTable(UPObserverSet) up_member:originalKey:]
+ -[UPChangedValue .cxx_destruct]
+ -[UPChangedValue currentValue]
+ -[UPChangedValue debugDescription]
+ -[UPChangedValue descriptionBuilderWithMultilinePrefix:]
+ -[UPChangedValue descriptionWithMultilinePrefix:]
+ -[UPChangedValue description]
+ -[UPChangedValue hash]
+ -[UPChangedValue initWithPreviousValue:currentValue:]
+ -[UPChangedValue initWithPreviousValue:currentValue:].cold.1
+ -[UPChangedValue isEqual:]
+ -[UPChangedValue previousValue]
+ -[UPChangedValue succinctDescriptionBuilder]
+ -[UPChangedValue succinctDescription]
+ -[UPDarwinNotificationListener .cxx_destruct]
+ -[UPDarwinNotificationListener _calloutQueue_handleNotification]
+ -[UPDarwinNotificationListener dealloc]
+ -[UPDarwinNotificationListener delegate]
+ -[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:]
+ -[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:].cold.1
+ -[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:].cold.2
+ -[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:].cold.3
+ -[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:].cold.4
+ -[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:].cold.5
+ -[UPDarwinNotificationListener initWithNotificationName:log:]
+ -[UPDarwinNotificationListener notificationName]
+ -[UPDarwinNotificationListener setDelegate:]
+ -[UPNullStoreObserverToken invalidate]
+ -[UPObserverHandle .cxx_destruct]
+ -[UPObserverHandle hash]
+ -[UPObserverHandle initWithOwningSet:target:userInfo:]
+ -[UPObserverHandle invalidateWithOptions:]
+ -[UPObserverHandle invalidate]
+ -[UPObserverHandle isEqual:]
+ -[UPObserverHandle isValid]
+ -[UPObserverHandle set]
+ -[UPObserverHandle targetPtr]
+ -[UPObserverHandle userInfo]
+ -[UPObserverSet .cxx_destruct]
+ -[UPObserverSet _getTable]
+ -[UPObserverSet _mutateObservers:withPreflight:]
+ -[UPObserverSet _newHandleForObject:withUserInfo:]
+ -[UPObserverSet _removeObserverForHandle:]
+ -[UPObserverSet addObserver:]
+ -[UPObserverSet addObserver:userInfo:]
+ -[UPObserverSet count]
+ -[UPObserverSet enumerateObserversUsingBlock:]
+ -[UPObserverSet handleClass]
+ -[UPObserverSet initWithHandleClass:]
+ -[UPObserverSet initWithOptions:]
+ -[UPObserverSet initWithOptions:handleClass:]
+ -[UPObserverSet init]
+ -[UPObserverSet removeObserver:]
+ -[UPObserverSet table]
+ -[UPObserverSet table_lock]
+ -[UPPersistentContainer _configureContext:]
+ -[UPPersistentContainer _configureContextIfNeeded:]
+ -[UPServiceNullProxy .cxx_destruct]
+ -[UPServiceNullProxy _handleAsyncRequestWithReply:]
+ -[UPServiceNullProxy _handleSyncBooleanRequestWithError:]
+ -[UPServiceNullProxy _handleSyncRequestWithError:]
+ -[UPServiceNullProxy initWithRequestError:]
+ -[UPServiceNullProxy initWithRequestError:].cold.1
+ -[UPServiceProxy .cxx_destruct]
+ -[UPServiceProxy _delegate]
+ -[UPServiceProxy _invalidateStateAndConnection:]
+ -[UPServiceProxy _queue_connectionInterrupted]
+ -[UPServiceProxy _queue_connectionInvalidated]
+ -[UPServiceProxy _remoteTarget]
+ -[UPServiceProxy _remoteTarget].cold.1
+ -[UPServiceProxy activate]
+ -[UPServiceProxy activate].cold.1
+ -[UPServiceProxy dealloc]
+ -[UPServiceProxy dealloc].cold.1
+ -[UPServiceProxy initWithConfigurator:]
+ -[UPServiceProxy initWithConfigurator:].cold.1
+ -[UPServiceProxy initWithConfigurator:].cold.2
+ -[UPServiceProxy invalidate]
+ -[UPServiceProxy remoteNotificationListenerDidReceiveNotification:]
+ -[UPServiceProxyConfiguration .cxx_destruct]
+ -[UPServiceProxyConfiguration delegate]
+ -[UPServiceProxyConfiguration init]
+ -[UPServiceProxyConfiguration log]
+ -[UPServiceProxyConfiguration nullProxyBlock]
+ -[UPServiceProxyConfiguration remoteNotificationListenerBlock]
+ -[UPServiceProxyConfiguration serviceSpecification]
+ -[UPServiceProxyConfiguration setDelegate:]
+ -[UPServiceProxyConfiguration setLog:]
+ -[UPServiceProxyConfiguration setNullProxyBlock:]
+ -[UPServiceProxyConfiguration setRemoteNotificationListenerBlock:]
+ -[UPServiceProxyConfiguration setServiceSpecification:]
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table13
+ GCC_except_table9
+ _BSDispatchQueueCreate
+ _BSDispatchQueueCreateSerial
+ _BSDispatchQueueCreateSerialWithQoS
+ _BSEqualObjects
+ _NSInvalidArgumentException
+ _NSMapMember
+ _OBJC_CLASS_$_BSDispatchQueueAttributes
+ _OBJC_CLASS_$_BSServiceConnection
+ _OBJC_CLASS_$_BSServiceConnectionEndpoint
+ _OBJC_CLASS_$_BSServiceQuality
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_UPChangedValue
+ _OBJC_CLASS_$_UPDarwinNotificationListener
+ _OBJC_CLASS_$_UPNullStoreObserverToken
+ _OBJC_CLASS_$_UPObserverHandle
+ _OBJC_CLASS_$_UPObserverSet
+ _OBJC_CLASS_$_UPServiceNullProxy
+ _OBJC_CLASS_$_UPServiceProxy
+ _OBJC_CLASS_$_UPServiceProxyConfiguration
+ _OBJC_CLASS_$_UPServiceSpecification
+ _OBJC_CLASS_$_UPSystemMachServiceSpecification
+ _OBJC_CLASS_$_UPXPCServiceSpecification
+ _OBJC_IVAR_$_UPChangedValue._currentValue
+ _OBJC_IVAR_$_UPChangedValue._previousValue
+ _OBJC_IVAR_$_UPDarwinNotificationListener._calloutQueue
+ _OBJC_IVAR_$_UPDarwinNotificationListener._delegate
+ _OBJC_IVAR_$_UPDarwinNotificationListener._log
+ _OBJC_IVAR_$_UPDarwinNotificationListener._notificationName
+ _OBJC_IVAR_$_UPDarwinNotificationListener._notificationToken
+ _OBJC_IVAR_$_UPObserverHandle._set
+ _OBJC_IVAR_$_UPObserverHandle._targetPtr
+ _OBJC_IVAR_$_UPObserverHandle._userInfo
+ _OBJC_IVAR_$_UPObserverHandle._valid
+ _OBJC_IVAR_$_UPObserverSet._handleClass
+ _OBJC_IVAR_$_UPObserverSet._table
+ _OBJC_IVAR_$_UPObserverSet._table_lock
+ _OBJC_IVAR_$_UPPersistentContainer._configureContextOnce
+ _OBJC_IVAR_$_UPServiceNullProxy._calloutQueue
+ _OBJC_IVAR_$_UPServiceNullProxy._requestError
+ _OBJC_IVAR_$_UPServiceProxy._lock
+ _OBJC_IVAR_$_UPServiceProxy._lock_connection
+ _OBJC_IVAR_$_UPServiceProxy._lock_delegate
+ _OBJC_IVAR_$_UPServiceProxy._lock_notificationListener
+ _OBJC_IVAR_$_UPServiceProxy._lock_nullProxy
+ _OBJC_IVAR_$_UPServiceProxy._lock_remoteTarget
+ _OBJC_IVAR_$_UPServiceProxy._log
+ _OBJC_IVAR_$_UPServiceProxy._nullProxyBlock
+ _OBJC_IVAR_$_UPServiceProxy._queue
+ _OBJC_IVAR_$_UPServiceProxyConfiguration._delegate
+ _OBJC_IVAR_$_UPServiceProxyConfiguration._log
+ _OBJC_IVAR_$_UPServiceProxyConfiguration._nullProxyBlock
+ _OBJC_IVAR_$_UPServiceProxyConfiguration._remoteNotificationListenerBlock
+ _OBJC_IVAR_$_UPServiceProxyConfiguration._serviceSpecification
+ _OBJC_METACLASS_$_UPChangedValue
+ _OBJC_METACLASS_$_UPDarwinNotificationListener
+ _OBJC_METACLASS_$_UPNullStoreObserverToken
+ _OBJC_METACLASS_$_UPObserverHandle
+ _OBJC_METACLASS_$_UPObserverSet
+ _OBJC_METACLASS_$_UPServiceNullProxy
+ _OBJC_METACLASS_$_UPServiceProxy
+ _OBJC_METACLASS_$_UPServiceProxyConfiguration
+ _OBJC_METACLASS_$_UPServiceSpecification
+ _OBJC_METACLASS_$_UPSystemMachServiceSpecification
+ _OBJC_METACLASS_$_UPXPCServiceSpecification
+ _UPMakeTemporaryDirectoryWithName
+ _UPMakeTemporaryDirectoryWithNameAndReturnError
+ _UPMakeUniqueTemporaryDirectory
+ _UPMakeUniqueTemporaryDirectoryAndReturnError
+ _UPPlatformDeviceClass.deviceClass
+ _UPPlatformDeviceClass.onceToken
+ _UPRemoveDirectory
+ _UPTemporaryDirectoryURL
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMapTable_$_UPObserverSet
+ __OBJC_$_CATEGORY_NSMapTable_$_UPObserverSet
+ __OBJC_$_CLASS_METHODS_UPChangedValue
+ __OBJC_$_CLASS_METHODS_UPObserverHandle
+ __OBJC_$_CLASS_METHODS_UPObserverSet
+ __OBJC_$_CLASS_METHODS_UPServiceSpecification
+ __OBJC_$_CLASS_METHODS_UPSystemMachServiceSpecification
+ __OBJC_$_CLASS_METHODS_UPXPCServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_UPServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_UPServiceSpecifying
+ __OBJC_$_CLASS_PROP_LIST_UPSystemMachServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_UPXPCServiceSpecification
+ __OBJC_$_INSTANCE_METHODS_UPChangedValue
+ __OBJC_$_INSTANCE_METHODS_UPDarwinNotificationListener
+ __OBJC_$_INSTANCE_METHODS_UPNullStoreObserverToken
+ __OBJC_$_INSTANCE_METHODS_UPObserverHandle
+ __OBJC_$_INSTANCE_METHODS_UPObserverSet
+ __OBJC_$_INSTANCE_METHODS_UPServiceNullProxy
+ __OBJC_$_INSTANCE_METHODS_UPServiceProxy
+ __OBJC_$_INSTANCE_METHODS_UPServiceProxyConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_UPChangedValue
+ __OBJC_$_INSTANCE_VARIABLES_UPDarwinNotificationListener
+ __OBJC_$_INSTANCE_VARIABLES_UPObserverHandle
+ __OBJC_$_INSTANCE_VARIABLES_UPObserverSet
+ __OBJC_$_INSTANCE_VARIABLES_UPServiceNullProxy
+ __OBJC_$_INSTANCE_VARIABLES_UPServiceProxy
+ __OBJC_$_INSTANCE_VARIABLES_UPServiceProxyConfiguration
+ __OBJC_$_PROP_LIST_NSManagedObject_$_UserProfilesCore
+ __OBJC_$_PROP_LIST_UPChangedValue
+ __OBJC_$_PROP_LIST_UPDarwinNotificationListener
+ __OBJC_$_PROP_LIST_UPNullStoreObserverToken
+ __OBJC_$_PROP_LIST_UPObserverHandle
+ __OBJC_$_PROP_LIST_UPObserverSet
+ __OBJC_$_PROP_LIST_UPRemoteNotificationListening
+ __OBJC_$_PROP_LIST_UPServiceProxy
+ __OBJC_$_PROP_LIST_UPServiceProxyConfiguration
+ __OBJC_$_PROTOCOL_CLASS_METHODS_UPServiceSpecifying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSInvalidatable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UPRemoteNotificationListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UPRemoteNotificationListening
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UPServiceProxyConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSInvalidatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UPRemoteNotificationListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UPRemoteNotificationListening
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UPServiceProxyConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UPServiceSpecifying
+ __OBJC_$_PROTOCOL_REFS_BSInvalidatable
+ __OBJC_$_PROTOCOL_REFS_UPRemoteNotificationListening
+ __OBJC_CLASS_PROTOCOLS_$_UPChangedValue
+ __OBJC_CLASS_PROTOCOLS_$_UPDarwinNotificationListener
+ __OBJC_CLASS_PROTOCOLS_$_UPNullStoreObserverToken
+ __OBJC_CLASS_PROTOCOLS_$_UPObserverHandle
+ __OBJC_CLASS_PROTOCOLS_$_UPServiceProxy
+ __OBJC_CLASS_PROTOCOLS_$_UPServiceProxyConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_UPServiceSpecification
+ __OBJC_CLASS_RO_$_UPChangedValue
+ __OBJC_CLASS_RO_$_UPDarwinNotificationListener
+ __OBJC_CLASS_RO_$_UPNullStoreObserverToken
+ __OBJC_CLASS_RO_$_UPObserverHandle
+ __OBJC_CLASS_RO_$_UPObserverSet
+ __OBJC_CLASS_RO_$_UPServiceNullProxy
+ __OBJC_CLASS_RO_$_UPServiceProxy
+ __OBJC_CLASS_RO_$_UPServiceProxyConfiguration
+ __OBJC_CLASS_RO_$_UPServiceSpecification
+ __OBJC_CLASS_RO_$_UPSystemMachServiceSpecification
+ __OBJC_CLASS_RO_$_UPXPCServiceSpecification
+ __OBJC_LABEL_PROTOCOL_$_BSInvalidatable
+ __OBJC_LABEL_PROTOCOL_$_UPRemoteNotificationListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UPRemoteNotificationListening
+ __OBJC_LABEL_PROTOCOL_$_UPServiceProxyConfiguring
+ __OBJC_LABEL_PROTOCOL_$_UPServiceSpecifying
+ __OBJC_METACLASS_RO_$_UPChangedValue
+ __OBJC_METACLASS_RO_$_UPDarwinNotificationListener
+ __OBJC_METACLASS_RO_$_UPNullStoreObserverToken
+ __OBJC_METACLASS_RO_$_UPObserverHandle
+ __OBJC_METACLASS_RO_$_UPObserverSet
+ __OBJC_METACLASS_RO_$_UPServiceNullProxy
+ __OBJC_METACLASS_RO_$_UPServiceProxy
+ __OBJC_METACLASS_RO_$_UPServiceProxyConfiguration
+ __OBJC_METACLASS_RO_$_UPServiceSpecification
+ __OBJC_METACLASS_RO_$_UPSystemMachServiceSpecification
+ __OBJC_METACLASS_RO_$_UPXPCServiceSpecification
+ __OBJC_PROTOCOL_$_BSInvalidatable
+ __OBJC_PROTOCOL_$_UPRemoteNotificationListenerDelegate
+ __OBJC_PROTOCOL_$_UPRemoteNotificationListening
+ __OBJC_PROTOCOL_$_UPServiceProxyConfiguring
+ __OBJC_PROTOCOL_$_UPServiceSpecifying
+ ___26-[UPChangedValue isEqual:]_block_invoke
+ ___26-[UPChangedValue isEqual:]_block_invoke_2
+ ___38-[UPObserverSet addObserver:userInfo:]_block_invoke
+ ___39-[UPServiceProxy initWithConfigurator:]_block_invoke
+ ___39-[UPServiceProxy initWithConfigurator:]_block_invoke_2
+ ___39-[UPServiceProxy initWithConfigurator:]_block_invoke_3
+ ___42-[UPObserverSet _removeObserverForHandle:]_block_invoke
+ ___42-[UPObserverSet _removeObserverForHandle:]_block_invoke_2
+ ___51-[UPPersistentContainer _configureContextIfNeeded:]_block_invoke
+ ___51-[UPServiceNullProxy _handleAsyncRequestWithReply:]_block_invoke
+ ___56+[UPObserverHandle isValidHandleSubclass:invalidReason:]_block_invoke
+ ___74-[UPDarwinNotificationListener initWithNotificationName:calloutQueue:log:]_block_invoke
+ ___NSDictionary0__struct
+ ___UPPlatformDeviceClass_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e20_B16?0"NSMapTable"8ls32l8
+ ___block_descriptor_40_e8_32s_e20_v16?0"NSMapTable"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_8?0ls32l8
+ ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s40s_e20_v16?0"NSMapTable"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40w_e42_v16?0"<BSServiceConnectionConfiguring>"8lu48l8s32l8w40l8
+ ___block_literal_global.2
+ __os_feature_enabled_impl
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _isValidHandleSubclass:invalidReason:.expectedIsEqualImplementation
+ _isValidHandleSubclass:invalidReason:.onceToken
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_autorelease
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_exception_throw
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$_calloutQueue_handleNotification
+ _objc_msgSend$_configureContextIfNeeded:
+ _objc_msgSend$_defaultHandleClass
+ _objc_msgSend$_descriptionObjectForObject:
+ _objc_msgSend$_getTable
+ _objc_msgSend$_invalidateStateAndConnection:
+ _objc_msgSend$_mutateObservers:withPreflight:
+ _objc_msgSend$_newHandleForObject:withUserInfo:
+ _objc_msgSend$_queue_connectionInterrupted
+ _objc_msgSend$_queue_connectionInvalidated
+ _objc_msgSend$_removeObserverForHandle:
+ _objc_msgSend$activate
+ _objc_msgSend$addObserver:userInfo:
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendObject:
+ _objc_msgSend$appendObject:counterpart:
+ _objc_msgSend$appendObject:withName:
+ _objc_msgSend$changedValues
+ _objc_msgSend$committedValuesForKeys:
+ _objc_msgSend$configureConnection:
+ _objc_msgSend$connectionEndpoint
+ _objc_msgSend$connectionWithEndpoint:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$delegate
+ _objc_msgSend$endpointForServiceName:oneshot:service:instance:
+ _objc_msgSend$endpointForSystemMachName:service:instance:
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithHandleClass:
+ _objc_msgSend$initWithNotificationName:calloutQueue:log:
+ _objc_msgSend$initWithOptions:handleClass:
+ _objc_msgSend$initWithOwningSet:target:userInfo:
+ _objc_msgSend$initWithPreviousValue:currentValue:
+ _objc_msgSend$instanceMethodForSelector:
+ _objc_msgSend$interface
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateWithOptions:
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$isValid
+ _objc_msgSend$isValidHandleSubclass:invalidReason:
+ _objc_msgSend$log
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$null
+ _objc_msgSend$nullProxyBlock
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$objectID
+ _objc_msgSend$queueAttributes
+ _objc_msgSend$relativePriority
+ _objc_msgSend$remoteNotificationListenerBlock
+ _objc_msgSend$remoteNotificationListenerDidReceiveNotification:
+ _objc_msgSend$remoteTarget
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$serial
+ _objc_msgSend$serviceClass
+ _objc_msgSend$serviceClass:relativePriority:
+ _objc_msgSend$serviceName
+ _objc_msgSend$serviceProxyConnectionDidInvalidate:
+ _objc_msgSend$serviceProxyDidReceiveUpdateNotification:
+ _objc_msgSend$serviceQuality
+ _objc_msgSend$serviceSpecification
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setInterface:
+ _objc_msgSend$setInterfaceTarget:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setServiceQuality:
+ _objc_msgSend$setTargetQueue:
+ _objc_msgSend$systemMachName
+ _objc_msgSend$up_member:originalKey:
+ _objc_msgSend$userInfo
+ _objc_msgSend$userInitiated
+ _objc_opt_respondsToSelector
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _objc_storeWeak
+ _os_unfair_lock_assert_not_owner
+ _swift_release_x1
+ _swift_release_x21
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x25
- +[UPPersistentContainer _configureContext:]
- -[UPPlatform isAppleTVDeviceClass]
- GCC_except_table11
- GCC_except_table7
- __UPDeviceIsAppleTV.__isAppleTV
- __UPDeviceIsAppleTV.onceToken
- ____UPDeviceIsAppleTV_block_invoke
- ___block_literal_global.121
- _objc_msgSend$isDeviceClass:
- _swift_retain
CStrings:
+ "%@ is not a valid subclass of %@: %@"
+ "%@-queue"
+ "0P`"
+ "1"
+ "@8@?0"
+ "Activation failed as service connection or its remote target is nil. Has the service proxy been invalidated?"
+ "AudioAccessory"
+ "B16@?0@\"NSMapTable\"8"
+ "BSEqualObjects(previousValue, currentValue) == __objc_no"
+ "Class (or one of its superclasses) unexpectedly implements -isEqual:"
+ "Class is not a subclass of UPObserverHandle"
+ "Connection interrupted"
+ "Connection invalidated"
+ "Connection remote target is nil. Requests will fail. Has the proxy been invalidated or not been activated?"
+ "Failed to subscribe to darwin notification. notificationName=%{public}@, status=%u"
+ "Handling darwin notification. name=%{public}@"
+ "Handling update notification"
+ "Must configure a specification"
+ "UPChangedValue.m"
+ "UPDarwinNotificationListener.m"
+ "UPServiceNullProxy.m"
+ "UPServiceProxy instance should be invalidated before being deallocated"
+ "UPServiceProxy.m"
+ "UPServiceSpecification is an abstract class and cannot return a service identifier."
+ "UPServiceSpecification is an abstract class and cannot return an interface."
+ "UPServiceSpecification.m"
+ "UPXPCServiceSpecification is an abstract class and cannot return a service name."
+ "UPXPCServiceSpecification.m"
+ "calloutQueue != ((void*)0)"
+ "com.apple.UserProfiles.UPDarwinNotificationController"
+ "com.apple.userprofiles"
+ "com.apple.userprofiles.%@"
+ "configurator != ((void*)0)"
+ "currentValue"
+ "homePod"
+ "iPad"
+ "iPhone"
+ "log != ((void*)0)"
+ "previousValue"
+ "requestError"
+ "v12@?0i8"
+ "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
+ "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
+ "v16@?0@\"NSMapTable\"8"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<UPPersistentContainerDescribing>\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"NSManagedObjectContext\""
- "@\"NSPersistentContainer\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8o^@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8#16@24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16o^@24"
- "@32@0:8Q16Q24"
- "@36@0:8@16B24o^@28"
- "@40@0:8#16#24@32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24o^@32"
- "@40@0:8Q16Q24Q32"
- "@44@0:8@16@24@32B40"
- "@48@0:8q16@24@32@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@16^Q24"
- "B32@0:8@16o^@24"
- "B32@0:8@16q24"
- "B32@0:8@?16o^@24"
- "B40@0:8@16@24@32"
- "BSDescriptionProviding"
- "BSXPCSecureCoding"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<UPPersistentContainerDescribing>\",R,N,V_persistentContainerDescription"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_buildVersion"
- "T@\"NSString\",R,C,N,V_productType"
- "T@\"NSString\",R,C,N,V_systemVersion"
- "T@\"NSURL\",R,N"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_supportsDaemon"
- "TQ,R"
- "TQ,R,N,V_majorVersion"
- "TQ,R,N,V_minorVersion"
- "TQ,R,N,V_updateVersion"
- "Tq,R,N"
- "Tq,R,N,V_deviceClass"
- "UPPersistentContainer"
- "UPPlatform"
- "UPSoftwareVersion"
- "URL"
- "URLByAppendingPathComponent:isDirectory:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "UserProfilesCore"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_buildVersion"
- "_compareSoftwareVersion:withPrecision:"
- "_configureContext:"
- "_context"
- "_defaultDeviceClass"
- "_deviceClass"
- "_initWithDeviceClass:"
- "_initWithDeviceClass:systemVersion:buildVersion:productType:"
- "_loadPersistentStoreWithPersistentContainerDescription:model:logObject:recreateStoreOnLoadFailure:"
- "_majorVersion"
- "_minorVersion"
- "_parsedVersionIntegerFromString:version:"
- "_persistentContainer"
- "_persistentContainerDescription"
- "_persistentContainerWithPersistentStoreDescription:model:"
- "_persistentStoreDescriptionWithPersistentContainerDescription:"
- "_productType"
- "_recreateEmptyPersistentStoreWithPersistentContainer:persistentStoreDescription:logObject:"
- "_shouldConsiderMinorVersionsWithPrecision:"
- "_shouldConsiderUpdateVersionsWithPrecision:"
- "_supportsDaemon"
- "_systemVersion"
- "_up_createDirectoryAtURL:error:"
- "_up_uniqueTemporaryFileURLWithIsDirectory:"
- "_updateVersion"
- "allowedTopLevelClasses"
- "allowsKeyedCoding"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendBool:withName:"
- "appendString:withName:"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:counterpart:"
- "appendUnsignedInteger:withName:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bs_CGRectValue"
- "bufferingPolicy"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "bundleForClass:"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "code"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "dataWithContentsOfURL:options:error:"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeUInt64ForKey:"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "destroyPersistentStoreAtURL:withType:options:error:"
- "didAccessValueForKey:"
- "didChangeValueForKey:"
- "domain"
- "encodeInteger:forKey:"
- "encodeUInt64:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "fileURLWithPath:isDirectory:"
- "getResourceValue:forKey:error:"
- "hash"
- "init"
- "initWithBSXPCCoder:"
- "initWithCoder:"
- "initWithMajorVersion:minorVersion:updateVersion:"
- "initWithName:managedObjectModel:"
- "initWithPersistentContainerDescription:recreateStoreOnLoadFailure:"
- "initWithString:"
- "initWithSuiteName:"
- "intValue"
- "isAfter:withPrecision:"
- "isAppleTVDeviceClass"
- "isBefore:withPrecision:"
- "isDeviceClass:"
- "isEqual"
- "isEqual:"
- "isEqualToString:"
- "isFileURL"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSameAs:withPrecision:"
- "isSameAsOrAfter:withPrecision:"
- "isSameAsOrBefore:withPrecision:"
- "length"
- "loadPersistentStoresWithCompletionHandler:"
- "localizedDescription"
- "logger"
- "model"
- "name"
- "newBackgroundContext"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "options"
- "performAndWaitWithBlock:"
- "performBlock:"
- "performBlockAndWait:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentContainerDescription"
- "persistentContainerWithDescription:"
- "persistentStoreCoordinator"
- "persistentStoreDescription"
- "predicateWithFormat:"
- "primitiveValueForKey:"
- "q"
- "q16@0:8"
- "q32@0:8@16q24"
- "registerValueTransformer"
- "release"
- "removeItemAtURL:error:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "save:"
- "scanUnsignedLongLong:"
- "scannerWithString:"
- "self"
- "setMergePolicy:"
- "setObject:forKey:"
- "setPersistentStoreDescriptions:"
- "setPrimitiveValue:forKey:"
- "setShouldAddStoreAsynchronously:"
- "setShouldInferMappingModelAutomatically:"
- "setShouldMigrateStoreAutomatically:"
- "setType:"
- "setURL:"
- "setValueTransformer:forName:"
- "setWithObjects:"
- "shouldYieldNewValue"
- "state"
- "stringValue"
- "stringWithFormat:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "supportsBSXPCSecureCoding"
- "supportsSecureCoding"
- "type"
- "unknownVersion"
- "unsignedIntegerValue"
- "up_CGRectForKey:"
- "up_NSValueForKey:"
- "up_boolForKey:"
- "up_coreFrameworkBundle"
- "up_createDirectoryAtURL:error:"
- "up_createUniqueTemporaryDirectoryAndReturnError:"
- "up_decodeHomogenousCollectionWithCollectionClass:elementClass:forKey:"
- "up_directoryURLWithName:parentDirectoryURL:"
- "up_directoryURLWithName:parentDirectoryURL:error:"
- "up_equalPredicateWithKeyPath:value:"
- "up_frameworkBundle"
- "up_isValidDirectory"
- "up_mappedDataFromFileURL:"
- "up_mappedDataFromFileURL:removeFile:"
- "up_mappedDataFromFileURL:removeFile:error:"
- "up_notEqualPredicateWithKeyPath:value:"
- "up_numberForKey:"
- "up_safeDecodeHomogenousArrayWithElementClass:forKey:"
- "up_safeDecodeHomogenousSetWithElementClass:forKey:"
- "up_saveWithFallbackErrorBlock:outError:"
- "up_setValue:forKey:"
- "up_sqlitePersistentStoreDescriptionWithURL:"
- "up_temporaryDirectoryURL"
- "up_uniqueTemporaryDirectoryURL"
- "up_uniqueTemporaryFileURL"
- "up_userProfilesCoreUserDefaults"
- "up_userProfilesUserDefaults"
- "up_valueForKey:"
- "up_valueInPredicateWithKeyPath:values:"
- "up_valueNotInPredicateWithKeyPath:values:"
- "v16@0:8"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@24"
- "versionWithMajorVersion:"
- "versionWithMajorVersion:minorVersion:"
- "versionWithMajorVersion:minorVersion:updateVersion:"
- "versionWithString:"
- "willAccessValueForKey:"
- "willChangeValueForKey:"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"

```
