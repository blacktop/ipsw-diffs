## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.58.0.0.0
-  __TEXT.__text: 0x74130
+904.72.0.0.0
+  __TEXT.__text: 0x74d10
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x22e02
+  __TEXT.__cstring: 0x2313c
   __TEXT.__const: 0x1e768
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x608
   __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x41b0
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__const: 0x4180
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F5B3C96C-49A2-3156-A280-872C695EC0A3
-  Functions: 609
+  UUID: 38F61798-5FB4-37C6-9BFD-A28588666387
+  Functions: 612
   Symbols:   354
-  CStrings:  2935
+  CStrings:  2959
 
CStrings:
+ "%lld %d AVE %s: %p %lld GetProp %s: %d"
+ "%lld %d AVE %s: %p %lld GetProp %s: %d\n"
+ "%lld %d AVE %s: %p %lld GetProp %s: %d %p"
+ "%lld %d AVE %s: %p %lld GetProp %s: %d %p\n"
+ "%lld %d AVE %s: %p %lld GetProp %s: %lld %p"
+ "%lld %d AVE %s: %p %lld GetProp %s: %lld %p\n"
+ "%lld %d AVE %s: %p %lld GetProp %s: %p"
+ "%lld %d AVE %s: %p %lld GetProp %s: %p\n"
+ "%lld %d AVE %s: %p %lld GetProp %s: %s"
+ "%lld %d AVE %s: %p %lld GetProp %s: %s\n"
+ "%lld %d AVE %s: %p %lld GetProp %s: 0x%x %p"
+ "%lld %d AVE %s: %p %lld GetProp %s: 0x%x %p\n"
+ "%lld %d AVE %s: %p %lld SetProp %s: %d"
+ "%lld %d AVE %s: %p %lld SetProp %s: %d\n"
+ "%lld %d AVE %s: %p %lld SetProp %s: %d %d"
+ "%lld %d AVE %s: %p %lld SetProp %s: %d %d\n"
+ "%lld %d AVE %s: %p %lld SetProp %s: %s"
+ "%lld %d AVE %s: %p %lld SetProp %s: %s\n"
+ "%lld %d AVE %s: %p %lld SetProp %s: 0x%x"
+ "%lld %d AVE %s: %p %lld SetProp %s: 0x%x\n"
+ "%lld %d AVE %s: %p %lld SetProp %s[%d]: %d %d"
+ "%lld %d AVE %s: %p %lld SetProp %s[%d]: %d %d\n"
+ "%lld %d AVE %s: %s pAttrDict :%p sourceFormat: 0x%x"
+ "%lld %d AVE %s: %s pAttrDict :%p sourceFormat: 0x%x\n"
+ "%lld %d AVE %s: %s pOutPxlBufAttr %p soruce %dx%d needed %dx%d"
+ "%lld %d AVE %s: %s pOutPxlBufAttr %p soruce %dx%d needed %dx%d\n"
+ "%lld %d AVE %s: %s:%d %s | AVE_Session_MCTF_BuildDestPixelBufAttributes failed, %p %lld 0x%x %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_Session_MCTF_BuildDestPixelBufAttributes failed, %p %lld 0x%x %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVE_Session_MCTF_BuildDestPixelBufAttributes failed, %p %p %lld 0x%x %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_Session_MCTF_BuildDestPixelBufAttributes failed, %p %p %lld 0x%x %d\n"
+ "%lld %d AVE %s: %s:%d %s | Fail to set MCTF InputPixelBufferAttributes, %p %lld %p %p %d"
+ "%lld %d AVE %s: %s:%d %s | Fail to set MCTF InputPixelBufferAttributes, %p %lld %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | Fail to set MCTF InputPixelBufferAttributes, %p %lld %p %p 0x%x %d"
+ "%lld %d AVE %s: %s:%d %s | Fail to set MCTF InputPixelBufferAttributes, %p %lld %p %p 0x%x %d\n"
+ "%lld %d AVE %s: %s:%d %s | Find output pixel format failed, %p %lld %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | Find output pixel format failed, %p %lld %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | Find output pixel format failed, %p %p %lld %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | Find output pixel format failed, %p %p %lld %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %p %d 0x%x 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %p %d 0x%x 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create input pixel buffer attribute %d %d 0x%x %d %dx%d %dx%d 0x%x %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create input pixel buffer attribute %d %d 0x%x %d %dx%d %dx%d 0x%x %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to get pixel format details %p 0x%x"
+ "%lld %d AVE %s: %s:%d %s | fail to get pixel format details %p 0x%x\n"
+ "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to get pixel format details %p %lld %p %p %p %d"
+ "%lld %d AVE %s: %s:%d %s | failed to get pixel format details %p %lld %p %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx"
+ "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %p %d 0x%x 0x%llx\n"
+ "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p %d (%d, %d)"
+ "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p %d (%d, %d)\n"
+ "%lld %d AVE %s: %s:%d %s | invalid source frame pixel format %p %lld %p %p %p 0x%x"
+ "%lld %d AVE %s: %s:%d %s | invalid source frame pixel format %p %lld %p %p %p 0x%x\n"
+ "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx"
+ "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %p %d 0x%x 0x%llx\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameter %p 0x%x"
+ "%lld %d AVE %s: %s:%d %s | wrong parameter %p 0x%x\n"
+ "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data"
+ "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data\n"
+ "22:24:14"
+ "904.72.0"
+ "AVE_Prop_MCTF_GetSourceFramePixelFormat"
+ "AVE_Prop_MCTF_SetSourceFramePixelFormat"
+ "Jul 25 2025"
+ "SourceFramePixelFormat"
+ "iOutPixelFormat != 0"
+ "kVTTemporalFilterPropertyKey_SourceFramePixelFormat"
+ "pMCTF != __null && sourceFormat != 0"
- "%lld %d AVE %s:  VTTemporalFilterPluginSessionSetOutputPixelBufferAttributes err:%d"
- "%lld %d AVE %s:  VTTemporalFilterPluginSessionSetOutputPixelBufferAttributes err:%d\n"
- "%lld %d AVE %s: %p %lld Get %s: %d"
- "%lld %d AVE %s: %p %lld Get %s: %d\n"
- "%lld %d AVE %s: %p %lld Get %s: %d %p"
- "%lld %d AVE %s: %p %lld Get %s: %d %p\n"
- "%lld %d AVE %s: %p %lld Get %s: %lld %p"
- "%lld %d AVE %s: %p %lld Get %s: %lld %p\n"
- "%lld %d AVE %s: %p %lld Get %s: %p"
- "%lld %d AVE %s: %p %lld Get %s: %p\n"
- "%lld %d AVE %s: %p %lld Get %s: %s"
- "%lld %d AVE %s: %p %lld Get %s: %s\n"
- "%lld %d AVE %s: %p %lld Get %s: 0x%x %p"
- "%lld %d AVE %s: %p %lld Get %s: 0x%x %p\n"
- "%lld %d AVE %s: %p %lld Set %s: %d"
- "%lld %d AVE %s: %p %lld Set %s: %d\n"
- "%lld %d AVE %s: %p %lld Set %s: %d %d"
- "%lld %d AVE %s: %p %lld Set %s: %d %d\n"
- "%lld %d AVE %s: %p %lld Set %s: %s"
- "%lld %d AVE %s: %p %lld Set %s: %s\n"
- "%lld %d AVE %s: %p %lld Set %s[%d]: %d %d"
- "%lld %d AVE %s: %p %lld Set %s[%d]: %d %d\n"
- "%lld %d AVE %s: %s FigCreatePixelBufferAttributesWithIOSurfaceSupport err:%d"
- "%lld %d AVE %s: %s FigCreatePixelBufferAttributesWithIOSurfaceSupport err:%d\n"
- "%lld %d AVE %s: %s pMCTF->pOutPxlBufAttr %p"
- "%lld %d AVE %s: %s pMCTF->pOutPxlBufAttr %p\n"
- "%lld %d AVE %s: %s sourceFormat CMPixelFormatType = 0x%x"
- "%lld %d AVE %s: %s sourceFormat CMPixelFormatType = 0x%x\n"
- "%lld %d AVE %s: %s source_width=%d source_height=%d needed %dx%d"
- "%lld %d AVE %s: %s source_width=%d source_height=%d needed %dx%d\n"
- "%lld %d AVE %s: %s:%d %s | AVE_PixelBuf_CreateAttrDict %s:%d failed."
- "%lld %d AVE %s: %s:%d %s | AVE_PixelBuf_CreateAttrDict %s:%d failed.\n"
- "%lld %d AVE %s: %s:%d %s | AVE_Session_MCTF_BuildDestPixelBufAttributes failed, res = %d, pMCTF = %p, %p, %lld"
- "%lld %d AVE %s: %s:%d %s | AVE_Session_MCTF_BuildDestPixelBufAttributes failed, res = %d, pMCTF = %p, %p, %lld\n"
- "%lld %d AVE %s: %s:%d %s | Find output pixel format failed, pMCTF = %p, %p, %lld"
- "%lld %d AVE %s: %s:%d %s | Find output pixel format failed, pMCTF = %p, %p, %lld\n"
- "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %s %d %d 0x%x 0x%llx %d"
- "%lld %d AVE %s: %s:%d %s | fail to add property %p %d %d 0x%x %lld | %d %s %s %d %d 0x%x 0x%llx %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to create CFString %p %d 0x%x %lld %p"
- "%lld %d AVE %s: %s:%d %s | fail to create CFString %p %d 0x%x %lld %p\n"
- "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx %d"
- "%lld %d AVE %s: %s:%d %s | fail to get property %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx %d"
- "%lld %d AVE %s: %s:%d %s | fail to set property %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %d %p %lld %d 0x%x %s"
- "%lld %d AVE %s: %s:%d %s | failed to create CFString %p %d %p %lld %d 0x%x %s\n"
- "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx"
- "%lld %d AVE %s: %s:%d %s | get function is not supported %p %lld %d 0x%x %p %p %p | %s %s %d %d 0x%x 0x%llx\n"
- "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p %d （%d, %d)"
- "%lld %d AVE %s: %s:%d %s | invalid LatencyMode %p %lld %p %p %p %d （%d, %d)\n"
- "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx"
- "%lld %d AVE %s: %s:%d %s | set function is not supported %p %lld %d 0x%x %p %p | %s %s %d %d 0x%x 0x%llx\n"
- "%lld %d AVE %s: %s:%d: pPixelBuf = %p, CMPixelFormatType = %d, pMCTF = %p, %p, %lld"
- "%lld %d AVE %s: %s:%d: pPixelBuf = %p, CMPixelFormatType = %d, pMCTF = %p, %p, %lld\n"
- "%lld %d AVE %s: Insufficient size for userQPMap, %d, %d"
- "%lld %d AVE %s: Insufficient size for userQPMap, %d, %d\n"
- "%lld %d AVE %s: pAttrDict :%p"
- "%lld %d AVE %s: pAttrDict :%p\n"
- "00:40:19"
- "904.58.0"
- "Jul 15 2025"
- "pCFKey != __null"

```
