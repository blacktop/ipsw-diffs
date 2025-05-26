## libnfrestore.dylib

> `/usr/lib/libnfrestore.dylib`

```diff

-342.4.1.0.0
-  __TEXT.__text: 0x21f48
+344.25.0.0.0
+  __TEXT.__text: 0x223f4
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__cstring: 0x50f9
-  __TEXT.__oslogstring: 0x409f
+  __TEXT.__cstring: 0x5132
+  __TEXT.__oslogstring: 0x4119
   __TEXT.__const: 0x90
-  __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x218
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__cfstring: 0xaa0
+  __AUTH_CONST.__cfstring: 0xa80
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__auth_got: 0x6e8
   __DATA.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   Functions: 177
-  Symbols:   520
-  CStrings:  1109
+  Symbols:   521
+  CStrings:  1113
 
Symbols:
+ _GetElapsedTimeInMillisecondsFromMachTime
+ __os_log_default
+ __os_log_fault_impl
+ _mach_continuous_time
+ _strlcpy
- ___strcpy_chk
- _malloc_type_malloc
- _strcpy
- _strncpy
CStrings:
+ "%s:%i Error : read in progress since %llu"
+ "%s:%i Invalid file name %s"
+ "%s:%i Read aborted while in progress since %llu."
+ "%s:%i Skipping SPMIIRQ"
+ "%s:%i calloc failure..."
+ "%{public}s:%i Error : read in progress since %llu"
+ "%{public}s:%i Invalid file name %s"
+ "%{public}s:%i Read aborted while in progress since %llu."
+ "%{public}s:%i Skipping SPMIIRQ"
+ "%{public}s:%i calloc failure..."
+ "Error : read already in progress."
+ "SE310S_FW_A0_01_01_10_rev144148.bin"
+ "SN100V_FW_A3_01_01_98_rev143656.bin"
+ "SN200V_FURY_FW_B1_02_01_9A_rev143673.bin"
+ "SN200V_FW_B1_02_01_9B_rev143664.bin"
+ "SN300V_FW_B0_02_01_43_rev144147.bin"
+ "SN300V_FW_B0_02_01_E0_rev140388.bin"
- "%s:%i Error : read in progress"
- "%s:%i Read aborted while in progress."
- "%s:%i malloc failure..."
- "%{public}s:%i Error : read in progress"
- "%{public}s:%i Read aborted while in progress."
- "%{public}s:%i malloc failure..."
- "SE310S_FW_A0_01_01_09_rev134410.bin"
- "SN100V_FW_A3_01_01_91_rev137668.bin"
- "SN200V_FURY_FW_B1_02_01_95_rev139831.bin"
- "SN200V_FW_B1_02_01_95_rev139831.bin"
- "SN300V_FW_B0_02_01_3F_rev141766.bin"
- "SN300V_FW_B0_02_01_DC_rev136335.bin"
- "spmiSlaveReset"

```
