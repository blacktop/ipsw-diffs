## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1245.1.0.0.0
-  __TEXT.__text: 0x250b0
+1284.1.1.0.0
+  __TEXT.__text: 0x27e80
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__const: 0x5f0
-  __TEXT.__cstring: 0x3fb4
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x14f8
+  __TEXT.__const: 0x680
+  __TEXT.__cstring: 0x490d
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x14a8
+  __DATA_CONST.__helper: 0x8
   __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x14d8
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x1860
   __AUTH.__data: 0x8
-  __DATA.__data: 0xf8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1030
-  __DATA.__common: 0x1
+  __DATA.__data: 0xf8
+  __DATA.__common: 0x19
+  __DATA.__bss: 0x1098
   __DATA_DIRTY.__common: 0x20
-  __TPRO_CONST.__dyld4: 0x48
+  __TPRO_CONST.__dyld_apis: 0x8
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 996
-  Symbols:   1287
-  CStrings:  510
+  Functions: 1081
+  Symbols:   1409
+  CStrings:  544
 
Symbols:
+ __dyld_for_each_prewarming_range
+ __dyld_stack_bottom
+ __dyld_stack_range
+ __dyld_stack_top
+ _basename
+ _macho_source_version
+ _malloc_type_aligned_alloc
+ _malloc_type_calloc
- __dyld_missing_symbol_abort
- _mach_vm_map
- _os_unfair_lock_assert_not_owner
- _os_unfair_lock_assert_owner
- _vm_page_mask
CStrings:
+ "!fixup.isBind && \"firmware format does not support binds\""
+ "!fixup.isBind && \"shared cache does not support binds\""
+ "!sMemoryManagerInitialized"
+ "(null)"
+ "/System/Cryptexes/ExclaveOS/System/ExclaveKit/System/Library/dyld/"
+ "/System/DriverKit/usr/lib/libSystem.B.dylib"
+ "/System/ExclaveKit/System/Library/dyld/"
+ "/System/ExclaveKit/usr/lib/libSystem.dylib"
+ "/System/Library/PrivateFrameworks/Dyld.framework/Dyld"
+ "/usr/lib/libSystem.B.dylib"
+ "Bad dyld_proces_info image info for\n\tplatform: %u\n\taddress = 0x%llx\n\tpath = %s\n"
+ "Bitmap.h"
+ "ChainedFixups.cpp"
+ "DTServiceHub"
+ "DYLD_CHAINED_PTR_ARM64E_SEGMENTED"
+ "FunctionVariants is too small"
+ "FunctionVariants tableCount=%u is too large for size=%lu"
+ "PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE"
+ "ReportCrash"
+ "_dyld_legacy_introspection_vtable"
+ "arm64e shared cache, 8-byte stride, target vmoffset"
+ "arm64e.kernel.v1"
+ "arm64e.kernel.v2"
+ "armv6"
+ "authBind24Ptr->next*stride() == delta"
+ "authBind24Ptr->ordinal == fixup.bind.bindOrdinal"
+ "authBindPtr->next*stride() == delta"
+ "authBindPtr->ordinal == fixup.bind.bindOrdinal"
+ "authRebasePtr->next*8 == delta"
+ "authRebasePtr->next*stride() == delta"
+ "authRebasePtr->runtimeOffset == fixup.rebase.targetVmOffset"
+ "authRebasePtr->target == fixup.rebase.targetVmOffset"
+ "authRebasePtr->targetSegIndex == segIndex"
+ "authRebasePtr->targetSegOffset == segOffset"
+ "authenticated arm64e, 8-byte stride, target segIndex/offset8"
+ "bind24Ptr->next*stride() == delta"
+ "bind24Ptr->ordinal == fixup.bind.bindOrdinal"
+ "bindPtr->addend == fixup.bind.embeddedAddend"
+ "bindPtr->next*4 == delta"
+ "bindPtr->next*stride() == delta"
+ "bindPtr->ordinal == fixup.bind.bindOrdinal"
+ "bit < _size"
+ "chained fixups, unknown pointer_format (%d)"
+ "checkBit"
+ "com.apple.dt.instruments.dtsecurity"
+ "dyld cache thread-local format too old"
+ "entry %d extends to 0x%08X which beyond total size 0x%08lX"
+ "file is too small (length=%llu)"
+ "fixup.bind.embeddedAddend == 0"
+ "found && \"target vm address not in any segment\""
+ "future"
+ "init"
+ "initializer 0x%08lX is not in an executable segment"
+ "initializer offsets section %.*s/%.*s has bad size"
+ "initializer offsets section %.*s/%.*s is not 4-byte aligned"
+ "initializer offsets section %.*s/%.*s must be in read-only segment"
+ "invalid FunctionVariantsRuntimeTable length %lu for count=%u"
+ "last entry in FunctionVariantsRuntimeTable entries is not 'default'"
+ "load command #%d LC_FUNCTION_VARIANTS size wrong"
+ "load command #%d LC_FUNCTION_VARIANT_FIXUPS size wrong"
+ "load commands do not fit in __TEXT segment filesize"
+ "load commands do not fit in __TEXT segment vmsize"
+ "malformed thread-local, offset=0x%lX is larger than total size=0x%lX"
+ "memoryManager"
+ "pthread_key_create() failed"
+ "rebasePtr->next == delta"
+ "rebasePtr->next*4 == delta"
+ "rebasePtr->next*8 == delta"
+ "rebasePtr->next*stride() == delta"
+ "rebasePtr->target == (low56 + (this->unauthRebaseIsVmAddr() ? preferedLoadAddress : 0))"
+ "rebasePtr->target == (low56+preferedLoadAddress)"
+ "rebasePtr->target == fixup.rebase.targetVmOffset"
+ "rebasePtr->target == low56"
+ "rebasePtr->target == target"
+ "rebasePtr->targetSegIndex == segIndex"
+ "rebasePtr->targetSegOffset == segOffset"
+ "riscv32"
+ "sMemoryManagerInitialized"
+ "section %.*s/%.*s address (0x%llX) is not pointer aligned"
+ "section %.*s/%.*s size (%llu) is not a multiple of pointer-size"
+ "signExtendedAddend(bind24Ptr) == fixup.bind.embeddedAddend"
+ "signExtendedAddend(bindPtr) == fixup.bind.embeddedAddend"
+ "size (%llu) of thread-locals section %.*s is not a multiple of %lu"
+ "tableOffsets[%d]=0x%08X which is > total size 0x%08lX"
+ "terminators section %.*s/%.*s not supported for arm64e"
+ "thread locals not initialized"
+ "thread_key_t %lu, larger than uint32_t"
+ "thumbv7"
+ "thumbv7em"
+ "thumbv7k"
+ "thumbv7m"
+ "thumbv7s"
+ "trace"
+ "trace_internal"
+ "unknown FunctionVariantsRuntimeTable::Kind (%d)"
+ "unsupported thread-local, larger than 4GB"
+ "unwrapCompactInfo"
+ "v16@?0^{TerminatorList=^{TerminatorList}Q[7{Terminator=^?^v}]}8"
+ "v24@?0r^{DyldSharedCache={dyld_cache_header=[16c]IIIIQQQQQQQ[16C]QIIQQQQQQQQQQQQIb8b1b1b1b1b1b19QQQQQQQQQQQIIQQQQQIIIIQQII[16C]QQQQIIIQQQQQQIIQQQQ}}8^B16"
+ "v32@?0{Platform=^{PlatformInfo}I}8{Version32=I}24{Version32=I}28"
+ "v37@?0r*8{LinkedDylibAttributes=(?={?=b1b1b1b1b4}C)}16{Version32=I}17{Version32=I}21B25^B29"
+ "v40@?0{PlatformAndVersions={Platform=^{PlatformInfo}I}{Version32=I}{Version32=I}{Version32=I}{Version32=I}}8"
+ "writeChainEntry"
+ "{Error=^v}24@?0{span<dyld::ThreadLocalVariables::Thunk, 18446744073709551615UL>=^{Thunk}Q}8"
- "\n\tRequested allgnment: 0x"
- "\n\tRequested size: 0x"
- "\n\tRequested target allgnment: 0x"
- "\n\tRequested target size: 0x"
- "\n\tkern return: 0x"
- "!allocated()"
- "%s"
- "(uint64_t)result != (uint64_t)this"
- "0 && \"vm_allocate failed\""
- "AllocationMetadata"
- "Could not vm_allocate 0x"
- "Pool"
- "__compact_unwind"
- "__gcc_except_tab"
- "__objc_arraydata"
- "__objc_classlist"
- "__objc_classname"
- "__objc_classrefs"
- "__objc_databytes"
- "__objc_doubleobj"
- "__objc_imageinfo"
- "__objc_init_offs"
- "__objc_nlcatlist"
- "__objc_nlclslist"
- "__objc_protolist"
- "__objc_protorefs"
- "__objc_superrefs"
- "__os_assumes_log"
- "__swift5_acfuncs"
- "__swift5_assocty"
- "__swift5_builtin"
- "__swift5_capture"
- "__swift5_fieldmd"
- "__swift5_reflstr"
- "__swift5_typeref"
- "_lastFreeMetadata->pool() == this"
- "aligned_alloc_best_fit"
- "allocated()"
- "armv8m"
- "buffer != nullptr"
- "consumeSpace"
- "consumedSpace <= size"
- "deallocate"
- "file is too short"
- "free()"
- "initializer offsets section %s/%s has bad size"
- "initializer offsets section %s/%s is not 4-byte aligned"
- "initializer offsets section %s/%s must be in read-only segment"
- "load commands do not fit in __TEXT segment"
- "markAllocated"
- "pool"
- "region.contains(freeRegion)"
- "reserve"
- "result"
- "section %s/%s address (0x%llX) is not pointer aligned"
- "section %s/%s size (%llu) is not a multiple of pointer-size"
- "setPoolHint"
- "size != 0"
- "stackAllocatorInternal"
- "swift5_backtrace"
- "terminators section %s/%s not supported for arm64e"
- "v16@?0r^{Buffer=^vQ}8"
- "v20@?0i8I12I16"
- "v24@?0r^{DyldSharedCache={dyld_cache_header=[16c]IIIIQQQQQQQ[16C]QIIQQQQQQQQQQQQIb8b1b1b1b1b20QQQQQQQQQQQIIQQQQQIIIIQQII[16C]QQQQIIIQQQQQQII}}8^B16"
- "v24@?0r^{SegmentInfo=QQQQQ*IIb1b1b1b1b12b16}8^B16"
- "v24@?0{Platform=^{PlatformInfo}}8{Version32=I}16{Version32=I}20"
- "v28@?0r^{SectionInfo={SegmentInfo=QQQQQ*IIb1b1b1b1b12b16}QQ*IIIII}8B16^B20"
- "v32@?0{PlatformAndVersions={Platform=^{PlatformInfo}}{Version32=I}{Version32=I}{Version32=I}{Version32=I}}8"
- "v33@?0r*8{LinkedDylibAttributes=(?={?=b1b1b1b1b4}C)}16{Version32=I}17{Version32=I}21^B25"
- "vm_allocate_bytes"

```
