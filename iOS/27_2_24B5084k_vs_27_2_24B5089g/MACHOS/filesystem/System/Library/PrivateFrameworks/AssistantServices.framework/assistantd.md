## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-3605.23.1.1.1
-  __TEXT.__text: 0x375518
-  __TEXT.__auth_stubs: 0x3900
-  __TEXT.__objc_stubs: 0x48400
-  __TEXT.__objc_methlist: 0x24040
-  __TEXT.__const: 0xede0
+3605.24.1.1.1
+  __TEXT.__text: 0x377220
+  __TEXT.__auth_stubs: 0x3910
+  __TEXT.__objc_stubs: 0x48560
+  __TEXT.__objc_methlist: 0x240f0
+  __TEXT.__const: 0xede8
   __TEXT.__dlopen_cstrs: 0x9e9
-  __TEXT.__gcc_except_tab: 0x3c14
-  __TEXT.__cstring: 0x54ba5
-  __TEXT.__oslogstring: 0x491a6
-  __TEXT.__objc_classname: 0x5273
-  __TEXT.__objc_methname: 0x6388e
-  __TEXT.__objc_methtype: 0x1021b
+  __TEXT.__gcc_except_tab: 0x3cc0
+  __TEXT.__cstring: 0x54fff
+  __TEXT.__oslogstring: 0x49755
+  __TEXT.__objc_classname: 0x52bc
+  __TEXT.__objc_methname: 0x63aa3
+  __TEXT.__objc_methtype: 0x10250
   __TEXT.__ustring: 0x98
-  __TEXT.__unwind_info: 0xd080
+  __TEXT.__unwind_info: 0xd0e8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x146a0
-  __DATA_CONST.__cfstring: 0x12ca0
-  __DATA_CONST.__objc_classlist: 0xd60
+  __DATA_CONST.__const: 0x147f8
+  __DATA_CONST.__cfstring: 0x12f40
+  __DATA_CONST.__objc_classlist: 0xd70
   __DATA_CONST.__objc_catlist: 0x630
-  __DATA_CONST.__objc_protolist: 0x730
+  __DATA_CONST.__objc_protolist: 0x738
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0xb30
-  __DATA_CONST.__objc_arraydata: 0x480
-  __DATA_CONST.__objc_arrayobj: 0x198
+  __DATA_CONST.__objc_superrefs: 0xb38
+  __DATA_CONST.__objc_arraydata: 0x530
+  __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_intobj: 0x8e8
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1c90
-  __DATA_CONST.__got: 0x3ea0
+  __DATA_CONST.__auth_got: 0x1c98
+  __DATA_CONST.__got: 0x3eb8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x35708
-  __DATA.__objc_selrefs: 0x15ab0
-  __DATA.__objc_ivar: 0x2760
-  __DATA.__objc_data: 0x85c0
-  __DATA.__data: 0x5db8
+  __DATA.__objc_const: 0x35988
+  __DATA.__objc_selrefs: 0x15b28
+  __DATA.__objc_ivar: 0x2774
+  __DATA.__objc_data: 0x8660
+  __DATA.__data: 0x5e20
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14866
-  Symbols:   3022
-  CStrings:  28469
+  Functions: 14889
+  Symbols:   3024
+  CStrings:  28547
 
