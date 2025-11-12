## keybagd

> `/usr/libexec/keybagd`

```diff

-674.40.3.0.0
-  __TEXT.__text: 0x21b54
-  __TEXT.__auth_stubs: 0x14b0
+674.60.2.0.0
+  __TEXT.__text: 0x21d48
+  __TEXT.__auth_stubs: 0x14c0
   __TEXT.__objc_stubs: 0x1020
   __TEXT.__objc_methlist: 0x814
-  __TEXT.__cstring: 0x9939
+  __TEXT.__cstring: 0x9b2e
   __TEXT.__const: 0x198
   __TEXT.__gcc_except_tab: 0x478
   __TEXT.__objc_methname: 0x181c

   __TEXT.__objc_methtype: 0x967
   __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__oslogstring: 0x281
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0xa68
+  __TEXT.__unwind_info: 0x778
+  __DATA_CONST.__auth_got: 0xa70
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x1030
-  __DATA_CONST.__cfstring: 0x4e80
+  __DATA_CONST.__const: 0x1050
+  __DATA_CONST.__cfstring: 0x4ea0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C00C1EEE-59B1-3023-A042-244DCB53370F
-  Functions: 645
-  Symbols:   400
-  CStrings:  2116
+  UUID: 89BB9900-FA0A-3C04-AB79-99C575A5454F
+  Functions: 648
+  Symbols:   401
+  CStrings:  2125
 
Symbols:
+ _AKSGetKeyBagStats
CStrings:
+ "AnalyticsEvent: report_version: %llu, kAppleKeyStoreDeviceBag_count: %llu, kAppleKeyStoreBackupBag_count: %llu, kAppleKeyStoreEscrowBag_count: %llu, kAppleKeyStoreOTABackupBag_count: %llu, kAppleKeyStoreAsymmetricBackupBag_count: %llu, analytics_failure: %llu"
+ "analytics_send_keybag_count_stats"
+ "com.apple.mobile.keybagd.keybag_count_stats"
+ "kAppleKeyStoreAsymmetricBackupBag_count"
+ "kAppleKeyStoreBackupBag_count"
+ "kAppleKeyStoreDeviceBag_count"
+ "kAppleKeyStoreEscrowBag_count"
+ "kAppleKeyStoreOTABackupBag_count"

```
