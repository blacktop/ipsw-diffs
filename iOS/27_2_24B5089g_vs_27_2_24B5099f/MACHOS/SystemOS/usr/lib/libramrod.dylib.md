## libramrod.dylib

> `/usr/lib/libramrod.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_classrefs`
- `__DATA.__data`

```diff

-3696.40.12.0.1
-  __TEXT.__text: 0xee548
+3696.40.14.0.1
+  __TEXT.__text: 0xee04c
   __TEXT.__objc_methlist: 0x119c
-  __TEXT.__cstring: 0x2beef
+  __TEXT.__cstring: 0x2bd87
   __TEXT.__const: 0x79130
   __TEXT.__gcc_except_tab: 0xb6c
   __TEXT.__oslogstring: 0xb92
-  __TEXT.__unwind_info: 0x2a10
+  __TEXT.__unwind_info: 0x29f8
   __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x2920
-  __TEXT.__auth_stubs: 0x2b50
+  __TEXT.__auth_stubs: 0x2b20
   __TEXT.__objc_classname: 0x18b
   __TEXT.__objc_methname: 0x29fe
   __TEXT.__objc_methtype: 0xb58

   __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x20b8
-  __AUTH_CONST.__cfstring: 0xc4c0
+  __AUTH_CONST.__cfstring: 0xc400
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x15b0
+  __AUTH_CONST.__auth_got: 0x1598
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x318
   __DATA.__objc_classrefs: 0x128

   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
-  - /usr/lib/updaters/libBMCMCUUpdater.dylib
-  Functions: 2874
-  Symbols:   1896
-  CStrings:  6388
+  Functions: 2869
+  Symbols:   1893
+  CStrings:  6377
 
Symbols:
- _BMCMCUUpdaterCleanupDeviceInfo
- _BMCMCUUpdaterGetDeviceInfo
- _BMCMCUUpdaterUpdateDevice
CStrings:
- "%s: %s failed\n"
- "%s: bad argument - no options"
- "%s: copy_available_fud_image_names returned NULL"
- "%s: failed to copy fud data for: %@"
- "%s: failed to get device name and tag from %s\n"
- "/usr/lib/updaters/libBMCMCUUpdater.dylib"
- "BMCMCUUpdaterGetDeviceInfo"
- "Could not find: %s, skipping update\n"
- "device has no BMC MCU, skipping update\n"
- "libBMCMCUUpdater.dylib"
- "update_bmc_mcu"
```
