## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3400.140.1.0.0
-  __TEXT.__text: 0x1f268
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0xf98
-  __TEXT.__cstring: 0x22c4
+3401.2.1.1.1
+  __TEXT.__text: 0x1f330
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_methlist: 0xfa8
+  __TEXT.__cstring: 0x22cf
   __TEXT.__swift5_typeref: 0x3f7
   __TEXT.__swift5_fieldmd: 0x350
   __TEXT.__const: 0x13c8

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_capture: 0x74
-  __TEXT.__oslogstring: 0x1a20
+  __TEXT.__oslogstring: 0x1a78
   __TEXT.__swift5_reflstr: 0x23f
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__unwind_info: 0xa40
   __TEXT.__eh_frame: 0x5a8
   __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methname: 0x2f2a
-  __TEXT.__objc_methtype: 0x6ab
-  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_methname: 0x2fa4
+  __TEXT.__objc_methtype: 0x6c3
+  __TEXT.__objc_stubs: 0x1f80
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb00
+  __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x7a0
   __AUTH_CONST.__auth_ptr: 0x1c0
   __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x1b88
+  __AUTH_CONST.__objc_const: 0x1be8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x150
-  __AUTH.__data: 0x3f8
-  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x4f8
   __DATA.__common: 0x110
-  __DATA.__bss: 0x2090
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x48
+  __DATA.__bss: 0x2088
+  __DATA_DIRTY.__objc_data: 0x470
+  __DATA_DIRTY.__data: 0x468
+  __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 930
-  Symbols:   675
-  CStrings:  973
+  Symbols:   686
+  CStrings:  979
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x12\x16"
+ "B32@0:8Q16Q24"
+ "Persist request for store (%!@(MISSING)) for %!l(MISSING)u bytes completed successfully."
+ "Persist request for store (%!@(MISSING)) for %!l(MISSING)u bytes failed with error %!@(MISSING)."
+ "SELECT batchId FROM batchStatus WHERE status=? ORDER BY rowid ASC LIMIT 1024;"
+ "SELECT s.batchId, s.timestampRefId, COALESCE(sum(length(r.payload)), 0), s.status, s.processedAttempts, s.dateCreated, s.dateUploaded, s.dateLastProcessed, COUNT(DISTINCT(r.rowId)), first_value(r.payload) OVER (ORDER BY r.rowId) FROM batchStatus s LEFT JOIN records r ON s.batchId = r.batchId WHERE s.batchId=? GROUP BY s.batchId;"
+ "TB,R,N"
+ "_deviceUnlockedSinceBoot"
+ "deviceUnlockedSinceBoot"
+ "persist:preferredBatchSize:"
+ "tryRolloverBatchIfNecessary:preferredBatchSize:"
+ "v48@0:8@16@24Q32@?40"
+ "write:store:preferredBatchSize:completion:"
- "\x02\x16"
- "B24@0:8Q16"
- "Persist request for store (%!@(MISSING)) for %!l(MISSING)u bytes %!@(MISSING)"
- "SELECT batchId FROM batchStatus WHERE status=? ORDER BY rowid ASC;"
- "SELECT s.batchId, s.timestampRefId, COALESCE(sum(length(r.payload)), 0), s.status, s.processedAttempts, s.dateCreated, s.dateUploaded, s.dateLastProcessed, COUNT(DISTINCT(r.rowId)), first_value(r.payload) OVER (ORDER BY r.rowId) FROM batchStatus s LEFT JOIN records r ON s.batchId = r.batchId WHERE s.batchId=? group by s.batchId;"
- "tryRolloverBatchIfNecessary:"
- "write:store:completion:"

```
