## footprint

> `/usr/bin/footprint`

```diff

-308.0.0.0.0
-  __TEXT.__text: 0x1ad64
+310.0.0.0.0
+  __TEXT.__text: 0x1aeec
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_stubs: 0x22e0
   __TEXT.__objc_methlist: 0x115c
-  __TEXT.__cstring: 0x3365
+  __TEXT.__cstring: 0x342b
   __TEXT.__objc_classname: 0x206
-  __TEXT.__objc_methtype: 0x7ab
+  __TEXT.__objc_methtype: 0x7ba
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x3d4
-  __TEXT.__objc_methname: 0x231a
+  __TEXT.__objc_methname: 0x2356
   __TEXT.__ustring: 0xd0
   __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__unwind_info: 0x488
   __DATA_CONST.__auth_got: 0x638
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x1768
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x17a8
   __DATA_CONST.__cfstring: 0x2220
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2e98
-  __DATA.__objc_selrefs: 0x9d0
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_const: 0x2eb8
+  __DATA.__objc_selrefs: 0x9e0
+  __DATA.__objc_ivar: 0x290
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x250
   __DATA.__bss: 0x4140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 625BEE60-583D-3B35-AD8A-6C88169AD483
-  Functions: 410
-  Symbols:   276
-  CStrings:  1434
+  UUID: A68D8BC3-48F1-37C9-859F-FC661DCFE02C
+  Functions: 412
+  Symbols:   274
+  CStrings:  1446
 
Symbols:
+ _objc_release_x2
+ _os_map_64_delete
+ _os_map_64_destroy
+ _os_map_64_find
+ _os_map_64_foreach
+ _os_map_64_init
+ _os_map_64_insert
- _CFArrayAppendValue
- _CFArrayCreateMutable
- _CFDictionaryAddValue
- _CFDictionaryCreateMutable
- _CFDictionaryGetValue
- _CFDictionaryReplaceValue
- _CFRelease
- _kCFAllocatorDefault
- _kCFTypeDictionaryValueCallBacks
CStrings:
+ "B24@?0Q8^v16"
+ "_memoryObjectMapsInitialized"
+ "finalized_linkedit_objects"
+ "finalized_memory_objects"
+ "finalized_shared_cache"
+ "finalized_text_objects"
+ "linkedit_memory_objects"
+ "memory_objects"
+ "pointerValue"
+ "shared_cache_memory_objects"
+ "text_memory_objects"
+ "valueWithPointer:"
+ "{_os_opaque_64_map_s=\"data\"[3^v]}"
- "^{__CFDictionary=}"

```
