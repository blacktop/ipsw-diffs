## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`

```diff

-41.7.0.0.0
-  __TEXT.__text: 0x250fec
+42.4.1.0.0
+  __TEXT.__text: 0x253e40
   __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__objc_stubs: 0x1f440
-  __TEXT.__objc_methlist: 0xea04
-  __TEXT.__const: 0x4da0
-  __TEXT.__gcc_except_tab: 0x5a3c
-  __TEXT.__cstring: 0x59333
-  __TEXT.__objc_classname: 0x1193
-  __TEXT.__objc_methname: 0x2d595
-  __TEXT.__objc_methtype: 0x42e2
+  __TEXT.__objc_stubs: 0x1f8c0
+  __TEXT.__objc_methlist: 0xec2c
+  __TEXT.__const: 0x4d70
+  __TEXT.__gcc_except_tab: 0x5a7c
+  __TEXT.__cstring: 0x59c53
+  __TEXT.__objc_classname: 0x11a3
+  __TEXT.__objc_methname: 0x2db75
+  __TEXT.__objc_methtype: 0x43a9
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x9efa
   __TEXT.__ustring: 0x10

   __TEXT.__swift_as_cont: 0xe8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x9798
+  __TEXT.__unwind_info: 0x98d0
   __TEXT.__eh_frame: 0x2db8
-  __DATA_CONST.__const: 0xce90
-  __DATA_CONST.__cfstring: 0xbba0
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__const: 0xcf58
+  __DATA_CONST.__cfstring: 0xbb40
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__auth_got: 0x1e50
-  __DATA_CONST.__got: 0x1158
+  __DATA_CONST.__got: 0x1170
   __DATA_CONST.__auth_ptr: 0x7c0
-  __DATA.__objc_const: 0x20490
-  __DATA.__objc_selrefs: 0x9360
-  __DATA.__objc_ivar: 0x18a0
-  __DATA.__objc_data: 0x36d8
-  __DATA.__data: 0x59c0
+  __DATA.__objc_const: 0x20800
+  __DATA.__objc_selrefs: 0x94a8
+  __DATA.__objc_ivar: 0x18ec
+  __DATA.__objc_data: 0x3728
+  __DATA.__data: 0x5a30
   __DATA.__common: 0x3a8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12102
-  Symbols:   1707
-  CStrings:  16434
+  Functions: 12180
+  Symbols:   1710
+  CStrings:  16525
 
Symbols:
+ _NRPairedDeviceRegistryWatchDidBecomeActiveDarwinNotification
+ _OBJC_CLASS_$_AAAccessoryUsageEvent
+ _OBJC_CLASS_$_DADaemonSession
+ _OBJC_CLASS_$_NSTimeZone
- _OBJC_CLASS_$_DASession
CStrings:
+ "    [%zu] isUsed %d, %@\n"
+ "### Accessory Usage History Activate failed: %{error}"
+ "### Failed to archive usage events: %{error}"
+ "### Failed to unarchive usage events: %{error}"
+ "### Fetch usage history failed: %{error}"
+ "### Third-party discovery activate failed: %@"
+ ","
+ "-- AAAccessoryUsageHistoryDaemon --\n"
+ "-[AAAccessoryUsageHistoryDaemon _appendEvent:]"
+ "-[AAAccessoryUsageHistoryDaemon _deviceDiscoveryEnsureStarted]"
+ "-[AAAccessoryUsageHistoryDaemon _deviceDiscoveryEnsureStarted]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon _deviceDiscoveryEnsureStarted]_block_invoke_4"
+ "-[AAAccessoryUsageHistoryDaemon _deviceUpdated:]"
+ "-[AAAccessoryUsageHistoryDaemon _invalidated]"
+ "-[AAAccessoryUsageHistoryDaemon _loadEventsFromPreference]"
+ "-[AAAccessoryUsageHistoryDaemon _reevaluateCapabilityGate]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon _saveEventsToPreference]"
+ "-[AAAccessoryUsageHistoryDaemon _startStartupGracePeriod]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon _thirdPartyDeviceFound:]"
+ "-[AAAccessoryUsageHistoryDaemon _thirdPartyDiscoveryEnsureStarted]"
+ "-[AAAccessoryUsageHistoryDaemon _thirdPartyDiscoveryEnsureStarted]_block_invoke_3"
+ "-[AAAccessoryUsageHistoryDaemon activate]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon audioRouteChanged:withUUID:]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon invalidate]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon localAudioCategoryChanged:]_block_invoke"
+ "-[AAAccessoryUsageHistoryDaemon otherTipiAudioCategoryChanged:forAddress:]_block_invoke"
+ "-[AAServicesXPCConnection activateAccessoryUsageHistoryManager:completion:]"
+ "-[AAServicesXPCConnection activateAccessoryUsageHistoryManager:completion:]_block_invoke"
+ "-[AAServicesXPCConnection fetchAccessoryUsageHistory:interval:completion:]"
+ "3P device classified: %@ deviceType=%d userSelectedDeviceType=%d appearanceValue=%d -> headphone=%d"
+ "704c505e-d459-42a9-b3b1-81b4cfa5911d"
+ "@\"AAAccessoryUsageHistoryManager\""
+ "@\"DADaemonSession\""
+ "AAAccessoryUsageHistory"
+ "AAAccessoryUsageHistoryDaemon"
+ "AADeviceManager: send config: %@, to device with identifier: %@, from client: %#{pid}"
+ "Appending usage event: %@"
+ "Capability gate closed - stopping device discovery"
+ "Capability gate opened - starting device discovery"
+ "Capability gate: exclaveCapable %d, watchCapable %d"
+ "DADaemonSession started"
+ "DADaemonSession stopped"
+ "Device updated: %@, listeningMode %s, audioStreamState %s, routed %d, primaryPlacement %s, secondaryPlacement %s"
+ "FetchDADevices: DADaemonSession not available"
+ "FetchDADevices: Getting devices from DADaemonSession"
+ "Loaded %zu usage event(s) from preference"
+ "Removed %@ from incomingPairedDevices (removal initiated %{public}@)"
+ "SetTCCFeatureSupport: DADaemonSession not available"
+ "SmartRouting audio route changed: route %d, routedAddress %@"
+ "SmartRouting local audio category changed: %@"
+ "SmartRouting other Tipi audio category changed: %@, category %u"
+ "Startup grace period ended"
+ "T@\"AAAccessoryUsageHistoryManager\",&,N,V_accessoryUsageHistoryManager"
+ "Third-party device discovery start"
+ "Third-party discovery activated"
+ "Usage events: %zu\n"
+ "Usage events: %zu (newest %zu shown)\n"
+ "[_updateCloudRecordIfNeeded] Back off! Not saving to cloud just yet"
+ "[updatePairedDeviceWithIdentifier] Back off! Not saving to cloud just yet"
+ "_accessoryUsageHistoryManager"
+ "_appendEvent:"
+ "_connectedThirdPartyHeadphones"
+ "_daDaemonSession"
+ "_deviceRemoved:"
+ "_events"
+ "_isAirPodsStreaming:"
+ "_isAnyDeviceANCOn"
+ "_isAnyDeviceRawStreaming"
+ "_isAudioCategoryAtLeastMediaPlayback:"
+ "_isDeviceANCOn:"
+ "_isDeviceWorn:"
+ "_isHeadphoneAppearanceValue:"
+ "_isHeadphoneInUsed"
+ "_isLocalAudioPlayingOnThirdPartyHeadphone:"
+ "_isOtherTipiDevicePlayingAudioOnAirPods:"
+ "_isPlacementWorn:"
+ "_isThirdPartyHeadphone:"
+ "_isWatchMindPalaceCapable"
+ "_lastKnownBTRoutedAddress"
+ "_lastKnownLocalAudioCategory"
+ "_loadEventsFromPreference"
+ "_nrRegistry"
+ "_otherTipiAudioCategories"
+ "_pruneExpiredEvents"
+ "_recomputeIsHeadphoneInUsed"
+ "_reevaluateCapabilityGate"
+ "_registerCapabilityGateObserver"
+ "_saveEventsToPreference"
+ "_startStartupGracePeriod"
+ "_startupGraceSinceDate"
+ "_streamingSinceDate"
+ "_streamingSustained"
+ "_thirdPartyDeviceFound:"
+ "_thirdPartyDeviceLost:"
+ "_thirdPartyDiscovery"
+ "_thirdPartyDiscoveryEnsureStarted"
+ "_thirdPartyDiscoveryEnsureStopped"
+ "accessoryUsageHistoryManager"
+ "activateAccessoryUsageHistoryManager:completion:"
+ "af1ab168-c48a-48c1-b3ed-cc77c9429eea"
+ "appearanceValue"
+ "fetchAccessoryUsageHistory:interval:completion:"
+ "fetchUsageHistoryForInterval:completionHandler:"
+ "initWithUsed:timestamp:"
+ "isUsed"
+ "localTimeZone"
+ "otherTipiAudioCategoryChanged:forAddress:"
+ "removeObjectsInRange:"
+ "setAccessoryUsageHistoryManager:"
+ "setTimeZone:"
+ "sharedAccessoryUsageHistoryDaemon"
+ "supportsCapability:"
+ "unarchivedArrayOfObjectsOfClass:fromData:error:"
+ "userSelectedDeviceType"
+ "v32@0:8@\"AAAccessoryUsageHistoryManager\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"AAAccessoryUsageHistoryManager\"16@\"NSDateInterval\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "yyyy-MM-dd HH:mm:ss.SSS ZZZ"
- "%@-Seed-mov"
- "+"
- "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
- "-[BTServicesDaemon openRadarforAudioQuality]"
- "1551854"
- "815886"
- "@\"DASession\""
- "AADeviceManager: send config: %@, to device with identifier: %@"
- "Back off! Not saving to cloud just yet"
- "Bluetooth Audio Quality Feedback"
- "CoreBluetooth - HFP Audio | iOS"
- "DASession started"
- "DASession stopped"
- "FetchDADevices: DASession not available"
- "FetchDADevices: Getting devices from DASession"
- "Keywords"
- "Performance"
- "Removed %@ from incomingPairedDevices"
- "SetTCCFeatureSupport: DASession not available"
- "_daSession"
- "audioQuality - File Radar"
- "audioQuality banner timeout"
- "audioQuality user click, openradar"
- "audioQuality user dismiss"
- "audioQuality: banner action: %s, %{error}"
- "audioQuality: banner error for device %@"
```
