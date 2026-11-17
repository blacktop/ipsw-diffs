## nanoregistryd

> `/usr/libexec/nanoregistryd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1075.17.2.1.0
-  __TEXT.__text: 0x101e7c
+1075.17.4.0.0
+  __TEXT.__text: 0x102814
   __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_stubs: 0x113c0
-  __TEXT.__objc_methlist: 0xdd94
+  __TEXT.__objc_stubs: 0x113e0
+  __TEXT.__objc_methlist: 0xddac
   __TEXT.__const: 0x748
   __TEXT.__gcc_except_tab: 0x1db0
-  __TEXT.__objc_methname: 0x1cd99
-  __TEXT.__cstring: 0xe507
-  __TEXT.__oslogstring: 0x16b48
+  __TEXT.__objc_methname: 0x1cdb9
+  __TEXT.__cstring: 0xe557
+  __TEXT.__oslogstring: 0x16c48
   __TEXT.__objc_classname: 0x22c5
   __TEXT.__objc_methtype: 0x4c68
   __TEXT.__dlopen_cstrs: 0xef

   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4998
+  __TEXT.__unwind_info: 0x49a0
   __DATA_CONST.__const: 0x4cb8
-  __DATA_CONST.__cfstring: 0xc4c0
+  __DATA_CONST.__cfstring: 0xc520
   __DATA_CONST.__objc_classlist: 0x818
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x240

   __DATA_CONST.__objc_arrayobj: 0x258
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__auth_got: 0xa50
-  __DATA_CONST.__got: 0xe18
+  __DATA_CONST.__got: 0xe28
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x1a980
-  __DATA.__objc_selrefs: 0x5fa0
+  __DATA.__objc_selrefs: 0x5fa8
   __DATA.__objc_ivar: 0x1204
   __DATA.__objc_data: 0x51e0
   __DATA.__data: 0x1af8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5927
-  Symbols:   780
-  CStrings:  8773
+  Functions: 5929
+  Symbols:   781
+  CStrings:  8781
 
Symbols:
+ __NRDevicePropertyPostRestoreSettingsResetPending
CStrings:
+ "35"
+ "NanoRegistry-1075.17.4"
+ "Same phone migration: %{public}@ is not active, deferring NPS domain clear to first switch"
+ "Same phone migration: adding transaction to erase NPS domains for %{public}@"
+ "Same phone migration: no data store path for active pairing %{public}@, not clearing NPS domains"
+ "clearNPSDomains-"
+ "clearNPSDomainsOnSwitch"
+ "clearNPSDomainsOnSwitchDone"
+ "settingsDomainsToClear"
- "NanoRegistry-1075.17.2.1"
```
