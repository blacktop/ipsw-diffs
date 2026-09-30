## SecureTransactionService

> `/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService`

```diff

-4.2.2.0.0
-  __TEXT.__text: 0x30d9c
+4.4.10.0.0
+  __TEXT.__text: 0x310a0
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x26c8
-  __TEXT.__const: 0x2d4
+  __TEXT.__objc_methlist: 0x2e14
+  __TEXT.__const: 0x2e0
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_reflstr: 0x94
   __TEXT.__swift5_assocty: 0x28

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x6367
+  __TEXT.__cstring: 0x658e
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x7f8
-  __TEXT.__oslogstring: 0x598
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__gcc_except_tab: 0x834
+  __TEXT.__oslogstring: 0x5ac
+  __TEXT.__unwind_info: 0xad8
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x837
-  __TEXT.__objc_methname: 0x6bc9
-  __TEXT.__objc_methtype: 0x19b9
-  __TEXT.__objc_stubs: 0x3b60
+  __TEXT.__objc_classname: 0x823
+  __TEXT.__objc_methname: 0x6bc6
+  __TEXT.__objc_methtype: 0x199c
+  __TEXT.__objc_stubs: 0x3be0
   __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0xa40
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1520
+  __DATA_CONST.__objc_selrefs: 0x1630
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1b8
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0x2e80
-  __AUTH_CONST.__objc_const: 0x68d8
-  __AUTH_CONST.__objc_intobj: 0x11d0
-  __AUTH.__objc_data: 0x13b0
+  __AUTH_CONST.__cfstring: 0x2fa0
+  __AUTH_CONST.__objc_const: 0x5a70
+  __AUTH_CONST.__objc_intobj: 0x1230
+  __AUTH.__objc_data: 0x1360
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x3a4
-  __DATA.__data: 0x8a0
+  __DATA.__objc_ivar: 0x39c
+  __DATA.__data: 0x8b8
   __DATA.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 996
-  Symbols:   287
-  CStrings:  2107
+  Functions: 984
+  Symbols:   292
+  CStrings:  2116
 
Symbols:
+ _OBJC_CLASS_$_ORReader
+ ___assert_rtn
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _OBJC_CLASS_$_SPRProvider
- _OBJC_CLASS_$_STSReaderCryptarch
- _OBJC_METACLASS_$_STSReaderCryptarch
- _swift_errorRelease
- _swift_initStructMetadata
CStrings:
+ "\x02\x13"
+ "-[ISO18013Handler _start18013Transaction]_block_invoke"
+ "-[ISO18013Handler _start18013Transaction]_block_invoke_2"
+ "-[ISO18013HybridHandler _startHandoverSession:]"
+ "-[ISO18013HybridHandler _startHandoverSession:]_block_invoke"
+ "-[STSHandler createHandoffTokenFromSession:outError:]"
+ "-[STSHandler retainUnusedHandoffToken:]"
+ "@\"NFSecureTransactionServicesHandoverHybridSession\"8@?0"
+ "@\"NFSession\""
+ "Child session previously activated"
+ "Consume existing token from handler"
+ "Create token from %@"
+ "Exchange Error Reported By Reader"
+ "Exchange Tag Not Found"
+ "Fail to create session token; missing active session"
+ "Fail to start SecureTransactionServicesSession, missing session token"
+ "ISO18013HybridHandler.m"
+ "Missing session token"
+ "Overwriting previous unused token %{public}@"
+ "Reader reported an error"
+ "Session Key Not Derived"
+ "T@\"NFSession\",W,N,V_activeChildSession"
+ "T@\"NSData\",&,N,V_unusedHandoffToken"
+ "TB,N,V_anonymousCredentialInfoSharing"
+ "_activeChildSession"
+ "_anonymousCredentialInfoSharing"
+ "_start18013Transaction"
+ "_startHandoverSession:"
+ "_unusedHandoffToken"
+ "activeChildSession"
+ "anonymousCredentialInfoSharing"
+ "consumeHandoffToken"
+ "createHandoffTokenFromSession:outError:"
+ "initWithDeviceEngagementType:dataRetrievalType:engagementData:"
+ "initWithIsProduction:error:"
+ "retainUnusedHandoffToken:"
+ "self.activeSTSCredentials.count > 0"
+ "setActiveChildSession:"
+ "setAnonymousCredentialInfoSharing:"
+ "setUnusedHandoffToken:"
+ "unusedHandoffToken"
- "\x05"
- "\""
- "-[ISO18013Handler _start18013TransactionWithToken:]_block_invoke"
- "-[ISO18013Handler _start18013TransactionWithToken:]_block_invoke_2"
- "-[ISO18013HybridHandler _startHandoverSession]"
- "-[ISO18013HybridHandler _startHandoverSession]_block_invoke"
- "@\"STSReaderCryptarch\""
- "@48@0:8Q16Q24@32@40"
- "Handoff has not been started"
- "STSReaderCryptarch"
- "T@\"NSData\",&,N,V_handoffToken"
- "T@\"NSData\",R,N,V_privateKey"
- "T@\"STSReaderCryptarch\",R,N,V_sessionCryptarch"
- "TQ,R,N,V_curve"
- "TQ,R,N,V_variant"
- "_curve"
- "_handoffToken"
- "_privateKey"
- "_sessionCryptarch"
- "_start18013TransactionWithToken:"
- "_startHandoverSession"
- "_variant"
- "configurationWithDeviceEngagementType:dataRetrievalType:engagementData:sessionCryptarch:"
- "curve"
- "handoffToken"
- "initWithCurve:variant:privateKey:"
- "initWithDeviceEngagementType:dataRetrievalType:engagementData:sessionCryptarch:"
- "makeORReaderAndReturnError:"
- "privateKey"
- "sessionCryptarch"
- "setHandoffToken:"
- "shared"
- "variant"

```
