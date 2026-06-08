## fskitd

> `/usr/libexec/fskitd`

```diff

-737.120.9.0.0
-  __TEXT.__text: 0x442e0
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_stubs: 0x4a60
-  __TEXT.__objc_methlist: 0x1f44
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x2414
-  __TEXT.__oslogstring: 0x3c75
-  __TEXT.__cstring: 0x2e0a
-  __TEXT.__objc_classname: 0x22d
-  __TEXT.__objc_methname: 0x5845
-  __TEXT.__objc_methtype: 0x1e58
-  __TEXT.__unwind_info: 0xfa8
-  __DATA_CONST.__auth_got: 0x560
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x20f0
-  __DATA_CONST.__cfstring: 0x7a0
+971.0.0.0.5
+  __TEXT.__text: 0x4bf60
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_stubs: 0x5240
+  __TEXT.__objc_methlist: 0x22cc
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0x1f08
+  __TEXT.__oslogstring: 0x44b0
+  __TEXT.__cstring: 0x388e
+  __TEXT.__objc_classname: 0x1fa
+  __TEXT.__objc_methname: 0x67ec
+  __TEXT.__objc_methtype: 0x27cf
+  __TEXT.__unwind_info: 0x1138
+  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x21f0
-  __DATA.__objc_selrefs: 0x16d8
-  __DATA.__objc_ivar: 0x174
+  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__got: 0x360
+  __DATA.__objc_const: 0x2300
+  __DATA.__objc_selrefs: 0x1908
+  __DATA.__objc_ivar: 0x180
   __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x710
+  __DATA.__data: 0x718
   __DATA.__common: 0x88
   __DATA.__bss: 0x61
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: E8E54D35-469C-36FE-A748-3BCE63EB65C5
-  Functions: 1313
-  Symbols:   288
-  CStrings:  1961
+  UUID: 5378E725-3BA1-3956-BAA9-EDFFAAE8B4A9
+  Functions: 1480
+  Symbols:   302
+  CStrings:  2177
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _FSModuleIdentityAttributeAlwaysIgnoreOwnership
+ _FSTaskPurposeAddVolume
+ _FSTaskPurposeRemoveVolume
+ _OBJC_CLASS_$_FSMachPort
+ ___NSArray0__struct
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _usleep
- _OBJC_CLASS_$_FSResourceManager
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s: About to start add volume task UUID (%@) on container (%@)"
+ "%s: About to start remove volume task UUID (%@) on container (%@)"
+ "%s: About to talk to the connection for %@"
+ "%s: Add volume task UUID (%@) on container (%@) is running"
+ "%s: Adding volumeDescription %@ to our instance"
+ "%s: Client has LiveFS.connection entitlement"
+ "%s: Client missing 'com.apple.private.fskit.mountAt' entitlement for path '%@'"
+ "%s: Couldn't create mount point for %@"
+ "%s: Created plugin mount instance for resource tracking"
+ "%s: Failed to activate volume: %@"
+ "%s: Failed to create SecTask"
+ "%s: Failed to deactivate volume during cleanup: %@"
+ "%s: Failed to load resource: %@"
+ "%s: Failed to mount volume: %@"
+ "%s: Failed to unload resource during cleanup: %@"
+ "%s: Generated mount reference %u for mount index %u"
+ "%s: Given resource (%@) not being used by any instance, returning ESTALE"
+ "%s: No module found with bundle ID '%@'"
+ "%s: Options MNT_FORCE, MNT_UPDATE, MNT_RELOAD not supported"
+ "%s: Path '%@' does not match any allowed prefixes in mountAt entitlement"
+ "%s: Path '%@' matches allowed prefix '%@'"
+ "%s: Remove volume task UUID (%@) on container (%@) is running"
+ "%s: Resource %@, already exists"
+ "%s: Starting with containerID (%@)"
+ "%s: Task UUID (%@), apply container error (%@), add volume error (%@)"
+ "%s: Task UUID (%@), apply container error (%@), remove volume error (%@)"
+ "%s: Task with UUID (%@) is running on given container (%@)"
+ "%s: Task with the same UUID (%@) is running"
+ "%s: Using existing FSKit instance for resource tracking"
+ "%s: feature flag useInlineData is enabled"
+ "%s: loadResource returned no volumes"
+ "%s: loadResource returned volume count of %lu, this method only mounts single volume file systems"
+ "%s: mount path is nil, try to create mount point for volume %@"
+ "%s: mountAt entitlement is not an array"
+ "%s: spontaneous unmount cleanup done with error %@ name %@"
+ "%s:%@: Can't start new task (%@), resource state is %d"
+ "%s:%@: Can't start probe task (%@), resource state is %d"
+ "%s:end:%@"
+ "%s:error: resourceID is nil"
+ "%s:finish:bundleID(%@):resource(%@):mountPath(%@):options(%@):actualMountURL(%@)"
+ "%s:hasEntitlement(%d)"
+ "%s:start:%@"
+ "%s:start:bundleID(%@):resource(%@):mountPath(%@):options(%@)"
+ "-[FSVolumeConnectorBridge makeDirectoryIn:named:attributes:auditToken:requestID:reply:]_block_invoke"
+ "-[FSVolumeConnectorBridge seek:fromOffset:forRegion:auditToken:requestID:reply:]"
+ "-[LiveFSVolumeCore_FSFileNameBridge otherAttributeOf:named:requestID:reply:]_block_invoke"
+ "-[fskitdExtensionClient addVolumeDescription:replyHandler:]"
+ "-[fskitdExtensionInstance addResource:]"
+ "-[fskitdExtensionInstance closeResource:andRevoke:]"
+ "-[fskitdExtensionInstance removeResource:]"
+ "-[fskitdExtensionInstance updateResource:]"
+ "-[fskitdMounter mount:]"
+ "-[fskitdXPCServer LiveMounterReallyMountVolume:fileSystem:displayName:provider:domainError:on:how:optionString:auditToken:reply:]"
+ "-[fskitdXPCServer _addVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _addVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke_2"
+ "-[fskitdXPCServer _deactivateVolume:usingIdentity:numericOptions:auditToken:replyHandler:]_block_invoke_4"
+ "-[fskitdXPCServer _loadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke_6"
+ "-[fskitdXPCServer _removeVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer _removeVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke_2"
+ "-[fskitdXPCServer applyContainer:usingIdentity:initiatorAuditToken:authorizingAuditToken:usingBlock:]"
+ "-[fskitdXPCServer canStartAddRemoveVolumeTask:containerID:]_block_invoke"
+ "-[fskitdXPCServer mountSingleVolumeForResource:bundleID:mountPath:options:replyHandler:]"
+ "-[fskitdXPCServer mountSingleVolumeForResource:bundleID:mountPath:options:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer mountSingleVolumeForResource:bundleID:mountPath:options:replyHandler:]_block_invoke_2"
+ "-[fskitdXPCServer tokenHasMountEntitlement:forPath:]"
+ "-[mountEntry createMountTaskForBSDName:]"
+ "@32@0:8@16^@24"
+ "@56@0:8@16@24@32@40@?48"
+ "@56@0:8{?=[8I]}16@48"
+ "Adding taskID %@ to instance %@"
+ "B56@0:8{?=[8I]}16@48"
+ "Client is missing 'com.apple.developer.fskit.mount' entitlement"
+ "Extension launch backoff completed"
+ "Extension launch failed, backing off before trying again loop %d"
+ "I32@0:8@16^@24"
+ "LiveMounterReallyMountVolume:fileSystem:displayName:provider:domainError:on:how:optionString:auditToken:reply:"
+ "Read zero-copy %@"
+ "T@\"NSMutableArray\",&,V_volumeDescriptions"
+ "T@\"NSMutableDictionary\",&,V_resources"
+ "T@\"NSMutableSet\",&,V_taskIDs"
+ "TB,R,V_ignoreOwnership"
+ "TB,V_devicefs_hacks"
+ "TB,V_ignoreOwnership"
+ "TI,R,V_mountReference"
+ "_N_INACTIVE"
+ "_N_mntflags"
+ "_addVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:"
+ "_devicefs_hacks"
+ "_ignoreOwnership"
+ "_mountReference"
+ "_removeVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:"
+ "_resources"
+ "_volumeDescriptions"
+ "activateVolume:resource:options:auditToken:replyHandler:"
+ "addResource:toInstance:"
+ "addVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:"
+ "addVolume:containerID:usingBundle:options:connection:replyHandler:"
+ "addVolume:options:connection:taskID:replyHandler:"
+ "addVolumeDescription:"
+ "addVolumeDescription:replyHandler:"
+ "apfsUseFSKitModule"
+ "applyContainer:usingIdentity:initiatorAuditToken:authorizingAuditToken:usingBlock:"
+ "canStartAddRemoveVolumeTask:containerID:"
+ "checkAccessTo:requestedAccess:auditToken:requestID:reply:"
+ "checkAccessTo:requestedAccess:auditToken:requestID:replyHandler:"
+ "close:keepingMode:auditToken:requestID:reply:"
+ "close:keepingMode:auditToken:requestID:replyHandler:"
+ "closeItem:auditToken:requestID:reply:"
+ "closeItem:auditToken:requestID:replyHandler:"
+ "com.apple.developer.fskit.mount"
+ "com.apple.diskarbitrationd"
+ "com.apple.dt.CoreDevice.Extensions.devicefs"
+ "com.apple.fskit.PluginMountedBundle"
+ "com.apple.private.fskit.mountAt"
+ "createCloneOfItem:named:inDirectory:attributes:usingFlags:auditToken:requestID:replyHandler:"
+ "createExtensionInstanceForPluginMount:"
+ "createIn:named:attributes:auditToken:requestID:reply:"
+ "createIn:named:type:attributes:auditToken:requestID:replyHandler:"
+ "createMountPoint:error:"
+ "createStreamOfItem:named:auditToken:requestID:replyHandler:"
+ "devicefs_hacks"
+ "devices"
+ "doTearDown"
+ "fileAttributes:auditToken:requestID:reply:"
+ "fileAttributes:requestedAttributes:auditToken:requestID:replyHandler:"
+ "findInstanceForResource:"
+ "firstObject"
+ "getAllResources"
+ "getBytes:length:"
+ "getMountIndexFromVolumeID:error:"
+ "ignoreOwnership"
+ "initWithMachPort:capacity:length:wrapsIOWMD:"
+ "initWithPort:"
+ "lifs_cache_close_send"
+ "lifs_cache_close_send_block_invoke"
+ "lifs_cache_open_send"
+ "lifs_cache_open_send_block_invoke"
+ "lifs_cache_upgrade_send"
+ "lifs_cache_upgrade_send_block_invoke"
+ "lifs_create_namedstream_send"
+ "lifs_create_namedstream_send_block_invoke"
+ "lifs_lookup_namedstream_send"
+ "lifs_lookup_namedstream_send_block_invoke"
+ "lifs_read_wrapped_send"
+ "lifs_remove_namedstream_send"
+ "lifs_remove_namedstream_send_block_invoke"
+ "lifs_seek_send"
+ "lifs_seek_send_block_invoke"
+ "lifs_write_wrapped_send"
+ "listXattrsOf:auditToken:requestID:reply:"
+ "listXattrsOf:auditToken:requestID:replyHandler:"
+ "lookupIn:name:flags:auditToken:requestID:replyHandler:"
+ "lookupIn:name:usingFlags:auditToken:requestID:reply:"
+ "lookupStreamOfItem:named:auditToken:requestID:replyHandler:"
+ "makeCloneOf:named:inDirectory:attributes:usingFlags:auditToken:requestID:reply:"
+ "makeDirectoryIn:named:attributes:auditToken:requestID:reply:"
+ "makeLinkOf:named:inDirectory:auditToken:requestID:reply:"
+ "makeLinkOf:named:inDirectory:auditToken:requestID:replyHandler:"
+ "makeSymLinkIn:named:contents:attributes:auditToken:requestID:reply:"
+ "makeSymlinkIn:named:contents:attributes:auditToken:requestID:replyHandler:"
+ "moduleAuditToken"
+ "mount:reference:reply:"
+ "mount:reference:replyHandler:"
+ "mountActivatedVolume:fileSystem:displayName:provider:on:how:options:auditToken:replyHandler:"
+ "mountActivatedVolume:fileSystem:displayName:provider:on:how:options:replyHandler:"
+ "mountReference"
+ "mountSingleVolumeForResource:bundleID:mountPath:options:replyHandler:"
+ "mountVolume:fileSystem:displayName:provider:domainError:on:how:optionsAsArray:reply:"
+ "newPluginMountInstance:"
+ "nextMountReference"
+ "open:withMode:auditToken:requestID:reply:"
+ "open:withMode:auditToken:requestID:replyHandler:"
+ "openItem:modes:cacheMode:auditToken:requestID:reply:"
+ "openItem:modes:cacheMode:auditToken:requestID:replyHandler:"
+ "readDirectory:intoBuffer:cookie:verifier:auditToken:requestID:reply:"
+ "readDirectory:intoBuffer:cookie:verifier:auditToken:requestID:replyHandler:"
+ "readDirectory:intoBuffer:requestedAttributes:cookie:verifier:auditToken:requestID:reply:"
+ "readDirectory:requestedAttributes:intoBuffer:cookie:verifier:auditToken:requestID:replyHandler:"
+ "readFrom:atOffset:length:machPort:requestID:reply:"
+ "readFrom:atOffset:length:machPort:requestID:replyHandler:"
+ "readLinkOf:auditToken:requestID:reply:"
+ "readSymbolicLinkOf:auditToken:requestID:replyHandler:"
+ "reclaim:lookupCount:requestID:reply:"
+ "reclaim:lookupCount:requestID:replyHandler:"
+ "removeDirectory:from:named:usingFlags:auditToken:requestID:reply:"
+ "removeDirectory:from:named:usingFlags:auditToken:requestID:replyHandler:"
+ "removeItem:from:named:usingFlags:auditToken:requestID:reply:"
+ "removeItem:from:named:usingFlags:auditToken:requestID:replyHandler:"
+ "removeStream:named:fromItem:auditToken:requestID:replyHandler:"
+ "removeVolume:containerID:usingBundle:options:auditToken:connection:replyHandler:"
+ "removeVolume:containerID:usingBundle:options:connection:replyHandler:"
+ "removeVolume:options:connection:taskID:replyHandler:"
+ "removeVolumeDescription:"
+ "renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:auditToken:requestID:reply:"
+ "renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:auditToken:requestID:replyHandler:"
+ "resources"
+ "sandboxCheckAuditToken:mountPath:"
+ "seek:fromOffset:forRegion:auditToken:requestID:reply:"
+ "seek:fromOffset:forRegion:auditToken:requestID:replyHandler:"
+ "setDevicefs_hacks:"
+ "setFileAttributesOf:to:auditToken:requestID:reply:"
+ "setFileAttributesOf:to:auditToken:requestID:replyHandler:"
+ "setIgnoreOwnership:"
+ "setOtherAttributeOf:named:value:auditToken:requestID:reply:"
+ "setOtherAttributeOf:named:value:auditToken:requestID:replyHandler:"
+ "setResources:"
+ "setSupportsSyncingTrash:"
+ "setVolumeDescriptions:"
+ "setXattrOf:named:value:how:auditToken:requestID:reply:"
+ "setXattrOf:named:value:how:auditToken:requestID:replyHandler:"
+ "state"
+ "taskOptions"
+ "tokenHasMountEntitlement:forPath:"
+ "upgradeItem:cacheMode:auditToken:requestID:reply:"
+ "upgradeItem:cacheMode:auditToken:requestID:replyHandler:"
+ "useInlineData"
+ "v108@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48i56@\"NSArray\"60{?=[8I]}68@?<v@?@\"NSError\">100"
+ "v108@0:8@16@24@32@40@48i56@60{?=[8I]}68@?100"
+ "v20@?0i8Q12"
+ "v20@?0i8q12"
+ "v24@?0@\"FSVolumeIdentifier\"8@\"NSError\"16"
+ "v28@?0i8@\"FSFileHandle\"12@\"NSData\"20"
+ "v32@0:8@\"FSVolumeDescription\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@24"
+ "v32@?0@\"NSNumber\"8@\"mountEntry\"16^B24"
+ "v32@?0@\"NSString\"8@\"FSResource\"16^B24"
+ "v36@0:8@\"FSTaskOptionsBundle\"16I24@?<v@?i>28"
+ "v36@0:8@16I24@?28"
+ "v40@?0@\"NSString\"8@\"NSXPCConnection\"16@\"fskitdExtensionInstance\"24@?<v@?@\"FSTaskDescription\">32"
+ "v44@0:8@\"NSString\"16I24Q28@?<v@?i@\"NSData\">36"
+ "v48@0:8@\"NSString\"16@\"FSAuditToken\"24Q32@?<v@?i>40"
+ "v48@0:8@\"NSString\"16@\"FSAuditToken\"24Q32@?<v@?i@\"NSArray\">40"
+ "v48@0:8@\"NSString\"16@\"FSAuditToken\"24Q32@?<v@?i@\"NSData\">40"
+ "v48@0:8@\"NSString\"16@\"FSAuditToken\"24Q32@?<v@?i@\"NSData\"@\"NSData\">40"
+ "v48@?0@\"NSString\"8@\"FSResource\"16@\"NSXPCConnection\"24@\"fskitdExtensionInstance\"32@?<v@?@\"FSTaskDescription\">40"
+ "v52@0:8@\"NSString\"16I24@\"FSAuditToken\"28Q36@?<v@?i>44"
+ "v52@0:8@\"NSString\"16i24@\"FSAuditToken\"28Q36@?<v@?i>44"
+ "v52@0:8@\"NSString\"16i24@\"FSAuditToken\"28Q36@?<v@?ii>44"
+ "v52@0:8@16I24@28Q36@?44"
+ "v52@0:8@16i24@28Q36@?44"
+ "v56@0:8@\"FSResource\"16@\"NSString\"24@\"NSString\"32@\"FSTaskOptionsBundle\"40@?<v@?@\"NSURL\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"FSAuditToken\"32Q40@?<v@?i@\"NSData\">48"
+ "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"FSAuditToken\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"FSAuditToken\"32Q40@?<v@?i@\"NSString\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16@\"NSData\"24@\"FSAuditToken\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16i24i28@\"FSAuditToken\"32Q40@?<v@?ii>48"
+ "v56@0:8@16i24i28@32Q40@?48"
+ "v60@0:8@\"NSString\"16@\"FSFileName\"24I32@\"FSAuditToken\"36Q44@?<v@?ii@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">52"
+ "v60@0:8@\"NSString\"16Q24I32@\"FSAuditToken\"36Q44@?<v@?iQ>52"
+ "v60@0:8@16@24I32@36Q44@?52"
+ "v60@0:8@16Q24I32@36Q44@?52"
+ "v60@?0i8q12@\"NSData\"20@\"FSFileHandle\"28@\"NSData\"36@\"NSData\"44@\"NSData\"52"
+ "v60@?0i8q12@\"NSData\"20@\"NSString\"28@\"NSData\"36@\"NSData\"44@\"NSData\"52"
+ "v64@0:8@\"FSFileName\"16@\"FSContainerIdentifier\"24@\"NSString\"32@\"FSTaskOptionsBundle\"40@\"FSMessageConnection\"48@?<v@?@\"NSUUID\"@\"NSError\">56"
+ "v64@0:8@\"FSVolumeIdentifier\"16@\"FSContainerIdentifier\"24@\"NSString\"32@\"FSTaskOptionsBundle\"40@\"FSMessageConnection\"48@?<v@?@\"NSUUID\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32@\"FSAuditToken\"40Q48@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32@\"FSAuditToken\"40Q48@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32@\"FSAuditToken\"40Q48@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"FSAuditToken\"40Q48@?<v@?i@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"FSAuditToken\"40Q48@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16Q24Q32@\"FSMachPort\"40Q48@?<v@?iQ@\"NSData\">56"
+ "v64@0:8@\"NSString\"16Q24Q32@\"FSMachPort\"40Q48@?<v@?iQ@\"NSData\"@\"NSData\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v64@0:8@16Q24Q32@40Q48@?56"
+ "v68@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32i40@\"FSAuditToken\"44Q52@?<v@?i>60"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"FSFileName\"32i40@\"FSAuditToken\"44Q52@?<v@?i@\"NSData\"@\"NSData\">60"
+ "v68@0:8@16@24@32i40@44Q52@?60"
+ "v72@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSData\"40@\"FSAuditToken\"48Q56@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">64"
+ "v72@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40@\"FSAuditToken\"48Q56@?<v@?iqQ>64"
+ "v72@0:8@16@24@32@40@48Q56@?64"
+ "v72@0:8@16@24Q32Q40@48Q56@?64"
+ "v76@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSData\"40I48@\"FSAuditToken\"52Q60@?<v@?iq@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\"@\"NSData\">68"
+ "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48i56@\"NSArray\"60@?<v@?@\"NSError\">68"
+ "v76@0:8@16@24@32@40I48@52Q60@?68"
+ "v80@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48@\"FSAuditToken\"56Q64@?<v@?iqQ>72"
+ "v80@0:8@16@24Q32Q40Q48@56Q64@?72"
+ "v92@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSString\"40@\"FSFileName\"48@\"NSString\"56I64@\"FSAuditToken\"68Q76@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">84"
+ "v92@0:8@16@24@32@40@48@56I64@68Q76@?84"
+ "v96@0:8@\"FSFileName\"16@\"FSContainerIdentifier\"24@\"NSString\"32@\"FSTaskOptionsBundle\"40{?=[8I]}48@\"FSMessageConnection\"80@?<v@?@\"NSUUID\"@\"NSError\">88"
+ "v96@0:8@\"FSVolumeIdentifier\"16@\"FSContainerIdentifier\"24@\"NSString\"32@\"FSTaskOptionsBundle\"40{?=[8I]}48@\"FSMessageConnection\"80@?<v@?@\"NSUUID\"@\"NSError\">88"
+ "v96@0:8@16@24@32@40{?=[8I]}48@80@?88"
+ "volumeDescriptions"
+ "volumeState"
+ "writeTo:atOffset:length:machPort:requestID:reply:"
+ "writeTo:atOffset:length:machPort:requestID:replyHandler:"
+ "xattrOf:named:auditToken:requestID:reply:"
+ "xattrOf:named:auditToken:requestID:replyHandler:"
+ "\xe1"
- "%s: Adding volumeID %@ to our instance"
- "%s: Can't find instance of bundleID %@ err %@"
- "%s: Given resource (%@) is not recognized by resource manager"
- "%s: sync is async"
- "%s:%@: Can't start new task, resource state is %d"
- "%s:%@: Can't start probe task, resource state is %d"
- "+[fskitdExtensionClient closeResource:andRevoke:]"
- "-[FSVolumeConnectorBridge makeDirectoryIn:named:attributes:requestID:reply:]_block_invoke"
- "-[fskitdXPCServer _deactivateVolume:usingIdentity:numericOptions:auditToken:replyHandler:]_block_invoke_5"
- "-[fskitdXPCServer _loadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke_2"
- "-[fskitdXPCServer _loadResource:usingIdentity:options:auditToken:replyHandler:]_block_invoke_5"
- "@\"FSResourceManager\""
- "T@\"FSResourceManager\",&,V_resourceManager"
- "T@\"NSMutableArray\",&,V_resourceIDs"
- "T@\"NSMutableArray\",&,V_taskIDs"
- "T@\"NSMutableArray\",&,V_volumeIDs"
- "_resourceIDs"
- "_resourceManager"
- "_volumeIDs"
- "activateVolume:resource:options:replyHandler:"
- "addResourceID:"
- "addVolumeID:"
- "checkAccessTo:requestedAccess:requestID:replyHandler:"
- "close:keepingMode:requestID:replyHandler:"
- "createIn:named:type:attributes:requestID:replyHandler:"
- "fileAttributes:requestedAttributes:requestID:replyHandler:"
- "getResource:"
- "getResourceState:"
- "getResources"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "listXattrsOf:requestID:replyHandler:"
- "lookupIn:name:flags:requestID:replyHandler:"
- "makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:"
- "makeLinkOf:named:inDirectory:requestID:replyHandler:"
- "makeSymlinkIn:named:contents:attributes:requestID:replyHandler:"
- "mount:reply:"
- "mount:replyHandler:"
- "open:withMode:requestID:replyHandler:"
- "readDirectory:intoBuffer:cookie:verifier:requestID:replyHandler:"
- "readDirectory:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:"
- "readSymbolicLinkOf:requestID:replyHandler:"
- "reclaim:requestID:replyHandler:"
- "removeDirectory:from:named:usingFlags:requestID:replyHandler:"
- "removeItem:from:named:usingFlags:requestID:replyHandler:"
- "removeResourceID:"
- "removeVolumeID:"
- "renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:"
- "resourceManager"
- "setFileAttributesOf:to:requestID:replyHandler:"
- "setOtherAttributeOf:named:value:requestID:replyHandler:"
- "setResourceIDs:"
- "setResourceManager:"
- "setVolumeIDs:"
- "setXattrOf:named:value:how:requestID:replyHandler:"
- "v32@0:8@\"FSTaskOptionsBundle\"16@?<v@?i>24"
- "v40@0:8@\"NSString\"16Q24@?<v@?i@\"NSArray\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?i@\"NSData\"@\"NSData\">32"
- "v40@?0@\"NSString\"8@\"FSResource\"16@\"NSXPCConnection\"24@?<v@?@\"FSTaskDescription\">32"
- "v44@0:8@\"NSString\"16i24Q28@?<v@?i>36"
- "v44@0:8@16i24Q28@?36"
- "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?i@\"NSData\"@\"NSData\">40"
- "v52@0:8@\"NSString\"16@\"FSFileName\"24I32Q36@?<v@?ii@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">44"
- "v52@0:8@16@24I32Q36@?44"
- "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24@\"FSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
- "v60@0:8@\"NSString\"16@\"FSFileName\"24@\"NSData\"32i40Q44@?<v@?i>52"
- "v60@0:8@\"NSString\"16@\"NSString\"24@\"FSFileName\"32i40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
- "v60@0:8@16@24@32i40Q44@?52"
- "v64@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">56"
- "v64@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
- "v64@0:8@16@24Q32Q40Q48@?56"
- "v68@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSData\"40I48Q52@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">60"
- "v68@0:8@16@24@32@40I48Q52@?60"
- "v72@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48Q56@?<v@?iqQ>64"
- "v72@0:8@16@24Q32Q40Q48Q56@?64"
- "v84@0:8@\"NSString\"16@\"FSFileName\"24@\"NSString\"32@\"NSString\"40@\"FSFileName\"48@\"NSString\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">76"
- "v84@0:8@16@24@32@40@48@56I64Q68@?76"
- "volumeIDs"
- "xattrOf:named:requestID:replyHandler:"
- "\xd1"

```
