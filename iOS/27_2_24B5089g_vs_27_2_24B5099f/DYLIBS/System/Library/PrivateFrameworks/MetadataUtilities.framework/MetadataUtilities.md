## MetadataUtilities

> `/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities`

```diff

-2465.1.3.0.0
-  __TEXT.__text: 0x73824
+2465.1.7.0.0
+  __TEXT.__text: 0x73ac4
   __TEXT.__objc_methlist: 0x494
   __TEXT.__const: 0x543e
-  __TEXT.__cstring: 0x8483
-  __TEXT.__oslogstring: 0x1eb5
+  __TEXT.__cstring: 0x7b6d
+  __TEXT.__oslogstring: 0x2056
   __TEXT.__ustring: 0x9a
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1a08
+  __TEXT.__unwind_info: 0x19b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA.__common: 0x858
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__bss: 0x398
+  __DATA_DIRTY.__bss: 0x388
   __DATA_DIRTY.__common: 0xf0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1676
-  Symbols:   2168
-  CStrings:  1824
+  Functions: 1659
+  Symbols:   2182
+  CStrings:  1794
 
Symbols:
+ __MDPlistContainerAbandonBuild
+ ___copyCSObject_block_invoke
+ ___copyCSObject_block_invoke_2
+ _addBufferedObjectOrNull
+ _arrayIterate
+ _copyCFString
+ _copyCSObject
+ _copyCSObject.kClassPrefix
+ _copyCrossedObject
+ _dictionaryIterate
+ _disposeBuildScratch
+ _logRejectedContainer
+ _metaAssertHelper
+ _parseRootPlistObjectFromBuffer
+ _refuseNestingPastLimit
+ _validatedPlistObjectOrRejection
- ____MDPlistContainerCopyCSObject_block_invoke
- ____MDPlistContainerCopyCSObject_block_invoke_2
CStrings:
+ "Abandoned MDPlistContainer build: nesting reached the %d level limit"
+ "Parsed v2 journal entry with faulty isFromMail size %ld"
+ "Refused a %zu byte buffer that does not carry the MDPlistContainer magic word"
+ "Rejected malformed MDPlistContainer, _MDPlistContainer.c:%d (a %d, b %d)"
+ "Rejected malformed MDPlistContainer, check at _MDPlistContainer.c:%d"
+ "Substituted null for MDPlistContainer object with unhandled type 0x%02x"
- "(size_t)headerRecord->common.offsetToBase <= containerBuffer->size"
- "*(uint16_t *)bytes == (0xBADE)"
- "CSLocalizedString"
- "__class:"
- "buf_size == headerRecord->totalSize"
- "containerBuffer->size == (size_t)headerRecord->totalSize"
- "containerBuffer->size >= sizeof(MDPlistContainerHeaderRecord)"
- "count <= objectCollection->totalSize"
- "count == 0 || headerRecord->uniqueKeysOffset != 0"
- "depth < (1024)"
- "headerRecord->common.totalSize == headerRecord->common.offsetToBase"
- "headerRecord->uniqueKeysOffset < headerRecord->totalSize"
- "headerRecord->uniqueKeysOffset == 0 || containerBuffer->bytes[containerBuffer->size - 1] == '\\0'"
- "length < collection->totalSize"
- "object.reference.embeddedReference + length <= buf_size"
- "object.reference.embeddedReference + length <= collectionBufferOffset + offsetToBase"
- "object.reference.embeddedReference + objectCollection->offsetToBase + ((slotCount + 1) * sizeof(uint16_t)) + (count * sizeof(MDPlistDictionaryElementRecord)) <= buf_size"
- "object.reference.embeddedReference + objectCollection->offsetToBase + count * sizeof(MDPlistObjectReference) <= buf_size"
- "object.reference.embeddedReference + sizeof(MDPlistCommonRecord) <= buf_size"
- "object.reference.embeddedReference + sizeof(MDPlistDictionaryHeaderRecord) <= buf_size"
- "object.reference.embeddedReference + sizeof(double) <= object.containerLength"
- "object.reference.embeddedReference + sizeof(uint32_t) <= buf_size"
- "object.reference.embeddedReference + sizeof(uint64_t) <= object.containerLength"
- "object.reference.embeddedReference + sizeof(uuid_t) <= object.containerLength"
- "object.reference.embeddedReference < collectionBufferOffset + offsetToBase"
- "object.reference.embeddedReference >= collectionBufferOffset"
- "objectCollection->count * sizeof(MDPlistObjectReference) <= indexArraySize"
- "objectCollection->offsetToBase <= objectCollection->totalSize + sizeof(uint32_t)"
- "objectCollection->totalSize + sizeof(uint32_t) - objectCollection->offsetToBase == (slotCount + 1) * sizeof(uint16_t) + count * sizeof(MDPlistDictionaryElementRecord)"
- "offset + length + sizeof(uint16_t) < headerRecord->totalSize - headerRecord->uniqueKeysOffset"
- "plist->sp < (1024)"
- "slotCount != 0"
- "slotCount < (objectCollection->count ? : 1) * 2"
- "totalSize <= arrayRecord->common.offsetToBase"
- "totalSize <= dictionaryRecord->common.offsetToBase"
- "type == 0xF4 || type == 0xF5 || type == 0xF6 || type == 0xF7"
```
