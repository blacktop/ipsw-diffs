## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-24500.25.9.301.0
-  __TEXT.__text: 0x36e17c
+24510.25.10.303.0
+  __TEXT.__text: 0x36e6c0
   __TEXT.__auth_stubs: 0x4dc0
-  __TEXT.__objc_methlist: 0x15bd0
+  __TEXT.__objc_methlist: 0x15be0
   __TEXT.__dlopen_cstrs: 0x114
   __TEXT.__const: 0x12b68
   __TEXT.__cstring: 0x2a307

   __TEXT.__swift5_fieldmd: 0x4150
   __TEXT.__swift5_assocty: 0xdc0
   __TEXT.__swift5_capture: 0x30f4
-  __TEXT.__oslogstring: 0x30c01
+  __TEXT.__oslogstring: 0x30e64
   __TEXT.__swift5_proto: 0x8dc
   __TEXT.__swift5_types: 0x488
   __TEXT.__swift_as_entry: 0x2cc
   __TEXT.__swift_as_ret: 0x36c
   __TEXT.__swift5_mpenum: 0xd8
   __TEXT.__swift5_protos: 0xe8
-  __TEXT.__gcc_except_tab: 0x5c74
+  __TEXT.__gcc_except_tab: 0x5cd8
   __TEXT.__ustring: 0x36c
-  __TEXT.__unwind_info: 0xaf58
+  __TEXT.__unwind_info: 0xaf68
   __TEXT.__eh_frame: 0x9a74
   __TEXT.__objc_classname: 0x3a63
-  __TEXT.__objc_methname: 0x36d27
+  __TEXT.__objc_methname: 0x36d4f
   __TEXT.__objc_methtype: 0x91db
-  __TEXT.__objc_stubs: 0x25700
+  __TEXT.__objc_stubs: 0x25720
   __DATA_CONST.__got: 0x2b60
-  __DATA_CONST.__const: 0x8be0
+  __DATA_CONST.__const: 0x8c08
   __DATA_CONST.__objc_classlist: 0xc10
   __DATA_CONST.__objc_catlist: 0x288
   __DATA_CONST.__objc_protolist: 0x730
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbbb0
+  __DATA_CONST.__objc_selrefs: 0xbbb8
   __DATA_CONST.__objc_protorefs: 0x330
   __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0x270
   __AUTH_CONST.__auth_got: 0x26f0
-  __AUTH_CONST.__auth_ptr: 0xc70
+  __AUTH_CONST.__auth_ptr: 0xc10
   __AUTH_CONST.__const: 0xdfa0
   __AUTH_CONST.__cfstring: 0x1b680
   __AUTH_CONST.__objc_const: 0x2f668

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 17373
-  Symbols:   12437
-  CStrings:  17637
+  Functions: 17375
+  Symbols:   12439
+  CStrings:  17643
 
CStrings:
+ "[AOT:%{public}@:%{public}@] _evaluateAutoPlayStateAfterItemsChanged | autoplay disabled [finished waitingForItems]"
+ "[AOT:%{public}@:%{public}@] _evaluateAutoPlayStateAfterItemsChanged | autoplay unsupported [no queue references]"
+ "[AOT:%{public}@:%{public}@] _evaluateAutoPlayStateAfterItemsChanged | autoplay waiting for trigger [finished waitingForItems]"
+ "[AOT:%{public}@:%{public}@] _evaluateAutoPlayStateAfterItemsChanged | autoplay waiting for trigger [new supported content]"
+ "[AOT:%{public}@:%{public}@] loadAdditionalUpcomingItems:completion: | evaluating autoPlayIsTriggered [no other datasources triggered load] triggered=YES"
+ "[BMUS:%{public}@:%{public}@] enumerator nextObject: | returning nil [encountered loading section in non-playback mode] sectionID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] enumerator nextObject: | returning placeholder [dataSource loading, playback mode] sectionID=%{public}@ nextContentItemID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] sectionedIdentifierList:dataSourceDidMoveItems:inSection: | ignoring SIL change [state: Loading]"
+ "[BMUS:%{public}@:%{public}@] sectionedIdentifierList:dataSourceDidRemoveItems:inSection: | ignoring SIL change [state: Loading]"
+ "[ECATS:%{public}@:%{public}@] loadAdditionalUpcomingItems:completion: | evaluating auto play [no other datasources triggered load] autoPlayState=%{public}@"
+ "_evaluateAutoPlayStateAfterItemsChanged"
- "[AOT:%{public}@:%{public}@] sectionedIdentifierList:dataSourceDidAddItems:toSection: | autoplay disabled [finished waitingForItems]"
- "[AOT:%{public}@:%{public}@] sectionedIdentifierList:dataSourceDidAddItems:toSection: | autoplay unsupported [no queue references]"
- "[AOT:%{public}@:%{public}@] sectionedIdentifierList:dataSourceDidAddItems:toSection: | autoplay waiting for trigger [finished waitingForItems]"
- "[AOT:%{public}@:%{public}@] sectionedIdentifierList:dataSourceDidAddItems:toSection: | autoplay waiting for trigger [new supported content]"
- "[ECATS:%{public}@:%{public}@] loadAdditionalUpcomingItems:completion: | evaluating autoPlayIsTriggered [loadAdditionalUpcomingItems called while WaitingForTriggerToEnable] triggered=YES"

```
