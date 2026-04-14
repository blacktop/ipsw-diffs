## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-1037.120.8.0.0
-  __TEXT.__text: 0x2ef98
+1037.120.9.0.0
+  __TEXT.__text: 0x2ef5c
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x353c
   __TEXT.__const: 0x10a

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0xd68
   __TEXT.__objc_classname: 0x703
-  __TEXT.__objc_methname: 0x6cc7
+  __TEXT.__objc_methname: 0x6cbc
   __TEXT.__objc_methtype: 0x101c
   __TEXT.__objc_stubs: 0x6280
   __DATA_CONST.__got: 0x328

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: EECAA362-1D9C-3106-8CCE-4AE309775C3E
+  UUID: F3DA2A02-0C6B-3654-B07C-A2A32E2AA078
   Functions: 1197
   Symbols:   4551
   CStrings:  2732
Symbols:
+ -[SKPartition buildWithScheme:]
+ ___31-[SKPartition buildWithScheme:]_block_invoke
+ _objc_msgSend$buildWithScheme:
- -[SKPartition buildWithScheme:sectorSize:]
- ___42-[SKPartition buildWithScheme:sectorSize:]_block_invoke
- _objc_msgSend$buildWithScheme:sectorSize:
Functions:
~ -[SKPartition buildWithScheme:sectorSize:] -> -[SKPartition buildWithScheme:] : 336 -> 324
~ -[SKPartitionTable writePartitionScheme:error:] : 816 -> 800
~ -[SKPartitionTable resizePartitionID:size:offset:error:] : 1532 -> 1500
CStrings:
+ "@20@0:8i16"
+ "buildWithScheme:"
- "@28@0:8i16Q20"
- "buildWithScheme:sectorSize:"

```
