## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-9100.26.0.0.0
-  __TEXT.__text: 0x1e314
+9110.1.0.0.0
+  __TEXT.__text: 0x1e330
   __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x2008
-  __TEXT.__cstring: 0x1679
+  __TEXT.__cstring: 0x169e
   __TEXT.__oslogstring: 0x10b8
   __TEXT.__tpad_act_plist: 0xe22d
   __TEXT.__unwind_info: 0x6d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7EF255A3-99E3-3219-AE0A-88E057F6E106
+  UUID: 39405123-A6B6-3CB4-BE94-32C43390069A
   Functions: 664
   Symbols:   1422
-  CStrings:  616
+  CStrings:  617
 
Functions:
~ __Z26MTParse_BinaryImagePayloadPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 540 -> 568
CStrings:
+ "Buffer(%u) too small to store compressed image(%u)!\n"
+ "Buffer(%u) too small to store uncompressed image(%u)!\n"
- "Buffer too small to uncompress image to %d bytes! (Buffer is only %u)\n"

```
