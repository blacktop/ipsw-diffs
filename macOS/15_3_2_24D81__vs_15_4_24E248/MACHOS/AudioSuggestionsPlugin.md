## AudioSuggestionsPlugin

> `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Contents/MacOS/AudioSuggestionsPlugin`

```diff

-3403.2.1.0.0
-  __TEXT.__text: 0xbe10
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__const: 0x888
-  __TEXT.__cstring: 0x8ca
-  __TEXT.__constg_swiftt: 0x2c4
-  __TEXT.__swift5_typeref: 0x2b9
-  __TEXT.__swift5_fieldmd: 0x36c
-  __TEXT.__swift5_reflstr: 0x31f
+3404.75.2.14.1
+  __TEXT.__text: 0x1a6cc
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__const: 0xbd0
+  __TEXT.__cstring: 0x85b
+  __TEXT.__constg_swiftt: 0x3f8
+  __TEXT.__swift5_typeref: 0x43f
+  __TEXT.__swift5_fieldmd: 0x4a0
+  __TEXT.__swift5_reflstr: 0x42f
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__objc_methname: 0x37
-  __TEXT.__oslogstring: 0x272
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__objc_methname: 0x78
+  __TEXT.__oslogstring: 0x4a1
+  __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__eh_frame: 0x380
-  __DATA_CONST.__auth_got: 0x3a0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__auth_ptr: 0x1d0
-  __DATA_CONST.__const: 0xa58
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__eh_frame: 0x690
+  __DATA_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_ptr: 0x2a0
+  __DATA_CONST.__const: 0xf50
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2f8
-  __DATA.__objc_selrefs: 0x30
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x780
-  __DATA.__common: 0xa48
+  __DATA.__objc_const: 0x3b0
+  __DATA.__objc_selrefs: 0x50
+  __DATA.__data: 0xa38
+  __DATA.__bss: 0xe80
+  __DATA.__common: 0xbb8
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
-  - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/Versions/A/SiriSuggestionsAPI
+  - /System/Library/PrivateFrameworks/SiriAudioSupport.framework/Versions/A/SiriAudioSupport
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/Versions/A/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/Versions/A/SiriUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 31111B04-8B70-34A6-81A2-734ADAC85B9A
-  Functions: 218
-  Symbols:   85
-  CStrings:  79
+  UUID: 4D629436-79C3-3248-9AE3-7F19CF4EE2B0
+  Functions: 370
+  Symbols:   105
+  CStrings:  95
 
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _bzero
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease_n
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_initStructMetadata
+ _swift_makeBoxUnique
+ _swift_release_n
+ _swift_setDeallocating
+ _swift_stdlib_isStackAllocationSafe
+ _swift_stdlib_random
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_willThrow
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_retain_n
CStrings:
+ "Filtering out suggestion because Apple Music subscription type/status is either unknown or notSubscribed"
+ "GenericMusicItemEntity/song"
+ "NewsPodcastRequest"
+ "PlaylistNameParameterBuilder#transformer Received playIntent: %s"
+ "PlaylistNameParameterBuilder#transformer mediaItemTitle: %s"
+ "PlaylistTypeParameterBuilder#transformer Apple catalog playlist: %s"
+ "PlaylistTypeParameterBuilder#transformer Received playIntent: %s"
+ "PlaylistTypeParameterBuilder#transformer personal playlist: %s"
+ "PlaylistTypeParameterBuilder#transformer personalized Apple playlist: %s"
+ "RecognizeMusicIntent"
+ "UseCases:PlayMoreLikeThis"
+ "UseCases:PlayXbyY"
+ "_TtC22AudioSuggestionsPlugin25FirstPartyMusicSubscriber"
+ "__intentParameterOverride_"
+ "backgroundMusic"
+ "chillOut"
+ "com.apple.musicrecognition.mac"
+ "debugDescription"
+ "discovery"
+ "internalSignals"
+ "musicKit://playlist?catalogID"
+ "musicKit://playlist?deviceLocalID"
+ "musicKit://station?catalogID=ra.u-"
+ "newMusicMix"
+ "peacefulFocus"
+ "playlistType"
+ "privatePlayMediaIntentData"
+ "productivity"
+ "subscriptionProvider"
+ "verb"
+ "x-sampradio://store/ra.u-"
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
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "sirikit.intent.media.PlayMediaIntent"

```
