## RapidResourceDelivery

> `/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery`

```diff

-3404.18.1.0.0
-  __TEXT.__text: 0x44af0
-  __TEXT.__auth_stubs: 0x1490
+3405.12.1.0.0
+  __TEXT.__text: 0x586f4
+  __TEXT.__auth_stubs: 0x1690
   __TEXT.__objc_methlist: 0x29c
-  __TEXT.__cstring: 0xc13
-  __TEXT.__swift5_typeref: 0xbaf
-  __TEXT.__const: 0x2a92
-  __TEXT.__constg_swiftt: 0xafe
-  __TEXT.__swift5_reflstr: 0x7e1
-  __TEXT.__swift5_fieldmd: 0xb94
-  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__cstring: 0xe23
+  __TEXT.__swift5_typeref: 0x1043
+  __TEXT.__const: 0x3b22
+  __TEXT.__constg_swiftt: 0xe1a
+  __TEXT.__swift5_reflstr: 0x951
+  __TEXT.__swift5_fieldmd: 0xf2c
+  __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x98
-  __TEXT.__swift5_proto: 0x268
-  __TEXT.__swift5_types: 0xe4
-  __TEXT.__oslogstring: 0xff1
-  __TEXT.__swift_as_entry: 0x60
-  __TEXT.__swift_as_ret: 0x6c
+  __TEXT.__swift5_proto: 0x378
+  __TEXT.__swift5_types: 0x134
+  __TEXT.__oslogstring: 0x1618
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x88
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_capture: 0x124
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x1030
-  __TEXT.__eh_frame: 0x26f0
+  __TEXT.__unwind_info: 0x1448
+  __TEXT.__eh_frame: 0x3100
   __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0x8a4
+  __TEXT.__objc_methname: 0xa1c
   __TEXT.__objc_methtype: 0x5c6
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x308
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xa48
-  __AUTH_CONST.__auth_ptr: 0x3d0
-  __AUTH_CONST.__const: 0x13a8
-  __AUTH_CONST.__objc_const: 0xbe0
-  __AUTH.__objc_data: 0x360
-  __AUTH.__data: 0xdc0
-  __DATA.__data: 0xe18
-  __DATA.__bss: 0x4b00
-  __DATA.__common: 0x1e8
+  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__auth_ptr: 0x3f0
+  __AUTH_CONST.__const: 0x1ae8
+  __AUTH_CONST.__objc_const: 0xc38
+  __AUTH.__objc_data: 0x3b0
+  __AUTH.__data: 0xfd0
+  __DATA.__data: 0x12d0
+  __DATA.__bss: 0x6d00
+  __DATA.__common: 0x268
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1138
-  Symbols:   212
-  CStrings:  330
+  Functions: 1458
+  Symbols:   232
+  CStrings:  388
 
Symbols:
+ _AnalyticsSendEventLazy
+ _NSURLContentAccessDateKey
+ _NSURLCreationDateKey
+ _OBJC_CLASS_$_NSFileHandle
+ _objc_autoreleaseReturnValue
+ _swift_getObjCClassFromMetadata
+ _swift_getTupleTypeMetadata3
+ _xpc_fd_create
+ _xpc_fd_dup
- _swift_deletedAsyncMethodErrorTu
CStrings:
+ "(assetsFolderURL: "
+ ", cachedFileInfo: "
+ "@\"NSDictionary\"8@?0"
+ "Cached update resource is still up to date."
+ "Cached update resource is within the grace period window."
+ "Caching new file info: %s"
+ "Clearing cached file info"
+ "Couldn't determine creation date of %s"
+ "Couldn't list subfolders of %s"
+ "Couldn't write updates to %{public}s."
+ "Created new cache subfolder %s"
+ "Different manifest URLs for ongoing (%s and new (%s) downloads"
+ "Different updates URLs for ongoing (%s and new (%s) downloads"
+ "Digest of received data did not agree with expected value. Computed digest %s, input digest %s"
+ "Error fetching resource updates: %@"
+ "Fetching updates because new updates are downloading."
+ "Fetching updates because the manifest has changed."
+ "Fetching updates because we have none cached."
+ "Leaving %s in place in case it's being used"
+ "Loaded existing cached file info: %s"
+ "Manifest fetch already in progress"
+ "No config found. Adopting config in client-provided assets folder."
+ "No manifest fetch scheduled."
+ "No update fetch scheduled."
+ "Opened FileHandle to %s"
+ "Received new update resource %s digest %s. Caching."
+ "Received updates that have already been cached."
+ "Removing %s, last accessed %s"
+ "Skipping %s"
+ "URLForDirectory:inDomain:appropriateForURL:create:error:"
+ "Updates cached are not the latest, but we're still in the grace period window. (digest: %s)"
+ "Updates cached are still current. (digest: %s)"
+ "Updates fetch already in progress"
+ "Updates requested: %s"
+ "Upgrading from a store with no updates digest."
+ "_manifestUpdatePeriod"
+ "cacheFolder"
+ "closeAndReturnError:"
+ "com.apple.aiml.RapidResourceDelivery.cacheSubfolder"
+ "com.apple.aiml.RapidResourceDelivery.digest"
+ "com.apple.aiml.RapidResourceDelivery.fileName"
+ "com.apple.rapidresourcedelivery.ConnectionMetrics"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "createFileAtPath:contents:attributes:"
+ "doubleForKey:"
+ "fetchStates"
+ "fileDescriptor"
+ "fileHandleForReadingFromURL:error:"
+ "fileHandleForWritingToURL:error:"
+ "fileName fileHandle digest "
+ "initWithFileDescriptor:"
+ "log"
+ "removeObjectForKey:"
+ "reportFetchMetrics: %lu, url: %s, resourceVersion: %@, statusCode: %@, taskInterval: %@"
+ "resourceUpdateError"
+ "setObject:forKey:"
+ "standardUserDefaults"
+ "taskInterval"

```
