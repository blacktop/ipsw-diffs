## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2624.100.67.0.0
-  __TEXT.__text: 0x2f814
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x3f5c
+2624.100.98.0.0
+  __TEXT.__text: 0x30884
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x4034
   __TEXT.__const: 0x590
-  __TEXT.__cstring: 0x7b33
-  __TEXT.__gcc_except_tab: 0x138c
-  __TEXT.__oslogstring: 0x2719
-  __TEXT.__unwind_info: 0x1118
-  __TEXT.__objc_classname: 0x387
-  __TEXT.__objc_methname: 0x9a0e
-  __TEXT.__objc_methtype: 0x1197
-  __TEXT.__objc_stubs: 0x4960
-  __DATA_CONST.__got: 0x390
+  __TEXT.__cstring: 0x7e0a
+  __TEXT.__gcc_except_tab: 0x13c4
+  __TEXT.__oslogstring: 0x2762
+  __TEXT.__unwind_info: 0x1148
+  __TEXT.__objc_classname: 0x397
+  __TEXT.__objc_methname: 0x9c6b
+  __TEXT.__objc_methtype: 0x11dc
+  __TEXT.__objc_stubs: 0x4b40
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x668
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c8
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_selrefs: 0x2358
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__auth_got: 0x718
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x5a60
-  __AUTH_CONST.__objc_const: 0x5128
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x5c80
+  __AUTH_CONST.__objc_const: 0x5268
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x380
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x388
   __DATA.__data: 0x308
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x150
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0xf8

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1572
-  Symbols:   1987
-  CStrings:  3132
+  Functions: 1597
+  Symbols:   2021
+  CStrings:  3183
 
Symbols:
+ _MCFeatureAccountModificationAllowed
+ _MCFeatureCloudBackupAllowed
+ _OBJC_CLASS_$_MBManagedPolicy
+ _OBJC_CLASS_$_MDMConfiguration
+ _OBJC_METACLASS_$_MBManagedPolicy
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_terminate
CStrings:
+ "%@ force disallowed by behavior option"
+ "%@ is disabled for this device in EDU mode"
+ "%@ is disabled for this device in RRTS mode"
+ "-[MBManagedPolicy _checkBehaviorOption:description:allowedOut:error:]"
+ "-[MBManagedPolicy _checkIfAnyBackupOrRestoreIsAllowed:error:]"
+ "=managed-policy= %@"
+ "=managed-policy= %@ force allowed by behavior option"
+ "@\"MBBehaviorOptions\""
+ "@\"MCProfileConnection\""
+ "AllowCloudAccountModification"
+ "AllowCloudBackup"
+ "AllowDriveBackup"
+ "AllowDriveRestore"
+ "AllowEnablingCloudBackup"
+ "B48@0:8@16@24^B32^@40"
+ "B60@0:8@16@24@32@40B48^@52"
+ "Cloud account modification"
+ "Cloud account modification is disabled by MDM"
+ "Cloud backup"
+ "Cloud backup enabling is disabled by MDM"
+ "Cloud backup is disabled by MDM"
+ "Diagnostic reporting is disabled by MDM"
+ "Drive backup"
+ "Drive restore"
+ "Enabling cloud backup"
+ "MBManagedPolicy"
+ "MBManagedPolicy.m"
+ "T@\"MBManagedPolicy\",R,N"
+ "_behaviorOptions"
+ "_checkBehaviorOption:description:allowedOut:error:"
+ "_checkIfAnyBackupOrRestoreIsAllowed:error:"
+ "_profileConnection"
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
+ "effectiveBoolValueForSetting:"
+ "isDiagnosticSubmissionAllowed"
+ "isRapidReturnToService"
+ "isSettingLockedDownByRestrictions:"
+ "restoreDomain:deviceUUID:snapshotUUID:intoPath:verified:error:"
+ "sharedPolicy"
- "B56@0:8@16@24@32@40^@48"
- "restoreDomain:deviceUUID:snapshotUUID:intoPath:error:"

```
