## abmlite

> `/usr/bin/abmlite`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0x19e1c
-  __TEXT.__auth_stubs: 0x760
+1563.0.0.0.0
+  __TEXT.__text: 0x1c3d4
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x560
-  __TEXT.__init_offsets: 0xc
+  __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0x1c24
-  __TEXT.__cstring: 0x92b
+  __TEXT.__const: 0x530
+  __TEXT.__gcc_except_tab: 0x20bc
+  __TEXT.__cstring: 0xa53
   __TEXT.__oslogstring: 0xc6
-  __TEXT.__objc_classname: 0xd
+  __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x14
   __TEXT.__objc_methname: 0x31e
-  __TEXT.__unwind_info: 0x490
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x490
+  __TEXT.__unwind_info: 0x560
+  __DATA_CONST.__const: 0x520
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x2d8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x158
   __DATA.__objc_data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5761791-E970-3269-A580-52FF40BCCFB9
-  Functions: 146
-  Symbols:   323
-  CStrings:  162
+  UUID: 6E4E3F02-51DC-3863-BC32-61BFEA366583
+  Functions: 173
+  Symbols:   356
+  CStrings:  173
 
Symbols:
+ _CFRelease
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN12capabilities5radio6vendorEv
+ __ZN12capabilities5radio7initiumEv
+ __ZN12capabilities5trace23supportsContainerFormatEv
+ __ZN3abm15kCollectIPCLogsE
+ __ZN3abm20kKeyIPCSnapshotQuotaE
+ __ZN3abm26kKeyTraceSettingsPlistDictE
+ __ZN3abm5trace31extractSettingsTypeFromFileNameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN3ctu9cf_to_xpcEPKv
+ __ZN4util23readPlistToCFDictionaryENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN8defaults3ipc22snapshot_total_size_mbEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEm
+ __ZTVN10__cxxabiv123__fundamental_type_infoE
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x27
+ _objc_retain_x8
- __Block_object_assign
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
CStrings:
+ " MB) is below minimum ("
+ " MB). Using minimum."
+ "-*"
+ "IPC log collection: Failed"
+ "IPC log collection: Success"
+ "IPC log collection: Unsupported"
+ "Invalid --quota value: "
+ "Warning: Requested quota ("
+ "[nocompress|tar.gz|tar] [no-split-archive|split-archive] [--quota=XMB] [REASON] collect IPC logs only"
+ "cellular"
+ "log-bundle_"

```
