## VoiceMemosSettingsWidgetExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosSettingsWidgetExtension.appex/VoiceMemosSettingsWidgetExtension`

```diff

-1380.0.0.0.0
-  __TEXT.__text: 0x178f4
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x160
-  __TEXT.__const: 0x39f4
-  __TEXT.__cstring: 0xfe4
+1428.0.0.0.0
+  __TEXT.__text: 0x1d168
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x1c8
+  __TEXT.__const: 0x4834
+  __TEXT.__cstring: 0x15c4
+  __TEXT.__oslogstring: 0x1a5
   __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methname: 0x3ba
-  __TEXT.__objc_methtype: 0x53
-  __TEXT.__oslogstring: 0xe5
-  __TEXT.__swift5_typeref: 0x110e
-  __TEXT.__swift5_reflstr: 0x41d
-  __TEXT.__swift5_assocty: 0x6c0
-  __TEXT.__constg_swiftt: 0x5a8
-  __TEXT.__swift5_fieldmd: 0x348
-  __TEXT.__swift5_proto: 0x2ec
-  __TEXT.__swift5_types: 0x84
-  __TEXT.__swift_as_entry: 0x108
-  __TEXT.__swift_as_ret: 0xd0
+  __TEXT.__objc_methtype: 0x5f
+  __TEXT.__objc_methname: 0x3b0
+  __TEXT.__constg_swiftt: 0x6e0
+  __TEXT.__swift5_typeref: 0x148e
+  __TEXT.__swift5_fieldmd: 0x40c
+  __TEXT.__swift5_reflstr: 0x50d
+  __TEXT.__swift5_assocty: 0x888
+  __TEXT.__swift5_proto: 0x3a4
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__swift_as_entry: 0x14c
+  __TEXT.__swift_as_ret: 0x100
+  __TEXT.__swift_as_cont: 0xac
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xb20
-  __TEXT.__eh_frame: 0xa38
-  __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0x718
-  __DATA_CONST.__const: 0x9f0
-  __DATA_CONST.__cfstring: 0x1a0
+  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__eh_frame: 0xc20
+  __DATA_CONST.__const: 0xcd0
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__auth_ptr: 0x758
   __DATA.__objc_const: 0x1e8
-  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_selrefs: 0x150
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xb38
-  __DATA.__bss: 0x5e40
-  __DATA.__common: 0x3b0
+  __DATA.__data: 0xdb8
+  __DATA.__bss: 0x7590
+  __DATA.__common: 0x4a8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22452A66-A09B-3A4D-8A7A-7BF058FB2B66
-  Functions: 909
-  Symbols:   112
-  CStrings:  173
+  UUID: 29858C52-8775-3DA9-B89C-1DB651A23C12
+  Functions: 1131
+  Symbols:   133
+  CStrings:  211
 
Symbols:
+ _RCDeviceSupportsSpatialAudioCapture
+ _RCDeviceSupportsStereoAudioRecording
+ _RCSpatialAudioCaptureIsAvailable
+ _RCStereoAudioRecordingIsAvailable
+ __os_feature_enabled_impl
+ __os_log_error_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x9
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release_x23
- _objc_retain_x19
- _rc_defaultAudioQuality
- _rc_defaultChannelConfiguration
CStrings:
+ "%s - Unexpected RCAudioQuality value"
+ "%s - Unexpected RCChannelConfiguration value"
+ "%s - Unexpected RCRecentlyDeletedWindow value"
+ "%s - Unexpected max channel configuration"
+ "%s -- failed to access shared settings user defaults"
+ "+[NSUserDefaults(VoiceMemosSettings) _sharedSettingsUserDefaultsForCaller:]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_audioQuality]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_channelConfiguration]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_deletionIsImmediate]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_deletionIsNever]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_recentlyDeletedWindow]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_setAudioQuality:]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_setChannelConfiguration:]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_setRecentlyDeletedWindow:]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_setUseLocationBasedNaming:]"
+ "+[NSUserDefaults(VoiceMemosSettings) rc_useLocationBasedNaming]"
+ "/RCVoiceMemosChannelConfigurationKey"
+ "@24@0:8r*16"
+ "DeviceSupportsStereoAudioRecording"
+ "Invalid settings: stereoError = %i, spatialError = %i"
+ "OPEN_INTENT_RECORDINGMODE_PARAMETER_TITLE"
+ "RECORDING_MODE_DESCRIPTION_TEXT"
+ "RECORDING_MODE_DISPLAY"
+ "RECORDING_MODE_INTENT_DESCRIPTION"
+ "RECORDING_MODE_MONO"
+ "RECORDING_MODE_OPEN_TITLE"
+ "RECORDING_MODE_SPATIAL"
+ "RECORDING_MODE_STEREO"
+ "RECORDING_MODE_SUBTITLE"
+ "RECORDING_MODE_TITLE"
+ "SETTINGS_RECORDING_MODE"
+ "SpatialAudioCapture"
+ "UPDATE_INTENT_RECORDINGMODEENTITY_VALUE_ENTITY_PARAMETER_TITLE"
+ "UPDATE_INTENT_RECORDINGMODEENTITY_VALUE_INTENT_TITLE"
+ "UPDATE_INTENT_RECORDINGMODEENTITY_VALUE_PROPERTY_PARAMETER_TITLE"
+ "UpdateRecordingModeEntityValueIntent"
+ "VoiceMemos"
+ "_sharedSettingsUserDefaultsForCaller:"
+ "com.apple.recordingMode"
+ "init(rcChannelConfiguration:)"
- "%s - Unexpected rcAudioQuality value"
- "%s - Unexpected rcDeletedWindow value"
- "rc_setUseStereoRecording:"
- "rc_useStereoRecording"

```
