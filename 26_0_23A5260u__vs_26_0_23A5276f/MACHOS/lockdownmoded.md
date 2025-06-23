## lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

-80.0.0.502.1
-  __TEXT.__text: 0x2b400
+80.0.4.0.0
+  __TEXT.__text: 0x2ce74
   __TEXT.__auth_stubs: 0x1200
-  __TEXT.__objc_stubs: 0x340
-  __TEXT.__objc_methlist: 0x4a8
+  __TEXT.__objc_stubs: 0x380
+  __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0xed8
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__objc_methname: 0x141f
-  __TEXT.__cstring: 0x1603
-  __TEXT.__oslogstring: 0x25b2
+  __TEXT.__objc_methname: 0x149d
+  __TEXT.__cstring: 0x16d3
+  __TEXT.__oslogstring: 0x2772
   __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methtype: 0x9e6
+  __TEXT.__objc_methtype: 0x9f8
   __TEXT.__swift5_typeref: 0x6e3
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xb84
+  __TEXT.__constg_swiftt: 0xb94
   __TEXT.__swift5_reflstr: 0x424
   __TEXT.__swift5_fieldmd: 0x438
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_types: 0x68
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__swift5_capture: 0x29c
+  __TEXT.__swift5_capture: 0x2c0
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x680
-  __TEXT.__eh_frame: 0x710
+  __TEXT.__unwind_info: 0x698
+  __TEXT.__eh_frame: 0x748
   __DATA_CONST.__auth_got: 0x910
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__auth_ptr: 0x300
-  __DATA_CONST.__const: 0xdd8
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__auth_ptr: 0x308
+  __DATA_CONST.__const: 0xe30
+  __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1130
-  __DATA.__objc_selrefs: 0x5d8
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x550
-  __DATA.__data: 0x134a
+  __DATA.__objc_const: 0x1158
+  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_data: 0x558
+  __DATA.__data: 0x135a
   __DATA.__bss: 0x11b0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 986D189C-76CB-3A63-B906-B68F71D2E352
-  Functions: 579
-  Symbols:   513
-  CStrings:  619
+  UUID: D2B22AC5-3208-3C36-94E5-0F0E7755C4C6
+  Functions: 594
+  Symbols:   509
+  CStrings:  638
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "@\"NSUserDefaults\""
+ "Client requested to set the managed configuration value: lockdownModeEnabled=%{bool}d"
+ "Could not get MC connection"
+ "Failed to set MC value: lockdownModeEnabled=%{bool}d"
+ "Failed to update managed configuration: %s"
+ "Successfully set MC value: lockdownModeEnabled=%{bool}d"
+ "Successfully set the managed configuration value: lockdownModeEnabled=%{bool}d"
+ "Unchanged MC value: lockdownModeEnabled=%{bool}d"
+ "Updated CFU to omit badge: %d"
+ "_cfuViewed"
+ "_userDefaults"
+ "com.apple.ThreatNotificationUI.FollowUpExtension"
+ "com.apple.ThreatNotificationUI.storage.cfuViewed"
+ "com.apple.lockdownmoded.updateManagedConfiguration"
+ "effectiveBoolValueForSetting:"
+ "initWithSuiteName:"
+ "setManagedConfigurationStateWithEnabled:completion:"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
- "Updated CFU for LDM enabled: %d"

```
