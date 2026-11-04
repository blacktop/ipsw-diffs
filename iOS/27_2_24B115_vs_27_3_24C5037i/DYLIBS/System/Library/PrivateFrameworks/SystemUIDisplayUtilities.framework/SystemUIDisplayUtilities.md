## SystemUIDisplayUtilities

> `/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`

```diff

-104.100.0.0.0
-  __TEXT.__text: 0xb1a8
-  __TEXT.__objc_methlist: 0x818
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x71b
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0xc4b
+105.2.1.0.0
+  __TEXT.__text: 0xbea0
+  __TEXT.__objc_methlist: 0x928
+  __TEXT.__const: 0x258
+  __TEXT.__cstring: 0x81b
+  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__oslogstring: 0xdbb
   __TEXT.__constg_swiftt: 0x110
   __TEXT.__swift5_typeref: 0xa8
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__eh_frame: 0x1b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x328
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e8
+  __DATA_CONST.__objc_selrefs: 0x758
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x1158
-  __AUTH_CONST.__auth_got: 0x4c8
-  __AUTH.__objc_data: 0x3d8
+  __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__objc_const: 0x13e0
+  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH.__objc_data: 0x428
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x408
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 308
-  Symbols:   591
-  CStrings:  80
+  Functions: 334
+  Symbols:   633
+  CStrings:  90
 
Symbols:
+ +[SDUDisplayRegionBlankingRequest signpostIdentifierForUniqueIdentifier:]
+ -[SDUDisplayRegionBlankingController acquireDisplayRegionBlankingAssertionForRequest:]
+ -[SDUDisplayRegionBlankingCoordinator blankingRequestDenied:]
+ -[SDUDisplayRegionBlankingCoordinator blankingRequestInvalidated:]
+ -[SDUDisplayRegionBlankingCoordinator blankingRequestReceived:initiatesStateChange:]
+ -[SDUDisplayRegionBlankingRequest .cxx_destruct]
+ -[SDUDisplayRegionBlankingRequest bundleIDs]
+ -[SDUDisplayRegionBlankingRequest clientRequestTime]
+ -[SDUDisplayRegionBlankingRequest description]
+ -[SDUDisplayRegionBlankingRequest initWithUniqueIdentifier:regionIdentifier:reason:bundleIDs:clientRequestTime:serverReceiveTime:inProcess:firstRequestOnConnection:]
+ -[SDUDisplayRegionBlankingRequest isFirstRequestOnConnection]
+ -[SDUDisplayRegionBlankingRequest isInProcess]
+ -[SDUDisplayRegionBlankingRequest reason]
+ -[SDUDisplayRegionBlankingRequest regionIdentifier]
+ -[SDUDisplayRegionBlankingRequest serverReceiveTime]
+ -[SDUDisplayRegionBlankingRequest signpostIdentifier]
+ -[SDUDisplayRegionBlankingRequest uniqueIdentifier]
+ -[SDUDisplayRegionBlankingServiceServer acquireDisplayRegionBlankingAssertionWithUniqueIdentifier:forDisplayRegion:reason:restrictingToBundleIDs:requestTime:]
+ GCC_except_table12
+ _OBJC_CLASS_$_SDUDisplayRegionBlankingRequest
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._bundleIDs
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._clientRequestTime
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._firstRequestOnConnection
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._inProcess
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._reason
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._regionIdentifier
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._serverReceiveTime
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._signpostIdentifier
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingRequest._uniqueIdentifier
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingServiceServer._connectionsThatHaveRequestedAssertions
+ _OBJC_METACLASS_$_SDUDisplayRegionBlankingRequest
+ __OBJC_$_CLASS_METHODS_SDUDisplayRegionBlankingRequest
+ __OBJC_$_INSTANCE_METHODS_SDUDisplayRegionBlankingRequest
+ __OBJC_$_INSTANCE_VARIABLES_SDUDisplayRegionBlankingRequest
+ __OBJC_$_PROP_LIST_SDUDisplayRegionBlankingRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SDUDisplayRegionBlankingControllerDelegate
+ __OBJC_CLASS_RO_$_SDUDisplayRegionBlankingRequest
+ __OBJC_METACLASS_RO_$_SDUDisplayRegionBlankingRequest
+ ___86-[SDUDisplayRegionBlankingController acquireDisplayRegionBlankingAssertionForRequest:]_block_invoke
+ ___86-[SDUDisplayRegionBlankingController acquireDisplayRegionBlankingAssertionForRequest:]_block_invoke_2
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e27_v16?0"BSSimpleAssertion"8lw56l8s32l8s40l8s48l8
+ __os_signpost_emit_with_name_impl
+ _mach_continuous_time
+ _os_signpost_enabled
- -[SDUDisplayRegionBlankingServiceServer acquireDisplayRegionBlankingAssertionWithUniqueIdentifier:forDisplayRegion:reason:restrictingToBundleIDs:]
- ___108-[SDUDisplayRegionBlankingController acquireDisplayRegionBlankingAssertionForReason:restrictingToBundleIDs:]_block_invoke
- _objc_retain_x28
CStrings:
+ "<%@: %p; uniqueIdentifier: %@; region: %@; reason: %@; bundleIDs: (%@); clientRequestTime: %llu; serverReceiveTime: %llu; inProcess: %d; firstRequestOnConnection: %d>"
+ "BlankingAssertionGranted"
+ "BlankingAssertionRequestReceived"
+ "BlankingAssertionRequested"
+ "SDUDisplayRegionBlankingRequest.m"
+ "region: %{public, name=region}@ reason: %{public, name=reason}@"
+ "region: %{public, name=region}@ reason: %{public, name=reason}@ assertions: %{public, name=assertion_count}lu"
+ "region: %{public, name=region}@ reason: %{public, name=reason}@ first: %{public, name=first_request_on_connection}d"
+ "request != ((void*)0)"
+ "uniqueIdentifier != ((void*)0)"
```
