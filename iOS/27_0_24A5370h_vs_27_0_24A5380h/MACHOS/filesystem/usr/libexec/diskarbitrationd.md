## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-  __TEXT.__text: 0x1bcfc
-  __TEXT.__auth_stubs: 0x1720
+  __TEXT.__text: 0x1f944
+  __TEXT.__auth_stubs: 0x1710
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x33fe
-  __TEXT.__const: 0x80
-  __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__cstring: 0x3368
+  __TEXT.__const: 0x120
+  __TEXT.__oslogstring: 0x1928
+  __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methname: 0x5d7
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x610
-  __DATA_CONST.__const: 0xef8
+  __TEXT.__unwind_info: 0x630
+  __DATA_CONST.__const: 0xf38
   __DATA_CONST.__cfstring: 0x21a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xba0
+  __DATA_CONST.__auth_got: 0xb98
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x168

   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130
-  __DATA.__bss: 0xdb0
+  __DATA.__bss: 0xdb8
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 530
-  Symbols:   421
-  CStrings:  972
+  Functions: 556
+  Symbols:   420
+  CStrings:  1107
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ __os_log_debug_impl
+ _objc_retain_x2
- _closelog
- _objc_retain_x28
- _openlog
CStrings:
+ "  dispatched response, id = %016llX:%016llX, kind = %s, disk = %{private}s, orphaned."
+ "%s: Failed to allocate retry context, falling through to cleanup"
+ "%{private}s"
+ "Skipping apfs_userfs.fs as apfsUseFSKitModule pref is on"
+ "__DASetIdleTimer %d %p"
+ "unable to copy disk description, id = %{private}s (status code 0x%08X)."
+ "unable to create session, id = %{private}s [%d] (status code 0x%08X)."
+ "unable to dispatch response, id = %016llX:%016llX, disk = %{private}s (status code 0x%08X)."
+ "unable to get disk claim state, id = %{private}s (status code 0x%08X)."
+ "unable to get disk options, id = %{private}s (status code 0x%08X)."
+ "unable to queue solicitation, id = %016llX:%016llX, kind = %s, disk = %{private}s (status code 0x%08X)."
+ "unable to set disk adoption, id = %{private}s (status code 0x%08X)."
+ "unable to set disk options, id = %{private}s (status code 0x%08X)."
+ "unable to unclaim disk, id = %{private}s (status code 0x%08X)."
- "  dispatched response, id = %016llX:%016llX, kind = %s, disk = %s, orphaned."
- "%{public}s"
- "DALog.c"
- "DALogDebug"
- "Failed to allocate retry context, falling through to cleanup"
- "Skipping apfs.fs as apfsUseFSKitModule pref is on"
- "__DAProbeWithFSKit_block_invoke_2"
- "__DASetIdleTimer %d %x"
- "__gDALogDebugHeaderNext"
- "apfs.fs"
- "unable to copy disk description, id = %s (status code 0x%08X)."
- "unable to create session, id = %s [%d] (status code 0x%08X)."
- "unable to dispatch response, id = %016llX:%016llX, disk = %s (status code 0x%08X)."
- "unable to get disk claim state, id = %s (status code 0x%08X)."
- "unable to get disk options, id = %s (status code 0x%08X)."
- "unable to queue solicitation, id = %016llX:%016llX, kind = %s, disk = %s (status code 0x%08X)."
- "unable to set disk adoption, id = %s (status code 0x%08X)."
- "unable to set disk options, id = %s (status code 0x%08X)."
- "unable to unclaim disk, id = %s (status code 0x%08X)."

```
