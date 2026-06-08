## AppleFSCompression

> `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression`

```diff

-174.100.2.0.0
-  __TEXT.__text: 0x7c68
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x21e6
+181.0.0.0.0
+  __TEXT.__text: 0x7c5c
+  __TEXT.__const: 0x180
+  __TEXT.__cstring: 0x21e3
   __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__got: 0x48
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x650
-  __AUTH_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__auth_got: 0x410
   __DATA.__data: 0x4
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9C42597C-7AD6-3752-AC58-6AF36D62C562
+  UUID: 3E5B93E5-4081-36A1-B9CA-FB983E92848D
   Functions: 99
   Symbols:   187
-  CStrings:  358
+  CStrings:  357
 
Symbols:
+ _openat
- _snprintf
CStrings:
+ "%s:%d: open resource fork %s: %s\n"
+ "..namedfork/rsrc"
- "%s%s"
- "%s:%d: fcntl F_GETPATH %s: %s\n"
- "/..namedfork/rsrc"

```
