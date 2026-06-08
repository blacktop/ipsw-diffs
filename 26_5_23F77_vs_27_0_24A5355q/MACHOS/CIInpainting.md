## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`

```diff

-1592.120.2.0.0
-  __TEXT.__text: 0xb3b4
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x1240
+1653.0.0.120.2
+  __TEXT.__text: 0x9d04
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x45c
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x1570
-  __TEXT.__cstring: 0x1854
-  __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methname: 0x1262
-  __TEXT.__objc_methtype: 0x24a
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x1520
+  __TEXT.__cstring: 0x12a5
+  __TEXT.__objc_classname: 0x3b
+  __TEXT.__objc_methname: 0x1132
+  __TEXT.__objc_methtype: 0x1c4
   __TEXT.__oslogstring: 0x6c6
-  __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__inpbpm: 0x944
-  __TEXT.__unwind_info: 0x420
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__cfstring: 0xc40
+  __TEXT.__unwind_info: 0x380
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0xc20
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x608
-  __DATA.__objc_selrefs: 0x5f0
-  __DATA.__objc_ivar: 0x5c
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x1b8
+  __DATA.__objc_const: 0x698
+  __DATA.__objc_selrefs: 0x538
+  __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0xa8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82745C27-FA5E-3D22-8C68-B20ECE0FDF67
-  Functions: 168
-  Symbols:   160
-  CStrings:  517
+  UUID: 185D5C3F-8182-3021-9366-D909E5023306
+  Functions: 135
+  Symbols:   152
+  CStrings:  447
 
Symbols:
+ _NSClassFromString
+ _kCIAttributeFilterCategories
+ _kCICategoryApplePrivate
+ _kCICategorySharpen
+ _kCICategoryStillImage
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
- _CFAbsoluteTimeGetCurrent
- _OBJC_CLASS_$_NSAssertionHandler
- _OBJC_CLASS_$_NSCache
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSObject
- __Block_object_dispose
- ___objc_personality_v0
- __sl_dlopen
- _dispatch_async
- _dispatch_queue_create
- _dispatch_sync
- _dlerror
- _dlsym
- _free
- _objc_msgSendSuper2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _printf
CStrings:
+ "CIEspressoWrapper"
+ "CIInpaintDetailFilter"
+ "T@\"NSNumber\",&,VinputEnableFirstPass"
+ "T@\"NSNumber\",&,VinputEnableSecondPass"
+ "bindInput:buffer:"
+ "bindOutput:buffer:"
+ "cachedWrapperWithPath:"
+ "inputEnableFirstPass"
+ "inputEnableSecondPass"
+ "setInputEnableFirstPass:"
+ "setInputEnableSecondPass:"
- "%s"
- "+[CIIF_EspressoWrapper cachedEspressoWrapper:]"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "B24@0:8r*16"
- "CIIF_EspressoWrapper"
- "CIImageProcessorDigestObject"
- "EspressoWrapper.m"
- "T@\"NSString\",R,V_path"
- "^v"
- "^v16@0:8"
- "_buildState"
- "_ctx"
- "_loadState"
- "_path"
- "_plan"
- "_planIdx"
- "_queue"
- "bind:buffer:"
- "build time: %g\n"
- "buildAsync"
- "buildWait"
- "c"
- "cache"
- "cachedEspressoWrapper:"
- "clearCache"
- "com.apple.CIIF_EspressoWrapper.nscache"
- "com.apple.rawexpose.espressowrapper"
- "ctx"
- "currentHandler"
- "dealloc"
- "errorWithDomain:code:userInfo:"
- "espresso_context_destroy"
- "espresso_context_ref_t soft_espresso_create_context(espresso_engine_t, int)"
- "espresso_create_context"
- "espresso_create_plan_and_load_network"
- "espresso_network_bind_direct_cvpixelbuffer"
- "espresso_network_query_blob_shape"
- "espresso_plan_build"
- "espresso_plan_destroy"
- "espresso_plan_execute_sync"
- "espresso_plan_ref_t soft_espresso_create_plan_and_load_network(espresso_context_ref_t, int, const char *, espresso_network_t *)"
- "espresso_plan_submit"
- "espresso_plan_submit_set_multiple_buffering"
- "espresso_return_status_t soft_espresso_context_destroy(espresso_context_ref_t)"
- "espresso_return_status_t soft_espresso_network_bind_direct_cvpixelbuffer(espresso_network_t, const char *, void *)"
- "espresso_return_status_t soft_espresso_network_query_blob_shape(espresso_network_t, const char *, size_t *, size_t *)"
- "espresso_return_status_t soft_espresso_plan_build(espresso_plan_ref_t)"
- "espresso_return_status_t soft_espresso_plan_destroy(espresso_plan_ref_t)"
- "espresso_return_status_t soft_espresso_plan_execute_sync(espresso_plan_ref_t)"
- "espresso_return_status_t soft_espresso_plan_submit(espresso_plan_ref_t, __strong dispatch_queue_t, void (^__strong)(espresso_error_info_t *))"
- "espresso_return_status_t soft_espresso_plan_submit_set_multiple_buffering(espresso_plan_ref_t, size_t)"
- "execute"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasBlob:"
- "i24@0:8@?16"
- "i32@0:8r*16^{__CVBuffer=}24"
- "init"
- "initWithPath:"
- "load time: %g\n"
- "loadAsync"
- "loadWait"
- "objectForKey:"
- "plan"
- "planIdx"
- "removeAllObjects"
- "setCountLimit:"
- "setCtx:"
- "setEvictsObjectsWhenApplicationEntersBackground:"
- "setName:"
- "setObject:forKey:"
- "setPlan:"
- "setPlanIdx:"
- "softlink:r:path:/System/Library/PrivateFrameworks/Espresso.framework/Espresso"
- "stringWithUTF8String:"
- "v16@?0^{?=ii*}8"
- "v20@0:8i16"
- "v24@0:8^v16"
- "void *EspressoLibrary(void)"
- "w"

```
