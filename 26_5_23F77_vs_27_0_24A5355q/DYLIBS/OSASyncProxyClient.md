## OSASyncProxyClient

> `/System/Library/PrivateFrameworks/OSASyncProxyClient.framework/OSASyncProxyClient`

```diff

-934.120.2.0.0
-  __TEXT.__text: 0x3a8
-  __TEXT.__auth_stubs: 0x110
-  __TEXT.__objc_methlist: 0x224
+1049.0.0.502.1
+  __TEXT.__text: 0x504
+  __TEXT.__objc_methlist: 0x280
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x3d
+  __TEXT.__cstring: 0x4d
   __TEXT.__oslogstring: 0x3a
-  __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x385
-  __TEXT.__objc_methtype: 0x285
-  __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x20
+  __TEXT.__unwind_info: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x148
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x188
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x280
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x2e0
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xc0
+  __DATA.__objc_ivar: 0xc
+  __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA97D52F-89EA-3F5A-9AF7-F4333B005447
-  Functions: 14
-  Symbols:   98
-  CStrings:  87
+  UUID: 0406ECB8-380F-3F94-AECF-B6E9D611ED63
+  Functions: 19
+  Symbols:   125
+  CStrings:  10
 
Symbols:
+ -[OSASyncProxyClient initWithErrorHandler:progressHandler:]
+ -[OSASyncProxyClient progressHandler]
+ -[OSASyncProxyClient request:generateTransparencyLogs:]
+ -[OSASyncProxyClient setProgressHandler:]
+ -[OSASyncProxyClient transferProgressForFilePath:sentBytes:totalBytes:]
+ _OBJC_IVAR_$_OSASyncProxyClient._progressHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OSASyncProxyCallbacks
+ __OBJC_$_PROTOCOL_METHOD_TYPES_OSASyncProxyCallbacks
+ __OBJC_$_PROTOCOL_REFS_OSASyncProxyCallbacks
+ __OBJC_LABEL_PROTOCOL_$_OSASyncProxyCallbacks
+ __OBJC_PROTOCOL_$_OSASyncProxyCallbacks
+ __OBJC_PROTOCOL_REFERENCE_$_OSASyncProxyCallbacks
+ ___kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$progressHandler
+ _objc_msgSend$request:generateTransparencyLogs:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setProgressHandler:
+ _objc_release_x22
+ _objc_release_x24
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_setProperty_nonatomic_copy
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
+ "wantsProgress"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<OSASyncProxyServices>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "OSASyncProxyClient"
- "OSASyncProxyServices"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_synchRemoteObjectProxy"
- "addEntriesFromDictionary:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "deliver:taskingFile:routing:taskId:asMessage:overRSD:"
- "description"
- "hash"
- "init"
- "initWithErrorHandler:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listDevices:"
- "mutableCopy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "request:logList:"
- "request:logListWithOptions:onComplete:"
- "request:transferGroupWithOptions:onComplete:"
- "request:transferLog:onComplete:"
- "request:transferLog:withOptions:onComplete:"
- "requestProxyMetadata:onComplete:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setRemoteObjectInterface:"
- "superclass"
- "synchronize:withOptions:onComplete:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@0:8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@@\"NSError\">16"
- "v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40B48B52"
- "v56@0:8@16@24@32@40B48B52"
- "zone"

```
