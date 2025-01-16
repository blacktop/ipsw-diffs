## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-803.48.1.0.0
-  __TEXT.__text: 0x565a8
+803.54.2.0.0
+  __TEXT.__text: 0x5697c
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x1ef21
+  __TEXT.__cstring: 0x1ef88
   __TEXT.__const: 0x11918
   __TEXT.__gcc_except_tab: 0x458
   __TEXT.__objc_methname: 0xb

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 519
+  Functions: 520
   Symbols:   346
-  CStrings:  2397
+  CStrings:  2400
 
CStrings:
+ "%lld %d AVE %s: %s:%d calling emitEncodedFrame %p on %ld bytes"
+ "%lld %d AVE %s: %s:%d calling emitEncodedFrame %p on %ld bytes\n"
+ "%lld %d AVE %s: %s:%d calling emitEncodedFrame on %d bytes"
+ "%lld %d AVE %s: %s:%d calling emitEncodedFrame on %d bytes\n"
+ "%lld %d AVE %s: %s:%d calling emitEncodedFrame on %d bytes (SPS PPS)"
+ "%lld %d AVE %s: %s:%d calling emitEncodedFrame on %d bytes (SPS PPS)\n"
+ "%lld %d AVE %s: H264FrameRec ERROR: FigSampleBufferAttached failed."
+ "%lld %d AVE %s: H264FrameRec ERROR: FigSampleBufferAttached failed.\n"
+ "01:21:41"
+ "803.54.2"
+ "AVE_DW_Uninit"
+ "Jan  7 2025"
- "%lld %d AVE %s: H264FrameRec: calling emitEncodedFrame %p on %ld bytes"
- "%lld %d AVE %s: H264FrameRec: calling emitEncodedFrame %p on %ld bytes\n"
- "%lld %d AVE %s: H264FrameRec: calling emitEncodedFrame on %d bytes"
- "%lld %d AVE %s: H264FrameRec: calling emitEncodedFrame on %d bytes\n"
- "%lld %d AVE %s: H264FrameRec: calling emitEncodedFrame on %d bytes (SPS PPS)"
- "%lld %d AVE %s: H264FrameRec: calling emitEncodedFrame on %d bytes (SPS PPS)\n"
- "23:31:54"
- "803.48.1"
- "Dec 17 2024"

```
