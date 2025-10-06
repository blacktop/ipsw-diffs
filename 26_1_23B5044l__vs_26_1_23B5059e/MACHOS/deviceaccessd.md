## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-321.4.1.0.0
-  __TEXT.__text: 0x35cc4
+321.7.2.0.0
+  __TEXT.__text: 0x35cb8
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__objc_stubs: 0x4cc0
-  __TEXT.__objc_methlist: 0x1aa0
+  __TEXT.__objc_methlist: 0x1ab8
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x1fe0
-  __TEXT.__objc_methname: 0x68d6
+  __TEXT.__gcc_except_tab: 0x1fd8
+  __TEXT.__objc_methname: 0x6927
   __TEXT.__objc_classname: 0x1ff
-  __TEXT.__objc_methtype: 0x145b
-  __TEXT.__cstring: 0xc147
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__objc_methtype: 0x14c8
+  __TEXT.__cstring: 0xc10a
+  __TEXT.__unwind_info: 0xac0
   __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0xf60
-  __DATA_CONST.__cfstring: 0x1080
+  __DATA_CONST.__const: 0xf40
+  __DATA_CONST.__cfstring: 0x10e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x2318
-  __DATA.__objc_selrefs: 0x1908
+  __DATA.__objc_const: 0x2328
+  __DATA.__objc_selrefs: 0x1910
   __DATA.__objc_ivar: 0x234
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x6e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62AD639C-495E-3F01-97CA-B4781ED2A9D2
-  Functions: 973
+  UUID: 71E24EB1-09A6-3D6E-A766-3B59EBDAE4F7
+  Functions: 969
   Symbols:   345
-  CStrings:  2542
+  CStrings:  2551
 
CStrings:
+ "Found %@ device: %@"
+ "GetDevices: %@, from %@, bundleID %@"
+ "Reporting connection status changed: %@"
+ "com.apple.accessory-transport-extension"
+ "connected"
+ "connectionEventDidOccur %@ %s transport=%d"
+ "disconnected"
+ "pairingRequestCompletedForDataSession:pairingKeyStoreID:deviceID:"
+ "pairingRequestCompletedForPublisher:pairingKeyStoreID:deviceID:"
+ "v40@0:8@\"WiFiAwareDataSession\"16@\"NSUUID\"24Q32"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"NSUUID\"24Q32"
+ "v40@0:8@16@24Q32"
- "### connectionEventDidOccur %@"
- "### connectionEventDidOccur %@ %s transport=%d"
- "### connectionEventDidOccur DADevice %@ for %@"
- "### connectionEventDidOccur getDevicesWithFlags %@ %@"
- "-[DADaemonServer centralManager:connectionEventDidOccur:forPeripheral:]_block_invoke"
- "reportDiscoveryEvent:appID:filterDiscoveryInApp:"

```
