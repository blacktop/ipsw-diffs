## SystemMigrationNetwork

> `/System/Library/PrivateFrameworks/SystemMigrationNetwork.framework/Versions/A/SystemMigrationNetwork`

```diff

-68.60.45.0.0
-  __TEXT.__text: 0x3e4b0
+128.100.161.0.0
+  __TEXT.__text: 0x3e3a8
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x404c
+  __TEXT.__objc_methlist: 0x4488
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x9a16
-  __TEXT.__gcc_except_tab: 0xdec
+  __TEXT.__cstring: 0x9ab5
+  __TEXT.__gcc_except_tab: 0xdf4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xda8
+  __TEXT.__unwind_info: 0xd88
   __TEXT.__objc_classname: 0x5de
   __TEXT.__objc_methname: 0xac20
   __TEXT.__objc_methtype: 0x1337

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2898
+  __DATA_CONST.__objc_selrefs: 0x2958
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x8c60
-  __AUTH_CONST.__objc_const: 0x6f40
+  __AUTH_CONST.__cfstring: 0x8ce0
+  __AUTH_CONST.__objc_const: 0x6758
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC8C1312-A7A1-3828-B9F5-025DF185F96E
-  Functions: 1509
-  Symbols:   4043
-  CStrings:  4508
+  UUID: 40E0E42E-2136-3950-9FC7-899641E0B53F
+  Functions: 1510
+  Symbols:   4052
+  CStrings:  4516
 
Symbols:
+ +[SMAutoLoaderSSL sessionKeychain].cold.1
+ +[SMNAnalyticsManager sharedManager].cold.1
+ +[SMNBundle bundle].cold.1
+ +[SMNBundleExtension commonBundleExtensions].cold.1
+ +[SMNNetworkMigrationBrowser addLocalInstanceName:].cold.1
+ +[SMNWifiDebugCapture capture].cold.1
+ SMNCurrentLogLevel.cold.1
+ SMNNetworkLogWithType.cold.1
+ SMNNetworkLogWithType.cold.2
CStrings:
+ "SoftAP channel override enabled; using: %@"
+ "SoftAPChannelOverride"
+ "^.*\\/Logs\\/Bluetooth\\/bluetoothd-hci-latest\\.pklg$"
+ "channelNumber == %@ and channelWidth <= %@"

```
