## com.apple.driver.usb.cdc.ncm

> `com.apple.driver.usb.cdc.ncm`

```diff

-372.40.2.0.0
+372.60.2.0.0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0xcf3
-  __TEXT_EXEC.__text: 0x8880
+  __TEXT.__cstring: 0xda4
+  __TEXT_EXEC.__text: 0x89ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf48
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: A6F0A78B-6A11-3F04-AC23-5785E3693DB4
-  Functions: 190
+  UUID: 37980D58-69FD-369D-B124-B09611F25707
+  Functions: 192
   Symbols:   0
-  CStrings:  129
+  CStrings:  133
 
CStrings:
+ "%06lu.%06u %s::%s: failed to clear stall : 0x%x\n"
+ "%06lu.%06u %s::%s: re-enqueue after stall returned 0x%x\n"
+ "%06lu.%06u %s::%s: result: %d, IN EP 0x%x, OUT EP 0x%x\n"
+ "transmitRecord"

```
