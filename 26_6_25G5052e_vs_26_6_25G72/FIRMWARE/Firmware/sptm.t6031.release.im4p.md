## sptm.t6031.release.im4p

> `Firmware/sptm.t6031.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

-611.160.18.0.0
-  __TEXT.__cstring: 0x10deb
+611.161.3.0.0
+  __TEXT.__cstring: 0x10ed7
   __TEXT.__const: 0xa80
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x5838
   __LATE_CONST.__late_const: 0x7c4b0
-  __TEXT_EXEC.__text: 0x589b4
+  __TEXT_EXEC.__text: 0x58ac8
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18

   __BOOTDATA.__data: 0x14000
   Functions: 359
   Symbols:   1
-  CStrings:  2130
+  CStrings:  2134
 
Functions:
~ sub_fffffff0270cbac8 : 872 -> 1036
~ sub_fffffff0270d2404 -> sub_fffffff0270d24a8 : 836 -> 948
~ sub_fffffff0270f8988 -> sub_fffffff0270f8a9c : 56 -> 52
CStrings:
+ "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
+ "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yCgSDZ/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yCgSDZ/Sources/SPTM/sptm/core/sptm_hibentry.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yCgSDZ/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
+ "SPTM-611.161.3|2026-07-11:14:35:03.433987|"
+ "t8110dart_verify_sid_config"
+ "t8110dart_verify_sid_shadow_config"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KvEKdI/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KvEKdI/Sources/SPTM/sptm/core/sptm_hibentry.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KvEKdI/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
- "SPTM-611.160.18|2026-06-17:23:54:20.173315|"
```
