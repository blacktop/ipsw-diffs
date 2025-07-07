## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-623.0.0.0.0
-  __TEXT.__text: 0x38274
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x225c
-  __TEXT.__const: 0x2b4
+628.0.0.0.0
+  __TEXT.__text: 0x38b18
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_methlist: 0x2294
+  __TEXT.__const: 0x2c4
   __TEXT.__oslogstring: 0x625a
-  __TEXT.__cstring: 0x14a7
+  __TEXT.__cstring: 0x1587
   __TEXT.__gcc_except_tab: 0x868
   __TEXT.__swift5_typeref: 0x38e
   __TEXT.__swift5_fieldmd: 0x9c

   __TEXT.__swift5_reflstr: 0x6b
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_capture: 0x114
+  __TEXT.__swift5_capture: 0x124
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xd88
-  __TEXT.__eh_frame: 0x220
+  __TEXT.__unwind_info: 0xd60
+  __TEXT.__eh_frame: 0x248
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0xb194
-  __TEXT.__objc_methtype: 0x19dd
-  __TEXT.__objc_stubs: 0x9260
+  __TEXT.__objc_methname: 0xb1ff
+  __TEXT.__objc_methtype: 0x1a09
+  __TEXT.__objc_stubs: 0x92c0
   __DATA_CONST.__got: 0x898
   __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29b0
+  __DATA_CONST.__objc_selrefs: 0x29d0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0xb20
-  __AUTH_CONST.__objc_const: 0x5990
+  __AUTH_CONST.__auth_got: 0x890
+  __AUTH_CONST.__const: 0x5d8
+  __AUTH_CONST.__cfstring: 0xbc0
+  __AUTH_CONST.__objc_const: 0x5998
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x208
-  __DATA.__data: 0xc50
+  __DATA.__data: 0xc60
   __DATA.__bss: 0xa
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x758
-  __DATA_DIRTY.__data: 0x420
+  __DATA_DIRTY.__data: 0x430
   __DATA_DIRTY.__bss: 0x60
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1F2FBAC0-A442-394C-AFC9-8B48BD8CC198
-  Functions: 1034
-  Symbols:   4162
-  CStrings:  2269
+  UUID: CF3C5FED-82E0-3528-B474-32EA9AA0C0D7
+  Functions: 1041
+  Symbols:   4171
+  CStrings:  2284
 
Symbols:
+ -[UNSNotificationSettingsService _modifySection:withKeyValues:]
+ -[UNSNotificationSettingsService setSourceSettings:]
+ -[UNSUserNotificationServerSettingsConnectionListener setSourceSettings:completionHandler:]
+ GCC_except_table21
+ __PROTOCOLS__TtC23UserNotificationsServerP33_6CD0587E614EF2F90D8E9A94F9DE973D20SummaryServiceHelper.32
+ _block_copy_helper.41
+ _block_copy_helper.8
+ _block_descriptor.10
+ _block_descriptor.43
+ _block_destroy_helper.42
+ _block_destroy_helper.9
+ _objc_msgSend$_modifySection:withKeyValues:
+ _objc_msgSend$setSourceSettings:
+ _objc_msgSend$unsignedIntegerValue
+ _objectdestroy.3Tm
- GCC_except_table18
- __PROTOCOLS__TtC23UserNotificationsServerP33_6CD0587E614EF2F90D8E9A94F9DE973D20SummaryServiceHelper.28
- _block_copy_helper.37
- _block_copy_helper.4
- _block_descriptor.39
- _block_descriptor.6
- _block_destroy_helper.38
- _block_destroy_helper.5
- _objectdestroyTm
CStrings:
+ "[%@]: Raw value of '%lu' cannot be mapped to UNNotificationSetting for '%@'"
+ "[%@]: Raw value of '%lu' cannot be mapped to UNShowPreviewsSetting for '%@'"
+ "[%@]: Source does not exist"
+ "_modifySection:withKeyValues:"
+ "setSourceSettings:"
+ "setSourceSettings:completionHandler:"
+ "unsignedIntegerValue"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"

```
