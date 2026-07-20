## ecosystemanalyticsd

> `/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x9b80
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0x120
+39.0.1.0.0
+  __TEXT.__text: 0xa190
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x2ba
+  __TEXT.__const: 0x2fa
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x359
-  __TEXT.__objc_methtype: 0xdd
-  __TEXT.__constg_swiftt: 0x1f0
-  __TEXT.__swift5_typeref: 0x17a
-  __TEXT.__swift5_reflstr: 0x17b
-  __TEXT.__swift5_fieldmd: 0x124
-  __TEXT.__cstring: 0x1654
-  __TEXT.__oslogstring: 0x486
-  __TEXT.__swift5_capture: 0x13c
-  __TEXT.__swift5_types: 0x10
+  __TEXT.__objc_methname: 0x379
+  __TEXT.__objc_methtype: 0xe6
+  __TEXT.__constg_swiftt: 0x230
+  __TEXT.__swift5_typeref: 0x19a
+  __TEXT.__swift5_reflstr: 0x19d
+  __TEXT.__swift5_fieldmd: 0x14c
+  __TEXT.__cstring: 0x1684
+  __TEXT.__oslogstring: 0x656
+  __TEXT.__swift5_capture: 0x128
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__const: 0x781
+  __DATA_CONST.__const: 0x7b1
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__auth_ptr: 0xf0
-  __DATA.__objc_const: 0x2d0
-  __DATA.__objc_selrefs: 0xe0
-  __DATA.__data: 0x3e8
+  __DATA_CONST.__auth_got: 0x500
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__auth_ptr: 0x118
+  __DATA.__objc_const: 0x2f0
+  __DATA.__objc_selrefs: 0xf0
+  __DATA.__data: 0x428
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 149
-  Symbols:   249
-  CStrings:  190
+  Functions: 152
+  Symbols:   259
+  CStrings:  201
 
Symbols:
+ _$s18EcosystemAnalytics21SystemPressureMonitorO07isUnderD020thermalStateProviderSbSo020NSProcessInfoThermalI0VyXE_tFZ
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$ss13ManagedBufferCMn
+ _$ss5Int32VMn
+ _$ss6UInt32VMn
+ _$ss6UInt64VMn
+ _OBJC_CLASS_$_NSProcessInfo
+ _notify_cancel
+ _notify_get_state
+ _notify_register_dispatch
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_endAccess
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
