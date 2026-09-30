## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-455.32.10.4.1
-  __TEXT.__text: 0x22240
+455.32.10.4.3
+  __TEXT.__text: 0x22698
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x2744
+  __TEXT.__objc_methlist: 0x2804
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x2a83
-  __TEXT.__cstring: 0x4084
+  __TEXT.__oslogstring: 0x2ac7
+  __TEXT.__cstring: 0x4105
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x7d0
-  __TEXT.__objc_classname: 0x63d
-  __TEXT.__objc_methname: 0x5042
-  __TEXT.__objc_methtype: 0x11f4
-  __TEXT.__objc_stubs: 0x3760
+  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__objc_classname: 0x669
+  __TEXT.__objc_methname: 0x514a
+  __TEXT.__objc_methtype: 0x1249
+  __TEXT.__objc_stubs: 0x3780
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x11a8
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1298
+  __DATA_CONST.__objc_selrefs: 0x12c0
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x3ba0
-  __AUTH_CONST.__objc_const: 0x7248
+  __AUTH_CONST.__cfstring: 0x3c60
+  __AUTH_CONST.__objc_const: 0x7480
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x218
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x228
   __DATA.__data: 0x970
   __DATA.__bss: 0x128
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4B818B5-B4B9-357E-A937-05EFF2629BB0
-  Functions: 989
-  Symbols:   3938
-  CStrings:  2396
+  UUID: 304FB24C-22D5-3837-BEE9-31966A8A0E7C
+  Functions: 1004
+  Symbols:   3993
+  CStrings:  2422
 
Symbols:
+ +[FMDCommandValidationSignatureRequestContext supportsSecureCoding]
+ -[FMDCommandValidationSignatureRequestContext .cxx_destruct]
+ -[FMDCommandValidationSignatureRequestContext altDSID]
+ -[FMDCommandValidationSignatureRequestContext dataToSign]
+ -[FMDCommandValidationSignatureRequestContext encodeWithCoder:]
+ -[FMDCommandValidationSignatureRequestContext ephemeralToken]
+ -[FMDCommandValidationSignatureRequestContext initWithCoder:]
+ -[FMDCommandValidationSignatureRequestContext requestEphemeralAuth]
+ -[FMDCommandValidationSignatureRequestContext setAltDSID:]
+ -[FMDCommandValidationSignatureRequestContext setDataToSign:]
+ -[FMDCommandValidationSignatureRequestContext setEphemeralToken:]
+ -[FMDCommandValidationSignatureRequestContext setRequestEphemeralAuth:]
+ -[FMDFMIPManager commandValidationSignatureWithContext:completion:]
+ _OBJC_CLASS_$_FMDCommandValidationSignatureRequestContext
+ _OBJC_IVAR_$_FMDCommandValidationSignatureRequestContext._altDSID
+ _OBJC_IVAR_$_FMDCommandValidationSignatureRequestContext._dataToSign
+ _OBJC_IVAR_$_FMDCommandValidationSignatureRequestContext._ephemeralToken
+ _OBJC_IVAR_$_FMDCommandValidationSignatureRequestContext._requestEphemeralAuth
+ _OBJC_METACLASS_$_FMDCommandValidationSignatureRequestContext
+ __OBJC_$_CLASS_METHODS_FMDCommandValidationSignatureRequestContext
+ __OBJC_$_CLASS_PROP_LIST_FMDCommandValidationSignatureRequestContext
+ __OBJC_$_INSTANCE_METHODS_FMDCommandValidationSignatureRequestContext
+ __OBJC_$_INSTANCE_VARIABLES_FMDCommandValidationSignatureRequestContext
+ __OBJC_$_PROP_LIST_FMDCommandValidationSignatureRequestContext
+ __OBJC_CLASS_PROTOCOLS_$_FMDCommandValidationSignatureRequestContext
+ __OBJC_CLASS_RO_$_FMDCommandValidationSignatureRequestContext
+ __OBJC_METACLASS_RO_$_FMDCommandValidationSignatureRequestContext
+ ___67-[FMDFMIPManager commandValidationSignatureWithContext:completion:]_block_invoke
+ ___67-[FMDFMIPManager commandValidationSignatureWithContext:completion:]_block_invoke.cold.1
+ _kDeviceInfoCommandLookupIdKey
+ _kFMDFMMAdditionalAccountInfoAltDSIDKey
+ _kFMDFindMyServiceValidationAccessEntitlement
+ _kWipeInfoValidationErrorKey
+ _objc_msgSend$commandValidationSignatureWithContext:completion:
CStrings:
+ "FMDCommandValidationSignatureRequestContext"
+ "FMDFMMAltDSID"
+ "T@\"NSData\",C,N,V_dataToSign"
+ "T@\"NSString\",C,N,V_altDSID"
+ "T@\"NSString\",C,N,V_ephemeralToken"
+ "TB,N,V_requestEphemeralAuth"
+ "Vv32@0:8@\"FMDCommandValidationSignatureRequestContext\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "XPC error for commandValidationSignatureWithContext:completion: %li"
+ "_altDSID"
+ "_requestEphemeralAuth"
+ "altDSID"
+ "com.apple.FindMyDevice.FindMyServiceValidation.access"
+ "commandLookupId"
+ "commandValidationSignatureWithContext:completion:"
+ "requestEphemeralAuth"
+ "setAltDSID:"
+ "setRequestEphemeralAuth:"
+ "validationError"

```
