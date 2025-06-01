## feedbackd

> `/usr/libexec/feedbackd`

```diff

-85.3.0.0.0
-  __TEXT.__text: 0x44484
-  __TEXT.__auth_stubs: 0x1440
+91.0.0.0.0
+  __TEXT.__text: 0x45690
+  __TEXT.__auth_stubs: 0x14a0
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0xb58
-  __TEXT.__cstring: 0x2c58
-  __TEXT.__objc_methname: 0xd26
+  __TEXT.__const: 0xb38
+  __TEXT.__cstring: 0x3011
+  __TEXT.__objc_methname: 0xd39
   __TEXT.__constg_swiftt: 0x748
   __TEXT.__swift5_typeref: 0x6ab
   __TEXT.__swift5_reflstr: 0x4ae

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x250
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1370
-  __TEXT.__eh_frame: 0x2600
-  __DATA_CONST.__auth_got: 0xa20
+  __TEXT.__unwind_info: 0x12c8
+  __TEXT.__eh_frame: 0x2578
+  __DATA_CONST.__auth_got: 0xa50
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0xfd8
+  __DATA_CONST.__const: 0xfc8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0xf8
   __DATA.__objc_const: 0x13c8
   __DATA.__objc_selrefs: 0x358
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0xf8
   __DATA.__objc_data: 0x588
-  __DATA.__data: 0x1258
+  __DATA.__data: 0x1248
   __DATA.__common: 0x88
-  __DATA.__bss: 0xfa0
+  __DATA.__bss: 0xf90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4C4E3F63-01FE-3F85-90C8-4AD6BFB3A545
-  Functions: 911
-  Symbols:   508
-  CStrings:  428
+  UUID: 21C92F3B-7572-3049-806D-78D9B61C9652
+  Functions: 914
+  Symbols:   514
+  CStrings:  449
 
Symbols:
+ _$s15FeedbackService21FBKSSharedPersistenceC14removeInboxTatyySSFZ
+ _$s15FeedbackService21FBKSSharedPersistenceC15fbaInboxFormTat14formIdentifierAA010FBKSSInboxH0CSgSS_tFZ
+ _$s15FeedbackService21FBKSSharedPersistenceC18removeAllInboxTatsyyFZ
+ _$s15FeedbackService21FBKSSharedPersistenceC23saveSurveyTatInFBAInbox14formIdentifierySS_tFZ
+ _$s15FeedbackService21FBKSSharedPersistenceCMa
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _objc_release_x9
+ _objc_retain_x2
+ _objc_retain_x9
+ _swift_release_n
- _$s15FeedbackService20FBKSSharePersistenceC14removeInboxTatyySSFZ
- _$s15FeedbackService20FBKSSharePersistenceC15fbaInboxFormTat14formIdentifierAA010FBKSSInboxH0CSgSS_tFZ
- _$s15FeedbackService20FBKSSharePersistenceC18removeAllInboxTatsyyFZ
- _$s15FeedbackService20FBKSSharePersistenceC23saveSurveyTatInFBAInbox14formIdentifierySS_tFZ
- _$s15FeedbackService20FBKSSharePersistenceCMa
- _swift_setDeallocating
CStrings:
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Making survey [%s] available in FBA inbox"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
