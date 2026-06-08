## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1413.100.6.0.0
-  __TEXT.__text: 0x17638 sha256:64cb0780bad364de43df443de998efc43f0fab9e72ab913a45d64f5b74b80d89
-  __TEXT.__auth_stubs: 0xdd0 sha256:d20a2a7a578c89e8c5728aefb03526dd53d21ddbdd2532ff8402e5954a798587
+1430.0.0.0.0
+  __TEXT.__text: 0x16d4c sha256:9f4505449e32b7a30b7110b1b4fa45700aee8c38ca88ab996bd036bde9d5209d
+  __TEXT.__auth_stubs: 0xdd0 sha256:e8740a7bff802a0b8c591d3da0344b3dd980861e2efa3570b6060c75498e9aac
   __TEXT.__cstring: 0xee0 sha256:e8437360200cf2a77ad9f4de697215f8d7413a9ee4bb5619a1b3395c906199bd
-  __TEXT.__const: 0x158 sha256:954359400b5015d5577fc744c7294372c661e1e69a3a0d353c0f30803e75ae30
-  __TEXT.__oslogstring: 0x31a7 sha256:40b8e73680b101e86c34be9fe18493c5e890d5c2f331e401dc971578b1e922b8
-  __TEXT.__unwind_info: 0x380 sha256:2e995a2cc48873731bd28c1990e805fdddcaac158d040baf771d574dc03e989e
-  __DATA_CONST.__auth_got: 0x6e8 sha256:00a5f4c1b5dfb9897f7cb7e000d3b7d63640ea50d358ff9dbd820efefe5d0326
-  __DATA_CONST.__got: 0xb0 sha256:9191eba7ba67b3d80bfa623cfa0a9414b42c5e43395399d29a1e479ff8cd703e
-  __DATA_CONST.__auth_ptr: 0x10 sha256:ddb148085de9d6b1372243aa43eea9e1256a15bf4ed0107164153d0e6d97faff
-  __DATA_CONST.__const: 0x318 sha256:840c4a2b4f9080f77daad9e998b695bdee041553c194a338007a9749ee5e9640
-  __DATA_CONST.__cfstring: 0x4c0 sha256:960af82c709db12830294ed0e9a1576814c3ac6770372ff64c999ab592f5f0a9
-  __DATA.__data: 0x232 sha256:aa50a5a7dc5d30ac2ea0f43308eda0710c5ce2bee611f51a1d5ed7af2c9c622f
+  __TEXT.__const: 0x168 sha256:7fab7237a9d7113466155bfba6da9439488a5fd52b95e7fe719f86415a32e2b3
+  __TEXT.__oslogstring: 0x326a sha256:24331cc343a08959c6b5da1fd581532aa672dfe07d69e20bae0301f80f35e87e
+  __TEXT.__unwind_info: 0x360 sha256:1c0d456ff81cecc025940f220ca885b3c38a09e2a15176e043bedd45045cef5c
+  __DATA_CONST.__const: 0x318 sha256:786c094f7dca8883d052518de7a4a9ad310e2e8b0eed7293830cfcbadfaa1161
+  __DATA_CONST.__cfstring: 0x4c0 sha256:e145f3f47934d57d8f13a16769b3b13eaffc86ca9100d98899ec6633c71068f8
+  __DATA_CONST.__auth_got: 0x6e8 sha256:c6c42b78eebeeb22e3b8bebe565b430451e07feb8f776adce31c64f82aa1454a
+  __DATA_CONST.__got: 0xb0 sha256:ae0ce8828ea0fc3ca4a72101b6c08fe84da86c14523b78376e2a96f18ea75e6c
+  __DATA_CONST.__auth_ptr: 0x10 sha256:8e34988fb0c3b8615e539ab7cbfa9bb88c39b1dabf302eeeb044d60b7ee0a34d
+  __DATA.__data: 0x232 sha256:78ae879b2e1d05e19ceead087e04ea9c5154933a1d78bbf73587c7ce1f83fdf7
   __DATA.__bss: 0x468 sha256:3731b0a75ab19d96b774da62d37eccacd517c6593af20aa66525dc0b951cdba9
   __DATA.__common: 0x2248 sha256:96debd282ce8291efca7334f08d2056f3a4f5ab0f0db3510b46d6feafd0a14bc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6B35C9AA-9EBF-3C07-BB9E-CFB680E1069C
-  Functions: 402
+  UUID: 45BFB51F-3742-386F-A8EA-7F39263C07A2
+  Functions: 392
   Symbols:   247
-  CStrings:  506
+  CStrings:  508
 
CStrings:
+ "%s: new checksum mis-match: file 0x%.8x, calculated 0x%.8x in index %d"
+ "get_last_event_id: new checksum mis-match: file 0x%.8x, calculated 0x%.8x in file %s"
+ "get_last_event_id: old checksum mis-match: file 0x%.8x, calculated 0x%.8x in file %s"
+ "process_disk_event_buf: magic is wrong (0x%.8x != (0x%.8x <OR> 0x%.8x <OR> 0x%.8x)) - buflen(%d) index(%d) dev(%d)"
+ "process_disk_event_buf: old checksum mis-match: file 0x%.8x, calculated 0x%.8x"
- "get_last_event_id: checksum mis-match: file 0x%.8x, calculated 0x%.8x in file %s"
- "process_disk_event_buf: checksum mis-match: file 0x%.8x, calculated 0x%.8x"
- "process_disk_event_buf: magic is wrong (0x%.8x != (0x%.8x <OR> 0x%.8x <OR> 0x%.8x))"

```
