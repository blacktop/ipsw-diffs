## PhotosSearchDiagnostics

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosSearchDiagnostics.appex/PhotosSearchDiagnostics`

```diff

-760.6.111.0.0
-  __TEXT.__text: 0x4d4
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x319
-  __TEXT.__oslogstring: 0x49
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x15e
-  __TEXT.__objc_methtype: 0xb
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x20
-  __DATA_CONST.__cfstring: 0x200
+760.6.150.0.0
+  __TEXT.__text: 0xc2c
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x64
+  __TEXT.__cstring: 0x37c
+  __TEXT.__oslogstring: 0x1b1
+  __TEXT.__objc_classname: 0x22
+  __TEXT.__objc_methname: 0x292
+  __TEXT.__objc_methtype: 0x23
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0xb8
+  __DATA.__objc_selrefs: 0xb0
+  __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Photos.framework/Photos

   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2
-  Symbols:   36
-  CStrings:  30
+  Functions: 9
+  Symbols:   74
+  CStrings:  53
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSString
+ _PHSearchFeedbackDiagnosticExtensionParameterKey
+ _PHSearchFeedbackDiagnosticExtensionSearchQueryInfoKey
+ _PHSearchFeedbackDiagnosticExtensionVisibleAssetUUIDsKey
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __dispatch_source_type_vnode
+ __os_log_error_impl
+ _close
+ _dispatch_once
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_resume
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_source_create
+ _dispatch_source_set_cancel_handler
+ _dispatch_source_set_event_handler
+ _dispatch_time
+ _objc_release
+ _objc_release_x28
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x8
+ _open
- _objc_release_x25
CStrings:
+ "@16@0:8"
+ "@32@0:8@16d24"
+ "Did not receive data from the Photos app."
+ "JSONObjectWithData:options:error:"
+ "PhotosSearchDiagnostics could not monitor filesystem. FD returned: %d"
+ "PhotosSearchDiagnostics found a file, but it could not get its contents because of: %@"
+ "PhotosSearchDiagnostics is attempting to read file."
+ "PhotosSearchDiagnostics timed out waiting for the diagnostic file to be created"
+ "PhotosSearchDiagnostics was unable to read data provided by Photos: %@"
+ "URLByDeletingLastPathComponent"
+ "collectDiagnosticsForLibrary:resultJSON:onScreenAssets:toPath:"
+ "com.apple.photossearchdiagnostics.filesystem"
+ "error"
+ "fileQueueToken"
+ "fileSystemRepresentation"
+ "filesystemQueue"
+ "firstObject"
+ "getContentsOfFileAtPath:timeout:"
+ "initWithBase64EncodedString:options:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "q"
+ "stringWithContentsOfURL:encoding:error:"
+ "v8@?0"
- "collectDiagnosticsForLibrary:toPath:"

```
