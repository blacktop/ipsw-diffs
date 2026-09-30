## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-128.100.159.0.0
-  __TEXT.__text: 0x1fd584
+128.100.161.0.0
+  __TEXT.__text: 0x1fe5c8
   __TEXT.__auth_stubs: 0x37d0
   __TEXT.__objc_methlist: 0x5a90
-  __TEXT.__const: 0x12a8a
-  __TEXT.__cstring: 0xe667
-  __TEXT.__oslogstring: 0x7022
+  __TEXT.__const: 0x12a7a
+  __TEXT.__cstring: 0xe697
+  __TEXT.__oslogstring: 0x7272
   __TEXT.__gcc_except_tab: 0x146c
   __TEXT.__constg_swiftt: 0x6dd0
-  __TEXT.__swift5_typeref: 0x53b6
+  __TEXT.__swift5_typeref: 0x53d0
   __TEXT.__swift5_fieldmd: 0x671c
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_reflstr: 0x5938

   __TEXT.__swift_as_ret: 0x6f4
   __TEXT.__swift5_protos: 0x118
   __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__unwind_info: 0x8028
+  __TEXT.__unwind_info: 0x8050
   __TEXT.__eh_frame: 0x11e38
   __TEXT.__objc_classname: 0xc1d
-  __TEXT.__objc_methname: 0xce8b
+  __TEXT.__objc_methname: 0xceb2
   __TEXT.__objc_methtype: 0x283b
-  __TEXT.__objc_stubs: 0x8e60
-  __DATA_CONST.__got: 0x1060
-  __DATA_CONST.__const: 0x900
+  __TEXT.__objc_stubs: 0x8ea0
+  __DATA_CONST.__got: 0x1068
+  __DATA_CONST.__const: 0x950
   __DATA_CONST.__objc_classlist: 0x890
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39c8
+  __DATA_CONST.__objc_selrefs: 0x39d8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0x4a0
   __AUTH_CONST.__auth_got: 0x1c00
-  __AUTH_CONST.__auth_ptr: 0x15f0
-  __AUTH_CONST.__const: 0x99b0
-  __AUTH_CONST.__cfstring: 0x4f80
+  __AUTH_CONST.__auth_ptr: 0x1710
+  __AUTH_CONST.__const: 0x9a00
+  __AUTH_CONST.__cfstring: 0x4fa0
   __AUTH_CONST.__objc_const: 0x12a10
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   __AUTH.__objc_data: 0x5418
   __AUTH.__data: 0xa3f0
   __DATA.__objc_ivar: 0x754
-  __DATA.__data: 0x6660
+  __DATA.__data: 0x66b0
   __DATA.__bss: 0x19ad0
   __DATA.__common: 0xad0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos
   - /System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks
+  - /System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9412
-  Symbols:   2796
-  CStrings:  5810
+  Functions: 9426
+  Symbols:   2803
+  CStrings:  5826
 
Symbols:
+ _OBJC_CLASS_$_WLWelcomeViewController
CStrings:
+ "completed migration. zoom_enabled=%{bool}d"
+ "completed move to ios. success=%{bool}d, zoom_enabled=%{bool}d"
+ "did reset the device. delegate=%@"
+ "enable_os_migration"
+ "failed to migrate data and will reset the device."
+ "failed to migrate data."
+ "migrated and will send the callback. delegate=%@, success=%d, zoom_enabled=%d"
+ "sent the callback. delegate=%@, success=%d, zoom_enabled=%d"
+ "setCompletionHandler:"
+ "setResetHandler:"
+ "there is no delegate."
+ "v20@?0B8@\"WLSettings\"12"
+ "will reset the device. delegate=%@"
+ "will return the migration view controller."
+ "will return the migration view controller. delegate=%@"
+ "will return welcome view controller."

```
