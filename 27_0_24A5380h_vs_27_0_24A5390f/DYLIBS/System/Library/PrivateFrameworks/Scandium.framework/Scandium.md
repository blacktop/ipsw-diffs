## Scandium

> `/System/Library/PrivateFrameworks/Scandium.framework/Scandium`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x312e4
+96.0.0.0.0
+  __TEXT.__text: 0x31398
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__const: 0x3b5c
-  __TEXT.__gcc_except_tab: 0x2854
-  __TEXT.__oslogstring: 0xc70
+  __TEXT.__const: 0x3b64
+  __TEXT.__gcc_except_tab: 0x2850
+  __TEXT.__oslogstring: 0xcb3
   __TEXT.__cstring: 0x2202
   __TEXT.__unwind_info: 0xf70
   __TEXT.__objc_stubs: 0x0

   __AUTH_CONST.__cfstring: 0x1300
   __AUTH_CONST.__objc_const: 0x260
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x2c
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 785
-  Symbols:   1265
-  CStrings:  497
+  Functions: 786
+  Symbols:   1264
+  CStrings:  498
 
Symbols:
- __ZNSt3__16__sortIRNS_6__lessIffEEPfEEvT0_S5_T_
Functions:
~ __ZN8Scandium11sort_medianEPKfi : 420 -> 424
~ __ZN8Scandium11ScandiumPPG19calc_ppg_ac_metricsEPKfiPfS3_ : 708 -> 744
~ __ZN8Scandium11ScandiumPPG25scandium_spo2_processor_t11compute_ppgEv : 668 -> 732
~ __ZN8Scandium11ScandiumPPG25scandium_spo2_processor_t11compute_bgaERNS0_7beats_tE : 2260 -> 2268
+ __ZN8Scandium11ScandiumPPG25scandium_spo2_processor_t11compute_ppgEv.cold.1
CStrings:
+ "scandium green average: green_divisor is zero, no valid green path"
```
