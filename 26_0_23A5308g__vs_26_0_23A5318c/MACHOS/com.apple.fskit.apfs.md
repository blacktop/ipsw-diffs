## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2632.0.77.0.1
-  __TEXT.__text: 0xa8530
+2632.2.1.0.0
+  __TEXT.__text: 0xa8818
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x88f0
-  __TEXT.__cstring: 0x2e50f
+  __TEXT.__cstring: 0x2e647
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__oslogstring: 0x11b
   __TEXT.__objc_classname: 0x5b

   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1068
   __DATA.__common: 0xad8
-  __DATA.__bss: 0x1e221
+  __DATA.__bss: 0x1e229
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0D8CF634-6C87-3DEA-953C-4421BAACE5AE
-  Functions: 2331
-  Symbols:   1197
-  CStrings:  3975
+  UUID: 1479C3F0-BD1E-3F6D-ADA9-D8A89754A11C
+  Functions: 2333
+  Symbols:   1200
+  CStrings:  3980
 
Symbols:
+ _clonegroup_abort
+ _clonegroup_register_resource_fork
+ _copy_obj_abort
CStrings:
+ "%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than CLONEGROUP_ID_MIN (%u)\n"
+ "(oid 0x%llx) %s: object read was finished already\n"
+ "2632.2.1"
+ "Skipping clonegroup cross-check since INVALID flag is set\n"
+ "clone group tree (id %llu): invalid cookie key length (%u)\n"
+ "clone group tree (id %llu): invalid cookie val length (%u)\n"
+ "clone group tree: cookie group_id (%llu) or cookie_group_id (%llu) is invalid\n"
+ "clone group tree: mapping group_id (%llu) is invalid\n"
- "%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than MIN_CLONEGROUP_ID (%u)\n"
- "2632.0.77.0.1"
- "clone group tree: group_id (%llu) is invalid\n"

```
