## spindump

> `/usr/sbin/spindump`

```diff

-383.2.0.0.0
-  __TEXT.__text: 0x96080
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_stubs: 0x3f00
+383.6.0.0.0
+  __TEXT.__text: 0x96674
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_stubs: 0x3f20
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x12964
-  __TEXT.__oslogstring: 0x2199b
+  __TEXT.__cstring: 0x12972
+  __TEXT.__oslogstring: 0x219bb
   __TEXT.__objc_classname: 0xe5
-  __TEXT.__gcc_except_tab: 0x1d3c
-  __TEXT.__objc_methname: 0x40f4
+  __TEXT.__gcc_except_tab: 0x1dd0
+  __TEXT.__objc_methname: 0x4105
   __TEXT.__objc_methtype: 0x52d
-  __TEXT.__unwind_info: 0xba0
-  __DATA_CONST.__auth_got: 0x908
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x13a0
+  __TEXT.__unwind_info: 0xc90
+  __DATA_CONST.__auth_got: 0x900
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x13a8
   __DATA_CONST.__cfstring: 0x89c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x1118
+  __DATA.__objc_selrefs: 0x1120
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1608
-  Symbols:   365
+  Functions: 1602
+  Symbols:   364
   CStrings:  4249
 
Symbols:
- _fmod
CStrings:
+ "Microstackshot statistics:\n%llu bytes parsed (%llu ms, %llu non-ms, %llu invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
+ "Unable to format: Microstackshot statistics:\n%llu bytes parsed (%llu ms, %llu non-ms, %llu invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
+ "bytes_other_data"
- "/"
- "Microstackshot statistics:\n%llu bytes parsed (%llu bytes invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
- "Unable to format: Microstackshot statistics:\n%llu bytes parsed (%llu bytes invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"

```
