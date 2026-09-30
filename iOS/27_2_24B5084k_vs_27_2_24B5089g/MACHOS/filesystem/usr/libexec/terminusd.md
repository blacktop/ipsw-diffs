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
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-914.40.22.0.0
-  __TEXT.__text: 0x1fb854
+914.40.23.0.0
+  __TEXT.__text: 0x1fb9a4
   __TEXT.__auth_stubs: 0x3ef0
   __TEXT.__objc_stubs: 0x8e00
   __TEXT.__objc_methlist: 0x5594
   __TEXT.__const: 0x73c
   __TEXT.__swift5_typeref: 0x4ce
-  __TEXT.__cstring: 0x52a43
+  __TEXT.__cstring: 0x52a9a
   __TEXT.__swift5_capture: 0x4a4
   __TEXT.__objc_methtype: 0x433b
   __TEXT.__oslogstring: 0x2dee

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3908
+  Functions: 3909
   Symbols:   1547
-  CStrings:  11628
+  CStrings:  11629
 
CStrings:
+ "%s%.30s:%-4d Not marking %@ as my distributee: link type is Infra Relay"
+ "%s%.30s:%-4d Not marking %@ as my distributee: we are locally on %@ infrastructure Wi-Fi or Infra Relay"
+ "914.40.23"
- "%s%.30s:%-4d Not marking %@ as my distributee: we are locally on %@ infrastructure Wi-Fi"
- "914.40.22"
```
