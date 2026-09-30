## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`

```diff

-3034.100.1.0.0
-  __TEXT.__text: 0x1016a4
+3036.0.6.0.0
+  __TEXT.__text: 0x101f0c
   __TEXT.__auth_stubs: 0x30c0
-  __TEXT.__objc_methlist: 0x50cc
-  __TEXT.__cstring: 0x11930
+  __TEXT.__objc_methlist: 0x5174
+  __TEXT.__cstring: 0x119f4
   __TEXT.__swift5_typeref: 0x24bd
   __TEXT.__swift5_fieldmd: 0x13e8
-  __TEXT.__const: 0x3e00
+  __TEXT.__const: 0x3e10
   __TEXT.__constg_swiftt: 0x1f14
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_reflstr: 0x1386

   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_proto: 0x348
   __TEXT.__swift5_types: 0x19c
-  __TEXT.__oslogstring: 0xf672
+  __TEXT.__oslogstring: 0xf8a0
   __TEXT.__swift5_capture: 0x664
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__gcc_except_tab: 0x130c
+  __TEXT.__gcc_except_tab: 0x1384
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x4440
+  __TEXT.__unwind_info: 0x4480
   __TEXT.__eh_frame: 0x7264
   __TEXT.__objc_classname: 0xdbd
-  __TEXT.__objc_methname: 0x163fc
-  __TEXT.__objc_methtype: 0x49be
-  __TEXT.__objc_stubs: 0x10060
+  __TEXT.__objc_methname: 0x16666
+  __TEXT.__objc_methtype: 0x4a47
+  __TEXT.__objc_stubs: 0x10160
   __DATA_CONST.__got: 0x19e0
-  __DATA_CONST.__const: 0x28e0
+  __DATA_CONST.__const: 0x2980
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d78
+  __DATA_CONST.__objc_selrefs: 0x4dd8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x1870
-  __AUTH_CONST.__auth_ptr: 0xa20
+  __AUTH_CONST.__auth_ptr: 0xa18
   __AUTH_CONST.__const: 0x3878
   __AUTH_CONST.__cfstring: 0x44e0
-  __AUTH_CONST.__objc_const: 0xd180
+  __AUTH_CONST.__objc_const: 0xd280
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xf68
   __AUTH.__data: 0xc58
-  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_ivar: 0x4a8
   __DATA.__data: 0x3408
   __DATA.__bss: 0x4a58
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5700
-  Symbols:   4263
-  CStrings:  6257
+  Functions: 5719
+  Symbols:   4283
+  CStrings:  6292
 
Symbols:
+ _VCSpotlightBatchSize
CStrings:
+ "%!s(MISSING) ! no item generated for reference %!@(MISSING)"
+ "%!s(MISSING) + indexed searchable item for reference %!@(MISSING)"
+ "%!s(MISSING) > generating searchable item for reference %!@(MISSING)"
+ "%!s(MISSING) Eligibility changed handler already set for activity %!@(MISSING)"
+ "%!s(MISSING) Removing eligibility changed handler for activity: %!@(MISSING)"
+ "%!s(MISSING) We have delta update information, but the # of changed records larger than our batch size. Dropping down to regular indexing to stay within batch size (totalToIndex=%!l(MISSING)u, batchSize=%!l(MISSING)u)"
+ "%!s(MISSING) We seemed to have dropped some references. No errors, so continuing: check logs to see what references were dropped"
+ "-[WFXPCActivityScheduler addEligibilityChangedHandler:toActivity:]"
+ "-[WFXPCActivityScheduler removeEligibilityChangedHandlerIfNeeded]"
+ "@\"FBSDisplayLayout\""
+ "T@\"FBSDisplayLayout\",&,N,V_lastSeenLayout"
+ "T@\"FBSDisplayLayoutMonitor\",&,N,V_layoutMonitor"
+ "T@\"NSDictionary\",R,N,V_referencesToIndex"
+ "T@\"WFDebouncer\",&,N,V_debouncer"
+ "T@?,C,N,V_visibleApplicationFetchCompletionHandler"
+ "T^{_xpc_activity_eligibility_changed_handler_s=},N,V_lock_eligibilityChangedHandler"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "_fillIdentifiersToRemove:referencesToIndex:withMaximumUpdatedItems:references:localState:"
+ "_lastSeenLayout"
+ "_lock"
+ "_lock_eligibilityChangedHandler"
+ "_referencesToIndex"
+ "_visibleApplicationFetchCompletionHandler"
+ "addEligibilityChangedHandler:toActivity:"
+ "finishGettingVisibleApplications"
+ "getVisibleApplicationsWithCompletionHandler:"
+ "if_enumerateAsynchronously:completionHandler:"
+ "lastSeenLayout"
+ "lock_eligibilityChangedHandler"
+ "referencesToIndex"
+ "removeEligibilityChangedHandlerIfNeeded"
+ "setDebouncer:"
+ "setLastSeenLayout:"
+ "setLayoutMonitor:"
+ "setLock:"
+ "setLock_eligibilityChangedHandler:"
+ "setVisibleApplicationFetchCompletionHandler:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v32@0:8@?16@24"
+ "v32@?0@\"WFWorkflowReference\"8Q16@?<v@?@\"NSError\">24"
+ "v32@?0@\"WFWorkflowReference\"8Q16^B24"
+ "visibleApplicationFetchCompletionHandler"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "T@\"NSDictionary\",R,N,V_searchableItemRegistry"
- "T^{_xpc_activity_eligibility_changed_handler_s=},N,V_eligibilityChangedHandler"
- "_eligibilityChangedHandler"
- "_fillIdentifiersToRemove:searchableItemRegistry:withMaximumUpdatedItems:references:localState:"
- "_searchableItemRegistry"
- "currentDisplayLayout"
- "eligibilityChangedHandler"
- "searchableItemRegistry"
- "setEligibilityChangedHandler:"
- "v32@?0@\"NSString\"8Q16^B24"

```
