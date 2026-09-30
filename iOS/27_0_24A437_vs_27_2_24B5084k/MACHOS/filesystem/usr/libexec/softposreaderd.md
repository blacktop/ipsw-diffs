## softposreaderd

> `/usr/libexec/softposreaderd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-50.33.0.0.0
-  __TEXT.__text: 0x414f98
-  __TEXT.__auth_stubs: 0x4290
+51.4.0.0.0
+  __TEXT.__text: 0x40de2c
+  __TEXT.__auth_stubs: 0x42c0
   __TEXT.__objc_stubs: 0x2080
   __TEXT.__objc_methlist: 0xe7c
-  __TEXT.__const: 0x88340
+  __TEXT.__const: 0x708d0
   __TEXT.__swift5_typeref: 0x24cc
-  __TEXT.__cstring: 0x119ab
+  __TEXT.__cstring: 0x11b7b
   __TEXT.__objc_methtype: 0x1525
-  __TEXT.__oslogstring: 0xce4e
+  __TEXT.__oslogstring: 0xd12e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x795c
+  __TEXT.__constg_swiftt: 0x7984
   __TEXT.__swift5_proto: 0xcdc
   __TEXT.__swift5_types: 0x52c
   __TEXT.__objc_classname: 0x1a13
-  __TEXT.__objc_methname: 0x42cd
-  __TEXT.__swift_as_entry: 0x188
-  __TEXT.__swift_as_ret: 0x188
-  __TEXT.__swift_as_cont: 0x3b0
+  __TEXT.__objc_methname: 0x425d
+  __TEXT.__swift_as_entry: 0x18c
+  __TEXT.__swift_as_ret: 0x18c
+  __TEXT.__swift_as_cont: 0x3bc
   __TEXT.__swift5_protos: 0x138
-  __TEXT.__unwind_info: 0x60f0
-  __TEXT.__eh_frame: 0xcacc
-  __DATA_CONST.__const: 0x182d0
+  __TEXT.__unwind_info: 0x6120
+  __TEXT.__eh_frame: 0xcbc8
+  __DATA_CONST.__const: 0x18198
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__auth_got: 0x2150
-  __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__auth_ptr: 0xe40
+  __DATA_CONST.__auth_got: 0x2168
+  __DATA_CONST.__got: 0xde8
+  __DATA_CONST.__auth_ptr: 0xe48
   __DATA.__objc_const: 0x9190
   __DATA.__objc_selrefs: 0xb10
   __DATA.__objc_data: 0x21f8
-  __DATA.__data: 0xc7e8
+  __DATA.__data: 0xc7f8
   __DATA.__common: 0x8c0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6163
-  Symbols:   1688
-  CStrings:  3582
+  Functions: 6169
+  Symbols:   1692
+  CStrings:  3606
 
Symbols:
+ _SPRConfigurationStatusIsNFCAvailable
+ _swift_task_deinitOnExecutor
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
CStrings:
+ " exceeds store size "
+ "%s.%s: no controllerInfo; assuming antenna present"
+ "Could not deserialize pinBlob to JSON"
+ "Could not deserialize trxBlob to JSON"
+ "Could not parse cipherBlob"
+ "Could not prepare signer"
+ "Could not remove batch: %@, repairing store."
+ "Error preparing signer: %@"
+ "Error repairing store when remove batch failed: %@"
+ "Failed to store boot UUID: %s"
+ "Failed to store completeAttestation: %@"
+ "Failed to store logDeletion: %@"
+ "Monitor store is unexpected size after removing batch. Got: "
+ "NFC antenna not present on this device"
+ "NFC antenna not supported on this device"
+ "Store cleared"
+ "batch reference "
+ "completeAttestation stored"
+ "controllerInfo"
+ "deviceClass"
+ "didPostPINEvent"
+ "hasAntenna"
+ "isAntennaPresent"
+ "logDeletion stored"
+ "monitoring-logs.tmp"
+ "pinBlob is empty"
+ "pinBlob is not a JSON object"
+ "readerBlobSigner certificate expires before time required: %ld seconds. Begin renewal."
+ "softposreaderd/UnifiedReaderPINController.swift"
+ "trxBlob is empty"
+ "trxBlob is not a JSON object"
- "Could not remove batch: %@"
- "Remove all events failed: "
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "_itemReplacementDirectory"
- "cannot delete itemReplacementDirectory"
- "failed to create itemReplacementDirectory"
- "truncateAtOffset:error:"
```
