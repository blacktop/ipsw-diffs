## Setup

> `/Applications/Setup.app/Setup`

```diff

-5347.0.0.0.0
-  __TEXT.__text: 0x1e686c
-  __TEXT.__auth_stubs: 0x2040
-  __TEXT.__objc_stubs: 0x236e0
-  __TEXT.__objc_methlist: 0x14aa0
-  __TEXT.__cstring: 0xdc48
-  __TEXT.__objc_methname: 0x34a11
+5350.3.0.0.0
+  __TEXT.__text: 0x1e8720
+  __TEXT.__auth_stubs: 0x2060
+  __TEXT.__objc_stubs: 0x239e0
+  __TEXT.__objc_methlist: 0x14c50
+  __TEXT.__cstring: 0xdce2
+  __TEXT.__objc_methname: 0x3500b
   __TEXT.__const: 0x1088
-  __TEXT.__constg_swiftt: 0x142c
+  __TEXT.__constg_swiftt: 0x145c
   __TEXT.__swift5_typeref: 0xcd2
-  __TEXT.__swift5_fieldmd: 0x844
+  __TEXT.__swift5_fieldmd: 0x850
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xa70
+  __TEXT.__swift5_reflstr: 0xa9c
   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0xac
-  __TEXT.__objc_classname: 0x32b9
-  __TEXT.__objc_methtype: 0xa179
-  __TEXT.__swift5_capture: 0x790
+  __TEXT.__objc_classname: 0x32e1
+  __TEXT.__objc_methtype: 0xa1b5
+  __TEXT.__swift5_capture: 0x7a0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0xefc0
-  __TEXT.__gcc_except_tab: 0x4d74
+  __TEXT.__oslogstring: 0xf0d9
+  __TEXT.__gcc_except_tab: 0x4e10
   __TEXT.__dlopen_cstrs: 0x10ba
-  __TEXT.__unwind_info: 0x7a18
+  __TEXT.__unwind_info: 0x7aa8
   __TEXT.__eh_frame: 0x1b38
-  __DATA_CONST.__auth_got: 0x1038
+  __DATA_CONST.__auth_got: 0x1048
   __DATA_CONST.__got: 0x1b50
-  __DATA_CONST.__auth_ptr: 0x230
-  __DATA_CONST.__const: 0x5a10
-  __DATA_CONST.__cfstring: 0xa840
-  __DATA_CONST.__objc_classlist: 0xab0
+  __DATA_CONST.__auth_ptr: 0x238
+  __DATA_CONST.__const: 0x5a40
+  __DATA_CONST.__cfstring: 0xa8c0
+  __DATA_CONST.__objc_classlist: 0xab8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x4c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x770
+  __DATA_CONST.__objc_superrefs: 0x778
   __DATA_CONST.__objc_arraydata: 0x3a0
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x427a0
-  __DATA.__objc_selrefs: 0xa488
-  __DATA.__objc_ivar: 0x1984
-  __DATA.__objc_data: 0x8558
-  __DATA.__data: 0x4120
+  __DATA.__objc_const: 0x42ab0
+  __DATA.__objc_selrefs: 0xa580
+  __DATA.__objc_ivar: 0x19b4
+  __DATA.__objc_data: 0x85e0
+  __DATA.__data: 0x4128
   __DATA.__bss: 0x1018
   __DATA.__common: 0x78
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9549
-  Symbols:   1288
-  CStrings:  12780
+  Functions: 9598
+  Symbols:   1291
+  CStrings:  12841
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _dispatch_block_cancel
+ _dispatch_block_perform
CStrings:
+ "\x04\x11\x12\x12\x11k\x19"
+ "@\"<UIViewControllerTransitionCoordinator>\""
+ "@40@0:8q16@24@32"
+ "AMS cache promise did not respond in time. Timing out!"
+ "AMSAccount fetchMedialLinkedAccountDSID force run flag found"
+ "BYStolenDeviceProtectionPreferenceMigrator"
+ "Found: Ignore back button handling key. Ignore back button handling."
+ "Neither postRestoreFromBackup or postSoftwareUpdate are set"
+ "No SDP migration occurred."
+ "SDP preferences updated. didMigrate: %!d(MISSING), didClear: %!d(MISSING). SDP State: %!d(MISSING)"
+ "Sep 30 2024"
+ "T@\"<UIViewControllerTransitionCoordinator>\",&,V_transitionCoordinator"
+ "T@\"BYPreferencesController\",&,N,V_sourcePreferences"
+ "T@\"BYPreferencesController\",&,N,V_targetPreferences"
+ "T@\"UINavigationController\",W,N,V_currentNavigationController"
+ "T@\"UIViewController\",&,N,V_previousViewController"
+ "TB,N,V_initialAnimateLanguageChoiceValue"
+ "TB,N,V_initialDisplayZoomRestartValue"
+ "Tq,N,V_migrationContext"
+ "_clearPreferenceKeyFromSourcePreferences"
+ "_currentNavigationController"
+ "_didClear"
+ "_didMigrate"
+ "_initialAnimateLanguageChoiceValue"
+ "_initialDisplayZoomRestartValue"
+ "_migratePreferenceKeyIfNeeded"
+ "_migrationContext"
+ "_previousViewController"
+ "_sourcePreferences"
+ "_targetPreferences"
+ "_transitionCoordinator"
+ "_updateNavigationBarBackButtonIfNeeded:forViewController:"
+ "_updateNavigationBarBackgroundIfNeeded:forViewController:"
+ "addTarget:action:"
+ "ams-force-run"
+ "childViewControllers"
+ "currentNavigationController"
+ "handleSwipeBackGesture:"
+ "ignoreBackButtonHandling"
+ "initWithEnclosedViewController:spinnerDelegate:overrideBackButton:"
+ "initWithMigrationContext:sourcePreferences:targetPreferences:"
+ "initialAnimateLanguageChoiceValue"
+ "initialDisplayZoomRestartValue"
+ "interactivePopGestureRecognizer"
+ "migratePreferenceWithSDPEnabledState:"
+ "migrationContext"
+ "overrideBackButton"
+ "previousViewController"
+ "removeTarget:action:"
+ "setCurrentNavigationController:"
+ "setInitialAnimateLanguageChoiceValue:"
+ "setInitialDisplayZoomRestartValue:"
+ "setMigrationContext:"
+ "setNavigationControllerIfNeeded:"
+ "setPreviousViewController:"
+ "setSourcePreferences:"
+ "setTargetPreferences:"
+ "setTransitionCoordinator:"
+ "sourcePreferences"
+ "targetPreferences"
+ "tintColor"
+ "transitionCoordinator"
+ "updateViewControllers"
+ "usesWhiteBackButton"
- "\x04\x11\x12\x12\x11[\x19"
- "/\x01"
- "Sep 18 2024"
- "_updateNavigationBarIfNeeded:forViewController:"

```
