## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-710.17.103.0.0
-  __TEXT.__text: 0xbe82c
-  __TEXT.__auth_stubs: 0x1c60
-  __TEXT.__objc_methlist: 0x64d8
+710.22.200.0.0
+  __TEXT.__text: 0xbf9c8
+  __TEXT.__auth_stubs: 0x1c70
+  __TEXT.__objc_methlist: 0x6510
   __TEXT.__const: 0x2484
-  __TEXT.__gcc_except_tab: 0x6da8
-  __TEXT.__cstring: 0x137ec
-  __TEXT.__oslogstring: 0x97eb
+  __TEXT.__gcc_except_tab: 0x6e50
+  __TEXT.__cstring: 0x13894
+  __TEXT.__oslogstring: 0x9aa8
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2f60
+  __TEXT.__unwind_info: 0x2f80
   __TEXT.__objc_classname: 0x104f
-  __TEXT.__objc_methname: 0x14eea
-  __TEXT.__objc_methtype: 0x4aca
-  __TEXT.__objc_stubs: 0xb5a0
-  __DATA_CONST.__got: 0xa88
+  __TEXT.__objc_methname: 0x14fd4
+  __TEXT.__objc_methtype: 0x4af6
+  __TEXT.__objc_stubs: 0xb640
+  __DATA_CONST.__got: 0xa90
   __DATA_CONST.__const: 0x3838
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47e0
+  __DATA_CONST.__objc_selrefs: 0x4808
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x418
-  __AUTH_CONST.__auth_got: 0xe40
+  __AUTH_CONST.__auth_got: 0xe48
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3290
-  __AUTH_CONST.__cfstring: 0x108e0
-  __AUTH_CONST.__objc_const: 0xcd70
+  __AUTH_CONST.__const: 0x32b0
+  __AUTH_CONST.__cfstring: 0x10940
+  __AUTH_CONST.__objc_const: 0xcd90
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3659
-  Symbols:   5459
-  CStrings:  7044
+  Functions: 3666
+  Symbols:   5468
+  CStrings:  7064
 
Symbols:
+ __os_log_send_and_compose_impl
+ _PFErrorDomain
CStrings:
+ "PLFileBackedLogger: Failed to open log file. Error: %!@(MISSING)"
+ "PLFileBackedLogger: Backend logging requires a file URL with an expected path extension %!{(MISSING)public}@"
+ "_inlock_createLoggerRecordWithLogFileURL:logRotate:didRebuildLogArchive:error:"
+ "PLFileBackedLogger: Backend logging failed to removed corrupt log file %!{(MISSING)public}@. Error: %!@(MISSING)"
+ "PLFileBackedLogger: Backend logging requires a file URL. Url specified is a directory %!{(MISSING)public}@"
+ "Log archive recreated on %!@(MISSING)"
+ "PLFileBackedLogger: Failed to create logger record. Invalidating logger initialization. Error: %!@(MISSING)"
+ "url parameter is not a file url"
+ "PLFileBackedLogger: Backend logging failed to determine the url status for %!{(MISSING)public}@. Error: %!@(MISSING)"
+ "url parameter is a directory"
+ "PLFileBackedLogger: Unable to write-open file descriptor at %!@(MISSING): Error: %!@(MISSING)"
+ "PLXPC Client: locationOfInterestUpdateWithError:"
+ "PLFileBackedLogger: open url found a corrupt log file. Attempting repair for: %!{(MISSING)public}@"
+ "-[PLAssetsdDebugClient locationOfInterestUpdateWithError:]_block_invoke"
+ "locationOfInterestUpdateWithReply:"
+ "B48@0:8^@16@24@32^@40"
+ "_openLoggerAtURL:logRotate:error:"
+ "@44@0:8@16B24^B28^@36"
+ "url filename is of an unknown type"
+ "locationOfInterestUpdateWithError:"
+ "_removeAndCreateLoggerAtURL:logRotate:error:"
+ "_getResourceValue:key:url:error:"
- "openLoggerAtURL:logRotate:"
- "PLFileBackedLogger: Unable to write-open file descriptor at %!@(MISSING): Error (%!d(MISSING)):%!s(MISSING)"

```
