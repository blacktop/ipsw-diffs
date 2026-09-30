## com.apple.driver.AppleT8150

> `com.apple.driver.AppleT8150`

```diff

-  __TEXT.__cstring: 0x5eaa
+  __TEXT.__cstring: 0x601c
   __TEXT.__const: 0x110
-  __TEXT_EXEC.__text: 0xd4bc
-  __TEXT_EXEC.__auth_stubs: 0x3a0
+  __TEXT_EXEC.__text: 0xdd0c
+  __TEXT_EXEC.__auth_stubs: 0x3c0
   __DATA.__data: 0xbbc
   __DATA.__common: 0x128
   __DATA.__bss: 0x610

   __DATA_CONST.__const: 0x9000
   __DATA_CONST.__kalloc_type: 0x1c0
   __DATA_CONST.__kalloc_var: 0x190
-  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0xb0
-  Functions: 426
+  Functions: 441
   Symbols:   0
-  CStrings:  779
+  CStrings:  787
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__got : content changed
CStrings:
+ "\"glb-time-source malformed: length %u, expected %lu\" @%s:%d"
+ "\"wake-time-counter present (%u entries) but glb-time-source missing\" @%s:%d"
+ "%s::%s: wake time tracking enabled: %u counter entries, %u apertures\n"
+ "1211111212221212121211111212222222222222222121212121212121211"
+ "1211111212221212121211111212222222222222222121212121212121211211211122222111121111211112"
+ "_clearWakeTimeCounters"
+ "_initWakeTimeFromSleep"
+ "_setWakeTimeFromSleep"
+ "glb-time-source"
+ "wake-time-counter"
- "121111121222121212121111121211"
- "121111121222121212121111121211211211122222111121111211112"

```
