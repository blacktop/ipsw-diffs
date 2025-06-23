## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-395.3.0.0.0
-  __TEXT.__text: 0x49ad4
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x21d0
-  __TEXT.__gcc_except_tab: 0x88c0
-  __TEXT.__cstring: 0x27d4
+398.101.0.0.0
+  __TEXT.__text: 0x49b2c
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x21b8
+  __TEXT.__gcc_except_tab: 0x88a8
+  __TEXT.__cstring: 0x284f
   __TEXT.__const: 0x21f
-  __TEXT.__oslogstring: 0x357f
-  __TEXT.__unwind_info: 0x2b18
+  __TEXT.__oslogstring: 0x35ea
+  __TEXT.__unwind_info: 0x2b08
   __TEXT.__objc_classname: 0x51b
-  __TEXT.__objc_methname: 0x4f83
+  __TEXT.__objc_methname: 0x4f67
   __TEXT.__objc_methtype: 0x1ec2
   __TEXT.__objc_stubs: 0x2c20
-  __DATA_CONST.__got: 0xaf0
+  __DATA_CONST.__got: 0xae8
   __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1598
+  __DATA_CONST.__objc_selrefs: 0x1588
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x1698
   __AUTH_CONST.__cfstring: 0x20a0
   __AUTH_CONST.__objc_const: 0x2778

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 05B192E9-B543-3378-B152-35990B02CB49
+  UUID: A9ECDA95-3510-3D0C-AAC5-19D80EF5E7FD
   Functions: 1580
-  Symbols:   5601
-  CStrings:  1889
+  Symbols:   5595
+  CStrings:  1894
 
Symbols:
+ GCC_except_table110
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table160
+ GCC_except_table185
+ GCC_except_table206
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table219
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table236
+ GCC_except_table237
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table288
+ GCC_except_table289
+ GCC_except_table294
+ GCC_except_table299
+ GCC_except_table302
+ GCC_except_table307
+ GCC_except_table308
+ GCC_except_table316
+ GCC_except_table324
+ GCC_except_table327
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table369
+ GCC_except_table379
+ GCC_except_table386
+ GCC_except_table389
+ GCC_except_table418
+ GCC_except_table427
+ GCC_except_table478
+ GCC_except_table479
+ GCC_except_table488
+ GCC_except_table489
+ GCC_except_table492
+ _CAAssertRtn
+ __ZN4avas6client21DeviceTimeGlobalState22obtainedNewSharedBlockEiPU24objcproto13OS_xpc_object8NSObject.cold.1
+ __ZN4avas6client21SessionCoreLegacy_iOS39unregisterForAvailableInputOutputChangeEv
+ __ZNK5caulk3ipc13mapped_memory7get_ptrIN4avas13DTSharedBlockEEENSt3__118__add_pointer_implIT_Xoosr25__libcpp_is_referenceableIS7_EE5valuesr7is_voidIS7_EE5valueEE4typeEm.cold.2
- -[AVAudioSession hasVideo]
- -[AVAudioSession setHasVideo:error:]
- GCC_except_table108
- GCC_except_table114
- GCC_except_table131
- GCC_except_table132
- GCC_except_table143
- GCC_except_table158
- GCC_except_table196
- GCC_except_table211
- GCC_except_table212
- GCC_except_table215
- GCC_except_table224
- GCC_except_table225
- GCC_except_table234
- GCC_except_table235
- GCC_except_table240
- GCC_except_table241
- GCC_except_table252
- GCC_except_table255
- GCC_except_table281
- GCC_except_table282
- GCC_except_table286
- GCC_except_table287
- GCC_except_table292
- GCC_except_table295
- GCC_except_table300
- GCC_except_table301
- GCC_except_table304
- GCC_except_table311
- GCC_except_table312
- GCC_except_table318
- GCC_except_table326
- GCC_except_table329
- GCC_except_table364
- GCC_except_table365
- GCC_except_table371
- GCC_except_table381
- GCC_except_table390
- GCC_except_table391
- GCC_except_table420
- GCC_except_table429
- GCC_except_table480
- GCC_except_table481
- GCC_except_table490
- GCC_except_table491
- GCC_except_table494
- __ZNK5caulk3ipc13mapped_memory11get_raw_ptrEm
- __ZNK5caulk3ipc13mapped_memory11get_raw_ptrEm.cold.1
- __os_assert_log
- _kMXSessionProperty_IsPlayingVideoOutput
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "%25s:%-5d Deallocating AudioSession client:0x%x"
+ "%25s:%-5d failed to set preferred input: %@ with an err: %d"
+ "%25s:%-5d pingClient called for session %x"
+ "(in_offset + sizeof(T)) <= size()"
+ "AVAudioSessionCallbackDispatcher.mm"
+ "SessionCore_iOS.h"
+ "in_offset < size()"
+ "mapped_memory.h"
- "%25s:%-5d failed to set preferred input: %@"
- "hasVideo"
- "setHasVideo:error:"

```
