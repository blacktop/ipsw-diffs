## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_types`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-825.56.0.0.0
-  __TEXT.__text: 0x155a10
+825.57.0.0.0
+  __TEXT.__text: 0x155bac
   __TEXT.__objc_methlist: 0x10678
   __TEXT.__const: 0x3d8
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__cstring: 0x14deb
-  __TEXT.__oslogstring: 0x119f4
+  __TEXT.__oslogstring: 0x11aa0
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x154
   __TEXT.__swift5_reflstr: 0xb1
   __TEXT.__swift5_fieldmd: 0x88
   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x2614
-  __TEXT.__unwind_info: 0x2a30
+  __TEXT.__gcc_except_tab: 0x2754
+  __TEXT.__unwind_info: 0x2a38
   __TEXT.__eh_frame: 0x2d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 6051
   Symbols:   10787
-  CStrings:  4075
+  CStrings:  4077
 
Symbols:
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0ls48l8w56l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
Functions:
~ -[WAClient _replyAllWithTimeoutErrorAndRemove] : 696 -> 728
~ ___46-[WAClient _replyAllWithTimeoutErrorAndRemove]_block_invoke : 436 -> 400
~ ___46-[WAClient _replyAllWithTimeoutErrorAndRemove]_block_invoke_2 : 92 -> 80
~ ___85-[AnalyticsStoreFileWriter batchedWriteAnalyticsStoreToCSVFilesWithBatchSize:maxAge:]_block_invoke : 1680 -> 2108
CStrings:
+ "%{public}s::%d:CoreData exception %@ in batchedWriteAnalyticsStoreToCSVFilesWithBatchSize:maxAge:"
+ "%{public}s::%d:analyticsStoreFileWriterDirectory nil, skipping CSV export"
+ "WiFiAnalytics-825.57 Jul 10 2026 23:31:20"
- "WiFiAnalytics-825.56 Jul  1 2026 23:27:25"
```
