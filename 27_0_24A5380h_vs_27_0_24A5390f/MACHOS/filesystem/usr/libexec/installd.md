## installd

> `/usr/libexec/installd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_fieldmd`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1663.0.0.0.1
-  __TEXT.__text: 0x6da34
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_stubs: 0x8dc0
-  __TEXT.__objc_methlist: 0x3774
+1673.0.0.0.0
+  __TEXT.__text: 0x70f48
+  __TEXT.__auth_stubs: 0x1760
+  __TEXT.__objc_stubs: 0x8fe0
+  __TEXT.__objc_methlist: 0x390c
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x18303
-  __TEXT.__objc_classname: 0x64f
-  __TEXT.__objc_methtype: 0x2375
-  __TEXT.__objc_methname: 0xd133
-  __TEXT.__gcc_except_tab: 0x3b64
-  __TEXT.__oslogstring: 0x14a7
+  __TEXT.__cstring: 0x18723
+  __TEXT.__objc_classname: 0x69f
+  __TEXT.__objc_methtype: 0x2405
+  __TEXT.__objc_methname: 0xd567
+  __TEXT.__gcc_except_tab: 0x3c00
+  __TEXT.__oslogstring: 0x14e7
   __TEXT.__ustring: 0x84
-  __TEXT.__swift5_typeref: 0xd2
-  __TEXT.__constg_swiftt: 0x54
+  __TEXT.__swift5_typeref: 0xe6
+  __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_capture: 0xa8
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1430
-  __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__const: 0x16d0
-  __DATA_CONST.__cfstring: 0xa520
-  __DATA_CONST.__objc_classlist: 0x150
-  __DATA_CONST.__objc_catlist: 0x8
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__swift5_capture: 0x80
+  __TEXT.__unwind_info: 0x14f8
+  __TEXT.__eh_frame: 0x218
+  __DATA_CONST.__const: 0x1638
+  __DATA_CONST.__cfstring: 0xa620
+  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30

   __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x670
   __DATA_CONST.__objc_dictobj: 0x1018
-  __DATA_CONST.__auth_got: 0xb80
+  __DATA_CONST.__auth_got: 0xbc0
   __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__objc_const: 0x6138
-  __DATA.__objc_selrefs: 0x2840
+  __DATA.__objc_const: 0x6348
+  __DATA.__objc_selrefs: 0x28d8
   __DATA.__objc_ivar: 0x2a4
-  __DATA.__objc_data: 0xd60
-  __DATA.__data: 0xb90
-  __DATA.__bss: 0x1e0
+  __DATA.__objc_data: 0xe40
+  __DATA.__data: 0xbf8
+  __DATA.__bss: 0x1f0
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1534
-  Symbols:   532
-  CStrings:  3869
+  Functions: 1593
+  Symbols:   538
+  CStrings:  3915
 
