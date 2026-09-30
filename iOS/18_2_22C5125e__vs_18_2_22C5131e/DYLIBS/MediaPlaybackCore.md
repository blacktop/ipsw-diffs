## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-24300.24.43.201.0
-  __TEXT.__text: 0x31e71c
-  __TEXT.__auth_stubs: 0x4f90
-  __TEXT.__objc_methlist: 0x11f00
-  __TEXT.__cstring: 0x2833d
+24300.24.44.301.0
+  __TEXT.__text: 0x31dd30
+  __TEXT.__auth_stubs: 0x4f30
+  __TEXT.__objc_methlist: 0x11ef8
+  __TEXT.__cstring: 0x282b4
   __TEXT.__const: 0xa2d0
   __TEXT.__constg_swiftt: 0x5ad8
   __TEXT.__swift5_typeref: 0x3ec3

   __TEXT.__swift5_types: 0x3e8
   __TEXT.__swift5_mpenum: 0xc4
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__oslogstring: 0x2da8e
+  __TEXT.__oslogstring: 0x2ddda
   __TEXT.__swift5_capture: 0x2cac
-  __TEXT.__gcc_except_tab: 0x5ee4
+  __TEXT.__gcc_except_tab: 0x5e1c
   __TEXT.__ustring: 0x354
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__unwind_info: 0xa080
-  __TEXT.__eh_frame: 0x74b8
-  __TEXT.__objc_classname: 0x39e7
-  __TEXT.__objc_methname: 0x36170
+  __TEXT.__unwind_info: 0xa050
+  __TEXT.__eh_frame: 0x7480
+  __TEXT.__objc_classname: 0x39ea
+  __TEXT.__objc_methname: 0x36157
   __TEXT.__objc_methtype: 0x8fc5
-  __TEXT.__objc_stubs: 0x25180
-  __DATA_CONST.__got: 0x2c88
-  __DATA_CONST.__const: 0x8e30
+  __TEXT.__objc_stubs: 0x25100
+  __DATA_CONST.__got: 0x2c80
+  __DATA_CONST.__const: 0x8db8
   __DATA_CONST.__objc_classlist: 0xbe8
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x750
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb568
+  __DATA_CONST.__objc_selrefs: 0xb550
   __DATA_CONST.__objc_protorefs: 0x350
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x238
-  __AUTH_CONST.__auth_got: 0x27d8
-  __AUTH_CONST.__auth_ptr: 0xa38
-  __AUTH_CONST.__const: 0xc7f0
-  __AUTH_CONST.__cfstring: 0x1af60
-  __AUTH_CONST.__objc_const: 0x33c08
+  __AUTH_CONST.__auth_got: 0x27a8
+  __AUTH_CONST.__auth_ptr: 0xa40
+  __AUTH_CONST.__const: 0xc7d0
+  __AUTH_CONST.__cfstring: 0x1af20
+  __AUTH_CONST.__objc_const: 0x33c58
   __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x40d8
   __AUTH.__data: 0x16f8
-  __DATA.__objc_ivar: 0x189c
-  __DATA.__data: 0x5d48
-  __DATA.__bss: 0xa928
+  __DATA.__objc_ivar: 0x18a0
+  __DATA.__data: 0x5d38
+  __DATA.__bss: 0xa918
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x4cf0
   __DATA_DIRTY.__data: 0x4f78
-  __DATA_DIRTY.__bss: 0x2ab0
+  __DATA_DIRTY.__bss: 0x2ac0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15952
-  Symbols:   11545
-  CStrings:  17091
+  Functions: 15940
+  Symbols:   11526
+  CStrings:  17094
 
