## cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

-710.1.103.0.0
-  __TEXT.__text: 0x1cf730
+710.7.140.0.0
+  __TEXT.__text: 0x1cfeb0
   __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_stubs: 0x1ace0
-  __TEXT.__objc_methlist: 0xc26c
+  __TEXT.__objc_stubs: 0x1ad80
+  __TEXT.__objc_methlist: 0xc274
   __TEXT.__const: 0x78e0
-  __TEXT.__cstring: 0x1a511
-  __TEXT.__objc_classname: 0x27a6
-  __TEXT.__objc_methname: 0x26f4c
-  __TEXT.__objc_methtype: 0x81dc
-  __TEXT.__gcc_except_tab: 0x3110
-  __TEXT.__oslogstring: 0x10173
+  __TEXT.__cstring: 0x1a6d4
+  __TEXT.__objc_classname: 0x27c4
+  __TEXT.__objc_methname: 0x27075
+  __TEXT.__objc_methtype: 0x82ab
+  __TEXT.__gcc_except_tab: 0x3118
+  __TEXT.__oslogstring: 0x10239
   __TEXT.__swift5_typeref: 0x182f
   __TEXT.__swift5_reflstr: 0x1ef7
   __TEXT.__swift5_assocty: 0x378

   __TEXT.__swift5_types: 0x158
   __TEXT.__swift5_capture: 0x348
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x65f0
-  __TEXT.__eh_frame: 0x1738
+  __TEXT.__unwind_info: 0x6628
+  __TEXT.__eh_frame: 0x1700
   __DATA_CONST.__auth_got: 0xd18
   __DATA_CONST.__got: 0xc08
   __DATA_CONST.__auth_ptr: 0x390
-  __DATA_CONST.__const: 0x9c90
-  __DATA_CONST.__cfstring: 0x10dc0
+  __DATA_CONST.__const: 0x9cf8
+  __DATA_CONST.__cfstring: 0x10e80
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x180
-  __DATA_CONST.__objc_protolist: 0x430
+  __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x608

   __DATA_CONST.__objc_floatobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x21de0
-  __DATA.__objc_selrefs: 0x8188
+  __DATA.__objc_const: 0x21e40
+  __DATA.__objc_selrefs: 0x81b0
   __DATA.__objc_ivar: 0x11c4
   __DATA.__objc_data: 0x42f8
-  __DATA.__data: 0x6938
+  __DATA.__data: 0x6998
   __DATA.__bss: 0xdd80
   __DATA.__common: 0x778
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9166
-  Symbols:   928
-  CStrings:  11250
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 9177
+  Symbols:   936
+  CStrings:  11269
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ " in sync bubble"
+ " outside of sync bubble"
+ "#__NONE__#"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Implementations/PrequeliteStore/CPLPrequeliteRecordComputeStatePushQueue.m"
+ "B48@0:8@\"CPLRecordComputeState\"16^@24^B32^@40"
+ "CPLRecordComputeStateDelegate"
+ "Couldn't find localScopedIdentifier for cloudScopedIdentifier %!@(MISSING) in cloudCache for compute state"
+ "Library manager has no compute state delegate"
+ "Memory Inline Playback Resources Download"
+ "Memory Inline Playback Resources Preload"
+ "Missing file storage identifier for %!@(MISSING)"
+ "Missing file storage identifier for %!@(MISSING)"
+ "Notified that user will be switched, we don't have a running logout sync task"
+ "Notified that user will be switched, we have a running logout sync task"
+ "Notified that we need to upload content. Starting sync task%!@(MISSING)"
+ "UPDATE OR FAIL %!@(MISSING) SET fileStorageIdentifier = %!@(MISSING) WHERE scopeIndex = %!l(MISSING)d AND localIdentifier = %!@(MISSING) AND version = %!@(MISSING) AND adjustmentFingerprint = %!@(MISSING)"
+ "UPDATE OR FAIL %!@(MISSING) SET fileStorageIdentifier = %!@(MISSING) WHERE scopeIndex = %!l(MISSING)d AND localIdentifier = %!@(MISSING) AND version = %!@(MISSING) AND adjustmentFingerprint IS NULL"
+ "endLogoutTaskForDaemonLibraryManager:"
+ "engineLibrary:providePayloadForComputeStates:inFolderWithURL:completionHandler:"
+ "libraryManager:providePayloadForComputeStates:inFolderWithURL:completionHandler:"
+ "providePayloadForComputeStates:inFolderWithURL:completionHandler:"
+ "recordComputeStateDelegate"
+ "setRecordComputeStateDelegate:"
+ "startLogoutTaskForDaemonLibraryManager:"
+ "updateFileURLForComputeState:discardedFileStorageIdentifier:hasUpdated:error:"
+ "v48@0:8@\"CPLEngineLibrary\"16@\"NSArray\"24@\"NSURL\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"CPLLibraryManager\"16@\"NSArray\"24@\"NSURL\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "DELETE FROM %!@(MISSING) WHERE scopeIndex = %!l(MISSING)d AND localIdentifier = %!@(MISSING) AND fileStorageIdentifier = %!@(MISSING)"
- "Notified that user will be switched, we don't have a running sync task"
- "Notified that user will be switched, we have a running sync task"
- "Notified that we need to upload content. Starting sync task"
- "UPDATE OR FAIL %!@(MISSING) SET mingled = %!i(MISSING) WHERE scopeIndex = %!l(MISSING)d AND mingled = %!i(MISSING)"
- "removeComputeState:discardedFileStorageIdentifier:error:"
- "resetMingledRecordsForScopeWithIdentifier:error:"
- "startSyncTaskForDaemonLibraryManager:"

```
