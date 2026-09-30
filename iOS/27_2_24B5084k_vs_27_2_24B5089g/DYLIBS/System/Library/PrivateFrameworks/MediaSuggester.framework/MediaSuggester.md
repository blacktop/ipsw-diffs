## MediaSuggester

> `/System/Library/PrivateFrameworks/MediaSuggester.framework/MediaSuggester`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x7e6bc
+98.0.0.0.0
+  __TEXT.__text: 0x7fe84
   __TEXT.__objc_methlist: 0x10ac
-  __TEXT.__const: 0x3890
-  __TEXT.__cstring: 0x21a4
-  __TEXT.__swift5_typeref: 0x1942
+  __TEXT.__const: 0x38a0
+  __TEXT.__cstring: 0x2194
+  __TEXT.__swift5_typeref: 0x195a
   __TEXT.__constg_swiftt: 0x1874
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_reflstr: 0x1636
   __TEXT.__swift5_assocty: 0x718
-  __TEXT.__swift5_capture: 0x1c58
-  __TEXT.__oslogstring: 0x247c
+  __TEXT.__swift5_capture: 0x1f28
+  __TEXT.__oslogstring: 0x255c
   __TEXT.__swift5_proto: 0x1cc
   __TEXT.__swift5_types: 0x10c
   __TEXT.__swift5_fieldmd: 0xe84

   __TEXT.__swift_as_ret: 0x154
   __TEXT.__swift_as_cont: 0x278
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x25d0
+  __TEXT.__unwind_info: 0x2608
   __TEXT.__eh_frame: 0x387c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbd0
+  __DATA_CONST.__objc_selrefs: 0xbc8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__got: 0x630
-  __AUTH_CONST.__const: 0x5a28
-  __AUTH_CONST.__cfstring: 0x40
+  __DATA_CONST.__got: 0x638
+  __AUTH_CONST.__const: 0x6130
   __AUTH_CONST.__objc_const: 0x3900
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc50
   __AUTH.__objc_data: 0xd40
   __AUTH.__data: 0x1cf0
   __DATA.__data: 0xf58

   - /System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3871
+  Functions: 3928
   Symbols:   345
-  CStrings:  405
+  CStrings:  407
 
Symbols:
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ _kTCCServiceSiriAccess
- _CFPreferencesCopyAppValue
- ___CFConstantStringClassReference
CStrings:
+ "No available bundleIDs after the Siri excluded apps filter, returning empty array"
+ "No installed app for bundle ID: %s"
+ "TCC gave no kTCCServiceSiriAccess exclusion list, treating each app as allowed"
+ "kTCCServiceSiriAccess exclusion list is not an array of bundle identifiers"
+ "requestIdentifierOverride"
- "No available bundleIDs that are enabled for LFTA, returning empty array"
- "SiriCanLearnFromAppBlacklist"
- "com.apple.suggestions"
```
