## footprint

> `/usr/bin/footprint`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`
- `__DATA.__common`

```diff

-360.0.0.0.0
-  __TEXT.__text: 0x1fae0
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0x124c
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x2d73
-  __TEXT.__objc_methname: 0x24d3
-  __TEXT.__objc_classname: 0x1db
-  __TEXT.__objc_methtype: 0x7f9
-  __TEXT.__gcc_except_tab: 0x444
+364.0.0.0.0
+  __TEXT.__text: 0x21314
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__objc_methlist: 0x131c
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x303f
+  __TEXT.__objc_classname: 0x1ea
+  __TEXT.__objc_methtype: 0x80c
+  __TEXT.__gcc_except_tab: 0x43c
+  __TEXT.__objc_methname: 0x25d4
   __TEXT.__ustring: 0xd0
   __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0x4a0
-  __DATA_CONST.__const: 0x708
-  __DATA_CONST.__cfstring: 0x1100
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__unwind_info: 0x4d0
+  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_got: 0x680
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x30b0
-  __DATA.__objc_selrefs: 0xa28
-  __DATA.__objc_ivar: 0x2b8
-  __DATA.__objc_data: 0x780
+  __DATA.__objc_const: 0x3200
+  __DATA.__objc_selrefs: 0xa78
+  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x250
-  __DATA.__bss: 0x48b8
+  __DATA.__bss: 0x48c8
   __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 434
-  Symbols:   1498
-  CStrings:  1069
+  Functions: 453
+  Symbols:   1556
+  CStrings:  1102
 
Symbols:
+ +[FPBootCarveout _loadBootStolenInfoLocked]
+ +[FPBootCarveout bootStolenSize]
+ +[FPBootCarveout isAvailable]
+ -[FPBootCarveout .cxx_destruct]
+ -[FPBootCarveout _canReuseInsteadOf:]
+ -[FPBootCarveout _gatherData:extendedInfoProvider:]
+ -[FPBootCarveout _isAlive]
+ -[FPBootCarveout _populateTask]
+ -[FPBootCarveout init]
+ -[FPBootCarveout memoryRegions]
+ -[FPBootCarveout setMemoryRegions:]
+ -[FPKernelProcess _gatherData:extendedInfoProvider:]
+ -[FPMemoryMultiRegion init]
+ -[FPMemoryObject hasSyntheticObjectID]
+ -[FPMemoryRegion adoptObjectIdentityFromMemoryObject:]
+ -[FPMemoryRegion hasSyntheticObjectID]
+ -[FPMemoryRegion setSyntheticObjectIDForPid:]
+ -[FPProcess _canReuseInsteadOf:]
+ -[FPProcess _gatherData:extendedInfoProvider:]
+ -[FPProcess canReuseInsteadOf:]
+ -[FPProcess isGathered]
+ -[FPUserProcess _canReuseInsteadOf:]
+ -[FPUserProcess _gatherData:extendedInfoProvider:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/27.arm64e.thinlto.o
+ FPBootCarveout.m
+ OBJC_IVAR_$_FPBootCarveout._memoryRegions
+ OBJC_IVAR_$_FPFootprint._cachedKernelProcess
+ OBJC_IVAR_$_FPFootprint._wireTagUniqueObjectsNextKey
+ OBJC_IVAR_$_FPFootprintArgs._includeBootCarveout
+ OBJC_IVAR_$_FPMemoryRegion._hasSyntheticObjectID
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperties
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _OBJC_CLASS_$_FPBootCarveout
+ _OBJC_METACLASS_$_FPBootCarveout
+ __OBJC_$_CLASS_METHODS_FPBootCarveout
+ __OBJC_$_CLASS_PROP_LIST_FPBootCarveout
+ __OBJC_$_INSTANCE_METHODS_FPBootCarveout
+ __OBJC_$_INSTANCE_VARIABLES_FPBootCarveout
+ __OBJC_CLASS_RO_$_FPBootCarveout
+ __OBJC_METACLASS_RO_$_FPBootCarveout
+ ___NSArray0__struct
+ ___block_descriptor_32_e43_q24?0"FPMemoryRegion"8"FPMemoryRegion"16l
+ _gRegionByStartAscSizeDesc_block_invoke
+ _kCFAllocatorDefault
+ _kDTKernelRegionNameCStr
+ _kIOMainPortDefault
+ _malloc_type_calloc
+ _objc_msgSend$_canReuseInsteadOf:
+ _objc_msgSend$_gatherData:extendedInfoProvider:
+ _objc_msgSend$bootStolenSize
+ _objc_msgSend$bytes
+ _objc_msgSend$canReuseInsteadOf:
+ _objc_msgSend$hasSyntheticObjectID
+ _objc_msgSend$isAvailable
+ _objc_msgSend$isGathered
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$setIs64bit:
+ _objc_msgSend$setPageSize:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$substringFromIndex:
+ _readDTValues
- +[FPSystemMem getBootCarveoutSize]
- -[FPFootprint _kernelProcess]
- -[FPFootprint _shouldEnableWireTagSharing]
- -[FPKernelProcess gatherData:extendedInfoProvider:]
- -[FPSystemMem init]
- -[FPUserProcess gatherData:extendedInfoProvider:]
- OBJC_IVAR_$_FPMemoryRegion._reserved
- OBJC_IVAR_$_FPSystemMem._bootCarveoutSize
- __OBJC_$_INSTANCE_VARIABLES_FPSystemMem
- _objc_msgSend$getBootCarveoutSize
CStrings:
+ "    --drainDeferredReclaim    drain deferred reclaim buffers before measuring (default varies by platform)\n    --noDrainDeferredReclaim  don't drain deferred reclaim buffers\n    --bootCarveout            show boot carveout memory breakdown\n"
+ "--bootCarveout is not available on this device"
+ "/%@"
+ "@\"FPKernelProcess\""
+ "Boot Carveout"
+ "Boot Carveout: BOOT_STOLEN tag unavailable from mach_memory_info; regions will not share with kernel_task"
+ "Boot Carveout: Kernel region not found in carveout-memory-map"
+ "Boot Carveout: Unable to open %s"
+ "Boot Carveout: Unable to read Kernel region from carveout-memory-map"
+ "Boot Carveout: Unable to read carveout-memory-map properties"
+ "Boot Carveout: Unable to read dram-base/dram-size from /chosen"
+ "FPBootCarveout"
+ "IODeviceTree:/chosen"
+ "IODeviceTree:/chosen/carveout-memory-map"
+ "TB,R"
+ "Unmanaged DRAM"
+ "_cachedKernelProcess"
+ "_canReuseInsteadOf:"
+ "_gatherData:extendedInfoProvider:"
+ "_hasSyntheticObjectID"
+ "_includeBootCarveout"
+ "_wireTagUniqueObjectsNextKey"
+ "bootCarveout"
+ "bootStolenSize"
+ "canReuseInsteadOf:"
+ "dram-base"
+ "dram-size"
+ "hasSyntheticObjectID"
+ "isAvailable"
+ "isGathered"
+ "q24@?0@\"FPMemoryRegion\"8@\"FPMemoryRegion\"16"
+ "region-%@"
+ "region-id-"
+ "region-name-id-"
+ "reverseObjectEnumerator"
+ "stringByAppendingFormat:"
+ "substringFromIndex:"
- "    --drainDeferredReclaim    drain deferred reclaim buffers before measuring (default varies by platform)\n    --noDrainDeferredReclaim  don't drain deferred reclaim buffers\n"
- "_bootCarveoutSize"
- "_reserved"
- "getBootCarveoutSize"
```
