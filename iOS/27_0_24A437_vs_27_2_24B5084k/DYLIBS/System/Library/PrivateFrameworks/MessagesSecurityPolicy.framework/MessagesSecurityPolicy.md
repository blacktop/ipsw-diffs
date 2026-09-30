## MessagesSecurityPolicy

> `/System/Library/PrivateFrameworks/MessagesSecurityPolicy.framework/MessagesSecurityPolicy`

```diff

-1491.100.1.2.25
-  __TEXT.__text: 0x19f24
-  __TEXT.__objc_methlist: 0x354
-  __TEXT.__const: 0x157e
-  __TEXT.__constg_swiftt: 0xc8c
-  __TEXT.__swift5_typeref: 0xb8c
+1491.200.63.2.1
+  __TEXT.__text: 0x1bf64
+  __TEXT.__objc_methlist: 0x364
+  __TEXT.__const: 0x18ce
+  __TEXT.__constg_swiftt: 0xdfc
+  __TEXT.__swift5_typeref: 0xc8c
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x737
-  __TEXT.__swift5_fieldmd: 0x840
-  __TEXT.__swift5_assocty: 0x2a8
-  __TEXT.__oslogstring: 0xf27
-  __TEXT.__cstring: 0x7e5
-  __TEXT.__swift5_proto: 0xec
-  __TEXT.__swift5_types: 0xa8
-  __TEXT.__swift5_capture: 0x8c4
-  __TEXT.__swift5_protos: 0x74
+  __TEXT.__swift5_reflstr: 0x7d7
+  __TEXT.__swift5_fieldmd: 0x90c
+  __TEXT.__swift5_assocty: 0x348
+  __TEXT.__oslogstring: 0x11e7
+  __TEXT.__cstring: 0x815
+  __TEXT.__swift5_proto: 0x118
+  __TEXT.__swift5_types: 0xc0
+  __TEXT.__swift5_capture: 0x8e4
+  __TEXT.__swift5_protos: 0x80
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0x718
-  __TEXT.__eh_frame: 0x588
+  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__eh_frame: 0x6b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a8
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__got: 0x1c8
-  __AUTH_CONST.__const: 0x1418
-  __AUTH_CONST.__objc_const: 0xdc8
-  __AUTH_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0x16b0
+  __AUTH_CONST.__objc_const: 0xde8
+  __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x1d0
-  __AUTH.__data: 0x4c8
-  __DATA.__data: 0x388
+  __AUTH.__data: 0x598
+  __DATA.__data: 0x3e0
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x738
+  __DATA_DIRTY.__data: 0x758
   __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 547
-  Symbols:   530
-  CStrings:  118
+  Functions: 585
+  Symbols:   553
+  CStrings:  130
 
Symbols:
+ _BlastDoorInstanceTypeLockDownMode
+ _OBJC_CLASS_$_IMSyndicationUtilities
+ _objc_msgSend$cloudKitShareURLInPayloadData:
+ _objc_msgSend$cloudKitShareURLsInAttributedString:
+ _objc_msgSend$deviceIsLockedDownFor:senderOrigin:
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _symbolic $s22MessagesSecurityPolicy20SyndicationUtilitiesP
+ _symbolic $s22MessagesSecurityPolicy21CloudKitShareURLRulesP
+ _symbolic $s22MessagesSecurityPolicy22CloudKitShareURLActionP
+ _symbolic Say_____G 10Foundation3URLV
+ _symbolic So18NSAttributedStringCSg
+ _symbolic _____ 22MessagesSecurityPolicy21CloudKitShareURLInputV
+ _symbolic _____ 22MessagesSecurityPolicy24CheckIfExistsAssetActionV
+ _symbolic _____ 22MessagesSecurityPolicy25SkipCloudKitShareURLRulesV
+ _symbolic _____ 22MessagesSecurityPolicy26SkipCloudKitShareURLActionV
+ _symbolic _____ 22MessagesSecurityPolicy28ScanForCloudKitShareURLRulesV
+ _symbolic _____ 22MessagesSecurityPolicy30ScanForCloudKitShareURLsActionV
+ _symbolic ______p 22MessagesSecurityPolicy20SyndicationUtilitiesP
+ _symbolic ______p 22MessagesSecurityPolicy22CloudKitShareURLActionP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation3URLV
+ _type_layout_string 22MessagesSecurityPolicy21CloudKitShareURLInputV
+ _type_layout_string 22MessagesSecurityPolicy30ScanForCloudKitShareURLsActionV
CStrings:
+ "CloudKitShareURLPolicyAction"
+ "CloudKitShareURLRulesSelector"
+ "Collecting CloudKit share URLs to register for %s, context: %ld"
+ "Executing CheckIfExistsAssetAction"
+ "Failed to check if attachment exists at URL: %s, with error: %@"
+ "Failed to collect CloudKit share URLs: %@"
+ "Selected BlastDoor interface for lock down mode"
+ "[CloudKitShareURLProcessing] Did not scan message for CloudKit share URLs"
+ "[CloudKitShareURLProcessing] Not scanning for CloudKit share URLs for %s sender"
+ "[CloudKitShareURLProcessing] Scanned message body and payload for CloudKit share URLs; found %{public}ld"
+ "[CloudKitShareURLProcessing] Scanning for CloudKit share URLs for %s sender"
+ "[CloudKitShareURLProcessing] Scanning for CloudKit share URLs for a junk report"
```
