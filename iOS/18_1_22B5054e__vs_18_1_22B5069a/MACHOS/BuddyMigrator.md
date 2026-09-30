## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5347.0.0.0.0
-  __TEXT.__text: 0x10658
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_stubs: 0x19e0
-  __TEXT.__objc_methlist: 0x874
+5350.3.0.0.0
+  __TEXT.__text: 0x10d30
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0x91c
   __TEXT.__const: 0x1bc
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__objc_methname: 0x204c
-  __TEXT.__cstring: 0xd61
-  __TEXT.__oslogstring: 0x1658
-  __TEXT.__objc_classname: 0xf2
-  __TEXT.__objc_methtype: 0x275
+  __TEXT.__objc_methname: 0x2275
+  __TEXT.__cstring: 0xdd1
+  __TEXT.__oslogstring: 0x1728
+  __TEXT.__objc_classname: 0x11f
+  __TEXT.__objc_methtype: 0x299
   __TEXT.__dlopen_cstrs: 0x166
   __TEXT.__swift5_typeref: 0x36a
   __TEXT.__swift5_fieldmd: 0x128

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__unwind_info: 0x548
   __TEXT.__eh_frame: 0x7b0
-  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__auth_got: 0x518
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x8c8
-  __DATA_CONST.__cfstring: 0xa00
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1780
-  __DATA.__objc_selrefs: 0x840
-  __DATA.__objc_ivar: 0xa8
-  __DATA.__objc_data: 0x800
+  __DATA.__objc_const: 0x18f0
+  __DATA.__objc_selrefs: 0x8a0
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_data: 0x850
   __DATA.__data: 0x418
   __DATA.__bss: 0x60
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 383
-  Symbols:   319
-  CStrings:  675
+  Functions: 403
+  Symbols:   324
+  CStrings:  709
 
Symbols:
+ _OBJC_CLASS_$_BYStolenDeviceProtectionPreferenceMigrator
+ _OBJC_METACLASS_$_BYStolenDeviceProtectionPreferenceMigrator
+ __os_log_debug_impl
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _objc_exception_throw
CStrings:
+ "\""
+ "@40@0:8q16@24@32"
+ "BYStolenDeviceProtectionPreferenceMigrator"
+ "DisplayZoomRestart"
+ "Migrating keys"
+ "Neither postRestoreFromBackup or postSoftwareUpdate are set"
+ "No SDP migration occurred."
+ "No SDP preference migration needed"
+ "SDP preference post SU migration"
+ "SDP preference post restore migration"
+ "SDP preferences updated. didMigrate: %!d(MISSING), didClear: %!d(MISSING). SDP State: %!d(MISSING)"
+ "T@\"BYPreferencesController\",&,N,V_sourcePreferences"
+ "T@\"BYPreferencesController\",&,N,V_targetPreferences"
+ "Tq,N,V_migrationContext"
+ "_clearPreferenceKeyFromSourcePreferences"
+ "_didClear"
+ "_didMigrate"
+ "_migrateKeys"
+ "_migratePreferenceKeyIfNeeded"
+ "_migrateStolenDeviceProtectionPreferenceKeys"
+ "_migrationContext"
+ "_sourcePreferences"
+ "_targetPreferences"
+ "com.apple.purplebuddy.notbackedup"
+ "initWithMigrationContext:sourcePreferences:targetPreferences:"
+ "migratePreferenceWithSDPEnabledState:"
+ "migrationContext"
+ "q16@0:8"
+ "setMigrationContext:"
+ "setSourcePreferences:"
+ "setTargetPreferences:"
+ "sourcePreferences"
+ "targetPreferences"
+ "v24@0:8q16"

```
