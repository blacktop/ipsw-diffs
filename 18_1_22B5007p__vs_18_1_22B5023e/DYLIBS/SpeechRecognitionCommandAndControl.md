## SpeechRecognitionCommandAndControl

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl`

```diff

-94.0.0.0.0
-  __TEXT.__text: 0x8df48
-  __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x9350
-  __TEXT.__const: 0x4b6
-  __TEXT.__oslogstring: 0x25d1
-  __TEXT.__cstring: 0x6bf7
-  __TEXT.__gcc_except_tab: 0x201c
+98.1.0.0.0
+  __TEXT.__text: 0x904c0
+  __TEXT.__auth_stubs: 0x15c0
+  __TEXT.__objc_methlist: 0x94e0
+  __TEXT.__const: 0x4c6
+  __TEXT.__oslogstring: 0x26b0
+  __TEXT.__cstring: 0x6d07
+  __TEXT.__gcc_except_tab: 0x1fe4
   __TEXT.__ustring: 0x36
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2448
-  __TEXT.__objc_classname: 0x1695
-  __TEXT.__objc_methname: 0x1d1d3
-  __TEXT.__objc_methtype: 0x3a3c
-  __TEXT.__objc_stubs: 0x13060
-  __DATA_CONST.__got: 0xd30
-  __DATA_CONST.__const: 0x1800
+  __TEXT.__unwind_info: 0x24b8
+  __TEXT.__objc_classname: 0x16eb
+  __TEXT.__objc_methname: 0x1d93a
+  __TEXT.__objc_methtype: 0x3ca8
+  __TEXT.__objc_stubs: 0x13560
+  __DATA_CONST.__got: 0xd50
+  __DATA_CONST.__const: 0x18b0
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6850
+  __DATA_CONST.__objc_selrefs: 0x69d8
   __DATA_CONST.__objc_superrefs: 0x2c8
-  __DATA_CONST.__objc_arraydata: 0x870
-  __AUTH_CONST.__auth_got: 0xad0
-  __AUTH_CONST.__const: 0x1620
-  __AUTH_CONST.__cfstring: 0x8b20
-  __AUTH_CONST.__objc_const: 0x10d80
+  __DATA_CONST.__objc_arraydata: 0x890
+  __AUTH_CONST.__auth_got: 0xaf0
+  __AUTH_CONST.__const: 0x16c0
+  __AUTH_CONST.__cfstring: 0x8c60
+  __AUTH_CONST.__objc_const: 0x111a8
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x29e0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x9e8
-  __DATA.__data: 0x14c0
-  __DATA.__bss: 0x468
+  __DATA.__objc_ivar: 0xa0c
+  __DATA.__data: 0x1590
+  __DATA.__bss: 0x480
   __DATA.__common: 0x1a8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices
+  - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices

   - /System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl
   - /System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI
   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3763
-  Symbols:   4983
-  CStrings:  6703
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3812
+  Symbols:   5050
+  CStrings:  6800
 
