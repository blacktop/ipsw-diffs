## com.apple.iokit.IOAccessoryManager

> `com.apple.iokit.IOAccessoryManager`

```diff

   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x11056
-  __TEXT.__os_log: 0x12066
-  __TEXT_EXEC.__text: 0xe49e8
+  __TEXT.__cstring: 0x11078
+  __TEXT.__os_log: 0x121cf
+  __TEXT_EXEC.__text: 0xe4e84
   __TEXT_EXEC.__auth_stubs: 0xbb0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x16b8
   __DATA.__bss: 0x142
   __DATA_CONST.__mod_init_func: 0x348
   __DATA_CONST.__mod_term_func: 0x340
-  __DATA_CONST.__const: 0x2ac50
+  __DATA_CONST.__const: 0x2ac98
   __DATA_CONST.__kalloc_type: 0x2500
   __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 5009
+  Functions: 5013
   Symbols:   0
-  CStrings:  2958
+  CStrings:  2964
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
CStrings:
+ "%s::%s(): Setting forcePortWet... (target: %s, forcePortWet: %s)\n"
+ "%s::%s(): [%s%s%s] ForcePortWet override active — treating measurement as wet\n\n"
+ "%s::%s(): [%s%s%s] LDCM: Empty port, no charger present - setting mitigations to Triggered\n\n"
+ "%s::%s(): [%s%s%s] LDCM: Empty port, was Failed - resetting to Triggered to dismiss intrusive UI\n\n"
+ "%s::%s(): [%s%s%s] forcePortWet: %s\n\n"
+ "1211111212221212111111211112112212122222222122121212"
+ "_setForcePortWet"
+ "setForcePortWet"
- "%s::%s(): [%s%s%s] Empty port, was Failed - resetting to Triggered to dismiss intrusive UI\n\n"
- "121111121222121211111121111211221212222222212212121"

```
