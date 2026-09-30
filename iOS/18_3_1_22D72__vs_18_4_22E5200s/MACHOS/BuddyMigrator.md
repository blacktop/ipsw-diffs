## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5355.6.0.0.0
-  __TEXT.__text: 0x12144
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x9ac
-  __TEXT.__const: 0x228
-  __TEXT.__gcc_except_tab: 0x258
-  __TEXT.__objc_methname: 0x23a7
-  __TEXT.__cstring: 0xf21
-  __TEXT.__oslogstring: 0x1968
+5359.4.6.100.0
+  __TEXT.__text: 0x121f8
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_stubs: 0x1c60
+  __TEXT.__objc_methlist: 0xcb0
+  __TEXT.__const: 0x238
+  __TEXT.__gcc_except_tab: 0x29c
+  __TEXT.__objc_methname: 0x25f6
+  __TEXT.__cstring: 0xf61
+  __TEXT.__oslogstring: 0x1988
   __TEXT.__objc_classname: 0x11f
-  __TEXT.__objc_methtype: 0x299
+  __TEXT.__objc_methtype: 0x2c9
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__swift5_typeref: 0x3a9
-  __TEXT.__swift5_fieldmd: 0x160
-  __TEXT.__constg_swiftt: 0x29c
-  __TEXT.__swift5_reflstr: 0x146
+  __TEXT.__swift5_typeref: 0x3fb
+  __TEXT.__swift5_fieldmd: 0x16c
+  __TEXT.__constg_swiftt: 0x2b4
+  __TEXT.__swift5_reflstr: 0x156
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x598
-  __TEXT.__eh_frame: 0x7b0
-  __DATA_CONST.__auth_got: 0x528
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__eh_frame: 0x780
+  __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0x968
   __DATA_CONST.__cfstring: 0xa80
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x19a8
-  __DATA.__objc_selrefs: 0x8e8
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x968
-  __DATA.__data: 0x458
+  __DATA.__objc_const: 0x16f0
+  __DATA.__objc_selrefs: 0xa08
+  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_data: 0x828
+  __DATA.__data: 0x478
   __DATA.__bss: 0x60
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 432
-  Symbols:   328
-  CStrings:  739
+  Functions: 458
+  Symbols:   323
+  CStrings:  757
 
Symbols:
+ _OBJC_CLASS_$_BYDeviceConfiguration
- _BYChronicleKey
- _NSStringFromClass
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x26
- _objc_retain_x28
- _swift_bridgeObjectRelease_n
CStrings:
+ "6"
+ "@\"<_TtP13BuddyMigrator20IntelligenceProvider_>\""
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32@40@48"
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"
+ "IntelligencePresented key found in notBackedUp preferences"
+ "IntelligencePresented key found in preferences"
+ "Migrating IntelligencePresented key to chronicle"
+ "Migrating preference keys"
+ "T@\"<_TtP13BuddyMigrator20IntelligenceProvider_>\",&,N,V_intelligenceManager"
+ "TB,N"
+ "_intelligenceManager"
+ "_migrateIntelligencePresentedKeyToChronicleIfNeeded"
+ "_migratePreferences"
+ "currentConfiguration"
+ "didUpsellAppleIntelligence"
+ "hasCrossedEBoundarySinceCreationForCurrentProductVersion:"
+ "initFromBackedUpPreferences:andNotBackedUpPreferences:"
+ "initWithFeatureFlags:availabilityProvider:stateProvider:preferences:chronicle:"
+ "initWithFeatureFlags:preferences:chronicle:"
+ "intelligenceManager"
+ "isAgeAttestationPhase1Enabled"
+ "isMDMEnrollmentFlowControllerAdoptionEnabled"
+ "persistBackedUpFeaturesInPreferences:andNotBackedFeaturesInPreferences:persistImmediately:"
+ "productVersion"
+ "recordFeatureShown:"
+ "removeRecordForFeature:"
+ "setDidUpsellAppleIntelligence:"
+ "setIntelligenceManager:"
- "5"
- "@48@0:8@16@24@32@40"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"
- "Creating new chronicle..."
- "Migrating intelligence presented preference key"
- "Migrating keys"
- "Unable to read chronicle data; found %@, expected NSDictionary!"
- "_migrateKeys"
- "dictionaryRepresentation"
- "initWithDictionary:"
- "initWithFeatureFlags:availabilityProvider:stateProvider:preferences:"
- "initWithFeatureFlags:preferences:"

```
