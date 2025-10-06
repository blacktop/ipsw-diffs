## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

-65.0.0.0.0
+65.100.3.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x446f
-  __TEXT_EXEC.__text: 0x13bb0
-  __TEXT_EXEC.__auth_stubs: 0x230
+  __TEXT.__cstring: 0x44bb
+  __TEXT_EXEC.__text: 0x13bd8
+  __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x40
   __DATA.__bss: 0x19
-  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x8

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x1400
-  UUID: 2264196E-722D-359C-B516-C5C190E183BB
+  UUID: 8E45A56A-0E70-3DD9-9F90-C7BB090B8BCD
   Functions: 168
-  Symbols:   606
-  CStrings:  466
+  Symbols:   609
+  CStrings:  470
 
Symbols:
+ LibCall_ACMKernelControl.cold.1
+ LibCall_ACMSetEnvironmentVariable.cold.1
+ LibCall_ACMSetEnvironmentVariable.cold.2
+ LibCall_ACMSetEnvironmentVariable.cold.3
+ _memmove
- ___memcpy_chk
- _memset
CStrings:
+ "acmService"
+ "inSize >= sizeof(acm_command_t)"
+ "performCommandV2"
+ "validateCommand"

```
