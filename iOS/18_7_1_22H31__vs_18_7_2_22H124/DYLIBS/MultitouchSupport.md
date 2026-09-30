## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-8140.4.0.0.0
-  __TEXT.__text: 0x1e200
+8140.5.0.0.0
+  __TEXT.__text: 0x1e21c
   __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x2010
-  __TEXT.__cstring: 0x16ba
+  __TEXT.__cstring: 0x16df
   __TEXT.__oslogstring: 0x10ca
   __TEXT.__tpad_act_plist: 0xe22d
   __TEXT.__unwind_info: 0x6d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93EEAB32-12D1-357E-AF76-1AEBB1413288
+  UUID: 05282DB4-1D88-35A9-83EF-AB5DD6A85EBD
   Functions: 661
   Symbols:   1420
-  CStrings:  627
+  CStrings:  628
 
Functions:
~ __Z26MTParse_BinaryImagePayloadPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 540 -> 568
CStrings:
+ "Buffer(%u) too small to store compressed image(%u)!\n"
+ "Buffer(%u) too small to store uncompressed image(%u)!\n"
- "Buffer too small to uncompress image to %d bytes! (Buffer is only %u)\n"

```
