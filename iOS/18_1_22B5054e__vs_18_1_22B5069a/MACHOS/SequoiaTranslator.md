## SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

-294.3.0.0.0
-  __TEXT.__text: 0x232474
-  __TEXT.__auth_stubs: 0x6230
+294.5.0.0.0
+  __TEXT.__text: 0x236098
+  __TEXT.__auth_stubs: 0x6250
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x1c40
   __TEXT.__const: 0x128e4
-  __TEXT.__cstring: 0xb1e1
+  __TEXT.__cstring: 0xb281
   __TEXT.__objc_methname: 0x8a2f
   __TEXT.__objc_classname: 0x377
   __TEXT.__objc_methtype: 0x2e06
   __TEXT.__constg_swiftt: 0xac48
-  __TEXT.__swift5_typeref: 0x1ca50
+  __TEXT.__swift5_typeref: 0x1cc1a
   __TEXT.__swift5_builtin: 0x30c
   __TEXT.__swift5_reflstr: 0x7d02
   __TEXT.__swift5_fieldmd: 0x5e08

   __TEXT.__swift5_types: 0x53c
   __TEXT.__swift5_capture: 0x26f4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x80bc
+  __TEXT.__oslogstring: 0x891c
   __TEXT.__swift5_protos: 0x80
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x6ba0
-  __TEXT.__eh_frame: 0x57b4
-  __DATA_CONST.__auth_got: 0x3120
+  __TEXT.__unwind_info: 0x6bd8
+  __TEXT.__eh_frame: 0x58ac
+  __DATA_CONST.__auth_got: 0x3130
   __DATA_CONST.__got: 0x1938
-  __DATA_CONST.__auth_ptr: 0x3028
-  __DATA_CONST.__const: 0xbff8
+  __DATA_CONST.__auth_ptr: 0x3010
+  __DATA_CONST.__const: 0xc000
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_const: 0xbfe0
   __DATA.__objc_selrefs: 0x1f70
   __DATA.__objc_data: 0x8550
-  __DATA.__data: 0xefb8
+  __DATA.__data: 0xefe8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x10d40
   __DATA.__common: 0x7a0

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
-  Functions: 9857
-  Symbols:   3028
-  CStrings:  3445
+  Functions: 9864
+  Symbols:   3031
+  CStrings:  3475
 
Symbols:
+ _$s10Foundation4UUIDV11descriptionSSvg
+ _$sSS5index_8offsetBy07limitedC0SS5IndexVSgAE_SiAEtF
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "\n    minCharNumberCrossed: "
+ "\n    minTimeHasPassed: "
+ "\n    moreThanMaxTimeHasPassed: "
+ "\n    textHasChanged: "
+ "    isTokenBoundary: "
+ "Adding final translation; source text length: %!l(MISSING)d; sourceText: '%!{(MISSING)sensitive}s'"
+ "Adding partial translation CANCELED; id: %!{(MISSING)public}s"
+ "Adding partial translation; id: %!{(MISSING)public}s"
+ "Additional request to translate; finalTranslationRequestsQueue.count: %!{(MISSING)public}ld, partialTranslationRequest: %!{(MISSING)public}s"
+ "CANCELLING update of last submission; streaming request does not match the current request; steamingRequest.id: %!{(MISSING)public}s, currentRequestId: %!{(MISSING)public}s"
+ "Cannot set text streaming config because given config is nil"
+ "Changing state from %!{(MISSING)public}s to %!{(MISSING)public}s"
+ "Getting next partial request; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s, currentRequestId: %!{(MISSING)public}s"
+ "Idle timer for final result fired, performing final translation with streaming request; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s."
+ "Idle timer for partial result fired, but conditions don't allow for re-triggering a translation; id: %!{(MISSING)public}s"
+ "Idle timer for partial result fired, performing another partial translation. id: %!{(MISSING)public}s"
+ "Idle timer for partial result fired; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s, timeIntervalSinceLastSubmission: %!{(MISSING)public}f,  minTimeBetweenTranslations: %!{(MISSING)public}f, lastTranslatedText: %!{(MISSING)sensitive}s"
+ "Invalid symbol %!{(MISSING)public}s: returning generic symbol"
+ "Invalidating idle timers"
+ "MRAVOutputDeviceSymbolProvider found symbol %!{(MISSING)public}s"
+ "Next final request; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s"
+ "Not changing state because it's the same, %!{(MISSING)public}s"
+ "Not sending translation to delegate because partial translation is outdated; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s"
+ "Not updating text streaming config values because overrides enabled"
+ "Performing final translation; sourceText: %!{(MISSING)sensitive}s"
+ "Performing passthrough"
+ "Processing next translation"
+ "Processing next translation CANCELLED because state is already .translating"
+ "Returning empty partial request, not a match with current request"
+ "Sending translation to delegate; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s"
+ "Setting manager's text streaming config to %!{(MISSING)public}s"
+ "Setting up final timer for streaming request; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s"
+ "Setting up idle timer for streaming request; id: %!{(MISSING)public}s, sourceText: %!{(MISSING)sensitive}s"
+ "Starting partial translation; sourceText: %!{(MISSING)sensitive}s"
+ "Translation request conditions NOT satisfied; conditions:\n%!{(MISSING)public}s"
+ "Translation request conditions satisfied; conditions:\n%!{(MISSING)public}s"
+ "Translation request conditions satisfied; source or target locale changed"
+ "Trying to add partial translation with source '%!{(MISSING)sensitive}s', id: %!{(MISSING)public}s"
+ "Updating last submission info; id: %!{(MISSING)public}s"
+ "Updating text streaming config values; minTime: %!{(MISSING)public}f, maxTime: %!{(MISSING)public}f, userIdleTime: %!{(MISSING)public}f"
- "Adding a final translation with content %!{(MISSING)sensitive}s"
- "Adding a partial translation with content %!{(MISSING)sensitive}s"
- "Idle timer for final result fired, performing final translation; sourceText: %!{(MISSING)sensitive}s"
- "Idle timer for partial result fired, but conditions don't allow for re-triggering a translation for the text '%!{(MISSING)sensitive}s', so not doing anything"
- "Idle timer for partial result fired, performing another partial translation; sourceText: %!{(MISSING)sensitive}s"
- "Invalid symbol: returning generic symbol."
- "MRAVOutputDeviceSymbolProvider found symbol %!s(MISSING)"
- "Parameters for streaming translation are set to %!{(MISSING)public}s"
- "Skipping returning outdated partial translation result"
- "Trying to add a partial translation with content %!{(MISSING)sensitive}s"

```
