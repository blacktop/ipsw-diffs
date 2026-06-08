## WiFiDataMigrator

> `/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator`

```diff

-2000.6.0.0.0
-  __TEXT.__text: 0x1f70
+2027.9.0.0.0
+  __TEXT.__text: 0x1f68
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x280
-  __TEXT.__objc_methlist: 0x134
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x140
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x376
-  __TEXT.__oslogstring: 0x321
+  __TEXT.__cstring: 0x3f7
+  __TEXT.__oslogstring: 0x34c
   __TEXT.__objc_classname: 0x11
-  __TEXT.__objc_methname: 0x283
+  __TEXT.__objc_methname: 0x299
   __TEXT.__objc_methtype: 0xaa
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_selrefs: 0xd0
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24CD51DF-FEC4-37B9-B965-B2F11E0BEE7B
-  Functions: 29
-  Symbols:   105
-  CStrings:  115
+  UUID: 1E3D5241-6B07-360B-B35C-66AF081E83B6
+  Functions: 30
+  Symbols:   104
+  CStrings:  120
 
Symbols:
+ _WiFiNetworkGetType
+ _WiFiNetworkSetCarPlayInternetCheckState
- _MGGetProductType
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "CarPlayCheckForInternet"
+ "EAPOLClientConfiguration"
+ "EAPOLClientConfigurationCompleteMigration"
+ "EAPOLClientConfigurationLazyMigration"
+ "Setting kWiFiPreferenceCarPlayInternetCheckStateKey property for CarPlay network"
+ "checkCarPlayInternet:"
- "Disabling WAPI for unsupported device"

```
