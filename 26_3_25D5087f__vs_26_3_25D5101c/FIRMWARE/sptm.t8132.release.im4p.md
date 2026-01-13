## sptm.t8132.release.im4p

> `sptm.t8132.release.im4p`

```diff

-611.80.31.0.0
-  __TEXT.__cstring: 0x11466
+611.80.35.0.0
+  __TEXT.__cstring: 0x11504
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x73e0
   __LATE_CONST.__late_const: 0x71930
-  __TEXT_EXEC.__text: 0x59560
+  __TEXT_EXEC.__text: 0x5998c
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x6028
   __DATA.__common: 0x9908
   __BOOTDATA.__data: 0x14000
-  UUID: 7ECB24D5-1B8E-337D-8FFE-EC0D49844C38
+  UUID: 5553FEA4-FF17-3EA7-868E-B63C3B9F6D7C
   Functions: 370
   Symbols:   1
-  CStrings:  2193
+  CStrings:  2197
 
Functions:
~ sub_fffffff0270aa89c : 1016 -> 1080
~ sub_fffffff0270ab748 -> sub_fffffff0270ab788 : 308 -> 744
~ sub_fffffff0270ae1a4 -> sub_fffffff0270ae398 : 4372 -> 4520
~ sub_fffffff0270e3a98 -> sub_fffffff0270e3d20 : 2032 -> 2452
~ sub_fffffff0270ed51c -> sub_fffffff0270ed948 : 68 -> 72
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
