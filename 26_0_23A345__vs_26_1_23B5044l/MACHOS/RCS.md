## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1448.100.1.2.101
-  __TEXT.__text: 0xe2550
-  __TEXT.__auth_stubs: 0x1be0
+1450.200.35.2.5
+  __TEXT.__text: 0xe65d8
+  __TEXT.__auth_stubs: 0x1d10
   __TEXT.__objc_stubs: 0x40
   __TEXT.__objc_methlist: 0x844
-  __TEXT.__const: 0x5078
+  __TEXT.__const: 0x50c8
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x4b77
+  __TEXT.__objc_methname: 0x4b52
   __TEXT.__objc_methtype: 0xe70
-  __TEXT.__cstring: 0x3235
-  __TEXT.__constg_swiftt: 0x1dcc
-  __TEXT.__swift5_typeref: 0x1dd1
-  __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_reflstr: 0x11cc
-  __TEXT.__swift5_assocty: 0x2d8
-  __TEXT.__oslogstring: 0x5ac9
-  __TEXT.__swift5_fieldmd: 0x1640
-  __TEXT.__swift5_proto: 0x2f8
+  __TEXT.__cstring: 0x32a5
+  __TEXT.__constg_swiftt: 0x1eb0
+  __TEXT.__swift5_typeref: 0x1dd7
+  __TEXT.__swift5_builtin: 0x17c
+  __TEXT.__swift5_reflstr: 0x121c
+  __TEXT.__swift5_assocty: 0x2c8
+  __TEXT.__oslogstring: 0x5c09
+  __TEXT.__swift5_fieldmd: 0x1698
+  __TEXT.__swift5_proto: 0x2fc
   __TEXT.__swift5_types: 0x1a4
-  __TEXT.__swift_as_entry: 0x248
-  __TEXT.__swift_as_ret: 0x2a8
+  __TEXT.__swift_as_entry: 0x24c
+  __TEXT.__swift_as_ret: 0x2ac
   __TEXT.__swift5_capture: 0x984
   __TEXT.__swift5_mpenum: 0xbc
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x3350
-  __TEXT.__eh_frame: 0x8cf8
-  __DATA_CONST.__auth_got: 0xdf8
-  __DATA_CONST.__got: 0x7f8
-  __DATA_CONST.__auth_ptr: 0x5b0
-  __DATA_CONST.__const: 0x5128
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__unwind_info: 0x3430
+  __TEXT.__eh_frame: 0x8f20
+  __DATA_CONST.__auth_got: 0xe90
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__auth_ptr: 0x5a8
+  __DATA_CONST.__const: 0x5108
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1e98
-  __DATA.__objc_selrefs: 0x1578
-  __DATA.__objc_data: 0x3e8
-  __DATA.__data: 0x3400
-  __DATA.__bss: 0x4b00
-  __DATA.__common: 0xb8
+  __DATA.__objc_const: 0x1f88
+  __DATA.__objc_selrefs: 0x1560
+  __DATA.__objc_data: 0x440
+  __DATA.__data: 0x3568
+  __DATA.__bss: 0x4b80
+  __DATA.__common: 0xd8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport
+  - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EFE40BCB-F195-37A6-8E91-127FC1B01D9D
-  Functions: 3290
-  Symbols:   407
-  CStrings:  1493
+  UUID: 13E1737C-7166-38B9-AB4F-AE24FD2E402F
+  Functions: 3337
+  Symbols:   410
+  CStrings:  1501
 
Symbols:
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_isUniquelyReferenced_native
- _OBJC_CLASS_$_NSMutableOrderedSet
CStrings:
+ "Adding message %s to retry set with total retry interval %ld"
+ "Handling error propagation for %s"
+ "Ignoring duplicate retry request for %s"
+ "MessageSendItem %s has failed all retries, or is otherwise invalid."
+ "MessageSendItem %s is no longer eligible as of %s. Marking finalRetry."
+ "Messages to retry on next interval in %fs: %s"
+ "No more eligible retries."
+ "Processed message but relay message %@ or chat %@ is nil"
+ "Retry set after removing ineligible messages: %s"
+ "Retry timer fired"
+ "Retry(expiryDate: "
+ "Successfully sent RCS message %s"
+ "_TtC3RCS18RCSMessageSendItem"
+ "isRetryingMessages, so skip RCS downgrade"
+ "rcsMessage"
+ "sendState"
+ "sourceMessage"
- "Adding message %s to retry set with interval %ld"
- "Finished considering retry for message %s"
- "Message %s is no longer eligible for retries as of %s. Removing from retry set..."
- "Messages to retry on next interval in %fs: %@"
- "Retry timer fired; retry set count: %ld"
- "Successfully sent rcsMessage %s"
- "addObject:"
- "containsObject:"
- "minusSet:"

```
