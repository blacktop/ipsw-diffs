## profiled

> `/usr/libexec/profiled`

```diff

-  __TEXT.__text: 0xd20bc
+  __TEXT.__text: 0xd23b0
   __TEXT.__auth_stubs: 0x2800
-  __TEXT.__objc_stubs: 0x13140
-  __TEXT.__objc_methlist: 0x619c
+  __TEXT.__objc_stubs: 0x13160
+  __TEXT.__objc_methlist: 0x61a4
   __TEXT.__const: 0x12fe
-  __TEXT.__gcc_except_tab: 0x1afc
-  __TEXT.__oslogstring: 0x10240
-  __TEXT.__cstring: 0xa74a
-  __TEXT.__objc_methname: 0x16852
+  __TEXT.__gcc_except_tab: 0x1b14
+  __TEXT.__oslogstring: 0x102c0
+  __TEXT.__cstring: 0xa76a
+  __TEXT.__objc_methname: 0x16892
   __TEXT.__objc_classname: 0xc1e
   __TEXT.__objc_methtype: 0x2392
   __TEXT.__constg_swiftt: 0xdc8

   __TEXT.__swift5_types: 0xac
   __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__unwind_info: 0x1cb0
   __TEXT.__eh_frame: 0x1c0
   __DATA_CONST.__auth_got: 0x1410
   __DATA_CONST.__got: 0x2048
   __DATA_CONST.__auth_ptr: 0x2f0
   __DATA_CONST.__const: 0x2ec8
-  __DATA_CONST.__cfstring: 0x86a0
+  __DATA_CONST.__cfstring: 0x86c0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0x1e0
+  __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x6fe0
-  __DATA.__objc_selrefs: 0x53e8
+  __DATA.__objc_selrefs: 0x53f0
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x8e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2698
+  Functions: 2699
   Symbols:   1769
-  CStrings:  6839
+  CStrings:  6844
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _MCFixPermissionsOfManagedConfigurationDirectoryAndContentsFM
- _MCFixPermissionsOfSystemGroupContainerDirectoryAndContentsFM
CStrings:
+ "Failed to fix permissions of system profile library with errors %{public}@"
+ "Failed to fix permissions of user profile storage with errors %{public}@"
+ "User profiles storage check found errors: %{public}@"
+ "_fixPermissionsOnTheUserProfileStorageDirectoryAndContents"
+ "com.apple.screentime.regulatory"
- "Failed to fix permissions of device profile library with errors %{public}@"

```
