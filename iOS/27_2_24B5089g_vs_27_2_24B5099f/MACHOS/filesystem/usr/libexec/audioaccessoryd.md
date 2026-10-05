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
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-41.4.0.0.0
-  __TEXT.__text: 0x25086c
+41.6.0.0.0
+  __TEXT.__text: 0x25077c
   __TEXT.__auth_stubs: 0x3c80
   __TEXT.__objc_stubs: 0x1f3e0
   __TEXT.__objc_methlist: 0xe9dc
   __TEXT.__const: 0x4da0
   __TEXT.__gcc_except_tab: 0x5a3c
-  __TEXT.__cstring: 0x59113
+  __TEXT.__cstring: 0x59133
   __TEXT.__objc_classname: 0x1193
   __TEXT.__objc_methname: 0x2d555
   __TEXT.__objc_methtype: 0x42e2

   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__unwind_info: 0x9780
-  __TEXT.__eh_frame: 0x2d90
+  __TEXT.__eh_frame: 0x2db8
   __DATA_CONST.__const: 0xce80
   __DATA_CONST.__cfstring: 0xbaa0
   __DATA_CONST.__objc_classlist: 0x3e0

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__auth_got: 0x1e50
-  __DATA_CONST.__got: 0x1160
+  __DATA_CONST.__got: 0x1158
   __DATA_CONST.__auth_ptr: 0x7c0
   __DATA.__objc_const: 0x20490
   __DATA.__objc_selrefs: 0x9348
   __DATA.__objc_ivar: 0x18a0
   __DATA.__objc_data: 0x36d8
-  __DATA.__data: 0x59e0
+  __DATA.__data: 0x59c0
   __DATA.__common: 0x3a8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 12109
-  Symbols:   1708
+  Symbols:   1707
   CStrings:  16414
 
Symbols:
+ _$s10Foundation4DateV2geoiySbAC_ACtFZ
- _$s10Foundation4DateVSLAAMc
- _$sSL2geoiySbx_xtFZTj
Functions:
~ sub_1001dc538 : 26272 -> 25968
~ sub_1001f581c -> sub_1001f56ec : 7524 -> 7544
~ sub_10020446c -> sub_100204350 : 144 -> 148
~ sub_1002044fc -> sub_1002043e4 : 148 -> 152
~ sub_1002212ac -> sub_100221198 : 32 -> 68
CStrings:
+ "Head gestures were unexpectedly disabled on %@? Please file a radar and attach ALL nearby devices' sysdiagnoses."
- "Head gestures were unexpectedly disabled on %@? Please file a radar."
```
