## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-35.2.2.0.0
-  __TEXT.__text: 0xa12a0
-  __TEXT.__auth_stubs: 0x1f10
+35.2.3.0.0
+  __TEXT.__text: 0xa16c8
+  __TEXT.__auth_stubs: 0x1f20
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0xf98
   __TEXT.__const: 0x3930
-  __TEXT.__oslogstring: 0x34c8
-  __TEXT.__cstring: 0x5014
+  __TEXT.__oslogstring: 0x3518
+  __TEXT.__cstring: 0x5004
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__swift5_typeref: 0x2996
+  __TEXT.__swift5_typeref: 0x29bc
   __TEXT.__swift5_fieldmd: 0x1b10
   __TEXT.__constg_swiftt: 0x317c
   __TEXT.__swift5_reflstr: 0x175f

   __TEXT.__swift5_proto: 0x2b0
   __TEXT.__swift5_types: 0x240
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x2300
-  __TEXT.__eh_frame: 0x2a28
+  __TEXT.__unwind_info: 0x2328
+  __TEXT.__eh_frame: 0x2aa0
   __TEXT.__objc_classname: 0x273
   __TEXT.__objc_methname: 0x2201
   __TEXT.__objc_methtype: 0x6cf

   __DATA_CONST.__objc_selrefs: 0x990
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__auth_ptr: 0x940
+  __AUTH_CONST.__auth_got: 0xfa0
+  __AUTH_CONST.__auth_ptr: 0x930
   __AUTH_CONST.__const: 0x6698
   __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x45b8

   - /System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3388
-  Symbols:   875
-  CStrings:  1298
+  Functions: 3391
+  Symbols:   876
+  CStrings:  1299
 
Symbols:
+ _DMIsMigrationNeeded
CStrings:
+ "Cannot hide a default app"
+ "skipping required settings actions check because migration is in flight"
- "Cannot hide the default browser or mail client"

```
