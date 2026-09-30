## AirPlayReceiverKit

> `/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit`

```diff

-890.61.4.11.2
-  __TEXT.__text: 0x23e24
+890.66.3.0.0
+  __TEXT.__text: 0x24240
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x13c4
-  __TEXT.__cstring: 0x85ec
+  __TEXT.__cstring: 0x869a
   __TEXT.__const: 0x52
   __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__unwind_info: 0xaa8
   __TEXT.__objc_classname: 0x248
-  __TEXT.__objc_methname: 0x4e69
+  __TEXT.__objc_methname: 0x4fbd
   __TEXT.__objc_methtype: 0x112c
-  __TEXT.__objc_stubs: 0x3480
+  __TEXT.__objc_stubs: 0x3600
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__const: 0x888
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_selrefs: 0x12b8
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x390

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF542C43-6BAD-3153-8FF4-A331A362265C
-  Functions: 894
-  Symbols:   3113
-  CStrings:  1946
+  UUID: 28632667-A480-3041-BFAB-544AF026F716
+  Functions: 896
+  Symbols:   3131
+  CStrings:  1961
 
Symbols:
+ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.3
+ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.4
+ _objc_msgSend$_primaryMediaCharacteristic
+ _objc_msgSend$availableLanguages
+ _objc_msgSend$currentEvent
+ _objc_msgSend$customMediaSelectionScheme
+ _objc_msgSend$extendedLanguageTag
+ _objc_msgSend$hasMediaCharacteristic:
+ _objc_msgSend$mediaCharacteristic
+ _objc_msgSend$mediaCharacteristicsOfPreferredCustomMediaSelectionSchemes
+ _objc_msgSend$selectMediaPresentationLanguage:forMediaSelectionGroup:
+ _objc_msgSend$selectMediaPresentationSetting:forMediaSelectionGroup:
+ _objc_msgSend$selectors
+ _objc_msgSend$settings
Functions:
~ -[APRKMediaPlayer _setPropertyWithDictionary:] : 3068 -> 3220
~ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:] : 644 -> 1440
+ _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_7
~ -[APRKMediaPlayer _updateAudioSessionMode:].cold.2 : 68 -> 60
~ -[APRKMediaPlayer _updateAudioSessionMode:].cold.3 : 68 -> 60
~ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.2 : 32 -> 60
+ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.3
+ ___48-[APRKMediaPlayer _pausePlayerIfNeededForState:]_block_invoke.cold.1
CStrings:
+ "890.66.3"
+ "Ignoring skippableState set property - payload eventID doesn't match the current eventID { %@ != %@ }"
+ "Selecting MediaPresentationLanguage %@"
+ "Selecting MediaPresentationSetting %@"
+ "_primaryMediaCharacteristic"
+ "availableLanguages"
+ "currentEvent"
+ "customMediaSelectionScheme"
+ "extendedLanguageTag"
+ "hasMediaCharacteristic:"
+ "mediaCharacteristic"
+ "mediaCharacteristicsOfPreferredCustomMediaSelectionSchemes"
+ "selectMediaPresentationLanguage:forMediaSelectionGroup:"
+ "selectMediaPresentationSetting:forMediaSelectionGroup:"
+ "selectors"
+ "settings"
- "890.61.4.11.2"

```
