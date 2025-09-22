## CTLazuliSupport

> `/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport`

```diff

-13091.1.14.0.0
-  __TEXT.__text: 0x41ea8
-  __TEXT.__auth_stubs: 0x1710
+13105.1.1.0.0
+  __TEXT.__text: 0x442b4
+  __TEXT.__auth_stubs: 0x1780
   __TEXT.__objc_methlist: 0x314
-  __TEXT.__cstring: 0xc58
-  __TEXT.__swift5_typeref: 0x1492
-  __TEXT.__swift5_fieldmd: 0xdc0
-  __TEXT.__const: 0x2e50
-  __TEXT.__constg_swiftt: 0xe80
+  __TEXT.__cstring: 0xca8
+  __TEXT.__swift5_typeref: 0x15a6
+  __TEXT.__swift5_fieldmd: 0xeac
+  __TEXT.__const: 0x3150
+  __TEXT.__constg_swiftt: 0xf94
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0xa2e
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_proto: 0x220
-  __TEXT.__swift5_types: 0xfc
+  __TEXT.__swift5_reflstr: 0xa9e
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_protos: 0x50
+  __TEXT.__swift5_proto: 0x24c
+  __TEXT.__swift5_types: 0x110
   __TEXT.__swift_as_entry: 0xe0
   __TEXT.__swift_as_ret: 0x110
-  __TEXT.__oslogstring: 0xe12
-  __TEXT.__swift5_capture: 0x218
+  __TEXT.__oslogstring: 0xf82
+  __TEXT.__swift5_capture: 0x228
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x10e0
-  __TEXT.__eh_frame: 0x2e34
+  __TEXT.__unwind_info: 0x1158
+  __TEXT.__eh_frame: 0x2f2c
   __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0x8c9
+  __TEXT.__objc_methname: 0x8e7
   __TEXT.__objc_methtype: 0x4c4
-  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xb88
-  __AUTH_CONST.__const: 0x1e98
+  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__const: 0x2188
   __AUTH_CONST.__objc_const: 0xa70
   __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x948
-  __DATA.__data: 0xeb0
-  __DATA.__bss: 0x3bf0
+  __DATA.__data: 0xf38
+  __DATA.__bss: 0x4070
   __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
   - /System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS
   - /System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9C3EB51C-2EEE-3927-8A7E-166EEDE8D061
-  Functions: 1117
-  Symbols:   736
-  CStrings:  347
+  UUID: C5ECC9A7-7F35-32FE-AB86-326605779AD1
+  Functions: 1178
+  Symbols:   766
+  CStrings:  357
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ ___swift_memcpy24_8
+ _associated conformance 15CTLazuliSupport21MLSFileTransferHelperV5ErrorOSHAASQ
+ _associated conformance 15CTLazuliSupport28RCSAttachmentsAnalyticsEventV13OperationTypeOSHAASQ
+ _associated conformance 15CTLazuliSupport28RCSAttachmentsAnalyticsEventV13SendDirectionOSHAASQ
+ _swift_getErrorValue
+ _symbolic $s15CTLazuliSupport18CoreAnalyticsEventP
+ _symbolic $s15CTLazuliSupport27CoreAnalyticsClientProtocolP
+ _symbolic $s15CTLazuliSupport29MLSFileTransferHelperProtocolP
+ _symbolic SS_So8NSObjectCt
+ _symbolic _____ 15CTLazuliSupport21MLSFileTransferHelperV
+ _symbolic _____ 15CTLazuliSupport21MLSFileTransferHelperV5ErrorO
+ _symbolic _____ 15CTLazuliSupport28RCSAttachmentsAnalyticsEventV
+ _symbolic _____ 15CTLazuliSupport28RCSAttachmentsAnalyticsEventV13OperationTypeO
+ _symbolic _____ 15CTLazuliSupport28RCSAttachmentsAnalyticsEventV13SendDirectionO
+ _symbolic _____ s5Int32V
+ _symbolic ______p 15CTLazuliSupport18CoreAnalyticsEventP
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _type_layout_string 15CTLazuliSupport28RCSAttachmentsAnalyticsEventV
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Attempting to encrypt file at path: %s to destination path: %s"
+ "CoreAnalyticsClient: Sending event %s"
+ "Failed to decrypt file because crypto material is nil"
+ "Failed to get original file size for: %s"
+ "Size of %s exceeds maximum value for UInt32: %ld vs %u"
+ "Successfully decrypted file at path: %s to outputDecryptedFile: %s"
+ "Successfully encrypted file at path: %s to destination path: %s"
+ "com.apple.Telephony.RCSAttachmentsEvent"
+ "initWithInt:"
+ "initWithInteger:"
- "Successfuly decrypted file at path: %s to outputDecryptedFile: %s"

```
