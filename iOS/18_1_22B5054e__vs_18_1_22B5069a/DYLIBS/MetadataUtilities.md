## MetadataUtilities

> `/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities`

```diff

-2314.8.0.0.0
-  __TEXT.__text: 0x4db7c
-  __TEXT.__auth_stubs: 0x17f0
+2314.10.1.0.8
+  __TEXT.__text: 0x4dfdc
+  __TEXT.__auth_stubs: 0x1840
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x3cbe
-  __TEXT.__cstring: 0x64ef
+  __TEXT.__cstring: 0x6544
   __TEXT.__oslogstring: 0xc58
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__ustring: 0x9a
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__unwind_info: 0x928
   __TEXT.__objc_classname: 0xcc
   __TEXT.__objc_methname: 0xf76
   __TEXT.__objc_methtype: 0x64d

   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH_CONST.__auth_got: 0xc28
   __AUTH_CONST.__auth_ptr: 0x70
   __AUTH_CONST.__const: 0x738
   __AUTH_CONST.__cfstring: 0x4080

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x28
   __DATA.__objc_ivar: 0x13c
-  __DATA.__data: 0x1d144
-  __DATA.__common: 0x8d8
+  __DATA.__data: 0x1d1b4
+  __DATA.__common: 0x8e0
   __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x130

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1120
-  Symbols:   1606
-  CStrings:  1355
+  Functions: 1128
+  Symbols:   1621
+  CStrings:  1360
 
Symbols:
+ _CFBitVectorCreateMutable
+ _CFBitVectorCreateMutableCopy
+ _CFBitVectorSetBitAtIndex
+ _CFBitVectorSetCount
+ _pthread_cond_wait
+ _strncat
- _strcat
CStrings:
+ "MDTrie.cpp"
+ "bit_vector.h"
+ "len < MDTRIE_MAX_KEY_LENGTH"
+ "newBV"
+ "newCapacity > bv->capacity"

```
