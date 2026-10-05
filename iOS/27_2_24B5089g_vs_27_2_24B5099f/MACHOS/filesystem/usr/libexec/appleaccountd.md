## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1069.125.4.0.0
-  __TEXT.__text: 0x3ceee0
-  __TEXT.__auth_stubs: 0x3810
+1069.125.7.0.0
+  __TEXT.__text: 0x3cf754
+  __TEXT.__auth_stubs: 0x3800
   __TEXT.__objc_stubs: 0x4de0
   __TEXT.__objc_methlist: 0xf80
   __TEXT.__objc_methname: 0x78b5

   __TEXT.__swift5_assocty: 0x938
   __TEXT.__swift5_proto: 0xc68
   __TEXT.__swift5_types: 0x63c
-  __TEXT.__swift5_capture: 0x66a0
-  __TEXT.__oslogstring: 0x210ad
+  __TEXT.__swift5_capture: 0x66a4
+  __TEXT.__oslogstring: 0x212ad
   __TEXT.__swift5_protos: 0x22c
   __TEXT.__swift_as_entry: 0x680
   __TEXT.__swift_as_ret: 0x88c
   __TEXT.__swift_as_cont: 0x11d8
   __TEXT.__swift5_acfuncs: 0xb4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xa310
-  __TEXT.__eh_frame: 0x14824
+  __TEXT.__unwind_info: 0xa320
+  __TEXT.__eh_frame: 0x1488c
   __DATA_CONST.__const: 0x14048
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1c10
-  __DATA_CONST.__got: 0x1580
+  __DATA_CONST.__auth_got: 0x1c08
+  __DATA_CONST.__got: 0x1568
   __DATA_CONST.__auth_ptr: 0x16a0
   __DATA.__objc_const: 0x1e170
   __DATA.__objc_selrefs: 0x1748
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x3360
-  __DATA.__data: 0x14480
+  __DATA.__data: 0x144a0
   __DATA.__objc_stublist: 0x68
   __DATA.__common: 0x4e0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10281
-  Symbols:   1820
-  CStrings:  4205
+  Functions: 10282
+  Symbols:   1818
+  CStrings:  4213
 
Symbols:
+ _$s10Foundation4DateV2geoiySbAC_ACtFZ
+ _$s11Distributed0A23TargetInvocationDecoderP18decodeNextArgumentqd__yKlFTj
- _$s10Foundation4DateVSLAAMc
- _$s14XPCDistributed9XPCSystemC17InvocationDecoderV18decodeNextArgumentxyKSeRzSERzlF
- _$sSL2geoiySbx_xtFZTj
- _swift_conformsToProtocol2
CStrings:
+ "Avatar update handled by Contacts, using 1-hour expiration"
+ "Avatar update handled by background upload, using 3-day expiration"
+ "Cached identity from network fetch"
+ "Cancelling in-flight background refresh and upload for avatar update"
+ "Invalidating cached identity for account: %{private,mask.hash}s"
+ "Name-only update, preserving existing cache metadata"
+ "Network fetch failed, returning identity with name components only"
+ "Removed cached identity file"
```
