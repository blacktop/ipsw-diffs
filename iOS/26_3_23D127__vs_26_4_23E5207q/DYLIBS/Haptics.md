## Haptics

> `/System/Library/PrivateFrameworks/Haptics.framework/Haptics`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x3680
-  __TEXT.__auth_stubs: 0x690
+33.500.0.0.0
+  __TEXT.__text: 0x33a4
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0xb6
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__cstring: 0x76b
+  __TEXT.__gcc_except_tab: 0x3b0
+  __TEXT.__cstring: 0x750
   __TEXT.__oslogstring: 0x212
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__unwind_info: 0x208
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x166
   __TEXT.__objc_methtype: 0x69

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0xa8
-  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__objc_const: 0xb8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63F0B879-BA4A-30E8-AC72-2130BEC51BB6
-  Functions: 57
-  Symbols:   420
-  CStrings:  164
+  UUID: FC54203C-84CF-3443-AB4F-AEF22AEEFB2F
+  Functions: 58
+  Symbols:   424
+  CStrings:  153
 
Symbols:
+ GCC_except_table0
+ GCC_except_table3
+ GCC_except_table7
+ _CAVerboseAbort
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __ZN5caulk5build6detail8get_kindEv
+ __ZN5caulk7product24full_hardware_model_nameEv
+ __ZN5caulk7product25short_hardware_model_nameEv
+ __ZN5caulk8platform12process_nameEi
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__117__call_once_proxyB9foe210106INS_5tupleIJOZL12logSubsystemvE3$_0EEEEEvPv
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x23
- GCC_except_table11
- GCC_except_table21
- GCC_except_table27
- GCC_except_table8
- _CFStringAppendCString
- __ZN10CACFStringaSERKS_
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZL12logSubsystemvE3$_0EEEEEvPv
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- _kCFBooleanTrue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x8
- _perror
- _sysctl
- _sysctlbyname
CStrings:
+ "@@ Strips Jan 26 2026 10:40:44"
- "@@ Strips Jan 16 2026 16:04:26"
- "AP"
- "DEV"
- "ap"
- "dev"
- "hw.model"
- "m"
- "u"

```
