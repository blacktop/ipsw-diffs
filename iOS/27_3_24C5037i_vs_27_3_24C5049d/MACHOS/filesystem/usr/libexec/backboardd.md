## backboardd

> `/usr/libexec/backboardd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
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

-877.3.5.0.0
-  __TEXT.__text: 0x59288
-  __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_stubs: 0xa020
-  __TEXT.__objc_methlist: 0x4b44
+877.3.9.0.0
+  __TEXT.__text: 0x5963c
+  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__objc_stubs: 0xa0e0
+  __TEXT.__objc_methlist: 0x4b64
   __TEXT.__const: 0x320
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__gcc_except_tab: 0x760
-  __TEXT.__objc_methname: 0xdd39
+  __TEXT.__objc_methname: 0xde08
   __TEXT.__objc_classname: 0x13fd
-  __TEXT.__cstring: 0x4d3e
+  __TEXT.__cstring: 0x4d5e
   __TEXT.__objc_methtype: 0x2ec3
-  __TEXT.__oslogstring: 0x738d
-  __TEXT.__unwind_info: 0x1bd0
+  __TEXT.__oslogstring: 0x74a3
+  __TEXT.__unwind_info: 0x1bd8
   __DATA_CONST.__const: 0x3398
   __DATA_CONST.__cfstring: 0x5080
   __DATA_CONST.__objc_classlist: 0x340

   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xad0
+  __DATA_CONST.__auth_got: 0xae0
   __DATA_CONST.__got: 0x8a0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0xb1a0
-  __DATA.__objc_selrefs: 0x3128
+  __DATA.__objc_selrefs: 0x3158
   __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x2080
   __DATA.__data: 0x1be8

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 1940
-  Symbols:   621
-  CStrings:  4122
+  Functions: 1943
+  Symbols:   623
+  CStrings:  4133
 
Symbols:
+ _IOHIDServiceGetRegistryID
+ __os_feature_enabled_impl
CStrings:
+ "Apple Logo for display %{public}@ (%{public}@) is laid out for the legacy main display: PUIProgressWindow can't target other displays"
+ "Apple Logo for display %{public}@ (%{public}@): %{public}@"
+ "Current bootUI for display %{public}@ is the spinny: it is not the legacy main display and the Apple Logo is not supported on multiple displays, level %g"
+ "RouteDoubleTapForVI"
+ "SpringBoard"
+ "_isSqueezeRoutingOwnedBySpringBoard"
+ "errorDescription"
+ "initWithOptions:contextLevel:appearance:targetDisplayUniqueId:"
+ "initial ringer state:%{public}@ service:0x%llX"
+ "instancesRespondToSelector:"
+ "isSupportedOnMultipleDisplays"
+ "no ringer switch state from %lu matching services"
+ "targetDisplayUniqueIdForDisplay:"
- "Current bootUI for display %{public}@ is the spinny because the Apple Logo can only be laid out for the legacy main display, level %g"
- "initial ringer state:%{public}@"
```
