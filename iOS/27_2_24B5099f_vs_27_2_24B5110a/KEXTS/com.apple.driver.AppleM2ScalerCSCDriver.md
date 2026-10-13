## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-200.67.0.0.0
+200.69.0.0.0
   __TEXT.__const: 0xc3140
-  __TEXT.__cstring: 0x2534c
-  __TEXT_EXEC.__text: 0x13c150
+  __TEXT.__cstring: 0x25390
+  __TEXT_EXEC.__text: 0x13c0b0
   __TEXT_EXEC.__auth_stubs: 0xbd0
   __DATA.__data: 0x22388
   __DATA.__common: 0x2738

   __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10275
+  Functions: 10276
   Symbols:   0
-  CStrings:  3714
+  CStrings:  3715
 
Functions:
~ __ZN27M2ScalerScalingControlMSR2326commitFilters_gatedContextEP18M2ScalerCSCRequestPA3_jPjPPK18FilterCoefficients20VerticalOrHorizontalbS4_S4_S4_ : 1456 -> 1204
+ sub_fffffe000919312c
~ __ZN33IosaPolyphaseScalingPipeUnitMSR2314prepareFiltersEP16pipeUnitExchangeb20VerticalOrHorizontal : 1812 -> 1556
CStrings:
+ "[%s][%s]bin %d phase 16 gain %d != %d (2*%d + COEFFX %#x), err %+d\n"
```
