## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`

```diff

-358.0.0.0.0
-  __TEXT.__text: 0x1da90
-  __TEXT.__objc_methlist: 0x28e4
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x2718
-  __TEXT.__gcc_except_tab: 0x648
-  __TEXT.__oslogstring: 0xb07
+361.0.0.0.0
+  __TEXT.__text: 0x1f878
+  __TEXT.__objc_methlist: 0x29cc
+  __TEXT.__const: 0x298
+  __TEXT.__cstring: 0x27da
+  __TEXT.__gcc_except_tab: 0x85c
+  __TEXT.__oslogstring: 0x101a
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__unwind_info: 0xa58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6a8
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1578
+  __DATA_CONST.__objc_selrefs: 0x1618
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__got: 0x288
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x28a0
-  __AUTH_CONST.__objc_const: 0x5a08
+  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__got: 0x2a0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x2980
+  __AUTH_CONST.__objc_const: 0x5b08
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x478
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x174
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0x2b0
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x840
+  __DATA.__bss: 0x2d8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  Functions: 874
-  Symbols:   2199
-  CStrings:  402
+  Functions: 894
+  Symbols:   2267
+  CStrings:  426
 
Symbols:
+ +[MXMOSSignpostProbe initialize]
+ +[MXMOSSignpostProbe invalidateIntervalCache]
+ +[MXMOSSignpostProbe registerSubsystem:category:]
+ +[MXMOSSignpostProbe registeredFilterEntries]
+ +[MXMOSSignpostProbe resetRegisteredFilterEntries]
+ -[MXMCompositeKeyDictionary .cxx_destruct]
+ -[MXMCompositeKeyDictionary count]
+ -[MXMCompositeKeyDictionary init]
+ -[MXMCompositeKeyDictionary objectForPrimaryKey:secondaryKey:]
+ -[MXMCompositeKeyDictionary removeAllObjects]
+ -[MXMCompositeKeyDictionary removeObjectForPrimaryKey:secondaryKey:]
+ -[MXMCompositeKeyDictionary setObject:forPrimaryKey:secondaryKey:]
+ -[MXMOSSignpostMetric prepareWithOptions:error:]
+ -[MXMOSSignpostProbe _cacheSignpostInterval:]
+ -[MXMOSSignpostProbe _isHitchSignpostMetric]
+ -[MXMOSSignpostProbe _replayIntervals:]
+ -[MXMProxyServiceManager _syncSignpostAllowlistConfig:response:]
+ GCC_except_table18
+ GCC_except_table31
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table66
+ _OBJC_CLASS_$_MXMCompositeKeyDictionary
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_SignpostSupportSubsystemCategoryAllowlist
+ _OBJC_IVAR_$_MXMCompositeKeyDictionary._count
+ _OBJC_IVAR_$_MXMCompositeKeyDictionary._storage
+ _OBJC_METACLASS_$_MXMCompositeKeyDictionary
+ __OBJC_$_INSTANCE_METHODS_MXMCompositeKeyDictionary
+ __OBJC_$_INSTANCE_VARIABLES_MXMCompositeKeyDictionary
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MXMSProxySignpostConfig_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MXMSProxySignpostConfig_Internal
+ __OBJC_$_PROTOCOL_REFS_MXMSProxySignpostConfig_Internal
+ __OBJC_CLASS_RO_$_MXMCompositeKeyDictionary
+ __OBJC_LABEL_PROTOCOL_$_MXMSProxySignpostConfig_Internal
+ __OBJC_METACLASS_RO_$_MXMCompositeKeyDictionary
+ __OBJC_PROTOCOL_$_MXMSProxySignpostConfig_Internal
+ ___48-[MXMOSSignpostMetric prepareWithOptions:error:]_block_invoke
+ ___51-[MXMOSSignpostProbe sampleWithTimeout:stopReason:]_block_invoke
+ ___51-[MXMOSSignpostProbe sampleWithTimeout:stopReason:]_block_invoke_2
+ ___64-[MXMProxyServiceManager _syncSignpostAllowlistConfig:response:]_block_invoke
+ ___block_descriptor_32_e47_q24?0"SignpostInterval"8"SignpostInterval"16l
+ ___block_descriptor_40_e8_32s_e43_B24?0"SignpostInterval"8"NSDictionary"16ls32l8
+ __intervalCache
+ __lastSeenIterationStartDate
+ __overflowedCacheKeys
+ __registeredFilterEntries
+ __totalIntervalsCached
+ _objc_msgSend$_cacheSignpostInterval:
+ _objc_msgSend$_isHitchSignpostMetric
+ _objc_msgSend$_replayIntervals:
+ _objc_msgSend$_syncSignpostAllowlistConfig:response:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$invalidateIntervalCache
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$numberOfSamples
+ _objc_msgSend$objectForPrimaryKey:secondaryKey:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$registerSubsystem:category:
+ _objc_msgSend$registeredFilterEntries
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeObjectForPrimaryKey:secondaryKey:
+ _objc_msgSend$setObject:forPrimaryKey:secondaryKey:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$sortUsingComparator:
- GCC_except_table50
- GCC_except_table52
- _OBJC_CLASS_$_SignpostSupportSubsystemCategoryWhitelist
- ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke_4
- ___44-[MXMOSSignpostProbe _setupProcessingBlocks]_block_invoke_5
CStrings:
+ "(subsystem='%@' category='%@')"
+ ", "
+ "B24@?0@\"SignpostInterval\"8@\"NSDictionary\"16"
+ "Intervals Found"
+ "MXM: Beginning to collect metric updates"
+ "MXM: Cache HIT — replayed %lu interval(s), produced %tu sample(s) for subsystem='%@' category='%@'"
+ "MXM: Cache MISS for subsystem='%@' category='%@'. Starting log archive scan."
+ "MXM: Cache lookup for subsystem='%@' category='%@' — %@"
+ "MXM: Cached signpost interval — subsystem='%@' category='%@' (total cached: %lu)"
+ "MXM: Helper iteration boundary detected (startDate=%@) — invalidating probe interval cache"
+ "MXM: Interval with subsystem=%@, category=%@ filtered by mach time, processed, and cached."
+ "MXM: Interval with subsystem=%@, category=%@ processed and cached. No mach time available for filtering."
+ "MXM: Probe interval cache invalidated"
+ "MXM: Probe registered filter: subsystem='%@' category='%@'"
+ "MXM: Processing complete. Cache now has %lu entries."
+ "MXM: Setting up processing filter with %lu entries: [%@]"
+ "MXM: Signpost allowlist not synced (%@); if SignpostSupport scans with an empty allowlist then ALL signposts may be extracted. Ensure that code is being on os 27 or higher."
+ "MXM: Signpost cache limit of %lu interval(s) reached; dropping subsystem='%@' category='%@' and all subsequent intervals for this iteration. Lookup for subsequent intervals will be done via SignpostSupport."
+ "MXM: Skipping cache — interval has nil subsystem or category"
+ "No Intervals Found"
+ "category"
+ "filterEntries"
+ "q24@?0@\"SignpostInterval\"8@\"SignpostInterval\"16"
+ "subsystem"
```
