## com.apple.driver.AppleSPMI

> `com.apple.driver.AppleSPMI`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-143.0.1.0.0
+143.0.2.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1efc
+  __TEXT.__cstring: 0x1f06
   __TEXT.__os_log: 0xbc5
-  __TEXT_EXEC.__text: 0xb160
+  __TEXT_EXEC.__text: 0xba40
   __TEXT_EXEC.__auth_stubs: 0x350
   __DATA.__data: 0xc4
   __DATA.__common: 0x38
   __DATA.__bss: 0x8
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x2210
-  __DATA_CONST.__kalloc_type: 0x340
+  __DATA_CONST.__const: 0x2668
+  __DATA_CONST.__kalloc_type: 0x3c0
   __DATA_CONST.__kalloc_var: 0x230
   __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x40
-  Functions: 210
-  Symbols:   677
-  CStrings:  282
+  Functions: 224
+  Symbols:   695
+  CStrings:  283
 
Symbols:
+ __ZN20AppleGen6SPMIHandler10resetQueueEv
+ __ZN20AppleGen6SPMIHandler11initHandlerEP19AppleSPMIControlleryy
+ __ZN20AppleGen6SPMIHandler12resetArbiterEv
+ __ZN20AppleGen6SPMIHandler13createHandlerEP19AppleSPMIControlleryy
+ __ZN20AppleGen6SPMIHandler14clearInterruptEjj
+ __ZN20AppleGen6SPMIHandler14dumpDebugQueueEPcm
+ __ZN20AppleGen6SPMIHandler14getQueueDepthsEPjS0_
+ __ZN20AppleGen6SPMIHandler16getSPMIRegistersEv
+ __ZN20AppleGen6SPMIHandler17dumpFaultCountersEPcm
+ __ZN20AppleGen6SPMIHandler23dumpFaultQueueIrqStatusEPcm
+ __ZN20AppleGen6SPMIHandler30getFaultInterruptNameForVectorEj
+ __ZN20AppleGen6SPMIHandler4freeEv
+ __ZN20AppleGen6SPMIHandlerD0Ev
+ __ZN20AppleGen6SPMIHandlerD1Ev
+ __ZTV20AppleGen6SPMIHandler
+ __ZZN20AppleGen6SPMIHandler30getFaultInterruptNameForVectorEjE12spmiIRQNames
+ __ZZN21IOTypedOperatorsMixinI20AppleGen6SPMIHandlerEdlEPvmE20kalloc_type_view_871
+ __ZZN21IOTypedOperatorsMixinI20AppleGen6SPMIHandlerEnwEmE20kalloc_type_view_871
CStrings:
+ "None-Gen6"
```
