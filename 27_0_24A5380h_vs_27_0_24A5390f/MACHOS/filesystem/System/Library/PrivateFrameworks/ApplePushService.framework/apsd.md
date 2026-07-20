## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
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
-  __TEXT.__text: 0x1177f0
+1165.100.1.0.0
+  __TEXT.__text: 0x117900
   __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x10ba0
+  __TEXT.__objc_stubs: 0x10b80
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0xb7f0
-  __TEXT.__objc_methname: 0x1b8d5
+  __TEXT.__objc_methlist: 0xb7c8
+  __TEXT.__objc_methname: 0x1b8a5
   __TEXT.__objc_classname: 0x132b
-  __TEXT.__objc_methtype: 0x5559
+  __TEXT.__objc_methtype: 0x5519
   __TEXT.__cstring: 0xfc14
   __TEXT.__const: 0xd983
-  __TEXT.__oslogstring: 0x14125
-  __TEXT.__gcc_except_tab: 0x2680
+  __TEXT.__oslogstring: 0x14165
+  __TEXT.__gcc_except_tab: 0x2670
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__constg_swiftt: 0x1340
   __TEXT.__swift5_typeref: 0x970

   __DATA_CONST.__auth_got: 0x1a70
   __DATA_CONST.__got: 0x938
   __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA.__objc_const: 0x1c540
-  __DATA.__objc_selrefs: 0x5668
-  __DATA.__objc_ivar: 0xbb0
+  __DATA.__objc_const: 0x1c550
+  __DATA.__objc_selrefs: 0x5660
+  __DATA.__objc_ivar: 0xbb4
   __DATA.__objc_data: 0x3618
   __DATA.__data: 0x4660
   __DATA.__bss: 0x1360

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6772
+  Functions: 6770
   Symbols:   1194
   CStrings:  8610
 
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
