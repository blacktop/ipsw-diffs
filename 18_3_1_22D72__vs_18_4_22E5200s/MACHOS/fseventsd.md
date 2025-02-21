## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1400.0.0.0.0
-  __TEXT.__text: 0x15b34
-  __TEXT.__auth_stubs: 0xc10
-  __TEXT.__cstring: 0xbbf
+1400.100.1.0.0
+  __TEXT.__text: 0x1632c
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__cstring: 0xbd5
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x2a73
+  __TEXT.__oslogstring: 0x2b59
   __TEXT.__unwind_info: 0x340
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__cfstring: 0x4a0
   __DATA.__data: 0x232

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 353
-  Symbols:   213
-  CStrings:  396
+  Functions: 354
+  Symbols:   219
+  CStrings:  404
 
Symbols:
+ _CFBundleGetIdentifier
+ _CFStringGetCString
+ _CFURLCreateWithFileSystemPath
+ _SecTaskCopySigningIdentifier
+ __CFBundleCreateWithExecutableURLIfLooksLikeBundle
+ _csops
CStrings:
+ "%s: !path || !bundle_id)"
+ "%s: (%s) -  CFStringCreateWithCString ERROR"
+ "%s: (%s) -  CFURLCreateWithFileSystemPath ERROR"
+ "%s: (%s) - CFBundleGetIdentifier ERROR"
+ "%s: (%s) - CFStringGetCString ERROR"
+ "%s: no bundle id available for pid %d"
+ "get_bundle_id"
+ "unknown"

```
