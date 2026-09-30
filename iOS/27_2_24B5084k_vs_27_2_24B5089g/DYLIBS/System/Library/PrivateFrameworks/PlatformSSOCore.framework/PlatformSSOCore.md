## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-643.40.23.0.0
-  __TEXT.__text: 0x93c24
-  __TEXT.__objc_methlist: 0x6330
+643.40.27.0.0
+  __TEXT.__text: 0x93ea8
+  __TEXT.__objc_methlist: 0x6388
   __TEXT.__const: 0x1a04
-  __TEXT.__cstring: 0xae28
-  __TEXT.__oslogstring: 0x1fd7
+  __TEXT.__cstring: 0xae78
+  __TEXT.__oslogstring: 0x2027
   __TEXT.__gcc_except_tab: 0x6f4
   __TEXT.__dlopen_cstrs: 0xa6
   __TEXT.__swift5_typeref: 0x166

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x2e28
+  __TEXT.__unwind_info: 0x2e40
   __TEXT.__eh_frame: 0x568
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2600
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d48
+  __DATA_CONST.__objc_selrefs: 0x2d68
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x9c0
-  __AUTH_CONST.__const: 0xc20
-  __AUTH_CONST.__cfstring: 0x7bc0
-  __AUTH_CONST.__objc_const: 0x14d58
+  __DATA_CONST.__got: 0x9d0
+  __AUTH_CONST.__const: 0xc60
+  __AUTH_CONST.__cfstring: 0x7c20
+  __AUTH_CONST.__objc_const: 0x14e40
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xdb8
-  __AUTH.__objc_data: 0x35a0
+  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH.__objc_data: 0x35f0
   __AUTH.__data: 0x1a8
-  __DATA.__objc_ivar: 0x658
+  __DATA.__objc_ivar: 0x65c
   __DATA.__data: 0x1250
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3858
-  Symbols:   6804
-  CStrings:  1769
+  Functions: 3869
+  Symbols:   6830
+  CStrings:  1775
 
Symbols:
+ +[POKeychainAccess isRunningInTestProcess]
+ -[POKeychainHelper .cxx_destruct]
+ -[POKeychainHelper init]
+ -[POKeychainHelper keychainAccess]
+ -[POKeychainHelper setKeychainAccess:]
+ -[POTokenHelper findInfoForTokenId:uid:]
+ _NSClassFromString
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_POKeychainAccess
+ _OBJC_IVAR_$_POKeychainHelper._keychainAccess
+ _OBJC_METACLASS_$_POKeychainAccess
+ _PO_LOG_POKeychainAccess.log
+ _PO_LOG_POKeychainAccess.once
+ __OBJC_$_CLASS_METHODS_POKeychainAccess
+ __OBJC_$_CLASS_PROP_LIST_POKeychainAccess
+ __OBJC_$_INSTANCE_VARIABLES_POKeychainHelper
+ __OBJC_$_PROP_LIST_POKeychainHelper
+ __OBJC_CLASS_RO_$_POKeychainAccess
+ __OBJC_METACLASS_RO_$_POKeychainAccess
+ ___42+[POKeychainAccess isRunningInTestProcess]_block_invoke
+ ___PO_LOG_POKeychainAccess_block_invoke
+ _isRunningInTestProcess.isTest
+ _isRunningInTestProcess.onceToken
+ _objc_msgSend$environment
+ _objc_msgSend$findInfoForTokenId:uid:
+ _objc_msgSend$processInfo
CStrings:
+ "%s tokenId = %{public}@, uid = %{public}@ on %@"
+ "-[POTokenHelper findInfoForTokenId:uid:]"
+ "POKeychainAccess"
+ "XCTestCase"
+ "XCTestConfigurationFilePath"
+ "XCTestSessionIdentifier"
+ "isRunningInTestProcess is true"
- "-[POTokenHelper findInfoForTokenId:]"
```
