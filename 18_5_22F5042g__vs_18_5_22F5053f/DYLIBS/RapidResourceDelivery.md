## RapidResourceDelivery

> `/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery`

```diff

-3405.12.1.0.0
-  __TEXT.__text: 0x586f4
-  __TEXT.__auth_stubs: 0x1690
+3405.18.1.0.0
+  __TEXT.__text: 0x5b828
+  __TEXT.__auth_stubs: 0x1720
   __TEXT.__objc_methlist: 0x29c
-  __TEXT.__cstring: 0xe23
-  __TEXT.__swift5_typeref: 0x1043
-  __TEXT.__const: 0x3b22
-  __TEXT.__constg_swiftt: 0xe1a
-  __TEXT.__swift5_reflstr: 0x951
-  __TEXT.__swift5_fieldmd: 0xf2c
-  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__const: 0x3b08
+  __TEXT.__cstring: 0xf69
+  __TEXT.__constg_swiftt: 0xee8
+  __TEXT.__swift5_typeref: 0x10eb
+  __TEXT.__swift5_reflstr: 0x9dc
+  __TEXT.__swift5_fieldmd: 0xfc8
+  __TEXT.__oslogstring: 0x1458
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x98
-  __TEXT.__swift5_proto: 0x378
-  __TEXT.__swift5_types: 0x134
-  __TEXT.__oslogstring: 0x1618
-  __TEXT.__swift_as_entry: 0x94
-  __TEXT.__swift_as_ret: 0xac
+  __TEXT.__swift5_proto: 0x37c
+  __TEXT.__swift5_types: 0x140
+  __TEXT.__swift_as_entry: 0x98
+  __TEXT.__swift_as_ret: 0xb8
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x124
+  __TEXT.__swift5_capture: 0x120
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x1448
-  __TEXT.__eh_frame: 0x3100
+  __TEXT.__unwind_info: 0x1500
+  __TEXT.__eh_frame: 0x3208
   __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0xa1c
+  __TEXT.__objc_methname: 0xa4a
   __TEXT.__objc_methtype: 0x5c6
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__auth_ptr: 0x3f0
-  __AUTH_CONST.__const: 0x1ae8
-  __AUTH_CONST.__objc_const: 0xc38
-  __AUTH.__objc_data: 0x3b0
-  __AUTH.__data: 0xfd0
-  __DATA.__data: 0x12d0
-  __DATA.__bss: 0x6d00
-  __DATA.__common: 0x268
+  __AUTH_CONST.__auth_got: 0xb90
+  __AUTH_CONST.__auth_ptr: 0x428
+  __AUTH_CONST.__const: 0x1bc0
+  __AUTH_CONST.__objc_const: 0xd30
+  __AUTH.__objc_data: 0x3b8
+  __AUTH.__data: 0x1150
+  __DATA.__data: 0x1370
+  __DATA.__common: 0x258
+  __DATA.__bss: 0x6d80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1458
-  Symbols:   232
-  CStrings:  388
+  Functions: 1515
+  Symbols:   241
+  CStrings:  397
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_arrayInitWithCopy
+ _swift_deletedAsyncMethodErrorTu
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
- _swift_unknownObjectRetain_n
CStrings:
+ "%s: Using cached updates."
+ ", subfolderName: "
+ "Bailing on updates fetch. Manifest is unsupported."
+ "Cache coherence error: %s not found"
+ "Cached manifest is too old."
+ "Caching new entry: %s"
+ "Can't persist updates with no manifest file"
+ "Configuration unchanged."
+ "Error reading manifest: %s"
+ "Exiting in invalid state"
+ "Fetching updates because cached ones are out of date."
+ "Manifest is unsupported."
+ "Manifest was re-configured, restarting ResourceManager."
+ "No cached updates."
+ "No manifest present, can't use cached updates."
+ "Pruning client cache"
+ "RapidResourceDelivery/Task+Deadline.swift"
+ "RapidResourceDelivery/TokenBucket.swift"
+ "Skip pruning current cached subfolder %s"
+ "_TtC21RapidResourceDelivery11TokenBucket"
+ "cache"
+ "com.apple.aiml.RapidResourceDelivery.ValidationError"
+ "getUpdatesInfo(assetsFolderURL:)"
+ "integerForKey:"
+ "manifestGracePeriod"
+ "reportValidationError: %s"
+ "setTimeoutIntervalForResource:"
+ "timeoutIntervalForResource"
+ "withDeadline unreachable"
- "Caching new file info: %s"
- "Clearing cached file info"
- "Different manifest URLs for ongoing (%s and new (%s) downloads"
- "Different updates URLs for ongoing (%s and new (%s) downloads"
- "Fetching manifest"
- "Inconsistent state: last seen network success time precedes manifest update time"
- "Inconsistent state: manifest update time is set while last seen network success is not."
- "Loaded existing cached file info: %s"
- "Logic error: No manifest file"
- "Manifest fetch already in progress"
- "No manifest fetch scheduled."
- "No update fetch scheduled."
- "RapidResourceDelivery/PersistenceManager.swift"
- "Resources are out of date. Failed to download updates within %f seconds."
- "Resources are out of date. Remain stale for %f seconds. No network failures detected within grace period or network success detected after network failures."
- "Resources are out of date. Stale for %f seconds and failed to update for %f seconds while still on network."
- "Resources are up to date. Stale for %f seconds and failed to update for %f seconds while still on network."
- "Resources are up to date. Stale for %f seconds."
- "Updates fetch already in progress"
- "fetchStates"

```
