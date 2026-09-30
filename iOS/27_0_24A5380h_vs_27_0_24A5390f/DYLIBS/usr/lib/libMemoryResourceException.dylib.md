## libMemoryResourceException.dylib

> `/usr/lib/libMemoryResourceException.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-360.0.0.0.0
-  __TEXT.__text: 0x1ac5c
-  __TEXT.__objc_methlist: 0x15fc
+364.0.0.0.0
+  __TEXT.__text: 0x1ad98
+  __TEXT.__objc_methlist: 0x167c
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x1b0c
+  __TEXT.__cstring: 0x1b16
   __TEXT.__oslogstring: 0xd18
-  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__ustring: 0xd0
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__unwind_info: 0x4c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x650
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf88
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_selrefs: 0xfc0
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__got: 0x290
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x1e00
-  __AUTH_CONST.__objc_const: 0x3090
+  __AUTH_CONST.__objc_const: 0x31c0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x290
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x800
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_ivar: 0xc
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x4101
+  __DATA_DIRTY.__bss: 0x4901
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 497
-  Symbols:   1643
+  Functions: 507
+  Symbols:   1668
   CStrings:  392
 
Symbols:
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
+ -[RMELogPath .cxx_destruct]
+ GCC_except_table30
+ _OBJC_CLASS_$_RMELogPath
+ _OBJC_IVAR_$_FPFootprint._wireTagUniqueObjectsNextKey
+ _OBJC_IVAR_$_FPMemoryRegion._hasSyntheticObjectID
+ _OBJC_IVAR_$_RMELogPath._fileCreationDate
+ _OBJC_IVAR_$_RMELogPath._filePath
+ _OBJC_METACLASS_$_RMELogPath
+ _RMEGetTimeOrderedLogPaths
+ __OBJC_$_INSTANCE_METHODS_RMELogPath
+ __OBJC_$_INSTANCE_VARIABLES_RMELogPath
+ __OBJC_CLASS_RO_$_RMELogPath
+ __OBJC_METACLASS_RO_$_RMELogPath
+ ___RMEGetTimeOrderedLogPaths_block_invoke
+ ___block_descriptor_32_e35_q24?0"RMELogPath"8"RMELogPath"16l
+ _objc_msgSend$_canReuseInsteadOf:
+ _objc_msgSend$_gatherData:extendedInfoProvider:
+ _objc_msgSend$hasSyntheticObjectID
+ _objc_msgSend$isGathered
+ _objc_msgSend$physFootprint
+ _objc_msgSend$setSyntheticObjectIDForPid:
- -[FPUserProcess gatherData:extendedInfoProvider:]
- GCC_except_table28
- _OBJC_IVAR_$_FPMemoryRegion._reserved
- _RMEGetTimeOrderedLogPathsMatchingPrefs
- ___RMEGetTimeOrderedLogPathsMatchingPrefs_block_invoke
- ___block_descriptor_32_e25_q24?0"NSURL"8"NSURL"16l
CStrings:
+ "q24@?0@\"RMELogPath\"8@\"RMELogPath\"16"
- "q24@?0@\"NSURL\"8@\"NSURL\"16"
```
