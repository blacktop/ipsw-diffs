## com.apple.driver.AudioDMACLLTEscalationDetector-T8150

> `com.apple.driver.AudioDMACLLTEscalationDetector-T8150`

```diff

-540.26.0.0.0
+600.43.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x5b6
+  __TEXT.__cstring: 0x5f2
   __TEXT.__os_log: 0x25e
-  __TEXT_EXEC.__text: 0x40c8
+  __TEXT_EXEC.__text: 0x41f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd00
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: F2C4D721-17A2-3FE5-ADDA-CB451BAFBDC0
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x40
+  UUID: 4C7AEE83-BA5E-318D-AEBA-5642E56252A5
   Functions: 83
   Symbols:   0
-  CStrings:  60
+  CStrings:  61
 
Functions:
~ sub_fffffe00096dccf0 -> sub_fffffe0009acf680 : 256 -> 268
~ sub_fffffe00096dd21c -> sub_fffffe0009acfbb8 : 292 -> 304
~ sub_fffffe00096dd79c -> sub_fffffe0009ad0144 : 1080 -> 1264
~ sub_fffffe00096e06d0 -> sub_fffffe0009ad3130 : 628 -> 716
CStrings:
+ "%s: Built on %s at %s. \n          \tRack tunables = %s\n          \tCED enabled   = %s\n          \tMode          = %s\n          \tAbs CLTR Ovr  = 0x%08x\n          \tEsc Dura Ovr  = 0x%08x\n          \tTrig Thr Ovr  = 0x%08x\n          \tPanic sPS(0)  = %s\n          \tAggressive    = %s\n          \n"
+ "02:47:10"
+ "121111121222121211111122121212121212121211212121212211112222221112222222222222222222222222222222222222222222222222222222"
+ "Jun  5 2026"
+ "override_tunables_aggressive"
- "%s: Built on %s at %s. \n          \tRack tunables = %s\n          \tCED enabled   = %s\n          \tMode          = %s\n          \tAbs CLTR Ovr  = 0x%08x\n          \tEsc Dura Ovr  = 0x%08x\n          \tTrig Thr Ovr  = 0x%08x\n          \tPanic sPS(0)  = %s\n          \n"
- "12111112122212121111112212121212121212121121212121221111222221112222222222222222222222222222222222222222222222222222222"
- "20:41:40"
- "Apr 23 2026"

```
