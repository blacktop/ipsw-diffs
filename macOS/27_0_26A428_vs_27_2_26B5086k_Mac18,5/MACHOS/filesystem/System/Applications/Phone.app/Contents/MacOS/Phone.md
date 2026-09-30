## Phone

> `/System/Applications/Phone.app/Contents/MacOS/Phone`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3072.100.1.1.3
-  __TEXT.__text: 0x1ea00
-  __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_stubs: 0x2de0
-  __TEXT.__objc_methlist: 0x1274
-  __TEXT.__const: 0x914
+3077.200.51.1.1
+  __TEXT.__text: 0x1f128
+  __TEXT.__auth_stubs: 0x1630
+  __TEXT.__objc_stubs: 0x2e80
+  __TEXT.__objc_methlist: 0x12a4
+  __TEXT.__const: 0x924
   __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__objc_methname: 0x5365
-  __TEXT.__cstring: 0x65c
-  __TEXT.__oslogstring: 0xcb5
+  __TEXT.__objc_methname: 0x5435
+  __TEXT.__cstring: 0x67c
+  __TEXT.__oslogstring: 0xdc5
   __TEXT.__objc_classname: 0x2f7
   __TEXT.__objc_methtype: 0x17dd
   __TEXT.__constg_swiftt: 0x348

   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xa08
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__eh_frame: 0x760
-  __DATA_CONST.__const: 0xb68
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__const: 0xbb8
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0xb20
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__auth_ptr: 0x2e8
-  __DATA.__objc_const: 0x1720
-  __DATA.__objc_selrefs: 0x12c0
-  __DATA.__objc_ivar: 0x80
+  __DATA_CONST.__auth_got: 0xb28
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__auth_ptr: 0x2f0
+  __DATA.__objc_const: 0x1780
+  __DATA.__objc_selrefs: 0x12e8
+  __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x4c8
   __DATA.__data: 0xb58
   __DATA.__common: 0x70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 626
-  Symbols:   616
-  CStrings:  1038
+  Functions: 635
+  Symbols:   619
+  CStrings:  1052
 
Symbols:
+ _$s10CallsAppUI21RecentsDetailProviderP9fileRadar3for4fromySo12CHRecentCallC_So16UIViewControllerCtFTq
+ _$s15ConversationKit15TTRCallReporterO25presentRecentsRadarPicker3for4fromySo12CHRecentCallC_So16UIViewControllerCtFZ
+ _OBJC_CLASS_$_NSUUID
CStrings:
+ "@\"NSUUID\""
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_contactsFetchQueue"
+ "T@\"NSUUID\",&,N,V_contactsUpdateGeneration"
+ "UUID"
+ "[handleUpdatedContacts] Discarding stale contact fetch (generation %@, current %@)"
+ "[handleUpdatedContacts] Fetching contacts for %lu handles using contact store %@"
+ "[handleUpdatedContacts] Found %lu contacts for contact handle %{sensitive}@; caching the first contact %{sensitive}@"
+ "_contactsFetchQueue"
+ "_contactsUpdateGeneration"
+ "com.apple.calls.queue.%@.contactsFetch.%p"
+ "contactsFetchQueue"
+ "contactsUpdateGeneration"
+ "recentCallsWithCompletion:"
+ "setContactsUpdateGeneration:"
```
