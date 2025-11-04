## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5380.0.0.0.0
-  __TEXT.__text: 0x16fe8
+5381.1.2.0.0
+  __TEXT.__text: 0x17924
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x2060
-  __TEXT.__objc_methlist: 0x1188
+  __TEXT.__objc_stubs: 0x20c0
+  __TEXT.__objc_methlist: 0x11e0
   __TEXT.__const: 0x5b8
-  __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__objc_methname: 0x2e78
-  __TEXT.__cstring: 0x1448
-  __TEXT.__oslogstring: 0x205e
-  __TEXT.__objc_classname: 0x207
+  __TEXT.__gcc_except_tab: 0x2fc
+  __TEXT.__objc_methname: 0x2f18
+  __TEXT.__cstring: 0x1478
+  __TEXT.__oslogstring: 0x217e
+  __TEXT.__objc_classname: 0x252
   __TEXT.__objc_methtype: 0x45c
-  __TEXT.__dlopen_cstrs: 0x1ac
+  __TEXT.__dlopen_cstrs: 0x202
   __TEXT.__constg_swiftt: 0x468
   __TEXT.__swift5_typeref: 0x608
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__unwind_info: 0x738
   __TEXT.__eh_frame: 0x7a8
   __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__got: 0x378
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__const: 0xa98
   __DATA_CONST.__cfstring: 0xaa0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x21e0
-  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_const: 0x2290
+  __DATA.__objc_selrefs: 0xbf8
   __DATA.__objc_ivar: 0xd0
-  __DATA.__objc_data: 0xd10
-  __DATA.__data: 0x678
-  __DATA.__bss: 0x160
+  __DATA.__objc_data: 0xd60
+  __DATA.__data: 0x6d8
+  __DATA.__bss: 0x180
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0C137528-62FB-3BF1-9061-3B44D75DA437
-  Functions: 563
-  Symbols:   347
-  CStrings:  991
+  UUID: EBCEF020-F3C5-3984-A9D6-78302DEE1C97
+  Functions: 574
+  Symbols:   350
+  CStrings:  1003
 
Symbols:
+ _OBJC_CLASS_$_BuddyAgeAssurancePresentationManager
+ _OBJC_METACLASS_$_BuddyAgeAssurancePresentationManager
+ _kCCSkipKeyWiFi
CStrings:
+ "AISAgeAssuranceContext"
+ "AISAgeAssuranceController"
+ "Age assurance runtime dependency does not exit"
+ "BuddyAgeAssurancePresentationManager"
+ "BuddyAgeAssurancePresentationProvider"
+ "BuddyMigrator: Queueing Age Assurance mini-buddy"
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"
+ "Did check whether to present age assurance with result %d error %{public}@"
+ "Returning should present age assurance %d"
+ "Will check whether to present age assurance (only local checks)"
+ "_shouldLaunchMiniBuddyForAgeAssurance"
+ "shouldPresentAgeAssuranceUsingOnlyLocalChecksWithHasCompletedInitialRun:"
+ "shouldPresentAgeAssuranceWithContext:completion:"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"

```
