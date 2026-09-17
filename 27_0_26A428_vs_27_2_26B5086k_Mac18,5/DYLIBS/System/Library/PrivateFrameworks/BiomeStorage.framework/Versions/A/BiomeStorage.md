## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x2afb0
-  __TEXT.__objc_methlist: 0x2094
+255.0.2.0.0
+  __TEXT.__text: 0x2c008
+  __TEXT.__objc_methlist: 0x217c
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x178b
-  __TEXT.__oslogstring: 0x43f2
-  __TEXT.__gcc_except_tab: 0x90c
+  __TEXT.__cstring: 0x17df
+  __TEXT.__oslogstring: 0x4615
+  __TEXT.__gcc_except_tab: 0x93c
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0xd48
+  __TEXT.__unwind_info: 0xdc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1350
+  __DATA_CONST.__objc_selrefs: 0x1408
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x238
-  __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x1560
-  __AUTH_CONST.__objc_const: 0x4cf8
+  __AUTH_CONST.__const: 0x690
+  __AUTH_CONST.__cfstring: 0x1580
+  __AUTH_CONST.__objc_const: 0x4d28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x2a0
+  __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x540
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1031
-  Symbols:   2063
-  CStrings:  441
+  Functions: 1062
+  Symbols:   2114
+  CStrings:  452
 
Symbols:
+ +[BMFrameStore isTimeTravelStreamOptInRequired]
+ +[BMFrameStore isTimeTravelStreamResetEnabledForConfig:]
+ +[BMFrameStore isTimeTravelStreamResetEnabled]
+ +[BMFrameStore timestampIsUnreachablyInTheFuture:]
+ -[BMFrameStore newestFrameTimestamp]
+ -[BMFrameStore(V2) newestFrameTimestampV2]
+ -[BMSegmentManager _lockfilePath]
+ -[BMSegmentManager _resetSegmentsOnUnrealisticFutureFrameWithGuardedData:]
+ -[BMSegmentManager _resetSegmentsWithGuardedData:]
+ -[BMSegmentManager resetSegmentsOnUnrealisticFutureFrame]
+ -[BMSegmentManager resetSegments]
+ -[BMSegmentManager segmentWithFilename:existingFileHandle:segmentNames:segmentFileHandles:error:]
+ -[BMStoreConfig recoversFromFutureDatedEvents]
+ -[BMStoreConfig setRecoversFromFutureDatedEvents:]
+ -[BMStreamDatastore _resetOnUnrealisticFutureFrame]
+ -[BMStreamDatastore resetOnUnrealisticFutureFrame]
+ -[BMStreamDatastore resetStreamWithReason:]
+ -[BMStreamDatastore resetSubstoreOnUnrealisticFutureFrame]
+ -[BMStreamDatastorePruner resetStreamWithReason:]
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table98
+ OBJC_IVAR_$_BMStoreConfig._recoversFromFutureDatedEvents
+ _OUTLINED_FUNCTION_13
+ ___33-[BMSegmentManager resetSegments]_block_invoke
+ ___33-[BMSegmentManager resetSegments]_block_invoke_2
+ ___57-[BMSegmentManager resetSegmentsOnUnrealisticFutureFrame]_block_invoke
+ ___57-[BMSegmentManager resetSegmentsOnUnrealisticFutureFrame]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0l
+ _objc_msgSend$_lockfilePath
+ _objc_msgSend$_resetOnUnrealisticFutureFrame
+ _objc_msgSend$_resetSegmentsOnUnrealisticFutureFrameWithGuardedData:
+ _objc_msgSend$_resetSegmentsWithGuardedData:
+ _objc_msgSend$date
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$isTimeTravelStreamOptInRequired
+ _objc_msgSend$isTimeTravelStreamResetEnabled
+ _objc_msgSend$isTimeTravelStreamResetEnabledForConfig:
+ _objc_msgSend$isUnlinked
+ _objc_msgSend$newestFrameTimestamp
+ _objc_msgSend$newestFrameTimestampV2
+ _objc_msgSend$recoversFromFutureDatedEvents
+ _objc_msgSend$removeFilesAtPaths:error:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resetOnUnrealisticFutureFrame
+ _objc_msgSend$resetSegments
+ _objc_msgSend$resetSegmentsOnUnrealisticFutureFrame
+ _objc_msgSend$resetStreamWithReason:
+ _objc_msgSend$segmentWithFilename:existingFileHandle:segmentNames:segmentFileHandles:error:
+ _objc_msgSend$setRecoversFromFutureDatedEvents:
+ _objc_msgSend$timestampIsUnreachablyInTheFuture:
- GCC_except_table32
- GCC_except_table41
- GCC_except_table55
- GCC_except_table61
- GCC_except_table65
- GCC_except_table68
- GCC_except_table69
- GCC_except_table71
- GCC_except_table77
- GCC_except_table85
- GCC_except_table92
- GCC_except_table94
CStrings:
+ "%{public}@ was reset because it held frames stamped unreachably in the future; events written before the reset are gone"
+ "%{public}@ was reset by another process; dropping our mapping of its removed segment %{public}@"
+ "BMFrameWriteStatusNonMonotonicTimestamp"
+ "Failed to assign a frameStore after resetting: %{public}@"
+ "Read %zd of %zu bytes of segment header for %{public}@: %{darwin.errno}d"
+ "TimeTravelStreamOptIn"
+ "TimeTravelStreamReset"
+ "Unable to open segment %{public}@ to read its version: %@"
+ "Unable to remove every segment of %{public}@: %@"
+ "_lockfilePath: Assertion Failed: [_path hasPrefix:_config.datastorePath]"
+ "failed to remove every segment of %{public}@; it stays wedged"
+ "not resetting %{public}@: its segments could not be listed: %@"
+ "resetting %{public}@ because it is stamped %f, unreachably in the future"
- "_segmentAfterFrameStore: Assertion Failed: [_path hasPrefix:_config.datastorePath]"
- "lastFrameStoreOrCreateWithTimestamp: Assertion Failed: [_path hasPrefix:_config.datastorePath]"
```
