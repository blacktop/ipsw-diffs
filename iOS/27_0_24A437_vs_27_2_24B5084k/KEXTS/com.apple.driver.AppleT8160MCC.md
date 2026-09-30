## com.apple.driver.AppleT8160MCC

> `com.apple.driver.AppleT8160MCC`

```diff

-127.0.3.0.0
+127.40.4.0.0
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x5ef2
-  __TEXT.__os_log: 0x26dc
-  __TEXT_EXEC.__text: 0x167dc
-  __TEXT_EXEC.__auth_stubs: 0x5a0
+  __TEXT.__cstring: 0x5f8f
+  __TEXT.__os_log: 0x26ff
+  __TEXT_EXEC.__text: 0x168f4
+  __TEXT_EXEC.__auth_stubs: 0x5b0
   __DATA.__data: 0xb200
   __DATA.__common: 0x1f0
   __DATA_CONST.__mod_init_func: 0x20

   __DATA_CONST.__const: 0x33c0
   __DATA_CONST.__kalloc_type: 0x440
   __DATA_CONST.__kalloc_var: 0x140
-  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xc0
-  Functions: 568
+  Functions: 569
   Symbols:   0
-  CStrings:  976
+  CStrings:  981
 
Functions:
+ sub_fffffe0009925744
CStrings:
+ "\"Register write failure. Instance: %u, offest:%#x\" @%s:%d"
+ "%s:%d: Instance %u offset %#x @ %p <- %#x\n"
+ "AppleT8160MemCacheController.cpp"
+ "Instance %u offset %#x @ %p <- %#x"
+ "memProtectedWriteReg32"
```