Symbols:
+ _$sSa10FoundationE19_bridgeToObjectiveCSo7NSArrayCyF
+ _$sSa10FoundationE36_unconditionallyBridgeFromObjectiveCySayxGSo7NSArrayCSgFZ
+ _$sSh10FoundationE36_unconditionallyBridgeFromObjectiveCyShyxGSo5NSSetCSgFZ
+ _$sSh11descriptionSSvg
+ _$sSh9hashValueSivg
+ _$sSo17OS_dispatch_queueC8DispatchE4sync7executexxyKXE_tKlF
+ _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
+ _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
+ _$ss18_CocoaArrayWrapperV8endIndexSivg
+ _$sytN
+ _sandbox_extension_release
+ _swift_initStackObject
+ _swift_setDeallocating
- _$sBi64_WV
- _$ss5ErrorWS
- _$ss6ResultOMn
- _swift_errorRetain
- _swift_getForeignTypeMetadata
- _swift_release_x27
- _swift_willThrowTypedImpl
CStrings:
+ "%s: Failed to release sandbox token %lld for %@ : %s"
+ "+[MIPersonaAssociationManager _replacePersona:withPersona:inExistingPersonaSet:forApp:defaultPersona:personasChanged:error:]"
+ "-[MIPersonaAssociationManager _addPersona:toApp:inDomain:ignoreUninstalledApp:lsPersonaUpdate:error:]"
+ "-[MIPersonaAssociationManager _setPersonas:forApp:inDomain:saveMapping:tellLS:lsPersonaUpdate:error:]"
+ "-[MIPersonaAssociationManager removePersona:fromApp:inDomain:lsPersonaUpdate:error:]"
+ "-[MIPersonaAssociationManager replaceAssociatedPersona:withPersona:forApp:inDomain:lsPersonaUpdate:error:]"
+ "-[MIUserManagement(DaemonUtilities) daemonContainerForPersonaUniqueString:personaVolumeMount:personaVolumeUUID:extensionTokenHandle:error:]"
+ "@56@0:8@16@24^@32^q40^@48"
+ "@56@0:8@16Q24@32Q40^@48"
+ "@72@0:8@16@24@32@40@48^B56^@64"
+ "Attempt to replace persona %@ on %@ but that persona is not currently associated"
+ "B16@?0@\"<MIBundleMetadataProvider>\"8"
+ "B32@?0@\"<MIBundleMetadataProvider>\"8@\"MIBundleMetadata\"16@\"NSSet\"24"
+ "B56@0:8@16@24Q32^@40^@48"
+ "B60@0:8@16@24Q32B40^@44^@52"
+ "B64@0:8@16@24@32Q40^@48^@56"
+ "B64@0:8@16@24Q32B40B44^@48^@56"
+ "DaemonUtilities"
+ "Failed to determine volume UUID for daemon container for persona %@ at %@"
+ "Failed to determine volume UUID for persona volume mount %@"
+ "Failed to get daemon container URL from %@"
+ "Failed to get daemon container for persona %@"
+ "Failed to get sandbox extension for daemon container for persona %@ at %@"
+ "Failed to release sandbox token %lld for %@ : %s"
+ "Got daemon container at %@ for data separated persona %@ that was not on persona mount %@"
+ "MILSPersonaUpdateOperation"
+ "MIPendingLSPersonaUpdate"
+ "T#,R,N"
+ "T@\"NSArray\",N,R"
+ "T@\"NSSet\",N,R"
+ "TB,N"
+ "TQ,N,R,Vdomain"
+ "__ObjC.MILSPersonaUpdateOperation"
+ "__ObjC.MIPendingLSPersonaUpdate"
+ "_addPersona:toApp:inDomain:ignoreUninstalledApp:lsPersonaUpdate:error:"
+ "_makeLSPersonaUpdateOperationWithPendingUpdates:"
+ "_onQueue_replaceAssociatedPersona:withPersona:forBuiltInApp:personasChanged:error:"
+ "_replaceAssociatedPersona:withPersona:forAppInBundleContainer:personasChanged:error:"
+ "_replacePersona:withPersona:inExistingPersonaSet:forApp:defaultPersona:personasChanged:error:"
+ "_setPersonas:forApp:inDomain:saveMapping:tellLS:lsPersonaUpdate:error:"
+ "_userManagement"
+ "addPersona:toApp:inDomain:lsPersonaUpdate:error:"
+ "applyWithError:"
+ "bundleMetadataProviderClass"
+ "daemonContainerForPersona:error:"
+ "daemonContainerForPersonaUniqueString:personaVolumeMount:personaVolumeUUID:extensionTokenHandle:error:"
+ "enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBundleMetadataProviderBlock:"
+ "initWithPendingUpdate:"
+ "initWithPendingUpdates:"
+ "initWithPersona:bundleID:domain:"
+ "initWithPersona:bundleIDs:domain:"
+ "initWithPersonas:bundleID:domain:"
+ "initWithPersonas:bundleIDs:domain:"
+ "onLSRegistrationQueueApplyWithError:"
+ "pendingUpdates"
+ "removePersona:fromApp:inDomain:lsPersonaUpdate:error:"
+ "replaceAssociatedPersona:withPersona:forApp:inDomain:lsPersonaUpdate:error:"
+ "setPersonas:forApp:inDomain:lsPersonaUpdate:error:"
+ "transferOwnershipOfSandboxExtensionToCaller"
+ "volumeUUIDForURL:error:"
- "-[MIPersonaAssociationManager _addPersona:toApp:inDomain:ignoreUninstalledApp:error:]"
- "-[MIPersonaAssociationManager _setPersonas:forApp:inDomain:saveMapping:tellLS:error:]"
- "-[MIPersonaAssociationManager removePersona:fromApp:inDomain:error:]"
- "B32@?0@\"MIBundleContainer\"8@\"MIBundleMetadata\"16@\"NSSet\"24"
- "B52@0:8@16@24Q32B40^@44"
- "B56@0:8@16@24Q32B40B44^@48"
- "B56@0:8@16Q24@32Q40^@48"
- "_addPersona:toApp:inDomain:ignoreUninstalledApp:error:"
- "_setPersona:viaLaunchServicesForApps:inDomain:error:"
- "_setPersonas:forApp:inDomain:saveMapping:tellLS:error:"
- "_setPersonas:viaLaunchServicesForApp:inDomain:error:"
- "addPersona:toApp:inDomain:error:"
- "removePersona:fromApp:inDomain:error:"
- "setPersonas:forApp:inDomain:error:"
```
