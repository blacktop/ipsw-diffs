## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-  __TEXT.__text: 0xf5478
-  __TEXT.__objc_methlist: 0xb284
-  __TEXT.__const: 0x1454
-  __TEXT.__cstring: 0x185c4
-  __TEXT.__oslogstring: 0x9227
-  __TEXT.__gcc_except_tab: 0xd10
+  __TEXT.__text: 0xf5c40
+  __TEXT.__objc_methlist: 0xb28c
+  __TEXT.__const: 0x14c4
+  __TEXT.__cstring: 0x1865d
+  __TEXT.__oslogstring: 0x925b
+  __TEXT.__gcc_except_tab: 0x1020
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x3240
+  __TEXT.__unwind_info: 0x3258
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4db8
+  __DATA_CONST.__const: 0x4e10
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d88
+  __DATA_CONST.__objc_selrefs: 0x5d90
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xab0
   __AUTH_CONST.__const: 0x20b0
-  __AUTH_CONST.__cfstring: 0x194c0
+  __AUTH_CONST.__cfstring: 0x19580
   __AUTH_CONST.__objc_const: 0xd740
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0x2300
+  __AUTH.__objc_data: 0x23a0
   __DATA.__objc_ivar: 0x990
-  __DATA.__data: 0xc40
-  __DATA.__bss: 0xc79
+  __DATA.__data: 0xc78
+  __DATA.__bss: 0xc59
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__bss: 0x228
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5782
-  Symbols:   17733
-  CStrings:  7828
+  Functions: 5790
+  Symbols:   17766
+  CStrings:  7841
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ -[MCNotifier sendEnablingRestrictionsChangedNotification]
+ GCC_except_table20
+ _MCEnablingRestrictionsChangedNotification
+ _MCSendEnablingRestrictionsChangedNotification
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
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
CStrings:
+ "GroupSeedGeneration"
+ "GroupSeedKCV"
+ "GroupSeedWrappingType"
+ "GroupUserCount"
+ "Sending enabling restrictions changed notification."
+ "VolumeBagVEKCacheStatus"
+ "com.apple.managedconfiguration.enablingrestrictionschanged"

```
