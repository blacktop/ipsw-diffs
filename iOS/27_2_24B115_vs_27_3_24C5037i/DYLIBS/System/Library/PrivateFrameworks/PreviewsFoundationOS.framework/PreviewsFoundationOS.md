## PreviewsFoundationOS

> `/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS`

```diff

-24.20.10.0.0
-  __TEXT.__text: 0x13eb4c
+24.30.6.0.0
+  __TEXT.__text: 0x13ff80
   __TEXT.__objc_methlist: 0x274
-  __TEXT.__const: 0x1006c
+  __TEXT.__const: 0x1012c
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x5599
-  __TEXT.__swift5_typeref: 0x5d17
+  __TEXT.__cstring: 0x5639
+  __TEXT.__swift5_typeref: 0x5d77
   __TEXT.__swift5_capture: 0x32e4
-  __TEXT.__constg_swiftt: 0x59fc
-  __TEXT.__swift5_reflstr: 0x228c
-  __TEXT.__swift5_fieldmd: 0x3dc4
+  __TEXT.__constg_swiftt: 0x5a18
+  __TEXT.__swift5_reflstr: 0x229c
+  __TEXT.__swift5_fieldmd: 0x3dec
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x1298
   __TEXT.__swift5_proto: 0x8b8
-  __TEXT.__swift5_types: 0x598
+  __TEXT.__swift5_types: 0x59c
   __TEXT.__swift5_protos: 0xd0
   __TEXT.__swift5_mpenum: 0x80
-  __TEXT.__swift_as_entry: 0x1d0
-  __TEXT.__swift_as_ret: 0x1c0
-  __TEXT.__swift_as_cont: 0x2d8
+  __TEXT.__swift_as_entry: 0x1d4
+  __TEXT.__swift_as_ret: 0x1c4
+  __TEXT.__swift_as_cont: 0x2dc
   __TEXT.__oslogstring: 0x7dc
-  __TEXT.__unwind_info: 0x6b78
-  __TEXT.__eh_frame: 0x8174
+  __TEXT.__unwind_info: 0x6bc0
+  __TEXT.__eh_frame: 0x81ec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x998
-  __AUTH_CONST.__const: 0x100f8
+  __DATA_CONST.__got: 0x9a8
+  __AUTH_CONST.__const: 0x10168
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x2768
-  __AUTH_CONST.__auth_got: 0x1ad0
+  __AUTH_CONST.__auth_got: 0x1b00
   __AUTH.__objc_data: 0x1f8
   __AUTH.__data: 0x26d0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x6bb0
+  __DATA.__data: 0x6bd8
   __DATA.__common: 0x18
   __DATA_DIRTY.__data: 0x38
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8083
-  Symbols:   2421
-  CStrings:  429
+  Functions: 8102
+  Symbols:   2429
+  CStrings:  434
 
Symbols:
+ _symbolic SS4path_t
+ _symbolic Ss_Ss4patht
+ _symbolic _____ 20PreviewsFoundationOS16CrashReportErrorV015DyldLibraryLoaddF0V13FailureReasonO
+ _symbolic _____ySs_Ss4pathtG 17_StringProcessing5RegexV
+ _symbolic _____ySs_Ss4patht_G 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_Ss4patht_GSg 17_StringProcessing5RegexV5MatchV
+ _symbolic _____y_____G s16PartialRangeFromV SS5IndexV
+ _type_layout_string 20PreviewsFoundationOS16CrashReportErrorV015DyldLibraryLoaddF0V13FailureReasonO
CStrings:
+ " couldn't load `"
+ " crashed because the App Sandbox blocked loading "
+ "#/'(?<path>[^']+)' \\(file system sandbox blocked open\\(\\)\\)/#"
+ "#/Library not loaded: (?<path>[^\\n]+)/#"
+ "__PREVIEWS_SIMULATE_ASSISTIVE_TECHNOLOGY"
+ "` because the App Sandbox blocked access to it. Previews loads your app's code after the sandbox is applied, so libraries outside the app's container need explicit access.\n\nTo fix this, add `"
+ "` environment variable in your scheme's Run settings, or embed "
- "(dyld: launch, loading dependent libraries(.|\\n)*)?Library not loaded: @rpath/(?<library>.+?(?=/))"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/UITestingAgent/Shared/PreviewsFoundation/Sources/PreviewsFoundation/CrashReports/Errors/CrashReportError+DyldLibraryLoadCrashError.swift"
```
