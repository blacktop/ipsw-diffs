## com.apple.iokit.IOSCSIBlockCommandsDevice

> `com.apple.iokit.IOSCSIBlockCommandsDevice`

```diff

-541.40.1.0.0
-  __TEXT.__cstring: 0xf50
-  __TEXT_EXEC.__text: 0xdc88
+545.100.7.0.0
+  __TEXT.__cstring: 0x1116
+  __TEXT_EXEC.__text: 0xd148
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a9
   __DATA.__common: 0x98
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__kalloc_type: 0x3c0
-  UUID: D9A3F17A-0D44-31EA-82CD-72881ED26ABD
-  Functions: 288
+  UUID: 0167152B-177D-396D-B58E-6439B154E5E8
+  Functions: 295
   Symbols:   0
-  CStrings:  123
+  CStrings:  132
 
CStrings:
+ "DetermineMediumWriteProtectState"
+ "Failed%s ReadRetries-%d"
+ "Read"
+ "SCSIBlockDevice_ReadWriteError"
+ "Write"
+ "[%s:%s] [%s]: MODE_SENSE_06 failed after %d retries, last serviceresponse: %x; TaskStatus: %x\n"
+ "[%s:%s] [%s]: MODE_SENSE_10 failed after %d retries, last serviceresponse: %x; TaskStatus: %x\n"
+ "[%s:%s] [%s]: ReadTest failed, last serviceresponse: %x; TaskStatus: %x\n"
+ "[%s:%s] [%s]: WriteTest failed: Read retries: %d; last serviceresponse: %x; TaskStatus: %x\n"

```
