## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-655.2.1.0.0
-  __TEXT.__text: 0xb1870
+655.2.3.0.0
+  __TEXT.__text: 0xb17a0
   __TEXT.__auth_stubs: 0x2610
-  __TEXT.__objc_methlist: 0xab20
+  __TEXT.__objc_methlist: 0xab40
   __TEXT.__const: 0x279a
-  __TEXT.__cstring: 0x8614
-  __TEXT.__gcc_except_tab: 0x8e0
-  __TEXT.__oslogstring: 0x3f9b
+  __TEXT.__cstring: 0x8684
+  __TEXT.__gcc_except_tab: 0x8a8
+  __TEXT.__oslogstring: 0x3fdb
   __TEXT.__dlopen_cstrs: 0x14e
-  __TEXT.__constg_swiftt: 0x27c8
+  __TEXT.__constg_swiftt: 0x2828
   __TEXT.__swift5_typeref: 0x2a60
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x1b62
-  __TEXT.__swift5_fieldmd: 0x1258
+  __TEXT.__swift5_reflstr: 0x1bc2
+  __TEXT.__swift5_fieldmd: 0x127c
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x120

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x2ac0
+  __TEXT.__unwind_info: 0x2ab0
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_classname: 0x1605
-  __TEXT.__objc_methname: 0x1db45
-  __TEXT.__objc_methtype: 0x83a0
-  __TEXT.__objc_stubs: 0xc880
+  __TEXT.__objc_methname: 0x1dcc8
+  __TEXT.__objc_methtype: 0x83a9
+  __TEXT.__objc_stubs: 0xc7e0
   __DATA_CONST.__got: 0xcd0
-  __DATA_CONST.__const: 0x1278
+  __DATA_CONST.__const: 0x1268
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6458
+  __DATA_CONST.__objc_selrefs: 0x6460
   __DATA_CONST.__objc_protorefs: 0x1f8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x1318
   __AUTH_CONST.__const: 0x3f08
   __AUTH_CONST.__cfstring: 0x2ec0
-  __AUTH_CONST.__objc_const: 0x10450
+  __AUTH_CONST.__objc_const: 0x10500
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x17b8
   __AUTH.__data: 0x7b8
-  __DATA.__objc_ivar: 0x728
-  __DATA.__data: 0x3930
+  __DATA.__objc_ivar: 0x730
+  __DATA.__data: 0x3950
   __DATA.__bss: 0x11f0
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x34d0
-  __DATA_DIRTY.__data: 0xa08
+  __DATA_DIRTY.__objc_data: 0x3548
+  __DATA_DIRTY.__data: 0x9f8
   __DATA_DIRTY.__bss: 0x9e8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6775E634-6913-35AE-9DA4-180098C3DEFA
-  Functions: 4774
-  Symbols:   10003
-  CStrings:  6774
+  UUID: 7447D496-A5EC-38CE-8B7C-07C9D8DD5E0E
+  Functions: 4768
+  Symbols:   10005
+  CStrings:  6783
 
