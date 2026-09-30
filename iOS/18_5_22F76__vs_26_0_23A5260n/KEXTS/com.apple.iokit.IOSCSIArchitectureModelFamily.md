## com.apple.iokit.IOSCSIArchitectureModelFamily

> `com.apple.iokit.IOSCSIArchitectureModelFamily`

```diff

-500.120.2.0.0
+529.0.0.0.2
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x1451
-  __TEXT_EXEC.__text: 0x184ec
+  __TEXT.__cstring: 0x184b
+  __TEXT_EXEC.__text: 0x19780
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x418
-  __DATA.__common: 0x1c8
+  __DATA.__common: 0x1d0
   __DATA.__bss: 0x68
-  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x60
   __DATA_CONST.__const: 0x3c70
   __DATA_CONST.__kalloc_var: 0x5a0
   __DATA_CONST.__kalloc_type: 0xa80
-  UUID: 6215930F-E8CF-3F4D-BE7E-D10BF791BBA6
-  Functions: 697
+  UUID: F7AAF1A6-54B6-3BD0-8C76-CA950F8C7C37
+  Functions: 711
   Symbols:   0
-  CStrings:  166
+  CStrings:  178
 
CStrings:
+ "122212222222222222222222"
+ "CheckForSufficientTimeForPMCommand"
+ "ClearPowerOnReset"
+ "MaxPowerCPORLatency"
+ "[%s::%s] [%s] ClearPowerOnReset either failed or took long; result %d, duration %llu sec, status 0x%llx\n"
+ "[%s::%s] [%s] ClearPowerOnReset in progress for %llu sec, service response 0x%x, task status 0x%x, valid Sense %d; sense data 0x%02X/0x%02X/0x%02X ...\n"
+ "[%s::%s] [%s] Could not send TEST_UNIT_READY to device; service response 0x%X, task status 0x%X; exiting ClearPowerOnReset \n"
+ "[%s::%s] [%s] drive READY, sense data 0x%02X, 0x%02X, 0x%02X\n"
+ "[%s::%s] [%s] isPMAborted %d elapsedTime %llu s command timeout %u ms\n"
+ "[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X\n"
+ "[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X, Sense Data 0x%02X, 0x%02X, 0x%02X\n"
+ "[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X, Sense Data: 0x%02X, 0x%02X, 0x%02X, happened %d times\n"
+ "[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X, happened %d times\n"
- "1222122"

```
