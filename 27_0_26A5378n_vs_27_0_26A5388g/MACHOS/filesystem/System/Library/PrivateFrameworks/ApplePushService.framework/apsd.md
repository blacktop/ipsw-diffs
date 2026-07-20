## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1163.100.1.0.0
-  __TEXT.__text: 0x13d52c
+1165.100.1.0.0
+  __TEXT.__text: 0x13d664
   __TEXT.__auth_stubs: 0x3440
-  __TEXT.__objc_stubs: 0x11da0
+  __TEXT.__objc_stubs: 0x11d80
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0xc6c0
+  __TEXT.__objc_methlist: 0xc698
   __TEXT.__const: 0x13330
-  __TEXT.__objc_methname: 0x1d035
+  __TEXT.__objc_methname: 0x1d005
   __TEXT.__cstring: 0xef9a
-  __TEXT.__oslogstring: 0x162a5
+  __TEXT.__oslogstring: 0x162e5
   __TEXT.__objc_classname: 0x129b
-  __TEXT.__objc_methtype: 0x4fd9
-  __TEXT.__gcc_except_tab: 0x2624
+  __TEXT.__objc_methtype: 0x4f99
+  __TEXT.__gcc_except_tab: 0x2614
   __TEXT.__dlopen_cstrs: 0xae
   __TEXT.__ustring: 0x28
   __TEXT.__swift5_typeref: 0x8a6

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4240
+  __TEXT.__unwind_info: 0x4238
   __TEXT.__eh_frame: 0x3e0
   __DATA_CONST.__const: 0xafd0
   __DATA_CONST.__cfstring: 0x9040

   __DATA_CONST.__auth_got: 0x1a38
   __DATA_CONST.__got: 0x920
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA.__objc_const: 0x1bdc8
-  __DATA.__objc_selrefs: 0x5ca0
-  __DATA.__objc_ivar: 0xc5c
+  __DATA.__objc_const: 0x1bdd8
+  __DATA.__objc_selrefs: 0x5c98
+  __DATA.__objc_ivar: 0xc60
   __DATA.__objc_data: 0x39c0
   __DATA.__data: 0x3bc8
   __DATA.__bss: 0x1bc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7039
+  Functions: 7036
   Symbols:   1172
   CStrings:  9114
 
CStrings:
+ "%@ Closed without starting connection, refunding offload info"
+ "%@: Burning offload info for connection attempt"
+ "_connectionStarted"
+ "insertObject:atIndex:"
+ "tcpStream:receivedOffloadInfo:onInterface:"
+ "v40@0:8@\"<APSTCPStream>\"16@\"APSConnectionOffloadInfo\"24q32"
- "%@: Burning offload info to start connection"
- "courierConnection:willStartConnectionWithOffloadInfo:"
- "tcpStream:receivedOffloadInfo:"
- "tcpStream:willStartConnectionWithOffloadInfo:"
- "v32@0:8@\"<APSTCPStream>\"16@\"APSConnectionOffloadInfo\"24"
- "v32@0:8@\"APSCourierConnection\"16@\"APSConnectionOffloadInfo\"24"
```
