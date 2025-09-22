## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64572.137.1.0.0
-  __TEXT.__text: 0xb0b74
+64572.146.1.0.0
+  __TEXT.__text: 0xb0f30
   __TEXT.__auth_stubs: 0x2410
   __TEXT.__objc_methlist: 0x65d8
   __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0xffe8
+  __TEXT.__cstring: 0x10048
   __TEXT.__gcc_except_tab: 0x4ed8
   __TEXT.__oslogstring: 0x17ac
   __TEXT.__ustring: 0x24

   __TEXT.__swift5_types: 0x14
   __TEXT.__unwind_info: 0x2948
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0xf48f
+  __TEXT.__objc_methname: 0xf51d
   __TEXT.__objc_methtype: 0x5e83
   __TEXT.__objc_stubs: 0x9a20
   __DATA_CONST.__got: 0x458

   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0x1220
   __AUTH_CONST.__const: 0x11f8
-  __AUTH_CONST.__cfstring: 0xd8a0
-  __AUTH_CONST.__objc_const: 0xbd38
+  __AUTH_CONST.__cfstring: 0xd8c0
+  __AUTH_CONST.__objc_const: 0xbdb8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18

   __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc78
+  __DATA.__objc_ivar: 0xc88
   __DATA.__data: 0xd58
   __DATA.__bss: 0x558
   __DATA.__common: 0xf9

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0050EDE5-4EA5-342B-9A8F-6E2EDAAF22EE
-  Functions: 3126
-  Symbols:   10552
-  CStrings:  7753
+  UUID: AA84FDAD-0E76-3AAA-81B2-435C5808081C
+  Functions: 3127
+  Symbols:   10558
+  CStrings:  7761
 
Symbols:
+ -[VMUTaskMemoryScanner _recordFakeRootRefsForMallocBlock:indexInSwiftTaskAllocationBlockIndexes:recorder:]
+ GCC_except_table154
+ _OBJC_IVAR_$_VMUTaskMemoryScanner._swiftTaskAllocationBlockIndexes
+ _OBJC_IVAR_$_VMUTaskMemoryScanner._swiftTaskAllocationBlockIndexesCount
+ _OBJC_IVAR_$_VMUTaskMemoryScanner._swiftTaskAllocationBlockIndexesSize
+ _OBJC_IVAR_$_VMUTaskMemoryScanner._swiftTaskAllocationsFakeRootNode
+ ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.310
+ ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.337
+ ___block_literal_global.183
+ ___block_literal_global.209
+ ___block_literal_global.234
+ ___block_literal_global.256
+ ___block_literal_global.280
- GCC_except_table124
- GCC_except_table153
- ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.301
- ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.328
- ___block_literal_global.178
- ___block_literal_global.204
- ___block_literal_global.229
- ___block_literal_global.251
- ___block_literal_global.274
Functions:
~ -[VMUTaskMemoryScanner dealloc] : 532 -> 548
~ -[VMUTaskMemoryScanner _addSpecialNodesFromTask] : 1288 -> 1696
~ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs] : 1056 -> 1208
~ ___78-[VMUTaskMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:scanCaches:]_block_invoke : 328 -> 380
~ ___55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2 : 3316 -> 2172
~ -[VMUTaskMemoryScanner processSnapshotGraphWithOptions:] : 3708 -> 3712
~ -[VMUObjectIdentifier _isaPointerRefersToVTable:remoteAddress:symbol:symbolNameOut:] : 352 -> 356
~ -[VMUProcessObjectGraph archiveDictionaryRepresentation:options:] : 5736 -> 5784
+ -[VMUTaskMemoryScanner _recordFakeRootRefsForMallocBlock:indexInSwiftTaskAllocationBlockIndexes:recorder:]
CStrings:
+ "SYMBOLICATION_DISABLE_FALSE_TASK_LEAKS_WORKAROUND"
+ "Swift Task Owned"
+ "_swiftTaskAllocationBlockIndexes"
+ "_swiftTaskAllocationBlockIndexesCount"
+ "_swiftTaskAllocationBlockIndexesSize"
+ "_swiftTaskAllocationsFakeRootNode"

```
