## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication`

```diff

-64578.92.1.0.0
-  __TEXT.__text: 0xc5ae8
-  __TEXT.__objc_methlist: 0x6c30
+64578.100.1.0.0
+  __TEXT.__text: 0xc64d8
+  __TEXT.__objc_methlist: 0x6c40
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x5bb4
-  __TEXT.__cstring: 0x117b8
+  __TEXT.__gcc_except_tab: 0x5c98
+  __TEXT.__cstring: 0x11838
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2e90
+  __TEXT.__unwind_info: 0x2ea8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x3b58
+  __DATA_CONST.__objc_selrefs: 0x3b50
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x8f8
   __DATA_CONST.__got: 0x4d0
-  __AUTH_CONST.__const: 0x4b60
-  __AUTH_CONST.__cfstring: 0xdec0
-  __AUTH_CONST.__objc_const: 0xd0b8
+  __AUTH_CONST.__const: 0x4bc0
+  __AUTH_CONST.__cfstring: 0xdf80
+  __AUTH_CONST.__objc_const: 0xd158
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH_CONST.__auth_got: 0xf88
   __AUTH.__objc_data: 0xe0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xdc0
+  __DATA.__objc_ivar: 0xdd0
   __DATA.__data: 0xd80
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x4b8
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x1ef0
   __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3501
-  Symbols:   7683
-  CStrings:  2947
+  Functions: 3509
+  Symbols:   7697
+  CStrings:  2954
 
Symbols:
+ -[VMUProcessDescription hasRootsPresent]
+ -[VMUProcessDescription setHasRootsPresent:]
+ -[VMUProcessDescription usesMTE]
+ -[VMUProcessObjectGraph hasRootsPresent]
+ -[VMUProcessObjectGraph setHasRootsPresent:]
+ -[VMUTask stripMTEPointer:]
+ -[VMUTask useMTEPointerStripping]
+ -[VMUTaskMemoryCache isExclaveCore]
+ GCC_except_table65
+ OBJC_IVAR_$_VMUProcessDescription._dscInstallNames
+ OBJC_IVAR_$_VMUProcessDescription._hasRootsPresent
+ OBJC_IVAR_$_VMUProcessObjectGraph._hasRootsPresent
+ OBJC_IVAR_$_VMUTask._targetUsesMTE
+ OBJC_IVAR_$_VMUTask._targetUsesMTEInitialized
+ OBJC_IVAR_$_VMUTaskMemoryScanner._hasRootsPresent
+ OBJC_IVAR_$_VMUVMRegion.is_mte_enabled
+ __ZZ32-[VMUProcessDescription usesMTE]E41osSecurityConfigGetForTaskFunctionPointer
+ __ZZ32-[VMUProcessDescription usesMTE]E9onceToken
+ ___32-[VMUProcessDescription usesMTE]_block_invoke
+ ___block_descriptor_40_ea8_32s_e23_v16?0^{dyld_image_s=}8l
+ ___block_descriptor_56_e8_32r40r48w_e29_v32?0"VMUFieldInfo"8Q16^B24l
+ ___copy_helper_block_e8_32r40r48w
+ ___destroy_helper_block_e8_32r40r48w
+ _dyld_image_get_installname
+ _dyld_shared_cache_for_each_image
+ _objc_msgSend$hasRootsPresent
+ _objc_msgSend$setHasRootsPresent:
+ _objc_msgSend$usesMTE
- -[VMUProcessDescription targetUsesExtraPointerBits:]
- -[VMUTask stripExtraPointerBits:]
- -[VMUTask useExtraPointerStripping]
- -[VMUVMRegion isExtraBits]
- -[VMUVMRegion isJIT]
- -[VMUVMRegion isTPRO]
- GCC_except_table61
- OBJC_IVAR_$_VMUTask._targetUsesExtraBits
- OBJC_IVAR_$_VMUTask._targetUsesExtraBitsInitialized
- OBJC_IVAR_$_VMUVMRegion.is_extra_bits
- __ZZ52-[VMUProcessDescription targetUsesExtraPointerBits:]E41osSecurityConfigGetForTaskFunctionPointer
- __ZZ52-[VMUProcessDescription targetUsesExtraPointerBits:]E9onceToken
- ___52-[VMUProcessDescription targetUsesExtraPointerBits:]_block_invoke
- _objc_msgSend$targetUsesExtraPointerBits:
CStrings:
+ " (MTE Enabled"
+ " (Roots Present)"
+ ", Roots Present"
+ "PropertyList.Element"
+ "PropertyList.Element Storage"
+ "buf"
+ "hasRootsPresent"
+ "v16@?0^{dyld_image_s=}8"
- " (MTE Enabled)"
```
