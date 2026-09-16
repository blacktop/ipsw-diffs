## com.apple.driver.AppleCamera

> `com.apple.driver.AppleCamera`

```diff

-20.77.1.0.0
-  __TEXT.__const: 0xa270
-  __TEXT.__cstring: 0x1a452
-  __TEXT.__os_log: 0x1601d
-  __TEXT_EXEC.__text: 0xa08c4
+20.104.4.0.0
+  __TEXT.__const: 0xa290
+  __TEXT.__cstring: 0x1a571
+  __TEXT.__os_log: 0x1613c
+  __TEXT_EXEC.__text: 0xa0bc4
   __TEXT_EXEC.__auth_stubs: 0x1160
   __DATA.__data: 0x2a8
   __DATA.__common: 0x540
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x164a8
-  __DATA_CONST.__kalloc_type: 0x1340
+  __DATA_CONST.__kalloc_type: 0x13c0
   __DATA_CONST.__kalloc_var: 0xa50
   __DATA_CONST.__auth_got: 0x8b0
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 1855
+  Functions: 1856
   Symbols:   0
-  CStrings:  2548
+  CStrings:  2551
 
Functions:
~ __ZN11AppleCamera23ISPSharedMemorySurfaces13allocateIOBMDEyjPP28ISPSharedMemorySurfaceParamsbb : 1288 -> 1308
~ __ZN11AppleCamera23ISP_PowerOnCamera_gatedEPvjb : 2380 -> 2992
~ __ZN11AppleCamera10ISP_deInitEv : 840 -> 860
+ sub_fffffe0008b3753c
CStrings:
+ "AppleCamera:%s - Power-off completed (fPowerEvent=%d), proceeding with power-on\n"
+ "AppleCamera:%s - Power-off did not complete within 1s (fPowerEvent=%d). Return busy\n"
+ "AppleCamera:%s - fPowerEvent=%d (PowerOffPending), waiting for power-off to complete before power-on\n"
+ "AppleCamera:%s - fPowerEvent=%d, fw timeout=%d. Return busy (firmware timeout)\n"
- "AppleCamera:%s - fPowerEvent=%d, fw timeout=%d. Return busy\n"
```
