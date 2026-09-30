## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3196.100.145.0.3
-  __TEXT.__text: 0xe18bc
-  __TEXT.__auth_stubs: 0x2860
+3196.100.158.0.1
+  __TEXT.__text: 0xe2320
+  __TEXT.__auth_stubs: 0x2880
   __TEXT.__objc_methlist: 0x109c
-  __TEXT.__cstring: 0x28580
+  __TEXT.__cstring: 0x2891d
   __TEXT.__const: 0x94938
-  __TEXT.__gcc_except_tab: 0xae4
+  __TEXT.__gcc_except_tab: 0xb20
   __TEXT.__oslogstring: 0x1ad2
-  __TEXT.__unwind_info: 0x1d68
+  __TEXT.__unwind_info: 0x1d80
   __TEXT.__eh_frame: 0x410
   __TEXT.__objc_classname: 0x18c
   __TEXT.__objc_methname: 0x2751
   __TEXT.__objc_methtype: 0xb58
   __TEXT.__objc_stubs: 0x2740
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x1f10
+  __DATA_CONST.__const: 0x1ee8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc08
-  __AUTH_CONST.__auth_got: 0x1448
+  __AUTH_CONST.__auth_got: 0x1458
   __AUTH_CONST.__auth_ptr: 0xa0
-  __AUTH_CONST.__const: 0x1f30
-  __AUTH_CONST.__cfstring: 0xbe20
+  __AUTH_CONST.__const: 0x1f50
+  __AUTH_CONST.__cfstring: 0xbfc0
   __AUTH_CONST.__objc_const: 0x1990
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x5a0
-  __AUTH.__data: 0x828
+  __AUTH.__data: 0x858
   __DATA.__objc_classrefs: 0x120
   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0x2388
-  __DATA.__bss: 0xaf0
+  __DATA.__bss: 0xb00
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2708
-  Symbols:   1882
-  CStrings:  6035
+  Functions: 2717
+  Symbols:   1884
+  CStrings:  6072
 
Symbols:
+ _AMSupportCreateDataFromMappedFileURL
+ _CFURLCreateWithFileSystemPath
+ _ramrod_device_has_int
- _ramrod_verify_resize_main_os_container
CStrings:
+ "%s: failed to copy updater functions"
+ "%s: failed to copy updater options"
+ "%s: failed to create BasebandUpdater obj"
+ "%s: failed to perform manifest check on BasebandUpdater"
+ "%s: failed to populate baseband updater context object"
+ "%s: failed to prep perform_manifest_check_baseband"
+ "%s: invalid create updater function"
+ "%s: invalid execute cmd updater function"
+ "%s: invalid options"
+ "%s: malloc failed for baseband updater context object"
+ "%s: updater library not found: %s"
+ "--slot=%d"
+ "/usr/lib/libBBUpdaterDynamic.dylib"
+ "????"
+ "BasebandChipset"
+ "BasebandManifestCheck"
+ "BasebandUpdater"
+ "Boolean _ramrod_load_ap_nonce_slot_from_data(CFDataRef, int *)"
+ "Boolean _ramrod_load_sep_nonce_slot_from_data(CFDataRef, int *)"
+ "Entering: %s\n"
+ "Failed to create_baseband_update_options"
+ "INFO: %s == %d\n"
+ "Missing updater options - this is fatal\n"
+ "Overriding baseband update options with limited context"
+ "Updater not supported\n"
+ "WARNING: %s is missing or of invalid type.\n"
+ "WARNING: failed to create path URL from: %s.\n"
+ "WARNING: failed to create path string from: %s.\n"
+ "WARNING: failed to open path %s with error: %d\n"
+ "WARNING: failed to read %s cf number.\n"
+ "WARNING: failed to read IM4R.\n"
+ "WARNING: sep_data == NULL in %s. Will return default.\n"
+ "Warning: No snid stitched to sep being loaded, will attempt to use flashing slot as proxy.\n"
+ "_ramrod_load_int_from_im4r_tag_in_data"
+ "await_update_baseband"
+ "baseband_postseal"
+ "creating BasebandUpdater obj\n"
+ "failed to copy updater functions\n"
+ "failed to copy updater options\n"
+ "failed to create BasebandUpdater obj\n"
+ "failed to perform manifest check on BasebandUpdater\n"
+ "failed to populate baseband updater context object\n"
+ "failed to prep perform_manifest_check_baseband\n"
+ "int"
+ "invalid create updater function\n"
+ "invalid execute cmd updater function\n"
+ "invalid options\n"
+ "malloc failed for baseband updater context object\n"
+ "operation not supported\n"
+ "outValue"
+ "perform_manifest_check_baseband"
+ "restoreInfo failed to alloc\n"
+ "update_baseband"
+ "updater library not found: %s\n"
- "%s: Failed resizing %s container back to its original size. original_container_size: %llu, post_check_container_size: %llu"
- "%s: Failed resizing APFS %s container to its original size. status: %d, errno: %d."
- "/AppleInternal/Diags/bin/diag.img4"
- "/System/Library/Caches/apticket.der"
- "/System/Library/Caches/com.apple.kernelcaches/kernelcache"
- "/usr/local/standalone/firmware/"
- "INFO: will use ap slot %d\n"
- "INFO: will use sep slot %d\n"
- "Successfuly shrank and grew APFS %s container to its original size, original_container_size: %llu.\n"
- "WARNING: anid in llb is of invalid type. Will write default.\n"
- "WARNING: failed to fetch llb for sandcat slot check. Will write default.\n"
- "WARNING: failed to fetch sep for sandcat slot check. Will write default.\n"
- "WARNING: failed to read ap slot cf number. Will write default.\n"
- "WARNING: failed to read sep slot cf number. Will write default.\n"
- "WARNING: snid in sep is of invalid type. Will write default.\n"
- "ramrod_verify_resize_main_os_container"
- "ramrod_verify_resize_main_os_container failed: %@"

```
