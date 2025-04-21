## TipsDaemon

> `/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon`

```diff

-778.4.3.0.0
-  __TEXT.__text: 0x7fdb0
+778.5.1.0.0
+  __TEXT.__text: 0x7ff28
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x3268
+  __TEXT.__objc_methlist: 0x3288
   __TEXT.__const: 0x1e18
   __TEXT.__gcc_except_tab: 0x15e0
   __TEXT.__oslogstring: 0x1f9d
-  __TEXT.__cstring: 0x3978
+  __TEXT.__cstring: 0x3988
   __TEXT.__dlopen_cstrs: 0xc65
   __TEXT.__swift5_typeref: 0xbbe
   __TEXT.__swift5_fieldmd: 0x64c

   __TEXT.__swift_as_entry: 0x104
   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x26b8
+  __TEXT.__unwind_info: 0x26c0
   __TEXT.__eh_frame: 0x37cc
-  __TEXT.__objc_classname: 0xeee
-  __TEXT.__objc_methname: 0x8c85
+  __TEXT.__objc_classname: 0xf0c
+  __TEXT.__objc_methname: 0x8cac
   __TEXT.__objc_methtype: 0xb4e
-  __TEXT.__objc_stubs: 0x7240
-  __DATA_CONST.__got: 0xb08
-  __DATA_CONST.__const: 0x1f08
-  __DATA_CONST.__objc_classlist: 0x498
+  __TEXT.__objc_stubs: 0x7280
+  __DATA_CONST.__got: 0xb10
+  __DATA_CONST.__const: 0x1f10
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2328
+  __DATA_CONST.__objc_selrefs: 0x2338
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0xe08
-  __AUTH_CONST.__auth_ptr: 0x4b0
-  __AUTH_CONST.__const: 0x1bd8
-  __AUTH_CONST.__cfstring: 0x2540
-  __AUTH_CONST.__objc_const: 0x7788
+  __AUTH_CONST.__auth_ptr: 0x4b8
+  __AUTH_CONST.__const: 0x1bf8
+  __AUTH_CONST.__cfstring: 0x2560
+  __AUTH_CONST.__objc_const: 0x7818
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x9a0
+  __AUTH.__objc_data: 0x9f0
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x234
   __DATA.__data: 0xa10
-  __DATA.__bss: 0x1c30
+  __DATA.__bss: 0x1c40
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2a18
   __DATA_DIRTY.__data: 0xc50

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2665
-  Symbols:   6258
-  CStrings:  2430
+  Functions: 2669
+  Symbols:   6279
+  CStrings:  2434
 
Symbols:
+ +[TPSCloudAccountChecker isiCloudPlusEnabled]
+ +[TPSCloudAccountChecker sharedAccountStore]
+ +[TPSCloudAccountChecker sharedAccountStore].cold.1
+ -[TPSCloudAccountPlusValidation validateWithCompletion:]
+ -[TPSCloudAccountPlusValidation validateWithCompletion:].cold.1
+ _OBJC_CLASS_$_TPSCloudAccountPlusValidation
+ _OBJC_METACLASS_$_TPSCloudAccountPlusValidation
+ __OBJC_$_INSTANCE_METHODS_TPSCloudAccountPlusValidation
+ __OBJC_CLASS_RO_$_TPSCloudAccountPlusValidation
+ __OBJC_METACLASS_RO_$_TPSCloudAccountPlusValidation
+ ___44+[TPSCloudAccountChecker sharedAccountStore]_block_invoke
+ ___block_literal_global.270
+ _kTPSCapabilityiCloudPlusAccount
+ _objc_msgSend$aa_isCloudSubscriber
+ _objc_msgSend$isiCloudPlusEnabled
+ _objc_msgSend$sharedAccountStore
+ _sharedAccountStore.predicate
+ _sharedAccountStore.sharedInstance
- +[TPSCloudAccountChecker _primaryCloudAccount]
- ___block_literal_global.266
- _objc_msgSend$_primaryCloudAccount
CStrings:
+ "TPSCloudAccountPlusValidation"
+ "aa_isCloudSubscriber"
+ "iCloudPlusAccount"
+ "isiCloudPlusEnabled"
+ "sharedAccountStore"
- "_primaryCloudAccount"

```
