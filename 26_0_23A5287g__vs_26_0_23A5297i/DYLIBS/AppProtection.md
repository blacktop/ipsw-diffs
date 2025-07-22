## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0xa1160
-  __TEXT.__auth_stubs: 0x1fa0
+43.0.0.0.0
+  __TEXT.__text: 0xa1c50
+  __TEXT.__auth_stubs: 0x1fb0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x16c4
-  __TEXT.__const: 0x4930
-  __TEXT.__oslogstring: 0x3be8
-  __TEXT.__cstring: 0x53cc
+  __TEXT.__objc_methlist: 0x170c
+  __TEXT.__const: 0x4960
+  __TEXT.__oslogstring: 0x3d48
+  __TEXT.__cstring: 0x549c
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0x2d5c
-  __TEXT.__swift5_fieldmd: 0x1e3c
-  __TEXT.__constg_swiftt: 0x3678
-  __TEXT.__swift5_reflstr: 0x1a11
+  __TEXT.__swift5_fieldmd: 0x1e54
+  __TEXT.__constg_swiftt: 0x3688
+  __TEXT.__swift5_reflstr: 0x1a81
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x468
-  __TEXT.__swift5_capture: 0x1800
+  __TEXT.__swift5_capture: 0x1820
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_proto: 0x314
   __TEXT.__swift5_types: 0x27c
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x23f8
-  __TEXT.__eh_frame: 0x2da0
+  __TEXT.__unwind_info: 0x2420
+  __TEXT.__eh_frame: 0x2d78
   __TEXT.__objc_classname: 0x2cc
-  __TEXT.__objc_methname: 0x2552
-  __TEXT.__objc_methtype: 0x758
+  __TEXT.__objc_methname: 0x25d6
+  __TEXT.__objc_methtype: 0x78b
   __TEXT.__objc_stubs: 0x580
   __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab0
+  __DATA_CONST.__objc_selrefs: 0xad0
   __DATA_CONST.__objc_protorefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xfe0
-  __AUTH_CONST.__const: 0x7120
+  __AUTH_CONST.__auth_got: 0xfe8
+  __AUTH_CONST.__const: 0x7210
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x4830
-  __AUTH.__objc_data: 0x22a8
+  __AUTH_CONST.__objc_const: 0x4880
+  __AUTH.__objc_data: 0x22b8
   __AUTH.__data: 0x2420
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x24e8
+  __DATA.__data: 0x24d8
   __DATA.__bss: 0x4790
   __DATA.__common: 0x108
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__data: 0x7d0
+  __DATA_DIRTY.__data: 0x7e0
   __DATA_DIRTY.__bss: 0x2f0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 390A82EB-1C91-3EEA-8D77-DB831C3B781B
-  Functions: 3568
-  Symbols:   3153
-  CStrings:  1421
+  UUID: E2823461-90CA-300A-B701-DBBF2C69BB8C
+  Functions: 3594
+  Symbols:   3181
+  CStrings:  1436
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ ___APGetConnectionWithNameAndActiveCacheWithLock_block_invoke.152
+ ___APGetConnectionWithNameAndActiveCacheWithLock_block_invoke.152.cold.1
+ _block_copy_helper.49
+ _block_copy_helper.83
+ _block_copy_helper.88
+ _block_descriptor.51
+ _block_descriptor.85
+ _block_descriptor.90
+ _block_destroy_helper.50
+ _block_destroy_helper.84
+ _block_destroy_helper.89
+ _objectdestroy.53Tm
- ___APGetConnectionWithNameAndActiveCacheWithLock_block_invoke.147
- ___APGetConnectionWithNameAndActiveCacheWithLock_block_invoke.147.cold.1
- _block_copy_helper.39
- _block_copy_helper.61
- _block_copy_helper.78
- _block_descriptor.41
- _block_descriptor.63
- _block_descriptor.80
- _block_destroy_helper.40
- _block_destroy_helper.62
- _block_destroy_helper.79
- _objectdestroy.37Tm
CStrings:
+ "Checked unlockUnacceptedPrivacyDisclosureApps before first unlock"
+ "Could not fetch viewSubject info proxy for getEffectiveContainerFromServer %@"
+ "Could not fetch viewSubject info proxy for getEffectiveContainerLocalizedNameFromServer %@"
+ "Could not getEffectiveContainerFromServer %@"
+ "Could not getEffectiveContainerLocalizedNameFromServer %@"
+ "effectiveContainer"
+ "effectiveContainerFor:completion:"
+ "effectiveContainerLocalizedName"
+ "effectiveContainerLocalizedNameFor:completion:"
+ "haveUnlockedUnacceptedPrivacyDisclosureApps"
+ "no containing bundle record for viewSubject %{public}s"
+ "unlockUnacceptedPrivacyDisclosureAppsIfNeccesary"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "could not unlock unaccepted privacy disclosure apps on first run: %@"

```
