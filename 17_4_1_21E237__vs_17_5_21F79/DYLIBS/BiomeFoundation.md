## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-123.5.23.1.0
-  __TEXT.__text: 0x26e14
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x1820
-  __TEXT.__const: 0xf0
+123.9.0.1.0
+  __TEXT.__text: 0x26f68
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_methlist: 0x1828
+  __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x4089
-  __TEXT.__oslogstring: 0x2589
+  __TEXT.__oslogstring: 0x25bd
   __TEXT.__gcc_except_tab: 0xa5c
   __TEXT.__dlopen_cstrs: 0x20c
-  __TEXT.__unwind_info: 0x98c
+  __TEXT.__unwind_info: 0x9a8
   __TEXT.__objc_classname: 0x411
-  __TEXT.__objc_methname: 0x3cbe
+  __TEXT.__objc_methname: 0x3cd0
   __TEXT.__objc_methtype: 0xb3b
-  __TEXT.__objc_stubs: 0x3480
+  __TEXT.__objc_stubs: 0x34a0
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x988
   __DATA_CONST.__objc_classlist: 0x128

   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3898
-  __DATA_CONST.__objc_selrefs: 0x10b0
+  __DATA_CONST.__objc_selrefs: 0x10b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x200
   __DATA_CONST.__objc_superrefs: 0xe8

   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_const: 0xff0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__auth_got: 0x510
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__auth_got: 0x518
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x170
-  __DATA.__data: 0x4e8
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA.__data: 0x508
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x1b0
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 875
-  Symbols:   3116
-  CStrings:  1746
+  Functions: 877
+  Symbols:   3122
+  CStrings:  1748
 
Symbols:
+ +[BMDataProtection isClassCXUnlocked]
+ +[BMDataProtection isClassCXUnlocked].cold.1
+ _aks_get_extended_device_state
+ _objc_msgSend$isClassCXUnlocked
CStrings:
+ "aks_get_extended_device_state failed with error: %d"
+ "isClassCXUnlocked"

```
