## visualintelligenced

> `/System/Library/PrivateFrameworks/VisualIntelligenceServices.framework/visualintelligenced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-234.0.0.0.0
-  __TEXT.__text: 0x3a988
-  __TEXT.__auth_stubs: 0x1c50
-  __TEXT.__objc_stubs: 0x1c0
+246.0.0.0.0
+  __TEXT.__text: 0x3b22c
+  __TEXT.__auth_stubs: 0x1c80
+  __TEXT.__objc_stubs: 0x260
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x1618
-  __TEXT.__cstring: 0x9b5
+  __TEXT.__const: 0x1628
+  __TEXT.__cstring: 0xa17
   __TEXT.__swift5_typeref: 0x8f5
   __TEXT.__objc_classname: 0x3a7
-  __TEXT.__objc_methname: 0x3c4
-  __TEXT.__objc_methtype: 0x16f
+  __TEXT.__objc_methname: 0x450
   __TEXT.__constg_swiftt: 0x580
   __TEXT.__swift5_reflstr: 0x354
   __TEXT.__swift5_fieldmd: 0x498
-  __TEXT.__oslogstring: 0x193a
-  __TEXT.__swift5_capture: 0x7a0
+  __TEXT.__oslogstring: 0x19fa
+  __TEXT.__swift5_capture: 0x7bc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xbc
   __TEXT.__swift5_types: 0x64
   __TEXT.__swift_as_entry: 0x12c
   __TEXT.__swift_as_ret: 0xec
-  __TEXT.__swift_as_cont: 0x1f8
+  __TEXT.__swift_as_cont: 0x200
   __TEXT.__swift5_assocty: 0x18
+  __TEXT.__objc_methtype: 0x19c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xc60
-  __TEXT.__eh_frame: 0x2508
-  __DATA_CONST.__const: 0x1698
+  __TEXT.__unwind_info: 0xc98
+  __TEXT.__eh_frame: 0x2568
+  __DATA_CONST.__const: 0x1710
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0xe30
-  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__auth_got: 0xe48
+  __DATA_CONST.__got: 0x6f8
   __DATA_CONST.__auth_ptr: 0x408
-  __DATA.__objc_const: 0x1098
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_const: 0x1388
+  __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xfa0
+  __DATA.__data: 0xfe0
   __DATA.__bss: 0x1790
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 800
-  Symbols:   777
-  CStrings:  271
+  Functions: 813
+  Symbols:   782
+  CStrings:  281
 
Symbols:
+ _$s22VisualIntelligenceCore24InferenceResourceManagerC22releaseWarmHoldForExityyFTj
+ _$s22VisualIntelligenceCore24InferenceResourceManagerC5clock11idleTimeout14evictionPolicy18warmStateDidChangeACyxGx_s8DurationVAA08EvictionK0OySbYbcSgtcfC
+ _$s22VisualIntelligenceCore24InferenceResourceManagerCAAs15ContinuousClockVRszrlE6sharedACyAEGvgZ
+ _$s22VisualIntelligenceCore24InferenceResourceManagerCyxGScAAAMc
+ _OBJC_CLASS_$_NSThread
+ __exit
- _$s22VisualIntelligenceCore24InferenceResourceManagerC5clock11idleTimeout14evictionPolicyACyxGx_s8DurationVAA08EvictionK0OtcfC
CStrings:
+ "%s graceful shutdown exceeded %{public}fs; force-exiting"
+ "Acquired warm os_transaction (IRM resources warm)"
+ "Cancelling in-flight prewarm work for daemon shutdown"
+ "Daemon shutdown raced prewarm launch handler setup; nothing to cancel"
+ "Released warm os_transaction (IRM resources evicted)"
+ "com.apple.visualintelligence.daemon.shutdown"
+ "com.apple.visualintelligenced.irm-warm"
+ "initWithBlock:"
+ "setName:"
+ "setQualityOfService:"
+ "sleepForTimeInterval:"
+ "start"
- "Daemon shutdown raced prewarm launch handler setup; transaction not released"
- "Releasing in-flight prewarm task for daemon shutdown"
```
