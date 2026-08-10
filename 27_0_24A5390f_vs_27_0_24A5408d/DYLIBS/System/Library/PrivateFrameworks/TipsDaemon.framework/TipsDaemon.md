## TipsDaemon

> `/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-857.0.0.0.0
-  __TEXT.__text: 0xa0254
-  __TEXT.__objc_methlist: 0x3878
-  __TEXT.__const: 0x3238
-  __TEXT.__oslogstring: 0x21fb
-  __TEXT.__cstring: 0x428c
-  __TEXT.__gcc_except_tab: 0x1394
+866.0.0.0.0
+  __TEXT.__text: 0xa0730
+  __TEXT.__objc_methlist: 0x3898
+  __TEXT.__const: 0x3258
+  __TEXT.__oslogstring: 0x2474
+  __TEXT.__cstring: 0x427c
+  __TEXT.__gcc_except_tab: 0x1484
   __TEXT.__swift5_typeref: 0x1182
   __TEXT.__swift5_fieldmd: 0x988
   __TEXT.__constg_swiftt: 0xeac

   __TEXT.__swift_as_ret: 0x208
   __TEXT.__swift_as_cont: 0x430
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2d08
+  __TEXT.__unwind_info: 0x2d30
   __TEXT.__eh_frame: 0x4cd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e68
+  __DATA_CONST.__const: 0x1eb0
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2690
+  __DATA_CONST.__objc_selrefs: 0x2688
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0xd20
+  __DATA_CONST.__got: 0xd18
   __AUTH_CONST.__const: 0x2838
   __AUTH_CONST.__cfstring: 0x2a00
   __AUTH_CONST.__objc_const: 0x80f8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1220
+  __AUTH_CONST.__auth_got: 0x1230
   __AUTH.__objc_data: 0xf00
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x8b0
-  __DATA.__bss: 0x1d30
+  __DATA.__bss: 0x1d40
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3420
   __DATA_DIRTY.__data: 0x10c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3307
-  Symbols:   4524
-  CStrings:  798
+  Functions: 3315
+  Symbols:   4535
+  CStrings:  807
 
Symbols:
+ +[TPSRegulatoryImageManager _findELabelURLsWithType:completion:]
+ +[TPSRegulatoryImageManager fetchELabelURLsForCurrentDevice:]
+ +[TPSRegulatoryImageManager notifyMetaCompletionsWithDocumentsMap:deliveryInfo:contentMapHash:error:]
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table45
+ GCC_except_table53
+ GCC_except_table61
+ ___101+[TPSRegulatoryImageManager notifyMetaCompletionsWithDocumentsMap:deliveryInfo:contentMapHash:error:]_block_invoke
+ ___53+[TPSRegulatoryImageManager fetchMetaWithCompletion:]_block_invoke_3
+ ___64+[TPSRegulatoryImageManager _findELabelURLsWithType:completion:]_block_invoke
+ ___block_descriptor_40_e47_v44?08"NSData"16B24"NSString"28"NSError"36l
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ __isFetchingMeta
+ __pendingMetaCompletions
+ _objc_msgSend$_findELabelURLsWithType:completion:
+ _objc_msgSend$notifyMetaCompletionsWithDocumentsMap:deliveryInfo:contentMapHash:error:
- GCC_except_table40
- _OBJC_CLASS_$_TPSNotification
- _objc_msgSend$isMacUI
- _objc_msgSend$isPadUI
- _objc_msgSend$setText:
- _objc_msgSend$siriCollectionIdentifier
CStrings:
+ "Device match: model=%{public}@ family=%{public}@ targets=%{public}@"
+ "Welcome collection %@ missing notification content, fall back to software welcome."
+ "Welcome collection fallback %@ missing notification content."
+ "Welcome collection fallback not found %@"
+ "Welcome collection not found %@"
+ "airpods.pro.gen3"
+ "eLabel XPC: no eLabel returned for type %{public}@ (no cached documents)"
+ "eLabel XPC: no eLabel returned for type %{public}@ style %{public}ld (matched document has no fileURL)"
+ "eLabel XPC: no eLabel returned for type %{public}@ style %{public}ld (no matching document)"
+ "eLabel XPC: returned eLabel for type %{public}@ style %{public}ld at %{public}@"
- "711495D10BB643F6BDA3693886C0BCAF"
```
