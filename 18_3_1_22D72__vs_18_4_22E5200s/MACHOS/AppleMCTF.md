## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-803.54.2.0.0
-  __TEXT.__text: 0x5697c
-  __TEXT.__auth_stubs: 0xcb0
+803.57.0.0.0
+  __TEXT.__text: 0x567a8
+  __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x1ef88
-  __TEXT.__const: 0x11918
-  __TEXT.__gcc_except_tab: 0x458
+  __TEXT.__cstring: 0x1f299
+  __TEXT.__const: 0x118f8
+  __TEXT.__gcc_except_tab: 0x490
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__auth_got: 0x668
+  __TEXT.__unwind_info: 0x588
+  __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x2760

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 520
-  Symbols:   346
-  CStrings:  2400
+  Functions: 500
+  Symbols:   349
+  CStrings:  2415
 
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
+ "07:01:23"
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
- "04:29:11"
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
