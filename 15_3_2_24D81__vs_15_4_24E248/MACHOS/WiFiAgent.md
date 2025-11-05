## WiFiAgent

> `/System/Library/CoreServices/WiFiAgent.app/Contents/MacOS/WiFiAgent`

```diff

-19045.5.0.0.0
-  __TEXT.__text: 0x1fd84
+19075.37.0.0.0
+  __TEXT.__text: 0x1ffd0
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_stubs: 0x4ac0
-  __TEXT.__objc_methlist: 0xeb8
-  __TEXT.__cstring: 0x51ef
+  __TEXT.__objc_methlist: 0x17d4
+  __TEXT.__cstring: 0x555d
   __TEXT.__oslogstring: 0x89
   __TEXT.__objc_classname: 0x275
   __TEXT.__objc_methname: 0x6496
   __TEXT.__objc_methtype: 0x1722
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__unwind_info: 0x848
   __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__cfstring: 0x1ca0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x28a8
-  __DATA.__objc_selrefs: 0x1688
+  __DATA.__objc_const: 0x1780
+  __DATA.__objc_selrefs: 0x18c8
   __DATA.__objc_ivar: 0x158
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x7a8

   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/Versions/A/WirelessDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34F59CFF-7931-3546-9847-25B08C6DBE16
-  Functions: 638
+  UUID: B1B2E0D2-7049-3778-B982-F4451500BD9A
+  Functions: 631
   Symbols:   223
-  CStrings:  1832
+  CStrings:  1844
 
CStrings:
+ "-[CWAutoHotspotNotifications _purgeTetherDevice:]"
+ "-[CWAutoHotspotNotifications bssidDidChange:forInterfaceWithName:]_block_invoke"
+ "-[CWAutoHotspotNotifications networkPathIsNowAvailable]_block_invoke"
+ "-[CWWiFiAgent session:updatedFoundDevices:]_block_invoke"
+ "<%s[%d]> %s: %s Notification for tether device [%@] being added. Retry : [%hhu]\n"
+ "<%s[%d]> %s: %s Purge tether device [%@] on BSSID change\n"
+ "<%s[%d]> %s: %s Purge tether device [%@] on network path availability\n"
+ "<%s[%d]> %s: %s Remove delivered notifications requested for [%@]\n"
+ "<%s[%d]> %s: %s Remove pending notifications requested for [%@]\n"
+ "<%s[%d]> %s: %s SFRemoteHotspotSession : Remote hotspot device cache emptied at [%llu]\n"
+ "<%s[%d]> %s: %s SFRemoteHotspotSession : Session ended and cache populated with new devices at [%llu]\n"
+ "<%s[%d]> %s: New Remote Hotspot device browsing request. Cache last updated at : [%llu]\n"

```