Symbols:
+ _AXDeviceIsRealityDevice
+ _AXValueCreate
+ _AudioServicesCreateSystemSoundIDWithOptions
+ _AudioServicesPlaySystemSoundWithOptions
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kAXWebContentTrait
+ _kAudioServicesCreateSystemSoundIDOptionAudioFileURLKey
+ _kAudioServicesPlaySystemSoundOptionBehaviorKey
+ _kAudioServicesPlaySystemSoundOptionFlagsKey
+ _kCACCommandContextRequiresCarPlay
+ _kCACCommandContextRequiresVoiceControlEnabled
CStrings:
+ "\x01!\x11"
+ "\x03\x15\x111\x11"
+ "@\"<CACEditingModeOverlayManagerDelegate>\""
+ "@\"<SRCSTextMarkerRangeProtocol>\"32@0:8@\"<SRCSTextMarkerProtocol>\"16@\"<SRCSTextMarkerProtocol>\"24"
+ "@\"<SRCSTextMarkerRangeProtocol>\"32@0:8{_NSRange=QQ}16"
+ "@\"<SRCSTextMarkerRangeProtocol>\"40@0:8@\"<SRCSTextMarkerProtocol>\"16@\"<SRCSTextMarkerProtocol>\"24@32"
+ "@\"CACEditingModeOverlayViewController\""
+ "@\"NSMutableArray\"24@?0B8@12B20"
+ "@\"NSString\"40@0:8@\"<SRCSTextMarkerRangeProtocol>\"16@\"NSDictionary\"24@?<v@?@\"<SRCSTextMarkerRangeProtocol>\"@\"NSString\">32"
+ "@32@0:8@\"<SRCSTextMarkerProtocol>\"16@\"<SRCSTextMarkerProtocol>\"24"
+ "@40@0:8@16@24@?32"
+ "@40@0:8{_NSRange=QQ}16q32"
+ "B24@0:8@\"CACEditingModeOverlayManager\"16"
+ "B32@0:8@\"<SRCSTextMarkerProtocol>\"16@24"
+ "B32@?0@\"CACSceneManager\"8Q16^B24"
+ "CACEditingModeOverlayManagerDelegate"
+ "CACElementTests"
+ "CarPlay Connected"
+ "CarPlay Disconnected"
+ "Disabling attention aware due to carplay active"
+ "InfoMessage.CarPlayInUse"
+ "InfoMessage.ReturnedToPhone"
+ "Loaded commands override table: %!@(MISSING)"
+ "Loaded commands table: %!@(MISSING)"
+ "Reproduced rdar://132435403.  Fell back to alternate element for scrolling."
+ "RequiresCarPlay"
+ "RequiresVoiceControlEnabled"
+ "Resolved attention aware setting - %!@(MISSING)"
+ "SRCSTextMarkerRangeProtocol"
+ "System.WakeListeningCarPlay"
+ "System.WakeListeningIPhoneFromCarPlay"
+ "T@\"<CACEditingModeOverlayManagerDelegate>\",W,N,V_delegate"
+ "T@\"CACEditingModeOverlayViewController\",&,N,V_editingModeOverlayViewController"
+ "TB,N,V_carPlayAvailable"
+ "TB,N,V_carPlayConnectedWirelessly"
+ "URLByDeletingLastPathComponent"
+ "URLByDeletingPathExtension"
+ "_appendCarPlayLayouts:"
+ "_builtinCommandsCatalogURL"
+ "_carPlayAvailable"
+ "_carPlayConnectedWirelessly"
+ "_combinationsFromTitle:isCarPlayConnected:"
+ "_dictationRecognizerModeUponCarPlayConnect"
+ "_editingModeOverlayViewController"
+ "_lineFetchingGeneration"
+ "_lineFetchingQueue"
+ "_programmaticallySelectedElement"
+ "_programmaticallySelectedRange"
+ "_suffixedURLsForURL:"
+ "_testCombinationsFromTitle:isCarPlayConnected:"
+ "_uiPresentingSceneManagers"
+ "_visibleLineRangesForElement:lineFetchingGeneration:"
+ "_webVisibleLineRangesForElement:lineFetchingGeneration:"
+ "addLikelySubtagsForLocaleIdentifier:"
+ "adjustCapsAndSpacingUsingLeadingText:localeIdentifier:vocabularyEntries:spellingGuessesBlock:"
+ "carPlayAvailable"
+ "carPlayConnectedDidChange"
+ "carPlayConnectedWirelessly"
+ "carPlayDidConnect:"
+ "containsMarker:forUIElement:"
+ "containsRange:forUIElement:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "currentSession"
+ "d24@0:8@\"CACEditingModeOverlayManager\"16"
+ "dictionaryByMergingEntriesFromDictionary:"
+ "editingModeOverlayViewController"
+ "elementForAttribute:"
+ "elementForAttribute:parameter:"
+ "elementForTextMarker:"
+ "en_CA"
+ "es_MX"
+ "es_US"
+ "f24@0:8@\"CACEditingModeOverlayManager\"16"
+ "indexesOfObjectsPassingTest:"
+ "initWithContentsOfURL:"
+ "intersectSet:"
+ "isCarPlayScene"
+ "isMainDisplayScene"
+ "isOverlayFadingEnabledForEditingModeOverlayManager:"
+ "objectForRange:withParameterizedAttribute:"
+ "overlayFadeDelayForEditingModeOverlayManager:"
+ "overlayFadeOpacityForEditingModeOverlayManager:"
+ "pathExtension"
+ "rangeForTextMarker:"
+ "rangeForTextMarkers:"
+ "rangeWithAXAttribute:"
+ "reverseObjectEnumerator"
+ "setCarPlayAvailable:"
+ "setCarPlayConnectedWirelessly:"
+ "setEditingModeOverlayViewController:"
+ "shouldScrollIfShowingLastVisibleRow"
+ "sleepCarPlay"
+ "systemBlackColor"
+ "systemGray4Color"
+ "systemLanguages"
+ "textLineEndMarker:"
+ "textLineStartMarker:"
+ "textMarkerFrame:"
+ "textMarkerRangeForSelection"
+ "textMarkersForRange:"
+ "transportType"
+ "unionOrderedSet:"
+ "v40@0:8{_NSRange=QQ}16@32"
+ "visibleTextRange"
+ "voice.control.slash"
+ "wakeCarPlay"
+ "willProgrammaticallySelectRange:forElement:"
- "\x03\x15\x11\x11"
- "@\"NSString\"48@0:8{_NSRange=QQ}16@\"NSDictionary\"32@?<v@?@\"<SRCSTextMarkerRangeProtocol>\"@\"NSString\">40"
- "@48@0:8{_NSRange=QQ}16@32@?40"
- "_carPlayDidConnect:"
- "_combinationsFromTitle:"
- "_pathToBuiltinCommandsCatalog"
- "_visibleRangesForElement:unit:"
- "adjustCapsAndSpacingUsingLeadingText:localeIdentifier:spellingGuessesBlock:"
- "status-mic-off"
- "status-mic-on"

```
