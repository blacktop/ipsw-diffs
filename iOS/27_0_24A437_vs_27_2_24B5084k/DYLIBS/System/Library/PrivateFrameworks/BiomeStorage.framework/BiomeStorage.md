## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x289d0
-  __TEXT.__objc_methlist: 0x208c
-  __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x16e1
-  __TEXT.__oslogstring: 0x43a4
-  __TEXT.__gcc_except_tab: 0x904
+255.0.2.0.0
+  __TEXT.__text: 0x29984
+  __TEXT.__objc_methlist: 0x2174
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x1735
+  __TEXT.__oslogstring: 0x45c7
+  __TEXT.__gcc_except_tab: 0x934
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0xd28
+  __TEXT.__unwind_info: 0xda0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1340
+  __DATA_CONST.__objc_selrefs: 0x13f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x238
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1560
-  __AUTH_CONST.__objc_const: 0x4cf8
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
-  Functions: 994
-  Symbols:   2033
-  CStrings:  438
+  Functions: 1026
+  Symbols:   2084
+  CStrings:  449
 
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
+ GCC_except_table26
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table82
+ _OBJC_IVAR_$_BMStoreConfig._recoversFromFutureDatedEvents
+ _OUTLINED_FUNCTION_13
+ ___33-[BMSegmentManager resetSegments]_block_invoke
+ ___33-[BMSegmentManager resetSegments]_block_invoke_2
+ ___57-[BMSegmentManager resetSegmentsOnUnrealisticFutureFrame]_block_invoke
+ ___57-[BMSegmentManager resetSegmentsOnUnrealisticFutureFrame]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48r_e40_v16?0"BMSegmentManagerProtectedState"8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
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
- GCC_except_table39
- GCC_except_table43
- GCC_except_table49
- GCC_except_table51
- GCC_except_table55
- GCC_except_table59
- GCC_except_table61
- GCC_except_table64
- GCC_except_table73
- GCC_except_table76
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
