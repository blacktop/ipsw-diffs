## SiriAutoCompleteAPI

> `/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI`

```diff

-3404.70.4.0.0
-  __TEXT.__text: 0x28f08
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__const: 0x146c
-  __TEXT.__cstring: 0xf7c
-  __TEXT.__swift5_typeref: 0x6d6
-  __TEXT.__oslogstring: 0x107e
-  __TEXT.__swift5_reflstr: 0x579
+3404.77.1.0.0
+  __TEXT.__text: 0x2cd14
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__const: 0x14cc
+  __TEXT.__cstring: 0x100c
+  __TEXT.__swift5_typeref: 0x720
+  __TEXT.__oslogstring: 0x1244
+  __TEXT.__swift5_reflstr: 0x599
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0x9b4
-  __TEXT.__swift5_fieldmd: 0x754
-  __TEXT.__swift5_proto: 0xd8
+  __TEXT.__constg_swiftt: 0xa04
+  __TEXT.__swift5_fieldmd: 0x788
+  __TEXT.__swift5_proto: 0xdc
   __TEXT.__swift5_types: 0x80
-  __TEXT.__swift5_protos: 0x20
+  __TEXT.__swift5_protos: 0x24
   __TEXT.__swift_as_entry: 0xa0
   __TEXT.__swift_as_ret: 0x94
-  __TEXT.__unwind_info: 0xbb8
-  __TEXT.__eh_frame: 0x1628
+  __TEXT.__unwind_info: 0xc38
+  __TEXT.__eh_frame: 0x17f8
   __TEXT.__objc_methname: 0x19b
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x8a0
-  __AUTH_CONST.__auth_ptr: 0x2a0
-  __AUTH_CONST.__const: 0xb48
-  __AUTH_CONST.__objc_const: 0xdb8
+  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_ptr: 0x2b8
+  __AUTH_CONST.__const: 0xbc8
+  __AUTH_CONST.__objc_const: 0xdf8
   __AUTH.__data: 0x430
-  __DATA.__data: 0x418
+  __DATA.__data: 0x420
+  __DATA.__common: 0x30
   __DATA.__bss: 0x1300
-  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0xa80
-  __DATA_DIRTY.__common: 0x60
+  __DATA_DIRTY.__data: 0xaa8
+  __DATA_DIRTY.__common: 0x58
   __DATA_DIRTY.__bss: 0x480
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1124
-  Symbols:   436
-  CStrings:  192
+  Functions: 1167
+  Symbols:   478
+  CStrings:  204
 
Symbols:
+ _objc_release_x28
+ _objc_retain_x8
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _objc_retain_x19
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "%s"
+ ",\nNormalizedPhraseTokens: "
+ ", \nSearchTokens: "
+ "CRLCreateBoardIntent"
+ "DefaultMorphunTokenizer: fallback to default tokenization"
+ "Fetched AFPreferences Siri Locale: %s"
+ "Freeform_CreateBoard"
+ "Function: %s > Count actionIdFilteredPhrases: '%ld'"
+ "Function: %s > Deduped '%s', with actionId %s"
+ "Function: %s > Empty attributeFilters, not querying DB"
+ "Function: %s > Initialized %s VectorDB client with DB directory: %s"
+ "Function: %s > Successfully deleted %ld phrases corresponding to source 'assistantSuggestions'"
+ "Function: %s > Successfully deleted %ld phrases corresponding to source tapped suggestion"
+ "Function: %s > Successfully deleted %ld phrases with source %lld"
+ "Function: %s > input parameter `phrases` is empty. Not running insertPhrasesForAssistantSuggestions"
+ "filterPhrasesBasedOnActionIdentifier(candidatePhrases:)"
+ "filterZhPhrasesBasedOnQueryCharacter: %s is not (a prefix) in %s, skip candidate"
+ "filterZhPhrasesBasedOnQueryCharacter: Morphun ready: %{bool}d, queryTokens: %s, filteredZhCharacterTokens: %s"
+ "locale"
- "    Phrase: %s,\n    InvocationPhrase: %s,\n    Source: %s,\n    EditDistance: %f, \n    BundleId: %s, \n    ActionIdentifier: %s"
- ", \nsearchTokens: "
- "Function: %s > Successfully deleted all phrases corresponding to source 'assistantSuggestions' with return code: %ld"
- "Function: %s > Successfully deleted all phrases corresponding to source tapped suggestion: %ld"
- "Function: %s > Successfully deleted all phrases with source %lld with return code: %ld"
- "Function: %s > creating DB directory path: %s"
- "Siri locale %s"

```
