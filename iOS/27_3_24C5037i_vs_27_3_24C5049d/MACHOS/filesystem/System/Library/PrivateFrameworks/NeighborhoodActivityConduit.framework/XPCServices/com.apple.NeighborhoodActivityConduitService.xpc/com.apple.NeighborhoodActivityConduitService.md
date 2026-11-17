## com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`

```diff

-1626.300.42.0.0
-  __TEXT.__text: 0x16f9e0
-  __TEXT.__auth_stubs: 0x3d80
-  __TEXT.__objc_stubs: 0x33c0
+1626.300.62.0.0
+  __TEXT.__text: 0x174300
+  __TEXT.__auth_stubs: 0x3dd0
+  __TEXT.__objc_stubs: 0x3400
   __TEXT.__objc_methlist: 0x187c
-  __TEXT.__objc_methname: 0x7719
-  __TEXT.__cstring: 0x2386
+  __TEXT.__objc_methname: 0x7769
+  __TEXT.__cstring: 0x23a6
   __TEXT.__objc_classname: 0xdbb
-  __TEXT.__objc_methtype: 0x12a1
-  __TEXT.__const: 0x51d8
-  __TEXT.__swift5_typeref: 0x3943
+  __TEXT.__objc_methtype: 0x12f1
+  __TEXT.__const: 0x5250
+  __TEXT.__swift5_typeref: 0x3a06
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2064
+  __TEXT.__constg_swiftt: 0x208c
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x2189
-  __TEXT.__swift5_fieldmd: 0x1658
+  __TEXT.__swift5_reflstr: 0x21a9
+  __TEXT.__swift5_fieldmd: 0x1664
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0x1c0
   __TEXT.__swift5_types: 0x140
-  __TEXT.__oslogstring: 0x80c5
-  __TEXT.__swift5_capture: 0x33f0
-  __TEXT.__swift_as_entry: 0x628
-  __TEXT.__swift_as_ret: 0x62c
-  __TEXT.__swift_as_cont: 0x12f0
+  __TEXT.__oslogstring: 0x81b5
+  __TEXT.__swift5_capture: 0x3494
+  __TEXT.__swift_as_entry: 0x638
+  __TEXT.__swift_as_ret: 0x638
+  __TEXT.__swift_as_cont: 0x1304
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x54b0
-  __TEXT.__eh_frame: 0xfb00
-  __DATA_CONST.__const: 0x75c0
+  __TEXT.__unwind_info: 0x5550
+  __TEXT.__eh_frame: 0xfc80
+  __DATA_CONST.__const: 0x7768
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1ec8
-  __DATA_CONST.__got: 0x10a8
+  __DATA_CONST.__auth_got: 0x1ef0
+  __DATA_CONST.__got: 0x10b8
   __DATA_CONST.__auth_ptr: 0x908
   __DATA.__objc_const: 0x4a40
-  __DATA.__objc_selrefs: 0x1910
+  __DATA.__objc_selrefs: 0x1920
   __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x1520
-  __DATA.__data: 0x3f88
+  __DATA.__objc_data: 0x1528
+  __DATA.__data: 0x4020
   __DATA.__common: 0x180
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4533
-  Symbols:   439
-  CStrings:  1841
+  Functions: 4583
+  Symbols:   440
+  CStrings:  1849
 
Symbols:
+ _CNContactStoreDidChangeNotification
CStrings:
+ "Contact info changed for %ld handles, pushing their contacts again."
+ "Replacing conduit device %s whose IDS device identifier changed to %s."
+ "[MeDetails] hasContact=%{bool}d hasImage=%{bool}d hasCallerID=%{bool}d"
+ "fetchMeDetails()"
+ "getLocalCallerIDWithCompletionHandler:"
+ "setDeviceChangedHandler:"
+ "v16@?0@\"TUHandle\"8"
+ "v20@?0@\"RPCompanionLinkDevice\"8I16"
```
