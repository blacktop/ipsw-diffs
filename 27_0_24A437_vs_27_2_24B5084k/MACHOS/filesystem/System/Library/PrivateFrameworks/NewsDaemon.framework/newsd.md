## newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5934.3.0.0.0
-  __TEXT.__text: 0x50fa8
-  __TEXT.__auth_stubs: 0x22b0
-  __TEXT.__objc_stubs: 0x42a0
-  __TEXT.__objc_methlist: 0x1a08
+5960.0.0.0.0
+  __TEXT.__text: 0x515e4
+  __TEXT.__auth_stubs: 0x22a0
+  __TEXT.__objc_stubs: 0x4360
+  __TEXT.__objc_methlist: 0x1a40
   __TEXT.__const: 0x1e70
-  __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__cstring: 0x2b61
-  __TEXT.__objc_methname: 0x5f25
-  __TEXT.__oslogstring: 0x27cd
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__cstring: 0x2a81
+  __TEXT.__objc_methname: 0x5f95
+  __TEXT.__oslogstring: 0x288d
   __TEXT.__objc_classname: 0x95c
   __TEXT.__objc_methtype: 0x1bf7
   __TEXT.__swift5_typeref: 0xd39

   __TEXT.__swift5_proto: 0x118
   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift_as_entry: 0xd8
-  __TEXT.__swift_as_cont: 0x1b8
+  __TEXT.__swift_as_cont: 0x1d0
   __TEXT.__swift5_capture: 0x520
   __TEXT.__swift_as_ret: 0x110
   __TEXT.__swift5_assocty: 0xd0
-  __TEXT.__unwind_info: 0x1780
-  __TEXT.__eh_frame: 0x2768
-  __DATA_CONST.__const: 0x25c0
-  __DATA_CONST.__cfstring: 0x4c0
+  __TEXT.__unwind_info: 0x17c8
+  __TEXT.__eh_frame: 0x26e8
+  __DATA_CONST.__const: 0x2658
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1168
+  __DATA_CONST.__auth_got: 0x1160
   __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x5a0
   __DATA.__objc_const: 0x3c90
-  __DATA.__objc_selrefs: 0x15c8
+  __DATA.__objc_selrefs: 0x15f8
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0xd78
   __DATA.__data: 0x1e50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1474
-  Symbols:   976
-  CStrings:  1527
+  Functions: 1483
+  Symbols:   975
+  CStrings:  1532
 
Symbols:
+ _$s10NewsDaemon29ProxyScoringServiceConnectionC13InterestTokenC10invalidateyyF
+ _$s10NewsDaemon29ProxyScoringServiceConnectionC13interestTokenAC08InterestH0CyF
- _$s10NewsDaemon29ProxyScoringServiceConnectionC11popInterestyyF
- _$s10NewsDaemon29ProxyScoringServiceConnectionC12pushInterestyyF
- _objc_retain_x28
CStrings:
+ "T@\"<NDDownloadConsumer>\",&,N,V_consumer"
+ "TB,N,GisInvalidated,V_invalidated"
+ "_invalidated"
+ "_sendPersistedArchivesToConsumerForRequest:"
+ "connectionDidInvalidate:"
+ "consumer proxy invalidated, draining %lu messages, connection=%{public}@"
+ "consumer proxy lost connection, will drain %lu messages, connection=%{public}@"
+ "ignoring consumer=%p registered outside of an XPC connection"
+ "isConnectedTo:"
+ "isInvalidated"
+ "removeAllObjects"
+ "setConsumer:"
+ "setInvalidated:"
+ "tearing down consumer=%p after its connection went away"
- "-[NDContentDownloadService registerDownloadConsumer:]_block_invoke"
- "-[NDContentDownloadService setCurrentConnection:]"
- "T@\"<NDDownloadConsumer>\",R,N,V_consumer"
- "T@\"NSXPCConnection\",W,N,V_currentConnection"
- "_currentConnection"
- "consumer proxy lost connection, will drop %lu messages, connection=%{public}@"
- "registering a consumer without an XPC connection"
- "replacing XPC connection while a consumer is already active"
- "setCurrentConnection:"
```
