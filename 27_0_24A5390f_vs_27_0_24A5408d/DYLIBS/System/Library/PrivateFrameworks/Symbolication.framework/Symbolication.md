## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-64578.92.1.0.0
-  __TEXT.__text: 0xbb97c
-  __TEXT.__objc_methlist: 0x69f0
+64578.100.1.0.0
+  __TEXT.__text: 0xbc230
+  __TEXT.__objc_methlist: 0x6a00
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x5884
-  __TEXT.__cstring: 0x11288
+  __TEXT.__gcc_except_tab: 0x596c
+  __TEXT.__cstring: 0x11308
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2da0
+  __TEXT.__unwind_info: 0x2db8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ee8
+  __DATA_CONST.__const: 0x3f38
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x39f8
+  __DATA_CONST.__objc_selrefs: 0x39f0
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x8f8
   __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x12f8
-  __AUTH_CONST.__cfstring: 0xdae0
-  __AUTH_CONST.__objc_const: 0xcb80
+  __AUTH_CONST.__cfstring: 0xdba0
+  __AUTH_CONST.__objc_const: 0xcc20
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x10d8
+  __AUTH_CONST.__auth_got: 0x10e8
   __AUTH.__objc_data: 0x680
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xd9c
+  __DATA.__objc_ivar: 0xdac
   __DATA.__data: 0xd18
   __DATA.__bss: 0x610
   __DATA.__common: 0x101

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3375
-  Symbols:   7485
-  CStrings:  2899
+  Functions: 3381
+  Symbols:   7500
+  CStrings:  2906
 
Symbols:
+ -[VMUProcessDescription hasRootsPresent]
+ -[VMUProcessDescription setHasRootsPresent:]
+ -[VMUProcessDescription usesMTE]
+ -[VMUProcessObjectGraph hasRootsPresent]
+ -[VMUProcessObjectGraph setHasRootsPresent:]
+ -[VMUTask stripMTEPointer:]
+ -[VMUTask useMTEPointerStripping]
+ -[VMUTaskMemoryCache isExclaveCore]
+ GCC_except_table61
+ OBJC_IVAR_$_VMUVMRegion.is_mte_enabled
+ _OBJC_IVAR_$_VMUProcessDescription._dscInstallNames
+ _OBJC_IVAR_$_VMUProcessDescription._hasRootsPresent
+ _OBJC_IVAR_$_VMUProcessObjectGraph._hasRootsPresent
+ _OBJC_IVAR_$_VMUTask._targetUsesMTE
+ _OBJC_IVAR_$_VMUTask._targetUsesMTEInitialized
+ _OBJC_IVAR_$_VMUTaskMemoryScanner._hasRootsPresent
+ __ZZ32-[VMUProcessDescription usesMTE]E41osSecurityConfigGetForTaskFunctionPointer
+ __ZZ32-[VMUProcessDescription usesMTE]E9onceToken
+ ___32-[VMUProcessDescription usesMTE]_block_invoke
+ ___68-[VMUProcessDescription initWithVMUTaskMemoryCache:getBinariesList:]_block_invoke_4
+ ____variantForSwiftClass_block_invoke_7
+ ___block_descriptor_40_ea8_32s_e23_v16?0^{dyld_image_s=}8ls32l8
+ ___block_descriptor_56_e8_32r40r48w_e29_v32?0"VMUFieldInfo"8Q16^B24lw48l8r32l8r40l8
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
- OBJC_IVAR_$_VMUVMRegion.is_extra_bits
- _OBJC_IVAR_$_VMUTask._targetUsesExtraBits
- _OBJC_IVAR_$_VMUTask._targetUsesExtraBitsInitialized
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
