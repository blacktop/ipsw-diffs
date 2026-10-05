## manageddeviced

> `/usr/libexec/manageddeviced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0x4039c
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_stubs: 0x8dc0
-  __TEXT.__objc_methlist: 0x3fd4
-  __TEXT.__const: 0x110
-  __TEXT.__objc_methname: 0x9d72
-  __TEXT.__cstring: 0x2f5e
-  __TEXT.__objc_classname: 0xd61
-  __TEXT.__objc_methtype: 0xdf2
-  __TEXT.__gcc_except_tab: 0x6ac
-  __TEXT.__oslogstring: 0x651b
+31.0.0.0.0
+  __TEXT.__text: 0x42778
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x92e0
+  __TEXT.__objc_methlist: 0x41ec
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x708
+  __TEXT.__objc_methname: 0xa4a7
+  __TEXT.__objc_classname: 0xdab
+  __TEXT.__cstring: 0x2f9e
+  __TEXT.__objc_methtype: 0xe98
+  __TEXT.__oslogstring: 0x6897
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__ustring: 0x7d0
-  __TEXT.__unwind_info: 0x1820
-  __DATA_CONST.__const: 0x1960
-  __DATA_CONST.__cfstring: 0x3480
-  __DATA_CONST.__objc_classlist: 0x358
+  __TEXT.__unwind_info: 0x18d8
+  __DATA_CONST.__const: 0x19b0
+  __DATA_CONST.__cfstring: 0x34c0
+  __DATA_CONST.__objc_classlist: 0x368
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0x238
   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x658
-  __DATA_CONST.__got: 0x9a8
-  __DATA.__objc_const: 0x8768
-  __DATA.__objc_selrefs: 0x28d8
-  __DATA.__objc_ivar: 0x1e8
-  __DATA.__objc_data: 0x2170
-  __DATA.__data: 0x480
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x9d0
+  __DATA.__objc_const: 0x8e78
+  __DATA.__objc_selrefs: 0x2a40
+  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_data: 0x2210
+  __DATA.__data: 0x4e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 1703
-  Symbols:   529
-  CStrings:  2684
+  Functions: 1756
+  Symbols:   541
+  CStrings:  2779
 
Symbols:
+ _MDFManagedAppClientObjectInterface
+ _MDFManagedAppEntitlement
+ _MDFManagedAppMachServiceName
+ _MDFManagedAppRemoteObjectInterface
+ _OBJC_CLASS_$_MDFManagedAppEvent
+ _OBJC_CLASS_$_MDFManagedAppSnapshot
+ _OBJC_CLASS_$_NSXPCConnection
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_getProperty
+ _objc_setProperty_atomic_copy
+ _objc_storeWeak
CStrings:
+ "!"
+ "%{public}@ for unknown managed app subscription %{public}@"
+ "@\"NSXPCConnection\""
+ "@40@0:8@16@24@32"
+ "Accepted managed app connection from pid %d"
+ "Duplicate managed app subscription %{public}@ from pid %d"
+ "MDDManagedAppService"
+ "MDDManagedAppSubscriber"
+ "MDFManagedAppRemoteInterface"
+ "Managed app %{public}@ to %lu subscriber(s)"
+ "Managed app connection gone; dropped %lu subscription(s), %lu remaining"
+ "Managed app delivery to subscription %{public}@ failed: %{public}@"
+ "Managed app service instance %{public}@"
+ "Managed app subscription %{public}@ ended (%lu remaining)"
+ "Managed app subscription %{public}@ from pid %d (%lu total)"
+ "No persona to add for bundle:%{public}@. Skipping."
+ "No persona to remove for bundle:%{public}@. Skipping."
+ "Rejecting %{public}@ of managed app subscription %{public}@ from pid %d: not the owning connection"
+ "Rejecting managed app connection from pid %d: missing %{public}@"
+ "Resynchronize"
+ "Resynchronizing managed app subscription %{public}@ (pid %d)"
+ "T@\"NSDictionary\",C,V_cachedManagementStates"
+ "T@\"NSDictionary\",R,C,N"
+ "T@\"NSMutableDictionary\",R,N,V_subscribers"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_stateQueue"
+ "T@\"NSSet\",C,N,V_publishedBundleIdentifiers"
+ "T@\"NSUUID\",R,C,N,V_sourceIdentifier"
+ "T@\"NSXPCConnection\",R,W,N,V_connection"
+ "T@\"NSXPCListener\",R,N,V_managedAppServiceListener"
+ "TB,N,V_reconciliationPending"
+ "TQ,N,V_generation"
+ "Ti,R,N,V_processIdentifier"
+ "UUIDString"
+ "Unhandled app state %lu in managed app membership predicate"
+ "Unsubscribe"
+ "_cachedManagementStates"
+ "_connection"
+ "_currentBundleIdentifiers"
+ "_deliverOnStateQueueEvent:toSubscriber:"
+ "_emitOnStateQueueEventOfType:bundleIdentifiers:"
+ "_generation"
+ "_init"
+ "_managedAppServiceListener"
+ "_managementStatesFromManifestOnQueue"
+ "_ownedSubscriberOnStateQueueWithIdentifier:connection:operation:"
+ "_processIdentifier"
+ "_publishedBundleIdentifiers"
+ "_reconcileOnStateQueue"
+ "_reconciliationPending"
+ "_removeSubscriberWithIdentifier:"
+ "_removeSubscribersForConnection:"
+ "_sendResetOnStateQueueToSubscriber:"
+ "_snapshotOnStateQueue"
+ "_sourceIdentifier"
+ "_stateQueue"
+ "_subscribers"
+ "array"
+ "cachedManagementStates"
+ "com.apple.mdd.managed-apps.state"
+ "connection"
+ "currentConnection"
+ "deliverEvent:forSubscriptionIdentifier:"
+ "dictionary"
+ "fetchManagedAppSnapshotWithReplyHandler:"
+ "generation"
+ "i16@0:8"
+ "initWithIdentifier:connection:"
+ "initWithManagedBundleIdentifiers:sourceIdentifier:generation:creationDate:"
+ "initWithType:bundleIdentifiers:snapshot:sourceIdentifier:generation:creationDate:"
+ "isEqualToSet:"
+ "managedAppServiceListener"
+ "managedAppsMayHaveChanged"
+ "managementStatesByBundleIdentifier"
+ "minusSet:"
+ "publishedBundleIdentifiers"
+ "reconciliationPending"
+ "remoteObjectProxyWithErrorHandler:"
+ "resynchronizeSubscriptionWithIdentifier:"
+ "setCachedManagementStates:"
+ "setGeneration:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setPublishedBundleIdentifiers:"
+ "setReconciliationPending:"
+ "setRemoteObjectInterface:"
+ "setWithCapacity:"
+ "sharedService"
+ "stateQueue"
+ "subscribeWithIdentifier:replyHandler:"
+ "subscribers"
+ "unsubscribeWithIdentifier:"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@?<v@?@\"MDFManagedAppSnapshot\"@\"NSError\">16"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
+ "v32@0:8q16@24"
```
