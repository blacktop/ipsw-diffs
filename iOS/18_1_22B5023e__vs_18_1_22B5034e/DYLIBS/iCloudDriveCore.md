## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3097.0.245.0.0
-  __TEXT.__text: 0x2d55e8
-  __TEXT.__auth_stubs: 0x1b70
+3097.40.3.0.0
+  __TEXT.__text: 0x2d54b8
+  __TEXT.__auth_stubs: 0x1b80
   __TEXT.__objc_methlist: 0x16688
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x78092
-  __TEXT.__oslogstring: 0x39823
+  __TEXT.__cstring: 0x78085
+  __TEXT.__oslogstring: 0x39825
   __TEXT.__gcc_except_tab: 0x1800c
   __TEXT.__ustring: 0x36
   __TEXT.__unwind_info: 0x85e8
   __TEXT.__objc_classname: 0x2388
-  __TEXT.__objc_methname: 0x3d2ef
+  __TEXT.__objc_methname: 0x3d2d1
   __TEXT.__objc_methtype: 0x762d
-  __TEXT.__objc_stubs: 0x29f80
+  __TEXT.__objc_stubs: 0x29f60
   __DATA_CONST.__got: 0x1650
-  __DATA_CONST.__const: 0x86a8
+  __DATA_CONST.__const: 0x8680
   __DATA_CONST.__objc_classlist: 0x8e0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd088
+  __DATA_CONST.__objc_selrefs: 0xd080
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x7e8
   __DATA_CONST.__objc_arraydata: 0xe00
-  __AUTH_CONST.__auth_got: 0xdc8
+  __AUTH_CONST.__auth_got: 0xdd0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x26a8
   __AUTH_CONST.__cfstring: 0x212e0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12351
+  Functions: 12350
   Symbols:   15090
-  CStrings:  21721
+  CStrings:  21720
 
Symbols:
+ _setiopolicy_np
CStrings:
+ "[CRIT] Assertion failed: setiopolicy_np(IOPOL_TYPE_VFS_IGNORE_PERMISSIONS, IOPOL_SCOPE_PROCESS, IOPOL_VFS_IGNORE_PERMISSIONS_ON) == 0%!@(MISSING)"
+ "-[BRCDownloadContent _stageWithDownloadStager:manifest:package:xattrsPackage:error:]"
- "br_setIOPolicy:type:forBlock:"
- "[CRIT] Assertion failed: getiopolicy_np(IOPOL_TYPE_VFS_IGNORE_PERMISSIONS, IOPOL_SCOPE_PROCESS) == IOPOL_VFS_IGNORE_PERMISSIONS_OFF%!@(MISSING)"
- "-[BRCDownloadContent _stageWithDownloadStager:manifest:package:xattrsPackage:error:]_block_invoke"

```
