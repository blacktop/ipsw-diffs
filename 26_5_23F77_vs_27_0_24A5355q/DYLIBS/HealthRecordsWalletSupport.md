## HealthRecordsWalletSupport

> `/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x15dac
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__const: 0x1218
-  __TEXT.__cstring: 0xb13
-  __TEXT.__constg_swiftt: 0x3c8
+7027.0.52.2.6
+  __TEXT.__text: 0x16104
+  __TEXT.__const: 0x1214
+  __TEXT.__cstring: 0xb22
+  __TEXT.__oslogstring: 0x35
   __TEXT.__swift5_typeref: 0x2d7
-  __TEXT.__swift5_reflstr: 0x513
+  __TEXT.__swift5_capture: 0x5c
   __TEXT.__swift5_fieldmd: 0x7a4
+  __TEXT.__constg_swiftt: 0x3c8
+  __TEXT.__swift5_reflstr: 0x514
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x58
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_capture: 0x4c
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__oslogstring: 0x35
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x598
-  __TEXT.__eh_frame: 0x798
-  __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0x442
-  __TEXT.__objc_methtype: 0x10
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x98
+  __TEXT.__swift_as_cont: 0x20
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__eh_frame: 0x868
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x210
-  __AUTH_CONST.__auth_got: 0x618
-  __AUTH_CONST.__const: 0xc88
+  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xcb0
   __AUTH_CONST.__objc_const: 0x190
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH.__data: 0x1f8
   __DATA.__data: 0x340
-  __DATA.__bss: 0x1980
   __DATA.__common: 0x18
+  __DATA.__bss: 0x1980
   __DATA_DIRTY.__data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F121B171-C5FF-3051-93C4-52DC60979D8C
-  Functions: 551
-  Symbols:   349
-  CStrings:  146
+  UUID: F2615C75-9DBF-3958-9507-F139D4A93C18
+  Functions: 547
+  Symbols:   378
+  CStrings:  73
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.32
+ ___swift_exist.box.addr_destructor
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_HealthRecordsWalletSupport
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_HealthRecordsWalletSupport
+ __swift_implicitisolationactor_to_executor_cast
+ _block_copy_helper.34
+ _block_descriptor.36
+ _block_destroy_helper.35
+ _get_type_metadata 15Synchronization5MutexVySo13PKPassLibraryCG noncopyable.19
+ _objc_msgSend$description
+ _objc_retain_x27
+ _swift_bridgeObjectRelease_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x23
- _HKSensitiveLogItem
- ___swift_project_boxed_opaque_existential_0
- _block_copy_helper.33
- _block_descriptor.35
- _block_destroy_helper.34
- _get_type_metadata 15Synchronization5MutexVySo13PKPassLibraryCG noncopyable.17
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x9
CStrings:
- "QRRepresentation"
- "URLForResource:withExtension:"
- "UUID"
- "_TtC26HealthRecordsWalletSupport17WalletPassManager"
- "_TtC26HealthRecordsWalletSupport35SignedClinicalDataWalletPassManager"
- "addDataToArchive:pathInArchive:"
- "addFileToArchive:pathInArchive:"
- "addUnsignedPassesAtURLs:withCompletionHandler:"
- "addresses"
- "alreadyScannedSegments"
- "archiveIsValid"
- "birthDate"
- "birthSex"
- "bundleForClass:"
- "canAddPassOfType:"
- "closeArchive"
- "codingSystem"
- "credentialTypes"
- "date"
- "dateForUTC"
- "displayString"
- "doseNumber"
- "doseQuantity"
- "emailAddresses"
- "error"
- "ethnicity"
- "expirationDate"
- "fallbackDisplayString"
- "fullName"
- "fullQRCodeValue"
- "gender"
- "hk_isUSLocale"
- "identifiers"
- "init"
- "initWithURL:archiveType:"
- "isWalletVisible"
- "issuedDate"
- "items"
- "localizedPreferredName"
- "mainRecord"
- "maritalStatus"
- "medicalRecordCodings"
- "medicalRecordSampleID"
- "medicalRecords"
- "mutex"
- "notGiven"
- "numberOfExpectedSiblings"
- "originIdentifier"
- "passLibrary"
- "passWithPassTypeIdentifier:serialNumber:"
- "phoneNumbers"
- "primaryConcept"
- "race"
- "recordIssuerDisplayName"
- "recordItemsDisplayName"
- "recordTypeDisplayName"
- "removeItemAtURL:error:"
- "removePass:"
- "setDateStyle:"
- "setFormatOptions:"
- "setTimeStyle:"
- "setTimeZone:"
- "signatureStatus"
- "signedClinicalDataRecordIdentifier"
- "sortDate"
- "sourceType"
- "stringFromDate:"
- "subject"
- "textSystem"
- "uniqueID"
- "v16@?0q8"
- "v8@?0"
- "walletManager"

```
