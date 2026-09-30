## SiriPlaybackControlIntents

> `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents`

```diff

-3404.28.1.11.2
-  __TEXT.__text: 0x2501b0
-  __TEXT.__auth_stubs: 0x48a0
+3405.12.1.0.0
+  __TEXT.__text: 0x252770
+  __TEXT.__auth_stubs: 0x47d0
   __TEXT.__objc_methlist: 0x2748
-  __TEXT.__const: 0x192f0
-  __TEXT.__cstring: 0x8018
-  __TEXT.__constg_swiftt: 0x6c5c
-  __TEXT.__swift5_typeref: 0x5e1a
+  __TEXT.__const: 0x192c0
+  __TEXT.__cstring: 0x8068
+  __TEXT.__constg_swiftt: 0x6c64
+  __TEXT.__swift5_typeref: 0x5dd4
   __TEXT.__swift5_builtin: 0x514
-  __TEXT.__swift5_reflstr: 0x4f23
-  __TEXT.__swift5_fieldmd: 0x5be4
-  __TEXT.__swift5_assocty: 0x1c00
-  __TEXT.__swift5_proto: 0x15c8
+  __TEXT.__swift5_reflstr: 0x4f93
+  __TEXT.__swift5_fieldmd: 0x5c38
+  __TEXT.__swift5_assocty: 0x1c18
+  __TEXT.__swift5_proto: 0x15b8
   __TEXT.__swift5_types: 0x6d0
   __TEXT.__swift5_protos: 0xc4
-  __TEXT.__swift5_capture: 0x4400
-  __TEXT.__oslogstring: 0x1bf86
-  __TEXT.__swift_as_entry: 0xe4
-  __TEXT.__swift_as_ret: 0xf0
+  __TEXT.__swift5_capture: 0x4408
+  __TEXT.__oslogstring: 0x1d016
+  __TEXT.__swift_as_entry: 0xf0
+  __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x72c0
-  __TEXT.__eh_frame: 0x4eb0
+  __TEXT.__unwind_info: 0x72f8
+  __TEXT.__eh_frame: 0x5040
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methname: 0x2d45
   __TEXT.__objc_methtype: 0x1d0
-  __DATA_CONST.__got: 0xea0
-  __DATA_CONST.__const: 0xb88
+  __DATA_CONST.__got: 0xe98
+  __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_protorefs: 0x100
-  __AUTH_CONST.__auth_got: 0x2450
-  __AUTH_CONST.__auth_ptr: 0x1bf0
-  __AUTH_CONST.__const: 0x12d10
-  __AUTH_CONST.__objc_const: 0x121c0
-  __AUTH.__objc_data: 0x5810
-  __AUTH.__data: 0x73d8
+  __AUTH_CONST.__auth_got: 0x23e8
+  __AUTH_CONST.__auth_ptr: 0x23e8
+  __AUTH_CONST.__const: 0x12dc0
+  __AUTH_CONST.__objc_const: 0x12150
+  __AUTH.__objc_data: 0x5818
+  __AUTH.__data: 0x73d0
   __DATA.__data: 0x4680
-  __DATA.__bss: 0x24680
-  __DATA.__common: 0x2a8
+  __DATA.__bss: 0x24400
+  __DATA.__common: 0x2a0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14104
-  Symbols:   4739
-  CStrings:  2892
+  Functions: 14155
+  Symbols:   4788
+  CStrings:  2910
 
CStrings:
+ "AppIntentInvoker#invokeCloseAccessoryItemAppIntentForLyrics"
+ "AppIntentInvoker#invokeCloseAccessoryItemAppIntentForLyrics response: %s"
+ "PlaybackControls#SetLyricsStateFailed"
+ "SetLyricsStateFlow#execute"
+ "SetLyricsStateFlow#execute caught exception with error %s"
+ "SetLyricsStateFlow#execute closing lyrics view"
+ "SetLyricsStateFlow#execute failed to create MediaPlayerIntent from parse"
+ "SetLyricsStateFlow#execute opening lyrics view"
+ "SetLyricsStateFlow#execute result: %s"
+ "SetLyricsStateFlow#execute returning complete"
+ "SetLyricsStateFlow#execute sent dismiss command"
+ "SetLyricsStateFlow#execute withCheckedContinuation"
+ "SetLyricsStateFlow#getLyricsState unsupported verb"
+ "SetLyricsStateFlow#onInput not a valid SetLyricsState parse"
+ "SetLyricsStateFlow#xecute failed to get lyrics state"
+ "SetVolumeLevelIntentHandler#boundVolumeLevel floatVolumeLevel: %f deceeds minimum level. This is okay, we'll still try to set it to the min value"
+ "SetVolumeLevelIntentHandler#boundVolumeLevel floatVolumeLevel: %f exceeds maximum level. This is okay, we'll still try to set it to the max value"
+ "SetVolumeLevelIntentHandler#confirm setVolumeLevel.SetVolumeLevelIntentHandler.confirm() called"
+ "SetVolumeLevelIntentHandler#handle called"
+ "SetVolumeLevelIntentHandler#handle no devices resolved, returning failure"
+ "SetVolumeLevelIntentHandler#handle resolvedVolumeOutput or currentVolume is undefined or could not be cast to float. Returning failure"
+ "SetVolumeLevelIntentHandler#handle setting volume for single local device"
+ "SetVolumeLevelIntentHandler#handle unable to get route ids for the intent devices: %s"
+ "SetVolumeLevelIntentHandler#handle unknown volume setting type: %s, returning failure."
+ "SetVolumeLevelIntentHandler#handle volume is already at 0%%. Skip setting volume."
+ "SetVolumeLevelIntentHandler#handle volume is already at 100%%. Skip setting volume."
+ "SetVolumeLevelIntentHandler#handle volume settingType: %s, increase: %{bool}d, decrease: %{bool}d, resolved output: %s"
+ "SetVolumeLevelIntentHandler#resolveDevices can't do volume controls on Apple TV, returning unsupported."
+ "SetVolumeLevelIntentHandler#resolveDevices can't do volume controls on CarPlay, returning unsupported."
+ "SetVolumeLevelIntentHandler#resolveDevices multiple devices selected."
+ "SetVolumeLevelIntentHandler#resolveDevices no context or device query, falling back to local device"
+ "SetVolumeLevelIntentHandler#resolveDevices resolving devices for SetVolume"
+ "SetVolumeLevelIntentHandler#resolveDevices whole House Audio requests are unsupported on this platform"
+ "SetVolumeLevelIntentHandler#resolveRelativeNumericChange calculated delta value: %f"
+ "SetVolumeLevelIntentHandler#resolveRelativeNumericChange calculating delta based on percent of current value"
+ "SetVolumeLevelIntentHandler#resolveRelativeNumericChange normalizing floatSettingValue percentage value"
+ "SetVolumeLevelIntentHandler#resolveRelativeNumericChange percent not specified so increase/decrease based on defaultRelativeChangeStepSize and value"
+ "SetVolumeLevelIntentHandler#resolveRelativeNumericChange recalculating delta based on percent of current value"
+ "SetVolumeLevelIntentHandler#resolveRelativeNumericChange using value directly as delta because value is less than normalizedMinimumValueToUseAsMultiplier or current volume is 0"
+ "SetVolumeLevelIntentHandler#resolveVolumeForUnmute nothing to unmute"
+ "SetVolumeLevelIntentHandler#resolveVolumeForUnmute volume Level retrieved from stash: %f"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevel an error occurred in the GetVolumeLevel media remote call: %{public}s"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevel failed to get volume for accessory"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevel no devices resolved. Returning failure"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevel resolving volume level for SetVolume"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelCompletionHandler error getting the volume resolution result"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelCompletionHandler resolvedVolumeOutput = %f"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelCompletionHandler user did not specify a numeric volume level in the intent, but intent has qualifiers. Trying to resolve volume level using qualifiers"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelCompletionHandler user did not specify neither a numeric value in the intent nor any qualifiers. Returning .needsValue"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelCompletionHandler user specified a numeric value in the intent. Trying to resolve the volume level from numeric input"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelForMute already Muted"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelForMute failed to get routeId to use when storing previous volume level"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelFromNumericInput intent does not contain a volumeSettingValue. Cannot resolve volume level from numeric input"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelFromNumericInput this is a relative volume adjust intent"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelFromNumericInput this is an absolute volume adjust intent"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelFromNumericInput user specified a numeric value in the intent: %@"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelUsingQualifiers found unexpected volumeSettingState: %{public}s. Returning failure"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelUsingQualifiers resolveVolumeLevelUsingQualifiers decrease by %f"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelUsingQualifiers resolveVolumeLevelUsingQualifiers increase by %f"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelUsingQualifiers resolveVolumeLevelUsingQualifiers volume set to max"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelUsingQualifiers resolveVolumeLevelUsingQualifiers volume set to mean"
+ "SetVolumeLevelIntentHandler#resolveVolumeLevelUsingQualifiers resolveVolumeLevelUsingQualifiers volume set to min"
+ "SetVolumeLevelIntentHandler#setAbsoluteVolume an error occurred in the SetVolumeLevel media remote call: %{public}s"
+ "SetVolumeLevelIntentHandler#setAbsoluteVolume attempting to set the volume to %f for routeIds: %s isLocal: %{bool}d"
+ "SetVolumeLevelIntentHandler#setRelativeVolume an error occurred in the SetVolumeLevel media remote call: %{public}s"
+ "SetVolumeLevelIntentHandler#setRelativeVolume attempting to change the volume by %f for routeIds: %s"
+ "SetVolumeLevelIntentHandler#setVolumeForLocalDevice an error occurred in the SetVolumeLevel media remote call: %{public}s"
+ "SetVolumeLevelIntentHandler#setVolumeForLocalDevice attempting to set the volume for local device to %f for routeId: %s"
+ "SetVolumeLevelIntentHandler#setVolumeForSidekickDevice attempting to set the volume for sidekick device to %f for routeId: %s"
+ "SetVolumeLevelIntentHandler#setVolumeForSidekickDevice failed to set volume for accessory"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning checking if we should be presenting loud volume warning for expectedOutputVolume = %f, currentVolumeOutput = %s, device = %@, volumeSettingState: %ld"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning could not find a resolveVolumeOutput in the intent. shouldPresentLoudVolumeWarning = false"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning delta = %f is smaller than the required volume delta before loud warning %f. shouldPresentLoudVolumeWarning = false"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning expected volume output = %f is smaller than the loud volume range start value of %f. shouldPresentLoudVolumeWarning = false"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning incrementing loud volume confirmation count for this device"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning loud volume confirmation already presented twice on this device, skipping confirmation"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning request is to decrease volume, skip loud volume confirmation"
+ "SetVolumeLevelIntentHandler#shouldPresentLoudVolumeWarning volume level is too loud, device has very loud audio output (hence should present warning): %{bool}d"
+ "SiriPlaybackControlsOutputProvider.confirmationViewOutput creating confirmationViewOutput without snippet using RF 2.0"
+ "_TtC26SiriPlaybackControlIntents18SetLyricsStateFlow"
+ "hide"
+ "isShowLyricsRequest"
+ "setPlaybackSpeedFaster"
+ "setPlaybackSpeedSlower"
+ "sirikit.intents.custom.com.apple.siri.SiriPlaybackControlIntents.HideLyricsIntent"
+ "sirikit.intents.custom.com.apple.siri.SiriPlaybackControlIntents.SetLyricsStateIntent"
- "ASIH#AddNoTopologyChanges"
- "ASIH#MoveNoTopologyChanges"
- "Already Muted"
- "An error occurred in the SetVolumeLevel media remote call: %{public}s"
- "Attempting to change the volume by %f for routeIds: %s"
- "Attempting to set the volume for local device to %f for routeId: %s"
- "Attempting to set the volume for sidekick device to %f for routeId: %s"
- "Attempting to set the volume to %f for routeIds: %s isLocal: %{bool}d"
- "Calculated delta value: %f"
- "Calculating delta based on percent of current value"
- "Checking if we should be presenting loud volume warning for expectedOutputVolume = %f, currentVolumeOutput = %s, device = %@, volumeSettingState: %ld"
- "Could not find a resolveVolumeOutput in the intent. shouldPresentLoudVolumeWarning = false"
- "Delta = %f is smaller than the required volume delta before loud warning %f. shouldPresentLoudVolumeWarning = false"
- "Error getting the volume resolution result"
- "Expected volume output = %f is smaller than the loud volume range start value of %f. shouldPresentLoudVolumeWarning = false"
- "Failed to get routeId to use when storing previous volume level"
- "Failed to set volume for accessory"
- "Found unexpected volumeSettingState: %{public}s. Returning failure"
- "Incrementing loud volume confirmation count for this device"
- "Intent does not contain a volumeSettingValue. Cannot resolve volume level from numeric input"
- "Loud volume confirmation already presented twice on this device, skipping confirmation"
- "MSIH#MoveNoTopologyChanges"
- "Multiple devices selected."
- "No devices resolved. Returning failure"
- "Normalizing floatSettingValue percentage value"
- "Nothing to unmute"
- "Percent not specified so increase/decrease based on defaultRelativeChangeStepSize and value"
- "PlaybackControls#NoTopologyChanges"
- "PlaybackControls#ShowLyricsFailed"
- "Recalculating delta based on percent of current value"
- "Request is to decrease volume, skip loud volume confirmation"
- "Resolving devices for SetVolume"
- "Resolving volume level for SetVolume"
- "SetVolumeLevel.SetVolumeLevelIntentHandler.confirm() called"
- "SetVolumeLevel.SetVolumeLevelIntentHandler.handle() called"
- "ShowLyricsFlow#execute"
- "ShowLyricsFlow#execute caught exception with error %s"
- "ShowLyricsFlow#execute indicating complete"
- "ShowLyricsFlow#execute result: %s"
- "ShowLyricsFlow#execute sent dismiss command"
- "ShowLyricsFlow#execute withCheckedContinuation"
- "SiriPlaybackControlsOutputProvider.confirmationViewOutput creating confirmationViewOutput without snippet for HomePod using RF 2.0"
- "This is a relative volume adjust intent"
- "This is an absolute volume adjust intent"
- "Unknown volume setting type: %s, returning failure."
- "User did not specify a numeric volume level in the intent, but intent has qualifiers. Trying to resolve volume level using qualifiers"
- "User did not specify neither a numeric value in the intent nor any qualifiers. Returning .needsValue"
- "User specified a numeric value in the intent. Trying to resolve the volume level from numeric input"
- "User specified a numeric value in the intent: %@"
- "Using value directly as delta because value is less than normalizedMinimumValueToUseAsMultiplier or current volume is 0"
- "UsoTask_request_common_MediaItem#shouldHandle not a lyrics request. Not handling in controls"
- "Volume Level retrieved from stash: %f"
- "Volume is already at 0%%. Skip setting volume."
- "Volume is already at 100%%. Skip setting volume."
- "Volume level is too loud, device has very loud audio output (hence should present warning): %{bool}d"
- "Volume settingType: %s, increase: %{bool}d, decrease: %{bool}d, resolved output: %s"
- "_TtC26SiriPlaybackControlIntents14ShowLyricsFlow"
- "_TtC26SiriPlaybackControlIntents19AccessoryItemEntity"
- "floatVolumeLevel: %f deceeds minimum level. This is okay, we'll still try to set it to the min value"
- "floatVolumeLevel: %f exceeds maximum level. This is okay, we'll still try to set it to the max value"
- "resolveVolumeLevel: An error occurred in the GetVolumeLevel media remote call: %{public}s"
- "resolveVolumeLevelUsingQualifiers decrease by %f"
- "resolveVolumeLevelUsingQualifiers increase by %f"
- "resolveVolumeLevelUsingQualifiers volume set to max"
- "resolveVolumeLevelUsingQualifiers volume set to mean"
- "resolveVolumeLevelUsingQualifiers volume set to min"
- "resolvedVolumeOutput = %f"
- "resolvedVolumeOutput or currentVolume is undefined or could not be cast to float. Returning failure"

```
