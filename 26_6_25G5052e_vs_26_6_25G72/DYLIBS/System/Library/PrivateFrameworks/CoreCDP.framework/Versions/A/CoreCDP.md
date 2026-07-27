## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/CoreCDP`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-416.600.9.0.0
-  __TEXT.__text: 0x55c6c
-  __TEXT.__auth_stubs: 0xe90
+416.600.13.0.0
+  __TEXT.__text: 0x55f54
+  __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_methlist: 0x3a44
-  __TEXT.__const: 0x13a4
+  __TEXT.__const: 0x1414
   __TEXT.__gcc_except_tab: 0x12f0
   __TEXT.__oslogstring: 0x919c
-  __TEXT.__cstring: 0x60ba
+  __TEXT.__cstring: 0x6118
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1688
+  __TEXT.__unwind_info: 0x1698
   __TEXT.__objc_classname: 0x71e
   __TEXT.__objc_methname: 0x9142
   __TEXT.__objc_methtype: 0x1c0f
   __TEXT.__objc_stubs: 0x4f00
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x1e48
+  __DATA_CONST.__const: 0x1e70
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x1910
-  __AUTH_CONST.__cfstring: 0x3ca0
+  __AUTH_CONST.__cfstring: 0x3d40
   __AUTH_CONST.__objc_const: 0x87e8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x1118
+  __DATA.__data: 0x1148
   __DATA.__bss: 0xf9
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1040

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2385
-  Symbols:   4601
-  CStrings:  3196
+  Functions: 2392
+  Symbols:   4621
+  CStrings:  3201
 
Symbols:
+ _CFArrayContainsValue
+ ___der_key_group_seed_generation
+ ___der_key_group_seed_kcv
+ ___der_key_group_seed_wrapping_type
+ ___der_key_group_user_count
+ ___der_key_vek_group_seed_generation
+ ___der_key_volume_bag_vek_cache_status
+ _aks_unlock_bag_with_options
+ _der_key_group_seed_generation
+ _der_key_group_seed_kcv
+ _der_key_group_seed_wrapping_type
+ _der_key_group_user_count
+ _der_key_vek_group_seed_generation
+ _der_key_volume_bag_vek_cache_status
+ _kAKSInternalInfoGroupSeedGeneration
+ _kAKSInternalInfoGroupSeedKCV
+ _kAKSInternalInfoGroupSeedWrappingType
+ _kAKSInternalInfoGroupUserCount
+ _kAKSInternalInfoVolumeBagVEKCacheStatus
+ _pdk_generate
+ aks_se_get_reset_sig
- _OUTLINED_FUNCTION_89
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EU55BS/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "GroupSeedGeneration"
+ "GroupSeedKCV"
+ "GroupSeedWrappingType"
+ "GroupUserCount"
+ "VolumeBagVEKCacheStatus"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PengPR/Sources/AppleKeyStore_libs/shared_crypto.c"
```
