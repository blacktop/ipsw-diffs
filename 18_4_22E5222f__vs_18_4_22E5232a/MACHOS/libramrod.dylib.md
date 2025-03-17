## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3196.100.165.0.0
-  __TEXT.__text: 0xe1de0
-  __TEXT.__auth_stubs: 0x2830
+3196.100.165.0.2
+  __TEXT.__text: 0xe2520
+  __TEXT.__auth_stubs: 0x2880
   __TEXT.__objc_methlist: 0x109c
-  __TEXT.__cstring: 0x287a9
+  __TEXT.__cstring: 0x289be
   __TEXT.__const: 0x94938
   __TEXT.__gcc_except_tab: 0xb20
   __TEXT.__oslogstring: 0x1ad2
-  __TEXT.__unwind_info: 0x1d78
+  __TEXT.__unwind_info: 0x1d80
   __TEXT.__eh_frame: 0x410
   __TEXT.__objc_classname: 0x18c
   __TEXT.__objc_methname: 0x2751
   __TEXT.__objc_methtype: 0xb58
   __TEXT.__objc_stubs: 0x2740
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x1ee8
+  __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc08
-  __AUTH_CONST.__auth_got: 0x1430
+  __AUTH_CONST.__auth_got: 0x1458
   __AUTH_CONST.__auth_ptr: 0xa0
   __AUTH_CONST.__const: 0x1f50
   __AUTH_CONST.__cfstring: 0xbfc0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2714
-  Symbols:   1876
-  CStrings:  6059
+  Functions: 2717
+  Symbols:   1884
+  CStrings:  6076
 
Symbols:
+ _copyfile
+ _copyfile_skip_existing_callback
+ _copyfile_state_alloc
+ _copyfile_state_free
+ _copyfile_state_set
+ _mkpath_np
+ _ramrod_copyfile_callback
+ _ramrod_populate_preboot_volume_for_nerd
CStrings:
+ "%s already exists\n"
+ "%s/NeRD/%s"
+ "/AppleInternal/Diags/bin/diag.img4"
+ "/System/Library/Caches/apticket.der"
+ "/System/Library/Caches/com.apple.kernelcaches/kernelcache"
+ "/usr/local/standalone/firmware/"
+ "/usr/standalone/firmware/Bora/"
+ "Copying from path: %s\n"
+ "boot object '%s' does not exist, skipping\n"
+ "copyfile error during %d\n"
+ "copyfile error during %d processing %s\n"
+ "failed to allocate copyfile state\n"
+ "failed to copy '%s' to '%s': %d\n"
+ "failed to set copyfile callback\n"
+ "skipping symlink %s\n"
+ "unable to create directory %s: %d\n"
+ "unable to parse '%s'\n"

```
