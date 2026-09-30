## rmdinspect

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/rmdinspect`

```diff

-  __TEXT.__text: 0x10ea4
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x2d20
-  __TEXT.__objc_methlist: 0xea4
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1320
+  __TEXT.__text: 0x10dec
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_stubs: 0x2ca0
+  __TEXT.__objc_methlist: 0xe94
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x1309
   __TEXT.__objc_classname: 0x47d
-  __TEXT.__objc_methname: 0x2ee8
-  __TEXT.__objc_methtype: 0x3da
+  __TEXT.__objc_methname: 0x2e6a
+  __TEXT.__objc_methtype: 0x3cc
   __TEXT.__oslogstring: 0x306
   __TEXT.__gcc_except_tab: 0x410
   __TEXT.__unwind_info: 0x468
   __DATA_CONST.__const: 0x500
-  __DATA_CONST.__cfstring: 0x1ce0
+  __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x31a0
-  __DATA.__objc_selrefs: 0xdb0
+  __DATA.__objc_selrefs: 0xd90
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x301

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/Versions/A/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 345
-  Symbols:   138
-  CStrings:  1193
+  Functions: 344
+  Symbols:   137
+  CStrings:  1185
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _RMSwitchToDaemonUserIfNeeded
- _getpwnam
- _setuid
CStrings:
+ "Deprecated. Previously used to override the user home directory path; no longer needed now that user data is stored in the protected system container."
+ "_reportInScope:"
- "@32@0:8q16@24"
- "Library/Application Support/com.apple.RemoteManagementAgent/Database/RemoteManagement.sqlite"
- "Path to user home directory to use (may be needed for user scope on macOS)."
- "_reportInScope:overrideUserScopeHomePath:"
- "_rmd"
- "_switchToRMDUserIfNeeded"
- "fileURLWithPath:"
- "stringByAppendingPathComponent:"
- "stringByStandardizingPath"

```
