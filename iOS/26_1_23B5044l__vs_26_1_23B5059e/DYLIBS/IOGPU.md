## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-129.2.2.0.0
-  __TEXT.__text: 0x28ca8
+129.2.8.0.0
+  __TEXT.__text: 0x29044
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x4d3c
-  __TEXT.__cstring: 0x5f8c
+  __TEXT.__objc_methlist: 0x4d8c
+  __TEXT.__cstring: 0x5ffc
   __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae
-  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__unwind_info: 0xcd8
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0xb6dc
-  __TEXT.__objc_methtype: 0x6c34
-  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_methname: 0xb78b
+  __TEXT.__objc_methtype: 0x6c36
+  __TEXT.__objc_stubs: 0x31c0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_selrefs: 0x2868
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x7dc8
+  __AUTH_CONST.__objc_const: 0x7df8
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_ivar: 0x398
   __DATA.__data: 0x7e0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26393AB7-4022-362D-9A3F-71579B1973E0
-  Functions: 1422
-  Symbols:   4266
-  CStrings:  2959
+  UUID: EA4505C7-8D56-31FA-83EC-0C65FB4F4E12
+  Functions: 1429
+  Symbols:   4282
+  CStrings:  2967
 
Symbols:
+ -[IOGPUMemoryInfo getAnnotationListAndEmitResourceInfo]
+ -[IOGPUMetalBuffer emitResourceInfoTraceEvent]
+ -[IOGPUMetalResource attachedResourceInfoTraceEmitter]
+ -[IOGPUMetalResource emitResourceInfoTraceEvent]
+ -[IOGPUMetalResource emitResourceInfoTraceEvent].cold.1
+ -[IOGPUMetalResource setAttachedResourceInfoTraceEmitter:]
+ -[IOGPUMetalTexture emitResourceInfoTraceEvent]
+ _OBJC_IVAR_$_IOGPUMetalResource.attachedResourceInfoTraceEmitter
+ _objc_msgSend$emitResourceInfoTraceEvent
CStrings:
+ "-[IOGPUMetalResource emitResourceInfoTraceEvent]"
+ "@"
+ "T@,W,N,VattachedResourceInfoTraceEmitter"
+ "[attachedResourceInfoTraceEmitter respondsToSelector:selector]"
+ "attachedResourceInfoTraceEmitter"
+ "emitResourceInfoTraceEvent"
+ "getAnnotationListAndEmitResourceInfo"
+ "setAttachedResourceInfoTraceEmitter:"
+ "\xf0\xf0\""
- "\xf0\xf0!"

```
