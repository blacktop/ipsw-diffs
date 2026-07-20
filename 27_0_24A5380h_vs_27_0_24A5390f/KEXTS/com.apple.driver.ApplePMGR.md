## com.apple.driver.ApplePMGR

> `com.apple.driver.ApplePMGR`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1976.0.8.0.0
-  __TEXT.__cstring: 0xfedb
+1976.0.10.0.0
+  __TEXT.__cstring: 0x1011c
   __TEXT.__const: 0x2b0
-  __TEXT_EXEC.__text: 0x62100
+  __TEXT_EXEC.__text: 0x625fc
   __TEXT_EXEC.__auth_stubs: 0x820
   __DATA.__data: 0x138
   __DATA.__common: 0x5e0

   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0xb9f8
   __DATA_CONST.__kalloc_type: 0xb40
-  __DATA_CONST.__kalloc_var: 0xfa0
+  __DATA_CONST.__kalloc_var: 0xff0
   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2855
+  Functions: 2866
   Symbols:   0
-  CStrings:  1802
+  CStrings:  1810
 
CStrings:
+ "(PerfState)minPerfState < maxPerfStates"
+ "PerfState ApplePMGR::_getPerfDomainCurrentState(PerfDomainID, UInt32)"
+ "_die < _target->getDieCount()"
+ "perfDomain->devicePerfStateRequirements[die]"
+ "site.DeviceIDMask *"
+ "virtual IOReturn ApplePMGRFunctionGetValidPerfState::callFunction(void *, void *, void *)"
+ "virtual bool ApplePMGRFunctionGetValidPerfState::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)"
+ "virtual bool ApplePMGRFunctionSetPerfState::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)"
+ "void ApplePMGR::_updateDevicePerfDomainRequirementsGated(uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
- "PerfState ApplePMGR::_getPerfDomainCurrentState(PerfDomainID)"
```
