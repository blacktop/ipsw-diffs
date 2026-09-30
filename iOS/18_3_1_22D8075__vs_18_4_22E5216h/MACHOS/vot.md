## vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

-2393.3.10.0.0
-  __TEXT.__text: 0x120d14
-  __TEXT.__auth_stubs: 0x2520
-  __TEXT.__objc_stubs: 0x25780
-  __TEXT.__objc_methlist: 0xe6dc
-  __TEXT.__cstring: 0xe03f
-  __TEXT.__objc_classname: 0xfe8
-  __TEXT.__objc_methtype: 0x47bd
-  __TEXT.__const: 0x850
-  __TEXT.__objc_methname: 0x31026
-  __TEXT.__oslogstring: 0x8349
-  __TEXT.__gcc_except_tab: 0x2cd0
+2393.7.6.0.0
+  __TEXT.__text: 0x121298
+  __TEXT.__auth_stubs: 0x24e0
+  __TEXT.__objc_stubs: 0x259e0
+  __TEXT.__objc_methlist: 0xf7ec
+  __TEXT.__cstring: 0xde2f
+  __TEXT.__objc_classname: 0xfe9
+  __TEXT.__objc_methtype: 0x47d1
+  __TEXT.__const: 0x860
+  __TEXT.__objc_methname: 0x313cf
+  __TEXT.__oslogstring: 0x83f9
+  __TEXT.__gcc_except_tab: 0x2ca0
   __TEXT.__ustring: 0x33e
   __TEXT.__dlopen_cstrs: 0x248
   __TEXT.__constg_swiftt: 0x2a8

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x3ea0
-  __TEXT.__eh_frame: 0x740
-  __DATA_CONST.__auth_got: 0x12a0
-  __DATA_CONST.__got: 0x1e88
-  __DATA_CONST.__auth_ptr: 0xe0
-  __DATA_CONST.__const: 0x4480
-  __DATA_CONST.__cfstring: 0xd160
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__unwind_info: 0x3ee0
+  __TEXT.__eh_frame: 0x738
+  __DATA_CONST.__auth_got: 0x1280
+  __DATA_CONST.__got: 0x1e90
+  __DATA_CONST.__auth_ptr: 0xe8
+  __DATA_CONST.__const: 0x44d8
+  __DATA_CONST.__cfstring: 0xd1a0
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_arraydata: 0x808
   __DATA_CONST.__objc_arrayobj: 0x480
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x13c88
-  __DATA.__objc_selrefs: 0xb160
-  __DATA.__objc_ivar: 0x1308
+  __DATA.__objc_const: 0x11fa8
+  __DATA.__objc_selrefs: 0xb368
+  __DATA.__objc_ivar: 0x131c
   __DATA.__objc_data: 0x21d0
   __DATA.__data: 0x13aa
-  __DATA.__bss: 0x7d5
+  __DATA.__bss: 0x7d8
   __DATA.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6288
-  Symbols:   1642
-  CStrings:  11088
+  Functions: 6317
+  Symbols:   1639
+  CStrings:  11114
 
Symbols:
+ _AVSystemController_SomeSessionIsPlayingDidChangeNotification
+ _AXDeviceIsUnlocked
+ _kVOTEventCommandDecreaseSystemVolume
+ _kVOTEventCommandIncreaseSystemVolume
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$sypN
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy
CStrings:
+ "\x04\x11\x14\x13a\x11B\x7f\x03QC\"\x13RR4\x16\x11c%\x13\x12\xf0\xf0\xf0\xa1tA\x143\x11\xd11b#!\x13\x11\x12\x14\xe1C\x12\x13\xa2\x1a\x11C\x132\x14%"
+ "Not showing USB restricted mode alert because device is locked"
+ "SCROTokenSecureAttribute"
+ "Set system volume from %@ to %@"
+ "Should use AVAudioPlayer for sound. VoiceOverAudioPlayerEverywhere feature flag enabled"
+ "T@\"AXDispatchTimer\",&,N,V_simulatedLongPressTimer"
+ "TB,N,V_isIndefiniteLongPressOngoing"
+ "TI,N,V_indefiniteLongPressContextId"
+ "Td,N,V_lastSimulatedLongPressTime"
+ "T{CGPoint=dd},N,V_indefiniteLongPressPoint"
+ "VO loc string unexpectedly nil. key:'%@'. language:%@"
+ "VoiceOverAudioPlayerEverywhere"
+ "_cancelIndefiniteLongPress"
+ "_handleDecreaseSystemVolume:"
+ "_handleIncreaseSystemVolume:"
+ "_handleSystemVolumeChange:"
+ "_indefiniteLongPressContextId"
+ "_indefiniteLongPressPoint"
+ "_isIndefiniteLongPressOngoing"
+ "_lastSimulatedLongPressTime"
+ "_simulatedLongPressTimer"
+ "indefiniteLongPressContextId"
+ "indefiniteLongPressPoint"
+ "isEqualToVOTKeyInfo:"
+ "isIndefiniteLongPressOngoing"
+ "isLastItemInList"
+ "item.one.of.many"
+ "keyboardManagerHandleKeyDown:keyCode:modifierState:eventOrigin:"
+ "lastSimulatedLongPressTime"
+ "nameAndFootprintForLanguage:"
+ "setFlags:"
+ "setIndefiniteLongPressContextId:"
+ "setIndefiniteLongPressPoint:"
+ "setIsIndefiniteLongPressOngoing:"
+ "setIsLastItemInList:"
+ "setLastSimulatedLongPressTime:"
+ "setSimulatedLongPressTimer:"
+ "setUsagePage:"
+ "simulatedLongPressTimer"
+ "v36@0:8B16S20I24q28"
+ "voiceOverTraitFeedback"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1"
- "\x04\x11\x14\x13a\x11B\x7f\x03QC\"\x13RR4\x16\x11c%\x13\x12\xf0\xf0\xf0\xa1tA\x143\x11\xd11b#!\x13\x11\x12\x14\xd1C\x12\x13\xab\x11C\x132\x14%"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "VO loc string unexpectedly nil. key:'one.of.many'. language:%@"
- "invalid Collection: less than 'count' elements in collection"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91"

```
