## SwiftMLS

> `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS`

```diff

-  __TEXT.__text: 0x2acdac
+  __TEXT.__text: 0x2adf80
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x24d08
-  __TEXT.__constg_swiftt: 0x48e0
-  __TEXT.__swift5_typeref: 0x38aa
-  __TEXT.__swift5_reflstr: 0x5a91
-  __TEXT.__swift5_fieldmd: 0x5f94
+  __TEXT.__const: 0x24d50
+  __TEXT.__constg_swiftt: 0x4908
+  __TEXT.__swift5_typeref: 0x38b8
+  __TEXT.__swift5_reflstr: 0x5bb1
+  __TEXT.__swift5_fieldmd: 0x6000
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0xb08
   __TEXT.__swift5_proto: 0xdc4
   __TEXT.__swift5_types: 0x6b4
   __TEXT.__swift5_capture: 0x2a4
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__oslogstring: 0x6108
-  __TEXT.__cstring: 0x3e6d
-  __TEXT.__swift_as_entry: 0x618
-  __TEXT.__swift_as_ret: 0xc0c
+  __TEXT.__oslogstring: 0x62e8
+  __TEXT.__cstring: 0x3e8d
+  __TEXT.__swift_as_entry: 0x61c
+  __TEXT.__swift_as_ret: 0xc10
   __TEXT.__swift_as_cont: 0x15c0
   __TEXT.__swift5_mpenum: 0x138
-  __TEXT.__unwind_info: 0xa3e0
-  __TEXT.__eh_frame: 0x20130
+  __TEXT.__unwind_info: 0xa258
+  __TEXT.__eh_frame: 0x20420
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xc950
-  __AUTH_CONST.__objc_const: 0x10e0
-  __AUTH_CONST.__auth_got: 0x18d0
-  __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0x4a48
-  __DATA.__data: 0x3398
-  __DATA.__bss: 0x1b300
-  __DATA.__common: 0x580
+  __AUTH_CONST.__objc_const: 0x1100
+  __AUTH_CONST.__auth_got: 0x18d8
+  __AUTH.__objc_data: 0x48
+  __AUTH.__data: 0x22d0
+  __DATA.__data: 0x3090
+  __DATA.__bss: 0x1ae80
+  __DATA.__common: 0x4c0
+  __DATA_DIRTY.__objc_data: 0x290
+  __DATA_DIRTY.__data: 0x2ac8
+  __DATA_DIRTY.__common: 0xc0
+  __DATA_DIRTY.__bss: 0x480
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10469
-  Symbols:   2449
-  CStrings:  817
+  Functions: 10525
+  Symbols:   2451
+  CStrings:  823
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
Symbols:
+ _swift_release_x10
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 8SwiftMLS0E0O0C0O12ReadEpochKeyV
CStrings:
+ "%s: No current state available, skipping continuity token commitment verification"
+ "%s: clearing cached commit metadata on advance to new state %s"
+ "%s: clearing cached commit metadata on era advance from %u to %u"
+ "%s: discarding cached commit for era %u because group is now at era %u"
+ "%s: rejecting non-advancing Welcome { current: %s, proposed: %s }"
+ "%s: rejecting same-era Welcome — local self credential is still valid (no §9.5.4 replacement authorized)"
+ "%s: rejecting same-era Welcome — new self credential is not a valid successor of current local self credential"
+ "Join failed, Welcome was previously consumed { ref: %s }"
+ "maxRetainedEpochsPerGroup"
- "%s: We could not verify the continuity token commitment in era advancement: %@"
- "%s: We could not verify the continuity token commitment in resync: %@"
- "We could not verify the continuity token commitment: %@"

```
