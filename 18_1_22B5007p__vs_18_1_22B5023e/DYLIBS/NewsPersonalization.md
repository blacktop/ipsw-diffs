## NewsPersonalization

> `/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization`

```diff

-5564.0.0.0.0
-  __TEXT.__text: 0x2691d4
+5578.1.0.0.0
+  __TEXT.__text: 0x267d28
   __TEXT.__auth_stubs: 0x4980
   __TEXT.__objc_methlist: 0x2d0
-  __TEXT.__const: 0x125bc
-  __TEXT.__cstring: 0x116b7
-  __TEXT.__constg_swiftt: 0x4498
-  __TEXT.__swift5_typeref: 0x3870
-  __TEXT.__swift5_fieldmd: 0x4a18
+  __TEXT.__const: 0x1278c
+  __TEXT.__cstring: 0x11957
+  __TEXT.__constg_swiftt: 0x44f8
+  __TEXT.__swift5_typeref: 0x38b2
+  __TEXT.__swift5_fieldmd: 0x4a90
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_reflstr: 0x4240
-  __TEXT.__swift5_assocty: 0x7b8
-  __TEXT.__swift5_proto: 0xfbc
-  __TEXT.__swift5_types: 0x588
+  __TEXT.__swift5_reflstr: 0x42c0
+  __TEXT.__swift5_assocty: 0x7f8
+  __TEXT.__swift5_proto: 0xfd4
+  __TEXT.__swift5_types: 0x594
   __TEXT.__swift5_protos: 0xa8
-  __TEXT.__swift5_capture: 0xb10
+  __TEXT.__swift5_capture: 0xab4
   __TEXT.__swift5_mpenum: 0x110
-  __TEXT.__unwind_info: 0x7620
-  __TEXT.__eh_frame: 0xbc5c
+  __TEXT.__unwind_info: 0x7660
+  __TEXT.__eh_frame: 0xbc9c
   __TEXT.__objc_classname: 0x491
-  __TEXT.__objc_methname: 0xbfc0
+  __TEXT.__objc_methname: 0xc002
   __TEXT.__objc_methtype: 0x1a52
-  __DATA_CONST.__got: 0x1910
-  __DATA_CONST.__const: 0xab8
+  __DATA_CONST.__got: 0x1918
+  __DATA_CONST.__const: 0xaf8
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_catlist2: 0x8
   __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0x1c08
   __DATA_CONST.__objc_protorefs: 0x190
   __AUTH_CONST.__auth_got: 0x24c0
-  __AUTH_CONST.__auth_ptr: 0x1368
-  __AUTH_CONST.__const: 0x8b50
+  __AUTH_CONST.__auth_ptr: 0x1358
+  __AUTH_CONST.__const: 0x8b80
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xff70
-  __AUTH.__objc_data: 0x688
-  __AUTH.__data: 0x1228
-  __DATA.__data: 0x3db0
+  __AUTH_CONST.__objc_const: 0xffd0
+  __AUTH.__objc_data: 0x460
+  __AUTH.__data: 0xc40
+  __DATA.__data: 0x3b30
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x182a0
-  __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x8b8
-  __DATA_DIRTY.__data: 0x8188
-  __DATA_DIRTY.__bss: 0x4e90
-  __DATA_DIRTY.__common: 0x70
+  __DATA.__bss: 0x17fa0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0xae0
+  __DATA_DIRTY.__data: 0x8ac8
+  __DATA_DIRTY.__bss: 0x54a0
+  __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
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
-  Functions: 9958
-  Symbols:   396
-  CStrings:  3313
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 9996
+  Symbols:   403
+  CStrings:  3323
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x13
CStrings:
+ "App context was empty, returning no tag recommendations from app context"
+ "Attempting to fetch tag recommendations with %!l(MISSING)u context items using requestID %!{(MISSING)public}@"
+ "Error did not cast to NewsTabiTagSuggestionsWork.Errors %!{(MISSING)public}@"
+ "Failed to generate auto favorites as a result of a missing tag suggestions configuration however this user already has auto favorites, leaving them alone."
+ "Failed to generate auto favorites as a result of a missing tag suggestions configuration, this user also has no auto favorites, this is indicative of a first ever launch, setting gems as auto favorites."
+ "Fetching tag recommendations with %!l(MISSING)u app based context items"
+ "Fetching tag recommendations with %!l(MISSING)u web based context items"
+ "Web context was empty, returning no tag recommendations from web context"
+ "articleConfig"
+ "dataSource"
+ "myMagazinesConfiguration"
+ "scoreOutputName"
- "Attempting to fetch tag recommendations with requestID %!{(MISSING)public}@"
- "Encountered a FeedViewEvent for a topic or channel with no specified tagID %!@(MISSING)"

```
