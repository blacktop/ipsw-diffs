## sharingd

> `/usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 2131.10.1.2.11
-  __TEXT.__text: 0x6ad4c8
+  __TEXT.__text: 0x6adc6c
   __TEXT.__auth_stubs: 0xb060
-  __TEXT.__objc_stubs: 0x37700
-  __TEXT.__objc_methlist: 0x1e604
-  __TEXT.__cstring: 0x3ede1
-  __TEXT.__objc_methname: 0x4ebe5
+  __TEXT.__objc_stubs: 0x37840
+  __TEXT.__objc_methlist: 0x1e634
+  __TEXT.__cstring: 0x3efd1
+  __TEXT.__objc_methname: 0x4ecd5
   __TEXT.__objc_classname: 0x5af7
-  __TEXT.__objc_methtype: 0xbca2
+  __TEXT.__objc_methtype: 0xbcc2
   __TEXT.__const: 0x15eb8
-  __TEXT.__gcc_except_tab: 0x688c
+  __TEXT.__gcc_except_tab: 0x68a8
   __TEXT.__oslogstring: 0x3d183
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438

   __TEXT.__swift5_capture: 0x51f0
   __TEXT.__swift_as_ret: 0xf5c
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x148a0
+  __TEXT.__unwind_info: 0x148c8
   __TEXT.__eh_frame: 0x2480c
-  __DATA_CONST.__const: 0x1cc98
-  __DATA_CONST.__cfstring: 0x196c0
+  __DATA_CONST.__const: 0x1ccc0
+  __DATA_CONST.__cfstring: 0x19740
   __DATA_CONST.__objc_classlist: 0xe10
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x748

   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__auth_got: 0x5840
-  __DATA_CONST.__got: 0x3a30
+  __DATA_CONST.__got: 0x3a38
   __DATA_CONST.__auth_ptr: 0x4418
-  __DATA.__objc_const: 0x38698
-  __DATA.__objc_selrefs: 0x110e8
-  __DATA.__objc_ivar: 0x293c
+  __DATA.__objc_const: 0x386f8
+  __DATA.__objc_selrefs: 0x11138
+  __DATA.__objc_ivar: 0x2948
   __DATA.__objc_data: 0xa150
   __DATA.__data: 0x14a78
   __DATA.__common: 0x978

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26393
-  Symbols:   5017
-  CStrings:  27556
+  Functions: 26398
+  Symbols:   5018
+  CStrings:  27581
 
Symbols:
+ _OBJC_CLASS_$_CMDeviceStateManager
CStrings:
+ "### Device state no longer supports Handoff, cleaning up notifications\n"
+ "### Device state update error: %@\n"
+ "-[SDProxHandoffAgent _deviceStateEnsureStarted]"
+ "-[SDProxHandoffAgent _deviceStateEnsureStarted]_block_invoke"
+ "-[SDProxHandoffAgent _deviceStateEnsureStopped]"
+ "-[SDProxHandoffAgent _deviceStateUpdate:]"
+ "@\"CMDeviceStateManager\""
+ "Device state monitor start\n"
+ "Device state monitor stop\n"
+ "Device state supported: %s -> %s\n"
+ "_deviceStateEnsureStarted"
+ "_deviceStateEnsureStopped"
+ "_deviceStateMonitor"
+ "_deviceStateMonitorStarted"
+ "_deviceStateShouldStart"
+ "_deviceStateSupported"
+ "_deviceStateUpdate:"
+ "b518"
+ "b868e"
+ "b868m"
+ "com.apple.SharingServices.SDProxHandoffAgent"
+ "propertyB"
+ "startUpdatesToQueue:withHandler:"
+ "stopUpdates"
+ "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
```
