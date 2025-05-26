## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-342.4.1.0.0
-  __TEXT.__text: 0x15d28
-  __TEXT.__auth_stubs: 0x770
+344.25.0.0.0
+  __TEXT.__text: 0x1668c
+  __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x2803
-  __TEXT.__oslogstring: 0x1ece
-  __TEXT.__unwind_info: 0x26c
-  __DATA_CONST.__got: 0x68
+  __TEXT.__cstring: 0x293b
+  __TEXT.__oslogstring: 0x20b6
+  __TEXT.__unwind_info: 0x27c
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3d8
   __DATA.__data: 0x8
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  Functions: 177
-  Symbols:   264
-  CStrings:  564
+  Functions: 178
+  Symbols:   270
+  CStrings:  576
 
Symbols:
+ _GetElapsedTimeInMillisecondsFromMachTime
+ _NFIsInternalBuild
+ __os_log_default
+ __os_log_fault_impl
+ _mach_continuous_time
+ _malloc_default_zone
+ _phOsalNfc_IsHeapMemory
- _malloc_type_malloc
CStrings:
+ "%s:%i Debug : Current read cb = %p, context = %p"
+ "%s:%i Debug : Pending read %d, read cb = %p, context = %p"
+ "%s:%i Debug : Pending read cb = %p, context = %p"
+ "%s:%i Error : read in progress since %llu"
+ "%s:%i Failed to read : busy. Pending read = %d"
+ "%s:%i Failed to read : not initialized. Pending read = %d"
+ "%s:%i Read aborted while in progress since %llu."
+ "%s:%i phOsalNfc_IsHeapMemory: malloc_default_zone returned NULL"
+ "%{public}s:%i Debug : Current read cb = %p, context = %p"
+ "%{public}s:%i Debug : Pending read %d, read cb = %p, context = %p"
+ "%{public}s:%i Debug : Pending read cb = %p, context = %p"
+ "%{public}s:%i Error : read in progress since %llu"
+ "%{public}s:%i Failed to read : busy. Pending read = %d"
+ "%{public}s:%i Failed to read : not initialized. Pending read = %d"
+ "%{public}s:%i Read aborted while in progress since %llu."
+ "%{public}s:%i phOsalNfc_IsHeapMemory: malloc_default_zone returned NULL"
+ "Error : read already in progress."
+ "Error : read received after shutdown : %p / %p"
+ "Error : read received after shutdown : %p / %p. Driver context %llu, Controller config type %d"
+ "_phTmlNfc_DebugMWUnload"
+ "phOsalNfc_IsHeapMemory"
- "%s:%i Error : read in progress"
- "%s:%i Failed to read : busy"
- "%s:%i Failed to read : not initialized"
- "%s:%i Read aborted while in progress."
- "%{public}s:%i Error : read in progress"
- "%{public}s:%i Failed to read : busy"
- "%{public}s:%i Failed to read : not initialized"
- "%{public}s:%i Read aborted while in progress."
- "spmiSlaveReset"

```
