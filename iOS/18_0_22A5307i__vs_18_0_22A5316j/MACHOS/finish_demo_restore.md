## finish_demo_restore

> `/usr/libexec/finish_demo_restore`

```diff

-216.0.0.0.0
-  __TEXT.__text: 0x3734
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x1e4
+217.0.0.0.1
+  __TEXT.__text: 0x3a38
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0xf0
-  __TEXT.__cstring: 0xd39
-  __TEXT.__objc_methname: 0x807
+  __TEXT.__cstring: 0xe29
+  __TEXT.__objc_methname: 0x837
   __TEXT.__oslogstring: 0x16
   __TEXT.__objc_classname: 0x4c
   __TEXT.__objc_methtype: 0x100
   __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0xae0
+  __DATA_CONST.__cfstring: 0xb80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x318
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_selrefs: 0x2c0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x140
   __DATA.__bss: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45
-  Symbols:   103
-  CStrings:  214
+  Functions: 46
+  Symbols:   107
+  CStrings:  222
 
Symbols:
+ _acl_get_entry
+ _acl_get_file
+ _acl_get_flag_np
+ _acl_get_flagset_np
CStrings:
+ "-[MSDContentInstaller hasInheritanceACL:]"
+ "Cannot copy %!@(MISSING) to %!@(MISSING).  Error:  %!@(MISSING)"
+ "Cannot remove item %!@(MISSING).  Error:  %!@(MISSING)"
+ "Could not read ACL from %!@(MISSING): %!s(MISSING)"
+ "Failed to read ACL flagset from %!@(MISSING): %!s(MISSING)"
+ "Parent folder of content root item has inheritance ACL: %!@(MISSING)"
+ "copyItemAtPath:toPath:error:"
+ "hasInheritanceACL:"

```
