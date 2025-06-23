## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

-521.0.0.0.0
-  __TEXT.__text: 0x5a248
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__const: 0x2f0
-  __TEXT.__oslogstring: 0x5ea9
-  __TEXT.__cstring: 0x4072
-  __TEXT.__unwind_info: 0xbf0
-  __DATA_CONST.__auth_got: 0x818
+525.0.0.0.0
+  __TEXT.__text: 0x5af88
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__const: 0x300
+  __TEXT.__oslogstring: 0x5fdf
+  __TEXT.__cstring: 0x409a
+  __TEXT.__unwind_info: 0xc00
+  __DATA_CONST.__auth_got: 0x820
   __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__auth_ptr: 0xf8
-  __DATA_CONST.__const: 0x1d60
-  __DATA_CONST.__cfstring: 0x29e0
+  __DATA_CONST.__const: 0x1d88
+  __DATA_CONST.__cfstring: 0x2a20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x118
   __DATA.__bss: 0x1f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 74619A4C-BA49-3C71-8980-34C740966AD5
-  Functions: 1006
-  Symbols:   482
-  CStrings:  2036
+  UUID: 823A0957-015D-35E0-8D6A-2B5FD1804016
+  Functions: 1014
+  Symbols:   484
+  CStrings:  2047
 
Symbols:
+ _Apple80211Set
+ _WiFiAcknowledgeConnectionID
CStrings:
+ " ConnectionID=%u"
+ "%@: APPLE80211_IOC_PROTOCOL_CLEANUP_COMPLETE failed, %d"
+ "%@: SSID %@ BSSID %@ NetworkID %@ Security %s ConnectionID %u"
+ "%@: SSID %@ BSSID %@ Security %s ConnectionID %u"
+ "%s: acknowledge Wi-Fi connection ID %u failed"
+ "%s: acknowledged Wi-Fi connection ID %u"
+ "%s: close socket %d failed, %s"
+ "Apple80211BindToInterface(%@) failed, 0x%x"
+ "Apple80211Get(APPLE80211_IOC_CONNECTION_ID)failed, 0x%x"
+ "ConnectionID"
+ "IPv4.Router=%@;IPv4.RouterHardwareAddress=%@"
+ "Will NOT "
+ "[%s] %sTransmit %d byte packet\n%@"
+ "[%s] %sTransmit %d byte packet dest %d.%d.%d.%d scope %d\n%@"
+ "[%s] %sTransmit %d byte packet xid 0x%lx to %d.%d.%d.%d [scope=%d]"
- "%@: SSID %@ BSSID %@ NetworkID %@ Security %s"
- "%@: SSID %@ BSSID %@ Security %s"
- "IPv4.Router=%@;IPv4.RouterHardwareAddress=%s"
- "[%s] Transmit %d byte packet\n%@"
- "[%s] Transmit %d byte packet dest %d.%d.%d.%d scope %d\n%@"
- "[%s] Transmit %d byte packet xid 0x%lx to %d.%d.%d.%d [scope=%d]"

```
