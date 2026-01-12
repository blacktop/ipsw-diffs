## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1450.400.3.2.1
-  __TEXT.__text: 0xf2678
-  __TEXT.__auth_stubs: 0x1d90
+1450.400.13.2.1
+  __TEXT.__text: 0xf65d8
+  __TEXT.__auth_stubs: 0x1e10
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x85c
-  __TEXT.__const: 0x5b28
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x4f2c
-  __TEXT.__objc_methtype: 0xe70
-  __TEXT.__cstring: 0x33b5
-  __TEXT.__constg_swiftt: 0x20a4
-  __TEXT.__swift5_typeref: 0x1f81
+  __TEXT.__objc_methlist: 0x984
+  __TEXT.__const: 0x5ca8
+  __TEXT.__objc_classname: 0xae
+  __TEXT.__objc_methname: 0x5099
+  __TEXT.__objc_methtype: 0xea3
+  __TEXT.__cstring: 0x35b5
+  __TEXT.__constg_swiftt: 0x2220
+  __TEXT.__swift5_typeref: 0x1f8f
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x1323
+  __TEXT.__swift5_reflstr: 0x1424
   __TEXT.__swift5_assocty: 0x2c8
-  __TEXT.__oslogstring: 0x60f8
-  __TEXT.__swift5_fieldmd: 0x178c
-  __TEXT.__swift5_proto: 0x30c
-  __TEXT.__swift5_types: 0x1b8
-  __TEXT.__swift_as_entry: 0x254
-  __TEXT.__swift_as_ret: 0x2bc
-  __TEXT.__swift5_capture: 0x978
+  __TEXT.__oslogstring: 0x6238
+  __TEXT.__swift5_fieldmd: 0x1844
+  __TEXT.__swift5_proto: 0x318
+  __TEXT.__swift5_types: 0x1c8
+  __TEXT.__swift_as_entry: 0x258
+  __TEXT.__swift_as_ret: 0x2c0
+  __TEXT.__swift5_capture: 0x968
   __TEXT.__swift5_mpenum: 0xcc
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x35b0
-  __TEXT.__eh_frame: 0x9330
-  __DATA_CONST.__auth_got: 0xed0
-  __DATA_CONST.__got: 0x870
-  __DATA_CONST.__auth_ptr: 0x5e8
-  __DATA_CONST.__const: 0x5470
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__unwind_info: 0x36b8
+  __TEXT.__eh_frame: 0x9400
+  __DATA_CONST.__auth_got: 0xf10
+  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__auth_ptr: 0x608
+  __DATA_CONST.__const: 0x55a8
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1ff0
-  __DATA.__objc_selrefs: 0x1698
-  __DATA.__objc_data: 0x448
-  __DATA.__data: 0x3780
-  __DATA.__bss: 0x4c00
-  __DATA.__common: 0xd8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA.__objc_const: 0x2238
+  __DATA.__objc_selrefs: 0x1720
+  __DATA.__objc_data: 0x698
+  __DATA.__data: 0x3918
+  __DATA.__bss: 0x4d80
+  __DATA.__common: 0xe0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4B3FB534-FFE5-3547-B2CC-D120F4FF627D
-  Functions: 3428
-  Symbols:   419
-  CStrings:  1562
+  UUID: E19011B1-1029-3796-9DE4-2CEF02AE9CC8
+  Functions: 3496
+  Symbols:   427
+  CStrings:  1607
 
Symbols:
+ _IMIsRunningInUnitTesting
+ _IMMessageSummaryInfoFailureToDecryptInfo
+ _IMMetricsCollectorEventRCSGroupFragmentation
+ _OBJC_CLASS_$_CoreRCSSecureGroupVersion
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$__TtC7CoreRCS23RCSFailureToDecryptInfo
+ _OBJC_METACLASS_$_CoreRCSSecureGroupVersion
+ _OBJC_METACLASS_$__TtC7CoreRCS23RCSFailureToDecryptInfo
+ _swift_deallocPartialClassInstance
+ _swift_isaMask
- _IMMessageSummaryInfoOriginalMessageID
- _IMMessageSummaryInfoSecureGroupVersion
CStrings:
+ ", secureGroupVersion: "
+ "@24@0:8@\"NSCoder\"16"
+ "CoreRCS.RCSFailureToDecryptInfo"
+ "CoreRCS.SecureGroupVersion"
+ "CoreRCSSecureGroupVersion"
+ "Created lazuliMessageID %@ for %s messageItem with imMessageItem.guid %s,      imMessageItem.originalGUID %s"
+ "Duplicated failure to decrypt message has no original GUID"
+ "Failure to decrypt -- resending message %s with originalMessageID %@"
+ "GroupFragmentation"
+ "Ignoring message sent due to unknown message GUID %s"
+ "Ignoring message sent for a message I didn't send for messageGUID %s"
+ "Missing CTLazuliMessageID or secureGroupVersion for CTLazuliMessageID.uuid %s message.guid %s. FailureToDecrypt won't have the info it needs!"
+ "NSCoding"
+ "NSSecureCoding"
+ "RCS chat created with participants matching an existing chat."
+ "RCSGroupFragmentation"
+ "Set message summary info for RCSMessage->IMMessageItem %s with failureToDecryptInfo(%@)"
+ "T@\"NSString\",N,R"
+ "TB,R"
+ "Tq,N,R"
+ "_TtC7CoreRCS23RCSFailureToDecryptInfo"
+ "chatsWithHandles:displayName:identifier:domain:style:everOnServices:"
+ "copy"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "epoch"
+ "era"
+ "flags"
+ "forceAutoBugCaptureWithSubType:errorPayload:type:context:metadata:"
+ "initWithCoder:"
+ "originalGUID"
+ "q16@0:8"
+ "sendDate"
+ "sentAt"
+ "setGuid:"
+ "setOriginalGUID:"
+ "setSentAt:"
+ "storeMessage:forceReplace:modifyError:modifyFlags:flagMask:"
+ "supportsSecureCoding"
+ "trackEvent:"
+ "v24@0:8@\"NSCoder\"16"
- "Failure to decrypt -- resending message %s"
- "Ignoring message sent due to unknown message UUID"
- "Ignoring message sent for a message I didn't send"
- "Set message summary info for RCSMessage->IMMessageItem %s with originalID(%@), secureGroupVersion(%@) in the failure to decrypt case."

```
