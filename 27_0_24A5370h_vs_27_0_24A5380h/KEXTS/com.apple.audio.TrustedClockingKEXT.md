## com.apple.audio.TrustedClockingKEXT

> `com.apple.audio.TrustedClockingKEXT`

```diff

   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x31ae
-  __TEXT_EXEC.__text: 0xc2f4
+  __TEXT.__cstring: 0x3203
+  __TEXT_EXEC.__text: 0xc30c
   __TEXT_EXEC.__auth_stubs: 0x500
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x38
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x18d0
+  __DATA_CONST.__const: 0x18e0
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x40
-  Functions: 446
+  Functions: 447
   Symbols:   0
-  CStrings:  139
+  CStrings:  140
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
CStrings:
+ "TrustedClockingWorkloopContext::init - Invalid kernel primitive for use case ID: %u\n"

```
