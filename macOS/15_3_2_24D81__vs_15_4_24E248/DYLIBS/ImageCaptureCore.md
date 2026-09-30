## ImageCaptureCore

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/A/ImageCaptureCore`

```diff

-1936.2.1.0.0
-  __TEXT.__text: 0x6445c
+1936.4.3.0.0
+  __TEXT.__text: 0x640f4
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x5294
+  __TEXT.__objc_methlist: 0x58a4
   __TEXT.__cstring: 0x9fec
   __TEXT.__const: 0x1dc
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0x480
   __TEXT.__gcc_except_tab: 0x10dc
-  __TEXT.__unwind_info: 0x1250
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_classname: 0x5a1
   __TEXT.__objc_methname: 0xceb9
   __TEXT.__objc_methtype: 0x11db
   __TEXT.__objc_stubs: 0x8aa0
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fc8
+  __DATA_CONST.__objc_selrefs: 0x3170
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x2bf8
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x1208
   __AUTH_CONST.__cfstring: 0xd2c0
-  __AUTH_CONST.__objc_const: 0x89d0
+  __AUTH_CONST.__objc_const: 0x7e18
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0x2440
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B0876427-7A40-3291-96A5-F508947B5649
-  Functions: 2150
-  Symbols:   4681
+  UUID: D6B706BB-A9AE-3D83-8A0A-5CE11E564A50
+  Functions: 2160
+  Symbols:   4690
   CStrings:  6077
 
Symbols:
+ +[ICCommandCenter defaultCenter].cold.2
+ +[ICDeviceAccessManager sharedAccessManager].cold.1
+ +[ICScannerDeviceBrowser defaultBrowser].cold.1
+ -[ICCommandCenter addSelectorToInterface:selectorString:origin:].cold.1
+ -[ICDeviceManager addSelectorToInterface:selectorString:origin:].cold.1
+ -[NSArray(ImageCaptureCoreAdditions) copyGroupIntoDictionary:].cold.1
+ -[PTPCameraDeviceManager addSelectorToInterface:selectorString:origin:].cold.1
+ ICLocalizedString.cold.1
+ ICSubtractTimes.cold.1
+ SharedICDeviceHardwareHandler.cold.1
+ __ICLogDateString.cold.1
+ __ICOSLogCreate.cold.1
- GCC_except_table65
- _OUTLINED_FUNCTION_6

```
