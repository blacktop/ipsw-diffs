## storagekitd

> `/usr/libexec/storagekitd`

```diff

-934.120.4.0.0
-  __TEXT.__text: 0x2d528
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x61c0
-  __TEXT.__objc_methlist: 0x2854
-  __TEXT.__objc_classname: 0x50d
-  __TEXT.__objc_methname: 0x637a
+1000.0.0.0.0
+  __TEXT.__text: 0x2d750
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_stubs: 0x6220
+  __TEXT.__objc_methlist: 0x2874
+  __TEXT.__objc_classname: 0x4fc
+  __TEXT.__objc_methname: 0x6419
   __TEXT.__objc_methtype: 0xf6e
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0xc7c
-  __TEXT.__cstring: 0x2d70
-  __TEXT.__oslogstring: 0x26ee
-  __TEXT.__unwind_info: 0xa48
-  __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0x508
+  __TEXT.__gcc_except_tab: 0xc8c
+  __TEXT.__cstring: 0x2d66
+  __TEXT.__oslogstring: 0x2745
+  __TEXT.__unwind_info: 0xa58
+  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe60
+  __DATA_CONST.__const: 0xec8
   __DATA_CONST.__cfstring: 0x1f20
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5d50
-  __DATA.__objc_selrefs: 0x1c30
-  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_const: 0x5d68
+  __DATA.__objc_selrefs: 0x1c58
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__objc_data: 0xf50
-  __DATA.__data: 0x760
+  __DATA.__data: 0x700
   __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration
+  - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/StorageKit.framework/StorageKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 13E7768E-8267-3306-B766-90A4005F97C1
-  Functions: 890
-  Symbols:   370
-  CStrings:  2377
+  UUID: DA83CB25-A84A-3576-86FA-CF664A77D0AE
+  Functions: 895
+  Symbols:   373
+  CStrings:  2386
 
Symbols:
+ _SKAPFSVolumeRoleEnterprise
+ _kSKDiskRoleEnterprise
+ _objc_retain_x27
CStrings:
+ "%@ added. There are now %u client(s) connected to storagekitd"
+ "%@ removed. There are now %u client(s) connected to storagekitd"
+ "%s: Add subscriber for progress (%@)"
+ "%s: Subscribed to a progress"
+ "%s: Subscribed to progress"
+ "%s: Unsubscribed from progress."
+ "@?<v@?>16@?0@\"NSProgress\"8"
+ "Ti,N,V_authRefCreationError"
+ "_authRefCreationError"
+ "addSubscriberForFileURL:withPublishingHandler:"
+ "authRefCreationError"
+ "getProgressURLKey"
+ "proxyResourceForBSDName:isWritable:"
+ "setAuthRefCreationError:"
+ "sharedInstance"
+ "validateAuthRef"
- "%@ added. There are now %u client(s) connected to storagetkid"
- "%@ removed. There are now %u client(s) connected to storagetkid"
- "%s: Failed to get progress for %@, %@"
- "FSTaskMessageOps"
- "getFSProgressForTask:replyHandler:"
- "proxyResourceForBSDName:writable:"
- "v24@?0@\"FSTaskProgress\"8@\"NSError\"16"

```
