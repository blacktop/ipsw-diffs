## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-427.2.6.0.0
-  __TEXT.__text: 0x5ab9c
+427.3.1.0.0
+  __TEXT.__text: 0x5a94c
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_stubs: 0xd3c0
-  __TEXT.__objc_methlist: 0x62e4
+  __TEXT.__objc_stubs: 0xd3a0
+  __TEXT.__objc_methlist: 0x62ec
   __TEXT.__const: 0x724
-  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__oslogstring: 0x569b
-  __TEXT.__objc_methname: 0x111ef
-  __TEXT.__cstring: 0x2d37
+  __TEXT.__objc_methname: 0x111df
+  __TEXT.__cstring: 0x2d27
   __TEXT.__objc_classname: 0x14eb
-  __TEXT.__objc_methtype: 0x31b1
+  __TEXT.__objc_methtype: 0x3141
   __TEXT.__swift5_typeref: 0x280
   __TEXT.__constg_swiftt: 0x2b8
   __TEXT.__swift5_reflstr: 0x179

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e10
+  __TEXT.__unwind_info: 0x1e00
   __TEXT.__eh_frame: 0xb48
-  __DATA_CONST.__const: 0x1cc8
+  __DATA_CONST.__const: 0x1c78
   __DATA_CONST.__cfstring: 0x26c0
   __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x1d0
   __DATA.__objc_const: 0xd200
-  __DATA.__objc_selrefs: 0x3bc8
+  __DATA.__objc_selrefs: 0x3bc0
   __DATA.__objc_ivar: 0x5d4
   __DATA.__objc_data: 0x31b8
   __DATA.__data: 0x1ba0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2131
+  Functions: 2130
   Symbols:   602
-  CStrings:  4007
+  CStrings:  4003
 
CStrings:
+ "addUserInfoEntriesFromDictionary:"
+ "com.apple.shazam_internal_client"
+ "defaultCachedInstallationIDForAppleClient"
+ "iteratePresentationOptions:mediaItem:presentationSettings:completionHandler:"
+ "openNativeHistoryWithCompletionHandler:"
+ "presentTrackPageFromMediaItem:presentationSettings:completionHandler:"
+ "v48@0:8@16@24@32@?40"
- "displayShazamUpsell"
- "featureFlagsWithCompletion:"
- "initWithDictionary:"
- "iteratePresentationOptions:mediaItem:presentationSettings:featureFlags:completionHandler:"
- "openNativeHistoryWithShazamUpsell:completionHandler:"
- "presentTrackPageFromMediaItem:presentationSettings:displayShazamUpsell:completionHandler:"
- "shouldDisplayShazamUpsell"
- "v24@?0@\"SHFeatureFlags\"8@\"NSError\"16"
- "v44@0:8@\"SHMediaItem\"16@\"SHMediaItemPresentationSettings\"24B32@?<v@?q@\"NSURL\"@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v56@0:8@16@24@32@40@?48"
```
