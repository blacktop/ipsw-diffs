## wifid

> `/usr/sbin/wifid`

```diff

-  __TEXT.__text: 0x1c1760
+  __TEXT.__text: 0x1c1f4c
   __TEXT.__auth_stubs: 0x2bc0
-  __TEXT.__objc_stubs: 0x14e20
-  __TEXT.__objc_methlist: 0x6818
+  __TEXT.__objc_stubs: 0x14e40
+  __TEXT.__objc_methlist: 0x6820
   __TEXT.__gcc_except_tab: 0x2904
   __TEXT.__const: 0xe5b
-  __TEXT.__cstring: 0x7518d
-  __TEXT.__objc_methname: 0x1b130
+  __TEXT.__cstring: 0x75423
+  __TEXT.__objc_methname: 0x1b14f
   __TEXT.__objc_classname: 0x85e
   __TEXT.__objc_methtype: 0x33ac
   __TEXT.__dlopen_cstrs: 0x33c
   __TEXT.__oslogstring: 0x27ef
   __TEXT.__ustring: 0x4c2
-  __TEXT.__unwind_info: 0x4558
-  __DATA_CONST.__const: 0x7b68
-  __DATA_CONST.__cfstring: 0x1c520
+  __TEXT.__unwind_info: 0x4568
+  __DATA_CONST.__const: 0x7ba8
+  __DATA_CONST.__cfstring: 0x1c6a0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8

   __DATA_CONST.__objc_arrayobj: 0x258
   __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__auth_got: 0x15f0
-  __DATA_CONST.__got: 0x13a8
+  __DATA_CONST.__got: 0x1400
   __DATA_CONST.__auth_ptr: 0x160
   __DATA.__objc_const: 0xd390
-  __DATA.__objc_selrefs: 0x6320
+  __DATA.__objc_selrefs: 0x6328
   __DATA.__objc_ivar: 0xa14
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x1130

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 8781
+  Functions: 8785
   Symbols:   1345
-  CStrings:  21000
+  CStrings:  21031
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__objc_methtype : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s: Detaching MIS session to prevent stale host count"
+ "%s: Trial config applied — rssiDeep=%d rssi24G=%d rssi24G_MultiAP=%d rssi5G=%d rssiBadCell=%d waitShort=%.1f waitMedium=%.1f waitLong=%.1f rssiHighRSSI=%d lqaMask=0x%02x legacyMask=0x%02x augCritLink=%d augDeepRSSI=%d carPlayExempt=%d bcnPer=%.2f txPer=%.2f drive=%.0f tdImminent=%u monitorOnly=%d gateOnIC=%d gateMultiAP24GOnIC=%d alZoneHystDb=%d alRssiCap=%d wfaWalkout=%d wfaPoor2G=%d entryBoost[autoLeave=%d poor2G=%d cheap5G=%d drive=%d rtApp=%d] waitBoost[autoLeave=%d deepRSSI=%d poor2G=%d drive=%d rtApp=%d roamFail=%d noRoam=%d]"
+ "%s: Unable to detach MIS session: %s"
+ "%s: Unable to release MIS PM Assertion error=%d"
+ "%s: Unable to stop MIS service: %s"
+ "%s: Updated edge parameters for BSSID %@ - isEdge: %d, autoLeaveRssi(learnt): %d capped: %d, SSID %@ - 2G relevant: %d"
+ "%s: rssi is 0 for known network (not scan result), bypassing RSSI-based TD evaluation"
+ "AutoInstallMegaWiFiProfile"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "LinkDownManual"
+ "LinkDownNonManual"
+ "Superseded"
+ "Teardown"
+ "WiFiDeviceManagerDetachMISSession"
+ "WiFiManager-2027.18 Jul  1 2026 23:36:07"
+ "WiFiManager-2027.18 Jul  1 2026 23:36:58"
+ "scoreTD_allowAboveDeepOnPoor2GMultiAp"
+ "scoreTD_augmentOnLinkRec"
+ "scoreTD_autoLeaveRssiCap"
+ "scoreTD_autoLeaveZoneHysteresisDb"
+ "scoreTD_linkRecExcludeOnAutoLeavePermissive"
+ "scoreTD_wifiAssistOnPoor2G"
+ "scoreTD_wifiAssistOnWalkout"
+ "terminateRequestWithEndReason:"
- "%s: Trial config applied — rssiDeep=%d rssi24G=%d rssi24G_MultiAP=%d rssi5G=%d rssiBadCell=%d waitShort=%.1f waitMedium=%.1f waitLong=%.1f rssiHighRSSI=%d lqaMask=0x%02x legacyMask=0x%02x augCritLink=%d augDeepRSSI=%d carPlayExempt=%d bcnPer=%.2f txPer=%.2f drive=%.0f tdImminent=%u monitorOnly=%d gateOnIC=%d gateMultiAP24GOnIC=%d entryBoost[autoLeave=%d poor2G=%d cheap5G=%d drive=%d rtApp=%d] waitBoost[autoLeave=%d deepRSSI=%d poor2G=%d drive=%d rtApp=%d roamFail=%d noRoam=%d]"
- "%s: Updated edge parameters for BSSID %@ - isEdge: %d, autoLeaveRssi: %d, SSID %@ - 2G relevant: %d"
- "%s: initial IC state: feature=%s user=%s effective=%s"
- "WiFiManager-2027.13 Jun 17 2026 00:36:54"
- "WiFiManager-2027.13 Jun 17 2026 00:37:49"

```
