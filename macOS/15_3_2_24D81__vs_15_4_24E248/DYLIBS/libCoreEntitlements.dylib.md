## libCoreEntitlements.dylib

> `/usr/lib/libCoreEntitlements.dylib`

```diff

-60.0.0.0.0
-  __TEXT.__text: 0x9904
+69.100.2.0.0
+  __TEXT.__text: 0x7e5c
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__cstring: 0x1168
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__cstring: 0x12a7
+  __TEXT.__gcc_except_tab: 0x1f4
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_methname: 0x165
   __TEXT.__objc_stubs: 0x260
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __AUTH_CONST.__auth_got: 0x168

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97BA470F-1660-3BA6-B136-7DCC9EBCFBB0
-  Functions: 111
-  Symbols:   206
-  CStrings:  147
+  UUID: 2F910EB8-C015-33D2-A802-A855BA7042B7
+  Functions: 109
+  Symbols:   223
+  CStrings:  162
 
Symbols:
+ GCC_except_table91
+ GCC_except_table94
+ GCC_except_table96
+ GCC_except_table98
+ _CEStringBufferAppendN
+ __ZNKSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19CESerializedElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___der_vm_iterate_count_block_invoke
+ __block_descriptor_tmp.173
+ __block_descriptor_tmp.7
+ _count_keys
+ _der_decode_boolean
+ _der_decode_entitlements
+ _der_decode_number
+ _der_decode_numeric_string
+ _der_decode_string
+ _der_decode_utc_time
+ _der_validate_array
+ _der_vm_container_from_context
+ _der_vm_execute_match_integer
+ _der_vm_execute_match_string_prefix
+ _der_vm_iterate_count
+ _xml_size_string
- GCC_except_table76
- GCC_except_table79
- GCC_except_table80
- GCC_except_table82
- __ZNKSt3__16vectorI19CESerializedElementNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __block_descriptor_tmp.163
CStrings:
+ "&amp;"
+ "&apos;"
+ "&gt;"
+ "&lt;"
+ "&quot;"
+ "Entitlements element not allowed"
+ "UTC Time element not allowed"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown numeric string encoding"
+ "der_decode_entitlements"
+ "der_decode_numeric_string"
+ "der_decode_utc_time"
+ "der_vm_container_from_context"
+ "numeric string element not allowed"

```
