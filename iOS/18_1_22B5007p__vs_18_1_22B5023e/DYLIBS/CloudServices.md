## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

-638.0.5.0.0
-  __TEXT.__text: 0x1d894
+638.40.5.0.0
+  __TEXT.__text: 0x1dd60
   __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x10b4
+  __TEXT.__objc_methlist: 0x10ec
   __TEXT.__const: 0xc90
-  __TEXT.__cstring: 0x172f
+  __TEXT.__cstring: 0x1bb8
   __TEXT.__gcc_except_tab: 0x59c
   __TEXT.__oslogstring: 0x203d
-  __TEXT.__unwind_info: 0x6a0
-  __TEXT.__objc_classname: 0x149
-  __TEXT.__objc_methname: 0x3584
-  __TEXT.__objc_methtype: 0xae2
-  __TEXT.__objc_stubs: 0x26e0
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x9e8
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__objc_classname: 0x15f
+  __TEXT.__objc_methname: 0x3634
+  __TEXT.__objc_methtype: 0xae4
+  __TEXT.__objc_stubs: 0x27e0
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0xac0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd28
+  __DATA_CONST.__objc_selrefs: 0xd70
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x518
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x2258
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x22e8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x2a8
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 666
-  Symbols:   397
-  CStrings:  1168
+  Functions: 676
+  Symbols:   444
+  CStrings:  1211
 
Symbols:
+ _CloudServicesAnalyticsBackupForViewName
+ _CloudServicesAnalyticsBackupWithChangesFull
+ _CloudServicesAnalyticsBackupWithChangesIncremental
+ _CloudServicesAnalyticsDoubleCreateBlob
+ _CloudServicesAnalyticsDoubleEnrollment
+ _CloudServicesAnalyticsDoubleGetClubCert
+ _CloudServicesAnalyticsDoubleRecovery
+ _CloudServicesAnalyticsDoubleRecoveryDataMatch3
+ _CloudServicesAnalyticsDoubleRecoveryPCS
+ _CloudServicesAnalyticsDoubleRecoveryPCSDataMatch
+ _CloudServicesAnalyticsGestalt
+ _CloudServicesAnalyticsLakituResponse
+ _CloudServicesAnalyticsRecoverRecordWithInfo
+ _CloudServicesAnalyticsRecoverRequest
+ _CloudServicesAnalyticsRequestV1
+ _CloudServicesAnalyticsRequestV1Fallback
+ _CloudServicesAnalyticsRequestV1ToV0Fallback
+ _CloudServicesAnalyticsRequestV2
+ _CloudServicesAnalyticsRequestV2Fallback
+ _CloudServicesAnalyticsRequestV2ToV0Fallback
+ _CloudServicesAnalyticsRestoreBackupName
+ _CloudServicesAnalyticsRestoreKeychainWithBackupBag
+ _CloudServicesAnalyticsSetConfirmedManifest
+ _CloudServicesAnalyticsiCDPKeybag
+ _CloudServicesAnalyticsiCDPKeybagRecoveryKey
+ _CloudServicesBottledPeerRecovery
+ _CloudServicesInitializeLogging
+ _CloudServicesLog
+ _CloudServicesRecoverEscrowWithRequest
+ _CloudServicesSOSRestoreMetrics
+ _CloudServicesiCloudIdentity
+ _OBJC_CLASS_$_CSCertOperations
+ _OBJC_CLASS_$_CSDateUtilities
+ _OBJC_CLASS_$_CSSESWrapper
+ _OBJC_CLASS_$_CloudServicesAnalytics
+ _OBJC_CLASS_$_CloudServicesError
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_METACLASS_$_CSCertOperations
+ _OBJC_METACLASS_$_CSDateUtilities
+ _OBJC_METACLASS_$_CSSESWrapper
+ _OBJC_METACLASS_$_CloudServicesAnalytics
+ _OBJC_METACLASS_$_CloudServicesError
+ _SECURE_BACKUP_CONCURRENT_SERVICE_NAME
+ _SECURE_BACKUP_SERVICE_NAME
+ _SecureBackupSetupConcurrentProtocol
+ _SecureBackupSetupProtocol
CStrings:
+ "@\"CSSESWrapper\""
+ "CSCertOperations"
+ "CSDateUtilities"
+ "CSSESWrapper"
+ "CSSRPClientRequest"
+ "CloudServicesAnalyticsDoubleCreateBlob"
+ "CloudServicesAnalyticsDoubleEnrollment"
+ "CloudServicesAnalyticsDoubleGetClubCert"
+ "CloudServicesAnalyticsDoubleRecovery"
+ "CloudServicesAnalyticsDoubleRecoveryDataMatch3"
+ "CloudServicesAnalyticsDoubleRecoveryPCS"
+ "CloudServicesAnalyticsDoubleRecoveryPCSDataMatch"
+ "CloudServicesAnalyticsGestalt"
+ "CloudServicesAnalyticsRecoverRequest"
+ "CloudServicesAnalyticsRequestV1"
+ "CloudServicesAnalyticsRequestV1Fallback"
+ "CloudServicesAnalyticsRequestV1ToV0Fallback"
+ "CloudServicesAnalyticsRequestV2"
+ "CloudServicesAnalyticsRequestV2Fallback"
+ "CloudServicesAnalyticsRequestV2ToV0Fallback"
+ "CloudServicesAnalyticsRestoreKeychainWithBackupBag"
+ "CloudServicesAnalyticsiCDPKeybag"
+ "CloudServicesAnalyticsiCDPKeybagRecoveryKey"
+ "CloudServicesBackupForViewName"
+ "CloudServicesBackupWithChangesFull"
+ "CloudServicesBackupWithChangesIncremental"
+ "CloudServicesBottledPeerRecovery"
+ "CloudServicesLakituResponse"
+ "CloudServicesRecoverEscrowWithRequest"
+ "CloudServicesRecoverRecordWithInfo"
+ "CloudServicesRestoreBackupName"
+ "CloudServicesSOSRestoreMetrics"
+ "CloudServicesSetConfirmedManifest"
+ "CloudServicesiCloudIdentity"
+ "T@\"CSSESWrapper\",&,N,V_ses"
+ "dateFromString:"
+ "dd-MM-yyyy HH:mm:ss"
+ "en_US_POSIX"
+ "initWithLocaleIdentifier:"
+ "legacyDateFormatter"
+ "localStringFromDate:"
+ "localTimeZone"
+ "secureBackupDateFromString:"
+ "setDateFormat:"
+ "setLocale:"
+ "setTimeZone:"
+ "timeZoneForSecondsFromGMT:"
+ "yyyy-MM-dd HH:mm:ss"
+ "yyyy-MM-dd HH:mm:ssZZZZZ"
- "@\"SESWrapper\""
- "CertOperations"
- "SESWrapper"
- "SRPClientRequest"
- "T@\"SESWrapper\",&,N,V_ses"
- "secureBackupDate"

```
