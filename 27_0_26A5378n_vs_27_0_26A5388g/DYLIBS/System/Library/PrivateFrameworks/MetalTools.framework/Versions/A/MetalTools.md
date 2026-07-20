## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/Versions/A/MetalTools`

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
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-382.4.0.0.0
-  __TEXT.__text: 0x14ef08
+382.5.0.0.0
+  __TEXT.__text: 0x14f154
   __TEXT.__objc_methlist: 0x1b29c
   __TEXT.__gcc_except_tab: 0x32e8
-  __TEXT.__cstring: 0x361a2
+  __TEXT.__cstring: 0x36409
   __TEXT.__const: 0x5b0
   __TEXT.__oslogstring: 0x28d1
   __TEXT.__unwind_info: 0x5938

   __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x6e08
+  __DATA_CONST.__objc_selrefs: 0x6e10
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__got: 0xbe0
   __AUTH_CONST.__const: 0x1150
-  __AUTH_CONST.__cfstring: 0xfb80
+  __AUTH_CONST.__cfstring: 0xfc40
   __AUTH_CONST.__objc_const: 0x4b350
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x650

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 8406
-  Symbols:   15513
-  CStrings:  3741
+  Symbols:   15515
+  CStrings:  3747
 
Symbols:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$usedInternalResidencySets
Functions:
~ -[MTL4GPUDebugComputeCommandEncoder performDeepResidencyCheckWithDescriptor:commandInfo:] : 1600 -> 1612
~ -[MTLGPUDebugBuffer dealloc] : 244 -> 280
~ -[MTLDebugCommandBuffer preCommit] : 980 -> 1108
~ -[MTL4DebugCommandQueue validateCommitCommon:commandBuffers:count:] : 1444 -> 1856
CStrings:
+ "The command buffer (at index %lu) requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
+ "The command buffer (at index %lu) requires %lu residency sets which exceeds the maximum (%lu)."
+ "The command buffer requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
+ "The command buffer requires %lu residency sets which exceeds the maximum (%lu)."
+ "The command buffers (from index %lu to index %lu) require %lu Metal internal residency sets which exceeds the maximum (%lu)."
+ "The command buffers (from index %lu to index %lu) require %lu residency sets which exceeds the maximum (%lu)."
```
