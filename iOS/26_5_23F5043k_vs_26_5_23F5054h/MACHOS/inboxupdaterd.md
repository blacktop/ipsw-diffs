## inboxupdaterd

> `filesystem/usr/libexec/inboxupdaterd`

```diff

-176.120.8.0.0
-  __TEXT.__text: 0x7c994
-  __TEXT.__auth_stubs: 0x1330
-  __TEXT.__objc_stubs: 0x7360
-  __TEXT.__objc_methlist: 0x3728
-  __TEXT.__cstring: 0x4531
-  __TEXT.__objc_methname: 0x7509
-  __TEXT.__objc_classname: 0x593
-  __TEXT.__objc_methtype: 0x1382
+176.120.15.0.0
+  __TEXT.__text: 0x7e6d8
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_stubs: 0x74c0
+  __TEXT.__objc_methlist: 0x37e4
+  __TEXT.__cstring: 0x45cc
+  __TEXT.__objc_methname: 0x773d
+  __TEXT.__objc_classname: 0x5bf
+  __TEXT.__objc_methtype: 0x13c6
   __TEXT.__const: 0x6f98
-  __TEXT.__oslogstring: 0x8531
-  __TEXT.__gcc_except_tab: 0x187c
+  __TEXT.__oslogstring: 0x87a2
+  __TEXT.__gcc_except_tab: 0x1908
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1e78
-  __DATA_CONST.__auth_got: 0x9a8
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__unwind_info: 0x1ef8
+  __DATA_CONST.__auth_got: 0x9b0
+  __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xcdc8
-  __DATA_CONST.__cfstring: 0x3c40
+  __DATA_CONST.__const: 0xd010
+  __DATA_CONST.__cfstring: 0x3d40
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_intobj: 0x18f0
-  __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__objc_arrayobj: 0x588
+  __DATA_CONST.__objc_intobj: 0x19c8
+  __DATA_CONST.__objc_arraydata: 0x4b8
+  __DATA_CONST.__objc_arrayobj: 0x5d0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8248
-  __DATA.__objc_selrefs: 0x2150
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_const: 0x82c8
+  __DATA.__objc_selrefs: 0x21d0
+  __DATA.__objc_ivar: 0x398
   __DATA.__objc_data: 0xd20
-  __DATA.__data: 0x1ce0
+  __DATA.__data: 0x1d40
   __DATA.__bss: 0x138
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 237C7041-ED5A-3CD9-8BD3-8ADE60D97A67
-  Functions: 3559
-  Symbols:   441
-  CStrings:  3658
+  UUID: 2E2AE7A7-AE09-36DF-8AC6-190FBCBABD9D
+  Functions: 3605
+  Symbols:   443
+  CStrings:  3710
 
Symbols:
+ _DMPerformMigrationIfNeeded
+ _OBJC_CLASS_$_SBSHomeScreenService
CStrings:
+ "%{public}@: Failed to request Tatsu ticket before timeout: %lu"
+ "%{public}@: Requesting personalization ticket..."
+ ">> %{public}@"
+ "@40@0:8@16Q24^@32"
+ "Asset files extracted:"
+ "Data migration is done!"
+ "EnableLPMSU"
+ "Failed to create observer for home screen layout availability."
+ "Failed to deserialize shutdown command"
+ "Failed to request Tatsu ticket before timeout: %lu"
+ "Handling shutdown command with payload: %{public}@"
+ "Handling start SS update command with payload: %{public}@"
+ "Idle timer fired with user info: %{public}@"
+ "Operation is successful! Will shutdown: %{bool}d; With timeout: %f"
+ "PostUpdateTimeout"
+ "Received home screen layout availabilty changed callback!"
+ "SBSHomeScreenServiceLayoutAvailableObserver"
+ "Shutdown command completed successfully!"
+ "ShutdownDelay"
+ "SpringBoard readiness after wait: %{bool}d"
+ "SpringBoardReadinessTimeout"
+ "T@\"NSCondition\",&,N,V_springBoardReadyCondition"
+ "T@\"NSNumber\",&,N,V_postUpdateTimeout"
+ "Timed out in state %d, shutting down device (no longer wakeable)."
+ "Timed out waiting for SpringBoard to become ready."
+ "Waiting for SpringBoard to become ready with timeout: %{public}@"
+ "Waiting for data migration to finish..."
+ "_deserializeShutdown"
+ "_handleShutdown:"
+ "_postUpdateTimeout"
+ "_serializeShutdown"
+ "_springBoardReadyCondition"
+ "_startIdleTimerForState:forShutdown:withTimeout:"
+ "addHomeScreenLayoutAvailabilityObserver:"
+ "enumeratorAtPath:"
+ "homeScreenServiceLayoutAvailabilityDidChange:"
+ "isHomeScreenLayoutAvailable"
+ "nextObject"
+ "postUpdateTimeout"
+ "requestTatsuTicketForDevice:withTimeout:error:"
+ "setPostUpdateTimeout:"
+ "setSpringBoardReadyCondition:"
+ "springBoardReadyCondition"
+ "v24@0:8@\"SBSHomeScreenService\"16"
+ "v36@0:8Q16B24d28"
+ "waitForDataMigration"
+ "waitForSpringBoard"
- "%{public}@: Requesting personalization ticket ..."
- "An error happened while setting up asset file"
- "Failed to put device to LPM mode."
- "Handling start SS update command..."
- "Operation is successful."
- "Shutting down device (no longer wakeable)."

```
