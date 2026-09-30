## fseventsd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/FSEvents.framework/Versions/A/Support/fseventsd`

```diff

-1400.0.0.0.0
-  __TEXT.__text: 0x161e8
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__cstring: 0xcf8
+1400.100.1.0.0
+  __TEXT.__text: 0x169cc
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__cstring: 0xd0e
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0x2b11
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x640
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__oslogstring: 0x2bf7
+  __TEXT.__unwind_info: 0x348
+  __DATA_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__cfstring: 0x4a0
   __DATA.__data: 0x232

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C204AFAA-232F-30C3-94D4-6DE6F7C0A2E6
-  Functions: 362
-  Symbols:   221
-  CStrings:  443
+  UUID: 95A58207-5291-3A6A-984A-5FBB1B1BEF01
+  Functions: 361
+  Symbols:   227
+  CStrings:  451
 
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
