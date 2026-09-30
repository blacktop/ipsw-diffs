## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

-638.100.48.0.0
-  __TEXT.__text: 0x264dc
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x1f18
-  __TEXT.__const: 0xc90
-  __TEXT.__cstring: 0x21f4
-  __TEXT.__gcc_except_tab: 0x67c
+694.0.1.0.0
+  __TEXT.__text: 0x27aa0
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x1f60
+  __TEXT.__const: 0xd00
+  __TEXT.__cstring: 0x2300
+  __TEXT.__gcc_except_tab: 0x688
   __TEXT.__oslogstring: 0x20af
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x8b0
   __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x4821
-  __TEXT.__objc_methtype: 0xe08
-  __TEXT.__objc_stubs: 0x3160
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xab0
+  __TEXT.__objc_methname: 0x49bd
+  __TEXT.__objc_methtype: 0xe1e
+  __TEXT.__objc_stubs: 0x32a0
+  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__const: 0xb00
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1240
+  __DATA_CONST.__objc_selrefs: 0x1290
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2200
-  __AUTH_CONST.__objc_const: 0x2c40
+  __DATA_CONST.__objc_arraydata: 0x18
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x2240
+  __AUTH_CONST.__objc_const: 0x2d18
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x214
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x224
+  __DATA.__data: 0x2d0
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FFFE3046-3DFB-3924-A590-25C55DDE377F
-  Functions: 922
-  Symbols:   454
-  CStrings:  1792
+  UUID: F5F4B79C-32EC-3291-A1BC-C6041ACA9364
+  Functions: 959
+  Symbols:   476
+  CStrings:  1822
 
Symbols:
+ _IOConnectCallMethod
+ _IOObjectRelease
+ _IORegistryEntryFromPath
+ _IOServiceClose
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _IOServiceOpen
+ ___stdoutp
+ _calloc
+ _ccder_blob_decode_len
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_decode_tag
+ _ccder_blob_encode_body
+ _ccder_blob_encode_tl
+ _ccder_sizeof
+ _dispatch_queue_create
+ _dispatch_sync
+ _fprintf
+ _kIOMasterPortDefault
+ _kSecureBackupGenerateClientMetadataKey
+ _kSecureBackupPasscodeStashSecretKey
+ _mach_task_self_
+ _memcmp
+ _memset_s
+ _qsort
+ _syslog
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ ":"
+ "@\"NSData\"16@0:8"
+ "@40@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24^@32"
+ "@80@0:8@16@24@32@40@48@56B64@68i76"
+ "AppleKeyStore"
+ "Escrow error encrypting data (%x)"
+ "IOService:/IOResources/AppleKeyStore"
+ "SecureBackupGenerateClientMetadataKey"
+ "SecureBackupPasscodeStashSecret"
+ "T@\"NSData\",C,N,V_passcodeStashSecret"
+ "T@\"NSData\",R,C,N"
+ "T@\"NSData\",R,C,N,V_passcodeStashSecret"
+ "TB,N,V_generateClientMetadata"
+ "_generateClientMetadata"
+ "_passcodeStashSecret"
+ "_setError"
+ "aks"
+ "aks-client-queue"
+ "aks_get_icsc_srp"
+ "encodedEscrowRecordWithPublicKey:certificateData:error:"
+ "encodedEscrowRecordWithPublicKeyBytes:certificateData:error:"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "generateClientMetadata"
+ "getBytes:range:"
+ "hasError"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithDSID:escrowRecordContents:passcodeStashSecret:recoveryPassphrase:recordID:recordLabel:useAppleIDPassword:appleIDPasswordMetadata:reqVersion:"
+ "passcodeStashSecret"
+ "position"
+ "setGenerateClientMetadata:"
+ "setPasscodeStashSecret:"
+ "setPosition:"
- "/AppleInternal/Library/CloudServices/iCloudDevCert150.der"
- "@32@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16^@24"
- "@72@0:8@16@24@32@40@48B56@60i68"
- "encodedEscrowRecordWithPublicKey:error:"
- "encodedEscrowRecordWithPublicKeyBytes:error:"
- "initWithDSID:escrowRecordContents:recoveryPassphrase:recordID:recordLabel:useAppleIDPassword:appleIDPasswordMetadata:reqVersion:"

```
