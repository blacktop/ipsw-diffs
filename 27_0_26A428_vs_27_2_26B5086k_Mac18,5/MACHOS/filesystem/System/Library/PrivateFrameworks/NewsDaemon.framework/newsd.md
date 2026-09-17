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

-5934.0.2.0.0
-  __TEXT.__text: 0x47f68
+5960.0.0.0.0
+  __TEXT.__text: 0x486d0
   __TEXT.__auth_stubs: 0x1ca0
-  __TEXT.__objc_stubs: 0x4200
-  __TEXT.__objc_methlist: 0x19a0
+  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_methlist: 0x19d8
   __TEXT.__const: 0x1c90
-  __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0x2c81
-  __TEXT.__objc_methname: 0x5da5
-  __TEXT.__oslogstring: 0x205d
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__cstring: 0x2b91
+  __TEXT.__objc_methname: 0x5e05
+  __TEXT.__oslogstring: 0x211d
   __TEXT.__objc_classname: 0x8dc
   __TEXT.__objc_methtype: 0x1b37
   __TEXT.__swift5_typeref: 0xc89

   __TEXT.__swift5_proto: 0x110
   __TEXT.__swift5_types: 0x9c
   __TEXT.__swift_as_entry: 0xa8
-  __TEXT.__swift_as_cont: 0x154
+  __TEXT.__swift_as_cont: 0x16c
   __TEXT.__swift5_capture: 0x40c
   __TEXT.__swift_as_ret: 0xcc
   __TEXT.__swift5_assocty: 0xd0
-  __TEXT.__unwind_info: 0x15e0
-  __TEXT.__eh_frame: 0x1fe8
-  __DATA_CONST.__const: 0x23e8
-  __DATA_CONST.__cfstring: 0x4c0
+  __TEXT.__unwind_info: 0x1628
+  __TEXT.__eh_frame: 0x1f68
+  __DATA_CONST.__const: 0x2468
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x538
   __DATA.__objc_const: 0x3a78
-  __DATA.__objc_selrefs: 0x1590
+  __DATA.__objc_selrefs: 0x15c0
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0xc98
   __DATA.__data: 0x1cf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1398
+  Functions: 1408
   Symbols:   854
-  CStrings:  1484
+  CStrings:  1489
 
Symbols:
+ _$s10NewsDaemon29ProxyScoringServiceConnectionC13InterestTokenC10invalidateyyF
+ _$s10NewsDaemon29ProxyScoringServiceConnectionC13interestTokenAC08InterestH0CyF
- _$s10NewsDaemon29ProxyScoringServiceConnectionC11popInterestyyF
- _$s10NewsDaemon29ProxyScoringServiceConnectionC12pushInterestyyF
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
