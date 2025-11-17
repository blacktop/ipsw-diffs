## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5381.1.4.0.0
-  __TEXT.__text: 0x17924
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x20c0
+5381.2.2.0.0
+  __TEXT.__text: 0x17c00
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_stubs: 0x20e0
   __TEXT.__objc_methlist: 0x11e0
-  __TEXT.__const: 0x5b8
-  __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__objc_methname: 0x2f18
-  __TEXT.__cstring: 0x1478
-  __TEXT.__oslogstring: 0x217e
-  __TEXT.__objc_classname: 0x252
+  __TEXT.__const: 0x590
+  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__objc_methname: 0x2f23
+  __TEXT.__cstring: 0x1441
+  __TEXT.__oslogstring: 0x2228
+  __TEXT.__objc_classname: 0x25d
   __TEXT.__objc_methtype: 0x45c
-  __TEXT.__dlopen_cstrs: 0x202
-  __TEXT.__constg_swiftt: 0x468
-  __TEXT.__swift5_typeref: 0x608
+  __TEXT.__dlopen_cstrs: 0x260
+  __TEXT.__constg_swiftt: 0x424
+  __TEXT.__swift5_typeref: 0x61b
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x25d
+  __TEXT.__swift5_reflstr: 0x246
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_fieldmd: 0x2a4
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift5_fieldmd: 0x288
   __TEXT.__swift5_capture: 0x20c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__unwind_info: 0x750
   __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0xa98
+  __DATA_CONST.__const: 0xab0
   __DATA_CONST.__cfstring: 0xaa0
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2290
-  __DATA.__objc_selrefs: 0xbf8
+  __DATA.__objc_const: 0x2248
+  __DATA.__objc_selrefs: 0xc00
   __DATA.__objc_ivar: 0xd0
-  __DATA.__objc_data: 0xd60
-  __DATA.__data: 0x6d8
-  __DATA.__bss: 0x180
+  __DATA.__objc_data: 0xc98
+  __DATA.__data: 0x700
+  __DATA.__bss: 0x190
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AFB65062-4CD6-3453-915B-AD629BB038EC
-  Functions: 574
-  Symbols:   350
-  CStrings:  1003
+  UUID: A757EE42-78E2-31B3-8FC6-C1DC9083F7F3
+  Functions: 575
+  Symbols:   353
+  CStrings:  1008
 
Symbols:
+ _OBJC_CLASS_$_BYRunState
+ _dlerror
+ _dlsym
CStrings:
+ "Attempting to migrate FeaturesShowcasePresented key from OnBoardingCompleted"
+ "BYRunState"
+ "Migrating FeaturesShowcasePresented key from OnBoardingCompleted"
+ "New Feature video was skipped, updating chronicle record."
+ "Removing OnBoardingCompleted key from the chronicle"
+ "_migrateSolariumOnBoardingToNewFeatureShowcase"
+ "hasCompletedInitialRun"
+ "initWithChronicle:featureFlags:runState:"
+ "kCCSkipKeyAgeAssurance"
+ "recordFlowWasSkippedIfNeeded"
+ "runState"
+ "skipKey"
+ "softlink:r:path:/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary"
- "BuddyMigrator.SolariumOnBoardingManager"
- "BuddyMigrator: Queueing mini-buddy for user onboarding"
- "User onboarding was completed"
- "_TtC13BuddyMigrator25SolariumOnBoardingManager"
- "_shouldLaunchMiniBuddyForOnBoarding"
- "initWithChronicle:featureFlags:"
- "recordUserWasOnBoardedToSolarium"
- "shouldLaunchToOnBoardUserToSolarium"

```
