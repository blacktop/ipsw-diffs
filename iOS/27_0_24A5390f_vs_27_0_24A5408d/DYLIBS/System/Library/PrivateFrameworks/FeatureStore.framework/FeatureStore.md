## FeatureStore

> `/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore`

```diff

-3600.22.11.0.0
-  __TEXT.__text: 0x25d5c
-  __TEXT.__objc_methlist: 0xfd4
-  __TEXT.__const: 0x1600
-  __TEXT.__cstring: 0xb69
-  __TEXT.__oslogstring: 0xae2
+3600.22.17.0.0
+  __TEXT.__text: 0x264c4
+  __TEXT.__objc_methlist: 0x102c
+  __TEXT.__const: 0x1610
+  __TEXT.__cstring: 0xbe9
+  __TEXT.__oslogstring: 0xb62
   __TEXT.__swift5_typeref: 0x681
   __TEXT.__constg_swiftt: 0xd88
   __TEXT.__swift5_fieldmd: 0x4f4

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xdd0
+  __TEXT.__unwind_info: 0xdf8
   __TEXT.__eh_frame: 0x1490
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__got: 0x358
-  __AUTH_CONST.__const: 0x1568
+  __AUTH_CONST.__const: 0x1588
   __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x5258
-  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH_CONST.__objc_const: 0x55f8
+  __AUTH_CONST.__auth_got: 0xab8
   __AUTH.__objc_data: 0x3b0
   __AUTH.__data: 0x240
-  __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x668
+  __DATA.__objc_ivar: 0x88
+  __DATA.__data: 0x6c8
   __DATA.__bss: 0xee8
-  __DATA.__common: 0x58
+  __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x668
   __DATA_DIRTY.__data: 0x508
-  __DATA_DIRTY.__bss: 0xe50
+  __DATA_DIRTY.__bss: 0xe60
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1256
-  Symbols:   2910
-  CStrings:  137
+  Functions: 1281
+  Symbols:   2942
+  CStrings:  143
 
Symbols:
+ -[FSFCallKitUtil callObserver:callChanged:]
+ -[FSFCallKitUtil observerQueue]
+ -[FSFCallKitUtil recomputeOnCallFromCalls:]
+ -[FSFCallKitUtil setCallCenter:]
+ -[FSFCallKitUtil setObserverQueue:]
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiersShySSGvMZ
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiersShySSGvMZ.resume
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiersShySSGvau
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiersShySSGvgZ
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiersShySSGvpZ
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiersShySSGvsZ
+ _$s12FeatureStore0aB7ServiceC27fcsAllowedStreamIdentifiers_WZ
+ _$s12FeatureStore0aB7ServiceC28seedAllowedStreamIdentifiersShySSGvgZTm
+ _$s12FeatureStore0aB7ServiceC28seedAllowedStreamIdentifiersShySSGvsZTm
+ _FSFCallKitLog.onceToken
+ _FSFCallKitLog.sLog
+ _OBJC_IVAR_$_FSFCallKitUtil._isOnCall
+ _OBJC_IVAR_$_FSFCallKitUtil._observerQueue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CXCallObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CXCallObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_CXCallObserverDelegate
+ __OBJC_CLASS_PROTOCOLS_$_FSFCallKitUtil
+ __OBJC_LABEL_PROTOCOL_$_CXCallObserverDelegate
+ __OBJC_PROTOCOL_$_CXCallObserverDelegate
+ ___22-[FSFCallKitUtil init]_block_invoke
+ ___FSFCallKitLog_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ _dispatch_async
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _objc_msgSend$recomputeOnCallFromCalls:
+ _objc_msgSend$setDelegate:queue:
+ _os_log_create
- _$s12FeatureStore0aB7ServiceC28seedAllowedStreamIdentifiers_Wz
CStrings:
+ "CXCallObserver callChanged: changedCallEnded=%{public}d isOnCall=%{public}d"
+ "CallKit"
+ "FCS-build capture decision for stream %s: %s"
+ "allowed (in fcsAllowedStreamIdentifiers)"
+ "blocked (not in fcsAllowedStreamIdentifiers)"
+ "com.apple.FeatureStore.callkit"
```
