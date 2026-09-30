## AppleFSCompression

> `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression`

```diff

-170.0.0.0.0
-  __TEXT.__text: 0x78cc
-  __TEXT.__auth_stubs: 0x820
+174.0.0.0.0
+  __TEXT.__text: 0x7c34
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x1f61
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__cstring: 0x1fee
+  __TEXT.__unwind_info: 0x1e0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x498
-  __AUTH_CONST.__auth_got: 0x410
+  __DATA_CONST.__const: 0x4c0
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x11e0
+  __AUTH_CONST.__cfstring: 0x1240
   __DATA.__data: 0x4
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A981B04C-6689-36D2-858E-00D9AD3E31DD
-  Functions: 101
-  Symbols:   186
-  CStrings:  350
+  UUID: FB979B47-B1A3-317E-8F98-1387A58B56DE
+  Functions: 103
+  Symbols:   188
+  CStrings:  358
 
Symbols:
+ _kAFSCForceAsynchronous
+ _snprintf
CStrings:
+ "%s%s"
+ "%s:%d: Error: freed StreamCompressor for %s without closing rsrc fd\n"
+ "%s:%d: fcntl F_GETPATH %s: %s\n"
+ "/..namedfork/rsrc"
+ "ForceAsynchronous"

```
