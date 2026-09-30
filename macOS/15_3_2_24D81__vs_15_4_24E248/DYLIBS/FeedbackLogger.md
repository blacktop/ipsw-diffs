## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/Versions/A/FeedbackLogger`

```diff

-3403.3.3.0.0
-  __TEXT.__text: 0x1da24
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0xfa8
-  __TEXT.__cstring: 0x1f95
+3404.77.2.14.1
+  __TEXT.__text: 0x1e548
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_methlist: 0x1184
+  __TEXT.__const: 0x1368
+  __TEXT.__cstring: 0x1fe4
   __TEXT.__swift5_typeref: 0x2e1
   __TEXT.__swift5_fieldmd: 0x350
-  __TEXT.__const: 0x1368
   __TEXT.__constg_swiftt: 0x20c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x108

   __TEXT.__swift5_reflstr: 0x23f
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__oslogstring: 0x1842
+  __TEXT.__oslogstring: 0x1865
   __TEXT.__unwind_info: 0x9d0
-  __TEXT.__eh_frame: 0x5a8
+  __TEXT.__eh_frame: 0x578
   __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methname: 0x2eed
-  __TEXT.__objc_methtype: 0x6c3
-  __TEXT.__objc_stubs: 0x1f80
+  __TEXT.__objc_methname: 0x2fed
+  __TEXT.__objc_methtype: 0x6d4
+  __TEXT.__objc_stubs: 0x2080
   __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae8
+  __DATA_CONST.__objc_selrefs: 0xbc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__const: 0x7f0
-  __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x1be8
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x18c8
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x448
   __AUTH.__data: 0x448
   __DATA.__objc_ivar: 0x130
-  __DATA.__data: 0x4a0
-  __DATA.__common: 0x100
+  __DATA.__data: 0x488
   __DATA.__bss: 0x20d0
+  __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 16922D29-38F6-3B6C-8070-543217D66C47
-  Functions: 900
-  Symbols:   1207
-  CStrings:  1008
+  UUID: BE9B97E3-C21A-31AA-862F-92BC4F8B8EF9
+  Functions: 901
+  Symbols:   1205
+  CStrings:  1027
 
Symbols:
+ -[BatchMetadata batchEventCount]
+ -[BatchMetadata setBatchEventCount:]
+ -[FLLogger reportCADroppedBeforePersistPayloadFromBundleID:category:size:]
+ -[FLLogger reportCAIncomingPayloadFromBundleID:category:size:]
+ -[FLSQLitePersistence canAddRecords]
+ -[FLSQLitePersistence(SchemaManager) recreateDatabase]
+ -[FeedbackLoggerFBFClient dealloc]
+ GCC_except_table184
+ GCC_except_table252
+ GCC_except_table277
+ GCC_except_table349
+ OBJC_IVAR_$_BatchMetadata._batchEventCount
+ _OUTLINED_FUNCTION_25
+ __Block_byref_object_copy_.402
+ __Block_byref_object_dispose_.403
+ __block_literal_global.535
+ __block_literal_global.644
+ __block_literal_global.823
+ _flAnnotatedLogForObject
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$canAddRecords
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$recreateDatabase
+ _objc_msgSend$reportCADroppedBeforePersistPayloadFromBundleID:category:size:
+ _objc_msgSend$reportCAIncomingPayloadFromBundleID:category:size:
+ _objc_msgSend$setBatchEventCount:
+ _objc_msgSend$stringByDeletingLastPathComponent
- -[BatchMetadata eventCount]
- -[BatchMetadata setEventCount:]
- GCC_except_table182
- GCC_except_table248
- GCC_except_table273
- GCC_except_table344
- OBJC_IVAR_$_BatchMetadata._eventCount
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_48
- __Block_byref_object_copy_.415
- __Block_byref_object_dispose_.416
- __block_literal_global.544
- __block_literal_global.646
- __block_literal_global.826
- __os_log_debug_impl
- _objc_msgSend$setEventCount:
CStrings:
+ "%s[%@]"
+ "SQLite set busy timeout failed: %d"
+ "TQ,N,V_batchEventCount"
+ "_batchEventCount"
+ "batchEventCount"
+ "cStringUsingEncoding:"
+ "canAddRecords"
+ "com.apple.siri.metrics.MetricsExtension"
+ "dropped_before_persist"
+ "init()"
+ "isEqualToString:"
+ "lastPathComponent"
+ "received"
+ "recreateDatabase"
+ "reportCADroppedBeforePersistPayloadFromBundleID:category:size:"
+ "reportCAIncomingPayloadFromBundleID:category:size:"
+ "setBatchEventCount:"
+ "stringByDeletingLastPathComponent"
+ "v40@0:8@16@24Q32"
- "TQ,N,V_eventCount"
- "_eventCount"
- "eventCount"
- "setEventCount:"

```
