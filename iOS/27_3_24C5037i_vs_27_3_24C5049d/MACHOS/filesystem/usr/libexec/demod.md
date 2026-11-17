## demod

> `/usr/libexec/demod`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-1871.60.21.0.0
-  __TEXT.__text: 0x104174
-  __TEXT.__auth_stubs: 0x2660
-  __TEXT.__objc_stubs: 0x1c160
-  __TEXT.__objc_methlist: 0xde7c
+1871.60.27.0.0
+  __TEXT.__text: 0x1048a8
+  __TEXT.__auth_stubs: 0x2670
+  __TEXT.__objc_stubs: 0x1c220
+  __TEXT.__objc_methlist: 0xdedc
   __TEXT.__const: 0x6c0
-  __TEXT.__cstring: 0x11a1c
-  __TEXT.__objc_classname: 0x18fa
-  __TEXT.__objc_methtype: 0x4131
-  __TEXT.__gcc_except_tab: 0x4b14
-  __TEXT.__oslogstring: 0x1e0dc
-  __TEXT.__objc_methname: 0x21f9e
+  __TEXT.__cstring: 0x11abc
+  __TEXT.__objc_classname: 0x191a
+  __TEXT.__objc_methtype: 0x4151
+  __TEXT.__gcc_except_tab: 0x4b54
+  __TEXT.__oslogstring: 0x1e20c
+  __TEXT.__objc_methname: 0x22070
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__swift5_capture: 0x19c
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x54d0
+  __TEXT.__unwind_info: 0x5500
   __TEXT.__eh_frame: 0x1020
   __DATA_CONST.__const: 0x3540
-  __DATA_CONST.__cfstring: 0xf140
+  __DATA_CONST.__cfstring: 0xf180
   __DATA_CONST.__objc_classlist: 0x740
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x168
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_intobj: 0x528
   __DATA_CONST.__objc_arraydata: 0x950
   __DATA_CONST.__objc_arrayobj: 0x480
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__auth_got: 0x1340
+  __DATA_CONST.__auth_got: 0x1348
   __DATA_CONST.__got: 0x1258
   __DATA_CONST.__auth_ptr: 0x230
-  __DATA.__objc_const: 0x19cc0
-  __DATA.__objc_selrefs: 0x84b8
+  __DATA.__objc_const: 0x19cd0
+  __DATA.__objc_selrefs: 0x84f0
   __DATA.__objc_ivar: 0xb68
   __DATA.__objc_data: 0x4940
-  __DATA.__data: 0x2aa8
+  __DATA.__data: 0x2b08
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6314
-  Symbols:   1250
-  CStrings:  11214
+  Functions: 6324
+  Symbols:   1251
+  CStrings:  11235
 
Symbols:
+ _$s17CompanionSetupKit11CSKStepMiscC5EventO18personalContentAskyAESb_tcAEmFWC
+ _swift_release_x23
- _$s17CompanionSetupKit11CSKStepMiscC5EventO18personalContentAskyA2EmFWC
CStrings:
+ "%s - Failed to reset fileindexerd - %{public}@"
+ "%s - Successfully reset fileindexerd"
+ "+[MSDSpotlightIndexHelper resetFileIndexer]_block_invoke"
+ "-[MSDHelperAgent fallbackToQiOne]"
+ "EnableQi1ChargingFallback"
+ "Failed to apply Qi 1 charging fallback."
+ "Found test preference for enabling Qi 1 charging fallback!"
+ "MSDFileIndexerProtocol"
+ "Qi 1 charging fallback enabled; applying."
+ "Timed out while waiting for fileindexerd to reset."
+ "applyQi1ChargingFallbackIfNeeded"
+ "com.apple.FileIndexer"
+ "enableQi1ChargingFallback"
+ "fallbackToQiOne"
+ "fallbackToQiOne:"
+ "homeDidUpdateUnrecognizedUserSettings:"
+ "remoteObjectProxyWithErrorHandler:"
+ "resetFileIndexer"
+ "resetFileIndexer failed"
+ "resetScanningStateUrgent:completionHandler:"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
```
