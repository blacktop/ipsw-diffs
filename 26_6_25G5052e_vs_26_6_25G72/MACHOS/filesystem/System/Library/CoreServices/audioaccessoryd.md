## audioaccessoryd

> `/System/Library/CoreServices/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 35.14.0.0.0
-  __TEXT.__text: 0x228d08
+  __TEXT.__text: 0x229104
   __TEXT.__auth_stubs: 0x2990
-  __TEXT.__objc_stubs: 0x19740
+  __TEXT.__objc_stubs: 0x19760
   __TEXT.__objc_methlist: 0xc0fc
   __TEXT.__const: 0x43f0
   __TEXT.__gcc_except_tab: 0x5214
-  __TEXT.__cstring: 0x47aa3
+  __TEXT.__cstring: 0x47c43
   __TEXT.__objc_classname: 0xe83
   __TEXT.__objc_methname: 0x244e5
   __TEXT.__objc_methtype: 0x3a49

   __TEXT.__swift5_capture: 0x1a28
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6350
+  __TEXT.__unwind_info: 0x6360
   __TEXT.__eh_frame: 0x1c98
   __DATA_CONST.__auth_got: 0x14d8
   __DATA_CONST.__got: 0xaa0
   __DATA_CONST.__auth_ptr: 0x580
   __DATA_CONST.__const: 0xb5c8
-  __DATA_CONST.__cfstring: 0xa920
+  __DATA_CONST.__cfstring: 0xa960
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x158

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9991
+  Functions: 9994
   Symbols:   1155
-  CStrings:  13601
+  CStrings:  13609
 
CStrings:
+ "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]"
+ "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
+ "AudioQualityMonitor"
+ "Banner-AudioQualityMonitor"
+ "Voice Call"
+ "audioQuality banner click result %d"
+ "audioQuality banner user click"
+ "audioQuality: Type %s, Name %@, Addr %@,  Timeout %.3f"
```
