## CarCommandsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin`

```diff

-3405.3.1.0.0
-  __TEXT.__text: 0x151a48
+3405.5.1.0.0
+  __TEXT.__text: 0x1512fc
   __TEXT.__auth_stubs: 0x3430
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0xd70
   __TEXT.__const: 0xb484
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__objc_methname: 0x242e
-  __TEXT.__cstring: 0x126dd
+  __TEXT.__cstring: 0x1278d
   __TEXT.__oslogstring: 0x84f
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x99a
-  __TEXT.__constg_swiftt: 0x7070
+  __TEXT.__constg_swiftt: 0x7078
   __TEXT.__swift5_typeref: 0x4780
   __TEXT.__swift5_fieldmd: 0x3bac
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift_as_ret: 0x1264
   __TEXT.__swift5_capture: 0x5bc
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x6ed0
-  __TEXT.__eh_frame: 0x13d58
+  __TEXT.__unwind_info: 0x6ec0
+  __TEXT.__eh_frame: 0x13ce8
   __DATA_CONST.__auth_got: 0x1a28
   __DATA_CONST.__got: 0xb28
-  __DATA_CONST.__auth_ptr: 0x1a70
-  __DATA_CONST.__const: 0xa920
+  __DATA_CONST.__auth_ptr: 0x1ec0
+  __DATA_CONST.__const: 0xa928
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0x188

   __DATA.__objc_selrefs: 0xcd8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x21f0
-  __DATA.__data: 0xc4e8
+  __DATA.__data: 0xc4e0
   __DATA.__common: 0x448
   __DATA.__bss: 0xd400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8804
+  Functions: 8800
   Symbols:   346
-  CStrings:  2013
+  CStrings:  2014
 
CStrings:
+ "Sync mode is enabled. Checking for special cases"
+ "User requested change for all climate zones. Only setting the driver zone since sync is enabled"
+ "User requested to set passenger temperature when sync is on. Disabling sync mode and setting passenger temperature"
+ "climateZonesToModifyForCurrentSyncMode(intent:climateService:)"
- "Sync is off. Modifying all zones"
- "Sync is on. Only modifying driver's zone. Sync zone info: "
- "climateZonesForCurrentSyncMode(intent:climateService:)"

```
