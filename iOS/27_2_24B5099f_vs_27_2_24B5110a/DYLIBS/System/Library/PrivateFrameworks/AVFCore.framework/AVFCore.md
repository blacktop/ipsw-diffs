## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2475.12.1.0.0
-  __TEXT.__text: 0x1bd1f8
+2475.13.1.1.0
+  __TEXT.__text: 0x1bd580
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x1c2f4
+  __TEXT.__objc_methlist: 0x1c2fc
   __TEXT.__cstring: 0x26f53
-  __TEXT.__gcc_except_tab: 0xa02c
+  __TEXT.__gcc_except_tab: 0xa044
   __TEXT.__const: 0x1e48
-  __TEXT.__oslogstring: 0x50ad
+  __TEXT.__oslogstring: 0x5128
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x40d

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xc500
+  __TEXT.__unwind_info: 0xc508
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5bb8
+  __DATA_CONST.__const: 0x5be0
   __DATA_CONST.__objc_classlist: 0x1240
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb6b0
+  __DATA_CONST.__objc_selrefs: 0xb6b8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xd70
   __DATA_CONST.__objc_arraydata: 0x310

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12121
-  Symbols:   23982
-  CStrings:  4303
+  Functions: 12122
+  Symbols:   23984
+  CStrings:  4304
 
Symbols:
+ -[AVPlayerItemIntegratedTimelinePeriodicObserver _doesTimeResideInPrimarySegment:atTime:timeMappingOut:]
+ ___block_descriptor_57_e8_32o40r48r_e5_v8?0ls32l8r40l8r48l8
Functions:
~ -[AVSampleBufferVideoRenderer _setRequiresFlushToResumeDecoding:] : 708 -> 1104
~ ___65-[AVSampleBufferVideoRenderer _setRequiresFlushToResumeDecoding:]_block_invoke : 44 -> 112
~ -[AVPlayerItemIntegratedTimelinePeriodicObserver rescheduleObserverWithSnapshot:itemToSchedule:] : 1984 -> 2120
+ -[AVPlayerItemIntegratedTimelinePeriodicObserver _doesTimeResideInPrimarySegment:atTime:timeMappingOut:]
CStrings:
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Waking a suspended Swift enqueue because a flush is now required"
```
