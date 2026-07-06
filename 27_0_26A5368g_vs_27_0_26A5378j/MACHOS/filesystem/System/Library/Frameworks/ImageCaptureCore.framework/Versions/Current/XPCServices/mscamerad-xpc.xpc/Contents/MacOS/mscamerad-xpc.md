## mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/Current/XPCServices/mscamerad-xpc.xpc/Contents/MacOS/mscamerad-xpc`

```diff

-  __TEXT.__text: 0x17584
+  __TEXT.__text: 0x176c0
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_stubs: 0x2d20
   __TEXT.__objc_methlist: 0xf7c
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__const: 0x48
-  __TEXT.__objc_methname: 0x2fec
-  __TEXT.__cstring: 0x1133
+  __TEXT.__objc_methname: 0x2ff5
+  __TEXT.__cstring: 0x1182
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0x280
   __TEXT.__objc_classname: 0xec
   __TEXT.__objc_methtype: 0x574
   __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__const: 0x4a0
-  __DATA_CONST.__cfstring: 0x1d40
+  __DATA_CONST.__cfstring: 0x1d60
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/libsqlite3.dylib
   Functions: 393
   Symbols:   1161
-  CStrings:  1207
+  CStrings:  1209
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ -[MSCameraFile createBufferCacheAtOffset:]
+ _objc_msgSend$createBufferCacheAtOffset:
- -[MSCameraFile createBufferCache]
- _objc_msgSend$createBufferCache
Functions:
~ ___37-[ICBufferCache resetBufferAtOffset:]_block_invoke : 548 -> 552
~ -[ICBufferCache consumeBufferAtOffset:sized:] : 348 -> 360
~ ___45-[ICBufferCache consumeBufferAtOffset:sized:]_block_invoke : 284 -> 288
~ -[MSCameraFile createBufferCache] -> -[MSCameraFile createBufferCacheAtOffset:] : 128 -> 144
~ -[MSCameraFile readDataWithOptions:reply:] : 1748 -> 2028
CStrings:
+ "Buffer cache miss at offset: %lld, reading %lld bytes directly"
+ "ICReadBufferStreamOpen: %llu at offset: %lld"
+ "createBufferCacheAtOffset:"
- "ICReadBufferStreamOpen: %llu"
- "createBufferCache"

```
