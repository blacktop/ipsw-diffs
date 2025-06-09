## nanotimekitcompaniond

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond`

```diff

-2483.147.79.1.2
-  __TEXT.__text: 0x40334
+2483.284.3.0.0
+  __TEXT.__text: 0x3f8d4
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x5e60
+  __TEXT.__objc_stubs: 0x5e00
   __TEXT.__objc_methlist: 0x25d0
   __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x2418
-  __TEXT.__objc_methname: 0x6e65
-  __TEXT.__objc_classname: 0x64b
-  __TEXT.__objc_methtype: 0x14fe
-  __TEXT.__const: 0x120
-  __TEXT.__oslogstring: 0x55cd
-  __TEXT.__ustring: 0x286
-  __TEXT.__unwind_info: 0x10a8
+  __TEXT.__cstring: 0x239a
+  __TEXT.__objc_methname: 0x6de9
+  __TEXT.__objc_classname: 0x62c
+  __TEXT.__objc_methtype: 0x1515
+  __TEXT.__const: 0xf0
+  __TEXT.__oslogstring: 0x5539
+  __TEXT.__ustring: 0x1ae
+  __TEXT.__unwind_info: 0x1078
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x1cb0
-  __DATA_CONST.__cfstring: 0x1640
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x1bc0
+  __DATA_CONST.__cfstring: 0x1540
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x6358
-  __DATA.__objc_selrefs: 0x1ba0
+  __DATA.__objc_const: 0x38a8
+  __DATA.__objc_selrefs: 0x1b88
   __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0xa88
-  __DATA.__bss: 0x1f0
+  __DATA.__data: 0xa28
+  __DATA.__bss: 0x1f8
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AB5724C-DC6E-3EE6-843F-45321C2E100A
-  Functions: 1285
-  Symbols:   335
-  CStrings:  2171
+  UUID: ADBE2E60-EEA2-359C-BA07-93CCAF217585
+  Functions: 1267
+  Symbols:   332
+  CStrings:  2153
 
Symbols:
+ _NTKCacheSnapshotResultOfFace
+ _NTKCachedSnapshotResultForFace
+ _OBJC_CLASS_$_NTKKeyedHashingEncoder
+ _OBJC_CLASS_$_NTKReplicatedSnapshotListenerService
- _NTKCacheSnapshotOfFace
- _NTKCachedSnapshotForFace
- _NTKFaceBundleArgonDescriptorKey
- _NTKFaceBundleIdentifierKey
- _OBJC_CLASS_$_CLKKeyedHashingEncoder
- _OBJC_CLASS_$_NTKArgonKeyDescriptor
- _OBJC_CLASS_$_NTKFaceSupportUnlockAttemptEventRecorder
CStrings:
+ "%@: %s face: %@ requestSnapshotOfFaceInstanceDescriptor competionBlock: %@ %@."
+ "%@: %s wantsToPersistSnapshot: YES, result: %@"
+ "-[NTKDFaceSnapshotClientHandler requestSnapshotOfFaceInstanceDescriptor:options:completion:]"
+ "-[NTKDFaceSnapshotController requestSnapshotOfFace:options:completion:]"
+ "-[NTKDFaceSnapshotController requestSnapshotOfFace:options:completion:]_block_invoke"
+ "-[NTKDFaceSnapshotController requestSnapshotOfFace:options:completion:]_block_invoke_2"
+ "com.apple.nanotimekid.daemon"
+ "com.apple.nanotimekit.snapshots"
+ "faceSnapshotServiceInterface"
+ "hasBlankComplications"
+ "requestSnapshotOfFace:options:completion:"
+ "requestSnapshotOfFaceInstanceDescriptor:options:completion:"
+ "snapshot"
+ "v24@?0@\"NTKFaceSnapshotResult\"8@\"NSError\"16"
+ "v40@0:8@\"NTKFaceInstanceDescriptor\"16@\"NSDictionary\"24@?<v@?@\"NTKFaceSnapshotResult\"@\"NSError\">32"
- "%@: %s face: %@ provideSnapshotOfFace competionBlock: %d %@."
- "%@: %s wantsToPersistSnapshot: YES, image: %@"
- "-[NTKDFaceSnapshotController provideSnapshotOfFace:options:completion:]"
- "-[NTKDFaceSnapshotController provideSnapshotOfFace:options:completion:]_block_invoke"
- "-[NTKDFaceSnapshotController provideSnapshotOfFace:options:completion:]_block_invoke_2"
- "A rare error has occurred while syncing clock faces between your watch and phone. Please tap 'OK' to open Tap-to-Radar and file a bug. (Internal alert only.)"
- "Clock Face Sync Error"
- "Couldn't record being for %@ - %@"
- "Failed to create face from data: %@"
- "NTKFaceSnapshotServiceProtocol"
- "Sync: New Face Failed to Unzip After Syncing from Gizmo (via Prompt)"
- "argon_initWithJSONRepresentation:"
- "beginRecordingForIdentifier:method:completion:"
- "c"
- "couldn't decrypt face JSON from key descriptor %@"
- "fileName"
- "ingestKeyDescriptor:withMethod:completion:"
- "prompting to raise a radar re: unzip failure"
- "provideSnapshotOfFace:options:completion:"
- "provideSnapshotOfFaceInstanceDescriptor:options:completion:"
- "sharedRecorder"
- "tmp"
- "unzip failed, data written to disk for analysis: %@"
- "unzipFile:toPath:completionHandler:"
- "v20@?0B8@\"NSError\"12"
- "v40@0:8@\"NTKFaceInstanceDescriptor\"16@\"NSDictionary\"24@?<v@?B@\"UIImage\">32"

```
