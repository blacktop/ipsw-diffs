## terminusd

> `/usr/libexec/terminusd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-914.40.23.0.0
-  __TEXT.__text: 0x1fb9a4
-  __TEXT.__auth_stubs: 0x3ef0
+914.40.26.502.1
+  __TEXT.__text: 0x1fbf4c
+  __TEXT.__auth_stubs: 0x3f10
   __TEXT.__objc_stubs: 0x8e00
   __TEXT.__objc_methlist: 0x5594
   __TEXT.__const: 0x73c
   __TEXT.__swift5_typeref: 0x4ce
-  __TEXT.__cstring: 0x52a9a
+  __TEXT.__cstring: 0x52bd6
   __TEXT.__swift5_capture: 0x4a4
   __TEXT.__objc_methtype: 0x433b
   __TEXT.__oslogstring: 0x2dee

   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__gcc_except_tab: 0x62c8
-  __TEXT.__unwind_info: 0x3e98
-  __TEXT.__eh_frame: 0xe90
-  __DATA_CONST.__const: 0x4f18
+  __TEXT.__gcc_except_tab: 0x63b4
+  __TEXT.__unwind_info: 0x3ea8
+  __TEXT.__eh_frame: 0xeb8
+  __DATA_CONST.__const: 0x4f40
   __DATA_CONST.__cfstring: 0xe280
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1f88
-  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__auth_got: 0x1f98
+  __DATA_CONST.__got: 0xf08
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x19f78
   __DATA.__objc_selrefs: 0x2b60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3909
-  Symbols:   1547
-  CStrings:  11629
+  Functions: 3910
+  Symbols:   1550
+  CStrings:  11633
 
Symbols:
+ _RPOptionStatusFlags
+ _nw_advertise_descriptor_get_advertise_scope
+ _nw_endpoint_get_application_service_alias
CStrings:
+ "%s%.30s:%-4d Not starting NAN: room distributor is unused (wired link or 6GHz infrastructure Wi-Fi)"
+ "%s%.30s:%-4d advertise scope unset for %@, defaulting to personal|family"
+ "%s%.30s:%-4d no advertise descriptor for %@, ignoring resolve request"
+ "%s%.30s:%-4d not returning endpoint for %@ (%@), no common scope %u/%u"
+ "%s%.30s:%-4d returning endpoint for %@ (%@), common scope %u/%u"
+ "%s%.30s:%-4d returning endpoint for %@, advertise scope all"
+ "%s%.30s:%-4d room distributor unused (wired link or 6GHz infrastructure Wi-Fi), not establishing a distribution relationship towards the room distributor"
+ "-[NRApplicationServiceManager copyListenerEndpointForASName:asClient:]"
+ "914.40.26.502.1"
- "%s%.30s:%-4d Not starting NAN: room distributor is unused (wired link or 2.4GHz/6GHz infrastructure Wi-Fi)"
- "%s%.30s:%-4d room distributor unused (wired link or 2.4GHz/6GHz infrastructure Wi-Fi), not establishing a distribution relationship towards the room distributor"
- "-[NRApplicationServiceManager copyListenerEndpointForASName:]"
- "914.40.23"
- "disableWiFiAwareOn2GHz"
```
