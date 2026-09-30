## companiond

> `/usr/libexec/companiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-524.0.38.0.0
-  __TEXT.__text: 0x8bffc
-  __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__objc_stubs: 0x43a0
+524.0.56.0.0
+  __TEXT.__text: 0x8c560
+  __TEXT.__auth_stubs: 0x2d70
+  __TEXT.__objc_stubs: 0x43e0
   __TEXT.__objc_methlist: 0x2b60
-  __TEXT.__objc_methname: 0x6115
-  __TEXT.__swift5_typeref: 0xc9f
+  __TEXT.__objc_methname: 0x6155
+  __TEXT.__swift5_typeref: 0xcbb
   __TEXT.__swift5_fieldmd: 0x820
   __TEXT.__objc_classname: 0xb48
   __TEXT.__objc_methtype: 0x1588
-  __TEXT.__const: 0x2096
+  __TEXT.__const: 0x20b6
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_reflstr: 0x832
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x2669
+  __TEXT.__cstring: 0x2621
   __TEXT.__swift5_capture: 0x754
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0x118

   __TEXT.__swift_as_entry: 0x1b0
   __TEXT.__swift_as_ret: 0x1d0
   __TEXT.__swift_as_cont: 0x3a8
-  __TEXT.__oslogstring: 0x417e
+  __TEXT.__oslogstring: 0x4142
   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0x1ab0
   __TEXT.__ustring: 0x40
   __TEXT.__unwind_info: 0x2558
   __TEXT.__eh_frame: 0x4ed0
   __DATA_CONST.__const: 0x2560
-  __DATA_CONST.__cfstring: 0x1ba0
+  __DATA_CONST.__cfstring: 0x1b80
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x16d0
+  __DATA_CONST.__auth_got: 0x16c8
   __DATA_CONST.__got: 0xd08
   __DATA_CONST.__auth_ptr: 0x558
   __DATA.__objc_const: 0x7548
-  __DATA.__objc_selrefs: 0x1530
+  __DATA.__objc_selrefs: 0x1540
   __DATA.__objc_ivar: 0x410
   __DATA.__objc_data: 0x18e0
-  __DATA.__data: 0x1e20
+  __DATA.__data: 0x1e10
   __DATA.__bss: 0x2380
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/AppleConnectClient.framework/AppleConnectClient
-  Functions: 2295
-  Symbols:   1274
-  CStrings:  1952
+  Functions: 2296
+  Symbols:   1273
+  CStrings:  1950
 
Symbols:
- __os_feature_enabled_impl
CStrings:
+ "initWithUnsignedLongLong:"
+ "numberWithUnsignedLongLong:"
- "Feature flag not enabled."
- "Rejecting Incoming Calls session: Feature flag not enabled."
- "TelephonyUtilities"
- "telephonyCallNotifications"
```
