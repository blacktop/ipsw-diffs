## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.120.13.0.0
-  __TEXT.__cstring: 0xb0d5
-  __TEXT.__const: 0x1580
+1045.0.1.0.1
+  __TEXT.__cstring: 0xb28c
+  __TEXT.__const: 0x1590
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x26a70
+  __TEXT_EXEC.__text: 0x2843c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0
   __DATA.__bss: 0x71
-  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__auth_got: 0x7f8
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3ef0
-  __DATA_CONST.__kalloc_type: 0xfc0
-  __DATA_CONST.__kalloc_var: 0x1360
+  __DATA_CONST.__const: 0x4060
+  __DATA_CONST.__kalloc_type: 0xf00
+  __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  UUID: 378DF758-22D9-378D-9C3A-3C4C80DCAC65
-  Functions: 842
+  UUID: D5F93661-8038-3DB0-8590-4A2A7BB75E31
+  Functions: 881
   Symbols:   0
-  CStrings:  1105
+  CStrings:  1116
 
CStrings:
+ "\"%s: /chosen is missing unique-device-id-string\" @%s:%d"
+ "\"%s: /chosen/unique-device-id-string is too large: %d\" @%s:%d"
+ "\"AMFI: No AppleSocMisc?\\n\" @%s:%d"
+ "\"AMFI: Unable to query BPR via AppleSocMisc: 0x%x\\n\" @%s:%d"
+ "\"AMFI: Unable to set BPR via AppleSocMisc: 0x%x\\n\" @%s:%d"
+ "/arm-io/soc-misc"
+ "19:13:11"
+ "AMFI: [ApplePMGRNub] latched BPR\n"
+ "AMFI: [AppleSocMisc] latched BPR\n"
+ "AppleSoCMisc"
+ "CoreEntitlements: duplicate key | %.*s\n"
+ "CoreEntitlements: validation | %.*s: 0x%04X\n"
+ "May 30 2025"
+ "getBPR"
+ "setBPR"
+ "site.ACMRequirement.ACMRequirementDataPushButton"
+ "unique-device-id-string"
- "1221"
- "20:14:59"
- "AMFI: PMGRAON latched to: %x\n"
- "Apr 22 2025"
- "CoreEntitlements: %.*s | duplicated key\n"
- "site.Image3InternalState"

```
