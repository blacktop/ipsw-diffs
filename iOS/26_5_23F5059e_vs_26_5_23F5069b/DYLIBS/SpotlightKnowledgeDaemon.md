## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2418.5.7.0.0
-  __TEXT.__text: 0x29aaa4
-  __TEXT.__auth_stubs: 0x50c0
-  __TEXT.__objc_methlist: 0x9940
-  __TEXT.__const: 0xce50
+2418.5.9.101.0
+  __TEXT.__text: 0x29c680
+  __TEXT.__auth_stubs: 0x50e0
+  __TEXT.__objc_methlist: 0x99c0
+  __TEXT.__const: 0xd080
   __TEXT.__oslogstring: 0xd014
-  __TEXT.__gcc_except_tab: 0x5f40
-  __TEXT.__cstring: 0xb70e
+  __TEXT.__gcc_except_tab: 0x5f54
+  __TEXT.__cstring: 0xb77e
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0x8ef2
-  __TEXT.__swift5_fieldmd: 0x47f4
-  __TEXT.__constg_swiftt: 0x5378
+  __TEXT.__swift5_typeref: 0x8f44
+  __TEXT.__swift5_fieldmd: 0x4844
+  __TEXT.__constg_swiftt: 0x53e8
   __TEXT.__swift5_capture: 0x1a68
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x4034
+  __TEXT.__swift5_reflstr: 0x4054
   __TEXT.__swift5_assocty: 0xe18
   __TEXT.__swift5_protos: 0x158
   __TEXT.__swift5_proto: 0x918
-  __TEXT.__swift5_types: 0x4f0
+  __TEXT.__swift5_types: 0x4f8
   __TEXT.__swift_as_entry: 0xe8
   __TEXT.__swift_as_ret: 0x124
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x7d10
+  __TEXT.__unwind_info: 0x7d78
   __TEXT.__eh_frame: 0x79a0
-  __TEXT.__objc_classname: 0x1fbf
-  __TEXT.__objc_methname: 0x168c7
-  __TEXT.__objc_methtype: 0x2d5a
-  __TEXT.__objc_stubs: 0x10d60
-  __DATA_CONST.__got: 0x1a20
-  __DATA_CONST.__const: 0x3bf0
-  __DATA_CONST.__objc_classlist: 0x878
+  __TEXT.__objc_classname: 0x200f
+  __TEXT.__objc_methname: 0x169e7
+  __TEXT.__objc_methtype: 0x2dba
+  __TEXT.__objc_stubs: 0x10e40
+  __DATA_CONST.__got: 0x1a38
+  __DATA_CONST.__const: 0x3c08
+  __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ed8
+  __DATA_CONST.__objc_selrefs: 0x4f10
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x4f0
-  __DATA_CONST.__objc_arraydata: 0x828
-  __AUTH_CONST.__auth_got: 0x2878
-  __AUTH_CONST.__const: 0xdc88
-  __AUTH_CONST.__cfstring: 0x99c0
-  __AUTH_CONST.__objc_const: 0x15ad8
-  __AUTH_CONST.__objc_intobj: 0x990
+  __DATA_CONST.__objc_superrefs: 0x4f8
+  __DATA_CONST.__objc_arraydata: 0x8b8
+  __AUTH_CONST.__auth_got: 0x2888
+  __AUTH_CONST.__const: 0xdca8
+  __AUTH_CONST.__cfstring: 0x9a40
+  __AUTH_CONST.__objc_const: 0x15ce8
+  __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x678
-  __AUTH_CONST.__objc_dictobj: 0x2d0
+  __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2e48
-  __AUTH.__data: 0x2740
-  __DATA.__objc_ivar: 0xbb0
-  __DATA.__data: 0x2e68
-  __DATA.__bss: 0x9bc0
-  __DATA.__common: 0x60
+  __AUTH.__objc_data: 0x2ee8
+  __AUTH.__data: 0x2860
+  __DATA.__objc_ivar: 0xbc4
+  __DATA.__data: 0x2f18
+  __DATA.__bss: 0x9bd0
+  __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x2528
-  __DATA_DIRTY.__data: 0x6188
+  __DATA_DIRTY.__data: 0x6198
   __DATA_DIRTY.__bss: 0x4680
   __DATA_DIRTY.__common: 0x198
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E5D72216-A3A2-3CB9-9A0A-E3138F6A5C26
-  Functions: 11501
-  Symbols:   18545
-  CStrings:  8461
+  UUID: 516EC4D0-0A31-3B39-9B96-F7D4F4233778
+  Functions: 11534
+  Symbols:   18613
+  CStrings:  8489
 
