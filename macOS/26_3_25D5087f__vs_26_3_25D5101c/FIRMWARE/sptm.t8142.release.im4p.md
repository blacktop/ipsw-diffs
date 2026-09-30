## sptm.t8142.release.im4p

> `sptm.t8142.release.im4p`

```diff

-611.80.31.0.0
-  __TEXT.__cstring: 0x117e7
+611.80.35.0.0
+  __TEXT.__cstring: 0x11885
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x73e0
   __LATE_CONST.__late_const: 0x71948
-  __TEXT_EXEC.__text: 0x5904c
+  __TEXT_EXEC.__text: 0x59488
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x60a8
   __DATA.__common: 0xa308
   __BOOTDATA.__data: 0x14000
-  UUID: AAB39238-2F24-3038-9617-AB8561E0F10D
+  UUID: A9552431-0DBA-3BED-BC62-DC9172337DD2
   Functions: 375
   Symbols:   1
-  CStrings:  2222
+  CStrings:  2226
 
Functions:
~ sub_fffffff0270aa89c : 1000 -> 1064
~ sub_fffffff0270ab720 -> sub_fffffff0270ab760 : 308 -> 748
~ sub_fffffff0270ae178 -> sub_fffffff0270ae370 : 4372 -> 4520
~ sub_fffffff0270e2728 -> sub_fffffff0270e29b4 : 2468 -> 2900
~ sub_fffffff0270ed008 -> sub_fffffff0270ed444 : 72 -> 76
CStrings:
+ "%s: FTE %p should be held exclusive by sptm_retype()"
+ "%s: Only CPU pages may need a GMMU TLBI on retype"
+ "/AppleInternal/Library/BuildRoots/4~CE7tugBgg-06NcKTGmZp0MTd-1Nj3vAc6Rc0BT4/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
+ "/AppleInternal/Library/BuildRoots/4~CE7tugBgg-06NcKTGmZp0MTd-1Nj3vAc6Rc0BT4/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/core/sptm_hibentry.c"
+ "/AppleInternal/Library/BuildRoots/4~CE7tugBgg-06NcKTGmZp0MTd-1Nj3vAc6Rc0BT4/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
+ "1365"
+ "SPTM-611.80.35|2025-12-20:15:31:54.349430|"
+ "issue-gmmu-tlbis-at-retype"
+ "perform_gmmu_tlbi_if_needed"
- "/AppleInternal/Library/BuildRoots/4~CDx-ugD64TjRntq8jI33kzoGGqde7vrf0none1g/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
- "/AppleInternal/Library/BuildRoots/4~CDx-ugD64TjRntq8jI33kzoGGqde7vrf0none1g/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/core/sptm_hibentry.c"
- "/AppleInternal/Library/BuildRoots/4~CDx-ugD64TjRntq8jI33kzoGGqde7vrf0none1g/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
- "1364"
- "SPTM-611.80.31|2025-12-04:21:57:46.084055|"

```
