## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2467.2.2.0.0
-  __TEXT.__text: 0x1721bc
-  __TEXT.__auth_stubs: 0x2230
-  __TEXT.__objc_stubs: 0x1b040
-  __TEXT.__objc_methlist: 0x131f4
-  __TEXT.__const: 0x1568
-  __TEXT.__objc_methname: 0x2e5bd
-  __TEXT.__cstring: 0x10586
-  __TEXT.__oslogstring: 0x16c79
+2467.40.37.0.0
+  __TEXT.__text: 0x175100
+  __TEXT.__auth_stubs: 0x2240
+  __TEXT.__objc_stubs: 0x1b380
+  __TEXT.__objc_methlist: 0x1334c
+  __TEXT.__const: 0x1578
+  __TEXT.__objc_methname: 0x2ebb5
+  __TEXT.__cstring: 0x10706
+  __TEXT.__oslogstring: 0x171a9
   __TEXT.__objc_classname: 0x1ca8
-  __TEXT.__objc_methtype: 0x4201
-  __TEXT.__gcc_except_tab: 0x4f78
+  __TEXT.__objc_methtype: 0x4231
+  __TEXT.__gcc_except_tab: 0x502c
   __TEXT.__dlopen_cstrs: 0x552
   __TEXT.__swift5_typeref: 0x966
   __TEXT.__swift5_capture: 0x220

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6438
+  __TEXT.__unwind_info: 0x6520
   __TEXT.__eh_frame: 0xbd0
-  __DATA_CONST.__const: 0x4f00
-  __DATA_CONST.__cfstring: 0x11940
+  __DATA_CONST.__const: 0x4fa8
+  __DATA_CONST.__cfstring: 0x11ae0
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x218

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x5c0
   __DATA_CONST.__objc_intobj: 0x17b8
-  __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA_CONST.__objc_dictobj: 0x208
+  __DATA_CONST.__objc_arraydata: 0x4a0
+  __DATA_CONST.__objc_arrayobj: 0x1c8
+  __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA_CONST.__auth_got: 0x1128
-  __DATA_CONST.__got: 0xe38
+  __DATA_CONST.__auth_got: 0x1130
+  __DATA_CONST.__got: 0xe58
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x33ed8
-  __DATA.__objc_selrefs: 0x9cf0
-  __DATA.__objc_ivar: 0x1630
+  __DATA.__objc_const: 0x33fc8
+  __DATA.__objc_selrefs: 0x9e20
+  __DATA.__objc_ivar: 0x1644
   __DATA.__objc_data: 0x4908
-  __DATA.__data: 0x2190
+  __DATA.__data: 0x21a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8351
-  Symbols:   1014
-  CStrings:  12452
+  Functions: 8411
+  Symbols:   1019
+  CStrings:  12534
 
