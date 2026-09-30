## chassisplatformhostd

> `/usr/libexec/chassisplatformhostd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__objc_methname`
- `__TEXT.__objc_classname`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-60.0.0.0.0
-  __TEXT.__text: 0x7e48cc
-  __TEXT.__auth_stubs: 0x73d0
+61.0.0.0.0
+  __TEXT.__text: 0x7e2e40
+  __TEXT.__auth_stubs: 0x73c0
   __TEXT.__objc_stubs: 0x600
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x49ce2
+  __TEXT.__const: 0x49d42
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift_as_entry: 0x27c0
-  __TEXT.__swift_as_ret: 0x3694
-  __TEXT.__cstring: 0x12473
+  __TEXT.__swift_as_entry: 0x27d8
+  __TEXT.__swift_as_ret: 0x36b0
+  __TEXT.__cstring: 0x12433
   __TEXT.__objc_methname: 0x2ffa
   __TEXT.__objc_methtype: 0xe5
   __TEXT.__objc_classname: 0x229e
-  __TEXT.__constg_swiftt: 0x14554
-  __TEXT.__swift5_typeref: 0x15da8
-  __TEXT.__swift5_reflstr: 0x13412
-  __TEXT.__swift5_fieldmd: 0x13f4c
-  __TEXT.__oslogstring: 0x10b2e
-  __TEXT.__swift5_capture: 0xf5ac
+  __TEXT.__constg_swiftt: 0x14540
+  __TEXT.__swift5_typeref: 0x15de8
+  __TEXT.__swift5_reflstr: 0x133a2
+  __TEXT.__swift5_fieldmd: 0x13eec
+  __TEXT.__oslogstring: 0x10d6e
+  __TEXT.__swift5_capture: 0xf56c
   __TEXT.__swift5_proto: 0x2770
   __TEXT.__swift5_types: 0x16d0
-  __TEXT.__swift_as_cont: 0x6ba4
+  __TEXT.__swift_as_cont: 0x6be4
   __TEXT.__swift5_assocty: 0x44e8
   __TEXT.__swift5_acfuncs: 0xf3c
   __TEXT.__swift5_builtin: 0xce4

   __TEXT.__swift5_types2: 0x4
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__unwind_info: 0x29cb8
-  __TEXT.__eh_frame: 0x67b48
-  __DATA_CONST.__const: 0x40b08
+  __TEXT.__unwind_info: 0x29938
+  __TEXT.__eh_frame: 0x67d88
+  __DATA_CONST.__const: 0x40a88
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__auth_got: 0x39f8
+  __DATA_CONST.__auth_got: 0x39f0
   __DATA_CONST.__got: 0x21d8
-  __DATA_CONST.__auth_ptr: 0xc570
+  __DATA_CONST.__auth_ptr: 0xc588
   __DATA.__objc_const: 0xcdf0
   __DATA.__objc_selrefs: 0x238
   __DATA.__objc_data: 0x1130
-  __DATA.__data: 0x24a88
+  __DATA.__data: 0x24a08
   __DATA.__common: 0xe60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - @rpath/Astris.framework/Astris
-  Functions: 36057
-  Symbols:   3719
-  CStrings:  3886
+  Functions: 36083
+  Symbols:   3718
+  CStrings:  3894
 
Symbols:
- _$s18ChassisPlatformKit7CPKUDIDV9deriveULA8bmcIndex4nodeSSs5UInt8V_ACtFZ
CStrings:
+ "%s SoC is already in DFU, expecting %s to disconnect."
+ "%s cleanup finished"
+ "%s disconnected, cleaning up"
+ "%s downstreamMonitorTask did not exit within %llus, orphaning"
+ "%s ignoring pre-DFU-request restorable device %s, disconnect is expected."
+ "%s pre-DFU-request restorable device %s disappeared."
+ "%s prior downstreamMonitorTask did not exit within %llus, orphaning"
+ "%s setupTask for node %s did not exit within %llus, orphaning"
+ "BMC %s node %s: setupTask did not exit within %llus, orphaning"
+ "Deleting stale proxy RSD route: %s"
+ "No proxy RSD routes found or failed to query routing table: %@"
+ "ProxyRSD monitorBMCConnection finished, should not happen"
+ "^fd[0-9a-f][0-9a-f]:%04x[:/]"
+ "netstat -rn -f inet6 | grep '"
- "BMC %s: disconnected, cleaning up"
- "Deleting stale ULA route: %s"
- "No ULA routes found or failed to query routing table: %@"
- "Timed out determining SoC state."
- "determiningSoCState"
- "netstat -rn -f inet6 | grep '^fd'"
```
