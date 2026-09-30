## AppleLatticeSupport

> `/System/Library/PrivateFrameworks/AppleLatticeSupport.framework/AppleLatticeSupport`

```diff

-158.100.8.0.0
-  __TEXT.__text: 0x1120
+158.100.10.0.0
+  __TEXT.__text: 0x1200
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x80
+  __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__cstring: 0x245
+  __TEXT.__cstring: 0x29c
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x194
+  __TEXT.__objc_methname: 0x1c9
   __TEXT.__objc_methtype: 0x102
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x188

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CE129E1-DCD0-3A9C-93CC-2C61CAEA0103
-  Functions: 25
-  Symbols:   147
-  CStrings:  81
+  UUID: A3D3FAC3-ACE4-3CB1-B87D-AEA349763161
+  Functions: 27
+  Symbols:   151
+  CStrings:  85
 
Symbols:
+ -[AppleLatticeServiceRef addCarrierLocalInterface]
+ -[AppleLatticeServiceRef removeCarrierLocalInterface]
+ GCC_except_table11
+ GCC_except_table20
+ GCC_except_table23
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__110unique_ptrIN12_GLOBAL__N_113LatticeClientENS_14default_deleteIS2_EEE5resetB9nqe210106EPS2_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- GCC_except_table18
- GCC_except_table21
- GCC_except_table9
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__110unique_ptrIN12_GLOBAL__N_113LatticeClientENS_14default_deleteIS2_EEE5resetB9foe210106EPS2_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
CStrings:
+ "Unable to add carrier local interface: %x"
+ "Unable to remove carrier local interface: %x"
+ "addCarrierLocalInterface"
+ "removeCarrierLocalInterface"

```
