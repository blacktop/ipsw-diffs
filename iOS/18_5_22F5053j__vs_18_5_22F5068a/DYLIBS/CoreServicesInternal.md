## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-554.8.0.0.0
-  __TEXT.__text: 0x2cfb4
-  __TEXT.__auth_stubs: 0x13c0
+554.9.0.0.0
+  __TEXT.__text: 0x2d714
+  __TEXT.__auth_stubs: 0x1480
   __TEXT.__delay_stubs: 0x160
   __TEXT.__delay_helper: 0x3b0
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x1b24
-  __TEXT.__oslogstring: 0x1f9d
+  __TEXT.__const: 0x630
+  __TEXT.__cstring: 0x1b86
+  __TEXT.__oslogstring: 0x1fca
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__got: 0x6f8
-  __DATA_CONST.__const: 0x260
-  __AUTH_CONST.__auth_got: 0xa20
+  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__const: 0x288
+  __AUTH_CONST.__auth_got: 0xa80
   __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__const: 0x328
-  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__cfstring: 0x1020
   __DATA.__data: 0x94
   __DATA.__bss: 0x1011
   __DATA_DIRTY.__data: 0x250

   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 606
-  Symbols:   1830
-  CStrings:  461
+  Functions: 609
+  Symbols:   1851
+  CStrings:  466
 
Symbols:
+ __Block_object_dispose
+ __CFFileCoordinateReadingItemAtURL2
+ __CFURLCopyPromiseURLOfLogicalURL
+ __CFURLPromiseCopyPhysicalURL
+ __CFURLPromiseCopyResourcePropertyForKey
+ __CFURLPromiseSetPhysicalURL
+ __CFURLPromiseSetResourcePropertyForKey
+ __NSConcreteStackBlock
+ __ZL25DownloadCloudDocumentSyncPK7__CFURL
+ __ZL37createByResolvingBookmarkDataInternalPK13__CFAllocatorPK8__CFDatamPK7__CFURLPK9__CFArrayPhPP9__CFErrorPS7_
+ __ZL37createByResolvingBookmarkDataInternalPK13__CFAllocatorPK8__CFDatamPK7__CFURLPK9__CFArrayPhPP9__CFErrorPS7_.cold.1
+ __ZL37createByResolvingBookmarkDataInternalPK13__CFAllocatorPK8__CFDatamPK7__CFURLPK9__CFArrayPhPP9__CFErrorPS7_.cold.2
+ ____ZL25DownloadCloudDocumentSyncPK7__CFURL_block_invoke
+ ___block_descriptor_tmp.16
+ __kCFURLPromisePhysicalURLKey
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_release
- __CFURLCreateByResolvingBookmarkData.cold.3
- __CFURLCreateByResolvingBookmarkData.cold.4
CStrings:
+ "%s: downloading %@"
+ "%s: finished %@, error=%@"
+ "DownloadCloudDocumentSync"
+ "com.apple.bookmarkresolution"
+ "v32@?0^{__CFURL=}8^{__CFError=}16@?<v@?>24"

```
