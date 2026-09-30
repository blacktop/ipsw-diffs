## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/Versions/A/IOGPU`

```diff

-162.11.0.0.0
-  __TEXT.__text: 0x2bd10
-  __TEXT.__objc_methlist: 0x537c
+162.13.0.0.0
+  __TEXT.__text: 0x2bcf8
+  __TEXT.__objc_methlist: 0x5384
   __TEXT.__cstring: 0x6309
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x414
   __TEXT.__oslogstring: 0x8db
-  __TEXT.__unwind_info: 0x1530
+  __TEXT.__unwind_info: 0x1528
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x438
   __AUTH_CONST.__const: 0x8c0
   __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x84c8
+  __AUTH_CONST.__objc_const: 0x84e8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x720
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x3dc
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0x7f0
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x88

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1558
-  Symbols:   2887
+  Symbols:   2888
   CStrings:  650
 
Symbols:
+ -[IOGPUMetal4CommandAllocator getCommandBufferStorage:retainReferences:generation:]
+ -[IOGPUMetal4CommandBuffer allocatorGeneration]
+ OBJC_IVAR_$_IOGPUMetal4CommandBuffer._allocatorGeneration
+ _objc_msgSend$allocatorGeneration
+ _objc_msgSend$getCommandBufferStorage:retainReferences:generation:
- -[IOGPUMetal4CommandAllocator getCommandBufferStorage:retainReferences:]
- -[IOGPUMetal4CommandAllocator getGeneration]
- _objc_msgSend$getCommandBufferStorage:retainReferences:
- _objc_msgSend$getGeneration
```
