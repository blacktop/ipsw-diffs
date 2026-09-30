## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/Versions/A/IOMobileFramebuffer`

```diff

-700.50.85.0.0
-  __TEXT.__text: 0x3b2f0
-  __TEXT.__gcc_except_tab: 0x228
+700.50.97.9.0
+  __TEXT.__text: 0x3b368
+  __TEXT.__gcc_except_tab: 0x234
   __TEXT.__const: 0x1b04
-  __TEXT.__cstring: 0x967f
+  __TEXT.__cstring: 0x96f8
   __TEXT.__unwind_info: 0x890
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb8

   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 925
-  Symbols:   1134
-  CStrings:  951
+  Functions: 927
+  Symbols:   1136
+  CStrings:  954
 
Symbols:
+ _IOMFBGainMapCapGetBuffer
+ _IOMFBGainMapCapSetBuffer
Functions:
~ __ZN22DisplayDataBlockParser12process_alshEPNS_12Block_HeaderE : 2292 -> 2320
~ __ZN22DisplayDataBlockParser19cleanup_acss_configEv : 276 -> 268
+ _IOMFBGainMapCapSetBuffer
+ _IOMFBGainMapCapGetBuffer
~ _IOMobileFramebufferSwapSetGainMap : 116 -> 136
~ _IOMFBgainencoder_emit_run : 680 -> 712
~ _IOMFBgainencoder_finish : 304 -> 324
CStrings:
+ "IOMFB: SwapSetGainMap: map is NULL\n"
+ "Parser e: cannot allocate IOMFBACSSConfig"
+ "Parser e: cannot allocate IOMFBACSSConfig\n"
```
