## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

```diff

-  __TEXT.__text: 0x15a84
+  __TEXT.__text: 0x15c28
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x336e
-  __TEXT.__oslogstring: 0x1559
+  __TEXT.__cstring: 0x3383
+  __TEXT.__oslogstring: 0x1665
   __TEXT.__const: 0x398
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__unwind_info: 0x618
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18d0
+  __DATA_CONST.__const: 0x1870
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__cfstring: 0x1700
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x208
   __DATA.__data: 0x958
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 594
-  Symbols:   1779
-  CStrings:  789
+  Functions: 598
+  Symbols:   1800
+  CStrings:  794
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFPropertyListCreateWithStream
+ _CFReadStreamClose
+ _CFReadStreamCreateWithFile
+ _CFReadStreamOpen
+ _CFURLCreateFromFileSystemRepresentation
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
- ___TCCAccessCheckIfDisclosurePromptIsNeeded_block_invoke
- ___TCCAccessCheckIfDisclosurePromptIsNeeded_block_invoke_2
CStrings:
+ "%{public}s for bundleID: %s URL for cache: %s"
+ "%{public}s for bundleID: %s URL is empty)"
+ "%{public}s for bundleID: %s Unable to create read stream for URL: %s"
+ "%{public}s for bundleID: %s Unable to create stream for URL: %s"
+ "%{public}s: %s needs prompt for disclosure: %d"
+ "%{public}s: plist decode failed (bundleID: %s)"
+ "/private/var/mobile/Library/ManagedAppPrivacy/managed_disclosure_cache.plist"
- "TCCAccessCheckIfDisclosurePromptIsNeeded() IPC"
- "TCCAccessCheckIfDisclosurePromptIsNeeded_block_invoke_2"

```
