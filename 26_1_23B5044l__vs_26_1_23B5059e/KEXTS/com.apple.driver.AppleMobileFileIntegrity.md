## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-1045.40.2.0.2
-  __TEXT.__cstring: 0xbe1e
+1045.40.10.0.0
+  __TEXT.__cstring: 0xbf76
   __TEXT.__const: 0x1570
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x28ae4
+  __TEXT_EXEC.__text: 0x28bfc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x6f2
+  __DATA.__data: 0x702
   __DATA.__common: 0xb0
   __DATA.__bss: 0x81
   __DATA_CONST.__auth_got: 0x7f8

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x40c0
-  __DATA_CONST.__kalloc_type: 0xf00
+  __DATA_CONST.__const: 0x40d0
+  __DATA_CONST.__kalloc_type: 0xf80
   __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  UUID: 4266268C-AD00-31D4-874E-05B037FD865C
+  UUID: F21F6231-81A5-3C87-8DA4-84B8809F050D
   Functions: 894
   Symbols:   0
-  CStrings:  1210
+  CStrings:  1218
 
Functions:
~ sub_fffffe0009856aa4 -> sub_fffffe0009874284 : 40 -> 80
~ sub_fffffe0009856acc -> sub_fffffe00098742d4 : 44 -> 68
~ sub_fffffe000985e04c -> sub_fffffe000987b86c : 1476 -> 1532
~ sub_fffffe000985ea64 -> sub_fffffe000987c2bc : 220 -> 212
~ sub_fffffe000985f1dc -> sub_fffffe000987ca2c : 960 -> 1128
CStrings:
+ "112221122211201212222212"
+ "21:18:31"
+ "AMFI: Failed to allocate ProcessAccessor objects\n"
+ "Couldn't find trust cache UUID for library from SMAC"
+ "Couldn't find trust cache UUID for process when mapping library from SMAC"
+ "Non-SMAC process not permitted to map library from SMAC"
+ "Oct  1 2025"
+ "SMAC process not permitted to map library from different SMAC"
+ "com.apple.TelephonyUtilities"
+ "com.apple.coretelephony"
+ "site.ProcessAccessor"
- "20:21:00"
- "Sep 16 2025"
- "mapping process is not compatible with SMAC dylib"

```
