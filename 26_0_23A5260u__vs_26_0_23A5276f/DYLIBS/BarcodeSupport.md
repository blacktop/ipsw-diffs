## BarcodeSupport

> `/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport`

```diff

-1031.4.0.0.0
-  __TEXT.__text: 0x35a50
+1031.6.0.0.0
+  __TEXT.__text: 0x35c68
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x2b6c
-  __TEXT.__cstring: 0x43ee
+  __TEXT.__objc_methlist: 0x2b74
+  __TEXT.__cstring: 0x440e
   __TEXT.__const: 0x146
   __TEXT.__gcc_except_tab: 0xd44
   __TEXT.__oslogstring: 0x39ac

   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x11b0
+  __TEXT.__unwind_info: 0x11a8
   __TEXT.__objc_classname: 0x784
-  __TEXT.__objc_methname: 0x669c
+  __TEXT.__objc_methname: 0x66cb
   __TEXT.__objc_methtype: 0xfef
-  __TEXT.__objc_stubs: 0x5c40
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x11d0
+  __TEXT.__objc_stubs: 0x5c60
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x11b0
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b10
+  __DATA_CONST.__objc_selrefs: 0x1b18
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x32a0
+  __AUTH_CONST.__cfstring: 0x32c0
   __AUTH_CONST.__objc_const: 0x5568
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 754BCBE2-D641-3F89-930A-9B9D9FBAAEB4
-  Functions: 1416
-  Symbols:   5052
-  CStrings:  2664
+  UUID: 0DCAB893-9D76-33F5-BF16-27997598A36E
+  Functions: 1417
+  Symbols:   5047
+  CStrings:  2667
 
Symbols:
+ +[BCSAction _identityCredentialActionWithData:codePayload:]
+ __OBJC_$_PROP_LIST_BCSAction.330
+ _objc_msgSend$_identityCredentialActionWithData:codePayload:
- __OBJC_$_PROP_LIST_BCSAction.325
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_BarcodeSupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BarcodeSupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BarcodeSupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BarcodeSupport
Functions:
~ +[BCSAction getActionWithData:codePayload:completionHandler:] : 512 -> 548
+ +[BCSAction _identityCredentialActionWithData:codePayload:]
~ -[BCSInvalidDataAction localizedDefaultActionDescription] : 156 -> 296
~ -[BCSInvalidDataAction actionIconSystemImageName] : 156 -> 256
~ -[BCSInvalidDataAction actionPickerItems] : 288 -> 300
CStrings:
+ "Device not supported"
+ "_identityCredentialActionWithData:codePayload:"

```
