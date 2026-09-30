## LiveSpeechUIService

> `/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService`

```diff

-3180.6.1.0.0
-  __TEXT.__text: 0xa6f04
-  __TEXT.__auth_stubs: 0x3190
+3183.1.0.0.0
+  __TEXT.__text: 0xad268
+  __TEXT.__auth_stubs: 0x3320
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x8b0
-  __TEXT.__const: 0x5500
+  __TEXT.__objc_methlist: 0x8c8
+  __TEXT.__const: 0x5830
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x2a4f
-  __TEXT.__oslogstring: 0x1b19
+  __TEXT.__cstring: 0x2cfc
+  __TEXT.__oslogstring: 0x1e6a
   __TEXT.__objc_classname: 0xcb
-  __TEXT.__objc_methname: 0x1f89
+  __TEXT.__objc_methname: 0x1f9d
   __TEXT.__objc_methtype: 0x99b
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x12c7c
-  __TEXT.__constg_swiftt: 0x2098
+  __TEXT.__swift5_typeref: 0x13638
+  __TEXT.__constg_swiftt: 0x221c
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x1abf
-  __TEXT.__swift5_fieldmd: 0x1848
-  __TEXT.__swift5_assocty: 0x698
-  __TEXT.__swift5_proto: 0x214
-  __TEXT.__swift5_types: 0x16c
-  __TEXT.__swift5_capture: 0xcbc
+  __TEXT.__swift5_reflstr: 0x1c4f
+  __TEXT.__swift5_fieldmd: 0x1924
+  __TEXT.__swift5_assocty: 0x6e0
+  __TEXT.__swift5_proto: 0x220
+  __TEXT.__swift5_types: 0x17c
+  __TEXT.__swift5_capture: 0xd38
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2178
-  __TEXT.__eh_frame: 0x1d18
-  __DATA_CONST.__auth_got: 0x18d8
-  __DATA_CONST.__got: 0xd10
-  __DATA_CONST.__auth_ptr: 0xb90
-  __DATA_CONST.__const: 0x3f40
+  __TEXT.__unwind_info: 0x2288
+  __TEXT.__eh_frame: 0x1dc8
+  __DATA_CONST.__auth_got: 0x19a0
+  __DATA_CONST.__got: 0xd68
+  __DATA_CONST.__auth_ptr: 0xc10
+  __DATA_CONST.__const: 0x4200
   __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0x1e40
+  __DATA.__objc_const: 0x1f10
   __DATA.__objc_selrefs: 0x9a0
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x16a8
-  __DATA.__data: 0x3d50
+  __DATA.__objc_data: 0x17b8
+  __DATA.__data: 0x3e78
   __DATA.__objc_stublist: 0x18
-  __DATA.__bss: 0x47e8
-  __DATA.__common: 0x1d8
+  __DATA.__bss: 0x49a8
+  __DATA.__common: 0x1f0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 36B87570-94BE-371A-8008-B693FC8BCED6
-  Functions: 3086
-  Symbols:   377
-  CStrings:  870
+  UUID: A14BA7F8-B05B-3E69-87BA-29A7D721B047
+  Functions: 3173
+  Symbols:   373
+  CStrings:  898
 
Symbols:
+ _OBJC_CLASS_$__TtC19LiveSpeechUIService26LiveCaptionsSystemObserver
+ _OBJC_METACLASS_$__TtC19LiveSpeechUIService26LiveCaptionsSystemObserver
+ _swift_cvw_instantiateLayoutString
- _AXLogTemp
- _LiveSpeechLogCommon
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _swift_bridgeObjectRetain_n
CStrings:
+ "AXLCClearAllMenuOption"
+ "AXLCCollapseMenuOption"
+ "AXLCCopyAllMenuOption"
+ "AXLCMoreOptionsMenu"
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "CaptionsProvider Skip restarting transcription on Mic state: %{bool}d isTranscribing %{bool}d isActiveSourceTypeMic %{bool}d isActiveSourceTypeCall %{bool}d"
+ "CaptionsProvider: Added caption: %ld"
+ "CaptionsProvider: Received RTTCallUIVisible, processed: %{bool}d"
+ "CaptionsProvider: Updated the last caption %s"
+ "CaptionsProvider: canCopyCaptions updated %{bool}d"
+ "CaptionsProvider: clear captions %ld"
+ "CaptionsProvider: copy captions %{bool}d"
+ "CaptionsProvider: received caption, final: %{bool}d, text: %s"
+ "Coordinator asked to start LiveCaptions. isRunning=%{bool}d"
+ "Coordinator asked to stop LiveCaptions. isRunning=%{bool}d"
+ "Coordinator could not start LiveCaptions: %s"
+ "Coordinator could not stop LiveCaptions: %s"
+ "Coordinator did hide LiveCaptions UI on main screen (isRunning=%{bool}d)"
+ "Coordinator did show LiveCaptions UI on main screen"
+ "Did receive call status change: %s"
+ "Initial content height: %f, scroll to bottom: %f"
+ "LiveCaptions SettingsManager: forced save MicOn state: %{bool}d"
+ "LiveCaptionsCancel"
+ "LiveCaptionsClearHistoryConfirmation"
+ "LiveCaptionsConfirm"
+ "LiveCaptionsCopyHistory"
+ "LiveCaptionsMoreOptions"
+ "LiveCaptionsRootView: Received RTTCallUIVisible, switching to pip state"
+ "LiveCaptionsRootView: Received transitionToHomeOrAppSwitcher, switching to compact state"
+ "RTTCallUIVisibleNotificationName"
+ "_TtC19LiveSpeechUIService26LiveCaptionsSystemObserver"
+ "_canCopyCaptions"
+ "canCopyCaptionsChangedNotification"
+ "clearHistoryTimer"
+ "clearOldCaptionsIfNeeded"
+ "liveCaptionsTransitionToHomeOrAppSwitcherNotification"
+ "rttCallUIVisibleChanged"
+ "rttCallUIVisibleNotification"
+ "rttCallUIVisibleProcessed"
+ "transitionToHomeOrAppSwitcher"
+ "transitionToHomeOrAppSwitcherNotification"
- "AXLCClearHistoryButton"
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "CaptionsProvider Updated the last transcribed caption %s"
- "CaptionsProvider added transcribed caption: %ld"
- "CaptionsProvider last caption final: %{bool}d text: %s"
- "CaptionsProvider: clear captions"
- "CaptionsProvider: copy captions"
- "Did receive call status change: %@"
- "Optional<CGFloat>"
- "Optional<UserInterfaceSizeClass>"
- "cleanHistoryTimer"
- "cleanOldCaptionsIfNeeded"
- "updateLiveCaptionsStateForOneness"

```
