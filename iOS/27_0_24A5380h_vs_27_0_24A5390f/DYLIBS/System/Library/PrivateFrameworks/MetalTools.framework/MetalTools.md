## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-382.4.0.0.0
-  __TEXT.__text: 0x146170
+382.5.0.0.0
+  __TEXT.__text: 0x1463ac
   __TEXT.__objc_methlist: 0x1a71c
   __TEXT.__gcc_except_tab: 0x32ec
-  __TEXT.__cstring: 0x35270
+  __TEXT.__cstring: 0x354d7
   __TEXT.__const: 0x5a0
   __TEXT.__oslogstring: 0x28d1
   __TEXT.__unwind_info: 0x5770

   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x6ac0
+  __DATA_CONST.__objc_selrefs: 0x6ac8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0xf640
+  __AUTH_CONST.__cfstring: 0xf700
   __AUTH_CONST.__objc_const: 0x490c8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x6d0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 8190
-  Symbols:   15109
-  CStrings:  3680
+  Symbols:   15111
+  CStrings:  3686
 
Symbols:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$usedInternalResidencySets
Functions:
~ -[MTL4GPUDebugComputeCommandEncoder performDeepResidencyCheckWithDescriptor:commandInfo:] : 1592 -> 1604
~ -[MTLGPUDebugBuffer dealloc] : 244 -> 280
~ -[MTLDebugCommandBuffer preCommit] : 932 -> 1060
~ -[MTL4DebugCommandQueue validateCommitCommon:commandBuffers:count:] : 1396 -> 1792
CStrings:
+ "The command buffer (at index %lu) requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
+ "The command buffer (at index %lu) requires %lu residency sets which exceeds the maximum (%lu)."
+ "The command buffer requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
+ "The command buffer requires %lu residency sets which exceeds the maximum (%lu)."
+ "The command buffers (from index %lu to index %lu) require %lu Metal internal residency sets which exceeds the maximum (%lu)."
+ "The command buffers (from index %lu to index %lu) require %lu residency sets which exceeds the maximum (%lu)."
```
