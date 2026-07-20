## ShazamKit

> `/System/Library/Frameworks/ShazamKit.framework/Versions/A/ShazamKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-427.0.40.0.0
-  __TEXT.__text: 0xa4a80
-  __TEXT.__objc_methlist: 0x50e8
+427.0.44.0.0
+  __TEXT.__text: 0xa4bf4
+  __TEXT.__objc_methlist: 0x5160
   __TEXT.__const: 0x222b7
-  __TEXT.__cstring: 0x3a8b
-  __TEXT.__gcc_except_tab: 0x38d8
-  __TEXT.__oslogstring: 0x1441
+  __TEXT.__cstring: 0x3a9b
+  __TEXT.__gcc_except_tab: 0x38b8
+  __TEXT.__oslogstring: 0x1431
   __TEXT.__constg_swiftt: 0x7bc
   __TEXT.__swift5_typeref: 0xfd4
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x480
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x2508
+  __DATA_CONST.__objc_selrefs: 0x2518
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x250
-  __DATA_CONST.__got: 0x860
+  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__got: 0x868
   __AUTH_CONST.__const: 0x26d0
   __AUTH_CONST.__cfstring: 0x27a0
-  __AUTH_CONST.__objc_const: 0x9dd8
+  __AUTH_CONST.__objc_const: 0x9f08
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__auth_got: 0x1198
+  __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x298
-  __DATA.__objc_ivar: 0x4dc
+  __DATA.__objc_ivar: 0x4e4
   __DATA.__data: 0x1b2458
   __DATA.__bss: 0x1e18
   __DATA.__common: 0x168

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3660
-  Symbols:   6172
+  Functions: 3667
+  Symbols:   6191
   CStrings:  575
 
Symbols:
+ +[SHMediaItem isAddedToLibraryForIdentifier:]
+ +[SHMediaItemDaemonConnection fetchMediaItemForIdentifier:]
+ +[SHMediaItemDaemonConnection fetchMediaItemForIdentifier:completionHandler:]
+ +[SHPreRecordingRequest supportsSecureCoding]
+ -[SHPreRecordingRequest .cxx_destruct]
+ -[SHPreRecordingRequest encodeWithCoder:]
+ -[SHPreRecordingRequest initWithCoder:]
+ -[SHPreRecordingRequest initWithRequestID:preferredInputAudioRoute:]
+ -[SHPreRecordingRequest preferredInputAudioRoute]
+ -[SHPreRecordingRequest requestID]
+ -[SHShazamKitServiceConnection mediaItemForIdentifier:completionHandler:]
+ -[SHShazamKitServiceConnection prepareMatcherForRequest:completionHandler:]
+ -[SHShazamKitServiceConnection synchronouslyFetchMediaItemForIdentifier:completionHandler:]
+ OBJC_IVAR_$_SHPreRecordingRequest._preferredInputAudioRoute
+ OBJC_IVAR_$_SHPreRecordingRequest._requestID
+ _OBJC_CLASS_$_SHPreRecordingRequest
+ _OBJC_METACLASS_$_SHPreRecordingRequest
+ __OBJC_$_CLASS_METHODS_SHPreRecordingRequest
+ __OBJC_$_CLASS_PROP_LIST_SHPreRecordingRequest
+ __OBJC_$_INSTANCE_METHODS_SHPreRecordingRequest
+ __OBJC_$_INSTANCE_VARIABLES_SHPreRecordingRequest
+ __OBJC_$_PROP_LIST_SHPreRecordingRequest
+ __OBJC_CLASS_PROTOCOLS_$_SHPreRecordingRequest
+ __OBJC_CLASS_RO_$_SHPreRecordingRequest
+ __OBJC_METACLASS_RO_$_SHPreRecordingRequest
+ ___59+[SHMediaItemDaemonConnection fetchMediaItemForIdentifier:]_block_invoke
+ ___73-[SHShazamKitServiceConnection mediaItemForIdentifier:completionHandler:]_block_invoke
+ ___75-[SHShazamKitServiceConnection prepareMatcherForRequest:completionHandler:]_block_invoke
+ ___91-[SHShazamKitServiceConnection synchronouslyFetchMediaItemForIdentifier:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e33_v24?0"SHMediaItem"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e33_v24?0"SHMediaItem"8"NSError"16l
+ _objc_msgSend$fetchMediaItemForIdentifier:
+ _objc_msgSend$fetchMediaItemForIdentifier:completionHandler:
+ _objc_msgSend$initWithRequestID:preferredInputAudioRoute:
+ _objc_msgSend$mediaItemForIdentifier:completionHandler:
+ _objc_msgSend$prepareMatcherForRequest:completionHandler:
+ _objc_msgSend$synchronouslyFetchMediaItemForIdentifier:completionHandler:
- +[SHMediaItemDaemonConnection fetchRawSongResponseDataUsingMediaItemIdentifier:]
- +[SHMediaItemDaemonConnection fetchRawSongResponseDataUsingMediaItemIdentifier:completionHandler:]
- -[SHShazamKitServiceConnection fetchRawSongResponseDataForMediaItemIdentifier:completionHandler:]
- -[SHShazamKitServiceConnection prepareMatcherForRequestID:completionHandler:]
- -[SHShazamKitServiceConnection synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:]
- GCC_except_table40
- ___110-[SHShazamKitServiceConnection synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:]_block_invoke
- ___77-[SHShazamKitServiceConnection prepareMatcherForRequestID:completionHandler:]_block_invoke
- ___80+[SHMediaItemDaemonConnection fetchRawSongResponseDataUsingMediaItemIdentifier:]_block_invoke
- ___97-[SHShazamKitServiceConnection fetchRawSongResponseDataForMediaItemIdentifier:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32r_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_48_e8_32bs40w_e28_v24?0"NSData"8"NSError"16l
- ___copy_helper_block_e8_32b40w
- _objc_msgSend$fetchRawSongResponseDataForMediaItemIdentifier:completionHandler:
- _objc_msgSend$fetchRawSongResponseDataUsingMediaItemIdentifier:
- _objc_msgSend$fetchRawSongResponseDataUsingMediaItemIdentifier:completionHandler:
- _objc_msgSend$prepareMatcherForRequestID:completionHandler:
- _objc_msgSend$synchronouslyFetchRawSongResponseDataForMediaItemIdentifier:completionHandler:
CStrings:
+ "Error fetching media item: %@"
+ "[0-9]+x[0-9]+(?=[^/]*$)"
+ "v24@?0@\"SHMediaItem\"8@\"NSError\"16"
- "Error fetching raw response data: %@"
- "[0-9]+x[0-9]+"
- "v24@?0@\"NSData\"8@\"NSError\"16"
```
