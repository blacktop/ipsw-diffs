## com.apple.AGXG13G

> `com.apple.AGXG13G`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-360.31.1.0.0
+360.32.1.0.0
   __TEXT.__const: 0x26e4
-  __TEXT.__os_log: 0x126a
+  __TEXT.__os_log: 0x12b5
   __TEXT.__cstring: 0xdd24
-  __TEXT_EXEC.__text: 0xb8724
+  __TEXT_EXEC.__text: 0xb87cc
   __TEXT_EXEC.__auth_stubs: 0x1a50
   __DATA.__data: 0x21f0
   __DATA.__common: 0x10

   __DATA_CONST.__auth_got: 0xd28
   __DATA_CONST.__got: 0x268
   Functions: 2843
-  Symbols:   4498
+  Symbols:   4499
   CStrings:  1808
 
Symbols:
+ __ZZN15AGXCommandQueue24processSharedEventSignalEjybyPK24AGXHardwareKernelCommandE11_os_log_fmt
+ __ZZN9AGXShared11clientCloseEvE20kalloc_type_view_423
+ __ZZN9AGXShared32performanceCounterSamplerControlEP28AGXSPerfCtrSamplerControlRecS1_E20kalloc_type_view_808
- __ZZN9AGXShared11clientCloseEvE20kalloc_type_view_428
- __ZZN9AGXShared32performanceCounterSamplerControlEP28AGXSPerfCtrSamplerControlRecS1_E20kalloc_type_view_813
Functions:
~ __ZN15AGXCommandQueue24processSharedEventSignalEjybyPK24AGXHardwareKernelCommand : 336 -> 448
~ __ZN15AGXCommandQueue23processMLEncoderCommandERK24AGXHardwareKernelCommandRK36AGXMLEncoderSharedEventKernelCommand : 192 -> 196
~ __ZN24AGXHardwareKernelCommand16parseAndValidateER21AGXSharedStreamParserS1_ : 1032 -> 1092
~ __ZN36AGXMLEncoderSharedEventKernelCommand16parseAndValidateER21AGXSharedStreamParser : 92 -> 84
CStrings:
+ "Jul 14 2026 21:36:06"
- "Jun 30 2026 21:11:58"
```
