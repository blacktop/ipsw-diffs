## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3111.40.40.0.0
-  __TEXT.__text: 0x8b308
+3111.40.42.0.0
+  __TEXT.__text: 0x8b3dc
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__const: 0x2e5
   __TEXT.__cstring: 0x8f27
-  __TEXT.__oslogstring: 0x141b4
+  __TEXT.__oslogstring: 0x1423e
   __TEXT.__objc_methname: 0x506
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methtype: 0x237

   - /usr/lib/libsqlite3.dylib
   Functions: 489
   Symbols:   1184
-  CStrings:  2703
+  CStrings:  2704
 
Functions:
~ _srp_mdns_cancel_previous_instance : 524 -> 536
~ _prepare_update : 22068 -> 22056
~ _register_instance : 1680 -> 1684
~ _instance_vec_txns_forget : 368 -> 576
CStrings:
+ "%{public}s: forgetting previous sdref %p on %{public}s %p %{private, mask.hash}s instance %{private, mask.hash}s . %{private, mask.hash}s"
```
