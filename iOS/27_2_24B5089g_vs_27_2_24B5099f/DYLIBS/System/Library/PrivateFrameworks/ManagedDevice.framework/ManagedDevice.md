## ManagedDevice

> `/System/Library/PrivateFrameworks/ManagedDevice.framework/ManagedDevice`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0x298e8
-  __TEXT.__objc_methlist: 0x5434
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x4920
+31.0.0.0.0
+  __TEXT.__text: 0x2d820
+  __TEXT.__objc_methlist: 0x5824
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x4bb3
   __TEXT.__ustring: 0x9d8
-  __TEXT.__oslogstring: 0x712
-  __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__unwind_info: 0xc80
+  __TEXT.__oslogstring: 0x99c
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__unwind_info: 0xe38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc98
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __DATA_CONST.__const: 0xe98
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16d0
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x18c0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x4d0
-  __DATA_CONST.__got: 0x280
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x65c0
-  __AUTH_CONST.__objc_const: 0xb9a0
+  __DATA_CONST.__got: 0x298
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x68c0
+  __AUTH_CONST.__objc_const: 0xc670
   __AUTH_CONST.__objc_intobj: 0xf90
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x2120
-  __DATA.__objc_ivar: 0x750
-  __DATA.__data: 0x2a0
-  __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x30
+  __AUTH.__objc_data: 0x2210
+  __DATA.__objc_ivar: 0x7b8
+  __DATA.__data: 0x360
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1704
-  Symbols:   3547
-  CStrings:  875
+  Functions: 1834
+  Symbols:   3748
+  CStrings:  915
 
