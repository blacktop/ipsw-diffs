## wifivelocityd

> `/usr/libexec/wifivelocityd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1190.20.0.0.0
-  __TEXT.__text: 0x9913c
+  __TEXT.__text: 0x984d0
   __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_stubs: 0xd1c0
-  __TEXT.__objc_methlist: 0x53e4
+  __TEXT.__objc_stubs: 0xd200
+  __TEXT.__objc_methlist: 0x53d4
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__const: 0x3c0
-  __TEXT.__gcc_except_tab: 0x1874
-  __TEXT.__objc_methname: 0xddbb
-  __TEXT.__oslogstring: 0xb506
-  __TEXT.__cstring: 0xc5a6
+  __TEXT.__gcc_except_tab: 0x18a0
+  __TEXT.__objc_methname: 0xddb0
+  __TEXT.__oslogstring: 0xb560
+  __TEXT.__cstring: 0xc562
   __TEXT.__objc_classname: 0x7fa
   __TEXT.__objc_methtype: 0x23f7
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x2170
+  __TEXT.__unwind_info: 0x2130
   __DATA_CONST.__const: 0x2968
-  __DATA_CONST.__cfstring: 0xaf40
+  __DATA_CONST.__cfstring: 0xaea0
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_intobj: 0xeb8
-  __DATA_CONST.__objc_arraydata: 0x23b0
+  __DATA_CONST.__objc_arraydata: 0x23a0
   __DATA_CONST.__objc_dictobj: 0x14f0
-  __DATA_CONST.__objc_arrayobj: 0x1500
+  __DATA_CONST.__objc_arrayobj: 0x14d0
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__auth_got: 0x9e8
-  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x8ba0
-  __DATA.__objc_selrefs: 0x3aa8
-  __DATA.__objc_ivar: 0x6e4
+  __DATA.__objc_const: 0x8b30
+  __DATA.__objc_selrefs: 0x3ab0
+  __DATA.__objc_ivar: 0x6d8
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  Functions: 2367
-  Symbols:   504
-  CStrings:  5281
+  Functions: 2350
+  Symbols:   505
+  CStrings:  5275
 
Symbols:
+ _OBJC_CLASS_$_CWFSensingParameters
CStrings:
+ "-[W5PeerSensingListener performSensing:error:]"
+ "[wifivelocity] %s (%s:%u) Performing sensing with parameters='%{public}@'"
+ "[wifivelocity] %s (%s:%u) corewifi perform sensing for network='%{public}@'"
+ "configureSensingWithParameters:reply:"
+ "localizedDescription"
+ "performSensing:error:"
+ "setSensingEnabled:error:"
- "-dbg=print_nan_avail"
- "-nan"
- "-nan_peers"
- "Filtered known networks for customer install without MegaWiFi profile\n"
- "T@\"W5WiFiInterface\",R,&,V_nan"
- "[wifivelocity] %s (%s:%u) sensing is not supported on macOS"
- "__startNANPerfLogging"
- "__startNANQueryTimer"
- "_nan"
- "_nanQueryFileHandle"
- "_nanQueryTimer"
- "nan"
- "nan_%@"
```
