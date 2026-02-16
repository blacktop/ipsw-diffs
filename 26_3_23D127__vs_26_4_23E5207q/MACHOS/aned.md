## aned

> `/usr/libexec/aned`

```diff

-380.200.3.0.0
-  __TEXT.__text: 0x1e898
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x2760
-  __TEXT.__objc_methlist: 0xc9c
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x316c
-  __TEXT.__cstring: 0x827
-  __TEXT.__oslogstring: 0x2b57
+380.502.0.0.0
+  __TEXT.__text: 0x1f8d4
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x27c0
+  __TEXT.__objc_methlist: 0xcb4
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0x3258
+  __TEXT.__cstring: 0x841
+  __TEXT.__oslogstring: 0x2bf8
   __TEXT.__objc_classname: 0x1a0
-  __TEXT.__objc_methname: 0x2e6c
-  __TEXT.__objc_methtype: 0xb8a
-  __TEXT.__unwind_info: 0x5b0
-  __DATA_CONST.__auth_got: 0x410
+  __TEXT.__objc_methname: 0x2efd
+  __TEXT.__objc_methtype: 0xb90
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x468
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1120
-  __DATA.__objc_selrefs: 0xc20
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_const: 0x1150
+  __DATA.__objc_selrefs: 0xc38
+  __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x380
   __DATA.__bss: 0x68

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler
   - /System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63444913-B140-35D1-896D-1471DFBFA601
-  Functions: 377
-  Symbols:   216
-  CStrings:  978
+  UUID: 3AAAEAA6-92C5-3480-915E-1881547E31AE
+  Functions: 393
+  Symbols:   213
+  CStrings:  992
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
CStrings:
+ "Maximum model memory size: %llu"
+ "TQ,V_maxModelMemorySize"
+ "Unable to connect to ANE device."
+ "Unable to create device controller"
+ "_maxModelMemorySize"
+ "compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:"
+ "maxModelMemorySize"
+ "modelUnLoadingTime"
+ "reportTelemetryToCoreAnalytics:payload:"
+ "set maxModelMemorySize to 0"
+ "set maxModelMemorySize to 0x%llx"
+ "setMaxModelMemorySize:"
+ "unload"
+ "v96@0:8@\"_ANEModel\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@\"NSString\"48@\"NSString\"56@\"NSURL\"64@\"NSString\"72Q80@?<v@?B@\"NSDictionary\"@\"NSError\">88"
+ "v96@0:8@16@24@32@40@48@56@64@72Q80@?88"
- "compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:withReply:"
- "v88@0:8@\"_ANEModel\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@\"NSString\"48@\"NSString\"56@\"NSURL\"64@\"NSString\"72@?<v@?B@\"NSDictionary\"@\"NSError\">80"
- "v88@0:8@16@24@32@40@48@56@64@72@?80"

```
