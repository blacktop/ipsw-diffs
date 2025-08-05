## TeaUI

> `/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI`

```diff

-991.2.0.0.0
-  __TEXT.__text: 0x3caa70
-  __TEXT.__auth_stubs: 0x5590
-  __TEXT.__objc_methlist: 0x59e0
-  __TEXT.__const: 0x1ea84
-  __TEXT.__cstring: 0x149c4
+999.2.0.0.0
+  __TEXT.__text: 0x3cc1b8
+  __TEXT.__auth_stubs: 0x55b0
+  __TEXT.__objc_methlist: 0x59e8
+  __TEXT.__const: 0x1eb64
+  __TEXT.__cstring: 0x14c74
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__oslogstring: 0x9c
-  __TEXT.__constg_swiftt: 0x12208
-  __TEXT.__swift5_typeref: 0xc5a6
+  __TEXT.__constg_swiftt: 0x12244
+  __TEXT.__swift5_typeref: 0xc5b6
   __TEXT.__swift5_builtin: 0x8fc
-  __TEXT.__swift5_reflstr: 0xb25f
-  __TEXT.__swift5_fieldmd: 0xdfd4
+  __TEXT.__swift5_reflstr: 0xb2df
+  __TEXT.__swift5_fieldmd: 0xe02c
   __TEXT.__swift5_assocty: 0x1458
-  __TEXT.__swift5_proto: 0x14c8
-  __TEXT.__swift5_types: 0xfcc
-  __TEXT.__swift5_capture: 0x6a90
+  __TEXT.__swift5_proto: 0x14d4
+  __TEXT.__swift5_types: 0xfd0
+  __TEXT.__swift5_capture: 0x6a80
   __TEXT.__swift5_mpenum: 0x34c
   __TEXT.__swift5_protos: 0x4f4
-  __TEXT.__unwind_info: 0x11654
-  __TEXT.__eh_frame: 0x7390
+  __TEXT.__unwind_info: 0x11704
+  __TEXT.__eh_frame: 0x73e8
   __TEXT.__objc_classname: 0x7f0
-  __TEXT.__objc_methname: 0xf6b7
+  __TEXT.__objc_methname: 0xf6c3
   __TEXT.__objc_methtype: 0x3abe
   __TEXT.__objc_stubs: 0x3920
   __DATA_CONST.__got: 0x12f8

   __DATA_CONST.__objc_catlist: 0x260
   __DATA_CONST.__objc_protolist: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b638
-  __DATA_CONST.__objc_selrefs: 0x3a68
+  __DATA_CONST.__objc_const: 0x1b688
+  __DATA_CONST.__objc_selrefs: 0x3a70
   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_classrefs: 0x588
   __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__objc_const: 0x1ed0
-  __AUTH_CONST.__const: 0x2b070
+  __AUTH_CONST.__const: 0x2b0f0
   __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__auth_got: 0x2ad8
+  __AUTH_CONST.__auth_got: 0x2ae8
   __AUTH.__objc_data: 0x4a90
   __AUTH.__data: 0x2a00
   __DATA.__objc_ivar: 0x19c
   __DATA.__objc_data: 0x5c8
-  __DATA.__data: 0x6d08
+  __DATA.__data: 0x6d18
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x18860
-  __DATA.__common: 0x98
+  __DATA.__bss: 0x189e0
+  __DATA.__common: 0xa0
   __DATA_DIRTY.__const: 0x50
   __DATA_DIRTY.__objc_const: 0x48
   __DATA_DIRTY.__objc_data: 0x6dc8
-  __DATA_DIRTY.__data: 0xe908
+  __DATA_DIRTY.__data: 0xe8d8
   __DATA_DIRTY.__bss: 0x6b40
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 364BDE82-329D-3ECD-B235-330D3906F543
-  Functions: 34945
-  Symbols:   19090
-  CStrings:  5244
+  UUID: A99F05A8-523A-3D9A-B8F9-ECE8C92E48C8
+  Functions: 34985
+  Symbols:   19104
+  CStrings:  5251
 
Symbols:
+ __swift_stdlib_bridgeErrorToNSError
+ _associated conformance 5TeaUI24PresentationHandlerErrorOSHAASQ
+ _objectdestroy.16Tm
+ _symbolic _____ 5TeaUI24PresentationHandlerErrorO
+ _symbolic _____yytG 13TeaFoundation6ResultO
CStrings:
+ "Presentation handler UID (%s) does not have a presentation handler with a matching UID registered. | The operation (%s will NOT be presented."
+ "Presentation operation (%s) encountered the following error during presentation: %@.\nIts presentation count will not be incremented."
+ "Presentation operation (%s) has `ignoreAfterSuccessfulPresentation` set to `true` and has successfully presented in the past. | This operation will NOT be presented."
+ "Presentation operation (%s) has a retry count of %ld and a maximum retry value of %ld. | This operation will NOT be presented."
+ "Presentation operation (%s) has completed execution but doesn't match the UID that's currently pending completion (%s)! | This queue is in a bad state so no further items will be processed."
+ "canOpenURL:"
+ "retryCounts"
+ "successfulPresentations"
- "Presentation operation (%s) does not have a presentation handler with a matching UID registered. | This operation will NOT be presented."

```
