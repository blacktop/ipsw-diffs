## TranslationAPISupportExtension

> `/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension`

```diff

-300.15.0.0.0
-  __TEXT.__text: 0x1a520
-  __TEXT.__auth_stubs: 0x10d0
+336.4.0.0.0
+  __TEXT.__text: 0x1a4d0
+  __TEXT.__auth_stubs: 0x11a0
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0xc18
-  __TEXT.__swift5_typeref: 0x140d
-  __TEXT.__cstring: 0x612
+  __TEXT.__const: 0xca0
+  __TEXT.__swift5_typeref: 0x12b7
+  __TEXT.__cstring: 0x707
   __TEXT.__objc_methname: 0x43e
+  __TEXT.__constg_swiftt: 0x72c
   __TEXT.__swift5_reflstr: 0x22f
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__constg_swiftt: 0x670
   __TEXT.__swift5_fieldmd: 0x254
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__oslogstring: 0x49d

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6f0
-  __TEXT.__eh_frame: 0x5f8
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x758
+  __TEXT.__unwind_info: 0x748
+  __TEXT.__eh_frame: 0x6f4
+  __DATA_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__auth_ptr: 0x3b0
+  __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA.__objc_const: 0x4e8
   __DATA.__objc_selrefs: 0x1a0
-  __DATA.__objc_data: 0x3d8
-  __DATA.__data: 0x9d8
-  __DATA.__bss: 0x890
+  __DATA.__objc_data: 0x3f8
+  __DATA.__data: 0x978
+  __DATA.__bss: 0x8b0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/Translation.framework/Translation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/TranslationAPISupport.framework/TranslationAPISupport
   - /System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: EEE60692-AE94-3181-965B-363D3F03C37A
-  Functions: 553
-  Symbols:   169
-  CStrings:  136
+  UUID: 4A7C68D5-59AC-397E-AE13-11E37C329EA7
+  Functions: 560
+  Symbols:   180
+  CStrings:  149
 
Symbols:
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$__LTPreflightConfiguration
+ __LTRecommendedMaxLowConfidenceLocalesToSuggest
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __availability_version_check
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _rewind
+ _sscanf
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_bridgeObjectRelease_n
- _swift_release_n
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "ProductVersion"
+ "kCFAllocatorNull"
+ "r"
- "Contradictory frame constraints specified."

```
