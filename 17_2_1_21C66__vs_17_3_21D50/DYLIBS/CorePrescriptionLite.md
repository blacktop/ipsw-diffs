## CorePrescriptionLite

> `/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite`

```diff

-153.0.0.0.0
-  __TEXT.__text: 0xfda4
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x10a0
-  __TEXT.__const: 0x5298
-  __TEXT.__cstring: 0x1839
+164.40.6.0.0
+  __TEXT.__text: 0x1101c
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x1128
+  __TEXT.__const: 0x5d10
+  __TEXT.__cstring: 0x1cad
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x691
-  __TEXT.__unwind_info: 0x484
-  __TEXT.__objc_classname: 0x35e
-  __TEXT.__objc_methname: 0x3574
-  __TEXT.__objc_methtype: 0x9fd
-  __TEXT.__objc_stubs: 0x2280
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x750
+  __TEXT.__oslogstring: 0x713
+  __TEXT.__unwind_info: 0x4a4
+  __TEXT.__objc_classname: 0x368
+  __TEXT.__objc_methname: 0x3714
+  __TEXT.__objc_methtype: 0xa3a
+  __TEXT.__objc_stubs: 0x2380
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2328
-  __DATA_CONST.__objc_selrefs: 0xba8
+  __DATA_CONST.__objc_const: 0x2410
+  __DATA_CONST.__objc_selrefs: 0xc08
   __AUTH_CONST.__objc_const: 0xd90
-  __AUTH_CONST.__cfstring: 0x15a0
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1c0
+  __DATA.__objc_classrefs: 0x1d0
   __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x26c
-  __DATA.__data: 0x140
+  __DATA.__objc_ivar: 0x274
+  __DATA.__data: 0x1a0
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F16641E4-9111-35C0-81AB-FD070BB640F0
-  Functions: 431
-  Symbols:   1868
-  CStrings:  1190
+  UUID: 5D297492-2AE2-3A75-957D-640819DF7A35
+  Functions: 444
+  Symbols:   1919
+  CStrings:  1311
 
Symbols:
+ -[CRXFAppClipCode copyWithZone:]
+ -[CRXFAppClipCodeScanningState copyWithZone:]
+ -[CRXFAppClipCodeScanningState initWithLeftAppClipCode:leftAppClipCodePayload:rightAppClipCode:rightAppClipCodePayload:dualAppClipCode:dualAppClipCodePayload:allowUnsupportedRX:]
+ -[CRXFAppClipCodeTranscoder decodeAppClipCodeV5FromBuffer:allowUnsupportedRX:error:]
+ -[CRXFAppClipCodeTranscoder encodeAppClipCodeV5:toBuffer:error:]
+ -[CRXUDispatchQueue assert]
+ -[CRXUDispatchQueue setTracingEnabled:]
+ -[CRXUDispatchQueue tracingEnabled]
+ -[NSDictionary(CRXUExtensions) crxu_doubleForKey:]
+ -[NSError(CRXFExtensions) crxf_errorToken]
+ _HKMetadataKeySyncIdentifier
+ _HKMetadataKeySyncVersion
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_CRXUDispatchQueue._log
+ _OBJC_IVAR_$_CRXUDispatchQueue._tracingEnabled
+ __OBJC_$_INSTANCE_METHODS_NSError(CRXFExtensions)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_CRXFAppClipCode
+ __OBJC_CLASS_PROTOCOLS_$_CRXFAppClipCodeScanningState
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSCopying
+ ___34-[CRXUDispatchQueue dispatchSync:]_block_invoke
+ ___35-[CRXUDispatchQueue dispatchAsync:]_block_invoke
+ ___46-[CRXUDispatchQueue afterDelay:dispatchAsync:]_block_invoke
+ _dispatch_assert_queue$V2
+ _kCRXFErrorKeyRXUUID
+ _kCRXFMaxValidCalibrationRXIDValue
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$code
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$decodeAppClipCodeV5FromBuffer:allowUnsupportedRX:error:
+ _objc_msgSend$encodeAppClipCodeV5:toBuffer:error:
+ _objc_msgSend$initWithLeftAppClipCode:leftAppClipCodePayload:rightAppClipCode:rightAppClipCodePayload:dualAppClipCode:dualAppClipCodePayload:allowUnsupportedRX:
CStrings:
+ "%s @%d: <%{public}@> async enter"
+ "%s @%d: <%{public}@> async leave"
+ "%s @%d: <%{public}@> sync enter"
+ "%s @%d: <%{public}@> sync leave"
+ "-[CRXUDispatchQueue afterDelay:dispatchAsync:]_block_invoke"
+ "-[CRXUDispatchQueue dispatchAsync:]_block_invoke"
+ "-[CRXUDispatchQueue dispatchSync:]_block_invoke"
+ "@24@0:8^{_NSZone=}16"
+ "@68@0:8@16@24@32@40@48@56B64"
+ "ACCInvalidValues"
+ "ACCReadError"
+ "ACCScanAlreadyInProgress"
+ "ACCVersionInvalid"
+ "ACCVersionMismatch"
+ "ACCWriteError"
+ "ARKitInitError"
+ "CloudDownloadMissingResults"
+ "CloudKitDuplicateRecord"
+ "CloudKitInternalServerError"
+ "CloudKitInvalidRequest"
+ "CloudKitPermissionDenied"
+ "CloudKitRecordNotFound"
+ "CloudKitUserInfoLookupFailed"
+ "CryptoError"
+ "EnrollmentAlreadyExists"
+ "EnrollmentNotFound"
+ "Eye model deletion failed"
+ "EyeModelDeletionFailed"
+ "FailedToSelectEnrollment"
+ "HealthCloudSyncDisabled"
+ "HealthKitCallFailed"
+ "InvalidACCDetectionCount"
+ "InvalidACCPayload"
+ "InvalidACCURL"
+ "InvalidEnrollmentGroup"
+ "InvalidEnrollmentName"
+ "InvalidJSONData"
+ "InvalidLeftCalibrationIndex"
+ "InvalidLensCalibrationData"
+ "InvalidRightCalibrationIndex"
+ "LensPoseEstimationFailed"
+ "ManagedAssetsDataStoreError"
+ "MismatchedLensTypes"
+ "MultipleACCsDetected"
+ "NSCopying"
+ "NetworkUnreachable"
+ "NonComplementaryACCs"
+ "Operation cancelled"
+ "OperationCancelled"
+ "PrescriptionUUIDMismatch"
+ "SingleEyeEnrollment"
+ "Success"
+ "T@\"NSString\",R,N"
+ "TB,N,V_tracingEnabled"
+ "TableIsCreatedExternally"
+ "Timeout"
+ "UUID"
+ "UUIDString"
+ "UnexpectedRecordCount"
+ "UniqueEnrollmentNotFound"
+ "UnknownError"
+ "_tracingEnabled"
+ "allocWithZone:"
+ "assert"
+ "copyWithZone:"
+ "crxf_errorToken"
+ "crxu_doubleForKey:"
+ "d24@0:8@16"
+ "decodeAppClipCodeV5FromBuffer:allowUnsupportedRX:error:"
+ "encodeAppClipCodeV5:toBuffer:error:"
+ "initWithLeftAppClipCode:leftAppClipCodePayload:rightAppClipCode:rightAppClipCodePayload:dualAppClipCode:dualAppClipCodePayload:allowUnsupportedRX:"
+ "rxUUID"
+ "setTracingEnabled:"
+ "tracingEnabled"
- "ACC anchor not found"

```
