## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x2b554
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x1c68
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x16c8
-  __TEXT.__oslogstring: 0x3c1d
-  __TEXT.__gcc_except_tab: 0xaa0
+166.17.1.0.0
+  __TEXT.__text: 0x2d040
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x1f94
+  __TEXT.__const: 0x1f8
+  __TEXT.__cstring: 0x16bd
+  __TEXT.__oslogstring: 0x42fa
+  __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0xaa8
+  __TEXT.__unwind_info: 0xad0
   __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methname: 0x4f33
-  __TEXT.__objc_methtype: 0x1174
-  __TEXT.__objc_stubs: 0x3ae0
+  __TEXT.__objc_methname: 0x5096
+  __TEXT.__objc_methtype: 0x1228
+  __TEXT.__objc_stubs: 0x3c20
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11b8
+  __DATA_CONST.__objc_selrefs: 0x1290
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0x14c0
-  __AUTH_CONST.__objc_const: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x4b50
   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x200
+  __DATA.__bss: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B3B914EC-78DC-395C-9F5E-3CDEEE957454
-  Functions: 965
-  Symbols:   2292
-  CStrings:  1645
+  UUID: 5F1B5ED5-2475-30C1-BFE3-8DA469A3E9BB
+  Functions: 997
+  Symbols:   2337
+  CStrings:  1683
 
