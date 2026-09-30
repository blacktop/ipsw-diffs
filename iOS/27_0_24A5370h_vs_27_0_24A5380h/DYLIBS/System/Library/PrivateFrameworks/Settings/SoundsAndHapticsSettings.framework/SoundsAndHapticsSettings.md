## SoundsAndHapticsSettings

> `/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`

```diff

-  __TEXT.__text: 0x23364
-  __TEXT.__objc_methlist: 0x1b4c
+  __TEXT.__text: 0x2392c
+  __TEXT.__objc_methlist: 0x1c24
   __TEXT.__const: 0xc84
-  __TEXT.__gcc_except_tab: 0x9e8
-  __TEXT.__oslogstring: 0x118e
-  __TEXT.__cstring: 0x3243
+  __TEXT.__gcc_except_tab: 0xa50
+  __TEXT.__oslogstring: 0x11c1
+  __TEXT.__cstring: 0x3423
   __TEXT.__swift5_typeref: 0x1070
   __TEXT.__swift5_reflstr: 0x163
   __TEXT.__swift5_assocty: 0xf8

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_capture: 0x84
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x928
+  __TEXT.__unwind_info: 0x940
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1870
+  __DATA_CONST.__objc_selrefs: 0x18f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__got: 0x768
-  __AUTH_CONST.__const: 0x4f0
+  __DATA_CONST.__got: 0x780
+  __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__cfstring: 0x1b40
-  __AUTH_CONST.__objc_const: 0x28b0
+  __AUTH_CONST.__objc_const: 0x2a00
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH_CONST.__auth_got: 0xa08
+  __AUTH_CONST.__auth_got: 0xa10
   __AUTH.__objc_data: 0x630
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x168
+  __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x7f0
-  __DATA.__bss: 0x680
   __DATA.__common: 0x10
+  __DATA.__bss: 0x5f0
   __DATA_DIRTY.__objc_data: 0x538
   __DATA_DIRTY.__data: 0x1e0
-  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__bss: 0x350
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 803
-  Symbols:   2581
-  CStrings:  671
+  Functions: 823
+  Symbols:   2648
+  CStrings:  675
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[SHSAudioPlayback _handleMediaServicesWereResetNotification:]
+ -[SHSAudioPlayback _pendingRingtoneAlertType]
+ -[SHSAudioPlayback _pendingRingtoneIdentifier]
+ -[SHSAudioPlayback _pendingRingtoneLoop]
+ -[SHSAudioPlayback _pendingSystemSoundIdentifier]
+ -[SHSAudioPlayback _pendingSystemSoundLoop]
+ -[SHSAudioPlayback _pendingSystemSoundVolume]
+ -[SHSAudioPlayback _retryingAfterReset]
+ -[SHSAudioPlayback _setup]
+ -[SHSAudioPlayback _tearDown]
+ -[SHSAudioPlayback deactivateAudioSession]
+ -[SHSAudioPlayback set_pendingRingtoneAlertType:]
+ -[SHSAudioPlayback set_pendingRingtoneIdentifier:]
+ -[SHSAudioPlayback set_pendingRingtoneLoop:]
+ -[SHSAudioPlayback set_pendingSystemSoundIdentifier:]
+ -[SHSAudioPlayback set_pendingSystemSoundLoop:]
+ -[SHSAudioPlayback set_pendingSystemSoundVolume:]
+ -[SHSAudioPlayback set_retryingAfterReset:]
+ GCC_except_table16
+ _AVAudioSessionMediaServicesWereResetNotification
+ _OBJC_IVAR_$_SHSAudioPlayback.__pendingRingtoneAlertType
+ _OBJC_IVAR_$_SHSAudioPlayback.__pendingRingtoneIdentifier
+ _OBJC_IVAR_$_SHSAudioPlayback.__pendingRingtoneLoop
+ _OBJC_IVAR_$_SHSAudioPlayback.__pendingSystemSoundIdentifier
+ _OBJC_IVAR_$_SHSAudioPlayback.__pendingSystemSoundLoop
+ _OBJC_IVAR_$_SHSAudioPlayback.__pendingSystemSoundVolume
+ _OBJC_IVAR_$_SHSAudioPlayback.__retryingAfterReset
+ ___42-[SHSAudioPlayback deactivateAudioSession]_block_invoke
+ ___62-[SHSAudioPlayback _handleMediaServicesWereResetNotification:]_block_invoke
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ _objc_msgSend$_pendingRingtoneAlertType
+ _objc_msgSend$_pendingRingtoneIdentifier
+ _objc_msgSend$_pendingRingtoneLoop
+ _objc_msgSend$_pendingSystemSoundIdentifier
+ _objc_msgSend$_pendingSystemSoundLoop
+ _objc_msgSend$_pendingSystemSoundVolume
+ _objc_msgSend$_retryingAfterReset
+ _objc_msgSend$deactivateAudioSession
+ _objc_msgSend$deactivateWithOptions:completionHandler:
+ _objc_msgSend$set_pendingRingtoneAlertType:
+ _objc_msgSend$set_pendingRingtoneIdentifier:
+ _objc_msgSend$set_pendingRingtoneLoop:
+ _objc_msgSend$set_pendingSystemSoundIdentifier:
+ _objc_msgSend$set_pendingSystemSoundLoop:
+ _objc_msgSend$set_pendingSystemSoundVolume:
+ _objc_msgSend$set_retryingAfterReset:
+ _objc_setProperty_nonatomic_copy
- _objc_msgSend$setActive:withOptions:error:
CStrings:
+ "%s: Retrying ringtone preview '%{public}@' alertType '%{public}@'."
+ "%s: Retrying system sound preview '%{public}@'."
+ "-[SHSAudioPlayback _handleMediaServicesWereResetNotification:]_block_invoke"
+ "-[SHSAudioPlayback deactivateAudioSession]_block_invoke"
+ "Section footer on the Haptics options page; describes when haptics will play (or not play) for alarms, timers, alerts, and ringtones based on the selected option (Always Play, Play in Silent Mode, Don't Play in Silent Mode, Never Play)."
+ "Section header on the Haptics options page; introduces the four playback options that govern when haptics play for alarms, timers, alerts, and ringtones."
+ "v20@?0B8@\"NSError\"12"
- "%s: Failed to deactivate audio session with error '%{public}@'."
- "Section footer text explaining the effect of the selected options"
- "Section header"

```
