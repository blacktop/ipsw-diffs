## SecureTransactionService

> `/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService`

```diff

-4.5.1.0.0
-  __TEXT.__text: 0x31400
+5.0.12.0.0
+  __TEXT.__text: 0x31ba0
   __TEXT.__auth_stubs: 0x8c0
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x2e1c
+  __TEXT.__objc_methlist: 0x2e5c
   __TEXT.__const: 0x2e0
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_reflstr: 0x94

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x6690
+  __TEXT.__cstring: 0x67cb
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4

   __TEXT.__oslogstring: 0x5ac
   __TEXT.__unwind_info: 0xae0
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x823
-  __TEXT.__objc_methname: 0x6bd8
-  __TEXT.__objc_methtype: 0x19b9
-  __TEXT.__objc_stubs: 0x3c00
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0xa70
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__objc_classname: 0x836
+  __TEXT.__objc_methname: 0x6a7e
+  __TEXT.__objc_methtype: 0x19ce
+  __TEXT.__objc_stubs: 0x3c20
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1638
+  __DATA_CONST.__objc_selrefs: 0x1640
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0x3020
-  __AUTH_CONST.__objc_const: 0x5a70
-  __AUTH_CONST.__objc_intobj: 0x1230
-  __AUTH.__objc_data: 0x1360
+  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__objc_const: 0x5a80
+  __AUTH_CONST.__objc_intobj: 0x1260
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x13b0
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x39c
-  __DATA.__data: 0x8c0
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__data: 0x8b4
   __DATA.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 52D1C82A-33FB-37DF-B4AD-CA8DFE69D902
-  Functions: 986
-  Symbols:   295
-  CStrings:  2492
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: E50071C1-74BB-3B99-8F6F-07BA3FA07475
+  Functions: 988
+  Symbols:   299
+  CStrings:  2516
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_STSReaderCryptarch
+ _OBJC_METACLASS_$_STSReaderCryptarch
+ _STSNetworkNameAmex
+ _STSNetworkNameDiscover
+ _STSNetworkNameMastercard
+ _STSNetworkNameUnknown
+ _STSNetworkNameVisa
+ _STSSupportedNetworkNames
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- ___NSArray0__struct
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "+[STSTapToProvisionResult nameFromRid:]"
+ "-[DigitalCarKeyHandler setActiveCredentials:]"
+ "-[STSReader connectionEstablishedWithSTSReaderCryptarch:sessionTranscript:]"
+ "@\"STSReaderCryptarch\""
+ "A000000003"
+ "A000000004"
+ "A000000025"
+ "A000000152"
+ "Currently only support 1 credential for this handler"
+ "Invalid credentials"
+ "STSNetworkNameAmex"
+ "STSNetworkNameDiscover"
+ "STSNetworkNameMastercard"
+ "STSNetworkNameUnknown"
+ "STSNetworkNameVisa"
+ "STSReaderCryptarch"
+ "T@\"NSData\",R,N,V_privateKey"
+ "T@\"NSString\",R,N,V_networkName"
+ "T@\"STSReaderCryptarch\",&,N,V_stsReaderCryptarch"
+ "TQ,R,N,V_curve"
+ "TQ,R,N,V_variant"
+ "Unknown RID %@"
+ "Vv32@0:8@\"STSReaderCryptarch\"16@\"NSData\"24"
+ "_curve"
+ "_curve=%lu, _variant=%lu, _privateKey=%@"
+ "_networkName"
+ "_privateKey"
+ "_stsReaderCryptarch"
+ "_variant"
+ "connectionEstablishedWithSTSReaderCryptarch:sessionTranscript:"
+ "connectionEstablishedWithSTSReaderCryptarch:sessionTranscriptBytes:"
+ "curve"
+ "initWithCurve:variant:privateKey:"
+ "initWithProvisionDataBlob:casdCertificate:networkName:"
+ "nameFromRid:"
+ "networkName"
+ "privateKey"
+ "rid"
+ "setStsReaderCryptarch:"
+ "stsReaderCryptarch"
+ "v32@0:8@\"STSReaderCryptarch\"16@\"NSData\"24"
+ "variant"
- "(error not avail)"
- "+[DigitalCarKeyHandler requestAssertionForKeyID:options:outError:]"
- "-[STSReader sessionTranscriptGenerated:]"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "Failed to get assertion %@"
- "T@\"NSArray\",R,C,N,V_supportedPNOs"
- "T@\"NSData\",R,C,N,V_authenticationTag"
- "T@\"NSData\",R,C,N,V_casdSignature"
- "T@\"NSData\",R,C,N,V_ephemeralPublicKey"
- "T@\"NSData\",R,C,N,V_keyIdentifier"
- "T@\"NSString\",R,C,N,V_configId"
- "T@\"NSString\",R,C,N,V_formatVersion"
- "T@\"NSString\",R,C,N,V_platformId"
- "T@\"NSString\",R,C,N,V_transactionId"
- "Vv24@0:8@\"NSData\"16"
- "Vv24@0:8@16"
- "_authenticationTag"
- "_casdSignature"
- "_configId"
- "_ephemeralPublicKey"
- "_formatVersion"
- "_platformId"
- "_supportedPNOs"
- "authenticationTag"
- "casdSignature"
- "configId"
- "ephemeralPublicKey"
- "formatVersion"
- "initWithIdentifier:organization:organizationUnit:iconData:iconURL:iconMediaType:privacyPolicyURL:merchantCategoryCode:certificateData:"
- "initWithProvisionDataBlob:platformId:configId:transactionId:casdCertificate:casdSignature:authenticationTag:ephemeralPublicKey:formatVersion:keyIdentifier:"
- "initWithVersion:supportedPNOs:"
- "platformId"
- "sessionTranscriptGenerated:"
- "supportedPNOs"
- "v24@0:8@\"NSData\"16"

```
