## HeartRateCoordinator

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0x4a80
+41.1.0.0.0
+  __TEXT.__text: 0x4ad0
   __TEXT.__objc_methlist: 0x874
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__oslogstring: 0x48d
+  __TEXT.__oslogstring: 0x4cf
   __TEXT.__cstring: 0x25a
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__unwind_info: 0x290
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
CStrings:
+ "sending filtered HR with uuid : %{private}@, bpm : %{sensitive}f, confidence : %f, confidenceLevel : %{sensitive}u, context : %ld, date : %{private}@"
+ "sending one second streaming hr with uuid : %{private}@, bpm : %{sensitive}f, confidence : %f, confidenceLevel : %{sensitive}u, context : %ld, date : %{private}@"
- "sending filtered HR with uuid : %{private}@, bpm : %{sensitive}f, confidence : %f, context : %ld, date : %{private}@"
- "sending one second streaming hr with uuid : %{private}@, bpm : %{sensitive}f, confidence : %f, context : %ld, date : %{private}@"
```
