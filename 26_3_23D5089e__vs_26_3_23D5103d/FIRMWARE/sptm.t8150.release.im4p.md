## sptm.t8150.release.im4p

> `sptm.t8150.release.im4p`

```diff

-611.80.31.0.0
-  __TEXT.__cstring: 0x11705
+611.80.35.0.0
+  __TEXT.__cstring: 0x117a3
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x73e0
   __LATE_CONST.__late_const: 0x718c8
-  __TEXT_EXEC.__text: 0x59aa8
+  __TEXT_EXEC.__text: 0x59ee4
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x60a8
   __DATA.__common: 0x6208
   __BOOTDATA.__data: 0x14000
-  UUID: E6165125-3162-37FF-AEDF-153907F20B11
+  UUID: 0401F7CC-45B6-30BE-B9C2-8F7A8FC8D756
   Functions: 375
   Symbols:   1
-  CStrings:  2222
+  CStrings:  2226
 
Functions:
~ sub_fffffff0270ab46c : 1000 -> 1064
~ sub_fffffff0270ac2f0 -> sub_fffffff0270ac330 : 308 -> 748
~ sub_fffffff0270aed48 -> sub_fffffff0270aef40 : 4372 -> 4520
~ sub_fffffff0270e3184 -> sub_fffffff0270e3410 : 2468 -> 2900
~ sub_fffffff0270eda64 -> sub_fffffff0270edea0 : 76 -> 80
CStrings:
+ "%s: FTE %p should be held exclusive by sptm_retype()"
+ "%s: Only CPU pages may need a GMMU TLBI on retype"
+ "1365"
+ "SPTM-611.80.35|2025-12-20:15:51:08.815688|"
+ "issue-gmmu-tlbis-at-retype"
+ "perform_gmmu_tlbi_if_needed"
- "1364"
- "SPTM-611.80.31|2025-12-04:22:40:29.400392|"

```
