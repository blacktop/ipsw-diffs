## parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`

```diff

-3600.56.26.0.0
-  __TEXT.__text: 0x1768f4
+3600.56.26.11.2
+  __TEXT.__text: 0x175520
   __TEXT.__auth_stubs: 0x50c0
-  __TEXT.__objc_stubs: 0x4200
-  __TEXT.__objc_methlist: 0x10ec
-  __TEXT.__const: 0xf0e0
-  __TEXT.__cstring: 0x6944
-  __TEXT.__objc_classname: 0x14b7
-  __TEXT.__objc_methname: 0x6665
+  __TEXT.__objc_stubs: 0x41a0
+  __TEXT.__objc_methlist: 0x10a4
+  __TEXT.__const: 0xf080
+  __TEXT.__cstring: 0x6924
+  __TEXT.__objc_classname: 0x13d7
+  __TEXT.__objc_methname: 0x65d5
   __TEXT.__objc_methtype: 0x19e6
   __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x5aec
-  __TEXT.__swift5_typeref: 0x500a
-  __TEXT.__swift5_reflstr: 0x5603
-  __TEXT.__swift5_fieldmd: 0x5254
+  __TEXT.__constg_swiftt: 0x5a28
+  __TEXT.__swift5_typeref: 0x4f98
+  __TEXT.__swift5_reflstr: 0x5593
+  __TEXT.__swift5_fieldmd: 0x51c4
   __TEXT.__swift5_builtin: 0x35c
   __TEXT.__swift5_assocty: 0x650
   __TEXT.__swift5_capture: 0x39c0
-  __TEXT.__oslogstring: 0x6286
+  __TEXT.__oslogstring: 0x6156
   __TEXT.__swift5_proto: 0x8f4
-  __TEXT.__swift5_types: 0x4a0
+  __TEXT.__swift5_types: 0x494
   __TEXT.__swift_as_entry: 0xb0
   __TEXT.__swift_as_cont: 0xf8
   __TEXT.__swift5_protos: 0x138
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__unwind_info: 0x54f8
-  __TEXT.__eh_frame: 0x75e0
+  __TEXT.__unwind_info: 0x5498
+  __TEXT.__eh_frame: 0x75a0
   __DATA_CONST.__const: 0x10570
   __DATA_CONST.__cfstring: 0x8a0
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0x2870
   __DATA_CONST.__got: 0x1450
-  __DATA_CONST.__auth_ptr: 0x1f08
-  __DATA.__objc_const: 0x7738
-  __DATA.__objc_selrefs: 0x1598
+  __DATA_CONST.__auth_ptr: 0x1ef8
+  __DATA.__objc_const: 0x7498
+  __DATA.__objc_selrefs: 0x1580
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x1680
-  __DATA.__data: 0x9ce0
+  __DATA.__objc_data: 0x15b8
+  __DATA.__data: 0x9b40
   __DATA.__bss: 0xda00
   __DATA.__common: 0x5c0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9057
+  Functions: 9025
   Symbols:   2348
-  CStrings:  2552
+  CStrings:  2536
 
CStrings:
- "Caller location authorization changed: %{bool,public}d (status: %{public}d, accuracy: %{public}ld)"
- "Caller location authorized: %{bool,public}d for %{public}s"
- "Caller location request failed: %@"
- "Caller location updated: (%{public}f, %{public}f) accuracy: %{public}fm"
- "_TtC7parsecd21CallerLocationMonitor"
- "_TtCC7parsecd21CallerLocationMonitorP33_623A24F31DADE66D4B56BCDC3BA1128F5State"
- "_TtCC7parsecd21CallerLocationMonitorP33_623A24F31DADE66D4B56BCDC3BA1128F8Delegate"
- "accuracyAuthorization"
- "authHandler"
- "authorizationStatus"
- "authorized"
- "initWithEffectiveBundleIdentifier:delegate:onQueue:"
- "locationHandler"
- "manager"
- "parsecd.Delegate"
- "safariCallerLocationMonitor"
```
