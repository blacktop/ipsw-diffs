## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-1045.0.25.0.0
-  __TEXT.__cstring: 0xb1f6
-  __TEXT.__const: 0x1590
+1045.0.35.0.0
+  __TEXT.__cstring: 0xb320
+  __TEXT.__const: 0x1570
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x28418
+  __TEXT_EXEC.__text: 0x286a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0

   __DATA_CONST.__kalloc_type: 0xf00
   __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  UUID: 8DAB6793-53DC-325C-9808-951C1C2855A9
+  UUID: 58DDECEA-7870-336B-B210-20FCBD5DFB2C
   Functions: 882
   Symbols:   0
-  CStrings:  1114
+  CStrings:  1119
 
Functions:
~ __ZN24AppleMobileFileIntegrity31submitSHA1CodeDirectoryAnalyticEP13VnodeLazyPathP7cs_blob : 1140 -> 1748
~ __ZL22_vnode_check_signatureP5vnodeP5labeliP7cs_blobPjS5_ijPPcPm : 6384 -> 6388
~ sub_fffffff0097ff0a8 -> sub_fffffff00980394c : 640 -> 624
~ sub_fffffff0097ff328 -> sub_fffffff009803bbc : 252 -> 308
CStrings:
+ "21:46:16"
+ "AMFI: Failed to set cpu_type in the SHA1 code directory usage event payload\n"
+ "AMFI: Failed to set has_restricted_entitlements in the SHA1 code directory usage event payload\n"
+ "AMFI: Failed to set signing_identifier in the SHA1 code directory usage event payload\n"
+ "AMFI: Failed to set team_identifier in the SHA1 code directory usage event payload\n"
+ "AMFI: Failed to set validation_category in the SHA1 code directory usage event payload\n"
+ "Jul 25 2025"
+ "cpu_type"
+ "has_restricted_entitlements"
- "23:10:09"
- "AMFI: Failed to set signing identifier in the SHA1 code directory usage event payload\n"
- "AMFI: Failed to set team identifier in the SHA1 code directory usage event payload\n"
- "Jul 14 2025"

```
