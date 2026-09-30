## com.apple.driver.AppleSPU

> `com.apple.driver.AppleSPU`

```diff

   __TEXT.__cstring: 0x4e2f
   __TEXT.__os_log: 0xb12
   __TEXT.__const: 0x248
-  __TEXT_EXEC.__text: 0x42da4
+  __TEXT_EXEC.__text: 0x42e0c
   __TEXT_EXEC.__auth_stubs: 0xbc0
   __DATA.__data: 0x908
   __DATA.__common: 0x8f8

   __DATA_CONST.__kalloc_var: 0x320
   __DATA_CONST.__auth_got: 0x5e0
   __DATA_CONST.__got: 0x1c0
-  Functions: 2118
+  Functions: 2119
   Symbols:   3395
   CStrings:  885
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN22AppleSPUHIDEventDriver9copyEventEjP10IOHIDEventj
- __ZN16IOHIDEventDriver9copyEventEjP10IOHIDEventj
Functions:
+ __ZN22AppleSPUHIDEventDriver9copyEventEjP10IOHIDEventj
~ __ZL13IsOSDataEmptyP6OSData : 164 -> 148
~ __ZN17AppleSPUHIDDevice25unregisterUserClientGatedEP27AppleSPUHIDDeviceUserClientm : 156 -> 168
~ __ZN17AppleSPUHIDDriver27copyEventForAonBufferClientEP8OSObjectjPv : 748 -> 736
~ __ZN8AppleSPU13_asyncMessageEPvS0_ : 1792 -> 1808
~ _hexdump : 672 -> 680

```
