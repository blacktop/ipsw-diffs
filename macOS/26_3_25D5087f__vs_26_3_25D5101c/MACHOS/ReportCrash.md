## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

-927.60.6.0.0
-  __TEXT.__text: 0x331cc
-  __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_stubs: 0x3620
-  __TEXT.__objc_methlist: 0xe68
-  __TEXT.__cstring: 0x5651
+927.80.2.0.0
+  __TEXT.__text: 0x338e4
+  __TEXT.__auth_stubs: 0x1950
+  __TEXT.__objc_stubs: 0x3680
+  __TEXT.__objc_methlist: 0xe90
+  __TEXT.__cstring: 0x5791
   __TEXT.__const: 0x568
-  __TEXT.__objc_methname: 0x3d0c
+  __TEXT.__objc_methname: 0x3dba
   __TEXT.__oslogstring: 0x1d72
   __TEXT.__objc_classname: 0x116
-  __TEXT.__objc_methtype: 0x72d
+  __TEXT.__objc_methtype: 0x78b
   __TEXT.__gcc_except_tab: 0x488
   __TEXT.__dlopen_cstrs: 0xa5
   __TEXT.__swift5_typeref: 0x284

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x830
+  __TEXT.__unwind_info: 0x848
   __TEXT.__eh_frame: 0x2d8
-  __DATA_CONST.__auth_got: 0xc60
+  __DATA_CONST.__auth_got: 0xcb8
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__auth_ptr: 0x158
+  __DATA_CONST.__auth_ptr: 0x1a0
   __DATA_CONST.__const: 0x10b8
-  __DATA_CONST.__cfstring: 0x7600
+  __DATA_CONST.__cfstring: 0x76a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x398
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x210
-  __DATA.__objc_const: 0x2658
-  __DATA.__objc_selrefs: 0x1048
-  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_const: 0x2678
+  __DATA.__objc_selrefs: 0x1060
+  __DATA.__objc_ivar: 0x298
   __DATA.__objc_data: 0x8d8
   __DATA.__data: 0x610
   __DATA.__crash_info: 0x148

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CDC4596-BD39-3ABF-ADB0-CAEED3B0AD4C
-  Functions: 721
-  Symbols:   602
-  CStrings:  3070
+  UUID: 894AD2F6-DCB2-3683-8458-8AF7CBECF964
+  Functions: 725
+  Symbols:   613
+  CStrings:  3087
 
Symbols:
+ _MARCrashReportBacktraceGetBacktraceBuffer
+ _MARCrashReportBacktraceGetNumFrames
+ _MARCrashReportCreate
+ _MARCrashReportGetAllocationBacktrace
+ _MARCrashReportGetAllocationSizeBytes
+ _MARCrashReportGetConfidence
+ _MARCrashReportGetDeallocationBacktrace
+ _MARCrashReportGetErrorType
+ _MARCrashReportGetFaultAddress
+ _MARCrashReportRelease
+ _MARReportCrashExtractResults
CStrings:
+ "@48@0:8^{OpaquePASMARCrashReportBacktrace=}16{_CSTypeRef=QQ}24@40"
+ "B40@0:8{_CSTypeRef=QQ}16@32"
+ "Could not find a matching bmalloc MAR record."
+ "Could not locate MARCrashReport getters in JavaScriptCore."
+ "Could not locate MARCrashReportCreate or MARCrashReportRelease in JavaScriptCore."
+ "Could not locate MARReportCrashExtractResults in JavaScriptCore."
+ "_bmallocMARReport"
+ "_extractMARReportUsingSymbolicator:usingCatalog:"
+ "_extractMARStackTraceInfo:withSymbolicator:usingCatalog:"
+ "_isMemoryRegionAssociatedWithWebKit:usingCatalog:"
+ "bmallocMARReport"
+ "pas_mar_registry_for_crash_reporter_enumeration"

```
