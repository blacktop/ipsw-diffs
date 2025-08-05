## CoreSpeechDataAnalytics

> `/System/Library/PrivateFrameworks/CoreSpeechDataAnalytics.framework/CoreSpeechDataAnalytics`

```diff

-3500.115.2.0.0
-  __TEXT.__text: 0x4a8c8
-  __TEXT.__auth_stubs: 0x10c0
+3500.122.2.0.0
+  __TEXT.__text: 0x4c0f0
+  __TEXT.__auth_stubs: 0x10e0
   __TEXT.__objc_methlist: 0xe8
   __TEXT.__const: 0x18e0
   __TEXT.__cstring: 0x5df5
-  __TEXT.__constg_swiftt: 0x2300
+  __TEXT.__constg_swiftt: 0x2308
   __TEXT.__swift5_typeref: 0x9e8
   __TEXT.__swift5_reflstr: 0x1217
   __TEXT.__swift5_fieldmd: 0xdb0
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__oslogstring: 0x2ee5
+  __TEXT.__oslogstring: 0x30c5
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_types: 0xe4
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0x7c
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_capture: 0x64
+  __TEXT.__swift5_capture: 0x54
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xac0
-  __TEXT.__eh_frame: 0x13cc
+  __TEXT.__unwind_info: 0xa98
+  __TEXT.__eh_frame: 0x13fc
   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methname: 0xe31
   __TEXT.__objc_methtype: 0x88
   __TEXT.__objc_stubs: 0xc0
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x8948
+  __DATA_CONST.__const: 0x8950
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0xcf0
+  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__const: 0xca0
   __AUTH_CONST.__cfstring: 0x4a20
   __AUTH_CONST.__objc_const: 0x29e0
-  __AUTH.__objc_data: 0x560
-  __AUTH.__data: 0x4030
+  __AUTH.__objc_data: 0x568
+  __AUTH.__data: 0x3fe0
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x4b8
+  __DATA.__data: 0x4b0
   __DATA.__bss: 0x1000
   __DATA.__common: 0x280
+  __DATA_DIRTY.__data: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C79A69C9-4F19-3468-BE0C-77A27923A2B3
-  Functions: 832
-  Symbols:   663
-  CStrings:  1779
+  UUID: 56F5386D-E48F-3374-BD32-AF35CDE12AC5
+  Functions: 825
+  Symbols:   661
+  CStrings:  1785
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_CoreSpeechDataAnalytics
+ _block_copy_helper.14
+ _block_copy_helper.17
+ _block_copy_helper.23
+ _block_copy_helper.29
+ _block_copy_helper.35
+ _block_copy_helper.38
+ _block_descriptor.16
+ _block_descriptor.19
+ _block_descriptor.25
+ _block_descriptor.31
+ _block_descriptor.37
+ _block_descriptor.40
+ _block_destroy_helper.15
+ _block_destroy_helper.18
+ _block_destroy_helper.24
+ _block_destroy_helper.30
+ _block_destroy_helper.36
+ _block_destroy_helper.39
+ _swift_getErrorValue
- _block_copy_helper.13
- _block_copy_helper.16
- _block_copy_helper.22
- _block_copy_helper.28
- _block_copy_helper.34
- _block_copy_helper.44
- _block_copy_helper.47
- _block_descriptor.15
- _block_descriptor.18
- _block_descriptor.24
- _block_descriptor.30
- _block_descriptor.36
- _block_descriptor.46
- _block_descriptor.49
- _block_destroy_helper.14
- _block_destroy_helper.17
- _block_destroy_helper.23
- _block_destroy_helper.29
- _block_destroy_helper.35
- _block_destroy_helper.45
- _block_destroy_helper.48
CStrings:
+ "#BaseSiriRequestSamplingActionEvent: all audio upload failed"
+ "#BaseSiriRequestSamplingActionEvent: maxUploadCount is 0, do not generate manifest event"
+ "#CollectionManager: data aggregation failed with error: %@"
+ "#CollectionManager: some audio upload failed, count: %ld for days: %s"
+ "#CollectionManager: upload audio failed with error: %@ for date: %s"
+ "#DataAnalyticsController: Manager %s checkAndEndDeviceSampling failed: %s"
+ "#DataAnalyticsController: Manager %s sampling cycle ended at start of processing"
- "#BaseSiriRequestSamplingActionEvent: pruning remote devices with error: %@"

```
