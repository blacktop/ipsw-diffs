## sptm.t8112.release.im4p

> `sptm.t8112.release.im4p`

```diff

-611.80.31.0.0
-  __TEXT.__cstring: 0x100d4
+611.80.35.0.0
+  __TEXT.__cstring: 0x10172
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x6f20
   __LATE_CONST.__late_const: 0x71870
-  __TEXT_EXEC.__text: 0x53d68
+  __TEXT_EXEC.__text: 0x541a8
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x5fa8
   __DATA.__common: 0x7688
   __BOOTDATA.__data: 0x14000
-  UUID: 88B6D06D-6EF6-3626-96F7-340B314393F2
+  UUID: 46447EF2-38B3-35DC-B46B-C4A599D0AAE0
   Functions: 344
   Symbols:   1
-  CStrings:  2038
+  CStrings:  2042
 
Functions:
~ sub_fffffff0270aaf5c : 980 -> 1044
~ sub_fffffff0270abd2c -> sub_fffffff0270abd6c : 308 -> 748
~ sub_fffffff0270ae3d0 -> sub_fffffff0270ae5c8 : 3704 -> 3852
~ sub_fffffff0270de50c -> sub_fffffff0270de798 : 1720 -> 2156
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
