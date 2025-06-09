## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0x23c14
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_stubs: 0x9a0
+54.0.0.0.0
+  __TEXT.__text: 0x242ac
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0xa00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x30c
-  __TEXT.__gcc_except_tab: 0x2490
+  __TEXT.__objc_methlist: 0x31c
+  __TEXT.__gcc_except_tab: 0x2570
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x563e
+  __TEXT.__cstring: 0x56f6
   __TEXT.__objc_classname: 0x55
-  __TEXT.__objc_methname: 0xb35
-  __TEXT.__objc_methtype: 0x6b3
+  __TEXT.__objc_methname: 0xb71
+  __TEXT.__objc_methtype: 0x657
   __TEXT.__oslogstring: 0x8d2
-  __TEXT.__unwind_info: 0x6d0
-  __DATA_CONST.__auth_got: 0x400
+  __TEXT.__unwind_info: 0x710
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x538
-  __DATA_CONST.__cfstring: 0x39c0
+  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__cfstring: 0x3b00
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x618
-  __DATA.__objc_selrefs: 0x378
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_const: 0x638
+  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4FAD6B02-4780-3F08-94ED-6DA2F378727E
-  Functions: 433
-  Symbols:   402
-  CStrings:  1386
+  UUID: 73EB70B0-476B-3B80-8582-E9807CAA7E97
+  Functions: 439
+  Symbols:   407
+  CStrings:  1410
 
Symbols:
+ __Z18ecPearlStatusCheckv
+ __Z21stringForSensorStatusj
+ __Z38ecDiagnosticStatusCodeFromStatusStringP8NSString
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
- __Znwm
CStrings:
+ "%@ and also exclave detected value %d"
+ "Exclave"
+ "Exclave returne code"
+ "ExclavesStatus: %@"
+ "allowed"
+ "com.apple.sensors.cam_alt_faceid"
+ "control"
+ "denied"
+ "detecting exclave value %@ %d"
+ "getEcStatus"
+ "isEqualToString:"
+ "m_exclaveStatus"
+ "pending"
+ "setDictionary:"
+ "unknown"
+ "{vector<PearlConfiguration, std::allocator<PearlConfiguration>>=\"__begin_\"^{PearlConfiguration}\"__end_\"^{PearlConfiguration}\"__cap_\"^{PearlConfiguration}}"
- "RGB"
- "{vector<PearlConfiguration, std::allocator<PearlConfiguration>>=\"__begin_\"^{PearlConfiguration}\"__end_\"^{PearlConfiguration}\"__end_cap_\"{__compressed_pair<PearlConfiguration *, std::allocator<PearlConfiguration>>=\"__value_\"^{PearlConfiguration}}}"

```
