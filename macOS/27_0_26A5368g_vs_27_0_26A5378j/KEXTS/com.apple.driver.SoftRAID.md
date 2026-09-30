## com.apple.driver.SoftRAID

> `com.apple.driver.SoftRAID`

```diff

   __TEXT.__const: 0x180
   __TEXT.__cstring: 0x26fb
-  __TEXT_EXEC.__text: 0x31d18
+  __TEXT_EXEC.__text: 0x31cf8
   __TEXT_EXEC.__auth_stubs: 0x650
   __DATA.__data: 0xc8
   __DATA.__common: 0x818
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN47com_softraid_driver_SoftRAID_DaemonEventHandler24ClearErrorHistoryForDiskEP33com_softraid_driver_SoftRAID_Disk : 144 -> 128
~ __ZN35com_softraid_driver_SoftRAID_Volume19PostAddVolumeClientEP9IOServicej : 320 -> 324
~ __ZN35com_softraid_driver_SoftRAID_Volume25ClientHasAccessPermissionEPK9IOServicebb : 300 -> 292
~ __ZN35com_softraid_driver_SoftRAID_Volume18RemoveVolumeClientEP9IOService : 280 -> 268
CStrings:
+ "21:04:35"
+ "Jun 29 2026"
- "22:20:34"
- "Jun 15 2026"

```
