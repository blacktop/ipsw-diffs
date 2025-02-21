## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0x14b94
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x2540
-  __TEXT.__objc_methlist: 0xa70
-  __TEXT.__const: 0x420
-  __TEXT.__cstring: 0x3a05
-  __TEXT.__objc_methname: 0x2d0f
+2624.100.67.0.0
+  __TEXT.__text: 0x14544
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_stubs: 0x24e0
+  __TEXT.__objc_methlist: 0xc74
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0x3955
+  __TEXT.__objc_methname: 0x2cbf
   __TEXT.__objc_classname: 0x118
-  __TEXT.__objc_methtype: 0x5c5
-  __TEXT.__oslogstring: 0x261d
-  __TEXT.__gcc_except_tab: 0x38c
+  __TEXT.__objc_methtype: 0x5d1
+  __TEXT.__oslogstring: 0x251a
+  __TEXT.__gcc_except_tab: 0x2a0
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0xe4
   __TEXT.__swift5_reflstr: 0x8c

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__unwind_info: 0x468
   __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x678
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__const: 0x800
   __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x16d8
-  __DATA.__objc_selrefs: 0xb78
+  __DATA.__objc_const: 0x1330
+  __DATA.__objc_selrefs: 0xc60
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x510
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 368
-  Symbols:   299
-  CStrings:  1121
+  Functions: 372
+  Symbols:   303
+  CStrings:  1109
 
Symbols:
+ _IXStringForClientID
+ _OBJC_CLASS_$_IXApplicationIdentity
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _MBGroupWaitForever
- _OBJC_CLASS_$_MDMClient
- _OBJC_CLASS_$_UMUserManager
- _objc_opt_respondsToSelector
CStrings:
+ "-[RestorePostProcess _createInstallCoordinatorForPlaceholderAtPath:bundleID:personaIdentifier:isDataSeparated:installType:error:]"
+ "-[RestorePostProcess _installCoordinatorForPlaceholder:bundleID:installType:personaIdentifier:isDataSeparated:error:]"
+ "@60@0:8@16@24Q32@40B48^@52"
+ "Account is marked as managed %@"
+ "B52@0:8@16@24B32Q36@44"
+ "B60@0:8@16@24@32B40Q44^@52"
+ "Done configuring %lu/%lu placeholders for %@. Waiting for them to get installed"
+ "Finished installing app placeholders for persona %@ in %.3fs"
+ "IX: -coordinator:canceledWithReason:client: called with nil bundleID (%@)"
+ "IX: -coordinator:canceledWithReason:client: called with nil coordinator (%@)"
+ "IX: Configured the placeholder for %@(persona %@) at %@: %@"
+ "IX: Created the install coordinator for %@(persona %@) at %@: %@"
+ "IX: Setting app asset DRI for %@(persona %@) as %@"
+ "Installing %lu app placeholders for persona %@"
+ "_configurePlaceholderIPA:personaIdentifier:isDataSeparated:installType:migratorCache:"
+ "_createInstallCoordinatorForPlaceholderAtPath:bundleID:personaIdentifier:isDataSeparated:installType:error:"
+ "_installCoordinatorForPlaceholder:bundleID:installType:personaIdentifier:isDataSeparated:error:"
+ "_installTypeForBundleID:demotedAppsPlist:"
+ "_registerPlaceholdersForBackgroundRestore:personaIdentifier:isDataSeparated:migratorCache:demotedAppsPlist:"
+ "coordinatorForAppWithIdentity:withClientID:createIfNotExisting:created:error:"
+ "identity"
+ "initWithBundleIdentifier:personaUniqueString:"
+ "personaID"
+ "v52@0:8@16@24B32@36@44"
- "-[RestorePostProcess _installCoordinatorForPlaceholder:bundleID:installType:isDataSeparated:error:]"
- "-[RestorePostProcess _updateBundleIDsToPersonaIDMappingWithConfig:error:]"
- "@52@0:8@16@24Q32B40^@44"
- "B44@0:8@16Q24B32@36"
- "B52@0:8@16@24Q32B40^@44"
- "Done configuring %lu/%lu placeholders. Waiting for them to get installed"
- "Failed to update the bundle ID to persona ID mapping for persona %{public}@: %@"
- "Finished installing app placeholders in %.3fs"
- "Found %ld placeholders at %{public}@"
- "IX: -coordinator:canceledWithReason:client: called with nil bundleID (%lu)"
- "IX: -coordinator:canceledWithReason:client: called with nil coordinator (%lu)"
- "IX: Configured the placeholder for %@ at %@: %@"
- "IX: Created the install coordinator for %@ at %@: %@"
- "IX: Setting app asset DRI for %@ (%lu)"
- "Installing %lu app placeholders"
- "No directory found at %{public}@"
- "Not updating bundleID to personaID mapping because it was already set by MDM"
- "Updated the bundle ID to persona ID mapping for persona %{public}@"
- "Updating the bundle ID to persona ID mapping persona %{public}@: %@"
- "_configureAndIXInstallPlaceholdersInDirectory:isDataSeparated:migratorCache:demotedAppsPlist:"
- "_configureAppPlaceholderAtPath:installType:isDataSeparated:migratorCache:"
- "_createInstallCoordinatorForPlaceholderAtPath:bundleID:installType:isDataSeparated:error:"
- "_installCoordinatorForPlaceholder:bundleID:installType:isDataSeparated:error:"
- "_updateBundleIDsToPersonaIDMappingWithConfig:error:"
- "coordinatorForAppWithBundleID:withClientID:createIfNotExisting:created:error:"
- "hasSetPersonaMappingForRestore"
- "installTypeForBundleID:demotedAppsPlist:"
- "isNSFileNotFoundError:"
- "setBundlesIdentifiers:forPersonaWithPersonaUniqueString:completionHandler:"
- "sharedClient"
- "sharedManager"
- "v44@0:8@16B24@28@36"

```
