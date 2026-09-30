## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0x14b94
+2624.100.98.0.0
+  __TEXT.__text: 0x153b8
   __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x2540
-  __TEXT.__objc_methlist: 0xa70
-  __TEXT.__const: 0x420
-  __TEXT.__cstring: 0x3a05
-  __TEXT.__objc_methname: 0x2d0f
-  __TEXT.__objc_classname: 0x118
-  __TEXT.__objc_methtype: 0x5c5
-  __TEXT.__oslogstring: 0x261d
-  __TEXT.__gcc_except_tab: 0x38c
+  __TEXT.__objc_stubs: 0x26e0
+  __TEXT.__objc_methlist: 0xd0c
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0x3b95
+  __TEXT.__objc_methname: 0x2f27
+  __TEXT.__objc_classname: 0x128
+  __TEXT.__objc_methtype: 0x61f
+  __TEXT.__oslogstring: 0x2547
+  __TEXT.__gcc_except_tab: 0x2a0
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0xe4
   __TEXT.__swift5_reflstr: 0x8c

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__unwind_info: 0x480
   __TEXT.__eh_frame: 0x158
   __DATA_CONST.__auth_got: 0x678
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x828
-  __DATA_CONST.__cfstring: 0xe40
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__const: 0x820
+  __DATA_CONST.__cfstring: 0xfc0
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x16d8
-  __DATA.__objc_selrefs: 0xb78
-  __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0x510
+  __DATA.__objc_const: 0x1420
+  __DATA.__objc_selrefs: 0xd00
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_data: 0x560
   __DATA.__data: 0x360
-  __DATA.__bss: 0x5f0
+  __DATA.__bss: 0x600
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 368
-  Symbols:   299
-  CStrings:  1121
+  Functions: 389
+  Symbols:   310
+  CStrings:  1157
 
Symbols:
+ _IXStringForClientID
+ _MCFeatureAccountModificationAllowed
+ _MCFeatureCloudBackupAllowed
+ _OBJC_CLASS_$_IXApplicationIdentity
+ _OBJC_CLASS_$_MBBehaviorOptions
+ _OBJC_CLASS_$_MBManagedPolicy
+ _OBJC_CLASS_$_MDMConfiguration
+ _OBJC_METACLASS_$_MBManagedPolicy
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _MBGroupWaitForever
- _OBJC_CLASS_$_MDMClient
- _OBJC_CLASS_$_UMUserManager
CStrings:
+ "%@ force disallowed by behavior option"
+ "%@ is disabled for this device in EDU mode"
+ "%@ is disabled for this device in RRTS mode"
+ "-[MBManagedPolicy _checkBehaviorOption:description:allowedOut:error:]"
+ "-[MBManagedPolicy _checkIfAnyBackupOrRestoreIsAllowed:error:]"
+ "-[RestorePostProcess _createInstallCoordinatorForPlaceholderAtPath:bundleID:personaIdentifier:isDataSeparated:installType:error:]"
+ "-[RestorePostProcess _installCoordinatorForPlaceholder:bundleID:installType:personaIdentifier:isDataSeparated:error:]"
+ "=managed-policy= %@"
+ "=managed-policy= %@ force allowed by behavior option"
+ "@\"MBBehaviorOptions\""
+ "@\"MCProfileConnection\""
+ "@60@0:8@16@24Q32@40B48^@52"
+ "Account is marked as managed %@"
+ "B24@0:8^@16"
+ "B48@0:8@16@24^B32^@40"
+ "B52@0:8@16@24B32Q36@44"
+ "B60@0:8@16@24@32B40Q44^@52"
+ "Cloud account modification"
+ "Cloud account modification is disabled by MDM"
+ "Cloud backup"
+ "Cloud backup enabling is disabled by MDM"
+ "Cloud backup is disabled by MDM"
+ "Diagnostic reporting is disabled by MDM"
+ "Done configuring %lu/%lu placeholders for %@. Waiting for them to get installed"
+ "Drive backup"
+ "Drive restore"
+ "Enabling cloud backup"
+ "Finished installing app placeholders for persona %@ in %.3fs"
+ "IX: -coordinator:canceledWithReason:client: called with nil bundleID (%@)"
+ "IX: -coordinator:canceledWithReason:client: called with nil coordinator (%@)"
+ "IX: Configured the placeholder for %@(persona %@) at %@: %@"
+ "IX: Created the install coordinator for %@(persona %@) at %@: %@"
+ "IX: Setting app asset DRI for %@(persona %@) as %@"
+ "Installing %lu app placeholders for persona %@"
+ "MBManagedPolicy"
+ "MBManagedPolicy.m"
+ "Not changing the \"%{public}@\" state on account %{public}@: %@"
+ "T@\"MBManagedPolicy\",R,N"
+ "_behaviorOptions"
+ "_checkBehaviorOption:description:allowedOut:error:"
+ "_checkIfAnyBackupOrRestoreIsAllowed:error:"
+ "_configurePlaceholderIPA:personaIdentifier:isDataSeparated:installType:migratorCache:"
+ "_createInstallCoordinatorForPlaceholderAtPath:bundleID:personaIdentifier:isDataSeparated:installType:error:"
+ "_init"
+ "_installCoordinatorForPlaceholder:bundleID:installType:personaIdentifier:isDataSeparated:error:"
+ "_installTypeForBundleID:demotedAppsPlist:"
+ "_profileConnection"
+ "_registerPlaceholdersForBackgroundRestore:personaIdentifier:isDataSeparated:migratorCache:demotedAppsPlist:"
+ "allowCloudAccountModification"
+ "allowCloudBackup"
+ "allowDriveBackup"
+ "allowDriveRestore"
+ "allowEnablingCloudBackup"
+ "allowedOut"
+ "checkIfCloudAccountModificationIsAllowed:"
+ "checkIfCloudBackupIsAllowed:"
+ "checkIfDiagnosticTelemetryIsAllowed:"
+ "checkIfDriveBackupIsAllowed:"
+ "checkIfDriveRestoreIsAllowed:"
+ "checkIfEnablingCloudBackupIsAllowed:"
+ "coordinatorForAppWithIdentity:withClientID:createIfNotExisting:created:error:"
+ "effectiveBoolValueForSetting:"
+ "identity"
+ "initWithBundleIdentifier:personaUniqueString:"
+ "isDiagnosticSubmissionAllowed"
+ "isRapidReturnToService"
+ "isSettingLockedDownByRestrictions:"
+ "personaID"
+ "sharedOptions"
+ "sharedPolicy"
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
- "Not changing the \"%{public}@\" state on account %{public}@ since the device is in EDU mode"
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
