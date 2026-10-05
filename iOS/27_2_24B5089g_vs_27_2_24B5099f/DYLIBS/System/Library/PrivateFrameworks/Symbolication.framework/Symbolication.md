## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64578.100.1.0.0
-  __TEXT.__text: 0xb9504
-  __TEXT.__objc_methlist: 0x6a00
+64578.132.1.0.0
+  __TEXT.__text: 0xb9a6c
+  __TEXT.__objc_methlist: 0x6a38
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x5990
-  __TEXT.__cstring: 0x11308
+  __TEXT.__gcc_except_tab: 0x59a8
+  __TEXT.__cstring: 0x113f8
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x3478
+  __TEXT.__unwind_info: 0x3488
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x39f0
+  __DATA_CONST.__objc_selrefs: 0x3a10
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x8f8
   __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x12f8
-  __AUTH_CONST.__cfstring: 0xdbc0
-  __AUTH_CONST.__objc_const: 0xcc20
+  __AUTH_CONST.__cfstring: 0xdc20
+  __AUTH_CONST.__objc_const: 0xcc80
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x10e8
-  __AUTH.__objc_data: 0x680
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xdac
-  __DATA.__data: 0xd18
+  __DATA.__objc_ivar: 0xdb4
+  __DATA.__data: 0x80
   __DATA.__common: 0x101
-  __DATA_DIRTY.__objc_data: 0x17c0
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__objc_data: 0x1e40
+  __DATA_DIRTY.__data: 0xce8
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3381
-  Symbols:   6147
-  CStrings:  2907
+  Functions: 3387
+  Symbols:   6156
+  CStrings:  2912
 
Symbols:
+ -[VMUObjectIdentifier libswiftCoreSymbolOwner]
+ -[VMUTask isSimulator]
+ -[VMUTaskMemoryScanner _attemptIdentifySwiftMetadataBlocks]
+ -[VMUTaskMemoryScanner _generateMetadataClassInfoIsaIndexes]
+ -[VMUTaskMemoryScanner _nodeIsPossibleSwiftMetadataHeapBlock:]
+ GCC_except_table123
+ GCC_except_table131
+ GCC_except_table147
+ GCC_except_table161
+ _OBJC_IVAR_$_VMUObjectIdentifier._libswiftCoreSymbolOwner
+ _OBJC_IVAR_$_VMUTaskMemoryScanner._mslLiteZoneIndex
+ _VMUIsTaskSimulator
- GCC_except_table144
- GCC_except_table158
- GCC_except_table86
CStrings:
+ "Could not get current swift metadata allocation pool"
+ "Could not get node for swift metadata allocation pool"
+ "Could not read swift metadata block back pointer"
+ "__swift_debug_allocationPoolBackPointerOffset"
+ "__swift_debug_allocationPoolPointer"
+ "qb"
- "Qb"
```
