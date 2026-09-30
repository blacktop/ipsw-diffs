## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

 43.0.0.0.0
-  __TEXT.__text: 0x6530
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x860
+  __TEXT.__text: 0x7b70
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_stubs: 0x8c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x5d0
-  __TEXT.__gcc_except_tab: 0x834
-  __TEXT.__const: 0x162
-  __TEXT.__cstring: 0xa37
-  __TEXT.__objc_methname: 0x11e8
-  __TEXT.__oslogstring: 0x68c
+  __TEXT.__objc_methlist: 0x618
+  __TEXT.__gcc_except_tab: 0x8ac
+  __TEXT.__const: 0x1d0
+  __TEXT.__cstring: 0xc07
+  __TEXT.__objc_methname: 0x1222
+  __TEXT.__oslogstring: 0x855
   __TEXT.__objc_classname: 0x92
   __TEXT.__objc_methtype: 0x55e
-  __TEXT.__swift5_typeref: 0x66
-  __TEXT.__constg_swiftt: 0xe0
-  __TEXT.__swift5_fieldmd: 0x64
-  __TEXT.__swift5_reflstr: 0x13
+  __TEXT.__swift5_typeref: 0xb2
+  __TEXT.__constg_swiftt: 0x18c
+  __TEXT.__swift5_reflstr: 0x60
+  __TEXT.__swift5_fieldmd: 0x98
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x288
+  __TEXT.__unwind_info: 0x310
   __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x1000
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_ptr: 0x88
+  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__cfstring: 0x1040
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xf18
-  __DATA.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA.__objc_const: 0xfc8
+  __DATA.__objc_selrefs: 0x480
   __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x2b8
-  __DATA.__bss: 0x1b0
+  __DATA.__objc_data: 0x1b0
+  __DATA.__data: 0x308
+  __DATA.__bss: 0x1c0
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/ExclaveFDRDecode.framework/ExclaveFDRDecode
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 169
-  Symbols:   131
-  CStrings:  507
+  Functions: 203
+  Symbols:   158
+  CStrings:  538
 
Symbols:
+ _swift_endAccess
+ _swift_getSingletonMetadata
+ _objc_allocWithZone
+ _swift_deallocPartialClassInstance
+ _OBJC_CLASS_$__TtC22AppleProxServiceFilter22AppleProxExclaveClient
+ _objc_retain_x25
+ _swift_arrayDestroy
+ _swift_updateClassMetadata2
+ _swift_beginAccess
+ _swift_errorRelease
+ _OBJC_METACLASS_$__TtC22AppleProxServiceFilter22AppleProxExclaveClient
+ _MGGetBoolAnswer
+ __swiftEmptyArrayStorage
+ _AMFDRSealingMapCopyLocalMultiCombinedDataContextDestroy
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass
+ _swift_isaMask
+ __swift_stdlib_reportUnimplementedInitializer
+ _swift_getForeignTypeMetadata
+ _swift_slowDealloc
+ _malloc_size
+ _swift_errorRetain
+ _AMFDRSealingMapCopyLocalMultiCombinedDataBeginWithOptions
+ _objc_alloc
+ _swift_slowAlloc
+ _AMFDRSealingMapCopyLocalMultiCombinedDataEnd
+ _swift_dynamicCast
+ __swift_stdlib_bridgeErrorToNSError
CStrings:
+ "com.apple.backboardd.ExclaveFDRDecodeRawDataStoreKitService"
+ "Swift/Integers.swift"
+ "Calibration load in AppleProxExclave: %!d(MISSING)"
+ "@20@0:8B16"
+ "Not enough bits to represent the passed value"
+ "Error in AddSubCCForClass:%!@(MISSING)"
+ "_TtC22AppleProxServiceFilter22AppleProxExclaveClient"
+ "com.apple.backboardd.AppleProxExclaveService"
+ "proxExclaveService"
+ "Cannot find FDR data for classes %!@(MISSING):%!@(MISSING)"
+ "Conclave.service failed with tb_error_t = %!u(MISSING)"
+ "ExclaveCapability"
+ "Successfully queried FDR data for classes %!@(MISSING):%!@(MISSING)"
+ "Conclave.service failed: %!@(MISSING)"
+ "Error in BeginWithOptions:%!@(MISSING)"
+ "AppleProxServiceFilter.AppleProxExclaveClient"
+ "loadCalibration:"
+ "fdrDecodeRawDataStoreService"
+ "Calibration load failed: %!@(MISSING)"
+ "asid"
+ "Created Tightbeam clients"
+ "loadCalibrationExclave"
+ "initWithConclave:"
+ "init()"
+ "Sending raw data to FDR: %!u(MISSING) bytes"
+ "Calling AppleProxExclave loadCalibration"
+ "log"
+ "Starting conclave..."

```
