## HealthPlatform

> `/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform`

```diff

-5200.1.3.0.0
-  __TEXT.__text: 0x16ce5c
-  __TEXT.__auth_stubs: 0x3090
-  __TEXT.__objc_methlist: 0x53c
-  __TEXT.__const: 0xaf92
-  __TEXT.__cstring: 0x783d
-  __TEXT.__oslogstring: 0x5145
-  __TEXT.__swift5_typeref: 0x403e
-  __TEXT.__swift5_capture: 0x22bc
-  __TEXT.__constg_swiftt: 0x4820
-  __TEXT.__swift5_reflstr: 0x2ef4
-  __TEXT.__swift5_fieldmd: 0x3894
+5200.1.5.4.0
+  __TEXT.__text: 0x1751c4
+  __TEXT.__auth_stubs: 0x30d0
+  __TEXT.__objc_methlist: 0x54c
+  __TEXT.__const: 0xb032
+  __TEXT.__cstring: 0x797d
+  __TEXT.__oslogstring: 0x56e5
+  __TEXT.__swift5_typeref: 0x4130
+  __TEXT.__swift5_capture: 0x2428
+  __TEXT.__constg_swiftt: 0x4938
+  __TEXT.__swift5_reflstr: 0x3044
+  __TEXT.__swift5_fieldmd: 0x39c8
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x7e8
   __TEXT.__swift5_proto: 0x978
-  __TEXT.__swift5_types: 0x4a0
-  __TEXT.__swift5_protos: 0xc4
+  __TEXT.__swift5_types: 0x4b0
+  __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x54
-  __TEXT.__unwind_info: 0x5ca8
-  __TEXT.__eh_frame: 0x4e8c
+  __TEXT.__unwind_info: 0x5e30
+  __TEXT.__eh_frame: 0x514c
   __TEXT.__objc_classname: 0x123
-  __TEXT.__objc_methname: 0x28ff
+  __TEXT.__objc_methname: 0x295e
   __TEXT.__objc_methtype: 0x3ce
-  __DATA_CONST.__got: 0xc88
-  __DATA_CONST.__const: 0x8f8
-  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__got: 0xc90
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdd8
+  __DATA_CONST.__objc_selrefs: 0xdf0
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0x1848
-  __AUTH_CONST.__auth_ptr: 0xd58
-  __AUTH_CONST.__const: 0xc078
-  __AUTH_CONST.__objc_const: 0x4f60
-  __AUTH.__objc_data: 0x908
-  __AUTH.__data: 0xc60
-  __DATA.__data: 0x1b28
+  __AUTH_CONST.__auth_got: 0x1868
+  __AUTH_CONST.__auth_ptr: 0xd60
+  __AUTH_CONST.__const: 0xc5a0
+  __AUTH_CONST.__objc_const: 0x5128
+  __AUTH.__objc_data: 0x9c0
+  __AUTH.__data: 0xdd0
+  __DATA.__data: 0x1bc8
   __DATA.__bss: 0xa6b8
-  __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xcc8
-  __DATA_DIRTY.__data: 0x5938
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__data: 0x5958
   __DATA_DIRTY.__bss: 0x6580
   __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8803
-  Symbols:   673
-  CStrings:  1635
+  Functions: 8950
+  Symbols:   694
+  CStrings:  1669
 
CStrings:
+ "urgentWorkTimeoutInterval"
+ "%!{(MISSING)public}s Urgent work completed after %!l(MISSING)dms"
+ "%!{(MISSING)public}s Fire once completed"
+ "dataUploadRequestStatus"
+ "%!{(MISSING)public}s No requests for legacy generation"
+ "%!{(MISSING)public}s Requesting fire once barrier"
+ "initWithParent:userInfo:"
+ "@24@0:8@?16"
+ "%!{(MISSING)public}s Progress %!s(MISSING) cancellation handler called"
+ "ForegroundTaskQueue"
+ "[%!{(MISSING)public}s] Start was forcefully triggered since it was unexpectedly not yet started."
+ "%!{(MISSING)public}s Calling all fire once barriers"
+ "remote_runForegroundGenerationWithCompletion:"
+ "_TtC14HealthPlatform30HealthAppForegroundWorkManager"
+ "[%!{(MISSING)public}s] Starting"
+ "%!{(MISSING)public}s Cancelling original legacy generation progress"
+ "%!{(MISSING)public}s Starting fire once"
+ "HealthAppForegroundWorkManagerQueue"
+ "%!{(MISSING)public}s Fire once already completed before, calling barrier immediately"
+ "%!{(MISSING)public}s Cancelling legacy generation for progress %!s(MISSING)"
+ "%!{(MISSING)public}s Request to cancel legacy generation"
+ "workRunner"
+ "[%!{(MISSING)public}s] Not yet started, enqueueing a start deadline within %!{(MISSING)public}s"
+ "_TtC14HealthPlatformP33_5822D1995F2B4EBEEC835C675644E4E314ForegroundTask"
+ "%!{(MISSING)public}s Urgent work completion timed out: %!{(MISSING)public}s"
+ "%!{(MISSING)public}s Legacy generation for progress %!s(MISSING) cancelled, but already different current progress: %!s(MISSING)"
+ "%!{(MISSING)public}s Legacy generation completed: %!{(MISSING)bool}d"
+ "@\"NSProgress\"24@0:8@?<v@?@\"NSError\">16"
+ "%!{(MISSING)public}s Starting legacy generation"
+ "%!{(MISSING)public}s Cancelled, but fire once has not completed, calling all the completion with success false"
+ "%!{(MISSING)public}s Requesting legacy generation with created progress %!s(MISSING)"
+ "%!{(MISSING)public}s Starting urgent work"
+ "%!{(MISSING)public}s Cancelling"
+ "%!{(MISSING)public}s Ready, and urgent work already completed, starting legacy generation with progress %!s(MISSING)"

```
