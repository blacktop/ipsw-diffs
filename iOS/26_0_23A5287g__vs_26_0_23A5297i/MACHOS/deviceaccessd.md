## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-320.36.0.0.0
-  __TEXT.__text: 0x32194
+320.38.0.0.0
+  __TEXT.__text: 0x32fe0
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x4980
-  __TEXT.__objc_methlist: 0x19d8
+  __TEXT.__objc_stubs: 0x49a0
+  __TEXT.__objc_methlist: 0x1a00
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x1db0
-  __TEXT.__objc_methname: 0x657f
+  __TEXT.__gcc_except_tab: 0x1e08
+  __TEXT.__objc_methname: 0x6598
   __TEXT.__objc_classname: 0x1ff
   __TEXT.__objc_methtype: 0x14bc
-  __TEXT.__cstring: 0xb775
-  __TEXT.__unwind_info: 0xa50
+  __TEXT.__cstring: 0xba2f
+  __TEXT.__unwind_info: 0xa80
   __DATA_CONST.__auth_got: 0x710
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0xe58
+  __DATA_CONST.__const: 0xee8
   __DATA_CONST.__cfstring: 0x1000
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x22d0
-  __DATA.__objc_selrefs: 0x1830
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_const: 0x22f0
+  __DATA.__objc_selrefs: 0x1838
+  __DATA.__objc_ivar: 0x230
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x6e0
   __DATA.__bss: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4292F284-59F3-3AD9-8B37-EFA7EDABB271
-  Functions: 922
+  UUID: DDF12F3D-4CA2-3031-B29E-9FF36162DA76
+  Functions: 939
   Symbols:   341
-  CStrings:  2452
+  CStrings:  2469
 
CStrings:
+ "### Reset Wi-Fi Identifier - Removing all Wi-Fi Aware devices"
+ "### ResetWiFiIdentifier create reply failed"
+ "### ResetWiFiIdentifier failed: %@ from %@"
+ "-[DADaemonServer _activate]_block_invoke_4"
+ "-[DADaemonServer _activate]_block_invoke_9"
+ "-[DADaemonServer resetWiFiIdentifier:]"
+ "-[DADaemonServer resetWiFiIdentifier:]_block_invoke"
+ "-[DADaemonXPCConnection _xpcResetWiFiIdentifier:]_block_invoke"
+ "-[DADaemonXPCConnection _xpcResetWiFiIdentifier:]_block_invoke_2"
+ "Clearing All Wi-Fi Aware permissions and resetting Wi-Fi identifier"
+ "Listen for Network Settings Reset"
+ "Reset Wi-Fi Identifier failed with error %@"
+ "RsWf"
+ "WiFiAwarePairedUUID: %@"
+ "[WIFI] unable to create new DADevice for WiFi result: %@"
+ "_resetNetworkSettingsToken"
+ "_xpcResetWiFiIdentifier:"
+ "com.apple.Preferences.ResetNetworkSettingsNotification"
+ "deauthorizePairedDeviceFor:withDeviceID:remove:"
+ "deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:"
+ "removeAllPairedDevices:"
+ "resetWiFiIdentifier:"
- "-[DADaemonServer _activate]_block_invoke_7"
- "removePairedDeviceFor:withDeviceID:"
- "removePairedDeviceFor:withDeviceID:completionHandler:"
- "uninstallPairedDeviceFor:withDeviceID:"
- "uninstallPairedDeviceFor:withDeviceID:completionHandler:"

```
