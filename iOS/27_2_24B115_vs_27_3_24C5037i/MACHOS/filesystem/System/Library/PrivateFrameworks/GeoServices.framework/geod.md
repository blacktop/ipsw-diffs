## geod

> `/System/Library/PrivateFrameworks/GeoServices.framework/geod`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-2076.31.9.18.8
-  __TEXT.__text: 0x4fc74
+2076.32.9.18.5
+  __TEXT.__text: 0x513f0
   __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_stubs: 0xa000
-  __TEXT.__objc_methlist: 0x2f50
+  __TEXT.__objc_stubs: 0xa0c0
+  __TEXT.__objc_methlist: 0x3048
   __TEXT.__const: 0x2b9
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__cstring: 0x6077
-  __TEXT.__oslogstring: 0x3445
+  __TEXT.__cstring: 0x6195
+  __TEXT.__oslogstring: 0x367f
   __TEXT.__swift5_typeref: 0x62
-  __TEXT.__objc_methname: 0x9ee3
-  __TEXT.__objc_classname: 0xa34
-  __TEXT.__objc_methtype: 0x1b60
+  __TEXT.__objc_methname: 0xa056
+  __TEXT.__objc_classname: 0xabe
+  __TEXT.__objc_methtype: 0x1bd7
   __TEXT.__constg_swiftt: 0x2c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x11f8
-  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__gcc_except_tab: 0x1274
+  __TEXT.__unwind_info: 0x1750
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x2810
-  __DATA_CONST.__cfstring: 0x3d40
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x2898
+  __DATA_CONST.__cfstring: 0x3e40
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_intobj: 0x138
-  __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__objc_arrayobj: 0x570
+  __DATA_CONST.__objc_arraydata: 0x2a0
+  __DATA_CONST.__objc_arrayobj: 0x5a0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x940
-  __DATA_CONST.__got: 0xd30
+  __DATA_CONST.__got: 0xd58
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x4e10
-  __DATA.__objc_selrefs: 0x2bb0
-  __DATA.__objc_ivar: 0x248
-  __DATA.__objc_data: 0x1600
+  __DATA.__objc_const: 0x5140
+  __DATA.__objc_selrefs: 0x2bf0
+  __DATA.__objc_ivar: 0x260
+  __DATA.__objc_data: 0x1740
   __DATA.__data: 0x9d8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1331
-  Symbols:   708
-  CStrings:  2907
+  Functions: 1360
+  Symbols:   713
+  CStrings:  2951
 
Symbols:
+ _OBJC_CLASS_$_GEODynamicDailyCountsCancelRequest
+ _OBJC_CLASS_$_GEODynamicDailyCountsFetchReply
+ _OBJC_CLASS_$_GEODynamicDailyCountsFetchRequest
+ _OBJC_CLASS_$_GEODynamicDailyCountsResponse
+ _OBJC_CLASS_$_NSValue
CStrings:
+ "@\"GEODynamicDailyCountsRequest\""
+ "@\"GEODynamicDailyCountsServiceRequester\""
+ "@\"NSError\"32@0:8q16@\"NSError\"24"
+ "@32@0:8q16@24"
+ "Applying deferred cancel for fetch %{public}@"
+ "Cancelling fetch %{public}@"
+ "Deferring cancel for fetch %{public}@ until it starts"
+ "DynamicDailyCounts"
+ "Fetch %{public}@ failed: %{public}@"
+ "Fetch %{public}@ finished with %lu metrics"
+ "GEODynamicDailyCountsRequestConfig"
+ "GEODynamicDailyCountsServer"
+ "GEODynamicDailyCountsServiceRequester"
+ "GEOErrorWithCode:reason:underlyingError:"
+ "GEOProtobufSession"
+ "HTTP %ld"
+ "Ignoring cancel for unknown fetch %{public}@; it may have already finished"
+ "Received HTTP %ld; failing request with GEOError %ld"
+ "Received HTTP %ld; request failed after the response: %{public}@"
+ "Received HTTP %ld; request succeeded"
+ "Rejecting fetch %{public}@: duplicate request UUID"
+ "Rejecting fetch %{public}@: missing request"
+ "Rejecting fetch: missing request UUID"
+ "T@\"GEODynamicDailyCountsServiceRequester\",R,N,V_requester"
+ "_GEODynamicDailyCountsPendingRequest"
+ "_cancelRequested"
+ "_pendingRequests"
+ "_pendingRequestsIsolater"
+ "_started"
+ "cancelCountsWithRequest:"
+ "com.apple.GeoServices.DynamicDailyCounts.pendingRequests"
+ "duplicate request UUID"
+ "dynamicdailycounts"
+ "errorForHTTPStatusCode:underlyingError:"
+ "failed to decode response"
+ "fetchCountsWithRequest:"
+ "metrics"
+ "missing request"
+ "missing request UUID"
+ "no response and no error"
+ "performRequest:traits:auditToken:completionQueue:completion:"
+ "requester"
+ "v24@?0@\"GEODynamicDailyCountsResponse\"8@\"NSError\"16"
+ "valueWithNonretainedObject:"
```
