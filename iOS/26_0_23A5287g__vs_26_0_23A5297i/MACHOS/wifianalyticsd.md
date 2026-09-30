## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-776.83.4.1.0
-  __TEXT.__text: 0x97ab4
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_stubs: 0x8940
-  __TEXT.__objc_methlist: 0x3434
-  __TEXT.__const: 0x408
+776.85.0.0.0
+  __TEXT.__text: 0x99d40
+  __TEXT.__auth_stubs: 0x1650
+  __TEXT.__objc_stubs: 0x8980
+  __TEXT.__objc_methlist: 0x344c
+  __TEXT.__const: 0x418
   __TEXT.__dlopen_cstrs: 0x1e2
-  __TEXT.__cstring: 0x13e79
-  __TEXT.__constg_swiftt: 0x424
-  __TEXT.__swift5_typeref: 0x2de
+  __TEXT.__cstring: 0x13ecf
+  __TEXT.__constg_swiftt: 0x43c
+  __TEXT.__swift5_typeref: 0x2f2
   __TEXT.__swift5_fieldmd: 0x1e0
-  __TEXT.__oslogstring: 0x1384e
+  __TEXT.__oslogstring: 0x13df7
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_reflstr: 0x10b
-  __TEXT.__objc_methname: 0xd81c
-  __TEXT.__swift5_capture: 0x148
+  __TEXT.__objc_methname: 0xd850
+  __TEXT.__swift5_capture: 0x158
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__gcc_except_tab: 0x51e8
   __TEXT.__objc_classname: 0x334
   __TEXT.__objc_methtype: 0x10a2
-  __TEXT.__unwind_info: 0x10d0
-  __TEXT.__eh_frame: 0x2c8
-  __DATA_CONST.__auth_got: 0xb50
+  __TEXT.__unwind_info: 0x10e0
+  __TEXT.__eh_frame: 0x2d8
+  __DATA_CONST.__auth_got: 0xb40
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x1aa0
-  __DATA_CONST.__cfstring: 0x10560
+  __DATA_CONST.__const: 0x1ac8
+  __DATA_CONST.__cfstring: 0x105a0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x408
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA.__objc_const: 0x5498
-  __DATA.__objc_selrefs: 0x2da0
+  __DATA.__objc_selrefs: 0x2db0
   __DATA.__objc_ivar: 0x4fc
-  __DATA.__objc_data: 0x9d8
-  __DATA.__data: 0x9b8
+  __DATA.__objc_data: 0x9f0
+  __DATA.__data: 0x9c8
   __DATA.__bss: 0x208
   __DATA.__common: 0x88
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 74FC8499-F115-34FB-90C8-778EF70750F4
-  Functions: 1497
-  Symbols:   543
-  CStrings:  8275
+  UUID: 84CB85DC-FD2E-3BAA-B28F-456D56C92A01
+  Functions: 1506
+  Symbols:   541
+  CStrings:  8296
 
