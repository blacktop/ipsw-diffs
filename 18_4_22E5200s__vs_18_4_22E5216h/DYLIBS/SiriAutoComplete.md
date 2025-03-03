## SiriAutoComplete

> `/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete`

```diff

-3404.70.4.0.0
-  __TEXT.__text: 0x4cce4
-  __TEXT.__auth_stubs: 0x1790
-  __TEXT.__const: 0x1950
-  __TEXT.__cstring: 0xf87
-  __TEXT.__constg_swiftt: 0xca4
-  __TEXT.__swift5_typeref: 0xae1
-  __TEXT.__swift5_reflstr: 0x631
-  __TEXT.__swift5_fieldmd: 0x7e0
-  __TEXT.__swift5_capture: 0x114
-  __TEXT.__oslogstring: 0x29dc
-  __TEXT.__swift5_proto: 0x134
-  __TEXT.__swift5_types: 0xac
-  __TEXT.__swift_as_entry: 0xc4
-  __TEXT.__swift_as_ret: 0x14c
-  __TEXT.__swift5_protos: 0x2c
+3404.77.1.0.0
+  __TEXT.__text: 0x4b0c0
+  __TEXT.__auth_stubs: 0x17e0
+  __TEXT.__const: 0x19e0
+  __TEXT.__cstring: 0x1077
+  __TEXT.__constg_swiftt: 0xd1c
+  __TEXT.__swift5_typeref: 0xb5b
+  __TEXT.__swift5_reflstr: 0x641
+  __TEXT.__swift5_fieldmd: 0x834
+  __TEXT.__swift5_capture: 0xa0
+  __TEXT.__oslogstring: 0x304c
+  __TEXT.__swift5_proto: 0x13c
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift_as_entry: 0xb0
+  __TEXT.__swift_as_ret: 0xf0
+  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x11b0
-  __TEXT.__eh_frame: 0x2c60
-  __TEXT.__objc_methname: 0xb39
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x118
-  __DATA_CONST.__objc_classlist: 0xb0
+  __TEXT.__unwind_info: 0x1070
+  __TEXT.__eh_frame: 0x2630
+  __TEXT.__objc_methname: 0xb27
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x398
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH_CONST.__auth_ptr: 0x3e8
-  __AUTH_CONST.__const: 0x10f8
-  __AUTH_CONST.__objc_const: 0x1078
+  __DATA_CONST.__objc_selrefs: 0x390
+  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH_CONST.__auth_ptr: 0x3f8
+  __AUTH_CONST.__const: 0x10b0
+  __AUTH_CONST.__objc_const: 0x1148
   __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0xac0
-  __DATA.__data: 0x770
-  __DATA.__common: 0x80
-  __DATA.__bss: 0x1610
+  __AUTH.__data: 0xb68
+  __DATA.__data: 0x758
+  __DATA.__common: 0x98
+  __DATA.__bss: 0x1690
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x8b8
+  __DATA_DIRTY.__data: 0x8b0
   __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0x700
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

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

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1575
-  Symbols:   834
-  CStrings:  367
+  Functions: 1519
+  Symbols:   821
+  CStrings:  389
 
Symbols:
+ _OBJC_CLASS_$_INAddTasksIntent
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "%s: %lld is an unknown source and does not have a source runner"
+ "%s: AssistantSuggestions source does not have a source runner"
+ "%s: Attempted to update unregistered Morphun asset for locale %s onStartUpEvent, isAssetRegistered status for this locale: %{bool}d"
+ "%s: Locale change detected, update tokenizer"
+ "%s: Not adding intents from %s it is in deniedBundleIds"
+ "%s: Running index build, onStartUpEvent: %{bool}d. siriLocale: %s"
+ "%s: onStartUpEvent=true. Already built index for version %s within last 7 days. Not building again for this startUpEvent"
+ "Could not get AppIntentTranscriptSource runner in order to fetch phrases. Returning 0 AppIntentTranscript phrases"
+ "Could not get AppIntentTranscriptSource runner to build histogram for AppShortcut phrases. Returning 0 AppShortcut phrases"
+ "Could not get AppLaunchSource to fetch phrases. Returning 0 AppLaunch phrases"
+ "Could not get AppShortcutSource runner to fetch phrases. Returning 0 AppShortcut phrases"
+ "Could not get AssistantIntentExamplePhraseSource runner to fetch phrases. Returning 0 assistantIntentExamplePhrases phrases"
+ "Could not get SiriKitIntentTranscriptSource runner to fetch phrases. Returning 0 SiriKitIntentTranscript phrases"
+ "Could not get StaticSuggestionSource runner to fetch phrases. Returning 0 StaticSuggestion phrases"
+ "Could not get VoiceShortcutSource runner to fetch phrases. Returning 0 VoiceShortcut phrases"
+ "Current index version is: %s, and we want to build new index with version: %s. Index is not up-to-date and needs rebuilding"
+ "IndexBuilder: Not updating the full index build timestamp to user defaults due to: UpdateFullIndexBuildStamp=%{bool}d, numberStaticPhrasesAdded: %ld"
+ "IndexVersion %s is current and was built recently. Index does not need rebuilding"
+ "IndexVersion %s is current but was built awhile ago. Index needs rebuilding"
+ "Skipping App Shortcut from %s for %s since it's unlocalized"
+ "_TtC16SiriAutoComplete39DefaultAutoCompleteSourceRunnerProvider"
+ "com.apple.Keynote"
+ "com.apple.Numbers"
+ "com.apple.journal"
+ "deniedBundleIds"
+ "getApprovedPhrase: Failed to extract language code from {%s}, return nil"
+ "getApprovedPhrases: %s %s: %s"
+ "getPhrasesForApprovedActions: %s %s: %s"
+ "getPhrasesForApprovedActions: Action not approved %s - %s"
+ "getPhrasesForApprovedActions: Failed to get grouped phrases for %s - %s"
+ "getThirdPartyPhrases: %s %s: %s"
+ "sourceRunnerProvider"
+ "tokenAssetNotRegistered"
+ "tokenAssetRegistered"
- "%s: Locale change detected, update tokenizer and stopwords list"
- "%s: Running index build, onStartUpEvent: %{bool}d"
- "%s: Update unregistered Morphun asset onStartUpEvent, isAssetRegistered: %{bool}d"
- "%s: already built index on a start up event like GM Available or Suggestions startup recently, and Morphun asset was configured. Not building again"
- "allGroupedPhrases"
- "deniedLocalizedPhrases"
- "getFirstPartyEnPhrases: %s: %s"
- "getFirstPartyNonEnPhrases: %s: %s"
- "getFirstPartyNonEnPhrases: Action not approved %s - %s"
- "getFirstPartyNonEnPhrases: Failed to get grouped phrases for %s - %s"
- "getThirdPartyPhrases: %s: %s"
- "isLocalizedPhraseApproved: phrase {%s} approved: %{bool}d"

```
