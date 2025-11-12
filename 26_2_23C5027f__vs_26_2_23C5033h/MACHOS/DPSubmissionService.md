## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-684.60.1.0.5
-  __TEXT.__text: 0x4e7f8
+684.60.3.0.5
+  __TEXT.__text: 0x4dfe0
   __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0x1344
+  __TEXT.__objc_stubs: 0x3000
+  __TEXT.__objc_methlist: 0x1354
   __TEXT.__const: 0x41b0
-  __TEXT.__cstring: 0x2b80
-  __TEXT.__objc_methname: 0x3c1f
+  __TEXT.__cstring: 0x2a00
+  __TEXT.__objc_methname: 0x3c74
   __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methtype: 0xa1a
+  __TEXT.__objc_methtype: 0xa2b
   __TEXT.__oslogstring: 0x127e
   __TEXT.__gcc_except_tab: 0x23c
   __TEXT.__swift5_typeref: 0x8b8

   __TEXT.__swift5_assocty: 0x5e8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1c78
+  __TEXT.__unwind_info: 0x1c80
   __TEXT.__eh_frame: 0x41a8
   __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__got: 0x520
   __DATA_CONST.__auth_ptr: 0x2a8
   __DATA_CONST.__const: 0x2f70
-  __DATA_CONST.__cfstring: 0x1720
+  __DATA_CONST.__cfstring: 0x15e0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_intobj: 0x138
+  __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x2500
-  __DATA.__objc_selrefs: 0xe48
+  __DATA.__objc_selrefs: 0xe50
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0xe78
   __DATA.__data: 0x2490

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E3A5144-CB47-3E28-B6B2-F306DFC4F5B6
-  Functions: 2305
-  Symbols:   359
-  CStrings:  1326
+  UUID: CC27EF1D-BCD4-331F-84FC-8BF806EC7E53
+  Functions: 2306
+  Symbols:   353
+  CStrings:  1308
 
Symbols:
- __DPCoreAnalyticsEvent_PhaseCount
- __DPCoreAnalyticsField_Counts
- __DPCoreAnalyticsField_Phase
- __DPCoreAnalyticsField_Status
- __DPCoreAnalyticsField_TaskName
- ___kCFBooleanTrue
CStrings:
+ "Failed to upload DAP report to %@, error: %@"
+ "reportCoreAnalyticsExecutionStage:error:donation:"
+ "reportCoreAnalyticsExecutionStage:error:key:count:isTelemetryAllowed:"
+ "v40@0:8Q16@24@32"
- "Failed to create DAP payload encoder"
- "Failed to create payload encoder for Dedisco V2"
- "Failed to create payload for Dedisco V2"
- "Failed to download config file from server"
- "Failed to encrypt shares for Dedisco V1"
- "Failed to extract fields from config file"
- "Failed to obtain signature for payload"
- "Failed to serialize otherParams for Dedisco V1"
- "Failed to serialize payload"
- "Failed to upload\tDAP report to %@, error: %@"
- "Payload size exceeds 1 MB"
- "reportMetricsForEvent:withMetrics:"

```
