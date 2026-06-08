## BasebandVoice

> `/System/Library/Audio/Plug-Ins/HAL/BasebandVoice.driver/BasebandVoice`

```diff

-1075.0.0.0.0
-  __TEXT.__text: 0x9fe8
+1158.0.0.0.0
+  __TEXT.__text: 0x9a20
   __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0x251
-  __TEXT.__gcc_except_tab: 0x658
+  __TEXT.__gcc_except_tab: 0x55c
   __TEXT.__oslogstring: 0x91f
   __TEXT.__cstring: 0x4cb
-  __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x380
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__cfstring: 0x400
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0x78
   __DATA.__data: 0x218
   __DATA.__bss: 0x31
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libWirelessAudioIPC.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 3B4A5E16-A3EA-35DB-82CE-5EE927E22D11
+  UUID: 6310B839-87F5-3ED3-9808-8B73EC29BF02
   Functions: 125
   Symbols:   124
   CStrings:  188
CStrings:
+ "failed %{multichar}x"
+ "object %u, selector %{multichar}x, scope %{multichar}x, element %u"
+ "op %{multichar}x"
+ "op %{multichar}x, stream %u, currentTime %llu, ioBufferFrameSize %u"
+ "result %{multichar}x"
+ "result %{multichar}x, changed %zu"
+ "result %{multichar}x, dataSize %u"
+ "result %{multichar}x, isSettable %{BOOL}d"
+ "result %{multichar}x, sampleTime %lf, hostTime %llu, seed %llu"
+ "result %{multichar}x, willDo %{BOOL}d, willDoInPlace %{BOOL}d"
+ "sampleRate %lf, formatID %{multichar}x, formatFlags 0x%08x, bytesPerPacket %u, framesPerPacket %u, bytesPerFrame %u, channelsPerFrame %u, bitsPerChannel %u"
+ "success %{multichar}x"
+ "unsupported format ID %{multichar}x"
- "failed %{waipc:4cc}u"
- "object %u, selector %{waipc:4cc}u, scope %{waipc:4cc}u, element %u"
- "op %{waipc:4cc}u"
- "op %{waipc:4cc}u, stream %u, currentTime %llu, ioBufferFrameSize %u"
- "result %{waipc:4cc}u"
- "result %{waipc:4cc}u, changed %zu"
- "result %{waipc:4cc}u, dataSize %u"
- "result %{waipc:4cc}u, isSettable %{BOOL}d"
- "result %{waipc:4cc}u, sampleTime %lf, hostTime %llu, seed %llu"
- "result %{waipc:4cc}u, willDo %{BOOL}d, willDoInPlace %{BOOL}d"
- "sampleRate %lf, formatID %{waipc:4cc}u, formatFlags 0x%08x, bytesPerPacket %u, framesPerPacket %u, bytesPerFrame %u, channelsPerFrame %u, bitsPerChannel %u"
- "success %{waipc:4cc}u"
- "unsupported format ID %{waipc:4cc}u"

```
