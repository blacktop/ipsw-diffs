## com.apple.driver.AppleHPM

> `com.apple.driver.AppleHPM`

```diff

-624.100.15.0.0
-  __TEXT.__cstring: 0x1ddaa
+647.0.0.0.0
+  __TEXT.__cstring: 0x1de5c
   __TEXT.__const: 0xf0
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x61dd0
+  __TEXT_EXEC.__text: 0x61eb8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x6d0
+  __DATA.__data: 0x970
   __DATA.__common: 0x630
   __DATA.__bss: 0x4
+  __DATA_CONST.__mod_init_func: 0x130
+  __DATA_CONST.__mod_term_func: 0x130
+  __DATA_CONST.__const: 0x15ea8
+  __DATA_CONST.__kalloc_type: 0xcc0
   __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__mod_init_func: 0x130
-  __DATA_CONST.__mod_term_func: 0x130
-  __DATA_CONST.__const: 0x15db8
-  __DATA_CONST.__kalloc_type: 0xcc0
-  UUID: B7EF8F57-A4BB-3CDB-8B36-44C344FB0A44
+  UUID: EC5B3AF7-0E2E-3DAD-BE5C-D738C57CD8C5
   Functions: 1654
   Symbols:   0
-  CStrings:  1691
+  CStrings:  1694
 
Functions:
~ __ZN17AppleHPMInterface13setPowerStateEmP9IOService -> sub_fffffe0008effcf0 : 1112 -> 1116
~ sub_fffffe0008c3ac1c -> sub_fffffe0008f06a40 : 284 -> 276
~ __ZN17AppleHPMInterface20updateSSAMConnectionEjyj -> sub_fffffe0008f0c214 : 524 -> 516
~ __ZN17AppleHPMInterface15reconfigureSSAMEhjb -> sub_fffffe0008f0c418 : 692 -> 1012
~ __ZN17AppleTCController13setPowerStateEmP9IOService -> sub_fffffe0008f27da8 : 852 -> 856
~ sub_fffffe0008c6cf10 -> sub_fffffe0008f38e68 : 208 -> 212
~ sub_fffffe0008c71360 -> sub_fffffe0008f3d2bc : 152 -> 156
~ __ZN14AppleHPMDevice13setI2CAddressEj -> sub_fffffe0008f3d574 : 692 -> 696
~ sub_fffffe0008c760e4 -> sub_fffffe0008f42048 : 232 -> 236
~ sub_fffffe0008c7b588 -> sub_fffffe0008f474f0 : 3208 -> 3204
~ sub_fffffe0008c7e5c0 -> sub_fffffe0008f4a524 : 12992 -> 12900
CStrings:
+ "%s::%s(0x%x@0x%x): cable is captive\n\n"
+ "%s::%s(0x%x@0x%x): cable is not captive\n\n"
+ "%s::%s(0x%x@0x%x): no sop data, can't tell if captive, setting true by default\n\n"
+ "12111112122212121111112111121122121222222221221212111111121212"
- "121111121222121211111121111211221211111121212"

```
