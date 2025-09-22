## ContactsDonation

> `/System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation`

```diff

-1123.100.1.0.0
-  __TEXT.__text: 0xf4f8
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x1a30
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x8be
-  __TEXT.__oslogstring: 0xf4e
+1123.200.21.0.0
+  __TEXT.__text: 0xfec4
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x1ae0
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x8cf
+  __TEXT.__oslogstring: 0x1244
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__unwind_info: 0x460
-  __TEXT.__objc_classname: 0x49f
-  __TEXT.__objc_methname: 0x2f8f
-  __TEXT.__objc_methtype: 0xc56
-  __TEXT.__objc_stubs: 0x2020
-  __DATA_CONST.__got: 0x210
+  __TEXT.__unwind_info: 0x478
+  __TEXT.__objc_classname: 0x4cd
+  __TEXT.__objc_methname: 0x305b
+  __TEXT.__objc_methtype: 0xd95
+  __TEXT.__objc_stubs: 0x20a0
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x788
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x2ad8
+  __AUTH_CONST.__cfstring: 0xaa0
+  __AUTH_CONST.__objc_const: 0x2c60
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x880
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__data: 0x8e0
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17B82EC3-4791-3CB8-B0C5-EFF0E2A7283B
-  Functions: 500
-  Symbols:   1910
-  CStrings:  959
+  UUID: 7DB24DBD-C6F8-36DD-BB51-92C7CF9007AB
+  Functions: 508
+  Symbols:   1948
+  CStrings:  991
 
Symbols:
+ -[_CNDonationAccountLogger valueLogger]
+ -[_CNDonationValueLogger .cxx_destruct]
+ -[_CNDonationValueLogger initWithLog:]
+ -[_CNDonationValueLogger visitDonationValue:emailAddress:label:]
+ -[_CNDonationValueLogger visitDonationValue:imageData:]
+ -[_CNDonationValueLogger visitDonationValue:nameComponents:]
+ -[_CNDonationValueLogger visitDonationValue:phoneNumber:label:]
+ -[_CNDonationValueLogger visitDonationValue:postalAddress:style:label:]
+ _OBJC_CLASS_$_CNPostalAddressFormatter
+ _OBJC_CLASS_$_NSPersonNameComponentsFormatter
+ _OBJC_CLASS_$__CNDonationValueLogger
+ _OBJC_IVAR_$__CNDonationAccountLogger._valueLogger
+ _OBJC_IVAR_$__CNDonationValueLogger._log
+ _OBJC_METACLASS_$__CNDonationValueLogger
+ __OBJC_$_INSTANCE_METHODS__CNDonationValueLogger
+ __OBJC_$_INSTANCE_VARIABLES__CNDonationValueLogger
+ __OBJC_$_PROP_LIST__CNDonationValueLogger
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNDonationValueVisitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNDonationValueVisitor
+ __OBJC_$_PROTOCOL_REFS_CNDonationValueVisitor
+ __OBJC_CLASS_PROTOCOLS_$__CNDonationValueLogger
+ __OBJC_CLASS_RO_$__CNDonationValueLogger
+ __OBJC_LABEL_PROTOCOL_$_CNDonationValueVisitor
+ __OBJC_METACLASS_RO_$__CNDonationValueLogger
+ __OBJC_PROTOCOL_$_CNDonationValueVisitor
+ _objc_getProperty
+ _objc_msgSend$acceptDonationValueVisitor:
+ _objc_msgSend$initWithLog:
+ _objc_msgSend$singleLineStringFromPostalAddress:addCountryName:
+ _objc_msgSend$stringFromPersonNameComponents:
CStrings:
+ "@\"<CNDonationValueVisitor>\""
+ "CNDonationValueVisitor"
+ "Creating donation of %{public}@ \"%{private}@\" from %{public}@"
+ "Creating donation of %{public}@ \"%{private}@\" with label \"%{private}@\" from %{public}@"
+ "Creating donation of email address \"%{private}@\" from %{public}@"
+ "Creating donation of email address \"%{private}@\" with label \"%{private}@\" from %{public}@"
+ "Creating donation of empty %{public}@ from %{public}@"
+ "Creating donation of empty email address from %{public}@"
+ "Creating donation of empty name from %{public}@"
+ "Creating donation of empty phone number from %{public}@"
+ "Creating donation of image data (%lu bytes) from %{public}@"
+ "Creating donation of name \"%{private}@\" from %{public}@"
+ "Creating donation of phone number \"%{private}@\" from %{public}@"
+ "Creating donation of phone number \"%{private}@\" with label \"%{private}@\" from %{public}@"
+ "T@\"<CNDonationValueVisitor>\",R,V_valueLogger"
+ "T@\"NSObject<OS_os_log>\",R,V_log_t"
+ "_CNDonationValueLogger"
+ "_log"
+ "_valueLogger"
+ "address"
+ "initWithLog:"
+ "location"
+ "singleLineStringFromPostalAddress:addCountryName:"
+ "stringFromPersonNameComponents:"
+ "v32@0:8@\"CNDonationValue\"16@\"NSData\"24"
+ "v32@0:8@\"CNDonationValue\"16@\"NSPersonNameComponents\"24"
+ "v40@0:8@\"CNDonationValue\"16@\"CNPhoneNumber\"24@\"NSString\"32"
+ "v40@0:8@\"CNDonationValue\"16@\"NSString\"24@\"NSString\"32"
+ "v48@0:8@\"CNDonationValue\"16@\"CNPostalAddress\"24q32@\"NSString\"40"
+ "v48@0:8@16@24q32@40"
+ "valueLogger"
- "Creating donation: %{public}@"

```
