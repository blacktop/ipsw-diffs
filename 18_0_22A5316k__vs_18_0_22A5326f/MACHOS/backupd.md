## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2349.0.31.0.2
-  __TEXT.__text: 0x26bd2c
+2349.0.42.0.0
+  __TEXT.__text: 0x26b4f4
   __TEXT.__auth_stubs: 0x3320
   __TEXT.__objc_stubs: 0x2a580
   __TEXT.__objc_methlist: 0x174cc
-  __TEXT.__cstring: 0x69356
-  __TEXT.__objc_methname: 0x372e3
-  __TEXT.__const: 0x1480
+  __TEXT.__cstring: 0x69051
+  __TEXT.__objc_methname: 0x372ed
+  __TEXT.__const: 0x1470
   __TEXT.__constg_swiftt: 0x8e4
   __TEXT.__swift5_typeref: 0x9af
   __TEXT.__swift5_reflstr: 0x6b5

   __TEXT.__swift5_types: 0x8c
   __TEXT.__objc_classname: 0x1f5a
   __TEXT.__objc_methtype: 0x6724
-  __TEXT.__oslogstring: 0x30134
+  __TEXT.__oslogstring: 0x2feb9
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_capture: 0xe8

   __TEXT.__ustring: 0x4
   __TEXT.__info_plist: 0x500
   __TEXT.__unwind_info: 0x69e0
-  __TEXT.__eh_frame: 0x12b0
+  __TEXT.__eh_frame: 0x12a8
   __DATA_CONST.__auth_got: 0x19a0
   __DATA_CONST.__got: 0xe50
-  __DATA_CONST.__auth_ptr: 0x320
-  __DATA_CONST.__const: 0x7a20
-  __DATA_CONST.__cfstring: 0x1e840
+  __DATA_CONST.__auth_ptr: 0x318
+  __DATA_CONST.__const: 0x7a60
+  __DATA_CONST.__cfstring: 0x1e7e0
   __DATA_CONST.__objc_classlist: 0xa18
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x200

   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x7b0
   __DATA_CONST.__objc_intobj: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0xd30
+  __DATA_CONST.__objc_arraydata: 0xd38
   __DATA_CONST.__objc_dictobj: 0x258
-  __DATA_CONST.__objc_arrayobj: 0x4c8
+  __DATA_CONST.__objc_arrayobj: 0x4e0
   __DATA.__objc_const: 0x27c70
   __DATA.__objc_selrefs: 0xc120
   __DATA.__objc_ivar: 0x1cd4

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9658
-  Symbols:   1396
-  CStrings:  23860
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 9659
+  Symbols:   1404
+  CStrings:  23842
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "=restore-policy= Ignoring Lightrail data in snapshot"
+ "=restore-policy= Ignoring Lightrail data in snapshot"
+ "Failed to reset cache: %!@(MISSING)"
+ "Failed to reset cache: %!@(MISSING)"
+ "Invalidating pending snapshot - build %!@(MISSING) != %!@(MISSING)"
+ "Invalidating pending snapshot - build %!@(MISSING) != %!@(MISSING)"
+ "Invalidating pending snapshot - format %!l(MISSING)d != %!l(MISSING)d"
+ "Invalidating pending snapshot - format %!l(MISSING)d != %!l(MISSING)d"
+ "Invalidating pending snapshot - type %!l(MISSING)d != %!l(MISSING)d"
+ "Invalidating pending snapshot - type %!l(MISSING)d != %!l(MISSING)d"
+ "Not clearing follow up with identifier %!@(MISSING)"
+ "Not clearing follow up with identifier %!@(MISSING)"
+ "SELECT DISTINCT(domain) FROM Manifests WHERE snapshotID NOT IN (SELECT snapshotID FROM Snapshots) AND manifestID NOT IN (SELECT manifestID FROM Files)"
+ "clearPendingFollowUpsNotBelongingToAccounts:excluding:"
- "-[MBServiceManager setBackupEnabled:account:connection:]"
- "=restore-policy= Could not find cloudFormatInfo"
- "=restore-policy= Could not find cloudFormatInfo"
- "=restore-policy= Default ignoring Lightrail data in snapshot"
- "=restore-policy= Default ignoring Lightrail data in snapshot"
- "=restore-policy= Disabling Lightrail restore for %!@(MISSING) persona %!@(MISSING)"
- "=restore-policy= Disabling Lightrail restore for %!@(MISSING) persona %!@(MISSING)"
- "=restore-policy= Disabling Lightrail restore for %!@(MISSING) snapshot %!@(MISSING)"
- "=restore-policy= Disabling Lightrail restore for %!@(MISSING) snapshot %!@(MISSING)"
- "=restore-policy= Existing snapshot format: '%!@(MISSING)' does not match the BehaviorOption RequiredRestoreSnapshotFormat: '%!@(MISSING)'"
- "=restore-policy= Existing snapshot format: '%!@(MISSING)' does not match the BehaviorOption RequiredRestoreSnapshotFormat: '%!@(MISSING)'"
- "=restore-policy= Failed to determine if restoring from file lists - invalid value %!@(MISSING) for key %!@(MISSING)"
- "=restore-policy= Failed to determine if restoring from file lists - invalid value %!@(MISSING) for key %!@(MISSING)"
- "=restore-policy= Falling back to legacy restore, since last failure (%!@(MISSING)) was within two weeks"
- "=restore-policy= Falling back to legacy restore, since last failure (%!@(MISSING)) was within two weeks"
- "=restore-policy= Local preference disabled Lightrail restore"
- "=restore-policy= Local preference disabled Lightrail restore"
- "=restore-policy= Local preference enabled Lightrail restore"
- "=restore-policy= Local preference enabled Lightrail restore"
- "=restore-policy= Server disabled Lightrail restore"
- "=restore-policy= Server disabled Lightrail restore"
- "=restore-policy= Server enabled Lightrail restore"
- "=restore-policy= Server enabled Lightrail restore"
- "=restore-policy= Target snapshot %!@(MISSING) format (%!@(MISSING)) is not ManifestsFilesAndDomains"
- "=restore-policy= Target snapshot %!@(MISSING) format (%!@(MISSING)) is not ManifestsFilesAndDomains"
- "Could not find cloudFormatInfo"
- "Existing snapshot format: '%!@(MISSING)' does not match the BehaviorOption RequiredRestoreSnapshotFormat: '%!@(MISSING)'"
- "Failed to determine if restoring from file lists - invalid value %!@(MISSING)"
- "Invalidating pending snapshot (%!l(MISSING)d, %!l(MISSING)d) != (%!l(MISSING)d, %!l(MISSING)d)"
- "Invalidating pending snapshot (%!l(MISSING)d, %!l(MISSING)d) != (%!l(MISSING)d, %!l(MISSING)d)"
- "clearPendingFollowUpsNotBelongingToAccounts:"
- "missing com.apple.decmpfs error"

```
