## OSLog

> `/System/Library/Frameworks/OSLog.framework/OSLog`

```diff

-1861.120.4.0.0
-  __TEXT.__text: 0xafa4
-  __TEXT.__auth_stubs: 0x760
+1952.0.0.0.0
+  __TEXT.__text: 0xabac
   __TEXT.__objc_methlist: 0x678
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0xa00
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__cstring: 0xae4
   __TEXT.__oslogstring: 0x59
-  __TEXT.__unwind_info: 0x2f8
-  __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0xec4
-  __TEXT.__objc_methtype: 0x251
-  __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x368
+  __TEXT.__unwind_info: 0x310
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x480
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x130
+  __DATA_CONST.__got: 0xf0
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x11b0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x1f8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__os_assumes_log: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F4632D5-7351-3E7C-B5C1-D4FEE63DFDC6
-  Functions: 234
-  Symbols:   898
-  CStrings:  418
+  UUID: 709AE07C-3D0F-3243-B170-DF07B2335E9C
+  Functions: 240
+  Symbols:   936
+  CStrings:  178
 
Symbols:
+ GCC_except_table214
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table237
+ ___43-[OSLogCurrentProcessEnumerator nextObject]_block_invoke.39
+ ___68-[OSLogCurrentProcessEnumerator initWithOptions:predicate:position:]_block_invoke.36
+ ____os_persona_info_map_clear_block_invoke
+ ____os_procinfo_map_clear_block_invoke
+ ____os_procinfo_map_lookup_by_procid_block_invoke
+ ____os_trace_personas_in_oslog_enabled_block_invoke
+ ____os_trace_str_map_clear_block_invoke
+ ____os_trace_uuid_map_clear_block_invoke
+ ____os_trace_uuid_map_filter_block_invoke
+ ____os_trace_uuid_map_for_each_block_invoke
+ ___block_descriptor_tmp.1
+ ___block_descriptor_tmp.11.148
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.17.43
+ ___block_descriptor_tmp.2.103
+ ___block_descriptor_tmp.3.112
+ ___block_descriptor_tmp.3.59
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.5.119
+ ___block_descriptor_tmp.6
+ ___block_descriptor_tmp.77
+ ___block_descriptor_tmp.8.133
+ ___block_descriptor_tmp.82
+ ___block_descriptor_tmp.85
+ ___block_descriptor_tmp.95
+ ___block_literal_global.15
+ ___block_literal_global.38
+ ___block_literal_global.45
+ ___block_literal_global.499
+ ___block_literal_global.5.57
+ ___block_literal_global.75
+ ___block_literal_global.8
+ __catalog_insert_persona_info
+ __catalog_persona_info_free
+ __os_feature_enabled_impl
+ __os_persona_info_map_clear
+ __os_persona_info_map_insert
+ __os_procinfo_map_lookup_by_procid
+ __os_trace_personas_in_oslog_enabled
+ __os_trace_personas_in_oslog_enabled.enabled
+ __os_trace_personas_in_oslog_enabled.once
+ __os_trace_strdup
+ __os_trace_uuid_map_for_each
+ _catalog_procinfo_persona_add
+ _catalog_procinfo_persona_add_from_catalog
+ _kpersona_info
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _os_map_128_clear
+ _os_map_128_count
+ _os_map_128_destroy
+ _os_map_128_find
+ _os_map_128_foreach
+ _os_map_128_init
+ _os_map_128_insert
+ _os_map_32_clear
+ _os_map_32_destroy
+ _os_map_32_find
+ _os_map_32_init
+ _os_map_32_insert
+ _os_map_str_clear
+ _os_map_str_destroy
+ _os_map_str_entry
+ _os_map_str_find
+ _os_map_str_init
+ _os_map_str_insert
+ _strdup
+ _strnlen
- GCC_except_table209
- GCC_except_table222
- GCC_except_table226
- GCC_except_table232
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqn210106EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9nqn210106ERKS6_S9_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_S8_EEEE
- __ZNSt3__112__next_primeEm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqn210106ILi0EEEPKc
- __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZdlPv
- __ZdlPvSt19__type_descriptor_t
- __ZnwmSt19__type_descriptor_t
- ___43-[OSLogCurrentProcessEnumerator nextObject]_block_invoke.40
- ___68-[OSLogCurrentProcessEnumerator initWithOptions:predicate:position:]_block_invoke.37
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.116
- ___block_descriptor_tmp.3.96
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.78
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.90
- ___block_literal_global.103
- ___block_literal_global.39
- ___block_literal_global.452
- ___block_literal_global.5.94
- ___block_literal_global.55
- ___block_literal_global.86
- __os_procinfo_map_clear
- __os_procinfo_map_lookup
- __os_trace_str_map_entry
- _abort
- _bzero
- _hashkey_compare_array
- _hashkey_compare_uint16
- _hashkey_compare_uint64
- _hashtable_create
- _memcmp
- _memmove
CStrings:
+ "B20@?0I8^v12"
+ "B24@?0r*8^v16"
+ "B32@?0{os_map_128_key_s=[2Q]}8^v24"
+ "Catalog Persona Section"
+ "Error: Invalid persona name offset"
+ "Error: Not enough data for persona entries"
+ "Error: Persona name length exceeds maximum"
+ "Error: Persona name not null-terminated"
+ "Libtrace"
+ "Persona ID: %u, Type: %d, Name: %s\n"
+ "personas_in_oslog"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"OSLogEntry\""
- "@\"OSLogEventSource\""
- "@\"OSLogEventStream\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8d16"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16d24"
- "@32@0:8q16^@24"
- "@36@0:8@16@24i32"
- "@40@0:8@16Q24@32"
- "@40@0:8Q16@24@32"
- "@48@0:8Q16@24@32^@40"
- "B"
- "B16@0:8"
- "Catalog Persona Section (skipping)"
- "NSCoding"
- "NSSecureCoding"
- "OSLogCurrentProcessEnumerator"
- "OSLogEntry"
- "OSLogEntryActivity"
- "OSLogEntryBoundary"
- "OSLogEntryFromProcess"
- "OSLogEntryLog"
- "OSLogEntrySignpost"
- "OSLogEntryWithPayload"
- "OSLogEnumerator"
- "OSLogMessageComponent"
- "OSLogPosition"
- "OSLogServiceProtocol"
- "OSLogStore"
- "OSLogSystemEnumerator"
- "Persona section found with %hu entries - skipping for compatibility\n"
- "Q"
- "Q16@0:8"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_components"
- "T@\"NSData\",C,N,V_argumentDataValue"
- "T@\"NSDate\",R,N,V_date"
- "T@\"NSNumber\",C,N,V_argumentNumberValue"
- "T@\"NSString\",C,N,V_argumentStringValue"
- "T@\"NSString\",C,N,V_formatSubstring"
- "T@\"NSString\",C,N,V_placeholder"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_category"
- "T@\"NSString\",R,N,V_composedMessage"
- "T@\"NSString\",R,N,V_formatString"
- "T@\"NSString\",R,N,V_process"
- "T@\"NSString\",R,N,V_sender"
- "T@\"NSString\",R,N,V_signpostName"
- "T@\"NSString\",R,N,V_subsystem"
- "TB,R"
- "TQ,R,N"
- "TQ,R,N,V_activityIdentifier"
- "TQ,R,N,V_argumentUInt64Value"
- "TQ,R,N,V_parentActivityIdentifier"
- "TQ,R,N,V_signpostIdentifier"
- "TQ,R,N,V_threadIdentifier"
- "Td,R,N,V_argumentDoubleValue"
- "Td,R,N,V_offset"
- "Ti,R,N"
- "Ti,R,N,V_processIdentifier"
- "Tq,R,N,V_argumentCategory"
- "Tq,R,N,V_argumentInt64Value"
- "Tq,R,N,V_level"
- "Tq,R,N,V_precision"
- "Tq,R,N,V_signpostType"
- "Tq,R,N,V_storeCategory"
- "_activateStreamFromTimeIntervalSinceLastBoot:"
- "_activityIdentifier"
- "_argumentCategory"
- "_argumentDataValue"
- "_argumentDoubleValue"
- "_argumentInt64Value"
- "_argumentNumberValue"
- "_argumentStringValue"
- "_argumentUInt64Value"
- "_category"
- "_components"
- "_composedMessage"
- "_connectionToService"
- "_constrainedEntriesEnumeratorWithOptions:position:predicate:error:"
- "_constraint"
- "_date"
- "_done"
- "_formatString"
- "_formatSubstring"
- "_handleEventProxy:"
- "_handleInvalidation"
- "_handlerDone"
- "_level"
- "_next"
- "_offset"
- "_parentActivityIdentifier"
- "_placeholder"
- "_precision"
- "_process"
- "_processIdentifier"
- "_pushDone"
- "_sender"
- "_signpostIdentifier"
- "_signpostName"
- "_signpostType"
- "_source"
- "_storeCategory"
- "_stream"
- "_subsystem"
- "_threadIdentifier"
- "activateStreamFromDate:"
- "addObject:"
- "argumentAtIndex:"
- "argumentNumberValue"
- "arrayWithObjects:count:"
- "availability"
- "d"
- "d16@0:8"
- "dateByAddingTimeInterval:"
- "dealloc"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decomposedMessage"
- "dictionaryWithObjects:forKeys:count:"
- "distantPast"
- "doubleValue"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "entriesEnumeratorAndReturnError:"
- "entriesEnumeratorWithOptions:position:predicate:error:"
- "errorWithDomain:code:userInfo:"
- "fillWithData:"
- "fillWithScalar:"
- "fillWithString:"
- "getNextOSLogEntryWithReply:"
- "i"
- "i16@0:8"
- "init"
- "initForFactory"
- "initWithCoder:"
- "initWithDate:"
- "initWithDate:composedMessage:"
- "initWithDate:composedMessage:processIdentifier:"
- "initWithDecomposedMessage:atIndex:"
- "initWithEventProxy:"
- "initWithEventSource:timeIntervalSinceEnd:"
- "initWithEventStream:options:position:"
- "initWithOptions:predicate:position:"
- "initWithServiceName:"
- "initWithSource:"
- "initWithTimeIntervalSinceLatestBoot:"
- "int64Value"
- "interfaceWithProtocol:"
- "invalidate"
- "literalPrefixAtIndex:"
- "logType"
- "newestDate"
- "nextObject"
- "numberWithDouble:"
- "numberWithLongLong:"
- "numberWithUnsignedLongLong:"
- "objectRepresentation"
- "placeholderAtIndex:"
- "placeholderCount"
- "positionWithDate:"
- "positionWithTimeIntervalSinceEnd:"
- "positionWithTimeIntervalSinceLatestBoot:"
- "precision"
- "prepareWithCompletionHandler:"
- "q"
- "q16@0:8"
- "rawString"
- "reason"
- "resume"
- "scalarCategory"
- "setArgumentDataValue:"
- "setArgumentNumberValue:"
- "setArgumentStringValue:"
- "setEventHandler:"
- "setFilterPredicate:"
- "setFlags:"
- "setFormatSubstring:"
- "setInvalidationHandler:"
- "setPlaceholder:"
- "setRemoteObjectInterface:"
- "setUpWithPredicate:reply:"
- "setWithArray:"
- "state"
- "storeWithArchiveURL:"
- "storeWithScope:error:"
- "storeWithURL:error:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "type"
- "unsignedInt64Value"
- "unsignedLongLongValue"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"OSLogEntry\">16"
- "v32@0:8@\"NSPredicate\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"

```