Symbols:
+ _BMCarPlayConnectedIdentifier
+ _BMDeviceActivityPredictionIdentifier
+ _BMDeviceWirelessNFCTagIdentifier
+ _BMMediaNowPlayingIdentifier
+ _dispatch_assert_queue_not$V2
CStrings:
+ "%@ is %d"
+ "%{public}@: Process %d requested host-managed UI without the %{public}@ vouch"
+ "/carplay/connected"
+ "/device/activityPrediction"
+ "/device/nfcTagRead"
+ "/media/nowPlayingPlaybackState"
+ "@36@0:8@16i24d28"
+ "@52@0:8@16@24B32@36^@44"
+ "Adding %@ as stream for dasdDataCollection"
+ "App is not permitted to suppress system-vended progress UI."
+ "BAR re-enabled for %@"
+ "BARSchedulingDisabled"
+ "Convert stream: %@ : Failed to save %lu events: %@"
+ "Convert stream: %@ : Failed to save %lu final events: %@"
+ "Convert stream: %@ : Timed out waiting for conversion to complete"
+ "ERROR Submitting Activity: %@ due to configuration limits. Please contact us to prevent this activity from getting rejected. Configuration: %@"
+ "HostManagedProgressUI"
+ "Loaded trial parameter MLFreezerAllowListSpotlightEnabled: %d"
+ "MLFreezerAllowListSpotlightEnabled"
+ "Missing Tag"
+ "No bundleIdentifier was associated with the process handle, ignoring suspension update"
+ "Override status: %@"
+ "Remote Notification: %@ - BAR Scheduling Disabled by Trial"
+ "Siri AI"
+ "T@\"NSMutableSet\",&,N,V_suspendedBundleIDs"
+ "T@\"RBSProcessMonitor\",&,N,V_suspensionMonitor"
+ "TB,N,V_barSchedulingDisabledByTrial"
+ "TB,N,V_siriAIAllowListEnabled"
+ "TB,N,V_spotlightAllowListEnabled"
+ "TB,N,V_suspensionSendPending"
+ "Trial parameter MLFreezerAllowListSpotlightEnabled not found, using default: %d"
+ "Unable to resolve the client process handle; treating host-managed UI as unvouched"
+ "[%{public}@] Host manages its own UI; suppressing system-vended progress for %{public}@"
+ "[%{public}@] Not posting %@; host manages its own UI"
+ "_barSchedulingDisabledByTrial"
+ "_siriAIAllowListEnabled"
+ "_spotlightAllowListEnabled"
+ "_suspendedBundleIDs"
+ "_suspensionMonitor"
+ "_suspensionSendPending"
+ "activityPredictionEventForStream:eventBody:atTimestamp:"
+ "barSchedulingDisabledByTrial"
+ "confidenceLevel"
+ "currentStateMatchingDescriptor:"
+ "defaultPathIsInexpensive"
+ "defaultPathIsUnconstrained"
+ "directBiomeWriterStreamNames"
+ "handleSuspensionStateTransitionForProcess:withUpdate:"
+ "hasHostManagedProgressUIVouch"
+ "hostManagedProgressUI"
+ "initWithDKStreamIdentifier:"
+ "intervalEventForStream:openIntervalStartDate:starting:atTimestamp:newOpenIntervalStartDate:"
+ "isConstrained"
+ "isExpensive"
+ "isMindPalaceAmbientActivity"
+ "isMindPalaceUserInitiatedActivity"
+ "mindPalaceAmbient == 1"
+ "nfcTagEventForStream:atTimestamp:"
+ "nowPlayingEventForStream:playbackState:atTimestamp:"
+ "outputReason"
+ "playbackState"
+ "registerSuspensionMonitor"
+ "scheduleSuspensionSend"
+ "sendCachedFreezerRecommendationsOnSuspension"
+ "setBarSchedulingDisabledByTrial:"
+ "setSiriAIAllowListEnabled:"
+ "setSpotlightAllowListEnabled:"
+ "setSuspendedBundleIDs:"
+ "setSuspensionMonitor:"
+ "setSuspensionSendPending:"
+ "shouldPresentUIForActivity:"
+ "siriAIAllowListEnabled"
+ "spotlightAllowListEnabled"
+ "suspendedBundleIDs"
+ "suspensionMonitor"
+ "suspensionSendPending"
+ "tags"
+ "tagsVouchForHostManagedProgressUI:"
+ "v16@?0@\"_DKEvent\"8"
+ "v24@?0@?<v@?@\"_DKEvent\">8@?<v@?>16"
+ "writeActivityPredictionStream:toFileHandle:withEventPredicate:"
+ "writeCarPlayConnectedStream:toFileHandle:withEventPredicate:"
+ "writeDirectStreamName: %@ : Processed events are not valid JSON objects, skipping with error %@"
+ "writeDirectStreamName: %@ : Timed out waiting for write to complete, numberOfWrittenEvents may be an undercount"
+ "writeDirectStreamName: %@ : written %lu events, total written so far: %lu"
+ "writeDirectStreamName:toFileHandle:withEventPredicate:withEventProvider:"
+ "writeExperiment: %@ : stream %@ is in directBiomeWriterStreamNames but has no direct writer wired up"
+ "writeKeybagLockedStream:toFileHandle:withEventPredicate:"
+ "writeNFCTagStream:toFileHandle:withEventPredicate:"
+ "writeNowPlayingStream:toFileHandle:withEventPredicate:"
+ "writeStream: %@ : Timed out waiting for read to complete, numberOfWrittenEvents may be an undercount"
- "Campo"
- "ERROR Submitting Activity: %@ due to configuration limits. Please contact das-core@group.apple.com to prevent this activity from getting rejected. Configuration: %@"
- "TB,N,V_campoAllowListEnabled"
- "_campoAllowListEnabled"
- "campoAllowListEnabled"
- "convertKeybagLockedStream:toKnowledgeStoreStream:"
- "inexpensivePathAvailable"
- "initWithDKStreamIdentifier:contentProtection:"
- "setCampoAllowListEnabled:"
```