Symbols:
- _dispatch_activate
- _dispatch_queue_attr_make_initially_inactive
- _dispatch_set_target_queue
- _os_unfair_lock_trylock
CStrings:
+ "!\x16\x11"
+ "1\""
+ "B24@?0@\"MPCPlaybackEngineEvent\"8@\"<MPCPlaybackEngineEventStreamCursor>\"16"
+ "PlaybackEventStream_Oversize"
+ "Td,N,V_transactionDebounceTime"
+ "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] _onQueue_flush | running query [] lastEventSuccessTimestamp=%!l(MISSING)lu"
+ "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] _onQueue_flush | unusual delay between events [more than 5m between events] delta=%!l(MISSING)luns"
+ "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] _onQueue_flush | updating bookmark [successful delivery] lastEventSuccessTimestamp=%!l(MISSING)lu"
+ "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] flushEventsWithCompletion:… | flushed events"
+ "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] flushEventsWithCompletion:… | flushing events async"
+ "[EVS:%!{(MISSING)public}@] countOfPreviousEventsWithTypes:… | returning 0 [invalidated]"
+ "[EVS:%!{(MISSING)public}@] emitEventType:%!{(MISSING)public}@ payload:… atTime:%!{(MISSING)time_t}zd | emitting event [] continuousTime=%!l(MISSING)dns event.id=%!{(MISSING)public}@"
+ "[EVS:%!{(MISSING)public}@] emitEventType:%!{(MISSING)public}@ payload:… atTime:%!{(MISSING)time_t}zd | emitting payload [] event.id=%!{(MISSING)public}@ payload=%!{(MISSING)public}@"
+ "[EVS:%!{(MISSING)public}@] enumeratePreviousEventsWithType:… | skipping enumeration [invalidated]"
+ "[EVS:%!{(MISSING)public}@] findPreviousEventsWithTypes:… | return nil [invalidated]"
+ "[EVS:%!{(MISSING)public}@] invalidate | removing database [invalidation] url=%!{(MISSING)public}@"
+ "[EVS:%!{(MISSING)public}@] invalidate | removing database [invalidation] url=%!{(MISSING)public}@ error=%!{(MISSING)public}@"
+ "_onQueue_flush"
+ "_statementForColumnsExpression:eventTypes:payload:limit:"
+ "_transactionDebounceTime"
+ "flushEventsWithCompletion:"
+ "flushEventsWithConsumer:fromTimestamp:untilTimestamp:"
+ "mus"
+ "oth"
+ "pod"
+ "rps"
+ "setTransactionDebounceTime:"
+ "transactionDebounceTime"
+ "updateCurrentAudioRouteWithPickedRouteIfNeeded:"
+ "v32@0:8@\"NSString\"16@?<B@?@\"MPCPlaybackEngineEvent\"@\"<MPCPlaybackEngineEventStreamCursor>\">24"
+ "v40@0:8@\"NSString\"16Q24@?<B@?@\"MPCPlaybackEngineEvent\"@\"<MPCPlaybackEngineEventStreamCursor>\">32"
+ "void _MPCPlaybackEngineEventStreamValidateSystemTime(MPCPlaybackEngineEventType  _Nonnull __strong, uint64_t)"
+ "\xc1"
- "%!@(MISSING)#%!@(MISSING)"
- "'\x11"
- "1#"
- "@16@?0@\"<MSVSQLExecutable>\"8"
- "No more tracks"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] _onQueue_flush | failed query [] error=%!{(MISSING)public}@"
- "[EVS:%!{(MISSING)public}@:%!{(MISSING)public}@:%!p(MISSING)] _onQueue_flush | running query [] lastEventTimestamp=%!l(MISSING)lu"
- "[EVS:%!{(MISSING)public}@] invalidate | removed database [invalidation] url=%!{(MISSING)public}@"
- "[EVS:%!{(MISSING)public}@] invalidate | removed database [invalidation] url=%!{(MISSING)public}@ error=%!{(MISSING)public}@"
- "_MPCPlaybackEngineEventStreamCursor.m"
- "_MPCPlaybackEngineEventStreamSubscription.m"
- "_invalidateAssertion:"
- "_performDatabaseOperation:"
- "_statementForColumnsExpression:eventTypes:payload:limit:database:"
- "cachedEventWithTypes:matchingPayload:cursor:"
- "com.apple.MediaPlaybackCore/EVSSubscription"
- "flushWithCompletion:"
- "m"
- "o"
- "p"
- "processIDPrefix"
- "reportCacheMiss:"
- "setEpisodeNumber:"
- "setSeasonNumber:"
- "updateCurrentAudioRouteWithPickedRoutes:"
- "v24@?0@\"MPCPlaybackEngineEvent\"8@\"<MPCPlaybackEngineEventStreamCursor>\"16"
- "v32@0:8@\"NSString\"16@?<v@?@\"MPCPlaybackEngineEvent\"@\"<MPCPlaybackEngineEventStreamCursor>\">24"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"MPCPlaybackEngineEvent\"@\"<MPCPlaybackEngineEventStreamCursor>\">32"
- "void _MPCPlaybackEngineEventStreamValidateSystemTime(__strong MPCPlaybackEngineEventType _Nonnull, uint64_t)"

```
