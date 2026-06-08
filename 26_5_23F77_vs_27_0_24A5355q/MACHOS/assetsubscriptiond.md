## assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

-3525.2.1.0.0
-  __TEXT.__text: 0x908
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x220
+3600.61.1.0.0
+  __TEXT.__text: 0x974
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x4c
   __TEXT.__const: 0x74
-  __TEXT.__objc_methname: 0x154
-  __TEXT.__cstring: 0x244
-  __TEXT.__oslogstring: 0x11f
-  __TEXT.__objc_classname: 0x13
+  __TEXT.__objc_methname: 0x1ae
+  __TEXT.__cstring: 0x276
+  __TEXT.__oslogstring: 0x15a
+  __TEXT.__objc_classname: 0x10
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x88
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x98
+  __DATA.__objc_selrefs: 0xb8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x28

   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5635271D-3C4F-323D-88ED-481C0B4A8722
-  Functions: 12
-  Symbols:   58
-  CStrings:  52
+  UUID: CDAA4039-6004-3A7C-B7B7-F16976FBB372
+  Functions: 13
+  Symbols:   63
+  CStrings:  59
 
Symbols:
+ _OBJC_CLASS_$_UAFCommonUtilities
+ _OBJC_CLASS_$_UAFConfiguration
+ _OBJC_CLASS_$_UAFRootsV2AssetSet
+ _notify_register_dispatch
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s Received XPC event from notifyd: %{public}s"
+ "%s Sending notifications for installed asset roots"
+ "assetRootSupported"
+ "com.apple.mobile.keybagd.first_unlock"
+ "hasInstalledRoots"
+ "isInternalInstall"
+ "sendNotificationsForInstalledRoots"
+ "v12@?0i8"
- "%s Received XPC event from notifyd: %s"

```
