## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x27d78
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x1c58
-  __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x161e
-  __TEXT.__oslogstring: 0x3bcf
-  __TEXT.__gcc_except_tab: 0xa90
+166.15.0.0.0
+  __TEXT.__text: 0x29784
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_methlist: 0x1f84
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x1613
+  __TEXT.__oslogstring: 0x42ac
+  __TEXT.__gcc_except_tab: 0x998
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0xa68
+  __TEXT.__unwind_info: 0xab0
   __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methname: 0x4f04
-  __TEXT.__objc_methtype: 0x1169
-  __TEXT.__objc_stubs: 0x3aa0
+  __TEXT.__objc_methname: 0x5067
+  __TEXT.__objc_methtype: 0x121d
+  __TEXT.__objc_stubs: 0x3be0
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a8
+  __DATA_CONST.__objc_selrefs: 0x1280
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x14c0
-  __AUTH_CONST.__objc_const: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x4b50
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x1d0
+  __DATA.__bss: 0x218
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 931
-  Symbols:   1222
-  CStrings:  1489
+  Functions: 962
+  Symbols:   1248
+  CStrings:  1527
 
Symbols:
+ _OBJC_CLASS_$_BMXPCConnectionFactory
- _OBJC_CLASS_$_BMAccessConnectionFactory
- _fmod
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
