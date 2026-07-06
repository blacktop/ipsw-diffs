## libafc.dylib

> `/usr/lib/libafc.dylib`

```diff

-  __TEXT.__text: 0x15618
+  __TEXT.__text: 0x1562c
   __TEXT.__const: 0x110
   __TEXT.__oslogstring: 0x10bd
   __TEXT.__cstring: 0x1b40

   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__common: 0x10
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0xf9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__dof_afc : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ ___WaitForTimeoutOrEvent : 1304 -> 1312
~ ___AFCConnectionDispatchReply : 244 -> 232
~ _AFCProcessServerPacket : 14420 -> 14444

```
