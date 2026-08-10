## ProductKit

> `/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`

```diff

-152.100.1.0.0
-  __TEXT.__text: 0x6cae0
+155.100.1.2.3
+  __TEXT.__text: 0x6d30c
   __TEXT.__objc_methlist: 0x668
-  __TEXT.__const: 0x63ac
+  __TEXT.__const: 0x63ec
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x23e4
-  __TEXT.__oslogstring: 0x1d03
-  __TEXT.__swift5_typeref: 0x18c2
-  __TEXT.__swift5_reflstr: 0x1da9
+  __TEXT.__cstring: 0x23c4
+  __TEXT.__oslogstring: 0x1df3
+  __TEXT.__swift5_typeref: 0x18c8
+  __TEXT.__swift5_reflstr: 0x1e09
   __TEXT.__swift5_assocty: 0x7a0
-  __TEXT.__constg_swiftt: 0x18e4
-  __TEXT.__swift5_fieldmd: 0x2618
+  __TEXT.__constg_swiftt: 0x18ec
+  __TEXT.__swift5_fieldmd: 0x266c
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_proto: 0x3d4
   __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift5_capture: 0x35c
+  __TEXT.__swift5_capture: 0x34c
   __TEXT.__swift_as_entry: 0x170
   __TEXT.__swift_as_ret: 0x1b4
   __TEXT.__swift_as_cont: 0x314
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x1d08
+  __TEXT.__unwind_info: 0x1cf0
   __TEXT.__eh_frame: 0x44c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x840
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x4ea0
+  __AUTH_CONST.__const: 0x4e60
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x1598
+  __AUTH_CONST.__objc_const: 0x1678
   __AUTH_CONST.__auth_got: 0x10c8
-  __AUTH.__objc_data: 0x8b0
+  __AUTH.__objc_data: 0x8e8
   __AUTH.__data: 0xe08
   __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x18c0
+  __DATA.__data: 0x1908
   __DATA.__bss: 0x77a0
   __DATA.__common: 0x90
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2236
-  Symbols:   1443
-  CStrings:  632
+  Functions: 2235
+  Symbols:   1445
+  CStrings:  635
 
Symbols:
+ -[PKMediaPlayerView handleBoundaryTimeObserverForMediaItem:currentTime:]
+ _CMTimeCopyDescription
+ _objc_msgSend$handleBoundaryTimeObserverForMediaItem:currentTime:
+ _objc_msgSend$position
+ _symbolic SdSg
- -[PKMediaPlayerView handleBoundaryTimeObserverForMediaItem:]
- _notify_register_dispatch
- _objc_msgSend$handleBoundaryTimeObserverForMediaItem:
CStrings:
+ "%s mediaItem: %@, current time %@"
+ "-[PKMediaPlayerView handleBoundaryTimeObserverForMediaItem:currentTime:]"
+ "Seeking to time: %@"
+ "Skipping sceneTime update: non-finite time for %s"
+ "Skipping video plane size update: invalid original size (%f, %f)"
+ "Skipping video plane size update: non-finite size (%f, %f)"
- "-[PKMediaPlayerView handleBoundaryTimeObserverForMediaItem:]"
- "Seeking to time"
- "com.apple.ProductKit.updateVideoPlaneSize"
```
