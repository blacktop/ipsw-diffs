## swtransparencyd

> `/usr/libexec/swtransparencyd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1766.0.39.0.2
-  __TEXT.__text: 0xfde8c
+1766.0.60.0.0
+  __TEXT.__text: 0xfdeac
   __TEXT.__auth_stubs: 0x27e0
   __TEXT.__objc_stubs: 0x65c0
-  __TEXT.__objc_methlist: 0x709c
+  __TEXT.__objc_methlist: 0x70b4
   __TEXT.__const: 0x5ed0
   __TEXT.__cstring: 0x4da9
   __TEXT.__oslogstring: 0x36bd
   __TEXT.__objc_classname: 0x1a24
-  __TEXT.__objc_methname: 0x77cd
+  __TEXT.__objc_methname: 0x780d
   __TEXT.__objc_methtype: 0x20a5
   __TEXT.__gcc_except_tab: 0x448
   __TEXT.__swift5_typeref: 0x141b

   __DATA_CONST.__auth_got: 0x1400
   __DATA_CONST.__got: 0x698
   __DATA_CONST.__auth_ptr: 0x508
-  __DATA.__objc_const: 0xe830
-  __DATA.__objc_selrefs: 0x2148
-  __DATA.__objc_ivar: 0x464
+  __DATA.__objc_const: 0xe860
+  __DATA.__objc_selrefs: 0x2158
+  __DATA.__objc_ivar: 0x468
   __DATA.__objc_data: 0x3d10
   __DATA.__data: 0x48c0
   __DATA.__bss: 0x7118

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6029
+  Functions: 6031
   Symbols:   957
-  CStrings:  2890
+  CStrings:  2894
 
CStrings:
+ "T@\"NSString\",&,V_requestType"
+ "_requestType"
+ "requestType"
+ "setRequestType:"
```
