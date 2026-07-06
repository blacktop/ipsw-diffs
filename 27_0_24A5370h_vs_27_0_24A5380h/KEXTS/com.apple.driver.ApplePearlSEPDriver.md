## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0xaf3f
-  __TEXT.__os_log: 0x4ce4
-  __TEXT_EXEC.__text: 0x3f288
+  __TEXT.__cstring: 0xaf58
+  __TEXT.__os_log: 0x4d27
+  __TEXT_EXEC.__text: 0x3f444
   __TEXT_EXEC.__auth_stubs: 0xba0
   __DATA.__data: 0xcd
   __DATA.__common: 0x238
   __DATA.__bss: 0x7f
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x2420
+  __DATA_CONST.__const: 0x2428
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x150
-  Functions: 715
+  Functions: 717
   Symbols:   0
-  CStrings:  1716
+  CStrings:  1718
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
CStrings:
+ "%s <- cancelOptionsMask:0x%02x, failedAttempt:%d, lock:%d\n"
+ "%s <- request:%u, flags:0x%x data:%p timeout:%u\n"
+ "commandHoldMatchSpecific"
- "%s <- request:%u, flags:0x%x timeout:%u\n"

```
