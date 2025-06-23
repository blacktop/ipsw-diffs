## gamesaved

> `/usr/libexec/gamesaved`

```diff

-101.0.19.0.0
-  __TEXT.__text: 0x274a4
-  __TEXT.__auth_stubs: 0x1080
+101.0.20.0.0
+  __TEXT.__text: 0x27cd0
+  __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x348
-  __TEXT.__const: 0xc68
-  __TEXT.__objc_methname: 0xa9b
-  __TEXT.__cstring: 0xaf2
-  __TEXT.__oslogstring: 0xdcd
+  __TEXT.__const: 0xc98
+  __TEXT.__objc_methname: 0xafd
+  __TEXT.__cstring: 0xb02
+  __TEXT.__oslogstring: 0xe2d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x748
-  __TEXT.__swift5_typeref: 0x66c
-  __TEXT.__swift5_fieldmd: 0x3c8
+  __TEXT.__constg_swiftt: 0x760
+  __TEXT.__swift5_typeref: 0x684
+  __TEXT.__swift5_fieldmd: 0x3d4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x432
-  __TEXT.__swift5_capture: 0x27c
+  __TEXT.__swift5_reflstr: 0x452
+  __TEXT.__swift5_capture: 0x2a0
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x54
   __TEXT.__objc_classname: 0x66
   __TEXT.__objc_methtype: 0x3be
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0xcc
-  __TEXT.__unwind_info: 0xa68
-  __TEXT.__eh_frame: 0x1da0
-  __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x320
+  __TEXT.__swift_as_entry: 0x90
+  __TEXT.__swift_as_ret: 0xd4
+  __TEXT.__unwind_info: 0xaa8
+  __TEXT.__eh_frame: 0x1e50
+  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0xbe0
+  __DATA_CONST.__const: 0xc38
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0x3e8
+  __DATA.__objc_const: 0x13f0
+  __DATA.__objc_selrefs: 0x400
   __DATA.__objc_data: 0x430
-  __DATA.__data: 0xe70
+  __DATA.__data: 0xea0
   __DATA.__common: 0x78
   __DATA.__bss: 0xb80
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AEFBF8DE-22C8-37FD-8D32-4658AA8E7828
-  Functions: 626
-  Symbols:   447
-  CStrings:  342
+  UUID: C59325AC-1682-3849-8E08-AE04A5A9CEFF
+  Functions: 641
+  Symbols:   430
+  CStrings:  347
 
Symbols:
+ _BRAccountTokenDidChangeNotification
+ _OBJC_CLASS_$_BRAccount
+ _OBJC_CLASS_$_UIDevice
- _$s10Foundation12CharacterSetV13decimalDigitsACvgZ
- _$s10Foundation12CharacterSetV17controlCharactersACvgZ
- _$s10Foundation12CharacterSetV21punctuationCharactersACvgZ
- _$s10Foundation12CharacterSetVMa
- _$s10Foundation4DataVN
- _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
- _$sSS10FoundationE8EncodingV4utf8ACvgZ
- _$sSS10FoundationE8EncodingVMa
- _$sSSSysMc
- _$sSy10FoundationE18trimmingCharacters2inSSAA12CharacterSetV_tF
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
- _IOServiceMatching
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _kCFAllocatorDefault
- _kIOMainPortDefault
CStrings:
+ "Handling BRAccount Token Did Change notification"
+ "Invalidating container handlers"
+ "accountSigningInObserver"
+ "addObserverForName:object:queue:usingBlock:"
+ "currentDevice"
+ "startAccountTokenChangeObserverIfNeeded"
+ "v16@?0@\"NSNotification\"8"
- "GameSyncedDirectoryErrorDomain"
- "IOPlatformExpertDevice"

```
