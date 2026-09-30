## NewsScoringService

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x7de8
+5718.1.0.0.0
+  __TEXT.__text: 0x7910
   __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x764
+  __TEXT.__objc_methlist: 0x77c
   __TEXT.__const: 0x270
-  __TEXT.__objc_methname: 0x109a
+  __TEXT.__objc_methname: 0x109c
   __TEXT.__oslogstring: 0x172
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1a4
-  __TEXT.__swift5_typeref: 0x1f5
+  __TEXT.__constg_swiftt: 0x194
+  __TEXT.__swift5_typeref: 0x1d5
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
   __TEXT.__objc_classname: 0xe6
-  __TEXT.__objc_methtype: 0x811
-  __TEXT.__cstring: 0xa14
-  __TEXT.__swift5_reflstr: 0x15a
-  __TEXT.__swift5_fieldmd: 0x120
+  __TEXT.__objc_methtype: 0x85b
+  __TEXT.__cstring: 0x994
+  __TEXT.__swift5_reflstr: 0x13a
+  __TEXT.__swift5_fieldmd: 0x114
   __TEXT.__swift5_capture: 0x134
   __TEXT.__swift5_proto: 0x14
-  __TEXT.__unwind_info: 0x268
-  __TEXT.__eh_frame: 0xd8
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__eh_frame: 0xd0
   __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA.__objc_const: 0xdf8
-  __DATA.__objc_selrefs: 0x450
-  __DATA.__objc_data: 0x2b0
-  __DATA.__data: 0x760
+  __DATA.__objc_const: 0xdd8
+  __DATA.__objc_selrefs: 0x460
+  __DATA.__objc_data: 0x2a0
+  __DATA.__data: 0x750
   __DATA.__common: 0x18
   __DATA.__bss: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/ComputationalGraph.framework/ComputationalGraph
   - /System/Library/PrivateFrameworks/NewsCore.framework/NewsCore
   - /System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon
   - /System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed
   - /System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization
   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport
-  - /System/Library/PrivateFrameworks/Tabi.framework/Tabi
   - /System/Library/PrivateFrameworks/TeaDB.framework/TeaDB
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftGameplayKit.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftSpriteKit.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
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
-  UUID: B3B00389-A83A-3E9D-906F-C4838CE44595
-  Functions: 175
-  Symbols:   133
+  UUID: 08609318-5B5D-39B5-897B-8D8965ACD31F
+  Functions: 176
+  Symbols:   127
   CStrings:  325
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x9
- _OBJC_CLASS_$_FCUserEventHistorySession
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x27
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "@\"NSArray\"24@0:8@\"FCUserEventHistoryPruningPolicy\"16"
+ "@24@0:8@16"
+ "computeServiceScoringService"
+ "emptyWithSessionsOnDiskSize:"
+ "lastModifiedDate"
+ "pruneWithPolicy:"
+ "readBaseDirectoryWithAccessor:"
+ "v24@0:8@?<v@?@\"NSURL\">16"
- "@\"NSURL\"16@0:8"
- "NewsScoringService.NoopUserEventHistoryStorage"
- "T@\"NSURL\",N,R"
- "T@\"NSURL\",R,N"
- "baseDirectoryURL"
- "emptyWithSessionsOnDiskSize:personalizationAnalyticsEnabled:"
- "tabiScoringService"
- "user-event-history"

```
