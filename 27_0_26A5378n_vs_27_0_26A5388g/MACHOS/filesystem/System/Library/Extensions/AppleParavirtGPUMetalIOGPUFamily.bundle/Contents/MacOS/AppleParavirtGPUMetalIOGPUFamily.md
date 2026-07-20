## AppleParavirtGPUMetalIOGPUFamily

> `/System/Library/Extensions/AppleParavirtGPUMetalIOGPUFamily.bundle/Contents/MacOS/AppleParavirtGPUMetalIOGPUFamily`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-71.0.8.0.0
-  __TEXT.__text: 0x28d04
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_stubs: 0x4180
-  __TEXT.__objc_methlist: 0x7ca0
-  __TEXT.__objc_methname: 0x10548
-  __TEXT.__objc_classname: 0x947
-  __TEXT.__objc_methtype: 0x982f
+71.0.12.0.0
+  __TEXT.__text: 0x2995c
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_methlist: 0x7d80
+  __TEXT.__objc_methname: 0x10728
+  __TEXT.__objc_classname: 0x96a
+  __TEXT.__objc_methtype: 0x986f
   __TEXT.__const: 0x1d1
   __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__cstring: 0x6192
-  __TEXT.__oslogstring: 0xbdb
-  __TEXT.__unwind_info: 0xc10
-  __DATA_CONST.__const: 0x258
+  __TEXT.__cstring: 0x623b
+  __TEXT.__oslogstring: 0xd18
+  __TEXT.__unwind_info: 0xc50
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__cfstring: 0x3c0
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0x1d0
-  __DATA.__objc_const: 0xc700
-  __DATA.__objc_selrefs: 0x3a80
-  __DATA.__objc_ivar: 0x338
-  __DATA.__objc_data: 0xb90
+  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x1e0
+  __DATA.__objc_const: 0xc8e8
+  __DATA.__objc_selrefs: 0x3ac8
+  __DATA.__objc_ivar: 0x350
+  __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x1680
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x2
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1450
-  Symbols:   199
-  CStrings:  3482
+  Functions: 1476
+  Symbols:   203
+  CStrings:  3505
 
Symbols:
+ _OBJC_CLASS_$_NSMapTable
+ __NSConcreteGlobalBlock
+ __dispatch_data_empty
+ _dispatch_once
CStrings:
+ "%s: wired heap residency declaration overflowed segment resource list; ICB execute may fault on host lazy-walk after VM restore"
+ "%s: wired heap residency declaration overflowed segment resource list; ICB host-resource info may fail to resolve migrated function bytecode"
+ "-[AppleParavirtComputeCommandEncoder _addICBFunctionResourceReferences]_block_invoke"
+ "-[AppleParavirtRenderCommandEncoder _addICBFunctionResourceReferences]_block_invoke"
+ "00:41:38"
+ "@\"AppleParavirtCommandBuffer\""
+ "@\"NSMapTable\""
+ "@48@0:8@16@24@32@40"
+ "AppleParavirtComputeCommandEncoder"
+ "Failed to allocate creation args"
+ "Failed to allocate wired descriptor buffer"
+ "Jul 11 2026"
+ "_addICBFunctionResourceReferences"
+ "_commandBuffer"
+ "_migratedVariantCache"
+ "_migratedVariantCacheLock"
+ "_registerKernelVariantWithLength:functionType:"
+ "_wiredDescriptorHeaps"
+ "_wired_descriptor_heaps_lock"
+ "addWiredHeapReferencesToCommandBuffer:"
+ "initMigratedFromVariant:device:functionType:"
+ "initWithCommandBuffer:descriptor:serializer:device:"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "migratedFunctionVariantForVariant:"
+ "newWiredDescriptorBuffer:"
+ "supportsNonPageAlignedIOSurfacesSpanningPages"
- "21:04:13"
- "Jun 30 2026"
- "descbuffer.contents is null"
```
