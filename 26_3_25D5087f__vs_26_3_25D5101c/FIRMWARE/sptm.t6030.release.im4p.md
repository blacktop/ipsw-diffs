## sptm.t6030.release.im4p

> `sptm.t6030.release.im4p`

```diff

-611.80.31.0.0
-  __TEXT.__cstring: 0x1011b
+611.80.35.0.0
+  __TEXT.__cstring: 0x101b9
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x6f80
   __LATE_CONST.__late_const: 0x718f0
-  __TEXT_EXEC.__text: 0x551b4
+  __TEXT_EXEC.__text: 0x555f4
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x6128
   __DATA.__common: 0xb488
   __BOOTDATA.__data: 0x14000
-  UUID: C7577BF9-B7CE-3CAB-8196-E5FF1190D6F4
+  UUID: B1105BED-60A1-3E73-A08B-50C8B4C4F27B
   Functions: 347
   Symbols:   1
-  CStrings:  2043
+  CStrings:  2047
 
Functions:
~ sub_fffffff0270abc5c : 980 -> 1044
~ sub_fffffff0270aca2c -> sub_fffffff0270aca6c : 308 -> 748
~ sub_fffffff0270af0e0 -> sub_fffffff0270af2d8 : 3704 -> 3852
~ sub_fffffff0270dfb00 -> sub_fffffff0270dfd8c : 1720 -> 2156
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
