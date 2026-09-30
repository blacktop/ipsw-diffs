## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

-71.60.2.0.0
+71.100.4.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x4320
-  __TEXT_EXEC.__text: 0x13b14
+  __TEXT_EXEC.__text: 0x13b94
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x1400
-  Functions: 204
-  Symbols:   607
+  Functions: 196
+  Symbols:   619
   CStrings:  469
 
Symbols:
+ ACMKernelTransport.cold.1
+ _Z22LDMShouldEnforceParityv.cold.1
+ _Z22LDMShouldEnforceParityv.cold.2
+ _Z22LDMShouldEnforceParityv.cold.3
+ acm_mem_free_data.cold.1
- LibCall_ACMKernelControl.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.2
- LibCall_ACMSetEnvironmentVariable.cold.3
- __isNullOrEqualMem2

```
