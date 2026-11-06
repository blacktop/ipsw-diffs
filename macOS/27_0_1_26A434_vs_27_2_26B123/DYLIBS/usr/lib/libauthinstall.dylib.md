## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1155.0.5.0.0
-  __TEXT.__text: 0xb21ac
+1155.40.8.0.0
+  __TEXT.__text: 0xb22a8
   __TEXT.__objc_methlist: 0x262c
   __TEXT.__cstring: 0x21a53
   __TEXT.__const: 0xc2c1
   __TEXT.__gcc_except_tab: 0x3b6c
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0xad5
-  __TEXT.__unwind_info: 0x29a0
+  __TEXT.__unwind_info: 0x29a8
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0xbf8
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x1630
   __AUTH_CONST.__cfstring: 0xf120
   __AUTH_CONST.__objc_const: 0x4908

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 3824
-  Symbols:   5423
+  Functions: 3826
+  Symbols:   5426
   CStrings:  4817
 
Symbols:
+ _AMAuthInstallCopyDebugPath
+ _AMAuthInstallSetDebugPath
+ _kAMSupportHttpOptionRequestHTTPAllowed
CStrings:
+ "Helsinki_Restore_Host-58.1.4"
+ "libauthinstall-1155.40.8"
- "Helsinki_Restore_Host-58.0.45"
- "libauthinstall-1155.0.5"
```