Symbols:
+ -[BMFrameStore enumerateWithOptionsV1:fromOffset:usingBlock:].cold.1
+ -[BMFrameStore updateFrameStoreIndex].cold.1
+ -[BMFrameStore(V2) atomicReadDoubleByteValueAtAddress:]
+ -[BMFrameStore(V2) atomicReadEightByteValueAtAddress:]
+ -[BMFrameStore(V2) atomicReadFourByteValueAtAddress:]
+ -[BMFrameStore(V2) atomicReadSixteenByteValueAtAddress:]
+ -[BMFrameStore(V2) checkBoundsLength:]
+ -[BMFrameStore(V2) checkBoundsLength:].cold.1
+ -[BMFrameStore(V2) checkBoundsLength:].cold.2
+ -[BMFrameStore(V2) checkBoundsLength:].cold.3
+ -[BMFrameStore(V2) checkBoundsLength:].cold.4
+ -[BMFrameStore(V2) determineFrameNumberToBeWritten:]
+ -[BMFrameStore(V2) determineFrameNumberToBeWritten:].cold.1
+ -[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:].cold.1
+ -[BMFrameStore(V2) findValidOffsetTableEntryToReplaceMidFrame:bottomFrame:topFrame:reverse:]
+ -[BMFrameStore(V2) reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:]
+ -[BMFrameStore(V2) reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:].cold.1
+ -[BMFrameStore(V2) reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:].cold.2
+ -[BMFrameStore(V2) reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:].cold.3
+ -[BMFrameStore(V2) reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:].cold.4
+ -[BMFrameStore(V2) validOffsetTableEntry:frameNumber:]
+ -[BMFrameStore(V2) validOffsetTableEntryAtFrame:]
+ -[BMFrameStore(V2) validateOrUpdateTimestamp:frameNumberToBeWritten:]
+ -[BMMemoryMapping atomicWriteFourBytes:toOffset:expected:]
+ -[BMMemoryMapping atomicWriteSixteenBytes:toOffset:expected:]
+ -[BMMemoryMapping canAtomicallyAccessOffset:byteCount:]
+ -[BMStoreBookmark initWithStream:segment:iterationStartTime:offset:].cold.1
+ -[BMStoreBookmark initWithStream:segment:iterationStartTime:offset:].cold.2
+ -[BMStoreBookmark initWithStream:segment:iterationStartTime:offset:].cold.3
+ -[BMStoreBookmark initWithStream:segment:iterationStartTime:offset:].cold.4
+ -[BMStoreConfig _initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:].cold.1
+ -[BMStoreEnumerator initWithStreamDatastore:bookmarkEnumerator:error:].cold.1
+ -[BMStreamDatastore enumerateEventsFrom:to:options:usingBlock:].cold.1
+ -[BMStreamDatastore fetchEventFromFrameStore:atOffset:withOptions:callback:].cold.2
+ -[BMWriteServerExported checkEntitlementsAndReturnWriterForStreamIdentifier:user:error:].cold.2
+ -[BMWriteServerExported checkEntitlementsAndReturnWriterForStreamIdentifier:user:error:].cold.3
+ GCC_except_table113
+ GCC_except_table40
+ GCC_except_table87
+ _OBJC_CLASS_$_BMXPCConnectionFactory
+ __39-[BMSegmentManager removeSegmentNamed:]_block_invoke.66
+ __52-[BMFrameStore(V2) initWithFileHandleV2:permission:]_block_invoke.10
+ __56-[BMSegmentManager lastFrameStoreOrCreateWithTimestamp:]_block_invoke.57
+ __59-[BMFrameStore(V2) firstFrameNumberForTimestampV2:reverse:]_block_invoke.2
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.42
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.44
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.46
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.48
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.50
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.52
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.54
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.56
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.58
+ __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.60
+ __68-[BMSegmentManager initWithDirectory:fileManager:permission:config:]_block_invoke.25
+ __68-[BMSegmentManager initWithDirectory:fileManager:permission:config:]_block_invoke.27
+ __83-[BMSegmentManager _segmentAfterFrameStore:orCreateSegmentWithTimestamp:direction:]_block_invoke.59
+ ___100-[BMFrameStore(V2) reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:]_block_invoke
+ ___38-[BMFrameStore(V2) checkBoundsLength:]_block_invoke
+ ___49-[BMFrameStore(V2) validOffsetTableEntryAtFrame:]_block_invoke
+ ___52-[BMFrameStore(V2) determineFrameNumberToBeWritten:]_block_invoke
+ ___59-[BMFrameStore(V2) firstFrameNumberForTimestampV2:reverse:]_block_invoke
+ ___69-[BMFrameStore(V2) validateOrUpdateTimestamp:frameNumberToBeWritten:]_block_invoke
+ _objc_msgSend$atomicReadDoubleByteValueAtAddress:
+ _objc_msgSend$atomicReadEightByteValueAtAddress:
+ _objc_msgSend$atomicReadFourByteValueAtAddress:
+ _objc_msgSend$atomicReadSixteenByteValueAtAddress:
+ _objc_msgSend$atomicWriteFourBytes:toOffset:expected:
+ _objc_msgSend$atomicWriteSixteenBytes:toOffset:expected:
+ _objc_msgSend$canAtomicallyAccessOffset:byteCount:
+ _objc_msgSend$checkBoundsLength:
+ _objc_msgSend$determineFrameNumberToBeWritten:
+ _objc_msgSend$findValidOffsetTableEntryToReplaceMidFrame:bottomFrame:topFrame:reverse:
+ _objc_msgSend$replaceFileAtPath:withData:protection:flags:error:
+ _objc_msgSend$replaceFileAtPath:withFileHandle:protection:flags:error:
+ _objc_msgSend$reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:
+ _objc_msgSend$validOffsetTableEntry:frameNumber:
+ _objc_msgSend$validOffsetTableEntryAtFrame:
+ _objc_msgSend$validateOrUpdateTimestamp:frameNumberToBeWritten:
+ checkBoundsLength:.onceToken
+ determineFrameNumberToBeWritten:.onceToken
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.41
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.43
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.45
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.47
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.49
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.51
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.53
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.55
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.57
+ enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.59
+ firstFrameNumberForTimestampV2:reverse:.onceToken
+ firstFrameNumberForTimestampV2:reverse:.onceToken.1
+ initWithFileHandleV2:permission:.onceToken.9
+ reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:.onceToken
+ validOffsetTableEntryAtFrame:.onceToken
+ validateOrUpdateTimestamp:frameNumberToBeWritten:.onceToken
- -[BMFrameStore(V2) appendOffsetTableEntry:outOffsetForFrame:length:frameCount:]
- -[BMFrameStore(V2) appendOffsetTableEntry:outOffsetForFrame:length:frameCount:].cold.1
- -[BMFrameStore(V2) initWithFileHandleV2:permission:].cold.5
- -[BMFrameStore(V2) writeFrameV2ForBytes:length:dataVersion:timestamp:outOffset:].cold.2
- -[BMFrameStore(V2) writeFrameV2ForBytes:length:dataVersion:timestamp:outOffset:].cold.3
- -[BMFrameStore(V2) writeFrameV2ForBytes:length:dataVersion:timestamp:outOffset:].cold.4
- -[BMFrameStore(V2) writeFrameV2ForBytes:length:dataVersion:timestamp:outOffset:].cold.5
- -[BMFrameStore(V2) writeFrameV2ForBytes:length:dataVersion:timestamp:outOffset:].cold.6
- -[BMMemoryMapping canAtomicallyAccessOffset:]
- -[BMStreamDatastore initForPruningWithStream:config:includeTombstones:]
- -[BMStreamDatastore initForReadingWithStream:config:includeTombstones:]
- -[BMStreamDatastore initForWritingWithStream:config:includeTombstones:]
- GCC_except_table117
- GCC_except_table52
- GCC_except_table56
- GCC_except_table88
- GCC_except_table90
- _OBJC_CLASS_$_BMAccessConnectionFactory
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- __39-[BMSegmentManager removeSegmentNamed:]_block_invoke.60
- __47-[BMSegmentManager segmentContainingTimestamp:]_block_invoke.cold.1
- __52-[BMFrameStore(V2) initWithFileHandleV2:permission:]_block_invoke.4
- __56-[BMSegmentManager lastFrameStoreOrCreateWithTimestamp:]_block_invoke.51
- __56-[BMSegmentManager lastFrameStoreOrCreateWithTimestamp:]_block_invoke.51.cold.1
- __56-[BMSegmentManager lastFrameStoreOrCreateWithTimestamp:]_block_invoke.cold.1
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.41
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.43
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.45
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.47
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.49
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.51
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.53
- __65-[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:]_block_invoke.55
- __68-[BMSegmentManager initWithDirectory:fileManager:permission:config:]_block_invoke.21
- __68-[BMSegmentManager initWithDirectory:fileManager:permission:config:]_block_invoke.23
- __83-[BMSegmentManager _segmentAfterFrameStore:orCreateSegmentWithTimestamp:direction:]_block_invoke.53
- __83-[BMSegmentManager _segmentAfterFrameStore:orCreateSegmentWithTimestamp:direction:]_block_invoke.53.cold.1
- ___79-[BMFrameStore(V2) appendOffsetTableEntry:outOffsetForFrame:length:frameCount:]_block_invoke
- _fmod
- _objc_msgSend$appendOffsetTableEntry:outOffsetForFrame:length:frameCount:
- _objc_msgSend$canAtomicallyAccessOffset:
- _objc_msgSend$lastAbsoluteTimestamp
- _objc_msgSend$replaceFileAtPath:withData:protection:error:
- _objc_msgSend$replaceFileAtPath:withFileHandle:protection:error:
- _objc_msgSend$setLastAbsoluteTimestamp:
- appendOffsetTableEntry:outOffsetForFrame:length:frameCount:.onceToken
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.40
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.42
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.44
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.46
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.48
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.50
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.52
- enumerateWithOptionsV2:fromOffset:usingBlock:.onceToken.54
- initWithFileHandleV2:permission:.onceToken.3
CStrings:
+ "-[BMFrameStore(V2) validateOrUpdateTimestamp:frameNumberToBeWritten:]"
+ "B20@0:8i16"
+ "B36@0:8{?=(?={?=(?={?=II}Q)d})}16i32"
+ "C24@0:8Q16"
+ "C24@0:8^I16"
+ "C28@0:8^d16I24"
+ "C36@0:8I16Q20^I28"
+ "C40@0:8d16I24I28^I32"
+ "C48@0:8t16Q32^t40"
+ "I24@0:8^I16"
+ "I24@0:8^{?=(?={?=(?={?=II}Q)d})}16"
+ "Invalid BMFrameState (%d) for frame %d in segment: %@"
+ "Invalid offset (%d) for frame %d in segment: %@"
+ "Invalid timestamp (%f), too far in the future, for frame %d in segment: %@"
+ "Invalid timestamp (%f), too far in the past, for frame %d in segment: %@"
+ "NULL frame number sent to reserveSpaceAndAssignAnOffsetTableEntryForTimestamp"
+ "NULL value passed to determineFrameNumberToBeWritten for segment: %@"
+ "No space left to write an EOF into the mapped region"
+ "Q24@0:8^Q16"
+ "Unable to update frameStatusData, write status is %d"
+ "Unable to update status to written, someone else seems to have overwritten the value. We expect to see %u, but instead are seeing %u. The write status is %d"
+ "Unable to write frame (%d) for reason: %@ for segment: %@"
+ "^{?=(?={?=(?={?=II}Q)d})}20@0:8I16"
+ "atomicReadDoubleByteValueAtAddress:"
+ "atomicReadEightByteValueAtAddress:"
+ "atomicReadFourByteValueAtAddress:"
+ "atomicReadSixteenByteValueAtAddress:"
+ "atomicWriteFourBytes:toOffset:expected:"
+ "atomicWriteSixteenBytes:toOffset:expected:"
+ "canAtomicallyAccessOffset:byteCount:"
+ "checkBoundsLength:"
+ "d24@0:8^d16"
+ "determineFrameNumberToBeWritten:"
+ "determineFrameNumberToBeWritten: offsetTableEntryPtr:NULL outside of range for frames, frameNumber=%d for segment: %{public}@"
+ "enumerateWithOptions: offset (%u) beyond the space used:%u by the currentFrameCount:%d, state:%d prevOffsetToByteAFterFrame:%d  segment:%@"
+ "enumerateWithOptionsV2: lastOffsetTable:NULL outside of range for frames, mapping to frame: %d when segment has only %d frames in segment: %{public}@"
+ "enumerateWithOptionsV2: offsetTableEntryPtr:NULL outside of range for frames, frameNumber=%d for segment: %{public}@"
+ "findValidOffsetTableEntryToReplaceMidFrame:bottomFrame:topFrame:reverse:"
+ "firstFrameNumberForTimestampV2: offsetTableEntryPtr:NULL outside of range for frames, frameNumber=%d for segment: %{public}@"
+ "i24@0:8^{?=(?={?=(?={?=II}Q)d})}16"
+ "i32@0:8i16i20i24B28"
+ "replaceFileAtPath:withData:protection:flags:error:"
+ "replaceFileAtPath:withFileHandle:protection:flags:error:"
+ "reserveSpaceAndAssignAnOffsetTableEntryForTimestamp called with unexpected dataVersion:%d"
+ "reserveSpaceAndAssignAnOffsetTableEntryForTimestamp: timestamp was adjusted more than %d seconds beyond the original timestamp: %f to: %f"
+ "reserveSpaceAndAssignAnOffsetTableEntryForTimestamp:state:length:outFrameNumber:"
+ "t24@0:8^t16"
+ "validOffsetTableEntry:frameNumber:"
+ "validOffsetTableEntryAtFrame:"
+ "validOffsetTableEntryAtFrame: offsetTableEntryPtr:NULL outside of range for frames, frameNumber=%d for segment: %{public}@"
+ "validateOrUpdateTimestamp: offsetTableEntryPtr:NULL outside of range for frames, frameNumber=%d for segment: %{public}@"
+ "validateOrUpdateTimestamp:frameNumberToBeWritten:"
+ "writeFrameV2ForBytes: offsetTableEntryPtr:NULL outside of range for frames, frameNumber=%d for segment: %{public}@"
- "-[BMFrameStore(V2) writeFrameV2ForBytes:length:dataVersion:timestamp:outOffset:]"
- "@36@0:8@16@24B32"
- "C44@0:8^{?=(?={?=II}Q)d}16^I24I32^I36"
- "I24@0:8^{?=(?={?=II}Q)d}16"
- "^{?=(?={?=II}Q)d}20@0:8I16"
- "appendOffsetTable called with unexpected dataVersion:%d"
- "appendOffsetTableEntry:outOffsetForFrame:length:frameCount:"
- "canAtomicallyAccessOffset:"
- "enumerateWithOptions: lastOffsetTable:NULL outside of range for frames, mapping to frame: %d when segment has only %d frames in segment: %{public}@"
- "i24@0:8^{?=(?={?=II}Q)d}16"
- "initForPruningWithStream:config:includeTombstones:"
- "initForReadingWithStream:config:includeTombstones:"
- "initForWritingWithStream:config:includeTombstones:"
- "replaceFileAtPath:withData:protection:error:"
- "replaceFileAtPath:withFileHandle:protection:error:"

```
