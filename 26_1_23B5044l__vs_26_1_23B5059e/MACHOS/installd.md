## installd

> `/usr/libexec/installd`

```diff

-1513.40.8.0.0
-  __TEXT.__text: 0x56f84
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_stubs: 0x7ac0
-  __TEXT.__objc_methlist: 0x2fac
+1513.40.11.502.1
+  __TEXT.__text: 0x588b8
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0x7bc0
+  __TEXT.__objc_methlist: 0x304c
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x14981
-  __TEXT.__objc_classname: 0x5cf
-  __TEXT.__objc_methname: 0xb09b
-  __TEXT.__objc_methtype: 0x1e5e
-  __TEXT.__gcc_except_tab: 0x2f58
-  __TEXT.__oslogstring: 0x11f3
+  __TEXT.__cstring: 0x14df4
+  __TEXT.__objc_classname: 0x5cd
+  __TEXT.__objc_methname: 0xb377
+  __TEXT.__objc_methtype: 0x1eb0
+  __TEXT.__gcc_except_tab: 0x310c
+  __TEXT.__oslogstring: 0x11ac
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0xf48
-  __DATA_CONST.__auth_got: 0x7d0
-  __DATA_CONST.__got: 0x358
+  __TEXT.__unwind_info: 0xf98
+  __DATA_CONST.__auth_got: 0x7f0
+  __DATA_CONST.__got: 0x350
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xf48
-  __DATA_CONST.__cfstring: 0x93c0
+  __DATA_CONST.__const: 0x10b0
+  __DATA_CONST.__cfstring: 0x95c0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x5a0
-  __DATA_CONST.__objc_dictobj: 0xe10
-  __DATA.__objc_const: 0x5938
-  __DATA.__objc_selrefs: 0x2318
-  __DATA.__objc_ivar: 0x27c
+  __DATA_CONST.__objc_arraydata: 0x5d0
+  __DATA_CONST.__objc_dictobj: 0xe88
+  __DATA.__objc_const: 0x59c0
+  __DATA.__objc_selrefs: 0x2368
+  __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0xa18
   __DATA.__bss: 0x188

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4D7C6CD-8AE5-31CA-9EAB-E287E05A1E08
-  Functions: 1181
-  Symbols:   369
-  CStrings:  4613
+  UUID: EBDBB52A-64F7-31FE-A98C-3E588686E1D4
+  Functions: 1199
+  Symbols:   372
+  CStrings:  4666
 
Symbols:
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
- _OBJC_CLASS_$_ICLBundleRecord
CStrings:
+ "%@ key was not set in storage plist or was not an array of strings; found: %@"
+ "-[MIClientConnection reconcileContentsOnKnownOSModules:completion:]"
+ "-[MIClientConnection registerContentsOnOSModuleAtURL:completion:]"
+ "-[MIClientConnection unregisterContentsOnOSModuleAtURL:completion:]"
+ "-[MIDiskImageManager _initializeInfoFromStorageAtURL:expectingDictKey:]"
+ "-[MIDiskImageManager _onQueue_infoForEntityType:]"
+ "-[MIDiskImageManager _onQueue_registerContentsOnAttachedEntityAtURL:ofType:completion:]"
+ "-[MIDiskImageManager _onQueue_saveInfo:withTopLevelKey:atURL:]"
+ "-[MIDiskImageManager _onQueue_scanApps:returnMapInfo:error:]"
+ "-[MIDiskImageManager _onQueue_scanApps:returnMapInfo:error:]_block_invoke"
+ "-[MIDiskImageManager _onQueue_unregisterContentsOnDiskImageAtMountPoint:completion:]_block_invoke"
+ "-[MIDiskImageManager _onQueue_unregisterContentsOnOSModuleAtURL:withBundleIDs:completion:]_block_invoke"
+ "-[MIDiskImageManager unregisterContentsOnAttachedEntityAtURL:ofType:completion:]_block_invoke"
+ "B32@0:8@16Q24"
+ "B32@0:8Q16@24"
+ "DiskImage"
+ "Failed to fetch cached info for installed apps on module at %@"
+ "Failed to purge journal entry after failure to apply staged update %@ : %@"
+ "Failed to read %@: %@"
+ "Failed to scan apps on %@"
+ "Finalizing staged update identifier \"%@\" type %@ (LSInstallType = %lu, Domain: %@) requested by %@"
+ "Found unknown entity type %lu"
+ "Install successful for (%@:%@) [Distributor: %@]; Staging: %.2fs; Waiting: %.2fs; Preflight/Patch: %.2fs, Verifying: %.2fs; Overall: %.2fs"
+ "LS failed to unregister app %@ : %@"
+ "LS unregistered app %@"
+ "List of known OS modules was not a set."
+ "Made staged update live for (%@:%@) [Distributor: %@]; Overall: %.2fs"
+ "OS module path for registering contents was not a URL."
+ "OS module path for unregistering content was not a URL."
+ "OSModule"
+ "OSModulePaths"
+ "OSModulePaths.plist"
+ "Process %@ tried to register os module, but registration can only be done by InstallCoordination."
+ "Process %@ tried to set known os modules, but that operation can only be done by InstallCoordination."
+ "Process %@ tried to unregister os module, but unregistration can only be done by InstallCoordination."
+ "Registering applications on %@: %@"
+ "Retaining staged update container: %@"
+ "Staging %@"
+ "Staging update successful for (%@:%@) [Distributor: %@]; Staging: %.2fs; Waiting: %.2fs; Preflight/Patch: %.2fs, Verifying: %.2fs => %@"
+ "Successfully cleaned up temp %s container for %@"
+ "T@\"NSMutableDictionary\",&,N,V_osModuleInfo"
+ "T@\"NSString\",&,N,V_pendingPath"
+ "URLIsOnAttachedEntityType:at:"
+ "Unexpectedly found unknown MIAttachedEntityTypeUnknown"
+ "Unknown MIAttachedEntityType %lu"
+ "_addPath:toEntityType:withInfo:"
+ "_clearPendingPath"
+ "_initializeInfoFromStorage"
+ "_initializeInfoFromStorageAtURL:expectingDictKey:"
+ "_onQueue_infoForEntityType:"
+ "_onQueue_registerContentsOnAttachedEntityAtURL:ofType:completion:"
+ "_onQueue_resetDiskImagePaths"
+ "_onQueue_resetOSModulePaths"
+ "_onQueue_saveInfo:withTopLevelKey:atURL:"
+ "_onQueue_scanApps:returnMapInfo:error:"
+ "_onQueue_unregisterContentsOnDiskImageAtMountPoint:completion:"
+ "_onQueue_unregisterContentsOnOSModuleAtURL:withBundleIDs:completion:"
+ "_osModuleInfo"
+ "_pendingPath"
+ "_removePath:fromEntityType:"
+ "_setPendingPath:"
+ "appBundleIDsOnAttachedEntityType:"
+ "appInfoForBundleID:onAttachedEntityType:"
+ "attachedContentPathsForEntityType:"
+ "bundleID:isOnAttachedEntityType:"
+ "com.apple.installd.unregister-content-osmodule"
+ "fileURLWithPath:isDirectory:relativeToURL:"
+ "markContainerAsStagedUpdateWithError:"
+ "osModuleInfo"
+ "pendingPath"
+ "preconditionCheckingRelationshipToURL:ofBundleWithIdentifier:placeholderFetchBehavior:requiredRelationship:"
+ "reconcileContentsOnKnownOSModules:completion:"
+ "registerContainerizedApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerContentsOnAttachedEntityAtURL:ofType:completion:"
+ "registerContentsOnOSModuleAtURL:completion:"
+ "setOsModuleInfo:"
+ "setPendingPath:"
+ "stageUpdateForLaterWithError:"
+ "unregisterContentsOnAttachedEntityAtURL:ofType:completion:"
+ "unregisterContentsOnOSModuleAtURL:completion:"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@16@24@32"
- "%s: Failed to push persona unique strings for %@ to LaunchServices: %@"
- "-[MIDiskImageManager _initializeMountInfoFromStorage]"
- "-[MIDiskImageManager _onQueue_saveMountPaths]"
- "-[MIDiskImageManager _onQueue_scanApps:returnMapInfo:]"
- "-[MIDiskImageManager _onQueue_scanApps:returnMapInfo:]_block_invoke"
- "-[MIDiskImageManager registerContentsAtMountPoint:completion:]_block_invoke"
- "-[MIDiskImageManager unregisterContentsAtMountPoint:completion:]_block_invoke"
- "-[MIDiskImageManager unregisterContentsAtMountPoint:completion:]_block_invoke_2"
- "Applying Staged Update Successful for (%@:%@) [Distributor: %@]; Overall: %.2fs"
- "Encountered error while enumerating %@ : %@"
- "Failed to purge journal entry after staging update failure %@ : %@"
- "Failed to push persona unique strings for %@ to LaunchServices: %@"
- "Failed to read %@ : %@"
- "Install Successful for (%@:%@) [Distributor: %@]; Staging: %.2fs; Waiting: %.2fs; Preflight/Patch: %.2fs, Verifying: %.2fs; Overall: %.2fs"
- "Installing staged update of \"%@\" type %@ (LSInstallType = %lu, Domain: %@) requested by %@"
- "Making staged update live for \"%@\" requested by %@"
- "Mount paths key was not set in storage plist or was not an array of strings; found: %@"
- "Not freeing temp container because it is staged: %@"
- "Registering applications at mount point: %@"
- "Staging Update Phase Successful for (%@:%@) [Distributor: %@]; Staging: %.2fs; Waiting: %.2fs; Preflight/Patch: %.2fs, Verifying: %.2fs"
- "T@\"NSString\",&,N,V_pendingMountPath"
- "URLIsOnKnownImageMount:"
- "_addMountPath:withInfo:"
- "_clearPendingMountPath"
- "_initializeMountInfoFromStorage"
- "_mountInfoForPath:"
- "_onQueue_configureMountInfoForPaths:"
- "_onQueue_saveMountPaths"
- "_onQueue_scanApps:returnMapInfo:"
- "_pendingMountPath"
- "_removeMountPath:"
- "_setPendingMountPath:"
- "bundleIDIsOnKnownImageMount:"
- "bundleRecordArrayToInfoDictionaryArray:"
- "diskImageAppBundleIDs"
- "diskImageAppInfoForBundleID:"
- "diskMountPaths"
- "markContainerAsStagedUpdateContainer:"
- "pendingMountPath"
- "registerContainerizedApplicationWithInfoDictionaries:operationUUID:requestContext:saveObserver:registrationError:"
- "registerContentsAtMountPoint:completion:"
- "setPendingMountPath:"
- "stageUpdateForLater:"
- "stringByAppendingPathComponent:"
- "unregisterContentsAtMountPoint:completion:"

```
