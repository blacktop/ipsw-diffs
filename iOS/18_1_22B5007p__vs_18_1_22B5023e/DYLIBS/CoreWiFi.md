## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-805.86.0.0.0
-  __TEXT.__text: 0xee250
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x9db0
+805.95.0.0.0
+  __TEXT.__text: 0xf41e0
+  __TEXT.__auth_stubs: 0x1080
+  __TEXT.__objc_methlist: 0x9e54
   __TEXT.__const: 0x620
-  __TEXT.__cstring: 0xdd22
-  __TEXT.__gcc_except_tab: 0x37b0
-  __TEXT.__oslogstring: 0xbaef
+  __TEXT.__cstring: 0xe77f
+  __TEXT.__gcc_except_tab: 0x3c68
+  __TEXT.__oslogstring: 0xc069
   __TEXT.__dlopen_cstrs: 0x41a
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3238
-  __TEXT.__objc_classname: 0x87c
-  __TEXT.__objc_methname: 0x16221
-  __TEXT.__objc_methtype: 0x27db
-  __TEXT.__objc_stubs: 0x11220
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0x2c08
+  __TEXT.__unwind_info: 0x32b8
+  __TEXT.__objc_classname: 0x87d
+  __TEXT.__objc_methname: 0x163d5
+  __TEXT.__objc_methtype: 0x2817
+  __TEXT.__objc_stubs: 0x11300
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x2c30
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51a8
+  __DATA_CONST.__objc_selrefs: 0x51f8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0x10e8
-  __AUTH_CONST.__auth_got: 0x840
+  __DATA_CONST.__objc_arraydata: 0x10f8
+  __AUTH_CONST.__auth_got: 0x850
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1c20
-  __AUTH_CONST.__cfstring: 0x115c0
-  __AUTH_CONST.__objc_const: 0xfbf0
-  __AUTH_CONST.__objc_intobj: 0x2fd0
+  __AUTH_CONST.__const: 0x1c00
+  __AUTH_CONST.__cfstring: 0x114c0
+  __AUTH_CONST.__objc_const: 0xfcb0
+  __AUTH_CONST.__objc_intobj: 0x3000
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xadc
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xaec
   __DATA.__data: 0x8a0
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_ivar: 0x18
-  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4468
-  Symbols:   776
-  CStrings:  7321
+  Functions: 4481
+  Symbols:   777
+  CStrings:  7389
 
