## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-24310.24.46.301.0
-  __TEXT.__text: 0x31e1c0
-  __TEXT.__auth_stubs: 0x4f30
-  __TEXT.__objc_methlist: 0x11ef8
-  __TEXT.__cstring: 0x282d8
-  __TEXT.__const: 0xa2d0
+24400.24.47.401.0
+  __TEXT.__text: 0x326798
+  __TEXT.__auth_stubs: 0x4fb0
+  __TEXT.__objc_methlist: 0x11f38
+  __TEXT.__cstring: 0x287bc
+  __TEXT.__const: 0xa2e0
   __TEXT.__constg_swiftt: 0x5ad8
-  __TEXT.__swift5_typeref: 0x3ec3
+  __TEXT.__swift5_typeref: 0x3f03
   __TEXT.__swift5_reflstr: 0x3701
   __TEXT.__swift5_fieldmd: 0x37c8
   __TEXT.__swift5_builtin: 0x618

   __TEXT.__swift5_types: 0x3e8
   __TEXT.__swift5_mpenum: 0xc4
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__oslogstring: 0x2df0c
-  __TEXT.__swift5_capture: 0x2cac
-  __TEXT.__gcc_except_tab: 0x5e58
+  __TEXT.__oslogstring: 0x2ea89
+  __TEXT.__swift5_capture: 0x2d18
+  __TEXT.__gcc_except_tab: 0x5e68
   __TEXT.__ustring: 0x354
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__unwind_info: 0xa068
-  __TEXT.__eh_frame: 0x74a8
+  __TEXT.__unwind_info: 0xa138
+  __TEXT.__eh_frame: 0x77b8
   __TEXT.__objc_classname: 0x39ea
-  __TEXT.__objc_methname: 0x36157
-  __TEXT.__objc_methtype: 0x8fc5
-  __TEXT.__objc_stubs: 0x25100
-  __DATA_CONST.__got: 0x2c80
-  __DATA_CONST.__const: 0x8db8
-  __DATA_CONST.__objc_classlist: 0xbe8
+  __TEXT.__objc_methname: 0x361a9
+  __TEXT.__objc_methtype: 0x8fe4
+  __TEXT.__objc_stubs: 0x25120
+  __DATA_CONST.__got: 0x2c88
+  __DATA_CONST.__const: 0x8da0
+  __DATA_CONST.__objc_classlist: 0xbf0
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x750
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb550
+  __DATA_CONST.__objc_selrefs: 0xb558
   __DATA_CONST.__objc_protorefs: 0x350
   __DATA_CONST.__objc_superrefs: 0x698
-  __DATA_CONST.__objc_arraydata: 0x238
-  __AUTH_CONST.__auth_got: 0x27a8
-  __AUTH_CONST.__auth_ptr: 0xad8
-  __AUTH_CONST.__const: 0xc7d0
-  __AUTH_CONST.__cfstring: 0x1af20
-  __AUTH_CONST.__objc_const: 0x33c58
+  __DATA_CONST.__objc_arraydata: 0x240
+  __AUTH_CONST.__auth_got: 0x27e8
+  __AUTH_CONST.__auth_ptr: 0xa50
+  __AUTH_CONST.__const: 0xc938
+  __AUTH_CONST.__cfstring: 0x1b0c0
+  __AUTH_CONST.__objc_const: 0x33d18
   __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x40d8
-  __AUTH.__data: 0x16f8
-  __DATA.__objc_ivar: 0x18a0
-  __DATA.__data: 0x5d38
+  __AUTH.__objc_data: 0x4148
+  __AUTH.__data: 0x1738
+  __DATA.__objc_ivar: 0x18a4
+  __DATA.__data: 0x5d80
   __DATA.__bss: 0xa918
-  __DATA.__common: 0xa0
+  __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x4cf0
-  __DATA_DIRTY.__data: 0x4f78
+  __DATA_DIRTY.__data: 0x4f48
   __DATA_DIRTY.__bss: 0x2ac0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15941
-  Symbols:   11527
-  CStrings:  17096
+  Functions: 16003
+  Symbols:   11550
+  CStrings:  17193
 
