## SiriSuggestionsInternalXPCServices

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsInternalXPCServices.xpc/SiriSuggestionsInternalXPCServices`

```diff

-3400.118.1.0.0
-  __TEXT.__text: 0x2be8
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x58
-  __TEXT.__const: 0x134
-  __TEXT.__cstring: 0x4c0
-  __TEXT.__objc_methname: 0x269
-  __TEXT.__oslogstring: 0x207
+3400.124.2.0.0
+  __TEXT.__text: 0x75a8
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x8c
+  __TEXT.__const: 0x2e4
+  __TEXT.__cstring: 0x73d
+  __TEXT.__objc_methname: 0x2e9
+  __TEXT.__oslogstring: 0x379
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xb0
-  __TEXT.__swift5_typeref: 0xaf
-  __TEXT.__swift5_fieldmd: 0x40
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__constg_swiftt: 0x16c
+  __TEXT.__swift5_typeref: 0x155
+  __TEXT.__swift5_reflstr: 0x112
+  __TEXT.__swift5_fieldmd: 0xdc
+  __TEXT.__swift5_types: 0x18
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0xe9
-  __TEXT.__swift5_capture: 0x88
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__eh_frame: 0x180
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x230
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_capture: 0xf8
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__eh_frame: 0x4a0
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0xe0
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x460
-  __DATA.__objc_selrefs: 0x60
-  __DATA.__objc_data: 0x1d0
-  __DATA.__data: 0x168
-  __DATA.__common: 0x40
+  __DATA.__objc_const: 0x6a8
+  __DATA.__objc_selrefs: 0x78
+  __DATA.__objc_data: 0x258
+  __DATA.__data: 0x3a0
+  __DATA.__common: 0x48
+  __DATA.__bss: 0x200
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete
+  - /System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers
+  - /System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions
   - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI
+  - /System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 89
-  Symbols:   81
-  CStrings:  88
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 195
+  Symbols:   114
+  CStrings:  111
 
Symbols:
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_reportUnimplementedInitializer
+ _objc_release
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_allocBox
+ _swift_allocError
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_makeBoxUnique
+ _swift_willThrow
CStrings:
+ ".cxx_destruct"
+ "Enabled feature extraction logger"
+ "Enabled feature service"
+ "Feature Extraction disabled. Only using raw remembers logger"
+ "Feature Service disabled."
+ "SiriAutoCompleteIndexBuilder updateIndexForAppInstall done. Added %!l(MISSING)d phrases"
+ "SiriSuggestionsInternalXPCServices log failed in deserialisation. error: %!@(MISSING)"
+ "SiriSuggestionsInternalXPCServices log failed. error: %!@(MISSING)"
+ "SiriSuggestionsInternalXPCServices.ServiceDelegate"
+ "SiriSuggestionsInternalXPCServices.SiriSuggestionsInternalXPCServices"
+ "Unable to deserialise featureConfig from TransportWrapper"
+ "_TtC34SiriSuggestionsInternalXPCServices28DefaultFeatureServiceFactory"
+ "_TtC34SiriSuggestionsInternalXPCServices31DefaultSuggestionsLoggerFactory"
+ "featureFlagProvider"
+ "featureServiceFactory"
+ "init()"
+ "logEngagementFor:with:invocationType:featureConfig:with:"
+ "logFrom:deliveryVehicle:generationId:featureConfig:with:"
+ "siriRemembersLogger"
+ "suggestionsLoggerFactory"
+ "v16@0:8"
+ "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSUUID\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSData\"16@\"NSUUID\"24@\"NSData\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
- "SiriAutoCompleteIndexBuilder updateIndexForAppInstall function done with updatedRecords - %!l(MISSING)d"

```
