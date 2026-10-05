## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.48.1.0.0
-  __TEXT.__text: 0x87a0c
-  __TEXT.__auth_stubs: 0xd70
+913.63.1.0.0
+  __TEXT.__text: 0x88ff0
+  __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x286c9
-  __TEXT.__const: 0x229e8
-  __TEXT.__gcc_except_tab: 0x628
+  __TEXT.__cstring: 0x28d9b
+  __TEXT.__const: 0x22a98
+  __TEXT.__gcc_except_tab: 0x62c
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0xba0
+  __TEXT.__unwind_info: 0xbb8
   __DATA_CONST.__const: 0x5430
   __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_selrefs: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 672
-  Symbols:   341
-  CStrings:  3443
+  Functions: 678
+  Symbols:   346
+  CStrings:  3473
 
Symbols:
+ _CMBlockBufferAppendBufferReference
+ _CMBlockBufferCreateEmpty
+ _CMBlockBufferCreateWithBufferReference
+ _CMBlockBufferGetDataLength
+ _CMSampleBufferCreateCopyWithNewTiming
CStrings:
+ "%lld %d AVE %s: %s::%s:%d %s | %p TokenPush null frame"
+ "%lld %d AVE %s: %s::%s:%d %s | %p TokenPush null frame\n"
+ "%lld %d AVE %s: %s::%s:%d %s | AV1 token overflow %p %d"
+ "%lld %d AVE %s: %s::%s:%d %s | AV1 token overflow %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | AV1 token push failed %d frame %d"
+ "%lld %d AVE %s: %s::%s:%d %s | AV1 token push failed %d frame %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | WrapAV1BlockBuffer CMSampleBufferCreate failed %d"
+ "%lld %d AVE %s: %s::%s:%d %s | WrapAV1BlockBuffer CMSampleBufferCreate failed %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | WrapAV1BlockBuffer bad size %zu"
+ "%lld %d AVE %s: %s::%s:%d %s | WrapAV1BlockBuffer bad size %zu\n"
+ "%lld %d AVE %s: %s::%s:%d %s | WrapAV1BlockBuffer null block buffer"
+ "%lld %d AVE %s: %s::%s:%d %s | WrapAV1BlockBuffer null block buffer\n"
+ "%lld %d AVE %s: AV1 reorder bundle bbuf create failed %d"
+ "%lld %d AVE %s: AV1 reorder bundle bbuf create failed %d\n"
+ "%lld %d AVE %s: AV1 reorder disengaged with %d held / %d token(s) pending; flushing at frame %d"
+ "%lld %d AVE %s: AV1 reorder disengaged with %d held / %d token(s) pending; flushing at frame %d\n"
+ "%lld %d AVE %s: AV1 reorder hold overflow, dropping frame %d"
+ "%lld %d AVE %s: AV1 reorder hold overflow, dropping frame %d\n"
+ "%lld %d AVE %s: AV1 reorder ready FIFO overflow (bundle)"
+ "%lld %d AVE %s: AV1 reorder ready FIFO overflow (bundle)\n"
+ "%lld %d AVE %s: AV1 reorder ready FIFO overflow (sfx)"
+ "%lld %d AVE %s: AV1 reorder ready FIFO overflow (sfx)\n"
+ "%lld %d AVE %s: AV1 reorder retime failed %d for frame %lld; using placeholder timing"
+ "%lld %d AVE %s: AV1 reorder retime failed %d for frame %lld; using placeholder timing\n"
+ "913.63.1"
+ "TokenPush"
+ "WrapAV1BlockBuffer"
+ "bb != __null"
+ "err == noErr && sbuf != __null"
+ "iSampleSize > 0"
+ "m_iAV1TokenCount >= 0 && m_iAV1TokenCount < 32"
- "913.48.1"
```
