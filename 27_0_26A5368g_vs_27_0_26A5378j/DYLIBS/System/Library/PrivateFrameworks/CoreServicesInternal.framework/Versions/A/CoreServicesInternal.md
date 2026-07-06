## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal`

```diff

-  __TEXT.__text: 0x36c58
+  __TEXT.__text: 0x369a8
   __TEXT.__lazy_helpers: 0x690
-  __TEXT.__cstring: 0x2805
+  __TEXT.__cstring: 0x2784
   __TEXT.__const: 0x4f0
   __TEXT.__oslogstring: 0x2c14
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__unwind_info: 0xcb8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x428
-  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x1a60
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0xa0
-  __AUTH_CONST.__auth_got: 0xe48
+  __AUTH_CONST.__auth_got: 0xe50
   __DATA.__data: 0x58
   __DATA.__bss: 0x490
   __DATA_DIRTY.__data: 0x290

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
-  Functions: 784
-  Symbols:   1700
-  CStrings:  879
+  Functions: 787
+  Symbols:   1706
+  CStrings:  874
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__lazy_load_got : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _Z19_FileCacheGetForURLPK7__CFURLPv
+ _ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh
+ __ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh
+ __kCFURLVolumeFSKitModuleBundleIdentifierKey
+ __kCFURLVolumeIsFSKitKey
+ __os_crash
- _ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPhPS3_
- __ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPhPS3_
- __ZL22followTaggedSymlinkURLPK7__CFURL
CStrings:
+ "_FileCacheGetForURL would have returned NULL"
- "_NSURLVolumeFSKitModuleBundleIdentifierKey"
- "_NSURLVolumeIsFSKitKey"
- "com.apple.bookmark.archive.prefer-home-relative-symlink"
- "com.apple.bookmark.resolution.always-follow-symlink"

```
