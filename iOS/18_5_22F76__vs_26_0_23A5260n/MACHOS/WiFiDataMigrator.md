## WiFiDataMigrator

> `/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator`

```diff

-1935.4.0.0.0
-  __TEXT.__text: 0x1ea0
-  __TEXT.__auth_stubs: 0x3e0
+1975.87.0.0.0
+  __TEXT.__text: 0x1f78
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_stubs: 0x280
   __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x345
-  __TEXT.__oslogstring: 0x2c4
+  __TEXT.__cstring: 0x376
+  __TEXT.__oslogstring: 0x321
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methname: 0x283
   __TEXT.__objc_methtype: 0xaa
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F52D3B4C-130D-34C4-91E1-79AC647F3134
+  UUID: 52D5D586-84D1-3879-8BD9-C6BBFAFC532A
   Functions: 28
-  Symbols:   101
-  CStrings:  111
+  Symbols:   105
+  CStrings:  115
 
Symbols:
+ _DMGetUserDataDisposition
+ _WiFiManagerClientResetPrivateMAC
+ __os_feature_enabled_impl
+ _kWiFiPreferencesDeviceUUIDKey
Functions:
~ sub_2218 : 1416 -> 1628
~ sub_27a0 -> sub_2874 : 116 -> 120
CStrings:
+ "CoreWiFi"
+ "Restored from different device, clearing private MAC address derivation keys and device UUID"
+ "UnifiedPrivateMAC"
+ "UnifiedPrivateMAC_ios"

```