Symbols:
+ _OBJC_CLASS_$_SCDADeviceNameInfo
+ _TCCAccessCopyBundleIdentifiersDisabledForService
CStrings:
+ "%s %{public}s activity error: %{public}@"
+ "%s Activity %{public}s completed but another path already owns its transition; not setting done"
+ "%s Activity %{public}s did not accept DEFER during clean exit; it had already left the state we tried to release"
+ "%s Activity %{public}s finished, but the registry slot holds a DIFFERENT run; leaving it for its own owner"
+ "%s Activity %{public}s started while a previous run was still tracked (%{public}s object); the displaced run is unaccounted for"
+ "%s App %@ is excluded from Siri, not speaking announcement on platform: %@"
+ "%s App exclusion check for %@: excluded=%{BOOL}d, denyCount=%lu, expandedCount=%lu"
+ "%s App exclusions disabled by feature flag; treating %@ as not excluded"
+ "%s Clean exit: %lu of %lu in-flight XPC activit(ies) accepted a terminal transition for a pending clean exit"
+ "%s Deferring activity:%{public}s deferred:%{public}s"
+ "%s Failed setting activity state to continue for %{public}s"
+ "%s Failed setting activity state to done for %{public}s"
+ "%s Not deferring %{public}s: another path already owns its transition"
+ "%s Not starting activity %{public}s: the daemon began exiting cleanly. Releasing it."
+ "%s Not starting activity %{public}s: the daemon is exiting cleanly. Releasing it."
+ "%s Pending asset-fetch backstop count is unexpectedly large: %lu (threshold %lu), most recent language '%{public}@'. Either a client is looping on the asset-status XPC, or a tracking entry is being orphaned."
+ "%s Skipping CDM asset-status registration: no language code at registration time."
+ "%s Unable to retrieve LSApplicationRecord for %@: %@"
+ "%s getCompanionInfoFor couldn't find sharedUserId: %@ (primary user is %{private}@)"
+ "-[ADAssetManager _registerCDMStatusTrackerForLanguage:]"
+ "-[ADAssetManager fetchAssetsAvailabilityForLanguage:completion:]_block_invoke"
+ "/System/Library/Frameworks/CoreServices.framework/CoreServices"
+ "@\"SCDADeviceNameInfo\"24@0:8@\"NSString\"16"
+ "ADAppIsExcludedFromSiri"
+ "ADSCDADeviceNameResolver"
+ "B16@?0@\"NSObject<OS_xpc_object>\"8"
+ "MobileAssistantDaemons-3605.24.1.1.1"
+ "SCDADeviceNameResolving"
+ "_ADBundleIDIsAppClip"
+ "_ADDeferActivityIfExitingCleanly"
+ "_ADDeferInFlightActivitiesForExit"
+ "_ADFinishInFlightActivity"
+ "_ADHandleActivityState"
+ "_ADReleaseActivityForExit"
+ "_ADRunActivity"
+ "_ADSyncReplyGraphCanary"
+ "_ADTrackInFlightActivity"
+ "_ADUntrackInFlightActivity"
+ "_assetFetchCancelGeneration"
+ "_cancelPendingAssetFetchBackstopsOnQueue"
+ "_existingSharedStore"
+ "_isAppExcludedFromSiri:"
+ "_maxObservedPendingAssetFetchBackstops"
+ "_pendingAssetFetchBackstops"
+ "_registerCDMStatusTrackerForLanguage:"
+ "_syncExitFinishers"
+ "_syncExitLock"
+ "_syncExit_armFinisher:"
+ "_syncExit_drainForReason:"
+ "_syncExit_handleDaemonWillExitCleanly:"
+ "_syncExit_retireFinisher:"
+ "appClipMetadata"
+ "appExcludedFromSiri"
+ "com.apple.Fitness"
+ "com.apple.Health"
+ "com.apple.HeartRate"
+ "com.apple.Mind"
+ "com.apple.NanoHeartRhythm"
+ "com.apple.NanoMedications"
+ "com.apple.NanoMenstrualCycles"
+ "com.apple.NanoOxygenSaturation.watchkitapp"
+ "com.apple.NanoSleep.watchkitapp"
+ "com.apple.NanoStopwatch"
+ "com.apple.NanoWorldClock"
+ "com.apple.Noise"
+ "com.apple.app-clips"
+ "com.apple.findmy"
+ "com.apple.findmy.finddevices"
+ "com.apple.findmy.finditems"
+ "com.apple.findmy.findpeople"
+ "com.apple.findmy.watchapp"
+ "com.apple.mobiletimer"
+ "counterpartIdentifiers"
+ "daemon began exiting cleanly mid-sync"
+ "deviceNameResolver"
+ "different"
+ "initWithRoomName:deviceName:"
+ "isAppExclusionsEnabled"
+ "kTCCServiceSiriAccess"
+ "namesForIdsDeviceUniqueIdentifier:"
+ "removeObjectIdenticalTo:"
+ "same"
+ "setDeviceNameResolver:"
+ "the settings connection was invalidated before the sync finished"
+ "the settings connection went away before the sync finished"
+ "v24@0:8r*16"
+ "v32@?0@\"NSString\"8@16^B24"
- "%s %s activity error: %@"
- "%s Deferring activity:%@ deferred:%@"
- "%s Failed setting activity state to continue"
- "%s Failed setting activity state to done"
- "%s getCompanionInfoFor couldn't find sharedUserId: %@"
- "-[ADAssetManager _registerCDMStatusTracker]"
- "MobileAssistantDaemons-3605.23.1.1.1"
- "_RegisterXPCActivity_block_invoke"
- "_registerCDMStatusTracker"
```
