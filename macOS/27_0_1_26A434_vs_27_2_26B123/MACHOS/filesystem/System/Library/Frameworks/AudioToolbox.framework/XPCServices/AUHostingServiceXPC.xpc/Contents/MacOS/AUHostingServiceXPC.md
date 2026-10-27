## AUHostingServiceXPC

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AUHostingServiceXPC.xpc/Contents/MacOS/AUHostingServiceXPC`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_AUHosting`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1638.104.3.0.0
-  __TEXT.__text: 0x83ce
-  __TEXT.__stubs: 0x2dc
+1638.213.0.0.0
+  __TEXT.__text: 0x904f
+  __TEXT.__stubs: 0x324
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x8fc
-  __TEXT.__cstring: 0xbef
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x980
+  __TEXT.__cstring: 0xc14
   __TEXT.__objc_methname: 0x157d
   __TEXT.__objc_classname: 0x19f
   __TEXT.__objc_methtype: 0xdca
-  __TEXT.__oslogstring: 0x684
+  __TEXT.__oslogstring: 0x7c4
   __TEXT.__dof_AUHosting: 0x4a9
-  __TEXT.__unwind_info: 0x400
-  __DATA_CONST.__const: 0x880
+  __TEXT.__unwind_info: 0x438
+  __TEXT.__eh_frame: 0x58
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__got: 0x5b0
   __DATA.__objc_const: 0x1850
   __DATA.__objc_selrefs: 0x3f0
   __DATA.__objc_ivar: 0x78

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 174
-  Symbols:   178
-  CStrings:  467
+  Functions: 184
+  Symbols:   195
+  CStrings:  474
 
Symbols:
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZTVSt12length_error
+ ____chkstk_darwin
+ ___cxa_free_exception
+ __xpc_type_null
+ _getpid
+ _memchr
+ _memcpy
+ _proc_pidpath_audittoken
+ _xpc_copy_bootstrap
+ _xpc_dictionary_get_audit_token
+ _xpc_null_create
+ _xpc_release
CStrings:
+ "%25s:%-5d bootstrap dictionary did not carry a valid host audit token"
+ "%25s:%-5d failed to resolve executable path for host audit token: %{darwin.errno}d"
+ "%25s:%-5d no XPC bootstrap dictionary available; cannot resolve host bundle path"
+ "%25s:%-5d resolved host bundle path is empty"
+ "HOST_BUNDLE_PATH"
+ "basic_string"
+ "vector"
```
