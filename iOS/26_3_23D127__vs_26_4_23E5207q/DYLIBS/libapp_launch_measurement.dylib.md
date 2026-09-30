## libapp_launch_measurement.dylib

> `/usr/lib/libapp_launch_measurement.dylib`

```diff

-25.0.0.0.0
-  __TEXT.__text: 0x4110
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x45b
-  __TEXT.__oslogstring: 0x91d
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__got: 0x20
+29.0.0.0.0
+  __TEXT.__text: 0x43c0
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x4d2
+  __TEXT.__oslogstring: 0xa72
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_methname: 0x85
+  __TEXT.__objc_stubs: 0xc0
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x230
-  __AUTH_CONST.__auth_got: 0x238
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x100
-  __DATA.__bss: 0xc0
+  __AUTH_CONST.__cfstring: 0x80
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x358
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
-  UUID: 79C06F98-B355-3980-98C6-897E039C06E0
-  Functions: 98
-  Symbols:   253
-  CStrings:  96
+  - /usr/lib/libobjc.A.dylib
+  UUID: 585179E0-5D0F-3D24-8D84-95A1AD36B4F2
+  Functions: 106
+  Symbols:   288
+  CStrings:  114
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ ___CFConstantStringClassReference
+ ___block_descriptor_tmp.86
+ ___block_literal_global.88
+ _alm_acquire_pageins_recording_assertion
+ _alm_acquire_pageins_recording_assertion.cold.1
+ _alm_acquire_pageins_recording_assertion.cold.2
+ _alm_app_launch_has_started
+ _alm_release_pageins_recording_assertion
+ _objc_alloc
+ _objc_msgSend
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$invalidate
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x8
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _s_process_tag_assertion
- ___block_descriptor_tmp.84
- ___block_literal_global.86
CStrings:
+ "IsForeground=%{public, signpost.telemetry:number1}d PageInCount=%{public, signpost.telemetry:number2}llu enableTelemetry=YES "
+ "LaunchPrefetch"
+ "RBSPrefetchPageAttribute"
+ "acquireWithError:"
+ "alm_acquire_pageins_recording_assertion: FAILED create the prefetching attribute"
+ "alm_acquire_pageins_recording_assertion: FAILED to acquire assertion: %{public}@"
+ "alm_acquire_pageins_recording_assertion: acquired pageins recording assertion!"
+ "alm_release_pageins_recording_assertion: releasing pageins recording assertion"
+ "app_launch_measurement: pageins recording enabled"
+ "arrayWithObjects:count:"
+ "attributeWithDomain:name:"
+ "com.apple.pagein-prefetching"
+ "currentProcess"
+ "initWithExplanation:target:attributes:"
+ "invalidate"
- "IsForeground=%{public, signpost.telemetry:number1}d PageInCount=%{public, signpost.telemetry:number2}llu"

```
