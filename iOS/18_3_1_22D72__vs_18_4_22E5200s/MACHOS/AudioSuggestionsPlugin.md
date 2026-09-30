## AudioSuggestionsPlugin

> `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin`

```diff

-3403.2.1.0.0
-  __TEXT.__text: 0xbce8
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__const: 0x888
-  __TEXT.__cstring: 0x8ca
-  __TEXT.__constg_swiftt: 0x2c4
-  __TEXT.__swift5_typeref: 0x2b9
-  __TEXT.__swift5_fieldmd: 0x36c
-  __TEXT.__swift5_reflstr: 0x31f
+3404.63.1.0.0
+  __TEXT.__text: 0x179e8
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__const: 0xce8
+  __TEXT.__cstring: 0x7fb
+  __TEXT.__constg_swiftt: 0x3dc
+  __TEXT.__swift5_typeref: 0x441
+  __TEXT.__swift5_fieldmd: 0x46c
+  __TEXT.__swift5_reflstr: 0x40f
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__objc_methname: 0x37
-  __TEXT.__oslogstring: 0x272
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0x88
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__objc_methname: 0x67
+  __TEXT.__oslogstring: 0x2e9
+  __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__eh_frame: 0x380
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__auth_ptr: 0x1c0
-  __DATA_CONST.__const: 0xa70
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x468
+  __TEXT.__eh_frame: 0x648
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_ptr: 0x2c8
+  __DATA_CONST.__const: 0xe50
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2f8
-  __DATA.__objc_selrefs: 0x30
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x780
-  __DATA.__common: 0xa48
+  __DATA.__objc_const: 0x3b0
+  __DATA.__objc_selrefs: 0x48
+  __DATA.__data: 0xa48
+  __DATA.__bss: 0xe80
+  __DATA.__common: 0xbb8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
-  - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI
+  - /System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

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
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 218
-  Symbols:   96
-  CStrings:  79
+  Functions: 340
+  Symbols:   125
+  CStrings:  85
 
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _bzero
+ _objc_release
+ _objc_release_x19
+ _objc_release_x21
+ _objc_release_x8
+ _objc_retain_x19
+ _objc_retain_x20
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease_n
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_initStructMetadataWithLayoutString
+ _swift_makeBoxUnique
+ _swift_release_n
+ _swift_setDeallocating
+ _swift_stdlib_isStackAllocationSafe
+ _swift_stdlib_random
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_willThrow
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x22
- _objc_retain_x23
- _swift_retain_n
CStrings:
+ "Filtering out suggestion because Apple Music subscription type/status is either unknown or notSubscribed"
+ "GenericMusicItemEntity/song"
+ "NewsPodcastRequest"
+ "RecognizeMusicIntent"
+ "UseCases:PlayMoreLikeThis"
+ "UseCases:PlayXbyY"
+ "_TtC22AudioSuggestionsPlugin25FirstPartyMusicSubscriber"
+ "__intentParameterOverride_"
+ "backgroundMusic"
+ "chillOut"
+ "com.apple.musicrecognition"
+ "discovery"
+ "internalSignals"
+ "musicKit://station?catalogID=ra.u-"
+ "newMusicMix"
+ "peacefulFocus"
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
