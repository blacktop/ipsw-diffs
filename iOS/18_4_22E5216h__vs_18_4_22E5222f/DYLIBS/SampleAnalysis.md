## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-385.11.0.0.0
-  __TEXT.__text: 0xe8444
+385.13.0.0.0
+  __TEXT.__text: 0xe8af8
   __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_methlist: 0x5a74
+  __TEXT.__objc_methlist: 0x5a7c
   __TEXT.__const: 0x338
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x16c98
-  __TEXT.__oslogstring: 0xbce3
-  __TEXT.__gcc_except_tab: 0x9bf4
+  __TEXT.__cstring: 0x16ea3
+  __TEXT.__oslogstring: 0xbdd6
+  __TEXT.__gcc_except_tab: 0x9c04
   __TEXT.__unwind_info: 0x2040
   __TEXT.__objc_classname: 0xaae
-  __TEXT.__objc_methname: 0xce4d
-  __TEXT.__objc_methtype: 0x1791
+  __TEXT.__objc_methname: 0xce85
+  __TEXT.__objc_methtype: 0x1792
   __TEXT.__objc_stubs: 0x7960
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x34e0

   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0xbac0
-  __AUTH_CONST.__objc_const: 0xf730
+  __AUTH_CONST.__cfstring: 0xbae0
+  __AUTH_CONST.__objc_const: 0xf780
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xc60
+  __DATA.__objc_ivar: 0xc68
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x50

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2720
-  Symbols:   3271
-  CStrings:  6515
+  Functions: 2722
+  Symbols:   3273
+  CStrings:  6526
 
CStrings:
+ "\x01\x12\x11"
+ " (Exclave)"
+ "%*s%s: layoutid %llu, flags 0x%llx, sharedcache_index %u%s\n"
+ "%s: after serializing (with %u rootFrames, %u loadInfos), ended with length %ld, should be %lu"
+ "((void*)(additions + 1)) - ((void*)serializedExclave) <= (long) [self sizeInBytesForSerializedVersion]"
+ "Exclave %@ has shared cache index %u, but only %lu load infos"
+ "T@\"SASharedCache\",R,V_sharedCache"
+ "_isExclaveSharedCache"
+ "bufferLength %lu < serialized SAExclave struct v2 with %u root frames, %u image infos"
+ "bufferLength >= sizeof(*serializedSharedCache) + (sizeof(SASerializedIndex) * serializedSharedCache->numBinaryLoadInfos) + sizeof(SASerializedSharedCache_v4_additions)"
+ "r^{exclave_textlayout_info=QQI}"
- "\x01\x11\x11"
- "r^{exclave_textlayout_info=QQ}"

```
