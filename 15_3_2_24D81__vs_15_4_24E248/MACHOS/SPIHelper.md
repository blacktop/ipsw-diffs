## SPIHelper

> `/System/Library/PrivateFrameworks/CloudSharing.framework/Versions/A/XPCServices/SPIHelper.xpc/Contents/MacOS/SPIHelper`

```diff

-188.1.3.2.0
-  __TEXT.__text: 0x9fcfc
-  __TEXT.__auth_stubs: 0x1450
+188.4.2.0.0
+  __TEXT.__text: 0x98928
+  __TEXT.__auth_stubs: 0x1430
   __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x1ec
-  __TEXT.__const: 0x3da8
-  __TEXT.__objc_methname: 0x12a1
+  __TEXT.__objc_methlist: 0x3fc
+  __TEXT.__const: 0x3a70
+  __TEXT.__objc_methname: 0x12b6
   __TEXT.__objc_classname: 0x92
   __TEXT.__objc_methtype: 0x169
-  __TEXT.__cstring: 0x4104
+  __TEXT.__cstring: 0x3f30
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xc94
-  __TEXT.__swift5_typeref: 0x2061
-  __TEXT.__swift5_fieldmd: 0xf90
+  __TEXT.__constg_swiftt: 0xcb8
+  __TEXT.__swift5_typeref: 0x209f
+  __TEXT.__swift5_fieldmd: 0xfc4
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x119a
+  __TEXT.__swift5_reflstr: 0x11e5
   __TEXT.__swift5_assocty: 0x378
-  __TEXT.__swift5_proto: 0x194
-  __TEXT.__swift5_types: 0xcc
-  __TEXT.__oslogstring: 0x264c
+  __TEXT.__oslogstring: 0x26ec
+  __TEXT.__swift5_proto: 0x1a0
+  __TEXT.__swift5_types: 0xd0
+  __TEXT.__swift_as_entry: 0x160
+  __TEXT.__swift_as_ret: 0x224
   __TEXT.__swift5_capture: 0xebc
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2330
-  __TEXT.__eh_frame: 0x63d8
-  __DATA_CONST.__auth_got: 0xa30
+  __TEXT.__unwind_info: 0x2250
+  __TEXT.__eh_frame: 0x6588
+  __DATA_CONST.__auth_got: 0xa20
   __DATA_CONST.__got: 0x508
-  __DATA_CONST.__auth_ptr: 0x858
-  __DATA_CONST.__const: 0x2db8
+  __DATA_CONST.__auth_ptr: 0x860
+  __DATA_CONST.__const: 0x3010
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x1680
-  __DATA.__objc_selrefs: 0x4f0
+  __DATA.__objc_const: 0x1450
+  __DATA.__objc_selrefs: 0x588
   __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x5e8
-  __DATA.__data: 0x2040
+  __DATA.__objc_data: 0x448
+  __DATA.__data: 0x2020
   __DATA.__common: 0xa0
-  __DATA.__bss: 0x36a0
+  __DATA.__bss: 0x3820
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs
   - /System/Library/PrivateFrameworks/CloudSharing.framework/Versions/A/CloudSharing
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/ShareKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 91DD0F85-B8A7-3E3E-95D5-73CE5BA06252
-  Functions: 2126
-  Symbols:   238
-  CStrings:  740
+  UUID: 526021A0-15D3-3022-A7C2-A8D98FEE1F9F
+  Functions: 2118
+  Symbols:   239
+  CStrings:  736
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "%s: SPI Entitlement Protection is disabled. Allowing connection regardless."
+ "CloudSharing SPI: Attempted connection without entitlement. Denied."
+ "CloudSharingUI"
+ "Gelato"
+ "SPIEntitlementProtection"
+ "ShareAccessRequests"
+ "com.apple.private.CloudSharing.SPI"
+ "listener(_:shouldAcceptNewConnection:)"
+ "valueForEntitlement:"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
