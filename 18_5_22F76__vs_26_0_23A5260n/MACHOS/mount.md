## mount

> `/sbin/mount`

```diff

-737.100.3.0.0
-  __TEXT.__text: 0x4800
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x580
+751.0.0.0.0
+  __TEXT.__text: 0x4bc0
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x6a0
   __TEXT.__const: 0x3c
-  __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__cstring: 0x112c
+  __TEXT.__gcc_except_tab: 0x248
+  __TEXT.__cstring: 0x1223
   __TEXT.__oslogstring: 0xc
-  __TEXT.__objc_methname: 0x450
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_methname: 0x4ff
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__const: 0x450
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_selrefs: 0x1a8
   __DATA.__data: 0x4
   __DATA.__common: 0x54
   __DATA.__bss: 0x1

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74D55DDD-3FDF-3CF4-9917-45E0AFCD2609
-  Functions: 52
-  Symbols:   150
-  CStrings:  253
+  UUID: 516F272D-6AAD-3C9F-A2E2-1D0614EE92EB
+  Functions: 51
+  Symbols:   164
+  CStrings:  276
 
Symbols:
+ _CFRunLoopRun
+ _FSModuleIdentityAttributeActivateOptionSyntax
+ _FSModuleIdentityAttributeCheckOptionSyntax
+ _FSModuleIdentityAttributeFormatOptionSyntax
+ _OBJC_CLASS_$_FSGenericURLResource
+ _OBJC_CLASS_$_FSServerURLResource
+ _OBJC_CLASS_$_FSTaskMessageSTDIOWithProgress
+ _OBJC_CLASS_$_NSProgress
+ __NSConcreteGlobalBlock
+ _dispatch_async
+ _dispatch_get_global_queue
+ _objc_release_x1
+ _objc_retainBlock
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_unsafeClaimAutoreleasedReturnValue
- _FSActivateOptionSyntaxKey
- _FSCheckOptionSyntaxKey
- _FSFormatOptionSyntaxKey
- _objc_release_x26
CStrings:
+ "@?<v@?>16@?0@\"NSProgress\"8"
+ "FSSupportsGenericURLResources"
+ "FSSupportsServerURLs"
+ "Filesystem %s doesn't support Block Device or PathURL resources, can't preform format/check task."
+ "Filesystem %s supports neither Block Device nor PathURL resources nor ServerURL resources."
+ "Module %s is disabled!\n"
+ "URLWithString:"
+ "addSubscriberForFileURL:withPublishingHandler:"
+ "enumerateOptionsUsingBlock:"
+ "getProgressURLKey"
+ "invoke_tool_from_fskit_block_invoke_10"
+ "invoke_tool_from_fskit_block_invoke_14"
+ "isEnabled"
+ "n"
+ "o"
+ "proxyResourceForBSDName:isWritable:"
+ "q"
+ "receiverWithDelegate:"
+ "setDispatch_group:"
+ "setProgress:"
+ "sharedInstance"
+ "showProgress"
+ "v40@?0@\"NSString\"8@\"NSString\"16Q24^B32"
+ "v8@?0"
- "Filesystem %s supports neither Block Device nor PathURL resources."
- "enumerateOptionsWithBlock:"
- "invoke_tool_from_fskit_block_invoke_12"
- "invoke_tool_from_fskit_block_invoke_9"
- "proxyResourceForBSDName:writable:"
- "v36@?0i8@\"NSString\"12Q20^B28"

```