Symbols:
+ _MPCPlaybackEngineEventPayloadKeyRemoteControlCommandQueueData
+ _MPCPlaybackEngineEventPayloadKeyRemoteControlCommandQueueImmediatePlayback
+ _MRSystemAppPlaybackQueueCopyFeatureName
+ _MRSystemAppPlaybackQueueCopyTypeDescription
+ _MRSystemAppPlaybackQueueGetSiriAssetInfo
+ _MRSystemAppPlaybackQueueGetType
+ _MRSystemAppPlaybackQueueIsRequestingImmediatePlayback
+ _OBJC_CLASS_$__MPCMediaRemoteDetective
+ _OBJC_METACLASS_$__MPCMediaRemoteDetective
+ _swift_unknownObjectUnownedLoadStrong
CStrings:
+ "\x01\x11\x11\x11\x12&"
+ "@\"MPAVItem\"28@0:8@\"NSString\"16B24"
+ "@\"_MPCMediaRemoteDetective\""
+ "@16@?0@\"<MPCPlaybackEngineEventStreamCursor>\"8"
+ "Failed to find command begin for "
+ "Failed to find reason for command timeout: "
+ "MediaServices were lost (and has not recovered) during command"
+ "MediaServices were reset during command"
+ "Missing Asset Load for "
+ "Missing TimeControlStatus event"
+ "Missing asset assertion for "
+ "Placeholder item for "
+ "SEED"
+ "Session Activation did not complete"
+ "T@\"_MPCMediaRemoteDetective\",R,N,V_detective"
+ "TimeoutAssetInsertionMissing"
+ "TimeoutAssetLoadMissing"
+ "TimeoutInterruptor"
+ "TimeoutMediaServicesLost"
+ "TimeoutMediaServicesReset"
+ "TimeoutMediaStart"
+ "TimeoutMissingItem"
+ "TimeoutPlaceholderItem"
+ "TimeoutQueueLoadMissing"
+ "TimeoutSetRate"
+ "TimeoutTimeControlStatusMissing"
+ "TimeoutTimeControlStatusWaiting"
+ "TimeoutUnknownCommandInvalid"
+ "Unknown reason for missing item event"
+ "Unknown reason for remaining on placeholder item"
+ "Waiting on Asset Load for "
+ "Waiting on FirstAudioFrame for "
+ "Waiting on Media Start for "
+ "Waiting on QueueLoad for "
+ "Waiting on ReadyToPlay for "
+ "Waiting on TimeControlStatus: "
+ "Waiting on placeholder item for section: "
+ "Waiting on unknown current item to start playback"
+ "_MPCMediaRemoteDetective"
+ "_MediaPlaybackCore_Bridge._MPCMediaRemoteDetective"
+ "_detective"
+ "detective"
+ "investigateTimeoutForEvent:completion:"
+ "remote-control-queue-data"
+ "remote-control-queue-start"
+ "v32@0:8@\"MPRemoteCommandEvent\"16@?<v@?@\"MPRemoteCommandStatus\">24"
+ "|%{public}@ %{public}@ %2i %{public}@  │ hasSiriAssetInfo: %{BOOL}u; featureName: %{public}@"
+ "|%{public}@ %{public}@ %2i %{public}@  │ queueType: %{public}@; immediatePlayback: %{BOOL}u"
+ "— \U00100122 Detected Unspecialized Command"
+ "— \U00100284 Play Command"
+ "— \U00100284 SetQueue > Play"
+ "— \U001002ab Searching for AssetLoad event for %s"
+ "— \U001002ab Searching for FirstAudioFrame event for %s"
+ "— \U001002ab Searching for Interruption"
+ "— \U001002ab Searching for MediaServices events"
+ "— \U001002ab Searching for PlayerOperation Asset insertion event for %s"
+ "— \U001002ab Searching for PlayerOperation SetRate event for %s"
+ "— \U001002ab Searching for QueueLoad event for %{public}s"
+ "— \U001002ab Searching for QueueLoad event for last section"
+ "— \U001002ab Searching for ReadyToPlay event for %s"
+ "— \U001002ab Searching for Session Activation"
+ "— \U001002ab Searching for TimeControlStatus event for %s"
+ "— \U001002ab Searching for commandBegin %{public}s"
+ "— \U001002ab Searching for itemBegin event"
+ "— \U001008bd SetQueue Command"
+ "— \U00100a86 SetQueue > Wait"
+ "—— \U00100060 Failed to find commandBegin for %@"
+ "—— \U00100062 Found event: %{public}@"
+ "—— \U001003b9 No Interruption"
+ "—— \U001003b9 No MediaServices events"
+ "—— \U001003b9 No Session Activation"
+ "—— \U001003b9 No item found"
+ "—— \U001003b9 No item found: no item begin after last end"
+ "—— \U001003b9 No item found: on placeholder, but no section ID"
+ "—— \U001003be Found last item: %{public}s %{public}s"
+ "—— \U0010042b Waiting on AssetLoad"
+ "—— \U0010042b Waiting on FirstAudioFrame"
+ "—— \U0010042b Waiting on PlayerOperation Asset insertion"
+ "—— \U0010042b Waiting on PlayerOperation SetRate"
+ "—— \U0010042b Waiting on QueueLoad"
+ "—— \U0010042b Waiting on ReadyToPlay"
+ "—— \U0010042b Waiting on Session Activation"
+ "—— \U0010042b Waiting on TimeControlStatus"
+ "—— \U0010042b Waiting on interruption from %{public}s"
+ "—— \U00100b49 Placeholder found: currently on placeholder %{public}s"
+ "—— \U00100e74 Successful AssetLoad"
+ "—— \U00100e74 Successful FirstAudioFrame"
+ "—— \U00100e74 Successful PlayerOperation Asset insertion"
+ "—— \U00100e74 Successful PlayerOperation SetRate"
+ "—— \U00100e74 Successful QueueLoad"
+ "—— \U00100e74 Successful ReadyToPlay"
+ "—— \U00100e74 Successful Session Activation"
+ "—— \U00100e74 Successful TimeControlStatus"
+ "—— \U00100e76 Finished interruption from %{public}s"
+ "—— \U00100e76 MediaServices Reset event"
+ "—— \U00101712 MediaServices Lost event"
+ "——\u00a0\U001003b9 No AssetLoad found"
+ "——\u00a0\U001003b9 No QueueLoad found"
+ "——\u00a0\U001003b9 No QueueLoad found for %{public}s"
+ "——\u00a0\U001003b9 No TimeControlStatus found"
+ "🕵🏻\u200d♂️ Opening investigation for: %{public}@"
+ "🧑\u200d⚖️ Verdict for: %{public}@ => %{public}@"
- "\x01\x11\x11\x11\x12%"
- "@\"MPAVItem\"24@0:8@\"NSString\"16"
- "Failed to find CommandBegin event for commandID: %@"
- "Found SessionActivationBegin but not SessionActivationEnd event"
- "Publisher has no additional info for timeout"
- "_itemForContentItemID:"

```
