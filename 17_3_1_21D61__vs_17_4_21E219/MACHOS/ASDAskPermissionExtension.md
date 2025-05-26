## ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension`

```diff

-10.3.4.0.0
-  __TEXT.__text: 0x404
-  __TEXT.__auth_stubs: 0x120
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x14
+10.4.34.2.1
+  __TEXT.__text: 0x5a8
+  __TEXT.__auth_stubs: 0x130
+  __TEXT.__objc_stubs: 0x220
+  __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x8
-  __TEXT.__oslogstring: 0xe6
-  __TEXT.__cstring: 0x2c
+  __TEXT.__oslogstring: 0x177
+  __TEXT.__cstring: 0x41
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x10a
-  __TEXT.__objc_methtype: 0xf
-  __TEXT.__unwind_info: 0x50
-  __DATA_CONST.__auth_got: 0x98
+  __TEXT.__objc_methname: 0x15c
+  __TEXT.__objc_methtype: 0x17
+  __TEXT.__unwind_info: 0x58
+  __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x28
+  __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x28
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x78
-  __DATA.__objc_classrefs: 0x18
+  __DATA.__objc_selrefs: 0x98
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2
-  Symbols:   32
-  CStrings:  24
+  Functions: 4
+  Symbols:   36
+  CStrings:  33
 
Symbols:
+ _OBJC_CLASS_$_ASDCheckQueueRequest
+ _OBJC_CLASS_$_ASDCheckQueueRequestOptions
+ __NSConcreteGlobalBlock
+ _objc_alloc
CStrings:
+ "Download queue request complete with result: %{BOOL}d"
+ "Download queue request returned error: %{public}@"
+ "Request to check download queue received"
+ "checkDownloadQueue"
+ "initWithOptions:"
+ "initWithReason:"
+ "sendRequestCompletionBlock:"
+ "v16@0:8"
+ "v20@?0B8@\"NSError\"12"

```
