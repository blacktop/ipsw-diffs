## EchoRelay

> `/System/Library/PrivateFrameworks/EchoRelay.framework/EchoRelay`

```diff

-54.0.1.0.0
-  __TEXT.__text: 0xa0bc
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__const: 0x754
-  __TEXT.__cstring: 0x262
-  __TEXT.__swift5_typeref: 0x255
-  __TEXT.__swift5_fieldmd: 0x294
-  __TEXT.__constg_swiftt: 0x1f0
-  __TEXT.__swift5_reflstr: 0x260
+57.0.0.0.0
+  __TEXT.__text: 0x1284c
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__const: 0xbc4
+  __TEXT.__swift5_typeref: 0x310
+  __TEXT.__constg_swiftt: 0x398
+  __TEXT.__swift5_reflstr: 0x325
+  __TEXT.__swift5_fieldmd: 0x3c8
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__cstring: 0x603
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_types: 0x24
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__oslogstring: 0x12c
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_capture: 0x74
-  __TEXT.__unwind_info: 0x480
-  __TEXT.__eh_frame: 0xa98
-  __TEXT.__objc_methname: 0xb4
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x90
+  __TEXT.__oslogstring: 0x2fc
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_capture: 0x88
+  __TEXT.__unwind_info: 0x730
+  __TEXT.__eh_frame: 0x7d0
+  __TEXT.__objc_methname: 0x14c
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x488
-  __AUTH_CONST.__const: 0x340
-  __AUTH.__data: 0x360
-  __DATA.__data: 0x1c0
-  __DATA.__common: 0x48
-  __DATA.__bss: 0x900
+  __DATA_CONST.__objc_selrefs: 0x80
+  __AUTH_CONST.__auth_got: 0x638
+  __AUTH_CONST.__const: 0x398
+  __AUTH_CONST.__objc_const: 0x120
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x638
+  __DATA.__data: 0x418
+  __DATA.__bss: 0xf00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
+  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary_AppleInternal.framework/IntelligencePlatformLibrary_AppleInternal
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtoDataExtractor.framework/ProtoDataExtractor

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C0484296-6C3A-3695-A1CC-7AC4D50FB5B1
-  Functions: 334
-  Symbols:   103
-  CStrings:  44
+  UUID: CA4F80E3-3481-3C3B-92AD-D967EF0ECEDF
+  Functions: 655
+  Symbols:   126
+  CStrings:  94
 
Symbols:
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __objc_empty_cache
+ __swiftEmptyDictionarySingleton
+ _free
+ _malloc
+ _objc_release
+ _objc_release_x22
+ _objc_release_x26
+ _objc_retain_x8
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_checkMetadataState
+ _swift_coroFrameAlloc
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_endAccess
+ _swift_getGenericMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStackObject
+ _swift_lookUpClassMethod
+ _swift_stdlib_isStackAllocationSafe
+ _swift_updateClassMetadata2
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "%s"
+ "Current date: %s, expiration date: %s"
+ "Default PET3 extension approved streams: %s"
+ "Default PET3 extension provisonal streams: %s"
+ "Device.Audio.AdaptiveVolume"
+ "EchoRelay/PETUserDefaults.swift"
+ "Failed to create UserDefaults for PET3"
+ "Failed to serialize AMLPET3DeviceUploadWrapper: %@"
+ "Fatal error"
+ "No stream election status found"
+ "This platform does not have biome internal stream"
+ "Uploading is not enabled"
+ "_TtC9EchoRelay19PET3ExtensionConfig"
+ "_TtCV9EchoRelay26AMLPET3DeviceUploadWrapperP33_A7E7AA7FD5D28165875BE742AC0727A413_StorageClass"
+ "_biomeEventPayload"
+ "_metadata"
+ "approvedStreams"
+ "biomeEventTs"
+ "boolForKey:"
+ "checking stream eligibility: %s"
+ "com.apple.dpg.proactive"
+ "com.apple.pet3.BiomeStreamRelayLighthouse"
+ "com.apple.pet3.common.PET3BiomeStream"
+ "com.apple.pet3.common.PET3ExtensionConfig"
+ "com.apple.pet3.event.DeviceAdaptiveVolumeEvent"
+ "com.apple.proactive"
+ "dataWithJSONObject:options:error:"
+ "dateFromString:"
+ "defaults"
+ "dictionaryForKey:"
+ "dpgSchemaName"
+ "fbfBundleDBPrefix"
+ "fbfBundleIdPrefix"
+ "init"
+ "isEnabledByDefault"
+ "logger"
+ "maxCount"
+ "objectForKey:"
+ "perStreamElectionStatus"
+ "provisionalStreams"
+ "removeObjectForKey:"
+ "setDateFormat:"
+ "setObject:forKey:"
+ "startDate"
+ "stream: %s, isAllowed: %{bool}d, isEligible: %{bool}d"
+ "timeToLiveDays"
+ "timestamp %f"
+ "uploadingEnabled"
+ "uploadingEnabled set: %{bool}d, perStreamElectionStatus set: %{bool}d"
+ "userDefaultsDomain"

```
