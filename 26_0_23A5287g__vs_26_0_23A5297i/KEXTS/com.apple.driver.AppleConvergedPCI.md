## com.apple.driver.AppleConvergedPCI

> `com.apple.driver.AppleConvergedPCI`

```diff

-182.0.0.0.0
+183.0.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x6db2
-  __TEXT_EXEC.__text: 0x401d4
+  __TEXT.__cstring: 0x6e44
+  __TEXT_EXEC.__text: 0x407c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x118
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x48a8
+  __DATA_CONST.__const: 0x48b0
   __DATA_CONST.__kalloc_type: 0x1380
-  UUID: A65E3984-09EB-3763-96D3-808479078CD5
-  Functions: 1083
+  UUID: EF932975-0296-3004-B11D-23A37AEA75EE
+  Functions: 1084
   Symbols:   0
-  CStrings:  910
+  CStrings:  914
 
Functions:
+ sub_fffffff009080908
~ __ZN24AppleConvergedIPCControl5startEP9IOService : 7712 -> 7924
~ __ZN24AppleConvergedIPCControl19linkStateUpFunctionEPyS0_PjS1_ : 348 -> 708
CStrings:
+ "%s::%s: Disable MSI Addr re-write Workaround override : %u\n"
+ "%s::%s: Re-write MSI Address 0x%llx\n"
+ "acipc-pcie-disableMSIAddrRewriteWA"
+ "setMSIAddress"

```
