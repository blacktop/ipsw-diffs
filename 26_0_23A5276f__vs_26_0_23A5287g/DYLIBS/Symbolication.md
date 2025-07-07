## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64572.120.2.0.0
-  __TEXT.__text: 0xac8e8
-  __TEXT.__auth_stubs: 0x21b0
-  __TEXT.__objc_methlist: 0x64f8
+64572.129.1.0.0
+  __TEXT.__text: 0xacffc
+  __TEXT.__auth_stubs: 0x21a0
+  __TEXT.__objc_methlist: 0x6508
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xfcb5
-  __TEXT.__gcc_except_tab: 0x4ea4
+  __TEXT.__cstring: 0xfca3
+  __TEXT.__gcc_except_tab: 0x4f18
   __TEXT.__oslogstring: 0x1642
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x2820
+  __TEXT.__unwind_info: 0x2870
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0xf329
-  __TEXT.__objc_methtype: 0x5dd8
-  __TEXT.__objc_stubs: 0x9900
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x3638
+  __TEXT.__objc_methname: 0xf364
+  __TEXT.__objc_methtype: 0x5e0c
+  __TEXT.__objc_stubs: 0x9920
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x3660
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3508
+  __DATA_CONST.__objc_selrefs: 0x3518
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x870
-  __AUTH_CONST.__auth_got: 0x10f0
+  __AUTH_CONST.__auth_got: 0x10e8
   __AUTH_CONST.__const: 0xb88
   __AUTH_CONST.__cfstring: 0xd7c0
-  __AUTH_CONST.__objc_const: 0xbb80
+  __AUTH_CONST.__objc_const: 0xbb60
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x3c0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc6c
+  __DATA.__objc_ivar: 0xc68
   __DATA.__data: 0xce8
   __DATA.__bss: 0x530
   __DATA.__common: 0xf9

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 58BA6985-0287-3252-9274-DB6C22DA401E
-  Functions: 3006
-  Symbols:   10355
-  CStrings:  7692
+  UUID: 247499E2-6D40-323F-9ECF-9E298C776590
+  Functions: 3011
+  Symbols:   10367
+  CStrings:  7696
 
Symbols:
+ -[VMUProcessDescription _extractInfoPlistFromSymbolOwner:withMemory:]
+ -[VMUProcessDescription _readDataFromMemory:atAddress:size:]
+ -[VMUProcessDescription targetUsesExtraPointerBits:]
+ -[VMUWiredMemoryInfo counterInfo]
+ GCC_except_table26
+ GCC_except_table60
+ ___69-[VMUProcessDescription _extractInfoPlistFromSymbolOwner:withMemory:]_block_invoke
+ ___Block_byref_object_copy_.65
+ ___Block_byref_object_dispose_.66
+ ___block_descriptor_56_ea8_32s40s48r_e22_v24?0{_CSTypeRef=QQ}8lr48l8s32l8s40l8
+ ___block_literal_global.117
+ ___block_literal_global.91
+ ___copy_assignment_8_8_t0w16_sb16_s24_s32_t40w16_w56_w64_w72
+ ___destructor_8_sb16_s24_s32_w56_w64_w72
+ ___remoteZoneIntrospection_block_invoke.89
+ _objc_msgSend$_extractInfoPlistFromSymbolOwner:withMemory:
+ _objc_msgSend$_readDataFromMemory:atAddress:size:
- -[VMUProcessDescription bundleIdentifier]
- -[VMUProcessDescription isAppleApplication]
- GCC_except_table45
- GCC_except_table52
- _OBJC_IVAR_$_VMUProcessDescription._lsApplicationInformation
- ___block_literal_global.114
- ___block_literal_global.94
- ___copy_assignment_8_8_t0w16_sb16_s24_s32_t40w16_w56_w64
- ___destructor_8_sb16_s24_s32_w56_w64
- ___remoteZoneIntrospection_block_invoke.92
- _kCFBundleIdentifierKey
- _kCFBundleVersionKey
- _mapped_memory_pointer_to_local_mapping_updated_with_extra_bits
- _objc_msgSend$bundleIdentifier
CStrings:
+ "1"
+ "@40@0:8@16Q24Q32"
+ "ProductBuildVersion"
+ "__TEXT __info_plist"
+ "_extractInfoPlistFromSymbolOwner:withMemory:"
+ "_readDataFromMemory:atAddress:size:"
+ "a\x93"
+ "counterInfo"
+ "has_sec_transition"
+ "targetUsesExtraPointerBits:"
+ "{_VMUSwiftRemoteMirrorReaderContext=\"symbolicator\"{_CSTypeRef=\"_opaque_1\"Q\"_opaque_2\"Q}\"memoryReader\"@?\"remoteAddressToLocalAddressAndSizeMap\"@\"NSMapTable\"\"remoteStringToLengthMap\"@\"NSMapTable\"\"needToValidateAddressRange\"B\"isExclaveCore\"B\"swiftRemoteMirrorMemoryReadsLogLevel\"i\"readBytesCallCount\"I\"getStringLengthCallCount\"I\"objectIdentifier\"@\"VMUObjectIdentifier\"\"scanner\"@\"VMUTaskMemoryScanner\"\"vmuTask\"@\"VMUTask\"}"
- "*** Symbolication:  malloc zone address %#llx is invalid\n"
- "_lsApplicationInformation"
- "a\x92"
- "bundleIdentifier"
- "invalid zone pointer"
- "isAppleApplication"
- "{_VMUSwiftRemoteMirrorReaderContext=\"symbolicator\"{_CSTypeRef=\"_opaque_1\"Q\"_opaque_2\"Q}\"memoryReader\"@?\"remoteAddressToLocalAddressAndSizeMap\"@\"NSMapTable\"\"remoteStringToLengthMap\"@\"NSMapTable\"\"needToValidateAddressRange\"B\"swiftRemoteMirrorMemoryReadsLogLevel\"i\"readBytesCallCount\"I\"getStringLengthCallCount\"I\"objectIdentifier\"@\"VMUObjectIdentifier\"\"scanner\"@\"VMUTaskMemoryScanner\"}"

```