Symbols:
+ -[CCUIHeaderPocketView audioBundleIdentifierUsingAudioVideoControls]
+ -[CCUIHeaderPocketView audioDisplayNameUsingAudioVideoControls]
+ -[CCUIHeaderPocketView setAudioBundleIdentifierUsingAudioVideoControls:]
+ -[CCUIHeaderPocketView setAudioControlsEnabled:videoControlsEnabled:audioBundleIdentifier:videoBundleIdentifier:audioDisplayName:videoDisplayName:]
+ -[CCUIHeaderPocketView setAudioDisplayNameUsingAudioVideoControls:]
+ -[CCUIHeaderPocketView setVideoBundleIdentifierUsingAudioVideoControls:]
+ -[CCUIHeaderPocketView setVideoDisplayNameUsingAudioVideoControls:]
+ -[CCUIHeaderPocketView videoBundleIdentifierUsingAudioVideoControls]
+ -[CCUIHeaderPocketView videoDisplayNameUsingAudioVideoControls]
+ GCC_except_table46
+ GCC_except_table55
+ _AXShowBordersEnabledStatusDidChangeNotification
+ _OBJC_IVAR_$_CCUIHeaderPocketView._audioBundleIdentifierUsingAudioVideoControls
+ _OBJC_IVAR_$_CCUIHeaderPocketView._audioDisplayNameUsingAudioVideoControls
+ _OBJC_IVAR_$_CCUIHeaderPocketView._videoBundleIdentifierUsingAudioVideoControls
+ _OBJC_IVAR_$_CCUIHeaderPocketView._videoDisplayNameUsingAudioVideoControls
+ ___block_literal_global.137
+ _block_copy_helper.79
+ _block_copy_helper.86
+ _block_copy_helper.93
+ _block_descriptor.81
+ _block_descriptor.88
+ _block_descriptor.95
+ _block_destroy_helper.80
+ _block_destroy_helper.87
+ _block_destroy_helper.94
+ _objc_msgSend$setAudioControlsEnabled:videoControlsEnabled:audioBundleIdentifier:videoBundleIdentifier:audioDisplayName:videoDisplayName:
- -[CCUIHeaderPocketView audioVideoModeSelectionAttribution]
- -[CCUIHeaderPocketView setAudioControlsEnabled:videoControlsEnabled:forBundleIdentifier:]
- -[CCUIHeaderPocketView setAudioVideoModeSelectionAttribution:]
- -[CCUIHeaderPocketView setBundleIdentifierUsingAudioVideoControls:]
- GCC_except_table56
- _OBJC_IVAR_$_CCUIHeaderPocketView._audioVideoModeSelectionAttribution
- _OBJC_IVAR_$_CCUIHeaderPocketView._bundleIdentifierUsingAudioVideoControls
- _UIAccessibilityButtonShapesEnabled
- _UIAccessibilityButtonShapesEnabledStatusDidChangeNotification
- ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_2.133
- ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_3
- ___block_literal_global.139
- _block_copy_helper.68
- _block_descriptor.70
- _block_destroy_helper.69
- _objc_msgSend$attributionGroup
- _objc_msgSend$setAudioControlsEnabled:videoControlsEnabled:
- _objc_msgSend$setAudioControlsEnabled:videoControlsEnabled:forBundleIdentifier:
- _objc_msgSend$setAudioVideoHeaderTrailingText:
- _objc_msgSend$setAudioVideoModeSelectionAttribution:
- _objc_msgSend$setBundleIdentifierUsingAudioVideoControls:
CStrings:
+ "T@\"NSString\",&,N,V_audioBundleIdentifierUsingAudioVideoControls"
+ "T@\"NSString\",&,N,V_audioDisplayNameUsingAudioVideoControls"
+ "T@\"NSString\",&,N,V_videoBundleIdentifierUsingAudioVideoControls"
+ "T@\"NSString\",&,N,V_videoDisplayNameUsingAudioVideoControls"
+ "[AV Modules] Setting visibility of AV modules (audio: %{BOOL}d for %{public}@, video: %{BOOL}d for %{public}@)"
+ "[Cellular Data Module] (%{public}p) contextMenuShouldPresent... (contentModuleContext: %{public}@)"
+ "[Cellular Data Module] (%{public}p) didBeginContextMenuPresentation... (_contentMenuActions: %lu)"
+ "_audioBundleIdentifierUsingAudioVideoControls"
+ "_audioDisplayNameUsingAudioVideoControls"
+ "_videoBundleIdentifierUsingAudioVideoControls"
+ "_videoDisplayNameUsingAudioVideoControls"
+ "audioBundleIdentifier"
+ "audioBundleIdentifierUsingAudioVideoControls"
+ "audioDisplayName"
+ "audioDisplayNameUsingAudioVideoControls"
+ "setAudioBundleIdentifierUsingAudioVideoControls:"
+ "setAudioControlsEnabled:videoControlsEnabled:audioBundleIdentifier:videoBundleIdentifier:audioDisplayName:videoDisplayName:"
+ "setAudioDisplayNameUsingAudioVideoControls:"
+ "setVideoBundleIdentifierUsingAudioVideoControls:"
+ "setVideoDisplayNameUsingAudioVideoControls:"
+ "v56@0:8B16B20@24@32@40@48"
+ "videoBundleIdentifier"
+ "videoBundleIdentifierUsingAudioVideoControls"
+ "videoDisplayName"
+ "videoDisplayNameUsingAudioVideoControls"
+ "\x91\xa2!"
- "T@\"CCUISensorActivityData\",C,N,V_audioVideoModeSelectionAttribution"
- "T@\"NSString\",&,N,V_bundleIdentifierUsingAudioVideoControls"
- "[AV Modules] Adding sensor usage data for CAMERA [%{public}@]"
- "[AV Modules] Adding sensor usage data for MICROPHONE [%{public}@]"
- "[AV Modules] Setting visibility of AV modules (audio: %{BOOL}d, video: %{BOOL}d) for bundle identifier %{public}@"
- "_audioVideoModeSelectionAttribution"
- "_bundleIdentifierUsingAudioVideoControls"
- "attributionGroup"
- "audioVideoHeaderTrailingText"
- "audioVideoModeSelectionAttribution"
- "setAudioControlsEnabled:videoControlsEnabled:"
- "setAudioControlsEnabled:videoControlsEnabled:forBundleIdentifier:"
- "setAudioVideoHeaderTrailingText:"
- "setAudioVideoModeSelectionAttribution:"
- "setBundleIdentifierUsingAudioVideoControls:"
- "v32@0:8B16B20@24"
- "\x91\xa21"

```
