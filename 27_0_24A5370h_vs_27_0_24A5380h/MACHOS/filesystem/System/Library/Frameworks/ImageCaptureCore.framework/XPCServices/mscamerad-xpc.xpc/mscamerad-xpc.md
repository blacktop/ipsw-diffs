## mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc`

```diff

-  __TEXT.__text: 0x15964
+  __TEXT.__text: 0x15a8c
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__objc_stubs: 0x2d20
   __TEXT.__objc_methlist: 0xffc
   __TEXT.__const: 0x3c
   __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__objc_methname: 0x31e9
-  __TEXT.__cstring: 0x1136
+  __TEXT.__objc_methname: 0x31f2
+  __TEXT.__cstring: 0x1185
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0x280
   __TEXT.__objc_classname: 0x114
   __TEXT.__objc_methtype: 0x629
   __TEXT.__unwind_info: 0x398
   __DATA_CONST.__const: 0x430
-  __DATA_CONST.__cfstring: 0x1dc0
+  __DATA_CONST.__cfstring: 0x1de0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/libsqlite3.dylib
   Functions: 363
   Symbols:   1140
-  CStrings:  1230
+  CStrings:  1232
 
Sections:
~ __TEXT.__objc_methlist : content changed
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
~ ___37-[ICBufferCache resetBufferAtOffset:]_block_invoke : 496 -> 500
~ -[ICBufferCache consumeBufferAtOffset:sized:] : 332 -> 344
~ ___45-[ICBufferCache consumeBufferAtOffset:sized:]_block_invoke : 272 -> 280
~ -[MSCameraFile createBufferCache] -> -[MSCameraFile createBufferCacheAtOffset:] : 124 -> 140
~ -[MSCameraFile readDataWithOptions:reply:] : 1616 -> 1872
CStrings:
+ "Buffer cache miss at offset: %lld, reading %lld bytes directly"
+ "ICReadBufferStreamOpen: %llu at offset: %lld"
+ "createBufferCacheAtOffset:"
- "ICReadBufferStreamOpen: %llu"
- "createBufferCache"

```
