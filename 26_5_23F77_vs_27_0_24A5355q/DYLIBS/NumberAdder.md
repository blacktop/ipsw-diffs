## NumberAdder

> `/System/Library/PrivateFrameworks/NumberAdder.framework/NumberAdder`

```diff

 5.0.0.0.0
-  __TEXT.__text: 0xe30
-  __TEXT.__auth_stubs: 0x310
+  __TEXT.__text: 0xdd0
   __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0xa9
-  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__cstring: 0x149
   __TEXT.__oslogstring: 0xdf
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x13f
-  __TEXT.__objc_methtype: 0x142
-  __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x70
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0xf0
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FF76E53-6822-3A92-8A2A-39248F450A63
-  Functions: 34
-  Symbols:   179
-  CStrings:  41
+  UUID: 46F1A487-1BD0-3D63-8E47-C8BBC5F9D05F
+  Functions: 35
+  Symbols:   180
+  CStrings:  15
 
Symbols:
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table33
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__110unique_ptrI12CLConnection19CLConnectionDeleterE5resetB9fqe220100EPS1_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__112construct_atB9fqe220100I19CLConnectionMessageJRA28_KcRP12NSDictionaryEPS1_EEPT_SA_DpOT0_
+ __ZNSt3__115allocate_sharedB9fqe220100I19CLConnectionMessageNS_9allocatorIS1_EEJRA28_KcRP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220100Ev
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9fqe220100IJRA28_KcRP12NSDictionaryES3_Li0EEES3_DpOT_
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
- GCC_except_table21
- GCC_except_table24
- GCC_except_table26
- GCC_except_table32
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__110unique_ptrI12CLConnection19CLConnectionDeleterE5resetB9nqe210106EPS1_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112construct_atB9nqe210106I19CLConnectionMessageJRA28_KcRP12NSDictionaryEPS1_EEPT_SA_DpOT0_
- __ZNSt3__115allocate_sharedB9nqe210106I19CLConnectionMessageNS_9allocatorIS1_EEJRA28_KcRP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9nqe210106IJRA28_KcRP12NSDictionaryES3_Li0EEES3_DpOT_
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- _memcpy
CStrings:
- ".cxx_construct"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@16@0:8"
- "@32@0:8{unique_ptr<CLConnection, CLConnectionDeleter>={?=^{CLConnection}}}16@24"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionQueue"
- "_connection"
- "_connectionQueue"
- "connectionQueue"
- "copy"
- "dealloc"
- "dictionaryWithObjects:forKeys:count:"
- "handleMessage:"
- "init"
- "initWithConnection:onQueue:"
- "intValue"
- "numberOne:numberTwo:withCompletionHandler:"
- "numberWithInt:"
- "setConnectionQueue:"
- "setup"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8i16i20@?24"
- "v32@0:8{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}16"
- "{unique_ptr<CLConnection, CLConnectionDeleter>=\"\"{?=\"__ptr_\"^{CLConnection}}}"

```
