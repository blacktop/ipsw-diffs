## IOMobileFramebuffer

> `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/Versions/A/IOMobileFramebuffer`

```diff

-700.50.97.9.0
-  __TEXT.__text: 0x3b49c
+700.50.117.0.0
+  __TEXT.__text: 0x3b4ec
   __TEXT.__gcc_except_tab: 0x234
   __TEXT.__const: 0x1b04
-  __TEXT.__cstring: 0x96ae
+  __TEXT.__cstring: 0x96bb
   __TEXT.__unwind_info: 0x8a0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb8

   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 928
-  Symbols:   1136
+  Functions: 929
+  Symbols:   1137
   CStrings:  951
 
Symbols:
+ _isServicingExternal
Functions:
~ __ZN22DisplayDataBlockParser16set_ptuc_rr_lutsEv : 240 -> 276
~ _IOMobileFramebufferOpen : 3696 -> 3716
+ _isServicingExternal
~ _iomfb_match_callback : 1048 -> 968
CStrings:
+ "Parser e: failed to set PTUC TLS RR LUT dbv_nits=%d, attempt %u/%u\n"
- "Parser e: failed to set PTUC TLS RR LUT brightness %d\n"
```
