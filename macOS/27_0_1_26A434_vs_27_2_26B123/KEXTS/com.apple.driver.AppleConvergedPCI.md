## com.apple.driver.AppleConvergedPCI

> `com.apple.driver.AppleConvergedPCI`

```diff

-197.0.0.0.0
+197.40.2.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x6819
-  __TEXT_EXEC.__text: 0x3d190
+  __TEXT.__cstring: 0x682d
+  __TEXT_EXEC.__text: 0x3d27c
   __TEXT_EXEC.__auth_stubs: 0x6e0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0
   __DATA.__bss: 0x5
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x6f18
+  __DATA_CONST.__const: 0x6f28
   __DATA_CONST.__kalloc_type: 0x1380
   __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x118
-  Functions: 1098
-  Symbols:   1680
-  CStrings:  899
+  Functions: 1100
+  Symbols:   1682
+  CStrings:  900
 
Symbols:
+ __ZN24AppleConvergedIPCControl24handleAFLinkTimeoutGatedEv
+ __ZN24AppleConvergedIPCControl24handleAFLinkTimeoutGatedEv_vfpthunk_
+ __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2779
+ __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2803
+ __ZZN24AppleConvergedIPCControl20pciMessageThreadCallEPvS0_E21kalloc_type_view_2820
- __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2768
- __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2792
- __ZZN24AppleConvergedIPCControl20pciMessageThreadCallEPvS0_E21kalloc_type_view_2809
Functions:
~ __ZN24AppleConvergedIPCControl15providerMessageEPvjP9IOServiceS0_m : 1988 -> 2108
+ __ZN24AppleConvergedIPCControl19handleTimeSyncGatedEPy_vfpthunk_
+ __ZN24AppleConvergedIPCControl24handleAFLinkTimeoutGatedEv
CStrings:
+ "kACIPCAFLinkTimeout"
```
