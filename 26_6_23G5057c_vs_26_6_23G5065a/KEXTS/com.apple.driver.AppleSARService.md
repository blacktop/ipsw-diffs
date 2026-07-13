## com.apple.driver.AppleSARService

> `com.apple.driver.AppleSARService`

```diff

-  __TEXT.__os_log: 0xfd12
+  __TEXT.__os_log: 0xfd95
   __TEXT.__const: 0x1030
-  __TEXT.__cstring: 0xe16e
-  __TEXT_EXEC.__text: 0x6c4a4
+  __TEXT.__cstring: 0xe204
+  __TEXT_EXEC.__text: 0x6c7a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0x648

   __DATA_CONST.__const: 0x5930
   __DATA_CONST.__kalloc_type: 0x3f80
   __DATA_CONST.__kalloc_var: 0x190
-  Functions: 658
+  Functions: 659
   Symbols:   0
-  CStrings:  1826
+  CStrings:  1833
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
Functions:
+ sub_fffffe0009130294
CStrings:
+ "%s::%s:%d: CentralHSAR pointer is null"
+ "%s::%s:%d: cluster count (%u) must be in [1, %u]"
+ "%s::%s:%d: current index (%u) must be < %u"
+ "isValidCentralHSAR"

```
