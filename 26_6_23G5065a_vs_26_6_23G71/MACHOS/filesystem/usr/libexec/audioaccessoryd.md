## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

 35.14.0.0.0
-  __TEXT.__text: 0x23fbc0
+  __TEXT.__text: 0x2402a4
   __TEXT.__auth_stubs: 0x2c20
-  __TEXT.__objc_stubs: 0x1d640
+  __TEXT.__objc_stubs: 0x1d660
   __TEXT.__objc_methlist: 0xda8c
   __TEXT.__const: 0x4210
   __TEXT.__gcc_except_tab: 0x5bb0
-  __TEXT.__cstring: 0x53893
+  __TEXT.__cstring: 0x53a63
   __TEXT.__objc_classname: 0xff3
   __TEXT.__objc_methname: 0x2a455
   __TEXT.__objc_methtype: 0x3e59

   __TEXT.__swift5_capture: 0x1a28
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6cb8
+  __TEXT.__unwind_info: 0x6cc8
   __TEXT.__eh_frame: 0x1ca0
   __DATA_CONST.__auth_got: 0x1620
   __DATA_CONST.__got: 0xd60
   __DATA_CONST.__auth_ptr: 0x580
   __DATA_CONST.__const: 0xb9a0
-  __DATA_CONST.__cfstring: 0xb320
+  __DATA_CONST.__cfstring: 0xb3e0
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x170

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11047
+  Functions: 11055
   Symbols:   1283
-  CStrings:  15452
+  CStrings:  15466
 
CStrings:
+ "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
+ "-[BTServicesDaemon openRadarforAudioQuality]"
+ "1551854"
+ "815886"
+ "Bluetooth Audio Quality Feedback"
+ "CoreBluetooth - HFP Audio | iOS"
+ "Keywords"
+ "Performance"
+ "audioQuality - File Radar"
+ "audioQuality banner timeout"
+ "audioQuality user click, openradar"
+ "audioQuality user dismiss"
+ "audioQuality: banner action: %s, %{error}"
+ "audioQuality: banner error for device %@"
```
