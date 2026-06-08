## AppSSODaemon

> `/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon`

```diff

-483.120.4.0.0
-  __TEXT.__text: 0x7ff8
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x588
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__objc_methname: 0x159f
-  __TEXT.__objc_classname: 0x13b
-  __TEXT.__objc_methtype: 0x647
-  __TEXT.__cstring: 0xc52
-  __TEXT.__oslogstring: 0x7d3
-  __TEXT.__dlopen_cstrs: 0x1ae
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x4a0
-  __DATA_CONST.__cfstring: 0x4c0
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x48
+635.0.0.0.0
+  __TEXT.__text: 0x7e54
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x14a0
+  __TEXT.__objc_methlist: 0x5d8
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__objc_methname: 0x164f
+  __TEXT.__objc_classname: 0x16d
+  __TEXT.__objc_methtype: 0x6a8
+  __TEXT.__cstring: 0xd97
+  __TEXT.__oslogstring: 0x8f1
+  __TEXT.__dlopen_cstrs: 0x1f8
+  __TEXT.__unwind_info: 0x2a0
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__cfstring: 0x520
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x1198
-  __DATA.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0xf0
+  __DATA.__objc_const: 0x1258
+  __DATA.__objc_selrefs: 0x690
   __DATA.__objc_ivar: 0x48
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x360
-  __DATA.__bss: 0xf8
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33EE0BC4-4ECF-3033-8523-91B652D8C058
-  Functions: 166
-  Symbols:   102
-  CStrings:  479
+  UUID: FD62AFFE-13BF-3DEE-B79B-45CC4B09E529
+  Functions: 177
+  Symbols:   116
+  CStrings:  507
 
Symbols:
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSXPCInterface
+ __os_feature_enabled_impl
+ __xpc_event_key_name
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "DDM Configuration Service: %{public}@, %{public}@"
+ "ExtensibleSSOConfiguration"
+ "RemoteManagement"
+ "SODDMConfigurationListener"
+ "SODDMConfigurationService"
+ "SODDMConfigurationServiceProtocol"
+ "The remote object does not implement extensionCleanupWithCompletion"
+ "allDeclarationKeysWithCompletion:"
+ "applyConfiguration:replaceKey:completion:"
+ "client connection invalidated during authorization"
+ "com.apple.AppSSO.ddm-configuration-xpc"
+ "com.apple.AppSSODaemon.notifications"
+ "com.apple.distnoted.matching.trusted"
+ "errorWithCode:message:"
+ "extensionCleanupWithCompletion not implemented"
+ "firing orphaned authenticateCompletion — client disconnected during auth"
+ "interfaceWithProtocol:"
+ "main: DDM configuration listener disabled"
+ "main: received trusted distnoted event: %{public}@"
+ "removeConfiguration:completion:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO"
+ "stringWithUTF8String:"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSError\">32"

```
