## ULPNHeuristicsClientFramework

> `/System/Library/PrivateFrameworks/ULPNHeuristicsClientFramework.framework/ULPNHeuristicsClientFramework`

```diff

-106.0.0.0.0
-  __TEXT.__text: 0xde9c
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__const: 0xbe8
-  __TEXT.__cstring: 0x53d
-  __TEXT.__constg_swiftt: 0x604
-  __TEXT.__swift5_typeref: 0x387
-  __TEXT.__swift5_reflstr: 0x494
-  __TEXT.__swift5_fieldmd: 0x494
-  __TEXT.__oslogstring: 0x1f4
+119.0.0.0.0
+  __TEXT.__text: 0x10b04
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__const: 0xc68
+  __TEXT.__cstring: 0x78d
+  __TEXT.__constg_swiftt: 0x6bc
+  __TEXT.__swift5_typeref: 0x3d9
+  __TEXT.__swift5_reflstr: 0x574
+  __TEXT.__swift5_fieldmd: 0x4f8
+  __TEXT.__oslogstring: 0x5b4
   __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_types: 0x58
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2f8
   __TEXT.__eh_frame: 0x160
-  __TEXT.__objc_methname: 0xc
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_methname: 0xd2
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x38
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0x7d8
-  __AUTH_CONST.__objc_const: 0x400
-  __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x6d0
-  __DATA.__data: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__objc_const: 0x530
+  __AUTH.__objc_data: 0x190
+  __AUTH.__data: 0x810
+  __DATA.__data: 0x240
   __DATA.__bss: 0xa00
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A0DD8953-47A7-3977-AA70-342B14AC11A6
-  Functions: 279
-  Symbols:   221
-  CStrings:  59
+  UUID: D0AB053F-FA2E-3704-A6CE-D546D029D625
+  Functions: 307
+  Symbols:   249
+  CStrings:  99
 
Symbols:
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ __Block_copy
+ __Block_release
+ __DATA__TtC29ULPNHeuristicsClientFramework25ULPNHeuristicsDiagnostics
+ __IVARS__TtC29ULPNHeuristicsClientFramework25ULPNHeuristicsDiagnostics
+ __METACLASS_DATA__TtC29ULPNHeuristicsClientFramework25ULPNHeuristicsDiagnostics
+ __NSConcreteStackBlock
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _kSymptomDiagnosticReplySuccess
+ _objc_allocWithZone
+ _objc_release
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x8
+ _objc_retain_x23
+ _symbolic So21SDRDiagnosticReporterC
+ _symbolic _____ 29ULPNHeuristicsClientFramework0A11DiagnosticsC
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
CStrings:
+ "Created signature dictionary with %ld entries"
+ "Diagnostic response indicated failure"
+ "Diagnostic response received: %s"
+ "Diagnostic response successful at %s"
+ "Diagnostic snapshot completed with no response data"
+ "Diagnostic snapshot request was successfully submitted"
+ "Diagnostics disabled, not reporting event: %s/%s"
+ "DiagnosticsCollectionEnabled"
+ "Failed to submit diagnostic snapshot request at %s"
+ "FailureThresholdExceeded"
+ "IPv4FragmentationFailure"
+ "IPv6FragmentationFailure"
+ "OffloadHeuristicsConsiderPathNotViable"
+ "Reporting diagnostic event: %s/%s"
+ "Reporting diagnostics for interface %s: %s due to %s"
+ "RxPktDropExceeded"
+ "RxQueueDelayExceeded"
+ "Skipping diagnostic report - last snapshot failure was %ld minutes ago (minimum retry interval: %ld minutes)"
+ "Skipping diagnostic report - last successful report was %ld minutes ago (minimum interval: %ld minutes)"
+ "TxPktDropExceeded"
+ "TxQueueDelayExceeded"
+ "Updated diagnostics enabled state from preferences: %{bool}d"
+ "_TtC29ULPNHeuristicsClientFramework25ULPNHeuristicsDiagnostics"
+ "diagnosticReporter"
+ "excessive failure events"
+ "failed to convert signature dictionary to Swift dictionary"
+ "failed to create signature dictionary"
+ "init"
+ "isDiagnosticsEnabled"
+ "lastSnapshotFailureTimestamp"
+ "lastSuccessfulReportTimestamp"
+ "minimumSnapshotFailureRetryInterval"
+ "minimumSuccessReportInterval"
+ "processInfo"
+ "processName"
+ "setDateStyle:"
+ "setTimeStyle:"
+ "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:duration:event:payload:reply:"
+ "stringFromDate:"
+ "v16@?0@\"NSDictionary\"8"
- "OffloadHeuristicsConsierPathNotViable"

```
