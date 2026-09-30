## com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

-3.6.2.0.0
-  __TEXT.__text: 0xa5e4
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__const: 0x572
-  __TEXT.__cstring: 0x155
-  __TEXT.__swift5_typeref: 0x1cb
-  __TEXT.__objc_methname: 0x9e
-  __TEXT.__swift5_reflstr: 0xec
-  __TEXT.__swift5_assocty: 0x60
+3.7.13.0.0
+  __TEXT.__text: 0x9cd4
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__const: 0x74a
+  __TEXT.__cstring: 0x187
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xac
-  __TEXT.__swift5_fieldmd: 0x128
-  __TEXT.__oslogstring: 0x1e3
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__eh_frame: 0x5e0
-  __DATA_CONST.__auth_got: 0x5e8
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x220
-  __DATA_CONST.__const: 0x400
+  __TEXT.__swift5_typeref: 0x1c3
+  __TEXT.__constg_swiftt: 0xec
+  __TEXT.__swift5_reflstr: 0x159
+  __TEXT.__swift5_fieldmd: 0x1cc
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__oslogstring: 0x1ae
+  __TEXT.__objc_methname: 0x5f
+  __TEXT.__swift5_proto: 0x70
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__unwind_info: 0x308
+  __TEXT.__eh_frame: 0x678
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_ptr: 0x1f0
+  __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x40
-  __DATA.__data: 0x210
-  __DATA.__bss: 0xa50
+  __DATA.__objc_selrefs: 0x20
+  __DATA.__data: 0x1a8
+  __DATA.__bss: 0xe80
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 87163D92-C9C0-378E-A60C-2EB933C62264
-  Functions: 180
-  Symbols:   101
-  CStrings:  38
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 0CDE0D05-D155-3CFA-8779-B1462AE04868
+  Functions: 194
+  Symbols:   84
+  CStrings:  33
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x8
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSObject
- __swiftEmptyDictionarySingleton
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _bzero
- _objc_release_x26
- _objc_release_x28
- _objc_release_x8
- _objc_retain
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_getObjCClassMetadata
- _swift_release_n
- _swift_retain_n
CStrings:
+ "(correlationId: "
+ "Donating message %f to queue: %{bool}d"
+ "Fetched message from queue: %s"
+ "com.apple.mlhost.SampleWorker.topic"
+ "consumeListEvents"
+ "produceListEvents"
+ "usePublisherService"
+ "useSubscriptionService"
- "Custom Machine: %s"
- "Generated CA Data: %s"
- "Generated analytics: %s"
- "dictionaryService available: %{bool}d"
- "firstEventTimestamp"
- "initWithDouble:"
- "initWithInteger:"
- "initWithLongLong:"
- "lastEventTimestamp"
- "latestEventTimestamp"
- "processCustomEvents"
- "processingLatency"
- "stringValue"

```
