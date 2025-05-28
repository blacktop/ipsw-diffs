## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-3.26.5.12.0
-  __TEXT.__text: 0x24fc0
+3.26.6.4.0
+  __TEXT.__text: 0x25030
   __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x2d9c
+  __TEXT.__objc_methlist: 0x2ddc
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x61c
-  __TEXT.__cstring: 0x2d07
+  __TEXT.__gcc_except_tab: 0x5bc
+  __TEXT.__cstring: 0x2cef
   __TEXT.__ustring: 0x46
-  __TEXT.__unwind_info: 0xc68
-  __TEXT.__objc_classname: 0xa1b
-  __TEXT.__objc_methname: 0xa8f6
-  __TEXT.__objc_methtype: 0x1eea
-  __TEXT.__objc_stubs: 0x7580
+  __TEXT.__unwind_info: 0xc6c
+  __TEXT.__objc_classname: 0xa31
+  __TEXT.__objc_methname: 0xa98e
+  __TEXT.__objc_methtype: 0x1efe
+  __TEXT.__objc_stubs: 0x75c0
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5a50
-  __DATA_CONST.__objc_selrefs: 0x2360
+  __DATA_CONST.__objc_const: 0x5ae0
+  __DATA_CONST.__objc_selrefs: 0x2390
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x468
   __DATA_CONST.__objc_superrefs: 0x140

   __AUTH_CONST.__auth_got: 0x488
   __AUTH.__objc_data: 0xff0
   __DATA.__objc_ivar: 0x2e0
-  __DATA.__data: 0xae0
+  __DATA.__data: 0xb40
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1101
-  Symbols:   4401
-  CStrings:  2287
+  Functions: 1106
+  Symbols:   4417
+  CStrings:  2294
 
Symbols:
+ -[MCUIListController _mainQueue_setManagedSignInButtonEnabled:]
+ -[MCUIListController enrollmentDidBegin]
+ -[MCUIListController enrollmentDidFailWithError:]
+ -[MCUIListController enrollmentDidSucceed]
+ -[MCUIListController enrollmentWasCanceled]
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentDelegate
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentDelegate
+ __OBJC_PROTOCOL_$_DMCEnrollmentDelegate
+ ___63-[MCUIListController _mainQueue_setManagedSignInButtonEnabled:]_block_invoke
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ _objc_msgSend$_mainQueue_setManagedSignInButtonEnabled:
+ _objc_msgSend$initFromViewController:delegate:
+ _objc_msgSend$setManagedSignInButtonEnabled:
- ___45-[MCUIListController initWithNibName:bundle:]_block_invoke_3
- ___block_descriptor_40_e8_32w_e23_v24?0B8B12"NSError"16lw32l8
- _objc_msgSend$initFromViewController:enrollmentResultBlock:
CStrings:
+ "DMCEnrollmentDelegate"
+ "_mainQueue_setManagedSignInButtonEnabled:"
+ "enrollmentDidBegin"
+ "enrollmentDidFailWithError:"
+ "enrollmentDidSucceed"
+ "enrollmentWasCanceled"
+ "initFromViewController:delegate:"
+ "setManagedSignInButtonEnabled:"
+ "v24@0:8@\"NSError\"16"
- "initFromViewController:enrollmentResultBlock:"
- "v24@?0B8B12@\"NSError\"16"

```
