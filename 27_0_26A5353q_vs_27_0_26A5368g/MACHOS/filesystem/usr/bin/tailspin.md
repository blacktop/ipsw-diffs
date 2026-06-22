## tailspin

> `/usr/bin/tailspin`

```diff

-261.0.0.0.0
-  __TEXT.__text: 0x90c8 sha256:217c50da35feae27cdf2240ccb062851806cb81f8697ab61a82a1d899f464f57
-  __TEXT.__auth_stubs: 0x7f0 sha256:f9f9b024b76f7098100c9e80bce1ae654afa2b79b498dbd8a2e3949f24a3b5fa
-  __TEXT.__objc_stubs: 0x900 sha256:b2cd7aa92f2db34bf1ffbcb555099eb7a203a6a1504edf926e5067a972a4c17a
-  __TEXT.__const: 0x78 sha256:1269e9a651d0f8f26bd4da3ff14001c03e2ef502a62239257427146423d28abe
-  __TEXT.__gcc_except_tab: 0x2d8 sha256:3d2965efb036a4822cf2a24b6741283947bb1fd573e66d7a6356ccdc8d0dabf4
-  __TEXT.__cstring: 0x3340 sha256:24bf96e95768a7d8210faed4ee5ac9f93b8583f1c7d61d3e828639876caf4f68
+265.0.0.0.0
+  __TEXT.__text: 0x92dc sha256:ffb818eb7ddc1100763149d3e36527aefd25ecb24ac31b139ca1aa920e09019d
+  __TEXT.__auth_stubs: 0x7f0 sha256:f17af6525f6db5bacd6e9e90db566adea564569aaca172d00ae2dd206e9f3793
+  __TEXT.__objc_stubs: 0x940 sha256:87bd5c3ba313d895ce854c2f2b8727c77615e8b81dd8de48f6bc912af78cb1dd
+  __TEXT.__const: 0x78 sha256:9af95b6c782896ea9be14ecf21f83ce62b5e0dbd298f3fe5763ef5c926db293b
+  __TEXT.__gcc_except_tab: 0x2d8 sha256:263f912e6ef62e4f39d25211993113d3b3beb4775ae8dccf4b293d760d995e73
+  __TEXT.__cstring: 0x3508 sha256:78bdccd02a8da18690e905ac00b9cf43302010f1193faabfb113dba48f6c65d3
   __TEXT.__oslogstring: 0x55 sha256:b3ba3492df898d18f77f1ffdaa679341d1ba6dec6009856843452965c010ba41
-  __TEXT.__objc_methname: 0x5aa sha256:7c84cbf803c18a21563ae564182ca25691cb36699b89c47dfcceb24a5b630216
-  __TEXT.__unwind_info: 0x350 sha256:34d79122a7e8f5cdf63ccb2dc1e5af949e7bde5ec4992db94dc9c9ead1583927
-  __DATA_CONST.__const: 0x768 sha256:3a2f71c30904614ad59687fa456dfb93ffe96b13985292c50bb86cff58666ed6
-  __DATA_CONST.__cfstring: 0x660 sha256:71db3e8d28fa694a1c269df0b26a9124fc5ac7097a7318f565579ff60ce93d81
+  __TEXT.__objc_methname: 0x5cb sha256:8a53f5c9b442e6ac89fcb2ae82cfafe4ed20cfa633877c650a5aa8138acf0d84
+  __TEXT.__unwind_info: 0x350 sha256:5f9f2d6d67b7b6a05c9ebff04917074541e0fd411902301f5618f0c4300af6a7
+  __DATA_CONST.__const: 0x788 sha256:967931defd22de80dde8c1d0605d65283c5ba8980b54ee4f856577ddcdfc3aa8
+  __DATA_CONST.__cfstring: 0x6a0 sha256:af2b4df84e3a5ad57f8e489a692a349fac1fbaeb807a3d8f896e2735ec6db1df
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__auth_got: 0x408 sha256:555ed6de1573672b7cd756491dea52750b31808a1fd43b0437f0361b8e67522d
-  __DATA_CONST.__got: 0x150 sha256:c43ffa25b4147d7a8ce4dbbc113e5bb3339fb79c94b568626a82e974771cfc2a
-  __DATA_CONST.__auth_ptr: 0x10 sha256:cdf7058e369eea6dd8150a218714836f076a4e70fb5b9d1da667404423daddfa
-  __DATA.__objc_selrefs: 0x240 sha256:65b3cf6e5e63f4f7294b46ea54a6255c869e79cb51ae40a18101aecedc1cdd65
+  __DATA_CONST.__got: 0x158 sha256:718321908d52865003447c934b1f9a06c8ba1d454ca7d1551bfd9061cb384d43
+  __DATA_CONST.__auth_ptr: 0x10 sha256:fd9026d8b9fe13de92e227e8c479c9f7520f3a80df67536023353fc777975bcb
+  __DATA.__objc_selrefs: 0x250 sha256:bb09b93560cb3bf12026440bca949f533ac7de1adb226d2a0b9f75846ae2a3c0
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
   __DATA.__bss: 0x510 sha256:94637c6efefbdcc3d3bb74d61732b22250552654c8c11f0fa9c3b3ed11d38373
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: A634F6EA-C7E6-32F1-9650-3086282F4ADB
-  Functions: 154
-  Symbols:   176
-  CStrings:  390
+  UUID: C3198EE4-A2CE-3B98-8644-2E8433967BBD
+  Functions: 156
+  Symbols:   177
+  CStrings:  402
 
Symbols:
+ _TSPDumpOptions_OSSignpostLogSubsystemCategories
CStrings:
+ "\t\t                                            given subsystem and category. Repeatable. Use '*' or omit the category\n"
+ "\t\t                                            to match all categories under the subsystem.\n"
+ "\t\t    --filter-subsystem-category sub[:cat]   When gathering os_logs/os_signposts, restrict to entries matching the\n"
+ "*"
+ ":"
+ "Empty --filter-subsystem-category value\n"
+ "Empty subsystem in --filter-subsystem-category value: %s\n"
+ "filter-subsystem-category"
+ "rangeOfString:"
+ "substringToIndex:"

```
