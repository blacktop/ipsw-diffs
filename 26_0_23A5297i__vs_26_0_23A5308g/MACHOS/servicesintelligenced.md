## servicesintelligenced

> `/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced`

```diff

-1.23.0.0.0
-  __TEXT.__text: 0x2a48
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__const: 0xca
-  __TEXT.__cstring: 0x375
-  __TEXT.__swift5_typeref: 0x6a
+1.25.0.0.0
+  __TEXT.__text: 0x48cc
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__const: 0xe2
+  __TEXT.__cstring: 0x40f
+  __TEXT.__swift5_typeref: 0xbc
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x98
-  __TEXT.__objc_methname: 0x59
+  __TEXT.__objc_methname: 0xb2
+  __TEXT.__oslogstring: 0x45
   __TEXT.__swift5_types: 0x4
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__eh_frame: 0x1b0
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x2e8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__eh_frame: 0x300
+  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_ptr: 0x48
+  __DATA_CONST.__const: 0x338
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x110
+  __DATA.__objc_selrefs: 0x38
+  __DATA.__data: 0x168
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/ServicesIntelligence.framework/ServicesIntelligence
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9F565229-0A11-3AE1-B613-CCEA09BFD093
-  Functions: 71
-  Symbols:   117
-  CStrings:  20
+  UUID: AC615391-BCFE-3E45-AA09-3950F8A21B14
+  Functions: 100
+  Symbols:   175
+  CStrings:  30
 
Symbols:
+ _$s20ServicesIntelligence12MetricsTopicO8platformyA2CmFWC
+ _$s20ServicesIntelligence12MetricsTopicO8rawValueSSvg
+ _$s20ServicesIntelligence12MetricsTopicOMa
+ _$s20ServicesIntelligence14RequestContextVMa
+ _$s20ServicesIntelligence14RequestContextVMn
+ _$s20ServicesIntelligence20TreatmentStoreClientC17refreshTreatments14requestContextSbAA07RequestI0VSg_tYaKFTjTu
+ _$s20ServicesIntelligence26ConfigurationServiceClientC07refreshC014requestContextSbAA07RequestH0VSg_tYaKFTjTu
+ _$s20ServicesIntelligence7ProcessO18amsMetricsProducerSayACGvgZ
+ _$s20ServicesIntelligence7ProcessO8bundleIDSSvg
+ _$s20ServicesIntelligence7ProcessOMa
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSSN
+ _$sScC12continuation8functionScCyxq_GSccyxq_G_SStcfC
+ _$sScC6resume8throwingyq_n_tF
+ _$sScC6resume9returningyxn_tF
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsVN
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss20__StaticArrayStorageCN
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss5ErrorMp
+ _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
+ _$ss5ErrorWS
+ _$ss5UInt8VMn
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSMetrics
+ _OBJC_CLASS_$_NSNumber
+ __os_log_impl
+ __swiftImmortalRefCount
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_release_x19
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x24
+ _os_log_type_enabled
+ _swift_allocBox
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_willThrow
- _$s20ServicesIntelligence20TreatmentStoreClientC17refreshTreatmentsSbyYaKFTjTu
- _$s20ServicesIntelligence26ConfigurationServiceClientC07refreshC0SbyYaKFTjTu
CStrings:
+ "Error during flush metrics: %s"
+ "Flushed %@ events from container: %s"
+ "ServicesIntelligenceCore"
+ "_createCheckedThrowingContinuation(_:)"
+ "bagForProfile:profileVersion:"
+ "com.apple.ServicesIntelligence"
+ "flushTopic:"
+ "initWithContainerID:bag:"
+ "resultWithCompletion:"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"

```
