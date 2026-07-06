## SmartNameSuggestionsService

> `/System/Library/PrivateFrameworks/SmartNameSuggestions.framework/XPCServices/SmartNameSuggestionsService.xpc/SmartNameSuggestionsService`

```diff

-  __TEXT.__text: 0x30334
-  __TEXT.__auth_stubs: 0x1940
-  __TEXT.__objc_stubs: 0x600
-  __TEXT.__objc_methlist: 0x430
-  __TEXT.__const: 0x14f6
-  __TEXT.__objc_classname: 0x3c5
-  __TEXT.__objc_methname: 0xc31
-  __TEXT.__constg_swiftt: 0x984
-  __TEXT.__swift5_typeref: 0x660
-  __TEXT.__swift5_reflstr: 0x5a0
-  __TEXT.__swift5_fieldmd: 0x670
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0x120
-  __TEXT.__cstring: 0x997
-  __TEXT.__swift5_capture: 0xd0
-  __TEXT.__oslogstring: 0xc3b
-  __TEXT.__swift5_proto: 0x94
-  __TEXT.__swift5_types: 0x74
+  __TEXT.__text: 0x17230
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x198
+  __TEXT.__const: 0xd18
+  __TEXT.__objc_classname: 0x29f
+  __TEXT.__objc_methname: 0x4db
+  __TEXT.__constg_swiftt: 0x48c
+  __TEXT.__swift5_typeref: 0x468
+  __TEXT.__swift5_reflstr: 0x1d3
+  __TEXT.__swift5_fieldmd: 0x2b4
+  __TEXT.__cstring: 0x4bf
+  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__oslogstring: 0x8ab
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_assocty: 0xd8
+  __TEXT.__swift5_proto: 0x64
+  __TEXT.__swift5_types: 0x44
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x90
-  __TEXT.__objc_methtype: 0x295
-  __TEXT.__swift5_protos: 0x4
+  __TEXT.__objc_methtype: 0x1db
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x870
-  __TEXT.__eh_frame: 0xf18
-  __DATA_CONST.__const: 0xd98
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__eh_frame: 0xab8
+  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0xca8
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__auth_ptr: 0x298
-  __DATA.__objc_const: 0x1048
-  __DATA.__objc_selrefs: 0x318
-  __DATA.__objc_data: 0x9d8
-  __DATA.__data: 0x1198
-  __DATA.__bss: 0x1200
-  __DATA.__common: 0xc0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__auth_got: 0xa58
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_ptr: 0x2b0
+  __DATA.__objc_const: 0x860
+  __DATA.__objc_selrefs: 0x1b0
+  __DATA.__objc_data: 0x258
+  __DATA.__data: 0xa48
+  __DATA.__bss: 0xc80
+  __DATA.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/MapKit.framework/MapKit
-  - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/FileDerivatives.framework/FileDerivatives

   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit
+  - /System/Library/PrivateFrameworks/SmartNameSuggestions.framework/SmartNameSuggestions
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
-  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 655
-  Symbols:   249
-  CStrings:  319
+  Functions: 335
+  Symbols:   197
+  CStrings:  185
 
Sections:
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_entry : content changed
Symbols:
+ _SNSmartNameSuggestionsErrorDomain
+ _objc_release_x9
- _NLTagAdjective
- _NLTagAdverb
- _NLTagNoun
- _NLTagPronoun
- _NLTagSchemeLexicalClass
- _NLTagVerb
- _NSURLAttributeModificationDateKey
- _NSURLContentTypeKey
- _NSURLIsDirectoryKey
- _NSURLIsHiddenKey
- _NSURLIsPackageKey
- _OBJC_CLASS_$_FPSandboxingURLWrapper
- _OBJC_CLASS_$_NLLanguageRecognizer
- _OBJC_CLASS_$_NLTagger
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_SNDirectorySuggestionRequest
- _OBJC_CLASS_$_SNFileSuggestionRequest
- _OBJC_CLASS_$_SNNameSuggestionRequest
- _OBJC_CLASS_$_SNNameSuggestionResponse
- _OBJC_CLASS_$_UITextChecker
- _OBJC_METACLASS_$_SNDirectorySuggestionRequest
- _OBJC_METACLASS_$_SNFileSuggestionRequest
- _OBJC_METACLASS_$_SNNameSuggestionRequest
- _OBJC_METACLASS_$_SNNameSuggestionResponse
- __objc_autoreleasePoolPop
- __objc_autoreleasePoolPush
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- _free
- _log2
- _objc_autorelease
- _objc_autoreleaseReturnValue
- _objc_retain_x9
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _realpath$DARWIN_EXTSN
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_cvw_allocateGenericValueMetadataWithLayoutString
- _swift_endAccess
- _swift_getFunctionTypeMetadata0
- _swift_getGenericMetadata
- _swift_getObjCClassFromMetadata
- _swift_isaMask
- _swift_makeBoxUnique
- _swift_release_x1
- _swift_release_x22
- _swift_retain_x23
- _swift_retain_x28
- _swift_runtimeSupportsNoncopyableTypes
- _swift_unexpectedError
CStrings:
- "$__lazy_storage_$_allExtensions"
- "$__lazy_storage_$_originalBaseName"
- "$__lazy_storage_$_originalExtension"
- "$__lazy_storage_$_originalType"
- "$__lazy_storage_$_siblingNameSet"
- "?"
- "@20@0:8B16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@44@0:8@16@24B32@36"
- "@44@0:8@16@24B32^@36"
- "@48@0:8@16B24B28@32^@40"
- "An unknown error occurred."
- "B"
- "Children names have been provided skipping lookup"
- "Enumerating to get children of %{private}s"
- "Enumerating to get siblings of %{private}s"
- "Failed to get children %{public}@"
- "Failed to get enumerator for url %{private}s"
- "Failed to resolve url with realpath error=%d url=%{private}s"
- "Found children count=%{public}ld"
- "Found siblings count=%{public}ld"
- "Found type for url %{public}s"
- "Looking up type from url"
- "NSCoding"
- "NSSecureCoding"
- "No content was available to analyze."
- "No derived content could be produced from the input."
- "No suggestions could be produced for the given input."
- "Received invalid URL in the request: %s"
- "Request created with url %{private}s"
- "Request with initial url %{private}s"
- "SNDirectorySuggestionRequest"
- "SNFileSuggestionRequest"
- "SNNameSuggestionRequest"
- "SNNameSuggestionResponse"
- "Sibling names have been provided skipping lookup"
- "SmartNameSuggestionsService.NameSuggestionRequest"
- "SmartNameSuggestionsService.NameSuggestionResponse"
- "SmartNameSuggestionsService/FilenameQualityScorer.swift"
- "Suggestion Refiner Removed %{public}ld suggestions"
- "T@\"NSArray\",N,C"
- "T@\"NSDate\",N,C"
- "T@\"NSString\",N,C"
- "T@\"NSString\",N,R"
- "T@\"NSURL\",N,R"
- "TB,N,R"
- "TB,N,R,VisDirectory"
- "TB,R"
- "The caller does not have permission to use this service."
- "The content type is not supported."
- "The language model encountered an error."
- "The request did not contain enough content to produce meaningful suggestions."
- "The request was malformed or missing required parameters."
- "The request was rejected due to content safety policy."
- "The suggestion service is unavailable."
- "URL is not a file URL: "
- "Unable to caption image"
- "Unable to find type from URL %{public}@"
- "Unable to read siblings %{public}@"
- "Using non-default value for %{public}s: %{bool}d"
- "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
- "\\d{4}[-_]?\\d{2}[-_]?\\d{2}[-_T ]\\d{2}[-_:]?\\d{2}[-_:]?\\d{2}"
- "\\d{4}[-_]\\d{2}[-_]\\d{2}"
- "^[A-Z][a-z]+[A-Z][a-z]+"
- "^[a-z]+[A-Z][a-z]+"
- "^\\d[\\d\\s\\-_.]*\\d$|^\\d$"
- "_TtC27SmartNameSuggestionsService17SuggestionRefiner"
- "_TtC27SmartNameSuggestionsService21FilenameQualityScorer"
- "_isSpeculative"
- "_url"
- "bestExtension"
- "boolForKey:"
- "childrenNames"
- "creationDate"
- "currentLanguage"
- "currentScript"
- "decodeBoolForKey:"
- "defaultManager"
- "dominantLanguage"
- "dpCache"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "fetchMissingAttributes"
- "firstMatchInString:options:range:"
- "initWithCoder:"
- "initWithPattern:options:error:"
- "initWithSuggestions:url:directory:pathExtension:"
- "initWithSuggestions:url:directory:reasoning:"
- "initWithTagSchemes:"
- "initWithURL:typeIdentifier:speculative:error:"
- "initialSuggestions"
- "isDirectory"
- "languageRecognizer"
- "localeIdentifier"
- "locationString"
- "minWordLength"
- "originalFilename"
- "pathExtension"
- "processString:"
- "range"
- "rangeOfMisspelledWordInString:range:startingAt:wrap:language:"
- "requestURL"
- "reset"
- "setChildrenNames:"
- "setCreationDate:"
- "setLocaleIdentifier:"
- "setLocationString:"
- "setSiblingNames:"
- "setString:"
- "setTextContent:"
- "setTextSummary:"
- "siblingNames"
- "spellChecker"
- "startedAccessing"
- "stringByAppendingPathExtension:"
- "stringByDeletingPathExtension"
- "suggestedBaseNames"
- "suggestionsWithExtension:"
- "supportsSecureCoding"
- "textContent"
- "textSummary"
- "typeIdentifier"
- "url"
- "urlWrapper"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "visibleItemNamesIn:forChildrenRequest:forDirectory:dropName:error:"
- "wordCache"
- "wrapperWithURL:readonly:error:"
- "スクリーンショット"

```
