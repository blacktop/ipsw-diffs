## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 41.7.0.0.0
-  __TEXT.__text: 0x2508fc
+  __TEXT.__text: 0x250fec
   __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__objc_stubs: 0x1f420
+  __TEXT.__objc_stubs: 0x1f440
   __TEXT.__objc_methlist: 0xea04
   __TEXT.__const: 0x4da0
   __TEXT.__gcc_except_tab: 0x5a3c
-  __TEXT.__cstring: 0x59153
+  __TEXT.__cstring: 0x59333
   __TEXT.__objc_classname: 0x1193
   __TEXT.__objc_methname: 0x2d595
   __TEXT.__objc_methtype: 0x42e2

   __TEXT.__swift_as_cont: 0xe8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x9788
+  __TEXT.__unwind_info: 0x9798
   __TEXT.__eh_frame: 0x2db8
   __DATA_CONST.__const: 0xce90
-  __DATA_CONST.__cfstring: 0xbac0
+  __DATA_CONST.__cfstring: 0xbba0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12112
+  Functions: 12102
   Symbols:   1707
-  CStrings:  16419
+  CStrings:  16434
 
CStrings:
+ "%@-Seed-mov"
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
