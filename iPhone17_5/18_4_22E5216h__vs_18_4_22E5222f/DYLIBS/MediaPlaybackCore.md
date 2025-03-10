## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-24515.25.9.201.0
-  __TEXT.__text: 0x36ff54
-  __TEXT.__auth_stubs: 0x4db0
-  __TEXT.__objc_methlist: 0x15b98
+24500.25.9.301.0
+  __TEXT.__text: 0x36e17c
+  __TEXT.__auth_stubs: 0x4dc0
+  __TEXT.__objc_methlist: 0x15bd0
   __TEXT.__dlopen_cstrs: 0x114
   __TEXT.__const: 0x12b68
-  __TEXT.__cstring: 0x2a32b
+  __TEXT.__cstring: 0x2a307
   __TEXT.__constg_swiftt: 0x665c
   __TEXT.__swift5_typeref: 0x47e0
   __TEXT.__swift5_builtin: 0x690

   __TEXT.__swift5_fieldmd: 0x4150
   __TEXT.__swift5_assocty: 0xdc0
   __TEXT.__swift5_capture: 0x30f4
-  __TEXT.__oslogstring: 0x30cd6
+  __TEXT.__oslogstring: 0x30c01
   __TEXT.__swift5_proto: 0x8dc
   __TEXT.__swift5_types: 0x488
   __TEXT.__swift_as_entry: 0x2cc
   __TEXT.__swift_as_ret: 0x36c
   __TEXT.__swift5_mpenum: 0xd8
   __TEXT.__swift5_protos: 0xe8
-  __TEXT.__gcc_except_tab: 0x5c50
+  __TEXT.__gcc_except_tab: 0x5c74
   __TEXT.__ustring: 0x36c
-  __TEXT.__unwind_info: 0xaf50
-  __TEXT.__eh_frame: 0x9a54
-  __TEXT.__objc_classname: 0x3a60
-  __TEXT.__objc_methname: 0x36ce6
-  __TEXT.__objc_methtype: 0x91bb
-  __TEXT.__objc_stubs: 0x256c0
+  __TEXT.__unwind_info: 0xaf58
+  __TEXT.__eh_frame: 0x9a74
+  __TEXT.__objc_classname: 0x3a63
+  __TEXT.__objc_methname: 0x36d27
+  __TEXT.__objc_methtype: 0x91db
+  __TEXT.__objc_stubs: 0x25700
   __DATA_CONST.__got: 0x2b60
-  __DATA_CONST.__const: 0x8bf0
+  __DATA_CONST.__const: 0x8be0
   __DATA_CONST.__objc_classlist: 0xc10
   __DATA_CONST.__objc_catlist: 0x288
   __DATA_CONST.__objc_protolist: 0x730
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbba0
+  __DATA_CONST.__objc_selrefs: 0xbbb0
   __DATA_CONST.__objc_protorefs: 0x330
   __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0x270
-  __AUTH_CONST.__auth_got: 0x26e8
-  __AUTH_CONST.__auth_ptr: 0xcd0
+  __AUTH_CONST.__auth_got: 0x26f0
+  __AUTH_CONST.__auth_ptr: 0xc70
   __AUTH_CONST.__const: 0xdfa0
-  __AUTH_CONST.__cfstring: 0x1b6c0
-  __AUTH_CONST.__objc_const: 0x2f640
+  __AUTH_CONST.__cfstring: 0x1b680
+  __AUTH_CONST.__objc_const: 0x2f668
   __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x2a40
   __AUTH.__data: 0x1580
-  __DATA.__objc_ivar: 0x1894
+  __DATA.__objc_ivar: 0x1898
   __DATA.__data: 0x6260
   __DATA.__bss: 0xc9d0
   __DATA.__common: 0x58

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 17377
-  Symbols:   12443
-  CStrings:  17635
+  Functions: 17373
+  Symbols:   12437
+  CStrings:  17637
 
Symbols:
+ _MPCPlaybackEngineEventPayloadKeyQueueSectionItemCount
- _MPCPlaybackEngineEventTypeQueueItemAdd
- _MPCPlaybackEngineEventTypeQueueItemRemove
- _MPCPlaybackEngineEventTypeQueueItemReorder
CStrings:
+ "\x04\x11"
+ "Q24@0:8@\"NSString\"16"
+ "Q24@0:8@16"
+ "_lastItemStartIncitingEvent"
+ "_loadedItemCount"
+ "events.identifier, events.type, events.monoAbsolute, events.monoContinuous, events.monoTimebaseNS, events.userNS, events.threadPriority, events.payload"
+ "itemCountInSection:"
+ "queue-section-item-count"
+ "|%{public}@ %{public}@ %2i %{public}@ ╲╭ itemCount: %ld"
- "DISTINCT events.identifier, events.type, events.monoAbsolute, events.monoContinuous, events.monoTimebaseNS, events.userNS, events.threadPriority, events.payload"
- "queue-item-add"
- "queue-item-remove"
- "queue-item-reorder"
- "|%{public}@ %{public}@ %2i %{public}@\U001000dc QUEUE ITEM ADD             %{public}@ %{public}@"
- "|%{public}@ %{public}@ %2i %{public}@\U001000de QUEUE ITEM REMOVE          %{public}@ %{public}@"
- "|%{public}@ %{public}@ %2i %{public}@\U0010010e QUEUE ITEM REORDER         %{public}@ %{public}@"

```