Symbols:
+ _dispatch_block_create_with_qos_class
+ _mrc_cached_local_records_inquiry_invalidate
- _CWFSetNetworkIDForAssociation
CStrings:
+ "\x051\x12\x15\x15\x15!!\x19\x13/\x02"
+ "\x06$"
+ "\x1a\x19"
+ "%!"(MISSING)
+ "-[CWFAutoJoinManager __addRequest:]"
+ "-[CWFAutoJoinManager __addRequest:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToAllowAutoHotspotWithTrigger:error:]"
+ "-[CWFAutoJoinManager __calloutToAllowAutoHotspotWithTrigger:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToAllowAutoJoinWithTrigger:error:]"
+ "-[CWFAutoJoinManager __calloutToAllowAutoJoinWithTrigger:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToAllowHotspot:error:]"
+ "-[CWFAutoJoinManager __calloutToAllowHotspot:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToAllowJoinCandidate:trigger:defer:error:]"
+ "-[CWFAutoJoinManager __calloutToAllowJoinCandidate:trigger:defer:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]"
+ "-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToAssociateWithParameters:error:]"
+ "-[CWFAutoJoinManager __calloutToAssociateWithParameters:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToBrowseForHotspotsWithTimeout:maxCacheAge:cacheOnly:error:]"
+ "-[CWFAutoJoinManager __calloutToBrowseForHotspotsWithTimeout:maxCacheAge:cacheOnly:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToConnectToHotspot:error:]"
+ "-[CWFAutoJoinManager __calloutToConnectToHotspot:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToPerformGASQueryWithParameters:GASQueryNetworks:error:]"
+ "-[CWFAutoJoinManager __calloutToPerformGASQueryWithParameters:GASQueryNetworks:error:]_block_invoke"
+ "-[CWFAutoJoinManager __calloutToScanForNetworksWithParameters:scanChannels:error:]"
+ "-[CWFAutoJoinManager __calloutToScanForNetworksWithParameters:scanChannels:error:]_block_invoke"
+ "-[CWFAutoJoinManager __performAutoJoin]"
+ "-[CWFAutoJoinManager __performAutoJoin]_block_invoke"
+ "-[CWFAutoJoinManager __removeRedundantRequests:]"
+ "-[CWFAutoJoinManager __removeRedundantRequests:]_block_invoke"
+ "-[CWFAutoJoinManager __updateAutoJoinState:]"
+ "-[CWFAutoJoinManager __updateAutoJoinState:]_block_invoke"
+ "-[CWFAutoJoinManager __updateDiscoverTimestampForJoinCandidates:]"
+ "-[CWFAutoJoinManager __updateDiscoverTimestampForJoinCandidates:]_block_invoke"
+ "-[CWFAutoJoinManager __updateRNRChannel:has6GHzOnlyBSS:joinCandidate:]"
+ "-[CWFAutoJoinManager __updateRNRChannel:has6GHzOnlyBSS:joinCandidate:]_block_invoke"
+ "-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]"
+ "-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke"
+ "-[CWFAutoJoinManager invalidate]_block_invoke"
+ "-[CWFAutoJoinManager performAutoJoinWithParameters:reply:]"
+ "-[CWFAutoJoinManager performAutoJoinWithParameters:reply:]_block_invoke"
+ "-[CWFLocalDeviceDiscovery _callHandlerWithValidResults:filtered:]"
+ "-[CWFLocalDeviceDiscovery activate]"
+ "-[CWFLocalDeviceDiscovery activate]_block_invoke"
+ "-[CWFLocalDeviceDiscovery invalidate]"
+ "@\"NSObject<OS_mrc_cached_local_records_inquiry>\""
+ "CONNECTED_BSSID"
+ "CWFAutoJoinManager.m"
+ "I24@0:8q16"
+ "T@\"NSObject<OS_mrc_cached_local_records_inquiry>\",&,N,V_mrcInquiry"
+ "[corewifi] %!s(MISSING)"
+ "[corewifi] %!s(MISSING): calling handler"
+ "[corewifi] %!s(MISSING): handler is nil"
+ "[corewifi] %!s(MISSING): libMRC not available"
+ "[corewifi] <<<@[%!l(MISSING)lu.%!l(MISSING)lu] %!{(MISSING)public}s (%!{(MISSING)public}s:%!u(MISSING)) "
+ "[corewifi] >>> @[%!l(MISSING)lu.%!l(MISSING)lu] %!{(MISSING)public}s (%!{(MISSING)public}s:%!u(MISSING)) "
+ "[corewifi] AUTO-JOIN: Already found followup 6GHz BSS target, using cached result"
+ "[corewifi] AUTO-JOIN: Queueing block for new auto-join trigger with higher QoS (qos=%!d(MISSING), prev=%!d(MISSING), trigger=%!{(MISSING)public}@)"
+ "[corewifi] AUTO-JOIN: Will run request (qos=%!d(MISSING), request=%!{(MISSING)public}@"
+ "[corewifi] Failed to get HW MAC address from SCNetworkInterface, falling back to network stack (intf=%!{(MISSING)public}@)"
+ "[corewifi] Failed to get HW MAC address from the WiFi stack (intf=%!{(MISSING)public}@)"
+ "[corewifi] Failed to get HW MAC address from the network stack, falling back to WiFi stack (intf=%!{(MISSING)public}@)"
+ "[corewifi] PRIVATE MAC: Did not find cached association network ID, forgetting IP configuration for network (%!{(MISSING)public}@)"
+ "[corewifi] PRIVATE MAC: FAILED to create network ID for association (error=%!@(MISSING), network=%!{(MISSING)public}@)"
+ "[corewifi] [%!{(MISSING)public}@] Incoming QoS is less than 'default', promoting to 'default'"
+ "[corewifi] [%!{(MISSING)public}@] QoS override specified for request (self=%!d(MISSING), override=%!l(MISSING)d)"
+ "[corewifi] filtered home profiles='%!@(MISSING)'"
+ "[corewifi] home profile='%!@(MISSING)' distance exceeds max distance to non-home profile='%!@(MISSING)' (distance=%!f(MISSING))"
+ "[corewifi] profile='%!@(MISSING)' distance exceeds max distance from primary callout (distance=%!f(MISSING))"
+ "[corewifi] remaining profiles='%!@(MISSING)'"
+ "[corewifi] results exceed maximum removing at range='%!@(MISSING)'"
+ "__alreadyFoundFollowup6GHzBSSWithSignature:"
+ "__qosForAutoJoinTrigger:"
+ "_callHandlerWithValidResults:filtered:"
+ "_filterProfilesForHomeNetworksExceedingMaximumDistance:"
+ "_highestPendingQoS"
+ "_mrcInquiry"
+ "_networkIDCache"
+ "_networkIDCacheIDList"
+ "hardwareMACAddress:"
+ "logRedactionSetting"
+ "mrcInquiry"
+ "numberWithUnsignedShort:"
+ "removeLastObject"
+ "removeObjectsInRange:"
+ "setLogRedactionSetting:"
+ "setMrcInquiry:"
+ "setNetworkIDForAssociationWithMACAddress:networkProfile:"
+ "v32@?0@\"CWFNetworkProfile\"8Q16^B24"
+ "wasConnectedDuringSleep"
+ "wasConnectedDuringSleep"
+ "wasConnectedDuringSleep=%!l(MISSING)i, "
- "\x051\x17\x15\x15!!\x19\x13/\x02"
- "\a#"
- "\x18\x19"
- "$"
- "-[CWFLocalDeviceDiscovery discover]"
- "-[CWFLocalDeviceDiscovery discover]_block_invoke"
- "-[CWFLocalDeviceDiscovery discover]_block_invoke_2"
- "SCAN_BSS_TYPE"
- "SCAN_CHANNELS"
- "SCAN_DWELL_TIME"
- "SCAN_FLAGS"
- "SCAN_MERGE"
- "SCAN_MIN_TIMESTAMP"
- "SCAN_NUM_SCANS"
- "SCAN_PHY_MODE"
- "SCAN_REST_TIME"
- "SCAN_SSID_LIST"
- "SCAN_TYPE"
- "T@\"NSObject<OS_dispatch_queue>\",&"
- "[corewifi] %!{(MISSING)public}s (%!{(MISSING)public}s:%!u(MISSING)) Background scan result is missing BSSID, skipping (0x%!@(MISSING))"
- "__scanDictionaryWithParameters:"
- "_isIPv4Address"
- "_queue"
- "_setQueue:"

```
