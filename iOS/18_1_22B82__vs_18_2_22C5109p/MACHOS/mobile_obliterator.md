## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-320.42.1.0.0
-  __TEXT.__text: 0x15028
+320.60.2.0.0
+  __TEXT.__text: 0x15284
   __TEXT.__auth_stubs: 0x13f0
   __TEXT.__objc_stubs: 0x580
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x8d42
+  __TEXT.__cstring: 0x8e34
   __TEXT.__const: 0x688
   __TEXT.__objc_methname: 0x3ff
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__unwind_info: 0x3d0
   __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x8

   __DATA.__objc_selrefs: 0x170
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x520
+  __DATA.__data: 0x920
   __DATA.__common: 0x11c
-  __DATA.__bss: 0x4b0
+  __DATA.__bss: 0x4f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libz.1.dylib
   Functions: 222
   Symbols:   369
-  CStrings:  1092
+  CStrings:  1100
 
Symbols:
+ _objc_release_x23
- _objc_release_x21
CStrings:
+ "%!s(MISSING): %!s(MISSING) volume %!s(MISSING) is already mounted at '%!s(MISSING)'"
+ "%!s(MISSING): Cleaning up the Update volume"
+ "%!s(MISSING): Failed to mount %!s(MISSING) volume (%!s(MISSING)) with error %!d(MISSING)"
+ "%!s(MISSING): Failed to unmount the %!s(MISSING) volume: %!s(MISSING)"
+ "%!s(MISSING): Found Update volume device %!s(MISSING), default mount point '%!s(MISSING)'"
+ "%!s(MISSING): Successfully mounted %!s(MISSING) volume"
+ "%!s(MISSING): Successfully unmounted the %!s(MISSING) volume"
+ "%!s(MISSING): Unknown or unsupported volume role 0x%!x(MISSING)"
+ "%!s(MISSING): Warning: %!s(MISSING) volume device-node/default-mount unknown!"
+ "%!s(MISSING): safeObliterate: Cleaning Update volume"
+ "Hardware"
+ "Update"
+ "epdm_fixup_update_volume"
+ "epdm_skip_update_cleanup=1"
+ "try_mount_volume_by_role"
+ "unmount_volume_by_role"
- "%!s(MISSING): Failed to mount Hardware volume"
- "%!s(MISSING): Failed to unmount the Hardware volume: %!s(MISSING)"
- "%!s(MISSING): Hardware volume %!s(MISSING) is already mounted at '%!s(MISSING)'"
- "%!s(MISSING): Successfully mounted Hardware volume"
- "%!s(MISSING): Successfully unmounted the Hardware volume"
- "%!s(MISSING): Warning: Hardware volume device-node/default-mount unknown!"
- "try_mount_hw_volume"
- "unmount_hw_volume"

```
