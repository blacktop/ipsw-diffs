## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-805.93.4.1.0
-  __TEXT.__text: 0xefdc4
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x9e4c
-  __TEXT.__const: 0x630
-  __TEXT.__cstring: 0xddad
-  __TEXT.__gcc_except_tab: 0x3858
-  __TEXT.__oslogstring: 0xbf3e
+805.95.0.0.0
+  __TEXT.__text: 0xf41e0
+  __TEXT.__auth_stubs: 0x1080
+  __TEXT.__objc_methlist: 0x9e54
+  __TEXT.__const: 0x620
+  __TEXT.__cstring: 0xe77f
+  __TEXT.__gcc_except_tab: 0x3c68
+  __TEXT.__oslogstring: 0xc069
   __TEXT.__dlopen_cstrs: 0x41a
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3260
-  __TEXT.__objc_classname: 0x87c
-  __TEXT.__objc_methname: 0x163b0
-  __TEXT.__objc_methtype: 0x280c
-  __TEXT.__objc_stubs: 0x112c0
+  __TEXT.__unwind_info: 0x32b8
+  __TEXT.__objc_classname: 0x87d
+  __TEXT.__objc_methname: 0x163d5
+  __TEXT.__objc_methtype: 0x2817
+  __TEXT.__objc_stubs: 0x11300
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x2c30
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51f0
+  __DATA_CONST.__objc_selrefs: 0x51f8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x10f8
-  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__auth_got: 0x850
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1c00
-  __AUTH_CONST.__cfstring: 0x11600
-  __AUTH_CONST.__objc_const: 0xfc90
-  __AUTH_CONST.__objc_intobj: 0x3018
+  __AUTH_CONST.__cfstring: 0x114c0
+  __AUTH_CONST.__objc_const: 0xfcb0
+  __AUTH_CONST.__objc_intobj: 0x3000
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xae8
+  __DATA.__objc_ivar: 0xaec
   __DATA.__data: 0x8a0
   __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_ivar: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4480
-  Symbols:   776
-  CStrings:  7354
+  Functions: 4481
+  Symbols:   777
+  CStrings:  7389
 
Symbols:
+ _dispatch_block_create_with_qos_class
CStrings:
+ "\x051\x12\x15\x15\x15!!\x19\x13/\x02"
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
+ "CWFAutoJoinManager.m"
+ "I24@0:8q16"
+ "[corewifi] <<<@[%!l(MISSING)lu.%!l(MISSING)lu] %!{(MISSING)public}s (%!{(MISSING)public}s:%!u(MISSING)) "
+ "[corewifi] >>> @[%!l(MISSING)lu.%!l(MISSING)lu] %!{(MISSING)public}s (%!{(MISSING)public}s:%!u(MISSING)) "
+ "[corewifi] AUTO-JOIN: Queueing block for new auto-join trigger with higher QoS (qos=%!d(MISSING), prev=%!d(MISSING), trigger=%!{(MISSING)public}@)"
+ "[corewifi] AUTO-JOIN: Will run request (qos=%!d(MISSING), request=%!{(MISSING)public}@"
+ "__qosForAutoJoinTrigger:"
+ "_highestPendingQoS"
+ "numberWithUnsignedShort:"
- "\x051\x17\x15\x15!!\x19\x13/\x02"
- "SCAN_BSS_TYPE"
- "SCAN_CHANNELS"
- "SCAN_DWELL_TIME"
- "SCAN_FLAGS"
- "SCAN_MERGE"
- "SCAN_NUM_SCANS"
- "SCAN_PHY_MODE"
- "SCAN_REST_TIME"
- "SCAN_SSID_LIST"
- "SCAN_TYPE"
- "__scanDictionaryWithParameters:"

```
