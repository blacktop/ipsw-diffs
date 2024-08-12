## Settings

> `/System/Library/PrivateFrameworks/Settings.framework/Settings`

```diff

-203.0.0.0.0
-  __TEXT.__text: 0x7c128
-  __TEXT.__auth_stubs: 0x2350
+206.0.0.0.0
+  __TEXT.__text: 0x7ed5c
+  __TEXT.__auth_stubs: 0x2400
   __TEXT.__delay_helper: 0x158
   __TEXT.__objc_methlist: 0x610
-  __TEXT.__const: 0x3f98
+  __TEXT.__const: 0x3f38
   __TEXT.__cstring: 0x3d22
   __TEXT.__constg_swiftt: 0x2020
-  __TEXT.__swift5_typeref: 0x20a6
-  __TEXT.__swift5_reflstr: 0x1041
-  __TEXT.__swift5_fieldmd: 0x1220
+  __TEXT.__swift5_typeref: 0x20e0
+  __TEXT.__swift5_reflstr: 0x106a
+  __TEXT.__swift5_fieldmd: 0x1244
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x5f0
-  __TEXT.__swift5_capture: 0x3ec
+  __TEXT.__swift5_capture: 0x414
   __TEXT.__swift5_proto: 0x2a0
   __TEXT.__swift5_types: 0x164
-  __TEXT.__oslogstring: 0x769
+  __TEXT.__oslogstring: 0x791
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1d18
-  __TEXT.__eh_frame: 0x1950
+  __TEXT.__unwind_info: 0x1da8
+  __TEXT.__eh_frame: 0x19c8
   __TEXT.__objc_classname: 0xc1
-  __TEXT.__objc_methname: 0x1484
+  __TEXT.__objc_methname: 0x14ee
   __TEXT.__objc_methtype: 0x303
-  __DATA_CONST.__got: 0x740
-  __DATA_CONST.__const: 0x4d0
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__const: 0x510
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_protorefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x11a8
-  __AUTH_CONST.__auth_ptr: 0xc98
-  __AUTH_CONST.__const: 0x2250
+  __AUTH_CONST.__auth_got: 0x1200
+  __AUTH_CONST.__auth_ptr: 0xc80
+  __AUTH_CONST.__const: 0x22a0
   __AUTH_CONST.__objc_const: 0x4c40
-  __AUTH.__objc_data: 0x580
-  __AUTH.__data: 0x900
-  __DATA.__data: 0x18d8
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4868
-  __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x11b8
-  __DATA_DIRTY.__data: 0x13a8
-  __DATA_DIRTY.__bss: 0x700
-  __DATA_DIRTY.__common: 0x20
+  __AUTH.__objc_data: 0x450
+  __DATA.__data: 0x13c0
+  __DATA.__bss: 0x3258
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0x12e8
+  __DATA_DIRTY.__data: 0x2210
+  __DATA_DIRTY.__crash_info: 0x40
+  __DATA_DIRTY.__bss: 0x1d00
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

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
-  Functions: 2578
-  Symbols:   358
-  CStrings:  739
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2613
+  Symbols:   372
+  CStrings:  746
 
Symbols:
+ _CGRectGetMinY
+ _OBJC_CLASS_$_LNContentType
+ _OBJC_CLASS_$_LNExportedContentConfiguration
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
+ _swift_getOpaqueTypeMetadata2
CStrings:
+ "Entity and Enum indexing threw: %!@(MISSING)"
+ "Error during %!s(MISSING):%!s(MISSING) URL request %!@(MISSING)"
+ "Error fetching URL for %!@(MISSING)"
+ "Error performing entity query %!s(MISSING)"
+ "LNEntity<%!@(MISSING)> url fetch error: %!@(MISSING)"
+ "Unable to export or fetch entity URL for %!s(MISSING)"
+ "data"
+ "exportedContent"
+ "fileURL"
+ "initWithContentType:preferredExtractionType:"
+ "setExportConfiguration:"
- "Error performing entity request %!s(MISSING)"
- "Error performing enum URL request %!@(MISSING)"
- "Missing URL for %!@(MISSING)"
- "Unable to fetch entity URL for %!s(MISSING)"
- "fetching URL for LNEntity.identifier: %!@(MISSING)"

```
