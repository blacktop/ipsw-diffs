## BackgroundTasks

> `/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks`

```diff

-2109.0.44.502.1
-  __TEXT.__text: 0x8e30
+2109.0.61.502.1
+  __TEXT.__text: 0x937c
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xba0
+  __TEXT.__objc_methlist: 0xbc0
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x5d2
+  __TEXT.__cstring: 0x65c
   __TEXT.__oslogstring: 0x7e8
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x1cd2
-  __TEXT.__objc_methtype: 0x37b
-  __TEXT.__objc_stubs: 0x14c0
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__objc_classname: 0x1bd
+  __TEXT.__objc_methname: 0x1dea
+  __TEXT.__objc_methtype: 0x38f
+  __TEXT.__objc_stubs: 0x15a0
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x730
+  __DATA_CONST.__objc_selrefs: 0x760
   __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x13b8
+  __AUTH_CONST.__cfstring: 0x4a0
+  __AUTH_CONST.__objc_const: 0x13e8
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x188
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B40B4B6-3F1C-3574-B4E7-AC83DD7368E6
-  Functions: 242
-  Symbols:   981
-  CStrings:  506
+  UUID: 1DADD63A-75AB-3A07-978F-70EDE406FFA7
+  Functions: 248
+  Symbols:   1001
+  CStrings:  517
 
Symbols:
+ -[BGContinuedProcessingTaskRequest _activity].cold.1
+ -[BGContinuedProcessingTaskRequest initWithIdentifier:title:subtitle:onBehalfOf:]
+ -[BGContinuedProcessingTaskRequest representedApplicationBundleIdentifier]
+ -[BGContinuedProcessingTaskRequest setRepresentedApplicationBundleIdentifier:]
+ _OBJC_IVAR_$_BGContinuedProcessingTaskRequest._representedApplicationBundleIdentifier
+ _objc_msgSend$initWithIdentifier:title:subtitle:onBehalfOf:
+ _objc_msgSend$representedApplicationBundleIdentifier
+ _objc_msgSend$resources
+ _objc_msgSend$setIsForegroundAppProxy:
+ _objc_msgSend$setRepresentedApplicationBundleIdentifier:
+ _objc_msgSend$setRequiredResources:
+ _objc_msgSend$setStrategy:
+ _objc_msgSend$submissionStrategy
- _objc_msgSend$initWithIdentifier:title:subtitle:
CStrings:
+ "<BGContinuedProcessingTaskRequest: %@, (title: %@, subtitle: %@, resources: %@, submissionStrategy: %@, applicationBundleIdentifier: %@)>"
+ "@48@0:8@16@24@32@40"
+ "T@\"NSString\",C,N,V_representedApplicationBundleIdentifier"
+ "_representedApplicationBundleIdentifier"
+ "initWithIdentifier:title:subtitle:onBehalfOf:"
+ "representedApplicationBundleIdentifier"
+ "resources"
+ "setIsForegroundAppProxy:"
+ "setRepresentedApplicationBundleIdentifier:"
+ "submissionStrategy"

```