Symbols:
+ +[MDFManagedAppEvent supportsSecureCoding]
+ +[MDFManagedAppMonitor sharedMonitor]
+ +[MDFManagedAppSnapshot supportsSecureCoding]
+ -[MDFManagedAppEvent .cxx_destruct]
+ -[MDFManagedAppEvent bundleIdentifiers]
+ -[MDFManagedAppEvent copyWithZone:]
+ -[MDFManagedAppEvent creationDate]
+ -[MDFManagedAppEvent description]
+ -[MDFManagedAppEvent encodeWithCoder:]
+ -[MDFManagedAppEvent generation]
+ -[MDFManagedAppEvent initWithCoder:]
+ -[MDFManagedAppEvent initWithType:bundleIdentifiers:snapshot:sourceIdentifier:generation:creationDate:]
+ -[MDFManagedAppEvent setByApplyingToSet:]
+ -[MDFManagedAppEvent snapshot]
+ -[MDFManagedAppEvent sourceIdentifier]
+ -[MDFManagedAppEvent type]
+ -[MDFManagedAppMonitor .cxx_destruct]
+ -[MDFManagedAppMonitor _abandonSubscription:error:]
+ -[MDFManagedAppMonitor _forgetSubscription:]
+ -[MDFManagedAppMonitor _handOffEvent:toSubscription:]
+ -[MDFManagedAppMonitor _ingestEvent:forSubscription:]
+ -[MDFManagedAppMonitor _init]
+ -[MDFManagedAppMonitor _invalidateAllSubscriptionsWithReason:error:]
+ -[MDFManagedAppMonitor _makeAndRegisterSubscriptionWithEventHandler:invalidationHandler:]
+ -[MDFManagedAppMonitor _openSubscription:completionHandler:]
+ -[MDFManagedAppMonitor _requestResynchronizationForSubscription:]
+ -[MDFManagedAppMonitor dealloc]
+ -[MDFManagedAppMonitor deliverEvent:forSubscriptionIdentifier:]
+ -[MDFManagedAppMonitor fetchSnapshotWithCompletionHandler:]
+ -[MDFManagedAppMonitor fetchSnapshotWithError:]
+ -[MDFManagedAppMonitor stateQueue]
+ -[MDFManagedAppMonitor subscribeWithEventHandler:invalidationHandler:completionHandler:]
+ -[MDFManagedAppMonitor subscribeWithEventHandler:invalidationHandler:error:]
+ -[MDFManagedAppMonitor subscriptionsByIdentifier]
+ -[MDFManagedAppMonitor xpcConnection]
+ -[MDFManagedAppSnapshot .cxx_destruct]
+ -[MDFManagedAppSnapshot bundleIdentifiersAddedSinceSnapshot:]
+ -[MDFManagedAppSnapshot bundleIdentifiersRemovedSinceSnapshot:]
+ -[MDFManagedAppSnapshot copyWithZone:]
+ -[MDFManagedAppSnapshot creationDate]
+ -[MDFManagedAppSnapshot description]
+ -[MDFManagedAppSnapshot encodeWithCoder:]
+ -[MDFManagedAppSnapshot generation]
+ -[MDFManagedAppSnapshot initWithCoder:]
+ -[MDFManagedAppSnapshot initWithManagedBundleIdentifiers:sourceIdentifier:generation:creationDate:]
+ -[MDFManagedAppSnapshot isNewerThanSnapshot:]
+ -[MDFManagedAppSnapshot managedBundleIdentifiers]
+ -[MDFManagedAppSnapshot requiresFullRebuildFromSnapshot:]
+ -[MDFManagedAppSnapshot sourceIdentifier]
+ -[MDFManagedAppSubscription .cxx_destruct]
+ -[MDFManagedAppSubscription awaitingReset]
+ -[MDFManagedAppSubscription dealloc]
+ -[MDFManagedAppSubscription deliveredGeneration]
+ -[MDFManagedAppSubscription deliveredSourceIdentifier]
+ -[MDFManagedAppSubscription deliveryQueue]
+ -[MDFManagedAppSubscription description]
+ -[MDFManagedAppSubscription eventHandler]
+ -[MDFManagedAppSubscription identifier]
+ -[MDFManagedAppSubscription initWithIdentifier:eventHandler:invalidationHandler:resynchronizeBlock:cancellationBlock:]
+ -[MDFManagedAppSubscription invalidate]
+ -[MDFManagedAppSubscription invalidationHandler]
+ -[MDFManagedAppSubscription isOpen]
+ -[MDFManagedAppSubscription isValid]
+ -[MDFManagedAppSubscription markInvalidWithReason:error:]
+ -[MDFManagedAppSubscription markInvalidWithReason:error:notifyInvalidationHandler:]
+ -[MDFManagedAppSubscription pendingEvents]
+ -[MDFManagedAppSubscription resynchronize]
+ -[MDFManagedAppSubscription setAwaitingReset:]
+ -[MDFManagedAppSubscription setDeliveredGeneration:]
+ -[MDFManagedAppSubscription setDeliveredSourceIdentifier:]
+ -[MDFManagedAppSubscription setOpen:]
+ GCC_except_table14
+ GCC_except_table19
+ GCC_except_table36
+ GCC_except_table42
+ GCC_except_table6
+ _MDFManagedAppClientObjectInterface
+ _MDFManagedAppClientObjectInterface.interface
+ _MDFManagedAppClientObjectInterface.onceToken
+ _MDFManagedAppEntitlement
+ _MDFManagedAppMachServiceName
+ _MDFManagedAppRemoteObjectInterface
+ _MDFManagedAppRemoteObjectInterface.interface
+ _MDFManagedAppRemoteObjectInterface.onceToken
+ _OBJC_CLASS_$_MDFManagedAppEvent
+ _OBJC_CLASS_$_MDFManagedAppMonitor
+ _OBJC_CLASS_$_MDFManagedAppSnapshot
+ _OBJC_CLASS_$_MDFManagedAppSubscription
+ _OBJC_IVAR_$_MDFManagedAppEvent._bundleIdentifiers
+ _OBJC_IVAR_$_MDFManagedAppEvent._creationDate
+ _OBJC_IVAR_$_MDFManagedAppEvent._generation
+ _OBJC_IVAR_$_MDFManagedAppEvent._snapshot
+ _OBJC_IVAR_$_MDFManagedAppEvent._sourceIdentifier
+ _OBJC_IVAR_$_MDFManagedAppEvent._type
+ _OBJC_IVAR_$_MDFManagedAppMonitor._stateQueue
+ _OBJC_IVAR_$_MDFManagedAppMonitor._subscriptionsByIdentifier
+ _OBJC_IVAR_$_MDFManagedAppMonitor._xpcConnection
+ _OBJC_IVAR_$_MDFManagedAppSnapshot._creationDate
+ _OBJC_IVAR_$_MDFManagedAppSnapshot._generation
+ _OBJC_IVAR_$_MDFManagedAppSnapshot._managedBundleIdentifiers
+ _OBJC_IVAR_$_MDFManagedAppSnapshot._sourceIdentifier
+ _OBJC_IVAR_$_MDFManagedAppSubscription._awaitingReset
+ _OBJC_IVAR_$_MDFManagedAppSubscription._cancellationBlock
+ _OBJC_IVAR_$_MDFManagedAppSubscription._deliveredGeneration
+ _OBJC_IVAR_$_MDFManagedAppSubscription._deliveredSourceIdentifier
+ _OBJC_IVAR_$_MDFManagedAppSubscription._deliveryQueue
+ _OBJC_IVAR_$_MDFManagedAppSubscription._eventHandler
+ _OBJC_IVAR_$_MDFManagedAppSubscription._identifier
+ _OBJC_IVAR_$_MDFManagedAppSubscription._invalidationHandler
+ _OBJC_IVAR_$_MDFManagedAppSubscription._open
+ _OBJC_IVAR_$_MDFManagedAppSubscription._pendingEvents
+ _OBJC_IVAR_$_MDFManagedAppSubscription._resynchronizeBlock
+ _OBJC_IVAR_$_MDFManagedAppSubscription._validUnderLock
+ _OBJC_IVAR_$_MDFManagedAppSubscription._validityLock
+ _OBJC_METACLASS_$_MDFManagedAppEvent
+ _OBJC_METACLASS_$_MDFManagedAppMonitor
+ _OBJC_METACLASS_$_MDFManagedAppSnapshot
+ _OBJC_METACLASS_$_MDFManagedAppSubscription
+ __OBJC_$_CLASS_METHODS_MDFManagedAppEvent
+ __OBJC_$_CLASS_METHODS_MDFManagedAppMonitor
+ __OBJC_$_CLASS_METHODS_MDFManagedAppSnapshot
+ __OBJC_$_CLASS_PROP_LIST_MDFManagedAppEvent
+ __OBJC_$_CLASS_PROP_LIST_MDFManagedAppMonitor
+ __OBJC_$_CLASS_PROP_LIST_MDFManagedAppSnapshot
+ __OBJC_$_INSTANCE_METHODS_MDFManagedAppEvent
+ __OBJC_$_INSTANCE_METHODS_MDFManagedAppMonitor
+ __OBJC_$_INSTANCE_METHODS_MDFManagedAppSnapshot
+ __OBJC_$_INSTANCE_METHODS_MDFManagedAppSubscription
+ __OBJC_$_INSTANCE_VARIABLES_MDFManagedAppEvent
+ __OBJC_$_INSTANCE_VARIABLES_MDFManagedAppMonitor
+ __OBJC_$_INSTANCE_VARIABLES_MDFManagedAppSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_MDFManagedAppSubscription
+ __OBJC_$_PROP_LIST_MDFManagedAppEvent
+ __OBJC_$_PROP_LIST_MDFManagedAppMonitor
+ __OBJC_$_PROP_LIST_MDFManagedAppSnapshot
+ __OBJC_$_PROP_LIST_MDFManagedAppSubscription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MDFManagedAppClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MDFManagedAppRemoteInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MDFManagedAppClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MDFManagedAppRemoteInterface
+ __OBJC_$_PROTOCOL_REFS_MDFManagedAppClientInterface
+ __OBJC_$_PROTOCOL_REFS_MDFManagedAppRemoteInterface
+ __OBJC_CLASS_PROTOCOLS_$_MDFManagedAppEvent
+ __OBJC_CLASS_PROTOCOLS_$_MDFManagedAppMonitor
+ __OBJC_CLASS_PROTOCOLS_$_MDFManagedAppSnapshot
+ __OBJC_CLASS_RO_$_MDFManagedAppEvent
+ __OBJC_CLASS_RO_$_MDFManagedAppMonitor
+ __OBJC_CLASS_RO_$_MDFManagedAppSnapshot
+ __OBJC_CLASS_RO_$_MDFManagedAppSubscription
+ __OBJC_LABEL_PROTOCOL_$_MDFManagedAppClientInterface
+ __OBJC_LABEL_PROTOCOL_$_MDFManagedAppRemoteInterface
+ __OBJC_METACLASS_RO_$_MDFManagedAppEvent
+ __OBJC_METACLASS_RO_$_MDFManagedAppMonitor
+ __OBJC_METACLASS_RO_$_MDFManagedAppSnapshot
+ __OBJC_METACLASS_RO_$_MDFManagedAppSubscription
+ __OBJC_PROTOCOL_$_MDFManagedAppClientInterface
+ __OBJC_PROTOCOL_$_MDFManagedAppRemoteInterface
+ __OBJC_PROTOCOL_REFERENCE_$_MDFManagedAppClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_MDFManagedAppRemoteInterface
+ ___29-[MDFManagedAppMonitor _init]_block_invoke
+ ___29-[MDFManagedAppMonitor _init]_block_invoke_2
+ ___37+[MDFManagedAppMonitor sharedMonitor]_block_invoke
+ ___44-[MDFManagedAppMonitor _forgetSubscription:]_block_invoke
+ ___44-[MDFManagedAppMonitor _forgetSubscription:]_block_invoke_2
+ ___47-[MDFManagedAppMonitor fetchSnapshotWithError:]_block_invoke
+ ___47-[MDFManagedAppMonitor fetchSnapshotWithError:]_block_invoke_2
+ ___51-[MDFManagedAppMonitor _abandonSubscription:error:]_block_invoke
+ ___53-[MDFManagedAppMonitor _handOffEvent:toSubscription:]_block_invoke
+ ___59-[MDFManagedAppMonitor fetchSnapshotWithCompletionHandler:]_block_invoke
+ ___60-[MDFManagedAppMonitor _openSubscription:completionHandler:]_block_invoke
+ ___63-[MDFManagedAppMonitor deliverEvent:forSubscriptionIdentifier:]_block_invoke
+ ___65-[MDFManagedAppMonitor _requestResynchronizationForSubscription:]_block_invoke
+ ___65-[MDFManagedAppMonitor _requestResynchronizationForSubscription:]_block_invoke_2
+ ___68-[MDFManagedAppMonitor _invalidateAllSubscriptionsWithReason:error:]_block_invoke
+ ___76-[MDFManagedAppMonitor subscribeWithEventHandler:invalidationHandler:error:]_block_invoke
+ ___76-[MDFManagedAppMonitor subscribeWithEventHandler:invalidationHandler:error:]_block_invoke_2
+ ___83-[MDFManagedAppSubscription markInvalidWithReason:error:notifyInvalidationHandler:]_block_invoke
+ ___88-[MDFManagedAppMonitor subscribeWithEventHandler:invalidationHandler:completionHandler:]_block_invoke
+ ___89-[MDFManagedAppMonitor _makeAndRegisterSubscriptionWithEventHandler:invalidationHandler:]_block_invoke
+ ___89-[MDFManagedAppMonitor _makeAndRegisterSubscriptionWithEventHandler:invalidationHandler:]_block_invoke_2
+ ___89-[MDFManagedAppMonitor _makeAndRegisterSubscriptionWithEventHandler:invalidationHandler:]_block_invoke_3
+ ___MDFManagedAppClientObjectInterface_block_invoke
+ ___MDFManagedAppRemoteObjectInterface_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32w_e35_v16?0"MDFManagedAppSubscription"8lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"MDFManagedAppSnapshot"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e43_v24?0"MDFManagedAppSnapshot"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ _dispatch_sync
+ _objc_retainAutoreleasedReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sharedMonitor.onceToken
+ _sharedMonitor.sharedMonitor
CStrings:
+ "(type == MDFManagedAppEventTypeReset) == (snapshot != nil)"
+ "<%@: %@ %lu app(s), source %@, generation %llu>"
+ "<%@: %@, %@, generation %llu>"
+ "<%@: %lu app(s), source %@, generation %llu>"
+ "Dropping managed app delta while awaiting reset for %{public}@"
+ "MDFManagedAppEvent.m"
+ "MDFManagedAppMonitor.m"
+ "MDFManagedAppSnapshot.m"
+ "MDFManagedAppSubscription.m"
+ "Managed app connection lost (reason %ld); invalidating subscriptions"
+ "Managed app event delivered with nil event or identifier"
+ "Managed app event for unknown subscription %{public}@"
+ "Managed app event stream broke for %{public}@: expected generation %llu, got %llu (source %{public}@)"
+ "Managed app fetch failed: %{public}@"
+ "Managed app resynchronize failed: %{public}@"
+ "Managed app subscribe (sync) failed: %{public}@"
+ "Managed app subscribe failed: %{public}@"
+ "Managed app subscribe refused: %{public}@"
+ "Managed app subscription established: %{public}@"
+ "Managed app unsubscribe failed: %{public}@"
+ "added"
+ "changed"
+ "com.apple.manageddeviced.managed-apps"
+ "com.apple.manageddeviced.managed-apps.read"
+ "com.apple.mdf.managed-apps.delivery"
+ "com.apple.mdf.managed-apps.state"
+ "completionHandler"
+ "creationDate"
+ "eventHandler"
+ "generation"
+ "invalid"
+ "managedBundleIdentifiers"
+ "removed"
+ "reset"
+ "same"
+ "snapshot"
+ "unknown"
+ "v16@?0@\"MDFManagedAppSubscription\"8"
+ "v24@?0@\"MDFManagedAppSnapshot\"8@\"NSError\"16"
+ "valid"
```
