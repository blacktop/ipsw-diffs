## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

-212.120.2.0.0
-  __TEXT.__text: 0x30b10
+212.120.3.0.0
+  __TEXT.__text: 0x31258
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x383c
+  __TEXT.__objc_methlist: 0x38e4
   __TEXT.__const: 0x164
-  __TEXT.__cstring: 0x2b81
+  __TEXT.__cstring: 0x2bba
   __TEXT.__oslogstring: 0x215e
   __TEXT.__gcc_except_tab: 0x1394
-  __TEXT.__unwind_info: 0xf88
-  __TEXT.__objc_classname: 0x748
-  __TEXT.__objc_methname: 0x774e
-  __TEXT.__objc_methtype: 0x1adc
-  __TEXT.__objc_stubs: 0x5b40
-  __DATA_CONST.__got: 0x358
+  __TEXT.__unwind_info: 0xf98
+  __TEXT.__objc_classname: 0x779
+  __TEXT.__objc_methname: 0x7875
+  __TEXT.__objc_methtype: 0x1b10
+  __TEXT.__objc_stubs: 0x5c40
+  __DATA_CONST.__got: 0x360
   __DATA_CONST.__const: 0xb88
-  __DATA_CONST.__objc_classlist: 0x1f8
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_selrefs: 0x1ca8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2c40
-  __AUTH_CONST.__objc_const: 0x6230
+  __AUTH_CONST.__cfstring: 0x2cc0
+  __AUTH_CONST.__objc_const: 0x63a0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x11f8
-  __DATA.__objc_ivar: 0x398
+  __AUTH.__objc_data: 0x1248
+  __DATA.__objc_ivar: 0x3a4
   __DATA.__data: 0x800
   __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2F7E7F46-24B3-396B-91EB-A61EB1FAF1B7
-  Functions: 1245
-  Symbols:   4556
-  CStrings:  2642
+  UUID: 7B663E21-B9B3-390D-BE4F-0FBEBACFBF9A
+  Functions: 1257
+  Symbols:   4601
+  CStrings:  2665
 
Symbols:
+ +[ASTAuthInfoResult authInfoResultWithAttestation:certificate:type:errorObject:]
+ +[ASTAuthInfoResultErrorObject errorObjectWithError:resultCode:]
+ -[ASTAuthInfoResult errorObject]
+ -[ASTAuthInfoResult setErrorObject:]
+ -[ASTAuthInfoResultErrorObject .cxx_destruct]
+ -[ASTAuthInfoResultErrorObject error]
+ -[ASTAuthInfoResultErrorObject initWithError:resultCode:]
+ -[ASTAuthInfoResultErrorObject resultCode]
+ -[ASTAuthInfoResultErrorObject setError:]
+ -[ASTAuthInfoResultErrorObject setResultCode:]
+ -[NSError(ASTSerialization) base64EncodedJSONString]
+ -[NSError(ASTSerialization) jsonSerializableDictionary]
+ _OBJC_CLASS_$_ASTAuthInfoResultErrorObject
+ _OBJC_IVAR_$_ASTAuthInfoResult._errorObject
+ _OBJC_IVAR_$_ASTAuthInfoResultErrorObject._error
+ _OBJC_IVAR_$_ASTAuthInfoResultErrorObject._resultCode
+ _OBJC_METACLASS_$_ASTAuthInfoResultErrorObject
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSError_$_ASTSerialization
+ __OBJC_$_CATEGORY_NSError_$_ASTSerialization
+ __OBJC_$_CLASS_METHODS_ASTAuthInfoResultErrorObject
+ __OBJC_$_INSTANCE_METHODS_ASTAuthInfoResultErrorObject
+ __OBJC_$_INSTANCE_VARIABLES_ASTAuthInfoResultErrorObject
+ __OBJC_$_PROP_LIST_ASTAuthInfoResultErrorObject
+ __OBJC_CLASS_RO_$_ASTAuthInfoResultErrorObject
+ __OBJC_METACLASS_RO_$_ASTAuthInfoResultErrorObject
+ _objc_msgSend$authInfoResultWithAttestation:certificate:type:errorObject:
+ _objc_msgSend$base64EncodedJSONString
+ _objc_msgSend$errorObject
+ _objc_msgSend$errorObjectWithError:resultCode:
+ _objc_msgSend$initWithError:resultCode:
+ _objc_msgSend$jsonSerializableDictionary
+ _objc_msgSend$setErrorObject:
+ _objc_msgSend$userInfo
CStrings:
+ "@\"ASTAuthInfoResultErrorObject\""
+ "@48@0:8@16@24q32@40"
+ "ASTAuthInfoResultErrorObject"
+ "ASTSerialization"
+ "T@\"ASTAuthInfoResultErrorObject\",&,N,V_errorObject"
+ "T@\"NSError\",&,N,V_error"
+ "_errorObject"
+ "authInfoResultWithAttestation:certificate:type:errorObject:"
+ "base64EncodedJSONString"
+ "errorObject"
+ "errorObjectWithError:resultCode:"
+ "initWithError:resultCode:"
+ "internalErrorString"
+ "jsonSerializableDictionary"
+ "setErrorObject:"
+ "userInfo"

```
