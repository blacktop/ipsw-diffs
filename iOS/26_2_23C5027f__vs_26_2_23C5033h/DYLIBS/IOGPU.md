## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-129.2.10.0.0
-  __TEXT.__text: 0x29054
+129.3.2.0.0
+  __TEXT.__text: 0x29108
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x4d94
   __TEXT.__cstring: 0x5ffc

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE663A5C-805E-308E-99A6-5BA0A4F54535
+  UUID: 015585D7-D57B-3703-A5F3-CE0406A4FB8F
   Functions: 1429
   Symbols:   4282
   CStrings:  2968
Functions:
~ -[IOGPUMetalDevice kickCleanupQueue] : 192 -> 204
~ -[IOGPUMetalDevice periodicUpdateResourcePoolPurgeability] : 240 -> 260
~ -[IOGPUMetalComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalIndirectArgumentEncoder setIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalRenderCommandEncoder setVertexIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalRenderCommandEncoder setFragmentIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalRenderCommandEncoder setTileIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalRenderCommandEncoder setObjectIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalRenderCommandEncoder setMeshIntersectionFunctionTables:withBufferRange:] : 296 -> 316
~ -[IOGPUMetalDevice cancelPeriodicUpdateResourcePoolPurgeability] : 104 -> 112

```
