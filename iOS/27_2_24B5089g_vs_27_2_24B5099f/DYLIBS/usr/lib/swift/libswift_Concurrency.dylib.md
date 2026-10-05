## libswift_Concurrency.dylib

> `/usr/lib/swift/libswift_Concurrency.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-6.4.0.34.1
-  __TEXT.__text: 0x6c31c
+6.4.2.1.7
+  __TEXT.__text: 0x6c2ec
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x30aa
   __TEXT.__cstring: 0x2266

   __AUTH.__data: 0xa70
   __DATA.__data: 0xf0
   __DATA.__common: 0x88
-  __DATA_DIRTY.__data: 0x470
+  __DATA_DIRTY.__data: 0x468
   __DATA_DIRTY.__bss: 0x19d0
   __DATA_DIRTY.__common: 0x70
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/system/libdispatch.dylib
-  Functions: 3046
-  Symbols:   5829
+  Functions: 3045
+  Symbols:   5827
   CStrings:  217
 
Symbols:
- __ZL19dispatchEnqueueFunc
- __ZL29initializeDispatchEnqueueFuncP16dispatch_queue_sPv11qos_class_t
Functions:
~ _swift_dispatchEnqueueGlobal : 168 -> 160
~ _swift_dispatchEnqueueMain : 32 -> 24
- __ZL29initializeDispatchEnqueueFuncP16dispatch_queue_sPv11qos_class_t
~ _swift_task_enqueueOnDispatchQueue : 32 -> 24
CStrings:
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
- "Initialized count set to greater than specified capacity."
```
