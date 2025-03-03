## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-548.3.0.0.0
-  __TEXT.__text: 0x2d7a4
-  __TEXT.__auth_stubs: 0x1450
+554.5.0.0.0
+  __TEXT.__text: 0x2cfa4
+  __TEXT.__auth_stubs: 0x13b0
   __TEXT.__delay_stubs: 0x160
   __TEXT.__delay_helper: 0x3b0
-  __TEXT.__const: 0x460
-  __TEXT.__cstring: 0x1b25
-  __TEXT.__oslogstring: 0x1fca
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x288
-  __AUTH_CONST.__auth_got: 0xa68
+  __TEXT.__const: 0x620
+  __TEXT.__cstring: 0x1b24
+  __TEXT.__oslogstring: 0x1f9d
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__got: 0x6f8
+  __DATA_CONST.__const: 0x260
+  __AUTH_CONST.__auth_got: 0xa18
   __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__const: 0x328
-  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__cfstring: 0x1000
   __DATA.__data: 0x94
-  __DATA.__bss: 0x861
+  __DATA.__bss: 0x1011
   __DATA_DIRTY.__data: 0x250
-  __DATA_DIRTY.__bss: 0x1648
+  __DATA_DIRTY.__bss: 0xe58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 590
-  Symbols:   1154
-  CStrings:  462
+  Functions: 606
+  Symbols:   1169
+  CStrings:  461
 
Symbols:
+ _CFStringCreateWithFormat
+ _strtoul
- __Block_object_dispose
- __CFFileCoordinateReadingItemAtURL2
- __CFURLCopyPromiseURLOfLogicalURL
- __CFURLPromiseCopyPhysicalURL
- __CFURLPromiseCopyResourcePropertyForKey
- __CFURLPromiseSetPhysicalURL
- __CFURLPromiseSetResourcePropertyForKey
- __NSConcreteStackBlock
- __kCFURLPromisePhysicalURLKey
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_wait
- _dispatch_release
CStrings:
+ "/.nofollow%s"
+ "/.nofollow/"
+ "/.resolve/"
+ "/.resolve/%u%s"
+ "file:///.file/id=%lld.%lld%s"
+ "file:///.file/id=%lld.%lld/?.resolve=%u"
- "%s: downloading %@"
- "%s: finished %@, error=%@"
- "._"
- "/.file/id=%lld.%lld"
- "DownloadCloudDocumentSync"
- "com.apple.bookmarkresolution"
- "v32@?0^{__CFURL=}8^{__CFError=}16@?<v@?>24"

```
