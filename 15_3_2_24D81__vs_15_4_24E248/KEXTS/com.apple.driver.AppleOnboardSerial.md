## com.apple.driver.AppleOnboardSerial

> `com.apple.driver.AppleOnboardSerial`

```diff

-201.0.0.0.0
-  __TEXT.__cstring: 0x1906
-  __TEXT.__const: 0x68
-  __TEXT_EXEC.__text: 0x12904
+203.0.0.0.0
+  __TEXT.__cstring: 0x192e
+  __TEXT.__const: 0x88
+  __TEXT_EXEC.__text: 0x12f18
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x2a8
   __DATA.__bss: 0x288
-  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x5618
   __DATA_CONST.__kalloc_type: 0x380
-  UUID: 2DD583E7-F413-306E-A790-82BC28620861
-  Functions: 467
-  Symbols:   1187
-  CStrings:  241
+  __DATA_CONST.__assert: 0x64
+  UUID: E1D46142-4B78-32B2-9B95-5071D3D8D451
+  Functions: 470
+  Symbols:   1197
+  CStrings:  243
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _ZN15IOConditionGate14conditionSleepEyi.cold.1
+ __ZZN15IOConditionGate14conditionSleepEyiE6__desc
+ __ZZN19AppleSimpleUARTSync18dmaCompleteCommandEP22AppleSimpleUARTCommandE6__desc
+ __ZZN19AppleSimpleUARTSync22rxCompleteCommandGatedER22AppleSimpleUARTCommandE6__desc
+ __ZZZN19AppleSimpleUARTSync11enqueueDataEP6__mbufENK3$_0clERS_PP28IOSimpleMbufMemoryDescriptorS1_E6__desc
+ __ZZZN19AppleSimpleUARTSync11enqueueDataEP6__mbufENK3$_0clERS_PP28IOSimpleMbufMemoryDescriptorS1_E6__desc_0
- _Assert
CStrings:
+ "!workLoop->inGate()"
+ "IOConditionGate.cpp"

```
