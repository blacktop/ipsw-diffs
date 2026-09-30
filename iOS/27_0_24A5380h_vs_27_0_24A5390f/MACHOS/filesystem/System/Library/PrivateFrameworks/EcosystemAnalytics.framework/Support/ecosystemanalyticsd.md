## ecosystemanalyticsd

> `/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x5ebc
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0xa0
+39.0.1.0.0
+  __TEXT.__text: 0x64c0
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x22a
+  __TEXT.__const: 0x28a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x2e9
-  __TEXT.__objc_methtype: 0xd7
-  __TEXT.__constg_swiftt: 0x14c
-  __TEXT.__swift5_typeref: 0x120
-  __TEXT.__swift5_reflstr: 0x12b
-  __TEXT.__swift5_fieldmd: 0x100
-  __TEXT.__cstring: 0x1016
-  __TEXT.__swift5_capture: 0x11c
-  __TEXT.__oslogstring: 0xc6
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__objc_methname: 0x319
+  __TEXT.__objc_methtype: 0xe6
+  __TEXT.__constg_swiftt: 0x198
+  __TEXT.__swift5_typeref: 0x140
+  __TEXT.__swift5_reflstr: 0x14d
+  __TEXT.__swift5_fieldmd: 0x128
+  __TEXT.__cstring: 0x1046
+  __TEXT.__swift5_capture: 0x108
+  __TEXT.__oslogstring: 0x297
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__const: 0x6e1
+  __TEXT.__unwind_info: 0x168
+  __DATA_CONST.__const: 0x739
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__auth_ptr: 0xc8
-  __DATA.__objc_const: 0x270
-  __DATA.__objc_selrefs: 0xc8
-  __DATA.__data: 0x338
+  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_ptr: 0xf0
+  __DATA.__objc_const: 0x290
+  __DATA.__objc_selrefs: 0xd8
+  __DATA.__data: 0x378
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 118
-  Symbols:   215
-  CStrings:  141
+  Functions: 121
+  Symbols:   234
+  CStrings:  152
 
Symbols:
+ _$s18EcosystemAnalytics21SystemPressureMonitorO07isUnderD020thermalStateProviderSbSo020NSProcessInfoThermalI0VyXE_tFZ
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$ss13ManagedBufferCMn
+ _$ss5Int32VMn
+ _$ss6UInt32VMn
+ _$ss6UInt64VMn
+ _OBJC_CLASS_$_NSProcessInfo
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _notify_cancel
+ _notify_get_state
+ _notify_register_dispatch
+ _objc_retain_x19
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_endAccess
+ _swift_getForeignTypeMetadata
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x28
+ _swift_retain_x24
+ _swift_retain_x28
- _$sSo17OS_dispatch_queueC8DispatchE4sync7executexxyKXE_tKlF
- _dispatch_sync
- _swift_isEscapingClosureAtFileLocation
CStrings:
+ "com.apple.ecosystem.gameModeNotify"
+ "com.apple.system.game_mode_status_changed"
+ "ecosystemanalyticsd: Game Mode notification received, active: %{bool}d"
+ "ecosystemanalyticsd: Seeded initial Game Mode state, active: %{bool}d"
+ "ecosystemanalyticsd: gameModeActive value set to: %{bool}d"
+ "ecosystemanalyticsd: memoryPressureDetected value set to: %{bool}d"
+ "ecosystemanalyticsd: notify_get_state failed for Game Mode (status %u)"
+ "ecosystemanalyticsd: notify_get_state failed seeding Game Mode (status %u)"
+ "ecosystemanalyticsd: notify_register_dispatch failed for Game Mode (status %u)"
+ "gameModeLock"
+ "gameModeNotificationToken"
+ "memoryPressureLock"
+ "processInfo"
+ "thermalState"
+ "v12@?0i8"
- "_memoryPressureDetected"
- "com.apple.ecosystem.memoryPressureQueue"
- "ecosystemanalyticsd: _memoryPressureDetected value set to: %{bool}d"
- "memoryPressureQueue"
```
