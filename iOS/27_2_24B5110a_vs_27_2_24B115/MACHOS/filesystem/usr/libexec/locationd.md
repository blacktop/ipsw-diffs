## locationd

> `/usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 3186.0.22.0.0
-  __TEXT.__text: 0x1af6be4
+  __TEXT.__text: 0x1af7144
   __TEXT.__auth_stubs: 0x6580
   __TEXT.__objc_stubs: 0x3e8c0
   __TEXT.__init_offsets: 0xc0c
   __TEXT.__objc_methlist: 0x2e9b8
   __TEXT.__const: 0x1669b8
-  __TEXT.__gcc_except_tab: 0xdaaf0
-  __TEXT.__oslogstring: 0x29376c
-  __TEXT.__cstring: 0x2115ae
+  __TEXT.__gcc_except_tab: 0xdab38
+  __TEXT.__oslogstring: 0x29395c
+  __TEXT.__cstring: 0x2115de
   __TEXT.__objc_methname: 0x5d66f
   __TEXT.__objc_classname: 0x812d
   __TEXT.__objc_methtype: 0x39766

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 113642
   Symbols:   2920
-  CStrings:  85426
+  CStrings:  85431
 
Functions:
~ sub_10003749c : 5324 -> 5832
~ sub_10015ac58 -> sub_10015ae54 : 1320 -> 1772
~ sub_100c0b418 -> sub_100c0b7d8 : 1448 -> 1864
CStrings:
+ "#CoreLocationAgent ignoring a disconnection from a connection that does not hold the agent slot"
+ "#CoreLocationAgent rejecting an unentitled connection"
+ "com.apple.private.locationd.corelocationagent"
+ "{\"msg%{public}.0s\":\"#CoreLocationAgent ignoring a disconnection from a connection that does not hold the agent slot\", \"UserName\":%{public, location:escape_only}s, \"Connection\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#CoreLocationAgent rejecting an unentitled connection\", \"Connection\":%{public, location:escape_only}s, \"PID\":%{public}d}"
```
