## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0xacedc
+55.1.1.0.0
+  __TEXT.__text: 0xae898
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x16ec
+  __TEXT.__objc_methlist: 0x1734
   __TEXT.__const: 0x5190
-  __TEXT.__oslogstring: 0x3e98
-  __TEXT.__cstring: 0x3212
+  __TEXT.__oslogstring: 0x3f28
+  __TEXT.__cstring: 0x33e2
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0x2dca
   __TEXT.__swift5_fieldmd: 0x1ecc
-  __TEXT.__constg_swiftt: 0x36ac
+  __TEXT.__constg_swiftt: 0x36bc
   __TEXT.__swift5_reflstr: 0x1ad1
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0x468
-  __TEXT.__swift5_capture: 0x17d8
+  __TEXT.__swift5_capture: 0x185c
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_proto: 0x330
   __TEXT.__swift5_types: 0x278
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x2bf0
-  __TEXT.__eh_frame: 0x2728
+  __TEXT.__unwind_info: 0x2c48
+  __TEXT.__eh_frame: 0x2848
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb08
   __DATA_CONST.__objc_protorefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x5b8
-  __AUTH_CONST.__const: 0x72f8
-  __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0x4828
+  __DATA_CONST.__got: 0x5c8
+  __AUTH_CONST.__const: 0x73a0
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x4830
   __AUTH_CONST.__auth_got: 0x1100
-  __AUTH.__objc_data: 0x2188
+  __AUTH.__objc_data: 0x2190
   __AUTH.__data: 0x22f8
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x2448

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3508
-  Symbols:   2366
-  CStrings:  624
+  Functions: 3529
+  Symbols:   2367
+  CStrings:  634
 
Symbols:
+ __OBJC_$_INSTANCE_METHODS_APSettingsManager(SearchAndSiriPrivate|ForAppProtectionUI|AppMigration)
+ _objc_msgSend$migrateSettingsFromBundleIdentifier:toBundleIdentifier:completion:
- __OBJC_$_INSTANCE_METHODS_APSettingsManager(SearchAndSiriPrivate|ForAppProtectionUI)
CStrings:
+ "%s has no settings to migrate to %s"
+ "%s is already protected; only clearing the settings of %s"
+ "Cannot migrate the settings of a hidden application"
+ "cannot migrate an application's settings to itself"
+ "cannot migrate settings to an application which is not installed"
+ "errorPreventingMigratingSettings(from:to:)"
+ "migrateSettings(fromBundleIdentifier:toBundleIdentifier:completion:)"
+ "migrateSettings(fromBundleWithIdentifier:toBundleWithIdentifier:)"
+ "migrated settings from %s to %s"
+ "settings can only be migrated between applications"
```