Symbols:
+ -[SKDAnalyticsErrorKey .cxx_destruct]
+ -[SKDAnalyticsErrorKey code]
+ -[SKDAnalyticsErrorKey copyWithZone:]
+ -[SKDAnalyticsErrorKey domain]
+ -[SKDAnalyticsErrorKey hash]
+ -[SKDAnalyticsErrorKey initWithDomain:code:]
+ -[SKDAnalyticsErrorKey isEqual:]
+ -[SKDAnalyticsLogger accumulateBatchTracker:]
+ -[SKDAnalyticsLogger accumulateError:]
+ -[SKDAnalyticsLogger flushNow]
+ -[SKDAnalyticsLogger flushNow].cold.1
+ -[SKDAnalyticsLogger initWithDomain:analyticsLogSender:flushInterval:]
+ -[SKDAnalyticsLogger startFlushTimer]
+ -[SKDAnalyticsTrackingEvent batchCount]
+ -[SKDAnalyticsTrackingEvent completedCount]
+ -[SKDAnalyticsTrackingEvent elapsedSeconds]
+ _OBJC_CLASS_$_SKDAnalyticsErrorKey
+ _OBJC_IVAR_$_SKDAnalyticsErrorKey._code
+ _OBJC_IVAR_$_SKDAnalyticsErrorKey._domain
+ _OBJC_IVAR_$_SKDAnalyticsLogger._batchCells
+ _OBJC_IVAR_$_SKDAnalyticsLogger._errorKeys
+ _OBJC_IVAR_$_SKDAnalyticsLogger._errorOverflow
+ _OBJC_IVAR_$_SKDAnalyticsLogger._flushIntervalSeconds
+ _OBJC_IVAR_$_SKDAnalyticsLogger._flushQueue
+ _OBJC_IVAR_$_SKDAnalyticsLogger._flushTimer
+ _OBJC_IVAR_$_SKDAnalyticsLogger._processTable
+ _OBJC_METACLASS_$_SKDAnalyticsErrorKey
+ __DATA__TtC24SpotlightKnowledgeDaemon15PurgeController
+ __IVARS__TtC24SpotlightKnowledgeDaemon15PurgeController
+ __METACLASS_DATA__TtC24SpotlightKnowledgeDaemon15PurgeController
+ __OBJC_$_INSTANCE_METHODS_SKDAnalyticsErrorKey
+ __OBJC_$_INSTANCE_METHODS_SKDAnalyticsLogger
+ __OBJC_$_INSTANCE_VARIABLES_SKDAnalyticsErrorKey
+ __OBJC_$_PROP_LIST_SKDAnalyticsErrorKey
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_SKDAnalyticsErrorKey
+ __OBJC_CLASS_RO_$_SKDAnalyticsErrorKey
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_SKDAnalyticsErrorKey
+ __OBJC_PROTOCOL_$_NSCopying
+ ___37-[SKDAnalyticsLogger startFlushTimer]_block_invoke
+ ___70-[SKDAnalyticsLogger initWithDomain:analyticsLogSender:flushInterval:]_block_invoke
+ ___pipelineIndexFromName_block_invoke
+ _atexit_b
+ _block_copy_helper.104
+ _block_copy_helper.111
+ _block_copy_helper.118
+ _block_copy_helper.125
+ _block_copy_helper.55
+ _block_copy_helper.69
+ _block_copy_helper.76
+ _block_copy_helper.83
+ _block_copy_helper.90
+ _block_descriptor.106
+ _block_descriptor.113
+ _block_descriptor.120
+ _block_descriptor.127
+ _block_descriptor.57
+ _block_descriptor.71
+ _block_descriptor.78
+ _block_descriptor.85
+ _block_descriptor.92
+ _block_destroy_helper.105
+ _block_destroy_helper.112
+ _block_destroy_helper.119
+ _block_destroy_helper.126
+ _block_destroy_helper.56
+ _block_destroy_helper.70
+ _block_destroy_helper.77
+ _block_destroy_helper.84
+ _block_destroy_helper.91
+ _dispatch_resume
+ _get_type_metadata 15Synchronization5MutexVy24SpotlightKnowledgeDaemon15PurgeControllerC5StateVG noncopyable.9
+ _objc_msgSend$batchCount
+ _objc_msgSend$completedCount
+ _objc_msgSend$elapsedSeconds
+ _objc_msgSend$flushNow
+ _objc_msgSend$initWithDomain:analyticsLogSender:flushInterval:
+ _objc_msgSend$initWithDomain:code:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$replaceBytesInRange:withBytes:
+ _objc_msgSend$unsignedCharValue
+ _objectdestroy.50Tm
+ _pipelineIndexFromName.map
+ _pipelineIndexFromName.onceToken
+ _symbolic SDy__________GSg 18SpotlightKnowledge9IndexTypeO 0aB6Daemon15PurgeControllerC
+ _symbolic _____ 24SpotlightKnowledgeDaemon15PurgeControllerC
+ _symbolic _____ 24SpotlightKnowledgeDaemon15PurgeControllerC5StateV
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 24SpotlightKnowledgeDaemon15PurgeControllerC5StateV
+ _symbolic _____y_____G 15Synchronization5_CellVAARi_zrlE 24SpotlightKnowledgeDaemon15PurgeControllerC5StateV
+ _symbolic _____y__________G s18_DictionaryStorageC 18SpotlightKnowledge9IndexTypeO 0cD6Daemon15PurgeControllerC
- -[SKDAnalyticsLogger addTrackingEventLogs:]
- -[SKDAnalyticsLogger analyticsLogSender]
- -[SKDAnalyticsLogger initWithDomain:analyticsLogSender:]
- -[SKDAnalyticsLogger(Internal) setMaxLogCount:]
- -[SKDAnalyticsTrackingEvent .cxx_destruct]
- _OBJC_IVAR_$_SKDAnalyticsLogger._logs
- _OBJC_IVAR_$_SKDAnalyticsLogger._maxLogCount
- _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._errorCount
- _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._logs
- __OBJC_$_INSTANCE_METHODS_SKDAnalyticsLogger(Internal)
- _block_copy_helper.110
- _block_copy_helper.117
- _block_copy_helper.124
- _block_copy_helper.60
- _block_copy_helper.68
- _block_copy_helper.75
- _block_copy_helper.82
- _block_copy_helper.96
- _block_descriptor.112
- _block_descriptor.119
- _block_descriptor.126
- _block_descriptor.62
- _block_descriptor.70
- _block_descriptor.77
- _block_descriptor.84
- _block_descriptor.98
- _block_destroy_helper.111
- _block_destroy_helper.118
- _block_destroy_helper.125
- _block_destroy_helper.61
- _block_destroy_helper.69
- _block_destroy_helper.76
- _block_destroy_helper.83
- _block_destroy_helper.97
- _objc_msgSend$addTrackingEventLogs:
- _objc_msgSend$initWithDomain:analyticsLogSender:
- _objectdestroy.49Tm
CStrings:
+ "@24@0:8^{_NSZone=}16"
+ "NSCopying"
+ "SKDAnalyticsErrorKey"
+ "Tq,R,N,V_code"
+ "[6[9{?=\"processedCount\"I\"pirCountTotal\"I\"pirCountItems\"I\"textSizeBucketCount\"[5I]}]]"
+ "_TtC24SpotlightKnowledgeDaemon15PurgeController"
+ "_batchCells"
+ "_errorKeys"
+ "_errorOverflow"
+ "_flushIntervalSeconds"
+ "_flushQueue"
+ "_flushTimer"
+ "_processTable"
+ "com.apple.spotlightknowledged.analytics-flush"
+ "completedCount"
+ "copyWithZone:"
+ "elapsedSeconds"
+ "errorCode"
+ "flushNow"
+ "initWithDomain:analyticsLogSender:flushInterval:"
+ "initWithDomain:code:"
+ "numberWithUnsignedChar:"
+ "other"
+ "replaceBytesInRange:withBytes:"
+ "skd_batch_summary"
+ "skd_error_summary"
+ "skd_process_summary"
+ "spotlightPurgeControllers"
+ "unsignedCharValue"
- "A"
- "_errorCount"
- "_maxLogCount"
- "addTrackingEventLogs:"
- "erroredCount"
- "initWithDomain:analyticsLogSender:"
- "setMaxLogCount:"

```
