## com.apple.driver.AppleMobileDispH19P-DCP

> `com.apple.driver.AppleMobileDispH19P-DCP`

```diff

-700.50.108.0.0
+700.50.112.5.0
   __TEXT.__const: 0x1920
-  __TEXT.__cstring: 0x78cd
-  __TEXT_EXEC.__text: 0x26218
+  __TEXT.__cstring: 0x79d9
+  __TEXT_EXEC.__text: 0x262b8
   __TEXT_EXEC.__auth_stubs: 0xe60
   __DATA.__data: 0x2e0
   __DATA.__common: 0x100
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x5100
+  __DATA_CONST.__const: 0x5118
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0xf0
   __DATA_CONST.__auth_got: 0x730
   __DATA_CONST.__got: 0xd0
-  Functions: 1484
+  Functions: 1487
   Symbols:   0
-  CStrings:  615
+  CStrings:  617
 
Functions:
+ sub_fffffe000929ba8c
+ sub_fffffe00092a51e4
~ __ZN23IOMobileFramebufferShim20set_digital_out_modeEjj : 8500 -> 8624
+ sub_fffffe00092bd6e8
CStrings:
+ "%s: Aborting set_digital_out_mode after dual pipe teardown on %d. HPD dropped during teardown, dual pipe timing cannot run on one pipe."
+ "Aborting set_digital_out_mode after dual pipe teardown on %d. HPD dropped during teardown, dual pipe timing cannot run on one pipe."
```