Symbols:
- _$s6Darwin0A7BooleanV11descriptionSSvg
- _swift_errorRelease
CStrings:
+ "\"WiFiAnalytics_executables-776.85\""
+ "%{public}s::%d:Dictionary contains multiple entries with hashID %@ at index %@ and at index %@"
+ "%{public}s::%d:_triggerQueryForNWActivityWithPeers peersArr hasDup %@"
+ "-[WAEngine hasDuplicateHashIDs:]"
+ "Deinit PeerEntry key %s %s"
+ "Init PeerEntry key %s %s"
+ "Jul 12 2025 01:09:29"
+ "WiFiAnalytics_executables-776.85"
+ "WiFiAnalytics_executables-776.85 Jul 12 2025 01:09:26"
+ "alreadyContainsHashID:inArray:"
+ "createSubscriptionForPeer: Error IOReporters don't exist yet for peer: %s"
+ "createSubscriptionForPeer: Error calling IOReportCreateSubscription on peer %s Error: %@"
+ "createSubscriptionForPeer: Error failed to create subscription candidates for peer: %s"
+ "createSubscriptionForPeer: Error finding drvName or providerService or providerNum"
+ "createSubscriptionForPeer: Fetching legend for peer: %s"
+ "createSubscriptionForPeer: Success fetching legend peer: %s %s legend.count: %ld"
+ "createSubscriptionForPeer: Zero result fetching peer: %s error: %{bool}d for: %s"
+ "getRegistryEntryID: Failed calling IORegistryEntryGetRegistryEntryID for entry: %u"
+ "hasDuplicateHashIDs:"
+ "hashID"
+ "peerEntryRSSIStateNoLongerExists: getIOReportLegend for peer %s encountered error, assuming noLongerExists"
+ "peerEntryRSSIStateNoLongerExists: getIOReportLegend for peer %s returned no results, assuming noLongerExists"
+ "peerEntryRSSIStateNoLongerExists: peer %s RSSI State not yet found, can't determine if its existence has changed"
+ "peerEntryRSSIStateNotYetFound: peer %s missing important RSSI State"
+ "sampleTrackedPeers: Adding keysNeedingNewSubscription peer %s missingPredicates: %{bool}d subscription %s subbedChs: %s"
+ "sampleTrackedPeers: Adding keysNoLongerExisting peer %s"
+ "sampleTrackedPeers: Attempting to sample IOReportCreateSamples on peer %s"
+ "sampleTrackedPeers: Converted %s peerDict is %s"
+ "sampleTrackedPeers: Converting samples to peerDict for %s"
+ "sampleTrackedPeers: ERROR cant access peer %s"
+ "sampleTrackedPeers: Error calling IOReportCreateSamples on peer %s Error: %@"
+ "sampleTrackedPeers: PeerEntry %s incomplete entry: %s"
+ "sampleTrackedPeers: Removing keysNeedingNewSubscription peer %s"
+ "sampleTrackedPeers: Removing keysNoLongerExisting peer %s"
+ "sampleTrackedPeers: Removing keysToPurgeForProducingErrors peer %s for previous encounterd errors"
+ "sampleTrackedPeers: Returning ret %s"
+ "sampleTrackedPeers: Success calling IOReportCreateSamples on peer %s"
+ "sampleTrackedPeers: createSubscriptionForPeer %s"
+ "sampleTrackedPeers: mergedDictionary is now %s"
+ "updateTrackedPeers: Added peer: %s Subscription"
+ "updateTrackedPeers: Bad list of peers"
- "\"WiFiAnalytics_executables-776.83.4.1\""
- "Added peer: %s Subscription"
- "Adding keysNeedingNewSubscription peer %s missingPredicates: %{bool}d subscription %s subbedChs: %s"
- "Bad list of peers"
- "Deinit PeerEntry %s"
- "Error IOReporters don't exist yet for peer: %s"
- "Error calling IOReportCreateSamples on peer %s Error: %@"
- "Error calling IOReportCreateSubscription on peer %s Error: %@"
- "Error failed to create subscription candidates for peer: %s"
- "Error finding drvName or providerService or providerNum"
- "Failed calling IORegistryEntryGetRegistryEntryID for entry: %u"
- "Init PeerEntry %s"
- "Jun 30 2025 22:29:41"
- "PeerEntry %s incomplete entry: %s"
- "Removing keysNeedingNewSubscription peer %s"
- "Removing keysToPurgeForProducingErrors peer %s for previous encounterd errors"
- "Success calling IOReportCreateSamples on peer %s"
- "Success fetching legend peer: %s %s legend.count: %ld"
- "WiFiAnalytics_executables-776.83.4.1"
- "WiFiAnalytics_executables-776.83.4.1 Jun 30 2025 22:29:39"
- "Zero result fetching peer: %s error: %s for: %s"
- "createSubscriptionForPeer %s"
- "peer %s missing important RSSI State"

```
