## IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

```diff

-399.27.7.0.0
-  __TEXT.__text: 0x967c
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__cstring: 0x22cd
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__const: 0x2e60
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__auth_got: 0x4e8
+524.7.0.0.0
+  __TEXT.__text: 0x9a3c
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__cstring: 0x24ba
+  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__const: 0x3250
+  __TEXT.__unwind_info: 0x2d0
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x258

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4B6E5891-1499-3FC1-900A-C659F67F31DE
-  Functions: 203
-  Symbols:   178
-  CStrings:  409
+  UUID: 45003AAD-5CFA-3D1E-8B6A-E6B61CE8A131
+  Functions: 206
+  Symbols:   179
+  CStrings:  425
 
Symbols:
+ _strcmp
CStrings:
+ "%s: file read failed"
+ "%s: get_big_block_buf failed, no memory "
+ ".tbics_gain_map"
+ "Failed to read 'TBIC' EAN"
+ "Failed to upload TBICS Gain Map"
+ "Known commands: init, epoch"
+ "TBICS BIC"
+ "TBICS Gain Map not saved to EAN"
+ "TBICS Gain Map saved to file system"
+ "TBICS Gain Map was not saved to File system. Error in fs.close()"
+ "TBICS Gain Map was not saved to File system. Error in fs.write()"
+ "epoch"
+ "init"
+ "only one command allowed"
+ "tbics_gain_map"
+ "upload_tbics_gain_map"
+ "upload_tbics_gain_map: reading from filesystem failed. Trying EAN"
- "TBICS BIC %ssaved"

```
