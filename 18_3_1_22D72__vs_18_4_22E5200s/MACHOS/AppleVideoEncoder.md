## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

-803.54.2.0.0
-  __TEXT.__text: 0xe2ea8
-  __TEXT.__auth_stubs: 0xf20
+803.57.0.0.0
+  __TEXT.__text: 0xe1fd8
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x5a890
-  __TEXT.__const: 0x15e18
-  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__cstring: 0x5aba1
+  __TEXT.__const: 0x15dc8
+  __TEXT.__gcc_except_tab: 0x604
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x7a8
-  __DATA_CONST.__auth_got: 0x7a0
+  __TEXT.__unwind_info: 0x738
+  __DATA_CONST.__auth_got: 0x7b8
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x2eb8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 694
-  Symbols:   544
-  CStrings:  5734
+  Functions: 669
+  Symbols:   547
+  CStrings:  5749
 
Symbols:
+ _VTPixelTransferSessionCreate
+ _VTPixelTransferSessionInvalidate
+ _VTPixelTransferSessionTransferImage
CStrings:
+ "%lld %d AVE %s: %s:%d %s | Failed to create image transfer session, err = %d"
+ "%lld %d AVE %s: %s:%d %s | Failed to create image transfer session, err = %d\n"
+ "%lld %d AVE %s: %s:%d %s | Failed to transfer image, err = %d"
+ "%lld %d AVE %s: %s:%d %s | Failed to transfer image, err = %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to transfer a pixel buffer to another format %p (0x%X -> 0x%X) %d."
+ "%lld %d AVE %s: %s:%d %s | failed to transfer a pixel buffer to another format %p (0x%X -> 0x%X) %d.\n"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferIn is NULL"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferIn is NULL\n"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferOut is NULL"
+ "%lld %d AVE %s: %s:%d %s | pixelBufferOut is NULL\n"
+ "07:15:40"
+ "803.57.0"
+ "AVE_ImageBuf_Transfer"
+ "AVE_ImageTransfer"
+ "Feb 16 2025"
+ "err == kCVReturnSuccess"
+ "pixelBufferIn != __null"
+ "pixelBufferOut != __null"
+ "psList != ((void*)0)"
+ "psList->psNext != ((void*)0)"
+ "psList->psPrev != ((void*)0)"
+ "psNewNode != ((void*)0)"
+ "psNode != ((void*)0)"
+ "psNode->psNext != ((void*)0)"
+ "psNode->psPrev != ((void*)0)"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d\n"
- "04:44:38"
- "803.54.2"
- "Jan 16 2025"
- "psList != ((void *)0)"
- "psList->psNext != ((void *)0)"
- "psList->psPrev != ((void *)0)"
- "psNewNode != ((void *)0)"
- "psNode != ((void *)0)"
- "psNode->psNext != ((void *)0)"
- "psNode->psPrev != ((void *)0)"

```
