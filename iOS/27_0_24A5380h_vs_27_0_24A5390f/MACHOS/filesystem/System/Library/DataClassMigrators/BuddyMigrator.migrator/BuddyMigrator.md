## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`

```diff

-5407.0.0.0.0
-  __TEXT.__text: 0x284c0
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0x1b08
-  __TEXT.__const: 0xd78
+5409.0.0.0.0
+  __TEXT.__text: 0x27edc
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_stubs: 0x2f80
+  __TEXT.__objc_methlist: 0x1a70
+  __TEXT.__const: 0xce8
   __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__objc_methname: 0x4aad
-  __TEXT.__cstring: 0xfeb
-  __TEXT.__oslogstring: 0x2c8d
-  __TEXT.__objc_classname: 0xd7a
-  __TEXT.__objc_methtype: 0xc96
+  __TEXT.__objc_methname: 0x4985
+  __TEXT.__cstring: 0xfc5
+  __TEXT.__oslogstring: 0x2c11
+  __TEXT.__objc_classname: 0xcea
+  __TEXT.__objc_methtype: 0xcd4
   __TEXT.__dlopen_cstrs: 0x2ac
-  __TEXT.__constg_swiftt: 0xa0c
-  __TEXT.__swift5_typeref: 0xb4e
+  __TEXT.__constg_swiftt: 0x998
+  __TEXT.__swift5_typeref: 0xac0
+  __TEXT.__swift5_reflstr: 0x486
+  __TEXT.__swift5_fieldmd: 0x578
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x4ba
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift5_fieldmd: 0x5d8
   __TEXT.__swift5_capture: 0x3cc
-  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x84
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x88
-  __TEXT.__unwind_info: 0xbe0
+  __TEXT.__unwind_info: 0xbc8
   __TEXT.__eh_frame: 0xdfc
-  __DATA_CONST.__const: 0x1078
+  __DATA_CONST.__const: 0x1068
   __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x870
+  __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0x480
-  __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x38b8
-  __DATA.__objc_selrefs: 0x10a8
+  __DATA_CONST.__auth_ptr: 0x180
+  __DATA.__objc_const: 0x3748
+  __DATA.__objc_selrefs: 0x1078
   __DATA.__objc_ivar: 0x110
-  __DATA.__objc_data: 0x1828
-  __DATA.__data: 0x10c0
+  __DATA.__objc_data: 0x1738
+  __DATA.__data: 0x1018
   __DATA.__bss: 0x650
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SetupAssistantPane.framework/SetupAssistantPane
   - /System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport
-  - /System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI
   - /System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 918
+  Functions: 906
   Symbols:   416
-  CStrings:  1254
+  CStrings:  1239
 
CStrings:
+ "firstSupportedOSReleaseVersionForThisDevice"
- "BYRunState"
- "BuddyMigrator.NewFeaturesFlowManager"
- "BuddyMigrator: Queueing mini-buddy to show new features"
- "New Feature video was skipped, updating chronicle record."
- "_TtC13BuddyMigrator22NewFeaturesFlowManager"
- "_TtP13BuddyMigrator26NewFeaturesFlowManagerType_"
- "_shouldLaunchForNewFeaturesUpsell"
- "hasCompletedInitialRun"
- "initWithChronicle:runState:"
- "lastSeenVersion"
- "needsToRun"
- "newFeaturesFlowHandler"
- "recordFlowWasSkippedIfNeeded"
- "runState"
- "setProductVersion:forFeature:"
- "updatePresentedKey:"
```
