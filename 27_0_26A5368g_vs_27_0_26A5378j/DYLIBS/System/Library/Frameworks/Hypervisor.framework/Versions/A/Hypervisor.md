## Hypervisor

> `/System/Library/Frameworks/Hypervisor.framework/Versions/A/Hypervisor`

```diff

-  __TEXT.__text: 0x84960
+  __TEXT.__text: 0x84a9c
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x557b
   __TEXT.__gcc_except_tab: 0x2dfc
   __TEXT.__cstring: 0x286e
   __TEXT.__oslogstring: 0x9b
-  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__unwind_info: 0x1c10
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2468
-  Symbols:   3278
+  Functions: 2478
+  Symbols:   3289
   CStrings:  672
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table33
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _ZN2Hv4Vcpu20handle_msr_trap_exitEb
+ _ZN2Hv4Vcpu28get_general_purpose_registerEj
+ _ZN2Hv4Vcpu28set_general_purpose_registerEjy
+ _ZThn8_N2Hv4Vcpu28get_general_purpose_registerEj
+ _ZThn8_N2Hv4Vcpu28set_general_purpose_registerEjy
+ __ZN2Hv4Vcpu22set_extension_registerE13_hv_ext_reg_ty
+ __hv_vcpu_set_ext_reg
- GCC_except_table32

```
