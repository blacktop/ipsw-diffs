## findmylocated

> `/usr/libexec/findmylocated`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-141.31.6.16.21
-  __TEXT.__text: 0x55c9e0
-  __TEXT.__auth_stubs: 0x5d90
-  __TEXT.__objc_stubs: 0x2100
+141.31.6.16.22
+  __TEXT.__text: 0x55e1f0
+  __TEXT.__auth_stubs: 0x5da0
+  __TEXT.__objc_stubs: 0x20e0
   __TEXT.__objc_methlist: 0x1004
-  __TEXT.__const: 0x20938
-  __TEXT.__cstring: 0xbd92
-  __TEXT.__swift5_typeref: 0x727c
-  __TEXT.__constg_swiftt: 0x7234
+  __TEXT.__const: 0x209a8
+  __TEXT.__cstring: 0xbdc2
+  __TEXT.__swift5_typeref: 0x72fa
+  __TEXT.__constg_swiftt: 0x7294
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x7eed
-  __TEXT.__swift5_fieldmd: 0x9114
+  __TEXT.__swift5_reflstr: 0x7efd
+  __TEXT.__swift5_fieldmd: 0x9140
   __TEXT.__swift5_assocty: 0x958
   __TEXT.__swift5_proto: 0x1790
   __TEXT.__swift5_types: 0x800
   __TEXT.__objc_classname: 0x1336
-  __TEXT.__objc_methname: 0x51f5
+  __TEXT.__objc_methname: 0x51c5
   __TEXT.__objc_methtype: 0x13a8
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__oslogstring: 0x1974c
-  __TEXT.__swift_as_entry: 0x1778
-  __TEXT.__swift_as_ret: 0x299c
-  __TEXT.__swift_as_cont: 0x45d0
-  __TEXT.__swift5_capture: 0x4fdc
+  __TEXT.__oslogstring: 0x1983c
+  __TEXT.__swift_as_entry: 0x1780
+  __TEXT.__swift_as_ret: 0x29ac
+  __TEXT.__swift_as_cont: 0x45ec
+  __TEXT.__swift5_capture: 0x4ff0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x18b08
-  __TEXT.__eh_frame: 0x4a288
-  __DATA_CONST.__const: 0x18878
+  __TEXT.__unwind_info: 0x18b68
+  __TEXT.__eh_frame: 0x4a468
+  __DATA_CONST.__const: 0x188c8
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__linkguard: 0x33
-  __DATA_CONST.__auth_got: 0x2ed0
-  __DATA_CONST.__got: 0x1dc0
+  __DATA_CONST.__auth_got: 0x2ed8
+  __DATA_CONST.__got: 0x1dd8
   __DATA_CONST.__auth_ptr: 0x1890
   __DATA.__objc_const: 0x65a0
-  __DATA.__objc_selrefs: 0xde8
+  __DATA.__objc_selrefs: 0xde0
   __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0xf380
+  __DATA.__data: 0xf370
   __DATA.__common: 0x13f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17812
-  Symbols:   2839
-  CStrings:  3931
+  Functions: 17836
+  Symbols:   2842
+  CStrings:  3934
 
Symbols:
+ _$s8Dispatch0A3QoSV0B6SClassO7utilityyA2EmFWC
+ _CLLocationCoordinate2DIsValid
+ _CNContactPhoneNumbersKey
CStrings:
+ "%{public}s: Dropping labeled location with invalid coordinate (lat: %{private}f, long: %{private}f)"
+ "[%{public}s] matchingContacts: finished, found %{public}ld match(es)"
+ "[%{public}s] matchingContacts: starting"
+ "labeledLocations(for:)"
+ "matchingContacts(predicate:keysToFetch:)"
- "ContactHandleCollaboration"
- "predicateForContactsMatchingPhoneNumber:prefixHint:"
```
