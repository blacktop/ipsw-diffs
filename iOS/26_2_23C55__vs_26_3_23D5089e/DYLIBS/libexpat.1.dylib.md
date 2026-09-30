## libexpat.1.dylib

> `/usr/lib/libexpat.1.dylib`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x18168
+45.0.0.0.0
+  __TEXT.__text: 0x18994
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0xd46
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__cstring: 0xfa7
+  __TEXT.__unwind_info: 0x2d0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xb18
+  __DATA_CONST.__const: 0xb48
   __AUTH_CONST.__auth_got: 0x78
   __AUTH_CONST.__const: 0x1960
   - /usr/lib/libSystem.B.dylib
-  UUID: B9D054F1-6B1C-3B49-9F1E-3910DDE6DB2A
-  Functions: 330
-  Symbols:   661
-  CStrings:  344
+  UUID: 6DAF9FB1-DD62-3D86-A38C-6E2E459347EA
+  Functions: 348
+  Symbols:   695
+  CStrings:  361
 
Symbols:
+ _XML_SetAllocTrackerActivationThreshold
+ _XML_SetAllocTrackerMaximumAmplification
+ _destroyBindings
+ _expat_free
+ _expat_free.cold.1
+ _expat_free.cold.2
+ _expat_heap_increase_tolerable
+ _expat_heap_increase_tolerable.cold.1
+ _expat_heap_increase_tolerable.cold.2
+ _expat_heap_increase_tolerable.cold.3
+ _expat_malloc
+ _expat_realloc
+ _expat_realloc.cold.1
+ _expat_realloc.cold.2
+ _expat_realloc.cold.3
+ _expat_realloc.cold.4
+ _hashTableClear
+ _parserCreate.cold.1
CStrings:
+ "(XmlBigCount)-1 - rootParser->m_alloc_tracker.bytesAllocated >= absDiff"
+ "EXPAT_MALLOC_DEBUG"
+ "SIZE_MAX - rootParser->m_alloc_tracker.bytesAllocated >= increase"
+ "SIZE_MAX - sizeof(size_t) - EXPAT_MALLOC_PADDING >= size"
+ "XML_AT_ACT_THRES"
+ "XML_AT_MAX_AMP"
+ "expat: Allocations(%p): Direct %10llu, allocated %c%10llu to %10llu (%10llu peak), amplification %8.2f (xmlparse.c:%d)\n"
+ "expat_2.7.3"
+ "expat_free"
+ "expat_heap_increase_tolerable"
+ "expat_realloc"
+ "increase > 0"
+ "newTotal > 0"
+ "parser != NULL"
+ "parserCreate"
+ "rootParser != NULL"
+ "rootParser->m_alloc_tracker.bytesAllocated >= absDiff"
+ "rootParser->m_alloc_tracker.bytesAllocated >= bytesAllocated"
- "expat_2.7.1"

```
