## com.apple.driver.AppleANELoadBalancer

> `com.apple.driver.AppleANELoadBalancer`

```diff

-9.512.0.0.0
-  __TEXT.__cstring: 0xcca
-  __TEXT.__os_log: 0x3535
+9.512.1.0.0
+  __TEXT.__cstring: 0xceb
+  __TEXT.__os_log: 0x3613
   __TEXT.__const: 0x45
-  __TEXT_EXEC.__text: 0xe2ec
+  __TEXT_EXEC.__text: 0xe3c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x1d4
-  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x6c98
   __DATA_CONST.__kalloc_type: 0x440
+  __DATA_CONST.__kalloc_var: 0x140
   Functions: 448
-  Symbols:   1180
-  CStrings:  321
+  Symbols:   1189
+  CStrings:  323
 
Symbols:
+ _IOFreeTypeVarImpl
+ _IOMallocTypeVarImpl
+ __ZZN15ANEClientDevice13programCreateEP23ANEProgramParamsWrapperE11_os_log_fmt_2
+ __ZZN15ANEClientDevice13programCreateEP23ANEProgramParamsWrapperE20kalloc_type_view_377
+ __ZZN15ANEClientDevice13programCreateEP23ANEProgramParamsWrapperE20kalloc_type_view_391
+ __ZZN15ANEClientDevice21programCreateInstanceEP23ANEProgramParamsWrapperE11_os_log_fmt_2
+ __ZZN15ANEClientDevice21programCreateInstanceEP23ANEProgramParamsWrapperE20kalloc_type_view_501
+ __ZZN15ANEClientDevice21programCreateInstanceEP23ANEProgramParamsWrapperE20kalloc_type_view_515
+ _memmove
Functions:
~ __ZN15ANEClientDevice13programCreateEP23ANEProgramParamsWrapper : 916 -> 1028
~ __ZN15ANEClientDevice21programCreateInstanceEP23ANEProgramParamsWrapper : 960 -> 1060
CStrings:
+ "[ERROR] ANELB: %s: ANEUserClient::%s failed to allocate kernel-private ANEProgramCreateArgsOutput (%zu bytes)\n"
+ "site.ANEProgramCreateArgsOutput"
```
