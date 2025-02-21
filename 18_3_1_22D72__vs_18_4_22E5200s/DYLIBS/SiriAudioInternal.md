## SiriAudioInternal

> `/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal`

```diff

-3403.2.1.0.0
-  __TEXT.__text: 0x4c410
-  __TEXT.__auth_stubs: 0x1b10
-  __TEXT.__objc_methlist: 0x120
-  __TEXT.__const: 0xc78
-  __TEXT.__cstring: 0x14c1
-  __TEXT.__swift5_typeref: 0xc1d
-  __TEXT.__swift5_fieldmd: 0x520
-  __TEXT.__constg_swiftt: 0x5bc
+3404.63.1.0.0
+  __TEXT.__text: 0x492a8
+  __TEXT.__auth_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0x388
+  __TEXT.__const: 0xd88
+  __TEXT.__cstring: 0x113a
+  __TEXT.__swift5_typeref: 0xc53
+  __TEXT.__swift5_fieldmd: 0x548
+  __TEXT.__constg_swiftt: 0x614
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x567
-  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_reflstr: 0x597
+  __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x58
-  __TEXT.__oslogstring: 0x6a2c
-  __TEXT.__swift5_capture: 0x7c8
-  __TEXT.__unwind_info: 0x898
-  __TEXT.__eh_frame: 0xc68
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__oslogstring: 0x65fc
+  __TEXT.__swift5_capture: 0x7b8
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x4c
+  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__eh_frame: 0xac0
   __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0xbc1
+  __TEXT.__objc_methname: 0xbae
   __TEXT.__objc_methtype: 0x494
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x540
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x350
+  __DATA_CONST.__objc_selrefs: 0x420
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xd90
-  __AUTH_CONST.__auth_ptr: 0x330
-  __AUTH_CONST.__const: 0x18d0
-  __AUTH_CONST.__objc_const: 0x1988
-  __AUTH.__objc_data: 0x590
-  __AUTH.__data: 0x2e8
-  __DATA.__data: 0x870
+  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH_CONST.__auth_ptr: 0x358
+  __AUTH_CONST.__const: 0x1870
+  __AUTH_CONST.__objc_const: 0x1648
+  __AUTH.__objc_data: 0x558
+  __AUTH.__data: 0x428
+  __DATA.__data: 0x940
   __DATA.__bss: 0x780
-  __DATA.__common: 0x400
+  __DATA.__common: 0x488
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
-  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
   - /System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit
   - /System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils

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
-  Functions: 723
-  Symbols:   240
-  CStrings:  599
+  Functions: 706
+  Symbols:   255
+  CStrings:  565
 
Symbols:
+ _swift_endAccess
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_initStructMetadataWithLayoutString
+ _swift_setDeallocating
+ _swift_storeEnumTagSinglePayloadGeneric
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "Filtering out suggestion because Apple Music subscription type/status is either unknown or notSubscribed"
+ "GenericMusicItemEntity/song"
+ "INSearchForMediaAppIntentHandler#handle failed to get criteria from internal signals or mediaSearch"
+ "INSearchForMediaAppIntentHandler#handle invoking SearchForPodcastsAppIntent with criteria: %s"
+ "INSearchForMediaAppIntentHandler#handle using SearchForPodcastsAppIntent"
+ "NewsPodcastRequest"
+ "UseCases:PlayMoreLikeThis"
+ "_TtC17SiriAudioInternal25FirstPartyMusicSubscriber"
+ "mediaContainer"
+ "subscriptionProvider"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "INSearchForMediaAppIntentHandler#handle detected app intent with invalid parameters, trying with updated version"
- "INSearchForMediaAppIntentHandler#handle failed to get criteria from mediaSearch"
- "INSearchForMediaAppIntentHandler#handle failed to get identifier from mediaItem"
- "INSearchForMediaAppIntentHandler#handle invoking OpenMusicItemAppIntent with identifier: %s"
- "INSearchForMediaAppIntentHandler#handle invoking OpenPodcastEpisodeAppIntent with identifier: %s"
- "INSearchForMediaAppIntentHandler#handle invoking OpenPodcastShowAppIntent with identifier: %s"
- "INSearchForMediaAppIntentHandler#handle mediaType is not podcastShow or podcastEpisode, defaulting to invoke OpenPodcastShowAppIntent with identifier: %s"
- "INSearchForMediaAppIntentHandler#handle updated app intent threw an error: %s"
- "INSearchForMediaAppIntentHandler#handle using OpenMusicItemIntent"
- "INSearchForMediaAppIntentHandler#handle using Podcasts open intent"
- "INSearchForMediaAppIntentHandler#resolveMediaItems failed to convert identifier to PlaybackItem for mediaItem: %{public}s"
- "INSearchForMediaAppIntentHandler#resolveMediaItems failed to get MusicSiriRepresentation"
- "INSearchForMediaAppIntentHandler#resolveMediaItems resolving item: %s"
- "INSearchForMediaAppIntentHandler#resolveMediaItems resolving podcast item: %s"
- "INSearchForMediaAppIntentHandler#resolveMediaItems with musicSiriRepresentationString = %s"
- "Insufficient space allocated to copy string contents"
- "LNActionExecutorErrorDomain"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "artwork"
- "code"
- "domain"
- "intentId"
- "invalid Collection: less than 'count' elements in collection"
- "sirikit.intent.media.PlayMediaIntent"
- "verb"

```
