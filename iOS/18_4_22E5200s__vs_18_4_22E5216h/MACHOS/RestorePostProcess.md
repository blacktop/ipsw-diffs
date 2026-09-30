## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2624.100.67.0.0
-  __TEXT.__text: 0x14544
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0xc74
+2624.100.98.0.0
+  __TEXT.__text: 0x153b8
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x26e0
+  __TEXT.__objc_methlist: 0xd0c
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x3955
-  __TEXT.__objc_methname: 0x2cbf
-  __TEXT.__objc_classname: 0x118
-  __TEXT.__objc_methtype: 0x5d1
-  __TEXT.__oslogstring: 0x251a
+  __TEXT.__cstring: 0x3b95
+  __TEXT.__objc_methname: 0x2f27
+  __TEXT.__objc_classname: 0x128
+  __TEXT.__objc_methtype: 0x61f
+  __TEXT.__oslogstring: 0x2547
   __TEXT.__gcc_except_tab: 0x2a0
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0xe4

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x468
+  __TEXT.__unwind_info: 0x480
   __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x670
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x800
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
-  __DATA.__objc_const: 0x1330
-  __DATA.__objc_selrefs: 0xc60
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
-  Functions: 372
-  Symbols:   303
-  CStrings:  1109
+  Functions: 389
+  Symbols:   310
+  CStrings:  1157
 
Symbols:
+ _MCFeatureAccountModificationAllowed
+ _MCFeatureCloudBackupAllowed
+ _OBJC_CLASS_$_MBBehaviorOptions
+ _OBJC_CLASS_$_MBManagedPolicy
+ _OBJC_CLASS_$_MDMConfiguration
+ _OBJC_METACLASS_$_MBManagedPolicy
+ _objc_opt_respondsToSelector
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
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
+ "B24@0:8^@16"
+ "B48@0:8@16@24^B32^@40"
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
+ "Not changing the \"%{public}@\" state on account %{public}@: %@"
+ "T@\"MBManagedPolicy\",R,N"
+ "_behaviorOptions"
+ "_checkBehaviorOption:description:allowedOut:error:"
+ "_checkIfAnyBackupOrRestoreIsAllowed:error:"
+ "_init"
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
+ "sharedOptions"
+ "sharedPolicy"
- "Not changing the \"%{public}@\" state on account %{public}@ since the device is in EDU mode"

```
