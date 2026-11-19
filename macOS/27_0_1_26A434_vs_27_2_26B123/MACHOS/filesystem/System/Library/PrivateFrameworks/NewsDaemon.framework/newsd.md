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
- `__TEXT.__info_plist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`

```diff

-5934.0.2.0.0
-  __TEXT.__text: 0x47f68
+5971.0.0.0.0
+  __TEXT.__text: 0x48498
   __TEXT.__auth_stubs: 0x1ca0
-  __TEXT.__objc_stubs: 0x4200
-  __TEXT.__objc_methlist: 0x19a0
+  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_methlist: 0x19e0
   __TEXT.__const: 0x1c90
-  __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0x2c81
-  __TEXT.__objc_methname: 0x5da5
-  __TEXT.__oslogstring: 0x205d
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__cstring: 0x2b91
+  __TEXT.__objc_methname: 0x5e45
+  __TEXT.__oslogstring: 0x211d
   __TEXT.__objc_classname: 0x8dc
-  __TEXT.__objc_methtype: 0x1b37
+  __TEXT.__objc_methtype: 0x1b47
   __TEXT.__swift5_typeref: 0xc89
   __TEXT.__swift5_fieldmd: 0x814
   __TEXT.__constg_swiftt: 0x760

   __TEXT.__swift5_proto: 0x110
   __TEXT.__swift5_types: 0x9c
   __TEXT.__swift_as_entry: 0xa8
-  __TEXT.__swift_as_cont: 0x154
+  __TEXT.__swift_as_cont: 0x16c
   __TEXT.__swift5_capture: 0x40c
   __TEXT.__swift_as_ret: 0xcc
   __TEXT.__swift5_assocty: 0xd0
   __TEXT.__info_plist: 0x586
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

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0xe60
-  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__got: 0x728
   __DATA_CONST.__auth_ptr: 0x538
-  __DATA.__objc_const: 0x3a78
-  __DATA.__objc_selrefs: 0x1590
+  __DATA.__objc_const: 0x3a90
+  __DATA.__objc_selrefs: 0x15c8
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0xc98
-  __DATA.__data: 0x1cf0
+  __DATA.__data: 0x1cd0
   __DATA.__bss: 0x20e0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1398
-  Symbols:   854
-  CStrings:  1484
+  Functions: 1407
+  Symbols:   853
+  CStrings:  1492
 
Symbols:
+ _$s10Foundation4DateV2geoiySbAC_ACtFZ
+ _$s10NewsDaemon29ProxyScoringServiceConnectionC13InterestTokenC10invalidateyyF
+ _$s10NewsDaemon29ProxyScoringServiceConnectionC13interestTokenAC08InterestH0CyF
+ _$s8NewsCore16FeedItemDatabaseC013feedIDsForTagG0ySaySSGAEKF
- _$s10Foundation4DateVSLAAMc
- _$s10NewsDaemon29ProxyScoringServiceConnectionC11popInterestyyF
- _$s10NewsDaemon29ProxyScoringServiceConnectionC12pushInterestyyF
- _$s8NewsCore16FeedItemDatabaseC20feedContextForTagIDsySDyS2S_So06FCFeedG0CtGSaySSGKF
- _$sSL2geoiySbx_xtFZTj
CStrings:
+ "@\"NSDictionary\"16@0:8"
+ "T@\"<NDDownloadConsumer>\",&,N,V_consumer"
+ "T@\"NSDictionary\",R,N"
+ "TB,N,GisInvalidated,V_invalidated"
+ "_invalidated"
+ "_sendPersistedArchivesToConsumerForRequest:"
+ "connectionDidInvalidate:"
+ "consumer proxy invalidated, draining %lu messages, connection=%{public}@"
+ "consumer proxy lost connection, will drain %lu messages, connection=%{public}@"
+ "dislikeDatesByArticleID"
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
