## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-500.71.0.0.0
-  __TEXT.__const: 0x2198
-  __TEXT.__os_log: 0x933b
-  __TEXT.__cstring: 0xf8b
-  __TEXT_EXEC.__text: 0x39b2c
+500.77.0.0.0
+  __TEXT.__const: 0x21e8
+  __TEXT.__os_log: 0x9688
+  __TEXT.__cstring: 0x1022
+  __TEXT_EXEC.__text: 0x3e230
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3b8
   __DATA.__common: 0x70
-  __DATA.__bss: 0x62c0
-  __DATA_CONST.__auth_got: 0x280
+  __DATA.__bss: 0x6cc0
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x9e68
+  __DATA_CONST.__const: 0xa138
   __DATA_CONST.__kalloc_type: 0x480
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 709C667C-2F6D-3A71-ACE6-B81E72E1863B
-  Functions: 1839
+  UUID: 3541DF7B-A28F-3600-9ABD-3B1F5286A080
+  Functions: 2043
   Symbols:   0
-  CStrings:  512
+  CStrings:  522
 
CStrings:
+ "\"AppleProResHW (0x%x): %s(): ProResHW is hung, client timed out attempting to transition to power state %lu\" @%s:%d"
+ "AppleProResHW (0x%x): %s(): Dec Desc V0\n"
+ "AppleProResHW (0x%x): %s(): Dec Desc V2\n"
+ "AppleProResHW (0x%x): %s(): Override CFA=%d Meta=%p Data/Stride R=%p,%u\n"
+ "AppleProResHW (0x%x): %s(): enablePsdService POWER_ON\n"
+ "AppleProResHW (0x%x): %s(): plane allocSize=%llu, Size=%u\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Compressed not allowed for RAW Planar pixel formats\n"
+ "ERROR: AppleProResHW: %d: %s(): enablePsdService(POWER_ON) Failed ret=0x%x\n"
+ "ERROR: AppleProResHW: %d: %s(): resetPsdService() Failed ret=0x%x\n"
+ "ProResHWPanicOnPowerRequestFailure"

```
