## SecureTransactionService

> `/System/Library/PrivateFrameworks/SecureTransactionService.framework/Versions/A/SecureTransactionService`

```diff

-4.2.2.0.0
-  __TEXT.__text: 0x2e90c
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x246c
-  __TEXT.__const: 0x280
+4.4.11.0.0
+  __TEXT.__text: 0x2f160
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x2a1c
+  __TEXT.__const: 0x260
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_reflstr: 0x94
   __TEXT.__swift5_assocty: 0x28

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x5431
+  __TEXT.__cstring: 0x5626
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__oslogstring: 0x40f
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__gcc_except_tab: 0x658
+  __TEXT.__oslogstring: 0x423
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x798
-  __TEXT.__objc_methname: 0x6575
-  __TEXT.__objc_methtype: 0x1394
-  __TEXT.__objc_stubs: 0x37a0
+  __TEXT.__objc_classname: 0x784
+  __TEXT.__objc_methname: 0x658b
+  __TEXT.__objc_methtype: 0x1387
+  __TEXT.__objc_stubs: 0x3840
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d0
+  __DATA_CONST.__objc_selrefs: 0x14e0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x190
-  __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x2a00
-  __AUTH_CONST.__objc_const: 0x62e8
-  __AUTH_CONST.__objc_intobj: 0xff0
-  __AUTH.__objc_data: 0x13b0
+  __DATA_CONST.__objc_superrefs: 0x188
+  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__const: 0xad0
+  __AUTH_CONST.__cfstring: 0x2b00
+  __AUTH_CONST.__objc_const: 0x5798
+  __AUTH_CONST.__objc_intobj: 0x1038
+  __AUTH.__objc_data: 0x1360
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0x720
+  __DATA.__objc_ivar: 0x398
+  __DATA.__data: 0x738
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/NearField.framework/Versions/A/NearField
+  - /System/Library/PrivateFrameworks/SEService.framework/Versions/A/SEService
   - /System/Library/PrivateFrameworks/STSXPCHelperClient.framework/Versions/A/STSXPCHelperClient
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F3175BD6-1047-3685-9C18-92AB94CC5126
-  Functions: 949
+  UUID: E111AC7D-3041-3E2A-9516-328E60C4B98D
+  Functions: 951
   Symbols:   250
-  CStrings:  2250
+  CStrings:  2268
 
Symbols:
+ ___assert_rtn
+ _dlopen
- _OBJC_CLASS_$_STSReaderCryptarch
- _OBJC_METACLASS_$_STSReaderCryptarch
CStrings:
+ "-[ISO18013HybridHandler _startHandoverSession:]"
+ "-[ISO18013HybridHandler _startHandoverSession:]_block_invoke"
+ "-[STSHandler createHandoffTokenFromSession:outError:]"
+ "-[STSHandler retainUnusedHandoffToken:]"
+ "@\"NFSecureTransactionServicesHandoverHybridSession\"8@?0"
+ "Child session previously activated"
+ "Consume existing token from handler"
+ "Create token from %@"
+ "Exchange Error Reported By Reader"
+ "Exchange Tag Not Found"
+ "Fail to create session token; missing active session"
+ "ISO18013HybridHandler.m"
+ "Missing session token"
+ "Overwriting previous unused token %{public}@"
+ "Reader reported an error"
+ "Session Key Not Derived"
+ "T@\"NFSession\",W,N,V_activeChildSession"
+ "T@\"NSData\",&,N,V_unusedHandoffToken"
+ "TB,N,V_anonymousCredentialInfoSharing"
+ "^{__SecAccessControl=}16@0:8"
+ "_activeChildSession"
+ "_anonymousCredentialInfoSharing"
+ "_start18013Transaction"
+ "_startHandoverSession:"
+ "_unusedHandoffToken"
+ "activeChildSession"
+ "anonymousCredentialInfoSharing"
+ "consumeHandoffToken"
+ "copyAccessControl"
+ "createHandoffTokenFromSession:outError:"
+ "initWithDeviceEngagementType:dataRetrievalType:engagementData:"
+ "retainUnusedHandoffToken:"
+ "self.activeSTSCredentials.count > 0"
+ "setActiveChildSession:"
+ "setAnonymousCredentialInfoSharing:"
+ "setUnusedHandoffToken:"
+ "unusedHandoffToken"
- "\""
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
- "privateKey"
- "sessionCryptarch"
- "setHandoffToken:"
- "variant"

```
