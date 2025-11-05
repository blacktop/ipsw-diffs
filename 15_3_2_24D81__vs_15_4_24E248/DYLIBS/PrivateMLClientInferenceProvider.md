## PrivateMLClientInferenceProvider

> `/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/Versions/A/PrivateMLClientInferenceProvider`

```diff

-109.0.0.0.0
-  __TEXT.__text: 0x3cd9c
-  __TEXT.__auth_stubs: 0x1a30
-  __TEXT.__const: 0x1148
-  __TEXT.__cstring: 0xe73
+113.711.0.0.0
+  __TEXT.__text: 0x3f138
+  __TEXT.__auth_stubs: 0x1b50
+  __TEXT.__const: 0x1178
+  __TEXT.__cstring: 0xab3
   __TEXT.__constg_swiftt: 0x344
-  __TEXT.__swift5_typeref: 0x5aa
-  __TEXT.__swift5_fieldmd: 0x60c
+  __TEXT.__swift5_typeref: 0x686
+  __TEXT.__swift5_fieldmd: 0x648
   __TEXT.__swift5_types: 0x4c
-  __TEXT.__swift5_reflstr: 0x78d
+  __TEXT.__swift5_reflstr: 0x82c
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0xcc
-  __TEXT.__oslogstring: 0x12fb
-  __TEXT.__swift5_capture: 0x7c
-  __TEXT.__unwind_info: 0x878
-  __TEXT.__eh_frame: 0x1180
+  __TEXT.__swift_as_entry: 0x9c
+  __TEXT.__swift_as_ret: 0x94
+  __TEXT.__oslogstring: 0x14db
+  __TEXT.__swift5_capture: 0xa6c
+  __TEXT.__unwind_info: 0x860
+  __TEXT.__eh_frame: 0x1238
   __TEXT.__objc_methname: 0x108
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0xd18
-  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__const: 0x24b0
   __AUTH_CONST.__objc_const: 0x258
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x4a0
-  __DATA.__data: 0x638
+  __DATA.__data: 0x648
   __DATA.__bss: 0x1400
-  __DATA.__common: 0x20
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9CD168FF-B7F8-3825-A737-DE4D8F1089FF
-  Functions: 590
-  Symbols:   301
-  CStrings:  223
+  UUID: 5DAC0629-524C-3F91-9A8E-6605186410FA
+  Functions: 763
+  Symbols:   333
+  CStrings:  210
 
Symbols:
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_project_boxed_opaque_existential_0
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_PrivateMLClientInferenceProvider
+ _block_copy_helper
+ _block_destroy_helper
+ _objectdestroyTm
+ _swift_setDeallocating
+ _symbolic SS3key______5valuet 19TokenGenerationCore18PromptTemplateInfoV19RichVariableBindingV
+ _symbolic SS3key______5valuetSg 19TokenGenerationCore18PromptTemplateInfoV19RichVariableBindingV
+ _symbolic SSIego_
+ _symbolic SbIegd_
+ _symbolic SccySDySSypGSg______pG s5ErrorP
+ _symbolic ShySSGIegr_
+ _symbolic _____ 19TokenGenerationCore18PromptTemplateInfoV19RichVariableBindingV9ComponentV7ContentO4TextV
+ _symbolic _____ s5UInt8V
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Iegr_ 10Foundation4UUIDV
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic _____Sg 15PrivateMLClient0A9MLRequestV12RichVariableV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 15PrivateMLClient0C9MLRequestV12RichVariableV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15PrivateMLClient0D9MLRequestV12RichVariableV9ComponentO
+ _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
- ___swift_destroy_boxed_opaque_existential_1Tm
- _symbolic SDySSypGSg
CStrings:
+ "%s No Support for countTokensPromptTemplate - %s"
+ "%s No support for countTokens - %s"
+ "%s Unknown default variable binding"
+ "%s VB Text %s isSelfAttention:%{bool}d"
+ "%s daemon %s for pid=%ld is not allowed"
+ "%s prewarm with no Tokenizer called. sessionUUID=%s modelBundleIdentifier=%s featureIdentifier=%s bundleIdentifier=%s"
+ "%s request assetBundleIdentifier: %s"
+ "Prewam Urgency Level: imminent"
+ "Request failed with TrustedCloudComputeError: %@"
+ "apple-tokenizer-name"
- "%s daemon for pid=%ld is not allowed"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
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
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
