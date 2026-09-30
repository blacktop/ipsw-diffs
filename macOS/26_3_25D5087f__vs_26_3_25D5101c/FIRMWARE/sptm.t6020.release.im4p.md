## sptm.t6020.release.im4p

> `sptm.t6020.release.im4p`

```diff

-611.80.31.0.0
-  __TEXT.__cstring: 0x101bc
+611.80.35.0.0
+  __TEXT.__cstring: 0x1025a
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x6f80
   __LATE_CONST.__late_const: 0x71a80
-  __TEXT_EXEC.__text: 0x5471c
+  __TEXT_EXEC.__text: 0x54b5c
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x6128
   __DATA.__common: 0x16288
   __BOOTDATA.__data: 0x14000
-  UUID: EF843429-C4A0-321F-B7F2-D3801BBADA19
+  UUID: 617E2766-7B5C-38E2-9F7B-EF6B3E899959
   Functions: 350
   Symbols:   1
-  CStrings:  2049
+  CStrings:  2053
 
Functions:
~ sub_fffffff0270aaf5c : 980 -> 1044
~ sub_fffffff0270abd2c -> sub_fffffff0270abd6c : 308 -> 748
~ sub_fffffff0270ae3e0 -> sub_fffffff0270ae5d8 : 3704 -> 3852
~ sub_fffffff0270deec0 -> sub_fffffff0270df14c : 1720 -> 2156
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
