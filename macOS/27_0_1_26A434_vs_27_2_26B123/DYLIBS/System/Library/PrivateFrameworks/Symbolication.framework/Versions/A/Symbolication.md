## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication`

```diff

-64578.100.1.0.0
-  __TEXT.__text: 0xc6568
-  __TEXT.__objc_methlist: 0x6c40
+64578.132.1.0.0
+  __TEXT.__text: 0xc6ba8
+  __TEXT.__objc_methlist: 0x6c78
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x5cbc
-  __TEXT.__cstring: 0x11838
+  __TEXT.__gcc_except_tab: 0x5cd4
+  __TEXT.__cstring: 0x11928
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2eb0
+  __TEXT.__unwind_info: 0x2eb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x3b50
+  __DATA_CONST.__objc_selrefs: 0x3b70
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x8f8
   __DATA_CONST.__got: 0x4d0
   __AUTH_CONST.__const: 0x4bc0
-  __AUTH_CONST.__cfstring: 0xdfa0
-  __AUTH_CONST.__objc_const: 0xd158
+  __AUTH_CONST.__cfstring: 0xe000
+  __AUTH_CONST.__objc_const: 0xd1b8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0xf88
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH.__objc_data: 0xe0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xdd0
-  __DATA.__data: 0xd80
+  __DATA.__objc_ivar: 0xdd8
+  __DATA.__data: 0xe8
   __DATA.__bss: 0x4b8
   __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_data: 0x1ef0
-  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__objc_data: 0x1fd0
+  __DATA_DIRTY.__data: 0xcf0
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0xc0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3512
-  Symbols:   7699
-  CStrings:  2955
+  Functions: 3518
+  Symbols:   7712
+  CStrings:  2960
 
Symbols:
+ -[VMUObjectIdentifier libswiftCoreSymbolOwner]
+ -[VMUTask isSimulator]
+ -[VMUTaskMemoryScanner _attemptIdentifySwiftMetadataBlocks]
+ -[VMUTaskMemoryScanner _generateMetadataClassInfoIsaIndexes]
+ -[VMUTaskMemoryScanner _nodeIsPossibleSwiftMetadataHeapBlock:]
+ GCC_except_table105
+ GCC_except_table136
+ GCC_except_table154
+ GCC_except_table172
+ GCC_except_table187
+ OBJC_IVAR_$_VMUObjectIdentifier._libswiftCoreSymbolOwner
+ OBJC_IVAR_$_VMUTaskMemoryScanner._mslLiteZoneIndex
+ _VMUIsTaskSimulator
+ _objc_msgSend$_attemptIdentifySwiftMetadataBlocks
+ _objc_msgSend$_generateMetadataClassInfoIsaIndexes
+ _objc_msgSend$_nodeIsPossibleSwiftMetadataHeapBlock:
+ _objc_msgSend$libswiftCoreSymbolOwner
- GCC_except_table141
- GCC_except_table151
- GCC_except_table169
- GCC_except_table184
CStrings:
+ "Could not get current swift metadata allocation pool"
+ "Could not get node for swift metadata allocation pool"
+ "Could not read swift metadata block back pointer"
+ "__swift_debug_allocationPoolBackPointerOffset"
+ "__swift_debug_allocationPoolPointer"
+ "qb"
- "Qb"
```
