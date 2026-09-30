## BackgroundTasks

> `/System/Library/Frameworks/BackgroundTasks.framework/Versions/A/BackgroundTasks`

```diff

-1786.80.10.0.0
-  __TEXT.__text: 0x7cd0
+1856.101.1.0.0
+  __TEXT.__text: 0x8230
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x8d8
+  __TEXT.__objc_methlist: 0xa40
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x4f8
+  __TEXT.__cstring: 0x52b
   __TEXT.__oslogstring: 0x5ae
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0x188
-  __TEXT.__objc_methname: 0x1594
-  __TEXT.__objc_methtype: 0x2e9
-  __TEXT.__objc_stubs: 0xf80
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__objc_classname: 0x18a
+  __TEXT.__objc_methname: 0x16cd
+  __TEXT.__objc_methtype: 0x2fa
+  __TEXT.__objc_stubs: 0x1060
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x5d8
   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x12f8
+  __AUTH_CONST.__objc_const: 0x10e0
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x120
   __DATA.__bss: 0x11
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 265770A3-B231-38D6-B36D-6F9080E7F0D5
-  Functions: 205
-  Symbols:   587
-  CStrings:  396
+  UUID: ABFA59F8-6D4D-388B-9E27-7B4E31693E3C
+  Functions: 211
+  Symbols:   601
+  CStrings:  407
 
Symbols:
+ +[BGTaskScheduler _isRunningInExtension].cold.1
+ +[BGTaskScheduler _isRunningInNonExtensionOrApplication].cold.1
+ +[BGTaskScheduler _log].cold.1
+ -[_BGContinuedProcessingTaskRequest applicationBundleIdentifier]
+ -[_BGContinuedProcessingTaskRequest initWithIdentifier:iconBundleIdentifier:applicationBundleIdentifier:]
+ -[_BGContinuedProcessingTaskRequest setApplicationBundleIdentifier:]
+ OBJC_IVAR_$__BGContinuedProcessingTaskRequest._applicationBundleIdentifier
+ _objc_msgSend$applicationBundleIdentifier
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$clientProvidedIconBundleIdentifier
+ _objc_msgSend$firstObject
+ _objc_msgSend$relatedApplications
+ _objc_msgSend$setApplicationBundleIdentifier:
+ _objc_msgSend$setRelatedApplications:
CStrings:
+ "<_BGContinuedProcessingTaskRequest: %@, title: %@, reason: %@, iconBundle: %@, applicationBundle: %@>"
+ "@40@0:8@16@24@32"
+ "T@\"NSString\",C,N,V_applicationBundleIdentifier"
+ "_applicationBundleIdentifier"
+ "applicationBundleIdentifier"
+ "arrayWithObject:"
+ "firstObject"
+ "initWithIdentifier:iconBundleIdentifier:applicationBundleIdentifier:"
+ "relatedApplications"
+ "setApplicationBundleIdentifier:"
+ "setRelatedApplications:"
- "<_BGContinuedProcessingTaskRequest: %@, title: %@>"

```
